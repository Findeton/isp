# SIG (paper-24) — INSTRUMENT-LENS HOSTILE REVIEW (K3)

**Seat:** INSTRUMENT (K3). **Object:** `v14/paper-24-sig.md` and its
instrument, at commit `025c4a6`. **Era:** post-engraving-native — HANDOFF §4,
RUNBOOK E-22, E-23, E-24 and the §14 addenda applied without discount.

## 0. Hash verification, start and end

| object | declared sha256-12 | start | end |
|---|---|---|---|
| `v14/paper-24-sig.md` | `72175d6fa85b` | verified | verified |
| `v14/code/sig_exact.py` | `a41b6d549e14` | verified | verified |
| `v14/code/sig_output.txt` | `f28b550c151e` | verified | verified |
| `v14/code/sig_receipt.json` | `ca9cd4ceb387` | verified | verified |
| `v14/note-sig-pin.md` (pin) | `ab73239daff5` | verified | verified |

All five blobs are identical at `025c4a6` and at `HEAD`, and `git status` on
them is empty after this review. Every execution was off-tree, in two
independent `git archive 025c4a6` provisionings plus one bare copy. The
siblings' uncommitted files were never read; they are disclaimed.

## 1. GRADE — **AWF** (accept with fixes)

**Nothing this unit computed is wrong.** 175 independent recomputations —
including a from-the-prose rebuild of the coupled walk, an independently
derived pruning licence, and a full re-derivation of the horizon-6 extension —
disagreed with the delivered artifacts **zero** times. Both prunes are
theorems and I proved both exhaustively rather than accepting them. The
outcome word `SIG-BLOCKED-AT-THE-EMISSION-READING` is the honest reading of
the numbers, and the arithmetic is exact end to end.

