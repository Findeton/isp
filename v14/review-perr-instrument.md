# PER-R (paper-29) — INSTRUMENT REVIEW (K3)

**Seat:** INSTRUMENT-LENS, the era audit — seal, coverage, injections, CLI,
#91 at its own hands; the full current disease sweep; the #267 template
compliance audit. **Object at 442b3fe** (`v14 #280`), verified at open and at
close.

**GRADE: AWF** — accept with fixes. **No measured quantity is wrong.** Every
headline number of this unit was recomputed here by routes the instrument does
not use — including a full brute-force census at R = 3 over all 3,697,960
grouping multisets, a nibble-free reimplementation of the entire saturating-
stratum convolution, an exact set-cover computation of the locking theorem, and
a coordinate-by-coordinate rebuild of the singular witness from its own
published groupings — and all agreed. The unit is byte-reproducible off-tree,
git-less, at two hash seeds. **The seven MAJORS are all perimeter defects:
things the instrument SAYS it binds and does not.** Six of the seven are
template diseases the #267 advisory named; one (the declared window) is
PER-R-specific and is the only one that puts a false sentence in the paper.

## 0. HASHES — VERIFIED AT OPEN AND AT CLOSE

| object | declared (sha256-12) | measured at open | measured at close |
|---|---|---|---|
| `v14/paper-29-perr.md` | `7d1d6ca3c5bc` | `7d1d6ca3c5bc` | `7d1d6ca3c5bc` |
| `v14/code/perr_exact.py` | `d2f8fdac143d` | `d2f8fdac143d` | `d2f8fdac143d` |
| `v14/code/perr_output.txt` | `6dad652f81fe` | `6dad652f81fe` | `6dad652f81fe` |
| `v14/code/perr_receipt.json` | `ac424c8a7bdd` | `ac424c8a7bdd` | `ac424c8a7bdd` |
| `v14/note-perr-pin.md` (pin) | `6339ba42f354` | `6339ba42f354` | `6339ba42f354` |

`git status` on all four objects: clean, before and after. All execution was
off-tree in `scratchpad/perr-in/`. Sibling working-tree drift (LOR, SIG, SEC,
AID, ACT) is disclaimed and untouched. Repo writes by this seat: **one** —
this file.

**Counts.** 71 executions of the instrument (2 full delivery runs at two
`PYTHONHASHSEED`s, 43 out-of-harness `--mutant` runs, 16 hostile-argv
invocations, `--selftest`, `--no-write` ×2, 2 bare-copy runs, 1 source-tamper
run, 2 patched write-path probes, 2 registry listings). **≈ 300 independent
recomputations of published quantities** (itemised in §3 and §8), plus **41
paper/code injections carrying 410 gate evaluations**. Zero disagreements with
any measured number.

---

## 1. THE DISEASE SWEEP — PRESENT / ABSENT, WITH DEMONSTRATIONS

