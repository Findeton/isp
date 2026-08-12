# LOR (paper-30) — K3 INSTRUMENT: the era audit

**Seat** K3 INSTRUMENT (seal, coverage, injections, CLI, #91 at its own hands;
the seam ruling). **Protocol** v14 ledger #253 row K3 (#257: launch delayed,
protocol unchanged). **Era** post-engraving-native. **Interpreter**
`/opt/homebrew/bin/python3.13`. Every execution below ran OUTSIDE the repo, in
off-tree git-less mirrors under the reviewer's scratch; the repo's LOR objects
were read-only throughout; git was read-only.

**THE OBJECT — hashed at start and again at close, unchanged**

| artifact | sha256-12 (start) | sha256-12 (close) |
|---|---|---|
| `v14/paper-30-lor.md` | `f3e9e9df2c70` | `f3e9e9df2c70` |
| `v14/code/lor_exact.py` | `878e6007b785` | `878e6007b785` |
| `v14/code/lor_output.txt` | `427a5da397aa` | `427a5da397aa` |
| `v14/code/lor_receipt.json` | `8b4ca74d954c` | `8b4ca74d954c` |
| `v14/note-lor-pin.md` (pin) | `5239c4671f1a` | `5239c4671f1a` |

Siblings disclaimed: the tree carried unrelated uncommitted work (`smu_*`,
`perr_*`, `sig_*`, papers 24/27/29, `note-paper23-correction`) before and after
this review; none was read as input and none was touched.

---

## GRADE: AWF — accept with fixes

**No measured quantity is wrong.** Every physics number I recomputed
independently reproduced exactly; the four verdict segments rebuild from the
serialized receipt; and the delivery run reproduces the committed artifacts
BYTE-IDENTICALLY off-tree and git-less under two hash seeds. The falsifier
layer is honest at all three E-23 legs, the anchors carry no phantom
consumers, and the seal manifest is total.

**But the paper layer does not hold what the paper says it holds.** Of 32
injections, 17 survived at exit 0 — two benign, **fifteen carrying a real
defect**, including three banned readings written into the paper, four false
table rows, a false measured number, a false declared window, and a corrupted
transcript promoted to disk. Three published counts are false. One gate is
positionally vacuous against its own statement, and one waived gate's
machine-readable forcing is untrue.

Every repair below is a few lines against machinery that already exists.
Nothing needs re-measuring.

---

## 1. What was run

| battery | executions | result |
|---|---|---|
| delivery run, off-tree + git-less, `PYTHONHASHSEED=0` | 1 | exit 0, artifacts **byte-identical** to `427a5da397aa` / `8b4ca74d954c` |
| delivery run, second mirror, `PYTHONHASHSEED=31337` | 1 | exit 0, **byte-identical again** — byte x2 across seeds discharged |
| `--verify-paper` on the pristine paper | 1 | exit 0, clean (the baseline for every injection) |
| paper injections (object under test) | 26 | 11 died at their predicted gates, **15 survived at exit 0** |
| code injections (the instrument itself) | 7 | 4 died, **2 survived at exit 0** |
| the 41-mutant sweep OUTSIDE the harness, one process each | 41 | see §4 — **41/41 ON TARGET** |
| CLI hostile argv + the two registries | 14 | 12/12 rejections exit 2; registries exit 0 |
| `--selftest`, whole-tree hash before and after | 1 | exit 1 at `G-PROVENANCE`; **tree hash identical** |
| `--verify-paper` on a foreign paper (`paper-29-perr.md`) | 1 | exit 1, DRIFT — no false "clean" |
| bare copy (code alone, no sources), plain and `--selftest` | 2 | exit 1, `[CLI] missing source: ...`, **nothing written** |

**95 executions completed. 258 recomputations** independent of the unit's
code: seal and gate accounting (10), anchors (13), the numeral sweep (11), the
substrate and census (23), the refined arena (14), the ladder (24), the cut
(4), the paper's table map (16), the falsifier census's three legs at 41
mutants plus 15 verbatim hook-versus-description comparisons (138), byte and
tree hashes (5).

---

## 2. MAJOR findings

### MAJOR-1 — the three reading-walls never scan the object under test

`G-WALL-BHS`, `G-WALL-KR` and `G-WALL-COSMO` all scan `surface`, built at
`lor_exact.py:2632-2635` from `MEASURED_KEYS` plus the gate statements and
evidence. `paper_text` is never added to it. Only `G-WALL-L1` scans the paper;
`G-WALL-COSMO` touches the paper only to confirm the description stamp is
present.

Demonstrated — three papers, each carrying an explicit banned reading, pass at
exit 0:

- INJ11 `Read cosmologically: the universe expands as the record refines and new space is created by the process.`
- INJ12 `The sprinkling here is Lorentz invariant at this arena.`
- INJ12b `The Myrheim-Meyer dimension estimate of this record is 2 and no height control is taken.`