**What fails is the instrument's account of itself.** Eighteen hostile
injections were run against the pristine object: **twelve survived at exit 0**,
six controls died on their named gates. The twelve are one kind of defect,
repeated: a gate, a normaliser or a manifest field that *names* a discipline
it does not enforce. Seven published compliance claims are claims the
instrument's own comparators cannot make — including two whose engraving
(E-23, #82) this era bought with earlier blood.

## 2. Counts

**Executions — 89.**

| kind | n |
|---|---|
| off-tree delivery runs (2 provisionings × 2 `PYTHONHASHSEED`) | 2 |
| bare-copy run (no repository present) | 1 |
| `--selftest` | 2 |
| CLI probes (24 hostile argv + 4 exit-code contract + 2 list modes) | 30 |
| cold **out-of-harness** `--mutant` processes | 17 |
| in-process pipeline runs under injection (2 warms + 18 injections) | 20 |
| independent analysis / recomputation programs | 14 |
| independent whole-subtree hashings | 3 |

**Recomputations — 175, zero disagreements.** Static census 14; region floors
4; dynamic Grover census 30 (both readings, both measures, per-step totals);
prune and extension 21; coin fiber 25; pruning licences 4; denominator
factorisations 6; paper numeral sweep 6; seal map 33; anchor maps 20;
allow-list forensics 3; comparator-overlap measurement 4; ledger arithmetic 5.

## 3. The disease sweep

| # | disease (my brief) | verdict | demonstration |
|---|---|---|---|
| 1 | phantom consumers (10+10+10 anchors, 33 seals) | **PRESENT** — all 10 verbatim consumers are labels; 1 path anchor unconsumed; 7 seal stamps name gates that never read the sealed object | INJ-15; source trace of every use of `vrows`/`arows` |
| 2 | referent-binding (the OCC lesson) | **PRESENT** at one head row and one label; the four static class names themselves are correctly bound | INJ-12; §8 vs §6.2 |
| 3a | constant-boolean falsifiers | **PRESENT** — the clause reads `pick`'s *normal* argument, not the corruption | AST probe: `pick(N, ok, False)` → not flagged; `pick(N, True, f())` → flagged |
| 3b | E-23 description-vs-code | **PRESENT** at 1 of 38 | MUT-CLEARING (see MINOR-3) |
| 3c | sweeps bound to executions | **ABSENT** | 17 cold `--mutant` processes, 17/17 ON TARGET, artifacts unchanged each time |
| 4 | seal windows (33 at value-close?) | **PRESENT** — value drift between gate and seal is undetected | INJ-13, INJ-14 |
| 5a | E-22 tables render as claims | **PRESENT** for 2 of 5 tables | INJ-01/02/03 survive; INJ-04/05/06 die on target |
| 5b | E-22 inline spans; fences by TRUE multiset | **ABSENT** | INJ-09 dies; fences multiset-matched 8 = 4 segments × 2 |
| 5c | no blanket whitelists | **PRESENT** — 18 numerals allowed only by hex-digest digit-runs | INJ-16 |
| 6 | **the pruning theorem's gate** | licence **SOUND** (proved, not accepted); the gate is **PROXY** in one place | brute force + independent horizon-6 re-derivation |
| 7 | the 2,197 two-route independence | **PRESENT** as prose overstatement; no shared intermediates | source trace: `q_of` called at exactly one site |
| 8 | E-24 (ratio stamps, denominators) | **ABSENT** | 6 fractions recomputed and refactorised; both measures sum to exactly 1 |
| 9 | vacuous clauses | **PRESENT** — 7 named | source trace |
| 10 | CLI + `--selftest` write-nothing | **ABSENT** | 30 probes all exit 2/0/1 per contract; independent whole-subtree hash |
| 11 | byte ×2 off-tree; bare-copy loud abort | **ABSENT** | both seeds byte-identical to the committed artifacts; bare copy exits 1, writes nothing |
| 12 | full numeral sweep | **ABSENT** | 597 tokens, 67 distinct, 0 unbacked; 18 fractions all in the receipt |

## 4. The injections table

Every injection ran the **pristine** object off-tree; nothing was written
anywhere. "SURVIVED" means the whole pipeline reached its close at exit 0 with
the corruption in place.

| id | corruption | outcome | reading |
|---|---|---|---|
| INJ-01 | §3.2 nested-classes table: swap the `full site` and `covering` budgets (R = 5 ↔ R = 6) | **SURVIVED** | the table is ungated |
| INJ-02 | §3.2: swap the `unrestricted` and `full site` rows entirely | **SURVIVED** | same |
| INJ-03 | §9 choice inventory: item 7 `declared, VERDICT-DETERMINING`/fiber 2 → `forced`/fiber 1 | **SURVIVED** | the inventory that carries the outcome word's own justification is ungated |
| INJ-04 | §3.3 covering ladder: `\| 5 \| ALL \| NO \|` → `YES` | killed at **G-PAPER-TABLES** | control — gated table |
| INJ-05 | §4.2 arena table: A4 first-indefinite 5 → 4 | killed at **G-PAPER-TABLES** | control |
| INJ-06 | §7.1 coin table: `W`'s Born mass → GROVER's | killed at **G-PAPER-TABLES** | control |
| INJ-07 | prose: insert `see § 4242 for the residual` | **SURVIVED** | `SECREF` deletes `§ <digits>` before the scan |
| INJ-08 | insert heading `## 4242. A forged section` | **SURVIVED** | `HEADNUM` deletes leading heading numerals |
| INJ-09 | prose: insert inline span `` `4242` `` | killed at **G-PAPER-COVERAGE** | control — inline spans are scanned (E-22 leg healthy) |
| INJ-10 | §6.2 gloss `roughly a tenth` → `roughly a half` | **SURVIVED** | ungated gloss (measured ratio ≈ 0.1053) |
| INJ-11 | §6.2 gloss `Nearly three times` → `Nearly nine times` | **SURVIVED** | ungated gloss (measured ratio ≈ 2.881) |
| INJ-12 | make the R = 1 field non-homogeneous (`r1_codes` = `[[1,0,0],[1,1,1]]`) | **SURVIVED**, head still emits `INDEFINITE AT 9 OF 9 SITES` | the quantifier is `NSITE`, typed |
| INJ-13 | corrupt `R["mutants"][0]["what"]` **after** G-FALSIFIER-HONEST passed, before its seal | **SURVIVED** | the seal binds the drifted value, stamped `sealed_at_gate: G-COVERAGE` |
| INJ-14 | corrupt `R["walk"]["exit_A"]` **after** G-WALK-ANCHORED passed, before SEAL-WALK | **SURVIVED** | same class; the stamp names a gate that never saw the value |
| INJ-15 | replace V-P21-BUDGET's needle with an unrelated true paper-21 quotation, consumer unchanged | **SURVIVED** | the consumer field is a label, not a consumer |
| INJ-16 | prose: insert `the residual is 24591 at the seam` (24591 occurs only inside a sha256-12 hex digest) | **SURVIVED** | allow-list contaminated by hex digits |
| INJ-17 | force no arena to reach the indefinite region | killed at **G-STAGE0-DYNAMIC** | the gate's own sealed statement says the head "would read SIG-BLOCKED-AT-REACHABILITY" — it would not; the run dies |
| INJ-18 | force both emission readings to agree | killed at **G-POLARITY-B** | `SIG-AVOIDED`/`SIG-SELECTED` are undeliverable |

**Cold out-of-harness falsifier sweep (17 of 38, chosen to cover every
memoised object and every late gate).** MUT-HERON, MUT-ANCHOR-VALUE,
MUT-VERBATIM, MUT-MEMO, MUT-FALSIFIER-DESC, MUT-SPECTRUM, MUT-DEPOSIT-MAX,
MUT-TRANSITIVE, MUT-FLOOR, MUT-R5, MUT-R6LIVE, MUT-WALK-ANCHOR, MUT-PRUNE,
MUT-CLEARING, MUT-POLARITY-A, MUT-MOD3, MUT-SEAL-DROP — each a **separate cold
process** with an empty memo, each killed by its own named gate, exit 1,
artifacts byte-unchanged after every one. The in-process sweep's ON-TARGET
column is therefore not an artefact of the shared cache.

## 5. MAJOR findings

### MAJOR-1 — E-23's constant-boolean clause reads the wrong argument and can never fire

`mutant_hooks` (line 1892) sets

    const = (f.id == "pick" and len(node.args) > 2
             and isinstance(node.args[1], ast.Constant)
             and isinstance(node.args[1].value, bool))

`pick(name, normal, corrupted)` — `args[1]` is the **normal** value, `args[2]`
is the corruption. Measured on a probe: `pick("M", ok, False)` (the corruption
*is* a constant boolean — the named disease) → `constant_boolean = False`;
`pick("M", True, compute())` → `True`. So G-FALSIFIER-HONEST's published
statement, "REJECTS any falsifier whose corruption is a constant boolean", and
§12's repetition of it, are compliance claims the comparator cannot make.
No declared mutant reaches the clause either, so it is also unfalsified —
RUNBOOK §14 addendum: *a compliance gate whose comparator cannot disagree with
the object under test is vacuous by construction*.

**Repair.** Test `node.args[2]`. Add a declared falsifier that introduces a
`pick(NAME, <computed>, False)` hook and is required to die at
G-FALSIFIER-HONEST. Correct §12.

### MAJOR-2 — G-VERDICT-RECONSTRUCTED's shared-literal clause is vacuous, and the comparator *is* the builder's prose typed twice

`template_constants` skips every string constant that is an `ast.Attribute`
value. `reconstruct` builds all four templates as `"...".format(...)`, so all
four are stripped before the scan. Measured: `build_verdict` contributes 7
constants (4 numeral-bearing); `reconstruct` contributes 4 (**0**
numeral-bearing); the intersection is `{"%s:%s"}` and the numeral-bearing
intersection is empty **by construction**, not by independence.

Worse, the thing the clause exists to catch is present. Normalising placeholder
syntax (`%d`/`%s` and `{name}` → `@`), the builder's entire 2,086-character
template skeleton is a **contiguous substring** of the comparator's
(similarity 0.9424, longest common run 2,086 of 2,086). That is the #82
amendment's named failure mode verbatim: *"the same concatenation written
twice"*.

**Repair.** Skip only `ast.Subscript` slices and `Call` keyword constants —
never `.format()` receivers — so the comparator's templates enter the scan.
Then either re-derive the head through a genuinely different phrasing, or drop
the textual-independence claim and state G-VERDICT-RECONSTRUCTED for what it
is: a **value-level** re-derivation of the outcome word (that part is real —
`reconstruct` re-derives the word from the serialized receipt's own rows
through its own conditional, and MUT-VERDICT dies there).

### MAJOR-3 — E-22 "tables render as claims" is discharged for 3 of 5 tables

`paper_tables` renders 16 rows: the covering ladder (§3.3), the arena floors
(§4.2) and the coin fiber (§7.1). It does **not** render the §3.2 four
nested classes table or the §9 choice inventory. Every numeral in both is in
the allow-list, so their rows can be permuted at exit 0 — INJ-01, INJ-02,
INJ-03. INJ-03 is the sharpest: the choice-inventory row that identifies
**item 7 as the one verdict-determining declaration** — the row the outcome
word `SIG-BLOCKED-AT-THE-EMISSION-READING` rests on — can be relabelled
`forced`, fiber 1, and the instrument certifies the paper clean.

**Repair.** Render both tables from the receipt into `paper_tables` (the class
table from `static.{r1,fullsite,covering,live}`; the inventory's class/fiber
columns from a declared inventory object), and require each row exactly once.

### MAJOR-4 — the coverage allow-list is contaminated by sha256 hex digests

`receipt_numbers` walks `provenance`, whose values are sha256-12 hex strings;
`NUMTOK` (`\d[\d,]*...`) harvests their digit-runs. 29 such tokens enter the
allow-list; **18 are backed by nothing else in the run**: `190`, `24591`,
`286`, `299`, `35`, `4538`, `4824`, `542`, `543`, `55273`, `6068`, `66`,
`7019`, `73`, `73239`, `814`, `8735`, `93`. Any of them may be written into
the paper as a measured quantity and pass G-PAPER-COVERAGE — INJ-16.

**Repair.** Exclude `provenance` and the `anchors` digest fields from
`receipt_numbers`, or drop tokens whose surrounding characters are hex.

### MAJOR-5 — the verbatim anchors' "consumer gate" is an unread label

`R["verbatim_anchors"]` is touched in exactly three places: the G-VERBATIM
existence check, SEAL-VERBATIM, and G-ANCHOR-CONSUMERS — which reads only the
gate **name**. Not one of the nine named consumer gates ever reads a needle:
G-WALK-ANCHORED compares against the *path* anchors, G-DEPOSIT-THEOREM against
`P-P21-SPECTRUM`, G-STATIC-LADDER against its own computed floor, G-WALL-BHS
against a keyword list. INJ-15 swaps V-P21-BUDGET's needle for an unrelated
true quotation from the same source, keeps its consumer, and the run survives.
This is the §14 amendment (v14 #62) by name: *"An anchor whose consumer is an
unread label binds existence, not meaning."*

**Repair.** Each anchor names the quantity it quotes; the consumer gate parses
that quantity out of the needle and compares it against its own measurement
(e.g. G-DEPOSIT-THEOREM reads `9` out of V-P21-BUDGET and compares against the
measured spectrum maximum). Ship one mutant per anchor that changes the quoted
*value* to another true sentence and dies at the consumer, not at G-VERBATIM.

### MAJOR-6 — the pin's other pre-registered outcomes are undeliverable, and one gate's sealed statement says the opposite

G-STAGE0-DYNAMIC's published statement reads: *"Had this gate found no arena,
the head would read SIG-BLOCKED-AT-REACHABILITY and no polarity word would be
emitted."* Its predicate is `bool(live) and consistent`. INJ-17: with no arena
reaching the region the run **dies at G-STAGE0-DYNAMIC** and writes nothing —
no head at all. The statement is false about its own gate, and it is sealed
(SEAL-GATES) and published in both artifacts.

The same holds downstream. G-POLARITY-A requires `word == "AVOIDED"`,
G-POLARITY-B requires `== "SELECTED"`, G-FORCEDNESS requires
`not readings_agree`. INJ-18 (both readings agree) dies at G-POLARITY-B. Of
the pin's five pre-registered outcomes exactly **one** is deliverable;
`outcome_word`'s two other branches and `reconstruct`'s reachability branch
are dead code that can never execute in a run that closes.

This does not make the delivered verdict wrong — the measurements are right
and I reproduced them — but "45 of 45 gates PASS" is not evidence *for* the
verdict, because the gates encode it.

**Repair.** Move the answer-encoding conjuncts out of the gates and into the
pre-registered polarity table (which already exists and already carries
PL-REACH / PL-FORCED-READING / PL-FORCED-COIN honestly). Restate
G-STAGE0-DYNAMIC's statement to describe what it does: *"a run that finds no
arena fails here and writes nothing; the BLOCKED-AT-REACHABILITY head is a
pin-level outcome this instrument does not implement."*

### MAJOR-7 — the object under test is not recorded in the sealed surface

The paper is the one runtime input with neither a path nor a hash anywhere in
the receipt: `paper-24-sig.md` does not occur in `sig_receipt.json` at all.
`paper_rel` is threaded through four signatures (1909, 2231, 2233, 2290, 2546)
and **never consumed**; `--verify-paper PATH` computes it and discards it.
G-READS-DECLARED checks only that the SOURCE set has 10 members. So the paper
gates certify agreement with *a* file, and the sealed record does not say
which. Under #119 totality and §14's path-value addendum this is the one
uncovered read.

**Repair.** Publish and seal
`object_under_test = {"path": paper_rel, "sha256_12": digest(paper_text)}`,
add it to `MEASURED_KEYS`, and have G-READS-DECLARED require exactly one
OBJECT-UNDER-TEST read at that path.

## 6. MINOR findings

**MINOR-1 — §2.1's two-route claim overstates.** "Every determinant in this
unit is computed by two routes that share no expression" is false as written:
`q_of` (route 1) is called at **exactly one site**, inside the
G-REGION-ARITHMETIC comparison over the 2,197-code box. Every determinant that
carries a measurement — `region_of`, `record_region`, `static_floors`, both
static searches, the collinear ladder, the naming sentence — uses `det4_of`
alone. The two routes share no intermediate, so the comparison is honest; the
claim about *every* determinant is not. (I verified the box does cover every
code the run evaluates: the maximum cell reached anywhere is 11, box 12.)
*Repair:* "the two routes are proved equal over the whole 2,197-code box, and
every determinant below is then taken by the symmetric form."

**MINOR-2 — "9 OF 9 SITES" is typed, and the R = 1 row has no gate.**
`ST["r1"]["sites"] = NSITE`; the measured per-site census
`r1_sites_indefinite` is computed (line 791), published, and never read.
`ST["r1"]["region"]` reads only `sorted(codes1)[0]`. INJ-12 makes the R = 1
field carry two distinct site codes and the head still asserts "INDEFINITE AT
9 OF 9 SITES" at exit 0. No gate binds the R = 1 row at all — it is bound only
to the frozen paper through claim C-R1, and C-R1 does not carry the quantifier.
*Repair:* derive `sites` from the per-site census and add a gate requiring all
nine site codes to be identical and indefinite. This also contradicts §12's
"Counts are computed, never typed."

**MINOR-3 — MUT-CLEARING's published description is false (E-23 leg 1).** It
declares that it "selects a clearing arena whose indefinite mass is zero". The
hook selects `pairs[-1]` = A5, whose indefinite masses are
`367635432032/7625597484987` (Born) and `269625780848/1016978783625` (record)
— both positive, both in the receipt. The kill comes from the
`no_new_declaration` and `len(free) == 1` conjuncts, not from a zero mass.
G-FALSIFIER-HONEST cannot see this: it only requires the named object
(`chosen`) to occur in the hook's source. *Repair:* reword to "selects the
last clearing pair, which is not the no-new-declaration one"; the other 37
descriptions I checked against their hooks are accurate.

**MINOR-4 — `sealed_at_gate` is a narrative field.** SEAL-WALK is stamped
`G-WALK-ANCHORED` but is taken after G-WALK-STOCHASTIC has added
`stochastic_checks`/`stochastic_violations` to the same object; SEAL-MUTANTS is
stamped `G-COVERAGE` although `R["mutants"]` is gated ~1,040 lines earlier at
G-FALSIFIER-HONEST; SEAL-SCHEMA, SEAL-COUNTS, SEAL-CLOSING, SEAL-TOTALS and
SEAL-TRANSCRIPT name gates whose predicates never examine the sealed path.
INJ-13/INJ-14 show the consequence: a value that drifts between its gate and
its seal is sealed in its drifted state and the close verifies clean — the
#119/#148 class ("satisfied at gate time, vacated at delivery time"). *Repair:*
take each seal in the same statement as the gate that vouches for it, and let
`sealed_at_gate` be filled from the gate row rather than typed.

**MINOR-5 — the closing-gate declaration is incomplete and `totals.gates` is
off by one.** 45 gates are evaluated; `R["gates"]` carries 42;
`closing_gates.names` lists 2 of the 3 missing — **G-READS-DECLARED is absent
from both**. `totals.gates` publishes 41 for a 42-row array. The published
transcript ends at G-SEAL-COMPLETE and never records G-READS-DECLARED or
G-ARTIFACT-INTEGRITY, the two gates whose passing is the precondition for
writing. *Repair:* add G-READS-DECLARED to `closing_gates.names`; set
`totals.gates = len(R["gates"])`.

**MINOR-6 — the pruning licence constant is an ungated one-coordinate probe.**
`run_pruned` computes `need` by growing **only cell index 2** of the base code
until the site leaves POSDEF. I verified by exhaustive search over all growth
vectors that this equals the true minimum max-increment for all three declared
bases — 3, 2, 1 for (1,1,1), (1,1,2), (1,1,3) — so the delivered prune is
sound. But nothing in the run checks that coincidence, and the docstring cites
"the region floor of section 4", i.e. `static_floors`, a different object
computed elsewhere and never compared to `need`. A base where growing another
cell were cheaper would make the prune silently unsound. *Repair:* gate `need`
against `static_floors`, or against a finite exhaustive check that no growth
vector with max increment `< need` leaves POSDEF.

**MINOR-7 — G-NULL-MEASURE claims per-object binding it does not do.** Its
statement says both measures are checked "at every step of every reading, per
object rather than in aggregate". The check sums per-region masses at each
**level** (10 level totals) on the clearing arena's two arms only. The
per-branch normalisation is checked elsewhere (G-WALK-STOCHASTIC, 23,225
checks) and only for the emission weights — the null measure is never checked
per branch. *Repair:* state it as a level-total check, or add the per-branch
null check.

**MINOR-8 — §12's self-test claim is false.** "The self-test clears the cache
and is required to record misses." `selftest()` clears the memo, then dies at
G-PROVENANCE — the **first** gate, upstream of every memoised object — records
0 misses, and returns 1 regardless; no miss requirement exists anywhere. The
printed line honestly says "reached it 0 times", so the code discloses what the
paper asserts away. *Repair:* either add the requirement (e.g. break an anchor
whose gate fires after the first census) or reword to match the printed line.

**MINOR-9 — the mod-3 instrument's two arms run at different horizons and the
record-menu denominator is mispaired.** `path_map(4, …)` for the Born menu (12
maps) and `path_map(3, …)` for the record menu (9 maps). Each receipt row
carries `levels: 4`, `identical_A: 4`, `identical_B: 0` — a reader takes 0 of
4, but the record-menu comparison had only 3 levels. §7.2's "the same
comparison under the record menu" is not the same comparison, and the head's
"AT NONE UNDER THE RECORD MENU" publishes no denominator (#34: honest
denominators). *Repair:* run both at the same horizon, or publish
`levels_B` beside `identical_B`.

**MINOR-10 — vacuous and dead published items (7).** (a) `pruned_mass` in
`run_pruned` — assigned and accumulated, never read. (b)
`clearing.alt_arena/alt_horizon/alt_R` — published, never gated, never used in
head or paper. (c) `static.r1_sites_indefinite` — computed, published, never
read (see MINOR-2). (d) path anchor `P-P21-DET` — verified at G-ANCHORS-READ,
no downstream consumer. (e) `paper_rel` — see MAJOR-7. (f) the `SECREF`
normaliser — **no `§` occurs anywhere in the paper**, so it is dead on this
object and is simultaneously a live escape (INJ-07). (g) `HEADNUM` strips
leading heading numerals with no compensating check (INJ-08); the 39-token gap
between my independent count (597) and the unit's (558) is exactly the 26
numbered headings. *Repair:* consume or delete (a)–(e); add "`§ N`" and
"heading numeral" to the declared exemption table so they must fire and are
counted, rather than being deleted before the scan.

**MINOR-11 — the polarity label is defined against the wrong measure.** §8:
"SELECTED and AVOIDED in this unit mean one thing and nothing more: **the Born
branch measure** puts more or less mass on a declared subset of records than
the uniform-on-support counting measure on the same tree." But §6.2's SELECTED
is the **record menu's** branch measure against the same null; the receipt key
is literally `born` under both readings. Given that this unit's whole outcome
is that the two menus disagree, the naming paragraph must not name one of them.
*Repair:* "the emission tree's own branch measure under the reading in force".

**MINOR-12 — two boxes are both called "the declared box".** G-REGION-ARITHMETIC
scans 0…12 (2,197 codes, published as `code_box`/`codes_checked`);
`static_floors` scans 1…12 (1,728 codes, unpublished). §3.2's "Both are
measured over the declared box" reads as one object. *Repair:* publish the
floor search's box.

## 7. What I could not break

This section is as load-bearing as the last two.

- **Byte ×2, off-tree and git-less.** Two independent `git archive 025c4a6`
  provisionings, `PYTHONHASHSEED=0` and `PYTHONHASHSEED=987654`, each produced
  `sig_output.txt` = `f28b550c151e…` and `sig_receipt.json` = `ca9cd4ceb387…`
  — byte-identical to the committed artifacts. The #160 tie-break exposure does
  not bite: no `sorted(key=repr)` over unordered containers appears.
- **Bare copy aborts loudly.** `sig_exact.py` alone in an empty tree: exit 1,
  `[CLI] missing source: …paper-24-sig.md`, nothing created.
- **`--selftest` writes nothing, proved independently.** Whole-subtree hash of
  `v14/ v13/ v11/` identical before and after
  (`c57c4b516edd…`), and a repo-wide `find -newer` shows no file created
  anywhere. The memo-clearing claim is true (`MEMO.clear()` runs) and its own
  printed line discloses that the corrupted run dies upstream of every memoised
  object — the disclosure is honest even though the property is untested
  (MINOR-8).
- **CLI, including arity beyond the six documented modes.** 24 hostile argv
  cases all exit 2 — unknown flags, `-x`, `---numbers`, `--numbers=1`,
  `--list-gates extra`, two mode flags in either order, `--mutant` with no
  name / an unknown name / two names, `--break-anchor` with two anchors,
  `--verify-paper` with a directory / a nonexistent file / two paths, the empty
  string, `--`, and case variation. Contract exit codes confirmed: killed
  mutant → 1, `--break-anchor` → 1, `--list-gates` → 0, non-file
  `--verify-paper` → 2. Artifacts unchanged across the entire battery.
- **The falsifier sweep is bound to real executions.** 17 falsifiers re-run as
  cold separate processes, 17/17 killed by their own named gate.
- **The coverage denominator is honest.** 34 gates with a mutant + 11 waived =
  45 evaluated, no overlap, no registry drift — recomputed independently.
- **The pruning theorem.** Both prunes are theorems and I proved them rather
  than accepting them. Static (`exists_covering_indefinite`): over all 5,832
  states (n₀,n₁,n₂ ≤ 8, rem ≤ 7) there is **no** state where the prune fires
  while an indefinite completion is reachable. Dynamic (`run_pruned`): the
  licence is exactly the floor theorem, `need` is the true minimum
  max-increment for all three bases, and the cross-check is **not vacuous** —
  at the shared horizon the pruned engine retains 1,316 of 35,381 branches and
  still reproduces both masses.
- **The horizon-6 extension, re-derived independently.** I rebuilt the coupled
  walk from the paper's prose (never importing the unit), re-anchored it on
  paper-20's committed exit probability `927415552/847288609443`, derived my
  own pruning licence from the floor theorem, and reproduced the extension row
  for row: retained 3 / 27 / 486 / 10,527 / 72,199 / 109,210; SINGULAR
  `927415552/847288609443` at t = 5 and `5219452727662592/450283905890997363`
  at t = 6; INDEFINITE `5526190575616/150094635296999121` first positive at
  **t = 6**. Every number identical.
- **The polarity census and the whole coin fiber.** Independently recomputed at
  the clearing arena: Born `146623744/847288609443` vs null
  `148895641/90632341800`, ratio `675143691622400/6409469116243161`; record
  `5072320/1162261467` vs `53/34992`, ratio `81157120/28166373`; branch counts
  284,078 and 314,928; both measures sum to **exactly 1** at all ten steps. All
  five coins exactly unitary; all 10 masses, all 10 null masses and all 10
  polarity words reproduced.
- **The static census.** 280 partitions; spectrum `0:1, 4:27, 6:54, 7:162,
  9:36`; max 1 per cell and 2 per site per round; 36 saturating partitions all
  foreign-free; pool 70; **16,108,764** multisets (also `C(74,5)` in closed
  form); minimum uncovered **2**; **2,210,000** full-site multisets. All
  reproduced from an independent implementation.
- **E-24.** Every published fraction carries its measure in the head; the six I
  refactorised are all in (0,1] with sane denominators (3²⁵, 3¹⁹, 3¹⁷, 3³⁶,
  2⁴·3⁷, 2³·3⁹·5²·7·11·13·23) and the two ratios are exactly born/null. No
  count is presented as a probability without its measure.
- **The numeral sweep.** 597 numeral tokens in the paper (67 distinct), **zero**
  absent from both output and receipt; all 18 fractions present verbatim in the
  receipt; 8 fenced blocks = the 4 verdict segments twice each, byte-exact; the
  transcript's verdict lines identical to the receipt's segments.
- **Inline spans and fence multisets** (E-22's other two legs) are genuinely
  enforced — INJ-09 dies, and the multiset gate is the reason a forged twin
  cannot hide behind a clean copy.

## 8. The seam ruling

**The seam of this unit is not between its numbers and the world — it is
between its measurements and its description of its own instrument.**

Everything downstream of a measurement is sound: the censuses are exhaustive
over the objects they name, the prunes are theorems, the arithmetic is exact,
the head is derived from the receipt and re-derived from the serialized
receipt, and the whole thing byte-reproduces off-tree at two hash seeds. I
attacked the hardest object in the brief — the pruning gate's licence — with an
independent rebuild and an exhaustive proof, and it held completely.

What does not hold is the layer that tells a successor what was checked. Seven
sentences in the sealed surface assert enforcement that does not exist: the
constant-boolean rejection (MAJOR-1), the shared-literal independence
(MAJOR-2), "tables render as claims" (MAJOR-3), "exactly three declared lists"
(MAJOR-4), "each naming the gate that consumes it" (MAJOR-5), "the head would
read SIG-BLOCKED-AT-REACHABILITY" (MAJOR-6), "the self-test is required to
record misses" (MINOR-8). Each is individually small; together they are the
unit's characteristic defect, and it is the one this seat exists to find,
because a successor inheriting this instrument would inherit seven guarantees
it does not provide.

A second, narrower seam is worth naming for the adjudicator rather than the
repair worker: **the instrument can deliver only one of the pin's five
pre-registered outcomes.** That is not a defect in the measurement — the
measurement really does show the two menus disagreeing, and I reproduced it —
but it means the "45 of 45 PASS" line is a statement about reproduction, not
about confirmation, and the paper should not be read as though the gates
tested the verdict.

## 9. #91 at my own hands

Everything in this review was computed off-tree. The two delivery runs, the
bare-copy run, the self-test, the CLI battery and the 17 cold falsifier
processes ran inside `git archive 025c4a6` provisionings in the scratch
directory; the 18 injections ran in-process against those same pristine bytes,
writing nothing anywhere. My independent walk, extension, coin-fiber, static
and E-24 recomputations share no code, no import and no typed literal with the
unit — they were written from the paper's prose and anchored on the *parents'*
committed rows, not on this unit's. Every number I report as "reproduced" was
produced by that independent chain before I compared it. The five object hashes
were verified at the start and again at the end of this review, and the git
blobs are identical at `025c4a6` and at `HEAD`; my only repository write is
this file.