| # | disease | verdict | demonstration |
|---|---|---|---|
| 1 | **referent-binding** (the OCC lesson) | **PRESENT — MAJOR-1** | 7 of 7 column-label swaps survive at exit 0, including the SIG-feed class ladder. The DATA cells are bound: 4 of 4 cell forgeries die at `G-PAPER-TABLES`. |
| 2 | phantom consumers (23 anchors) | **latent — MINOR-2** | All 18 named consumer gates exist in the 49-gate ledger, so no phantom today. But the binding is vacuous: renaming ALL 23 consumers to `G-DOES-NOT-EXIST` leaves `G-ANCHORS` passing. |
| 3 | constant-boolean falsifiers + E-23 three-legged | **ABSENT** | 43/43 hooks AST-located, 0 constant-boolean, 43 hook sources published. 15 sampled descriptions checked against their hooks verbatim — 15/15 exact. Sweep bound to the writer by `G-SWEEP-EXECUTED` and re-taken at `G-INTEGRITY`. |
| 4 | seal windows / read-back before replace | **mostly ABSENT — MINOR-9, MAJOR-7 (2nd clause)** | 48 seals, all taken at value-close with their gate downstream; integrity is disk-vs-seal with a corrupted probe shown detected. But `G-INTEGRITY` runs AFTER `os.replace`, so the "writes nothing" clause is false. |
| 5 | **E-22** (fences by multiset; all rows; inline spans; digest tokens; spelled numerals) | **ABSENT on every leg except headers** | Fences by TRUE multiset: forging one copy, forging both, appending a third and deleting one all die (4/4). Inline spans scanned (2/2 die). No all-digit digest enters the whitelist (0 of 113 digest strings). Spelled numerals above twelve ARE scanned — `thirteen`…`twenty`, `thirty`…`ninety`, `hundred`, `thousand`: unbacked `hundred`/`thousand` die. **Scanner verified: 121 number-words, not the 119 recorded in LOG #280.** 54 of 54 rendered rows occur exactly once. |
| 6a | **#267: paper-scanning walls** | **ABSENT — FIXED** | All four reading walls scan the paper body. Planted in §5.2: a sprinkling reading dies at `G-WALL-BHS`; a Myrheim–Meyer estimate at `G-WALL-KR`; an interference reading at `G-INTERFERENCE-CLOSED`; the retracted L-1 sentence, **line-wrapped AND blockquoted**, at `G-WALL-L1`. This is the LOR §269 caveat discharged: the plants die ON THE PAPER LEG. |
| 6b | **#267: no typed counts** | **PARTIAL — MINOR-1** | 49/43/23/54 are all computed (`len(LD.rows)`, `len(MUTANTS)`, `len(VERBATIM)`, `len(want)`), never typed. But §13 types two counts in prose that no gate binds: `14 sources` → `13 sources` survives; `Eight columns are back-validated` → `Nineteen columns` survives. |
| 6c | **#267: full-transcript integrity** | **PRESENT — MAJOR-3** | Two forged late lines PROMOTED into the delivered artifact at exit 0, with `G-INTEGRITY-PRE` and `G-INTEGRITY` both PASS. |
| 7 | **exhaustiveness licenses** (280⁵ by local type; 36⁵ schema) | **SOUND** — see §3 | Both reductions audited and independently validated. No local-type class can be dropped: the 7 bucket keys are exactly the measured alphabet and sum to 280. |
| 8 | **the W5 = 19 window's declaration + license** | **PRESENT — MAJOR-2** | The paper's §6.2 decomposition contradicts the run's own `driven.window`, in two places that cancel in the sum. |
| 9 | E-24 (fraction stamps; counter-column currencies) | **PARTIAL — MINOR-4** | The currencies ARE named and the counter-column IS published with labelled keys. But `COUNTING-ONLY` appears nowhere except one §13 sentence — 0 occurrences in the receipt: an E-24 self-list, LOR's M7 recurring. |
| 10 | the 43-mutant sweep outside the harness | **CLEAN** — see §5 | Registry read from the `MUTANTS` dict directly (the #281 name-format lesson). Artifacts tree-hashed before and after. |
| 11 | CLI (hostile argv incl. arity) + selftest write-nothing | **CLEAN — MINOR-5** | 16/16 hostile forms exit 2, arity included. Selftest write-nothing PROVED by an independently computed whole-tree hash. `--list-gates` lists 40 of 49 gates (an undisclosed convention). |
| 12 | byte ×2 across two seeds, off-tree; bare-copy abort | **CLEAN — MINOR-6** | Both artifacts byte-identical to the committed sha at `PYTHONHASHSEED` 0 and 99991, off-tree and git-less. Bare copy exits 1 writing nothing — but by an uncaught traceback, not a named gate. |
| 13 | the 825-numeral + 119-word sweep | **CLEAN, count corrected** | 825 numerals reproduced exactly; **121** number-words, 26/26 exemptions fired, 38,833 chars. |

---

## 2. THE #267 TEMPLATE-CHECKLIST COMPLIANCE AUDIT

The unit claims compliance with all four template diseases the LOR K3 review
routed as mid-flight advisories. Verified item by item:

| #267 item | claimed | measured | verdict |
|---|---|---|---|
| paper-scanning walls | yes | 4 plants, 4 deaths, all on the paper leg | **COMPLIANT** |
| full-table rendering | yes | 54 rendered rows, 61 rows in the paper; 4/4 cell forgeries die | **COMPLIANT ON CELLS, NOT ON HEADERS** (MAJOR-1) |
| typed totals-counts | yes | the four registry counts derived; two §13 prose counts free | **PARTIAL** (MINOR-1) |
| transcript-full-integrity | yes | forged lines promoted | **NOT COMPLIANT** (MAJOR-3) |
| digest-token whitelists | — | 113 digest strings, 0 all-digit, none enters the whitelist | **COMPLIANT** |
| spelled numerals above twelve | yes | scanned and killed when unbacked | **COMPLIANT** |

Two of six compliance claims do not hold as stated.

---

## 3. THE EXHAUSTIVENESS LICENSES — AUDITED AND INDEPENDENTLY VALIDATED

This was the hardest row. Both reductions are **sound**, and I could not drop a
class from either.

**(a) The 280⁵ ≈ 1.72×10¹² covering-class census "via local types."**
`covering_with_code` buckets all 280 partitions by their local type at one
site, enumerates every type multiset summing to the target, and carries the set
of achievable unions forward. Four soundness questions, all answered:

1. *Multisets vs. ordered tuples.* Union is commutative and associative and the
   DP explores every partition of every bucket independently, so the achievable
   union set of a multiset is order-independent. The quantifier is complete.
2. *Could a local-type class be dropped?* No. The bucket keys are exactly the
   seven measured alphabet codes and the bucket sizes sum to 280
   (100/50/50/50/10/10/10) — verified here. `type_multisets` draws from the same
   alphabet, gated at `G-ALPHABET` per site.
3. *Is the prune safe?* `popc(FULL & ~n) <= 9·left` is a necessary condition for
   any completion, so it drops no state that could reach FULLMASK. There is no
   beam: every surviving state is kept.
4. *Is one site enough?* Yes, and it is measured: translation carries masks
   (2,520 pairs, 0 mismatches), and covering is translation-invariant, so a
   covering tuple with code c at site x translates to one with code c at (0,0).

**Independent validation.** A full brute force at R = 3 over all **3,697,960**
grouping multisets returns exactly one covered covering-class code, `[1,1,1]` —
the instrument's answer. At R = 4 the instrument reproduces paper-21's
committed row (7 codes, max cell 2, 4det support {3,4,7}) by a route that unit
did not use. At R = 5 I confirmed independently that all 32 published codes lie
in the 90 covered codes, that the 4det support {0,3,4,7,8,11,12,15} and the
three non-posdef members recompute from the codes themselves, that none carries
a 5, and that all three indefinite covered codes are absent. A random,
DP-free witness search found explicit covering quintuples for `[1,3,3]`,
`[1,4,2]`, `[2,2,3]` and — the headline — `[1,1,4]`.

**The locking theorem, independently re-proved and STRENGTHENED.** It is not
trivial: the union of all 70 locked masks at each link *does* cover all 27
cells. An exact minimum-set-cover computation and a level-BFS, neither using
the instrument's DP, both return **7** as the minimum number of locked rounds
needed to cover — at every one of the three declared links. So "no covering
quintuple carries a cell count of 5" is true with two rounds to spare, and the
same computation independently rules out a cell count of 6 at R = 6. The
"seven distinct third members against five rounds" mechanism recomputes to 7 at
all three links.

**(b) The 36⁵ saturating-stratum schema.** The argument — 9 incidences maximum
per round, so 5 rounds carry at most 45; a homogeneous record summing to 5
needs 9·5 = 45; equality forces every round to saturate — is correct, and its
empirical premise (max 9) is measured at `G-ARENA` from the observed spectrum
{0:1, 4:27, 6:54, 7:162, 9:36}. It is a **proof, not a citation**. See MINOR-8
for the one weakness: the gate's own three conjuncts restate definitions.

**Independent validation of everything the stratum publishes.** I rebuilt the
whole convolution with unpacked 27-tuple keys (no `pack4` nibbles) and
meet-in-the-middle: R = 5 total **60,466,176**, cover **1,842,120**, distinct
fields **619,092**; homogeneous 680/1,350/680/1,350/1,350/680; and the R = 6
door **(2,2,2) at 48,600** and **G-SINGULAR at 1,350**. Every number matched.

---

## 4. THE INJECTIONS

Injections were driven through a harness that loads the committed instrument as
a module and replays each paper-facing gate's own source expression. **Harness
fidelity is proved, not asserted:** on the clean paper it reproduces the
committed evidence strings exactly — surface **93,698** chars, paper body
**36,683** chars, **825** numerals, **121** number-words, **26/26** exemptions,
**38,833** chars, **54** rendered rows, **61** paper rows. Wall-surface
reconstruction matches the run's own build point (source line 2882) to the
character.

| # | injection | target | result |
|---|---|---|---|
| INJ-01 | swap `covered site code` ↔ `covering record` headers (§3.6) | referent binding | **SURVIVES** |
| INJ-02 | swap `structurally live record` ↔ `I7-declared record` headers | referent binding | **SURVIVES** |
| INJ-03 | swap `site codes` ↔ `covering-class codes` headers (§3.2) | referent binding | **SURVIVES** |
| INJ-04 | swap `counts` ↔ `budget` headers (§3.5 floor table) | referent binding | **SURVIVES** |
| INJ-05 | swap `fate` ↔ `link-constant` headers (§6 fiber table) | referent binding | **SURVIVES** |
| INJ-06 | swap `at the rung below` ↔ `here` headers (§11.1 tally) | referent binding | **SURVIVES** |
| INJ-07 | swap `witnesses` ↔ `multisets` headers (§7 DIA) | referent binding | **SURVIVES** |
| INJ-08 | swap the SINGULAR/INDEFINITE row labels | control | dies `G-PAPER-TABLES` |
| INJ-09 | rename a floor-table row | control | dies `G-PAPER-TABLES` |
| INJ-10 | flip a fiber-table fate | control | dies `G-PAPER-TABLES` |
| INJ-11 | flip a persistence verdict | control | dies `G-PAPER-TABLES` |
| INJ-12 | plant a sprinkling reading in §5.2 | wall, paper leg | dies `G-WALL-BHS` |
| INJ-13 | plant a Myrheim–Meyer estimate in §5.2 | wall, paper leg | dies `G-WALL-KR` |
| INJ-14 | plant an interference reading in §5.2 | wall, paper leg | dies `G-INTERFERENCE-CLOSED` |
| INJ-15 | retracted L-1 sentence, line-wrapped + blockquoted | wall, #125 | dies `G-WALL-L1` |
| INJ-16 | delete the mandatory naming clause | wall | dies `G-WALL-LORENTZ` |
| INJ-17 | same reading planted INSIDE §9 | declared scope | survives (by design; MINOR-10) |
| INJ-18 | forge a numeral inside an inline code span | E-22 | dies `G-PAPER-COVERAGE` |
| INJ-19 | forge a numeral in ONE fence copy | E-22 multiset | dies `G-PAPER-FENCES` |
| INJ-20 | forge the same numeral in BOTH copies | E-22 multiset | dies `G-PAPER-FENCES` |
| INJ-21 | append a forged THIRD fence copy | E-22 multiset | dies `G-PAPER-FENCES` |
| INJ-22 | delete one fence copy | E-22 multiset | dies `G-PAPER-FENCES` |
| INJ-23 | unbacked spelled compound `Forty-two` | word scanner | dies `G-PAPER-COVERAGE` (on `forty`) |
| INJ-24 | 7 spelled numerals above twelve, backed and unbacked | word scanner | `hundred`/`thousand` die; `thirteen`…`ninety` correctly pass |
| INJ-25 | `14 sources` → `13 sources` (§13) | typed count | **SURVIVES** |
| INJ-26 | `Eight columns` → `Nineteen columns` (§13) | typed count | **SURVIVES** |
| INJ-27 | `280 partitions, 36 of` → `27 of` | control | dies `G-PAPER-CLAIMS` |
| INJ-28 | `The window is 19 schedules` → `8 schedules` | W5 declaration | **SURVIVES** |
| INJ-29 | W5-SEEDFAN `at all nine` → `at all seven` | W5 declaration | **SURVIVES** |
| INJ-30 | W5-LADDER `all six` → `all four` | W5 declaration | **SURVIVES** |
| INJ-31 | unbacked numeral in an inline span (§13) | E-22 | dies `G-PAPER-COVERAGE` |
| INJ-32 | drift the pin ledger number in an inline span | E-22 | dies `G-PAPER-COVERAGE` |
| INJ-33 | drift the census family size by one | license | dies `G-PAPER-COVERAGE` |
| INJ-34 | 23 anchor consumers → `G-DOES-NOT-EXIST` | phantom consumer | **SURVIVES** |
| INJ-35 | 23 anchor consumers → `G-EXACT` (consumes none) | phantom consumer | **SURVIVES** |
| INJ-36 | forged late line indented 9 spaces | transcript | **SURVIVES — PROMOTED** |
| INJ-37 | forged late line containing a closing gate name | transcript | **SURVIVES — PROMOTED** |
| INJ-38 | rebuild the wall surface from the FULL receipt | surface totality | 3 gates FAIL on the unit's own clean receipt |
| INJ-39 | corrupt one pinned source by one byte | provenance | dies, artifacts unchanged |
| INJ-40 | bare copy, no sources | provenance | exits 1, writes nothing (traceback) |
| INJ-41 | corrupt the JSON on disk after `os.replace` | post-write | detected at `G-INTEGRITY`, but the corrupt bytes REMAIN (MAJOR-7) |

**41 injections. 16 survived that should have died — every one a finding
below (INJ-01…07, 25, 26, 28…30, 34, 35, 36, 37). 25 behaved correctly,
including two survivals that are correct by design: INJ-17 (the wall section is
declared out of the scan's scope) and the backed members of INJ-24 (a spelled
numeral whose value IS receipt-backed should pass).**

---

## 5. THE 43-MUTANT SWEEP, OUTSIDE THE HARNESS

Registry read directly from the `MUTANTS` dict in source (never from
`--list-mutants` prose — the #281 name-format lesson). Each mutant run as its
own subprocess in an off-tree copy. **43 of 43 ON TARGET, zero survivors, zero
off-target deaths.** Every run exited 1 — the declared convention for "killed
at the named gate" — and the raising gate was parsed from each run's own line
and compared against the registry's declaration: 43 matches, 40 distinct gates
hit (three gates carry two mutants each).

Sweep-tree hash before and after the 43 runs:
`3a113925362f…` = `3a113925362f…` — **artifacts byte-unchanged across all 43
runs.** No mutant writes.

The one caveat of record, inherited from LOR §269 and discharged here rather
than repeated: the four wall mutants (`M-PAPER-BHS`, `M-PAPER-KR`,
`M-PAPER-INTERFERENCE`, `M-WALL-L1`) die on the PAPER leg, and I verified that
independently with four hand-planted readings in §5.2 (INJ-12…15). This unit's
green sweep on the walls IS evidence.

The one caveat I add: `M-TRANSCRIPT`'s green badge is NOT evidence — see
MAJOR-3.

The in-harness sweep is separately bound: a delivery run carries one sweep row
per declared mutant, `G-SWEEP-EXECUTED` requires all on target, and
`G-INTEGRITY` re-takes the conjunction, so the only writer in the file is
downstream of a sweep that actually ran. That binding is sound and I could not
break it.

---

## 6. FINDINGS

### MAJOR-1 — REFERENT BINDING: EVERY TABLE'S COLUMN LABELS ARE UNBOUND

`paper_tables` renders DATA rows only. Every table's header row — the row that
says what the numbers ARE — is never rendered and never matched, so
`G-PAPER-TABLES` (54 rendered, 0 not-exactly-once) is silent on it. Seven
header swaps survive at exit 0. The worst is the SIG-feed class ladder of §3.6,
the table this unit computes "first and states separately" because another
unit's Stage 0 consumes it: swapping `covered site code` and `covering record`
turns

> SINGULAR 4 5 6 6 / INDEFINITE 5 6 7 8

into the claim that the singular boundary is a COVERING RECORD at R = 4 and a
covered site code at R = 5 — the exact inversion of the headline
`COVER=POSDEF BREAKS AT R=5`, and of the feed §3.7 hands to SIG. The same
swap in §3.2 makes 54/105/181 read as covering-class codes and 1/7/32 as site
codes; in §11.1 it puts `cover = positive definite` at True HERE and False
BELOW.

The controls prove the gate is otherwise sound: swapping the SINGULAR/
INDEFINITE row labels, renaming a floor row, flipping a fiber fate and flipping
a persistence verdict all die at `G-PAPER-TABLES`.

**REPAIR R-PR-1.** Render the header row of every measurement table from the
receipt alongside its data rows, and require each to occur exactly once. The
column names are the class names — `COVERED-SITE-CODE`, `COVERING-RECORD`,
`STRUCTURALLY-LIVE-RECORD`, `I7-DECLARED-RECORD` — and they are already keys in
`R["reachability_ladder"]["rows"]`, so the header renders from the receipt with
no new declaration. Do the same for the other five tables.

### MAJOR-2 — THE DECLARED WINDOW W5 IS MISDESCRIBED IN THE PAPER, AND NOTHING BINDS IT

`R["driven"]["window"]` is
`{W4-ANCHOR: 1, W5-CTRL: 1, W5-LADDER: 6, W5-SEEDFAN: 8, W6-CTRL: 1, W6-DOOR: 2}`
= 19. The paper's §6.2 says:

> W5-LADDER is … all six, none sampled; W5-SEEDFAN is the (1, 1, 3) arrangement
> at **all nine** canonical transversal choices of its first two rounds;
> W5-CTRL and W6-CTRL are d66's own R = 5 and R = 6 points; W6-DOOR is …

Two errors, in the one scope this unit declares rather than exhausts. I measured
the mechanism of each rather than inferring it:

1. **The "all nine" clause double-counts one schedule.** `window_schedules`
   enumerates the 3 × 3 seed choices, but `add()` deduplicates, and the
   (s₀,s₁) = (0,0) choice is *identical* to the W5-LADDER member of (1,1,3).
   Verified by driving the tagging: (0,0) → `W5-LADDER`, the other eight →
   `W5-SEEDFAN`. So the clause is TRUE as a statement about the seed axis (all
   nine choices are in the window) and FALSE as a component of a decomposition
   (one of the nine is the ladder member, already counted).
2. **W4-ANCHOR is never named at all.** It is `committed_schedule(4)`, verified
   here to be of budget 4 and the ONLY budget-4 member of the window — while
   the head advertises `DRIVES 19 SCHEDULES OVER BUDGETS 4/5/6` and §6.1 leans
   on the R = 4 anchor. A reader reconstructing the window from §6.2 cannot
   reach budget 4 at all.

The two errors cancel exactly: the paper's decomposition reads
6 + 9 + 1 + 1 + 2 = 19, the run's is 6 + 8 + 1 + 1 + 2 + 1 = 19. Because they
cancel, no numeral in §6.2 is unbacked and no gate sees anything; and because
`driven.window` is published but never rendered as a claim or a table row,
nothing binds §6.2 to the dict it purports to describe.
`window_schedules`' own docstring repeats both errors — it says "all 3 x 3"
and omits W4-ANCHOR from its list — so E-23's description-honesty leg does not
catch it either. The three probes confirm the absence of any binding:
`19 schedules` → `8 schedules`, `all nine` → `all seven`, and `all six` →
`all four` ALL survive at exit 0.

This is the only finding that puts a false sentence in the paper. It matters
because §12 deviation 3 prices the window as the unit's one non-exhaustive
scope, and §6.2 is its licence.

**REPAIR R-PR-2.** (a) Correct §6.2: W5-SEEDFAN is eight schedules (the ninth
transversal choice coincides with the W5-LADDER member of (1,1,3)), and name
W4-ANCHOR as the budget-4 member. (b) Correct the `window_schedules`
docstring. (c) Render `R["driven"]["window"]` as a paper table — one row per
tag with its count — so the decomposition is bound cell by cell, not only its
sum.

### MAJOR-3 — TRANSCRIPT INTEGRITY ADMITS TWO OF THE THREE FORGED-LINE SHAPES

```
tail_ok = all(any(g in ln for g in closing) or ln.startswith(" " * 9)
              for ln in tail)
```

The sealed prefix (168 lines) is digested. Everything after it is admitted by
two whitelist clauses, both defeatable:

- `ln.startswith(" " * 9)` admits **any** line indented nine spaces — which is
  exactly the indentation of every statement and evidence line the instrument
  prints.
- `any(g in ln for g in closing)` is substring containment, not equality, so
  any line merely *containing* `G-SEAL-TOTAL` is admitted.

Demonstrated: a patched run appended
`         FORGED: the covering class and the positive-` and
`  [PASS] G-SEAL-TOTAL  forged twin row`. Both landed in the written artifact
(lines 172–173 of a 173-line file) with **`G-INTEGRITY-PRE` PASS and
`G-INTEGRITY` PASS, run completed at exit 0.** This is LOR MAJOR-5 recurring —
the disease the #267 advisory routed to this worker.

`M-TRANSCRIPT` appends `"  [PASS] G-FORGED\n"` — two spaces, non-closing name —
the one shape both clauses reject. The falsifier is calibrated to the guard
rather than to the threat, so the sweep's green badge on this gate is not
evidence.

**REPAIR R-PR-3.** Digest the WHOLE artifact text, not a prefix: take the
closing rows into a second sealed digest after `G-INTEGRITY-PRE` and compare
the full file against `prefix_digest ‖ closing_digest`; or render the expected
closing rows from the ledger and require the tail to equal them line for line.
Then re-point `M-TRANSCRIPT` at a nine-space-indented forgery.

### MAJOR-4 — THE PROVENANCE CLAIM IS UNBACKED: `READS` IS A PRODUCER-ONLY REGISTER

§13 says:

> 14 sources are read at run time, **the set of reads is required to be exactly
> the declared set**, and every reader records its category — SOURCE,
> OBJECT-UNDER-TEST, SELF or the run's own staged artifacts.

There is no such requirement. `READS` appears at exactly three lines in 4,176:
`READS = []` (296), `READS.append(...)` (304), `READS.clear()` (1571). No gate
predicate consumes it, no receipt key publishes it — grep for any category
token in `perr_receipt.json` returns 0. `read_text`'s own docstring ("so the
provenance gate holds all categories and not the pinned sources alone") is
false: `G-SOURCES` is built from the `SOURCES` loop and never touches `READS`.
This is LOR MAJOR-4's disease in its pure form — a register with a producer and
no consumer, vouched for in the paper as a gate.

The underlying property is nevertheless TRUE here: I verified by construction
that the run opens exactly the 14 sources, the paper, `SELF`, and its own two
staged artifacts, and invokes no subprocess. The defect is that nothing checks
it.

**REPAIR R-PR-4.** Publish `READS` as a receipt key and add a gate requiring
`{r["path"] for r in READS if r["category"] == "SOURCE"}` to equal the declared
source set, every category to be one of the four declared values, and the
non-SOURCE reads to be exactly the paper, SELF and the two artifacts.

### MAJOR-5 — THE HONEST DENOMINATOR IS SHORT BY THREE, AND ALL THREE ARE UNGUARDED

`G-COVERAGE-HONEST` reports **gates 47**. The run's own sealed ledger has
**49** rows (`totals.gates = 49`) and its artifact prints **50** PASS lines.
`waiver_ledger` is called on `LD.names()` before three further gates are added,
so the coverage ledger silently omits:

| gate | in the sealed ledger? | in the coverage ledger? | mutant | waiver |
|---|---|---|---|---|
| `G-COVERAGE-HONEST` | yes | no | none | none |
| `G-SWEEP-EXECUTED` | yes | no | none | none |
| `G-SEAL-TOTAL` | no | no | none | none |

All three would report **UNGUARDED** if counted. `G-SWEEP-EXECUTED` is the gate
that binds the writer to an executed sweep — precisely a load-bearing row. The
gate's own statement, "the denominator is this run's own gate count rather than
a hand-kept number", is measurably false: 47 ≠ 49 ≠ 50. `closing_gates` declares
three exclusions, but names a DIFFERENT three (`G-SEAL-TOTAL`,
`G-INTEGRITY-PRE`, `G-INTEGRITY`), so two of the omissions are undeclared. A
fourth waiver, for `G-INTEGRITY-PRE`, is declared in the `waivers` dict and can
never fire — that gate is never in `LD.names()` when the ledger is built.

**REPAIR R-PR-5.** Build the coverage ledger over the ledger rows PLUS the
declared closing gates, and give each of `G-COVERAGE-HONEST`,
`G-SWEEP-EXECUTED` and `G-SEAL-TOTAL` either a mutant or a forcing waiver.
Restate the evidence as `gates N of N`. Delete the dead `G-INTEGRITY-PRE`
waiver or move the ledger construction after it.

### MAJOR-6 — THE WALL SURFACE IS NOT "EVERY PUBLISHED RECEIPT KEY"

`G-INTERFERENCE-CLOSED`, `G-WALL-BHS` and `G-WALL-KR` each claim to scan "this
run's declared measurement surface — every published receipt key, the statement
and evidence of every gate evaluated". The surface is built once, at source
line 2882, from `R` as it then stands. Measured:

- **34 of 53** published receipt keys are in it. The 19 outside are
  `arithmetic`, `closing_gates`, `coverage`, `coverage_scan`, `falsifiers`,
  `gates`, `head_independence`, `interference`, `paper_claims`, `paper_fences`,
  `paper_tables`, `polarity`, `seal_manifest`, `sweep`, `totals`, `transcript`,
  `transcript_head`, `verdict`, `walls`.
- **32 of 49** gate rows are in it; the 17 outside include all five wall/
  interference rows, both head rows and all five paper rows.

`verdict` — the four verdict segments, the highest-stakes text the unit
publishes — is outside. A banned reading in the head would not be seen by any
of the three scanners.

The claim is not merely unmet, it is **unmeetable as worded**: rebuilding the
surface from the FULL committed receipt makes all three gates FAIL on the
unit's own clean run, because `R["walls"]["BHS"]["reason"]` contains
"sprinkling", `R["interference"]["authority"]` contains "Sidon at every", and
the gate statements contain "SPRINKLING-GRADE". That is the demonstration and
also the reason the wording cannot simply be honoured.

To be clear about what IS sound: the PAPER leg is scanned in full, and four
plants die there (INJ-12…15). The defect is the totality claim, not the wall.

**REPAIR R-PR-6.** Restate the three statements as "the census layer of this
run's receipt (34 of 53 published keys, enumerated in the receipt) together
with the statement and evidence of every gate evaluated before this one, AND
the paper's body", and publish the scanned key list as a receipt row so the
scope is data. Alternatively, move the three scans after the receipt is
complete and exempt the wall and interference rows by key — which is stronger,
because it would then cover `verdict`.

### MAJOR-7 — THE SEALED `closing_gates` WARRANT IS FALSE IN BOTH ITS CLAUSES

`R["closing_gates"]["warrant"]` is sealed and published. It says:

> The archived transcript therefore carries their rows while the sealed ledger
> does not, and a run that fails any gate writes nothing at all.

Both clauses are false.

1. **The transcript does not carry their rows.** `text = "\n".join(LINES)` is
   built at line 3944, BEFORE `G-INTEGRITY-PRE` (3953) and `G-INTEGRITY` (3988)
   are added. The delivered `perr_output.txt` carries `G-SEAL-TOTAL` and stops:
   50 PASS rows for 52 gates evaluated. Two of the three named closing gates
   appear in no artifact at all.
2. **A failing run CAN write.** `os.replace` is at 3975–3976; `G-INTEGRITY` is
   evaluated at 3988 and raises on failure. Demonstrated: a patched run
   corrupted the receipt on disk after `os.replace` and before the read-back.
   `G-INTEGRITY-PRE` **PASS**, `G-INTEGRITY` **FAIL** — correct detection — but
   the corrupt value survived on disk (`sig_feed.covered_codes = 999` where the
   census says 90), and the on-disk transcript's last row is
   `[PASS] G-SEAL-TOTAL` with no record of the failure anywhere in either
   artifact. A failing run wrote, and what it left behind is a corrupt receipt
   beside an all-PASS transcript.

This is a sealed vouching row — exactly the layer #119/#148 extended the seal
to cover — carrying two false statements.

**REPAIR R-PR-7.** (a) Append the closing rows to `text` after they are
evaluated (which R-PR-3 requires anyway), so the warrant becomes true. (b)
Restate the second clause as "a run that fails any gate before the write writes
nothing; a run that fails `G-INTEGRITY` leaves the artifacts it has just
written and exits non-zero", or write to the staging path, run `G-INTEGRITY`
against the staged bytes, and `os.replace` only after it passes.

---

## 7. MINOR FINDINGS

**MINOR-1 — two typed prose counts in §13 are unbound.** `14 sources are read
at run time` → `13 sources` survives (13 is an exempted literal, the corpus
version v13); `Eight columns are back-validated` → `Nineteen columns` survives
(19 is the window size). *Repair:* render both from `len(SOURCES)` and from the
back-validation list as `paper_claims` entries.

**MINOR-2 — `G-ANCHORS` does not enforce the second half of its own
statement.** "EVERY VERBATIM ANCHOR … NAMES THE GATE THAT CONSUMES IT" — the
`gate` field is recorded in the receipt and never checked. All 23 consumers can
be renamed to a non-existent gate, or all pointed at `G-EXACT` which consumes
none, and the gate still passes. No phantom exists today (all 18 named gates
are in the ledger, verified). *Repair:* require every anchor's named gate to be
in `LD.names()` at the close, and require every gate named by an anchor to have
been evaluated.

**MINOR-3 — spelled compound numerals are decomposed, not composed.**
`Forty-two` scans as `forty`(40) + `two`(2); it dies here only because 40 is
unbacked. A compound whose parts are both backed but whose value is not would
pass. *Repair:* fold hyphenated and `X hundred/thousand` forms before lookup.

**MINOR-4 — E-24 is a self-list.** `COUNTING-ONLY` occurs once, in §13 prose;
**0 occurrences in the receipt**, no per-quantity stamp, no `measure` key —
LOR's M7 recurring. The currencies themselves ARE named as data
(`prediction_c.currencies = ["A DECLARED RECORD", "A MOTIVATED WELD"]`) and the
counter-column is published with labelled keys under `richer_in`, so E-24's
substantive requirement is met in the receipt. Two gaps remain: (i) the
`stratum_cover` pair 9,936 → 1,842,120 sits in `richer_in` without its
denominators, which live in a different receipt key (`stratum.4.total` =
1,679,616 and `stratum.5.total` = 60,466,176) and nowhere in §4.3 — both the
raw and the density readings agree here, so nothing is wrong, but the column is
unlabelled where it is published; (ii) E-24 does not otherwise bite at all —
the unit publishes counts, and its only true fraction is the matrix entry 1/2
in the naming sentence. *Repair:* carry each `richer_in` pair with its own
denominator, and either stamp counts `COUNTING-ONLY` in the receipt or drop the
§13 sentence's "is stamped" clause.

**MINOR-5 — `--list-gates` lists 40 gates, not 49.** It enumerates
`{v[1] for v in MUTANTS.values()}` — the falsifiable gates — and includes
`G-INTEGRITY-PRE`, which is not in the ledger. *Repair:* rename to
`--list-falsified-gates` or list the ledger's own names.

**MINOR-6 — the bare-copy abort is a traceback, not a named gate.** Code alone,
and code + paper alone, both exit 1 writing nothing, but by an uncaught
`FileNotFoundError`. A reader cannot distinguish a missing source from a crash.
*Repair:* wrap the source loop and raise a named `G-SOURCES` failure.

**MINOR-7 — `pack4`'s no-carry invariant is a docstring, not a gate.** "every
budget here is below sixteen, so no cell can carry" is a correct forcing (max
budget 6), but ungated. S-3 explicitly contemplates other budgets. *Repair:*
gate `max cell count < 16` before the convolution.

**MINOR-8 — `G-SATURATION-SCHEMA`'s conjuncts are definitional.** `budget` is
defined as `per_round * ROUNDS`, `need[c]` as `len(SITES) * sum(c)`, and
`homo5` as the codes with `sum(c) == ROUNDS`, so all three clauses are
identities and only `M-SATURATION` can move them. The load-bearing empirical
premise — max 9 incidences per round — lives in `G-ARENA` and is not restated
here. The schema is still a re-proof (the arithmetic is re-run at this rung on
a measured `per_round`), but the gate does not bind it to the measurement.
*Repair:* add `per_round == max(spec)` and `spec[per_round] == nsat` to the
schema's own predicate.

**MINOR-9 — five keys are sealed in the closing block.** `gates`,
`closing_gates`, `transcript_head`, `transcript`, `totals`. `closing_gates`,
`transcript` and `totals` are consumed by the integrity gates; `gates` and
`transcript_head` are consumed by nothing but `SEAL.verify`. Compliant with
#148 (sealed, not orphaned) but worth naming, since #148 was bought by exactly
this shape. *Repair:* none required; declare the consumption in the manifest.

**MINOR-10 — the wall scan's scope is not stated in the paper.** `paper_body`
cuts §9, so a banned reading planted inside the wall section survives
(INJ-17). This is correct design — a section that NAMES an abstention must not
read as taking it — but §9 does not say that its own text is out of scope.
*Repair:* one sentence in §9.

**MINOR-11 (ledger-side, not the object).** LOG #280 records
"825+119 numerals/words". The receipt and the artifact both say **121**
number-words. The instrument is right; the ledger line is not.

---

## 8. WHAT I COULD NOT BREAK

Recorded so the panel can weigh the perimeter findings against the core.

- **Every measured quantity.** ≈ 300 independent recomputations, zero
  disagreements. The full list is in §3 and includes the alphabet (7 codes),
  the code space at R = 3/4/5/6 (54/105/181/287), the covered splits
  (44 = 41+3+0 and 90 = 84+3+3 with the indefinite codes at 4det −5), I7's box
  (361 admissible, 181 even / 180 odd, exactly 6 points at count-sum 5), the
  parity law record by record (9/9, with q₁₂ integral 9/9), the whole R = 5
  stratum, the R = 6 door, the DIA law (13/13 with the count clause alone at
  12/13, falsified exactly at [2,2,2]), and the locking theorem.
- **The singular witness — the object the headline rests on.** Rebuilt from its
  own published groupings by an independent route: covers 27/27, 41 incidences,
  max cell 4, per-round [7,7,9,9,9], 3 saturating, all nine site codes
  identical to the receipt, exactly one singular site at (1,1,4) with 4det 0.
- **Byte reproduction.** Both artifacts byte-identical to the committed sha256
  at `PYTHONHASHSEED` 0 and 99991, in two independently provisioned off-tree,
  git-less mirrors. No subprocess is invoked; no repository state outside the
  declared 14 + paper + SELF is read.
- **The CLI.** 16/16 hostile forms exit 2, arity and second-mode-flag included.
- **`--selftest` writes nothing**, proved by a whole-tree hash computed outside
  the instrument.
- **E-22 on fences, cells and spans.** 4/4 fence attacks, 4/4 cell forgeries,
  2/2 span forgeries die.
- **The paper-scanning walls.** The #267 disease is genuinely fixed here, and
  the LOR §269 caveat — "a green sweep is not evidence a wall holds" — is
  discharged: the plants die on the paper leg.
- **E-23 description honesty.** 15/15 sampled descriptions match their hooks.
- **The exhaustiveness licences.** Both sound; the 280⁵ reduction validated by
  full brute force at R = 3 and the 36⁵ convolution by a nibble-free rebuild.
- **The sweep-to-writer binding.** `G-SWEEP-EXECUTED` + the `swept` conjunct of
  `G-INTEGRITY` cannot be separated from the write.

## 9. THE SEAM RULING

**MAJOR-1, MAJOR-3, MAJOR-4, MAJOR-5, MAJOR-6 and MAJOR-7 are
TEMPLATE-SHAPED, not PER-R-shaped.** Every one is a property of the shared
instrument skeleton: unrendered table headers, a whitelist-based transcript
tail, a producer-only `READS` register, a coverage ledger built one call too
early, a wall surface snapshotted mid-run, and a warrant written before the
code it describes. LOR's K3 found four of these six in a sibling unit built
from the same template; PER-R was written under that advisory and fixed the two
that were named explicitly (paper-scanning walls, full-table rendering on
CELLS) while inheriting the rest. **The corpus sweep the #267 review
recommended should now run, and these six are the rows to sweep for.**

**MAJOR-2 is PER-R's own**, and it is the only finding that puts a false
sentence in the paper. It should be repaired in this unit regardless of the
sweep.

Nothing here touches a measured number, a verdict, or the licensed reading of
the rung. The three breaks, the parity law, the locking theorem, the R = 6 door
and the dictionary row all stand exactly as delivered.