The pin's wall ("NO cosmological reading") and §12's non-claim ("No
cosmological or expansion reading of the place-count growth") are constraints
on the paper; a falsifier that writes into the receipt surface cannot
discharge them. §9's own wording is internally honest — "this run's DECLARED
MEASUREMENT SURFACE — every measured receipt key together with the statement
and evidence of every gate" — which is precisely why the gap is invisible to a
reader: the wall is real, and it points somewhere else.

**R-K3-1.** `surface = surface + " " + (paper_text or "")` before the three
scans (guarding the `paper_text is None` path as `G-WALL-COSMO` already does),
and re-point the three declared falsifiers at `ptxt` rather than at `surface`,
so the paper leg is what is falsified. `G-WALL-L1` is the pattern to copy.

### MAJOR-2 — 27 of the paper's 40 table data rows are not rendered as claims

`paper_tables()` renders 13 rows: the four of the §4.3 new-places table and the
nine of the §6.4 completion census. The paper carries six tables:

| table | data rows | rendered |
|---|---|---|
| §2 the declared arena (§15) | 6 | 0 |
| §4.1 the three laws at R = 4 / R = 6 | 3 | 0 |
| §4.3 the new places | 4 | **4** |
| §6.4 the completion census | 9 | **9** |
| §7 the arena theorem's ladder | 5 | 0 |
| §10 the choice inventory | 13 | 0 |

Demonstrated, all at exit 0:

- **INJ02** — the ladder's **ceiling** column swapped between m = 3 and m = 4,
  so the paper's own arena theorem asserts ceiling 2 at R = 9 and 1 at R = 12.
- **INJ02b** — the ladder's **places** column swapped between m = 4 and m = 8.
- **INJ04** — paper-04's row in §4.1 swapped between the R = 4 and R = 6
  columns, so the table says the dyadic move is *empty at R = 6* while §4's
  rendered prose says it subdivides 27 of 27.
- **INJ05** — the §2 provenance row reading `26 (path, value) anchors; 31
  verbatim anchors` (both false; both numerals backed).

The two rendered tables behave correctly: INJ01b (values cross-swapped between
the sites and intervals rows) and INJ03 (one census class count 324 -> 144)
both die at `G-PAPER-TABLES`. Row *reordering* inside a rendered table is not
caught (INJ01a, INJ20) because the gate is containment per row — benign here,
since every row is self-labelled, but worth knowing.

The ladder is the cheapest and highest-stakes fix: the rows already exist in
the receipt at `R["ceiling"]["ladder"]` (8 rows: `m`, `R`, `ceiling`,
`refined_L`, `places`, `L_equals_R`). The §10 choice inventory has **no receipt
cells at all** — the RSQ standard's own instrument, and the "one genuinely free
item" claim resting on it, is unrendered prose.

**R-K3-2.** Extend `paper_tables()` with (a) the five ladder rows from
`R["ceiling"]["ladder"]`, (b) the three §4.1 law rows from `R["laws"]`, (c) the
§2 provenance row from `len(SOURCES)/len(PATH_ANCHORS)/len(VERBATIM)`; publish
a `choice_inventory` receipt key (item, class, fiber, binding) and render (d)
its thirteen rows. One mutant per new table.

### MAJOR-3 — three published counts are false

| published | value | truth | cause |
|---|---|---|---|
| `totals.seals` | **37** | 36 | `"seals": len(SEAL.rows) + 4` (line 3756), taken when 3 seals remain |
| `counts.gates` | **41** | 53 | `"gates": len(LD.rows) + 1` (line 2830) |
| `G-ANCHORS-READ`'s statement and paper §14: "31 rows are read out of **five** committed receipts" | five | **six** | typed word (line 1330; paper line 591) |

The first is contradicted inside its own file: `seal_manifest.rows` has 36
entries, `SEALED_PATHS` has 36, and `G-SEAL-COMPLETE`'s own evidence reads
"seals taken 36, declared 36". The second collides with `counts.mutants = 41`
and is contradicted by `coverage.gates_evaluated = 53` and `totals.gates = 53`
in the same object. The third: the path anchors are read from six receipts —
A-P21REC 13, A-P04REC 6, A-P06REC 6, A-P19REC 3, A-I7 2, A-P09REC 1 = 31.

No gate compares any of the three against its own data. All three are typed
offsets or literals against "counts computed, never typed", and all three are
sealed and vouched.

**R-K3-3.** `"seals": len(SEALED_PATHS)`; take the gate figure from
`len(GATE_REGISTRY)` (already forced equal to the evaluated set by
`G-COVERAGE`); `"%d rows are read out of %d committed receipts" %
(len(PATH_ANCHORS), len({a[0] for a in PATH_ANCHORS}))` in both the gate
statement and §14; add a `G-TOTALS-COMPUTED` gate holding every published total
against its own registry length, with a mutant.

### MAJOR-4 — `G-READS-DECLARED` is positionally vacuous against its own statement

The statement: *"a read of mutable repository state cannot be added without
failing here."* The live evidence: **`categories ['SOURCE'], source reads 19 of
19 declared`**.

The disclosed read-registry fix clears `READS_BY_CATEGORY` at `full_run` entry
(line 1228) — correct and necessary. Two consequences it did not close:

1. the object-under-test read is made in `main` (lines 3986/3996/4009), i.e.
   *before* `full_run` runs, so the clear erases it; `OBJECT-UNDER-TEST` never
   reaches the gate;
2. the gate fires second, at line 1267, before `read_text(SELF, "SELF")` (line
   1278) and before every later read. Its scope is the 19 source reads and
   nothing else.

Demonstrated — **CINJ01**: `read_text(os.path.join(REPO, "v14/LOG.md"),
"SOURCE")` inserted immediately after the gate, with the real 453,952-byte
mutable ledger present in the mirror. `--verify-paper` returns **clean, exit
0**. This is the #46 / R3-M1 class the §14 addendum was engraved against,
occurring at the gate that exists to prevent it.

**R-K3-4.** Register the object-under-test read inside `full_run` (pass the
path, read there) and **re-take `G-READS-DECLARED` in `finish()`**, holding the
full expected category set — `SOURCE` == the declared 19, `SELF` == {this
file}, `OBJECT-UNDER-TEST` == {the paper} or empty by declaration,
`ARTIFACT-STAGED` subset of {the two tmp paths} — with a mutant that adds an
undeclared read after the early gate.

### MAJOR-5 — the transcript's integrity check covers 40 of its 221 lines

`_write` reads the staged receipt back from disk and verifies all 36 seals
against it before `os.replace`. That leg is sound and proven live: **CINJ05**
(post-write corruption of `lor_receipt.json`) dies at `G-ARTIFACT-INTEGRITY`
naming `['SEAL-DIA']`, and the directory is left with **no artifacts at all**.

The staged transcript is only head-compared:
`read_text(tmp_t).split("\n")[:40] == R["transcript_head"]`. Nothing checks the
other 181 lines.

Demonstrated — **CINJ04**: line 121 of the staged `lor_output.txt` overwritten
with `evidence: FORGED BY THE REVIEWER` after the write and before the gate.
`G-ARTIFACT-INTEGRITY` **passes**, the run exits 0, and the corrupted
transcript is promoted: delivered `lor_output.txt` = `fc93aa9e9a68` (against
the committed `427a5da397aa`) while `lor_receipt.json` = `8b4ca74d954c`,
byte-identical to the committed one. The forged line replaced `G-WALL-L1`'s own
statement — a wall's testimony, silently rewritten at exit 0.

Under #119 the transcript is a published artifact and is owed disk-versus-seal
like any other.

**R-K3-5.** Seal the full transcript (`SEAL-TRANSCRIPT-BODY` over
`digest(text)`), read `tmp_t` back and compare the whole file against that
digest inside `G-ARTIFACT-INTEGRITY`, keeping the 40-line head compare as a
second leg. Build `text` after the last gate so the transcript carries it (see
MINOR-1).

### MAJOR-6 — four undeclared bypass channels in the numeral coverage

My independent recount reproduces the receipt's scan exactly — 771 scanned, 218
fenced, 343 inline-span, 111 word, 8 fenced blocks, multiset 8 of 8, both
exemptions firing once. The two rules E-22 bought are genuinely live: **INJ06**
forges one digit of a backticked digest and dies on the unbacked `77`;
**INJ07** forges one of the two copies of verdict segment 1 and dies on the
multiset; **INJ21** and **INJ22** forge *both* copies of segments 2 and 4 and
die too — so all four segments are multiset-protected, not only the
head-verbatim segment 1.

E-22's third rule — *no blanket whitelists* — does not hold. Four channels
remove or launder numerals; none is declared in `NUMERAL_EXEMPTIONS`, none is
required to fire:

1. **`SECREF = §\s*[\d.]+`** (line 3136), substituted away before the scan.
   INJ08: `A second step is treated in §4242 below.` — **survives**.
2. **`HEADNUM = ^#{1,6}\s*[\d.]+`** (line 3135). INJ09: `#### 4242.7 A note` —
   **survives**. Together these two strips remove **47 of the paper's 818
   numeral tokens** before anything is checked.
3. **sha256-12 digests in the allow list.** `receipt_numbers` walks
   `provenance`, whose `declared` and `measured` fields are 12-hex digests;
   **32 of the 116 allow-list tokens exist for no other reason** — among them
   `28 35 50 55 93 96 106 286 350 543 664 684 810 814 856`. **INJ18** changes
   §3.1's incidence spectrum from `162 at 7` to `106 at 7` — a **false measured
   number**, backed only by the digest `3d0516ab106e` — **survives**.
   **INJ18b** adds the fabricated sentence `At the seed fan 55 of the loci are
   live.` — **survives**.
4. **spelled numerals above twelve.** `WORDNUM` stops at `twelve`, so
   `sixteen`, `eighteen`, `nineteen`, `thirty-six` are never checked.
   **INJ23** rewrites §2's declared window to `seventeen six-round schedules
   ... nine one per measured dead class`, contradicting §3.2's rendered `16`
   claim — **survives**.

**R-K3-6.** (a) Move the two strips into `NUMERAL_EXEMPTIONS` as must-fire
declared rows publishing their occurrence counts, or scan the stripped tokens
against the allow list too. (b) Exclude `provenance/*/declared` and
`provenance/*/measured` from `receipt_numbers`'s walk — a digest is not a
measurement — and exempt the 19 digest literals by name instead. (c) Extend
`WORDNUM` through the words the paper actually uses (`thirteen`..`twenty`,
`eighteen`, `nineteen`, `thirty-six`, `fifty-four`), or require each spelled
form to be rendered from a receipt cell.

### MAJOR-7 — E-24 is a self-list, not a scan of what the paper publishes

`G-MEASURE-STAMP` checks that the four rows the unit typed into
`measure_stamps` each carry a stamp. It never looks at the object under test.

Demonstrated — **INJ10** adds to §6.4: `Six triangles and three lines occur at
324 of the 5,184 witnesses, so that class is typical.` — an unstamped fraction
over the witness space **and** an explicit typicality claim, both banned by
E-24 and by the unit's own §6.4 sentence. **Survives at exit 0.**

Where the stamp is applied it is correct, and every denominator recomputes
independently: 5,184 as 72² by exhaustive census; 17 loci from an 18-group
record; 27; 108; 216 anchored verbatim at V15; 864 by an independent edge
count; 792 = 864 − 72.

**R-K3-7.** Scan the object under test for `N of M` / `N of the M` / `N/M` over
the declared configuration spaces and require each hit to be covered by a
stamped row or a declared exemption; add `typical`, `typically`, `generic`,
`probability`, `likely` to the polarity probe list.

---

## 3. MINOR findings

**MINOR-1 — three gates appear in neither delivered artifact.** `R["gates"]` is
a snapshot copy taken at line 3752 (the correct fix for the growing-list seal),
but three gates are appended after it: `G-PAPER-COVERAGE-FINAL`,
`G-SEAL-COMPLETE`, `G-ARTIFACT-INTEGRITY`. The receipt publishes 50 of 53 gate
rows. And `text` is frozen at line 3798 before `_write`, so the transcript ends
at `G-SEAL-COMPLETE`: `G-ARTIFACT-INTEGRITY`'s PASS line is in neither
artifact. §14's claim about "a deliberately corrupted probe shown to be caught
first" therefore has no published evidence anywhere.
*Repair:* append the closing rows to `R["gates"]` inside `_write` before
serialising `final`, re-take `SEAL-GATES` there, and build `text` after the
last gate.

**MINOR-2 — `G-CEILING` carries two tautological clauses.**
`ceil_row["ceiling_after_the_step"] == 0` compares the literal `0` assigned at
line 2554 to itself; `all(r["places"] == (3 * 2 ** r["ceiling"]) ** 2 for r in
ladder)` compares `places` to its own defining expression (line 2538).
`steps_taken: 1` — which supplies `EXACTLY-1-STEP` to the head — is likewise
typed and ungated.
*Repair:* compute `ceiling_after_the_step` as `min(refined counts).bit_length()
- 1`; drop or re-derive the `places` clause; derive `steps_taken` from the step
actually applied.

**MINOR-3 — two head numbers about R = 4 are typed although the anchor
exists.** `at_r4_intervals_unique: 9` (line 1779) and `laws_non_empty_at_r4: 1`
(line 1867) are literals; the first reaches verdict segment 2 as
`AGAINST-9-OF-27-AT-R-4`, the second the rendered `laws` claim ("against 1 at
R = 4"). Paper-21's committed receipt — already read here, already the source
of 13 path anchors — carries the same quantity at `/split/law_06/intervals = 9`
(with `/split/law_06/record_level_splittable = false`). A path drift in the
predecessor that changed either would not die by anchor, which is the entire
purpose of the (path, value) layer.
*Repair:* add the two anchors and read them.

**MINOR-4 — one waived gate's machine-readable forcing is untrue.**
`G-DICTIONARY-CARRIER` is waived `SHARED-TARGET` with the forcing: "MUT-CARRIER
corrupts the carrier census the same construction feeds and is killed at
G-PROCESS-SUPPLY, one gate later; the bijection itself is a construction whose
failure would kill G-NEW-PLACES first." The second clause is false —
`G-NEW-PLACES` tests `places`, `COVERED` and `FREE_SLOTS` and never touches
`carrier`, `inc_ok` or `tri_ok`. **CINJ02** puts `inc_ok` off by one; the run
passes `G-NEW-PLACES` and dies at **`G-DICTIONARY-CARRIER` itself**. The gate
is live and falsifiable; it simply has no declared mutant, and the waiver
rationalises the absence with a statement measurement contradicts.
*Repair:* declare `MUT-INCIDENCE` (corrupting `inc_ok`) and delete the waiver.

**MINOR-5 — five inaccuracies in §14, the instrument section.**
(a) "Nineteen hash-pinned sources are read at run time **and nothing else**" —
the object under test and the two staged artifacts are also read (23 reads of
22 distinct files); the code's own docstring says so, the paper's does not.
(b) "26 verbatim text anchors ... **evaluated before the byte anchors**" —
`G-PROVENANCE` (the byte gate) is gate 1 and `G-VERBATIM` is gate 7; the true
statement is *before the source bytes are used for any measurement*.
(c) "the artifacts are **written from the sealed payload**" — `_write`
re-serialises `R` into `final`, which differs from the sealed `payload` by the
`payload_sha256_12` key.
(d) "the numeral scan covers **the whole object under test**" — 47 of 818
tokens are removed first (MAJOR-6).
(e) "each must exit 1 at exactly the gate its row declares **with both
artifacts byte-unchanged**" — the in-process sweep never writes and never
compares artifact digests; byte-unchangedness is asserted there, not measured.
(It is measured by this review, out of harness — §4.)

**MINOR-6 — the module docstring says the driven window is 13 schedules**
(line 18); it is 16 everywhere else, including the head.

**MINOR-7 — §6.4 "The 72 fractions here are stamped COUNTING-ONLY"** reads as
an assertion that there are 72 fractions; the referent is the single fraction
72 of 5,184.

**MINOR-8 — §6.4 "27 and 18 zero cells respectively"** has no antecedent
order: the two dead classes are not named in the sentence. Both values are
correct (`DEAD-triangles9-lines9` -> 27; `DEAD-triangles12-lines6` -> 18).

**MINOR-9 — the refined weld, the cut and the completion are measured at ONE
witness, unstamped.** `arena_wit` is the first `W6-SUPPLIED` row, i.e.
`supplied[0]`; `free_process`, `rel_proc`, `cf_arena` and the arena's live cut
locus all derive from its footprints. The carrier-isomorphism census and the
cut census do quantify over all 5,184 — but §6.5's "the refined weld returns
FOUND-candidate with 432 automorphisms and fibers 1/1/1" is an n = 1
measurement, and verdict segment 3 carries no scope stamp (the
`@WINDOW-16-DRIVEN` stamp sits on segment 1 only). The witness indices are
recoverable from `driven.rows`, so this is a disclosure gap, not a measurement
gap. *Repair:* run the refined detector at all six `W6-SUPPLIED` schedules, or
state the n = 1 scope in the segment.

---

## 4. The 41-mutant sweep, outside the harness

Each mutant re-invoked in **its own process** against an off-tree mirror; exit
code and death gate captured from stdout; the mirror's artifacts hashed before
and after the whole sweep.

**ALL 41 COMPLETED. Every one ON TARGET, every one exit 1, zero survivors,
zero crashes, zero off-target — and the mirror's `lor_output.txt` /
`lor_receipt.json` byte-unchanged across the entire sweep (`427a5da397aa` /
`8b4ca74d954c`).** The in-harness result the delivery run reports is therefore
independently confirmed, not relayed.

```
MUT-72                   -> G-72-TRIPLES            MUT-PARTITION        -> G-PARTITION-COUNT
MUT-ADDITIVITY           -> G-REFINED-BUILD         MUT-POLARITY         -> G-PAPER-CLAIM-POLARITY
MUT-ANCHOR-VALUE         -> G-ANCHORS-READ          MUT-SEAL-DROP        -> G-SEAL-COMPLETE
MUT-BUDGET               -> G-BUDGET-THEOREM        MUT-SIG              -> G-SIG
MUT-CARRIER              -> G-PROCESS-SUPPLY        MUT-SPLITFIBER       -> G-SPLIT-FIBER
MUT-CEILING              -> G-CEILING               MUT-SUPPLY           -> G-PROCESS-SUPPLY
MUT-CLAIM                -> G-PAPER-CLAIMS          MUT-TABLE            -> G-PAPER-TABLES
MUT-COMPAT               -> G-COMPATIBILITY         MUT-TWOWAY           -> G-TWO-WAY
MUT-CONSUMER-BINDING     -> G-ANCHOR-CONSUMERS      MUT-VERBATIM         -> G-VERBATIM
MUT-COVERAGE-SCAN        -> G-PAPER-COVERAGE        MUT-VERDICT          -> G-VERDICT-RECONSTRUCTED
MUT-CUT                  -> G-CUT-UNIQUE            MUT-WALL-BHS         -> G-WALL-BHS
MUT-DIA                  -> G-DIA                   MUT-WALL-COSMO       -> G-WALL-COSMO
MUT-EXEMPTION-DEAD       -> G-PAPER-COVERAGE        MUT-WALL-KR          -> G-WALL-KR
MUT-FALSIFIER-HONEST     -> G-FALSIFIER-HONEST      MUT-WALL-L1          -> G-WALL-L1
MUT-FIELD                -> G-R6-FIELD              MUT-WALL-LORENTZ     -> G-WALL-LORENTZ-NAMED
MUT-HEAD                 -> G-PAPER-HEAD-VERBATIM   MUT-WELD             -> G-WELD-COARSE
MUT-LAW04                -> G-LAW-04                MUT-WELDREF          -> G-WELD-REFINED
MUT-LAW06                -> G-LAW-06                MUT-WINDOW           -> G-DRIVEN-WINDOW
MUT-LAW09                -> G-LAW-09                MUT-WITNESSES        -> G-WITNESSES
MUT-MEASURE              -> G-MEASURE-STAMP         MUT-PAPER-FENCE-MULTISET -> G-PAPER-COVERAGE
MUT-NEWPLACES            -> G-NEW-PLACES
```

Note the standing of the three wall mutants in this list against MAJOR-1:
`MUT-WALL-BHS`, `MUT-WALL-KR` and `MUT-WALL-COSMO` each die exactly as
declared — because each writes its banned reading into `surface`. That is the
point of MAJOR-1: the falsifiers are honest and on target, and they falsify a
leg that is not the one the wall is owed. A green mutant sweep is not evidence
that a wall holds against the paper.

---

## 5. The injections table

| # | injected into | what | predicted | observed |
|---|---|---|---|---|
| INJ01a | §4.3 table | two rendered rows reordered | survive (benign) | exit 0 |
| INJ01b | §4.3 table | values cross-swapped between rows | die | **exit 1** `G-PAPER-TABLES` (missing 2) |
| INJ02 | §7 ladder | ceiling column swapped m=3 / m=4 | survive | **exit 0 — DEFECT** |
| INJ02b | §7 ladder | places column swapped m=4 / m=8 | survive | **exit 0 — DEFECT** |
| INJ03 | §6.4 census | class count 324 -> 144 | die | **exit 1** `G-PAPER-TABLES` (missing 1) |
| INJ04 | §4.1 laws | R=4 / R=6 cells swapped | survive | **exit 0 — DEFECT** |
| INJ05 | §2 arena | anchor counts 31 / 26 swapped | survive | **exit 0 — DEFECT** |
| INJ06 | inline span | one digit of a backticked digest | die | **exit 1** `G-PAPER-COVERAGE` unbacked `['77']` |
| INJ07 | §11 fence | one of two copies of segment 1 forged | die | **exit 1** `G-PAPER-COVERAGE` (multiset) |
| INJ08 | §12 | `§4242` | survive | **exit 0 — DEFECT** |
| INJ09 | §12 | heading `#### 4242.7` | survive | **exit 0 — DEFECT** |
| INJ10 | §6.4 | unstamped fraction + typicality claim | survive | **exit 0 — DEFECT** |
| INJ11 | §12 | expansion-of-space reading | **die** | **exit 0 — DEFECT (predicted death did not fire)** |
| INJ12 | §12 | sprinkling-grade Lorentz reading | **die** | **exit 0 — DEFECT (predicted death did not fire)** |
| INJ12b | §12 | Myrheim-Meyer dimension estimate | **die** | **exit 0 — DEFECT (predicted death did not fire)** |
| INJ13 | §12 | the retracted L-1 sentence, blockquoted + line-wrapped | die | **exit 1** `G-WALL-L1` hits 1 |
| INJ14 | §6.6 | naming sentence removed | die | **exit 1** `G-WALL-LORENTZ-NAMED` |
| INJ15 | §4.3 | description stamp removed | die | **exit 1** `G-WALL-COSMO` |
| INJ16 | §12 | negation of a measured fate | die | **exit 1** `G-PAPER-CLAIM-POLARITY` |
| INJ17 | §4.3 | rendered prose number 36 -> 108 | die | **exit 1** `G-PAPER-CLAIMS` missing `['places']` |
| INJ18 | §3.1 | false spectrum `162 at 7` -> `106 at 7`, hash-laundered | survive | **exit 0 — DEFECT** |
| INJ18b | §6.3 | fabricated sentence using hash-only `55` | survive | **exit 0 — DEFECT** |
| INJ20 | §6.4 census | two rendered rows reordered | survive (benign) | exit 0 |
| INJ21 | both fences | segment 2's R=4 number forged in BOTH copies | die | **exit 1** `G-PAPER-COVERAGE` |
| INJ22 | both fences | segment 4's ceiling-after forged in BOTH copies | die | **exit 1** `G-PAPER-COVERAGE` |
| INJ23 | §2 | spelled window `sixteen` -> `seventeen` | survive | **exit 0 — DEFECT** |
| CINJ01 | code | read the mutable ledger after `G-READS-DECLARED` | survive | **exit 0 — DEFECT** |
| CINJ02 | code | `inc_ok` off by one | die | **exit 1** `G-DICTIONARY-CARRIER` |
| CINJ04 | code | staged transcript line 121 forged post-write | survive | **exit 0 — DEFECT, corrupted transcript PROMOTED** |
| CINJ05 | code | staged receipt forged post-write | die | **exit 1** `G-ARTIFACT-INTEGRITY` `['SEAL-DIA']`, nothing written |
| CINJ06 | code | `R["dia"]` mutated after `SEAL-DIA` | die | **exit 1** `G-PAPER-CLAIMS` (one gate before the seal close) |
| CINJ07 | code | an evaluated gate absent from the registry | die | **exit 1** `G-COVERAGE` drift `['G-UNREGISTERED']` |

**18 injections were predicted to die. 15 died, each at its predicted gate.
Three predicted deaths did not fire** — the three wall readings (MAJOR-1).
Fourteen were predicted to survive and did: eleven exposing a defect, two
benign, one (CINJ01) a code-side probe.

Honest limit: **CINJ06 did not isolate the value-close branch.** Mutating
`R["dia"]` after its seal kills the run at `G-PAPER-CLAIMS`, one gate before
`SEAL.close` runs, so the "payload was sealed over a broken seal" branch was
not exercised by injection. It is unconditional over all 36 rows against the
final receipt, and the `verify()` it shares with the disk-vs-seal leg is proven
live by CINJ05 — but that branch itself remains untested here and is registered
as such.

---

## 6. The disease sweep

| # | row | verdict | demonstration |
|---|---|---|---|
| 1 | phantom consumers (26 verbatim + 31 path-value, 36 seals) | **ABSENT** | 26/26 verbatim found, 31/31 path-values matched; the 24 named consumer gates are all in the 53-gate registry AND all in the published gate rows (so all evaluated); `G-COVERAGE` forces registry ≡ evaluated, drift `[]`; 22/24 carry a declared mutant, the two that do not (`G-I7-READOUT`, `G-REFINED-ADMISSIBLE`) are waived with forcings that hold |
| 2 | constant-boolean falsifiers; E-23 three-legged honesty (15 sampled) | **ABSENT** | 41/41 hooks located by AST; the object each row names as corrupted appears in its own hook source 41/41; 0 constant-boolean corruptions; all 41 targets registered; every hook single-site. 15 descriptions read verbatim against their hook source — all accurate. Sweeps bound to executions by `G-SWEEP-BOUND` **and** re-taken unconditionally as `sweep_complete` inside `G-ARTIFACT-INTEGRITY`, so the file's only writer is downstream of a sweep that actually ran |
| 3a | seals taken before their object's last cell | **ABSENT (fix holds)** — one branch untested | `SEAL.close` re-digests all 36 sealed paths against the FINAL receipt and raises before any write; the shared `verify()` is proven live by CINJ05. The raising branch itself was not reached (see §5's honest limit) |
| 3b | seal over a still-growing list | **ABSENT (fix holds)** | `R["gates"]` is a snapshot copy, so `SEAL-GATES` cannot be broken by later appends — at the price of MINOR-1 (3 gate rows unpublished) |
| 3c | transcript-head compare broken by newline args | **ABSENT (fix holds)** | head taken as `"\n".join(LINES).split("\n")[:40]` and compared against the same slicing of the file as written; live evidence "transcript head matches True" |
| 3d | read-registry accumulating across in-process sub-runs | **PRESENT — the fix over-corrected** | the per-run clear also erases the object-under-test read made in `main`; gate evidence reads `categories ['SOURCE']`; CINJ01 proves the gate cannot see a mutable-state read added after it. **MAJOR-4** |
| 3e | the coverage hole (3 gates + `G-SWEEP-BOUND` registry drift) | **ABSENT (fix holds)** | `uncovered []`, `registry_drift []`; CINJ07 (an added unregistered gate) dies at `G-COVERAGE` naming it |
| 4 | 36 seals at value-close; read-back BEFORE `os.replace` | **PARTIAL** | receipt: all 36 verified from disk before `os.replace`; CINJ05 dies and writes nothing. transcript: 40 of 221 lines checked; CINJ04 promotes a forged line 121 at exit 0. **MAJOR-5** |
| 5 | E-22 — fences by TRUE multiset; ALL tables as claims; 343 inline spans; NO blanket whitelists | **PRESENT (2 of 4 legs fail)** | fences: multiset live at all four segments (INJ07/21/22 die). inline spans: live (INJ06 dies on a corrupted backticked numeral). tables: 13 of 40 data rows rendered; four table forgeries survive (**MAJOR-2**). whitelists: four undeclared channels; five forgeries survive (**MAJOR-6**) |
| 6 | vacuous clauses | **PRESENT (minor)** | `G-CEILING` carries two tautologies over values typed or defined a few lines above (**MINOR-2**). `G-SWEEP-BOUND`'s `not swept` short-circuit and the `paper_text is None` guards are declared and re-taken elsewhere — not vacuous |
| 7 | E-24 — the 72/5,184 COUNTING-ONLY stamp; denominators re-counted | **PARTIAL** | the stamp is present and correct, and every denominator recomputes independently (5,184 = 72² by census; 17; 27; 108; 216 anchored; 864 by an independent edge count; 792 = 864 − 72). But the gate polices only the unit's own four-row list — INJ10 survives with an unstamped witness-space fraction and an explicit typicality claim. **MAJOR-7** |
| 8 | the FULL 41-mutant sweep OUTSIDE the harness, raising gate parsed, artifacts unchanged | **CLEAN — 41 of 41** | every mutant in its own process: 41/41 ON TARGET, 41/41 exit 1, zero survivors, zero crashes, zero off-target; mirror artifacts byte-unchanged across the whole sweep. §4. Caveat of record: the three wall mutants die honestly on the `surface` leg, which is not the leg the wall is owed (MAJOR-1) |
| 9 | CLI hostile argv incl. arity; `--verify-paper` on a foreign paper; selftest write-nothing by tree hash | **CLEAN** | 12/12 hostile forms exit 2 (unknown flag, bare word, empty string, missing NAME, unknown NAME, trailing extra arg, two modes, duplicated mode, `-h`, missing file); both registries exit 0; foreign paper exit 1 DRIFT at `G-WALL-COSMO`; selftest exit 1 at `G-PROVENANCE` with the **whole mirror tree hash identical** before and after |
| 10 | byte x2 across two `PYTHONHASHSEED`s, off-tree provisioned; bare-copy loud abort writes nothing | **CLEAN** | seeds 0 and 31337 in two separate off-tree git-less mirrors both reproduce `427a5da397aa` / `8b4ca74d954c` exactly; bare copy exits 1 with `[CLI] missing source: ...`, plain and `--selftest`, writing nothing |
| 11 | the 771-numeral sweep (218 fenced, 343 inline, 111 words); the scanner's own coverage per E-22's inline rule | **RECONFIRMED — with 47 tokens outside it** | independent recount reproduces 771 / 218 / 343 / 111 / 8 blocks / 2 exemptions fired exactly; the raw paper carries **818** tokens, 47 removed by two undeclared strips before anything is checked. **MAJOR-6** |
| 12 | the W6 window's declaration (16 driven schedules) — declared in-string? licensed? | **DECLARED AND LICENSED — two gaps** | the window is published as data (`driven.rows`: 16 rows with triple indices, seed k, stratum), declared in §2, and stamped into the head as `@WINDOW-16-DRIVEN-OF-5,184-WITNESSES`; the 6 + 8 + 2 composition is gated per stratum against `len(supply_rows) - 1`; every other column is exhaustive. Gaps: §2's spelled "sixteen" is unscannable (INJ23), and the refined weld / cut / completion are n = 1 within the window, unstamped (MINOR-9) |

---

## 7. The seam ruling

**The seam is between the receipt and the paper.**

Everything this instrument measures, it measures correctly: it seals at value
close, it reproduces byte-for-byte off-tree and git-less under two hash seeds,
its 41 declared falsifiers are honest at all three E-23 legs and die where they
say, its anchors bind to gates that exist and are taken, and its own coverage
ledger, registry-drift check and sweep binding all work — three of which I
proved live by injection.

What it does not do is police the artifact a reader actually reads. Of the
paper's four defences — rendered claims, rendered tables, the numeral scan, the
walls — the first is sound, the second covers a third of the tables, the third
has four bypass channels, and three of the five walls point at the receipt
instead of the paper.

The practical shape of the seam: **a forged LOR paper that changes no rendered
sentence and no fenced segment passes `--verify-paper` at exit 0.** It may
carry, simultaneously, a false arena-theorem row, a false law-census table, a
false provenance row, a false incidence spectrum, a false declared window, an
unstamped typicality claim, and an explicit cosmological reading. None of that
touches a verdict; all of it touches what the verdict is read against. And on
the instrument side, a corrupted transcript reaches disk at exit 0 while the
receipt beside it is byte-perfect.

That is why this is AWF and not R. No measurement moved. The seven repairs are
each a few lines against machinery that already exists — the ladder is already
a receipt cell, `G-WALL-L1` already shows the paper-scanning pattern,
`SEAL.close` already shows the disk-vs-seal pattern the transcript needs, and
`G-COVERAGE` already shows how a registry is held against what actually ran.

**Registered for the adjudication, untested here.** The four defects that are
*template*-shaped rather than LOR-shaped — unrendered tables (MAJOR-2), the
numeral whitelists including the sha-digest launder (MAJOR-6), the
receipt-only wall surface (MAJOR-1) and the head-only transcript check
(MAJOR-5) — are inherited machinery, not this worker's invention. Before any
of them is engraved as a new rule, a corpus sweep of the sibling units built
on the same template is the cheaper move; on the evidence here I would expect
hits.

---

*Reviewer executions: 95, all off-tree, including the complete 41-mutant sweep
outside the harness (41/41 ON TARGET). Recomputations: 258. Repo writes: this
file only. Git: read-only. The LOR objects' hashes at close are identical to
those at start.*
