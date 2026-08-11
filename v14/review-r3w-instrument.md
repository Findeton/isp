# R3-WELD / paper-19 — INSTRUMENT-LENS HOSTILE REVIEW (K4, the era audit)

**Reviewer** instrument. **Object** paper `c669ab35e12a`, code `7a84aa27de8d`,
output `76ef29488b60`, receipt `03670731ba1c` at commit `ddcd475`; pin
`20fba9b15f5e`. **Protocol** v14 ledger #163, row K4. All five object hashes
re-verified at the head of this review and again at its close; working tree
clean; `git diff ddcd475 HEAD` over the four object files is empty. Read-only
git throughout. One repo write: this file.

**GRADE: ACCEPT-WITH-FIXES (AWF).**

The delivered numbers survive everything I could throw at them. Three findings
are instrument-side gaps between what §10 claims and what the gates do; none
moves a measured number, and all three are liftable in under fifty lines.

---

## 0. THE #91 SETTLEMENT — **CLOSED, BY BYTE-IDENTITY**

The disclosed anomaly (#162: "the off-tree/git-less leg ran the full pipeline
but failed at G-MUTANTS-ON-TARGET on an accounting defect the final code fixes
— NOT re-executed against the final code") is **settled and closed**. I re-ran
it myself against the committed code.

| leg | how |
|---|---|
| off-tree | a mirror at `…/scratchpad/r3w-in/mirror/` holding **exactly** the 13 pinned sources + the code + the paper, and nothing else |
| git-less | no `.git` anywhere in the mirror and none in **any ancestor** of the mirror path (scanned to `/`) |
| hostile PATH | `env -i PATH=/nonexistent-hostile-path HOME=/nonexistent LANG=C` — no `git`, no shell tool, nothing resolvable |
| fresh seed | `PYTHONHASHSEED=random`, `PYTHONDONTWRITEBYTECODE=1` |
| what ran | the **plain delivery run** — the full pipeline, the paper gates, the 59-mutant in-process sweep, the writers |

**Result: exit 0, empty stderr, 68 PASS, 0 FAIL** — including
`G-MUTANTS-ON-TARGET`, the exact gate that failed in the worker's aborted
attempt — and the artifacts written into the mirror are **byte-identical to
the committed ones**:

```
off-tree  r3_weld_output.txt   76ef29488b60      committed  76ef29488b60
off-tree  r3_weld_receipt.json 03670731ba1c      committed  03670731ba1c
```

The mirror after the run contains no file the declaration does not name. The
anomaly closes at the strongest available standard: not "it ran off-tree" but
"it reproduced the committed bytes off-tree, git-less, on a hostile PATH,
under a different hash seed." **#91 is evidenced end to end. Finding: none.**

---

## 1. THE SEAM RULING

> **The seal binds the artifact to the run completely and binds the run to the
> paper only through the outcome WORD. Everything a gate certifies is sealed
> and externally recomputable; what is not bound is (a) the head's own
> template, which the comparator shares with the builder, and (b) every
> numeral of the paper's verdict blocks, which the numeral gate never scans.
> The seam is therefore not in the measurements and not in the transport — it
> is exactly one layer wide, and it lies between the head as a *string* and
> the head as a *derivation*.**

Where the seal holds, it holds hard. From the delivered receipt alone, with
twenty lines of my own code, all **26** seal rows recompute, the manifest
equals the declared seal set exactly, **no receipt key is uncovered** (26
sealed + 4 declared-unsealed = 30 keys = the whole receipt), and
`payload_sha256_12` reproduces. Four of the six declared attacks die:

| attack (R4b/R5/U4b playbook) | outcome |
|---|---|
| post-gate head flip (`verdict.weld` FOUND→EMPTY after `SEAL-VERDICT`) | **KILLED at G-SEAL-COMPLETE** |
| census-row move (a row's fate flipped after `SEAL-WELD`) | **KILLED at G-SEAL-COMPLETE** |
| control-under-label (the walk control renamed after seal) | **KILLED at G-SEAL-COMPLETE** |
| silent seal-drop (`SEAL-WELD` removed from the taken rows) | **KILLED at G-SEAL-COMPLETE** |
| extra unsealed receipt key | **KILLED at G-SEAL-COMPLETE** |
| gate-registry drift / a stripped waiver | **KILLED at G-COVERAGE** |
| transcript-head preset before `finish` | no surface — the head is *derived* inside `finish` and overwrites the preset |
| **coherent seal-drop** (drop the row **and** the declaration **and** declare the key unsealed) | **SHIPPED** — see m1 |
| **sweep never ran** (`mutant_sweep: []`) | **SHIPPED** — see m2 |
| **coherent `weld_string` forgery** | **SHIPPED a `WELD3-EMPTY` head** — see M1 |

Post-write corruption of the delivered receipt, as a consumer sees it: one
edit is caught **twice** (the broken seal row *and* `payload_sha256_12`); two
edits (value + its seal row) are caught by `payload_sha256_12`; only a
three-edit forgery (value + seal row + payload sha) is internally consistent,
and it is then caught by the external file hash the ledger and the pin carry.
The transcript's 195 lines below the sealed 40-line head carry no seal, but
every one of the 66 receipt gate rows appears verbatim in the transcript, so a
transcript-body forgery is cross-checkable against the sealed receipt. That is
the correct boundary for a self-describing artifact and I do not fault it.

---

## 2. FINDINGS

### MAJOR

**M1 — the head comparator is not independent on the segment that carries the
verdict.** §10 states the head "is derived a second time by a comparator that
shares neither code nor input nor typed literal with the builder". True for
two of three segments: `reconstruct()` re-types the arena template (168 chars)
and the geometry template (173 chars), and I confirmed both are live by
perturbing the receipt fields they read. **The weld segment — 842 of 1183
characters, 71.2 % of the head, the segment carrying `WELD3-FOUND` — is
rebuilt by calling `weld_string()`, the same function the builder calls,
including the outcome-word rule.** The comparator therefore tests the
serialization round-trip, not the derivation.

Demonstrated, not argued: I patched `weld_string` so the outcome word is
`EMPTY`, ran the full pipeline, and **shipped a delivered receipt whose head
reads `WELD3-EMPTY-[ACTOR->SITE|…]` past all 68 gates** — past
`G-VERDICT-RECONSTRUCTED` (builder and comparator moved together), past
`G-PAPER-CLAIMS`, `G-PAPER-NUMERAL-COVERAGE` and `G-PAPER-CLAIM-POLARITY`
against the committed paper that says FOUND. In that shipped artifact the
receipt's own rows still read `FOUND-candidate` six times: the forgery is
internally contradictory and no gate notices.

The verdict word *is* protected in the direction that matters — you cannot
forge FOUND out of dead rows, because `EXPECTED[(arena, reading)]` pre-registers
all 18 fates and `G-WELD-CENSUS` compares each row against its own cell. But
that protection comes from a typed pre-registration, **not** from the
reconstruction the paper credits. The claim as written is false; the
protection is real but differently sourced.

This is also a partial miss against the **pin's own standard**, not only
against §10's prose: `note-r3weld-pin.md` requires "the head DERIVED and
rendered-from-receipt with string equality". 28.8 % of the head is derived;
71.2 % is rendered from the receipt through the builder's own function. The
string-equality half is met in full.

*Seam note, not a finding.* `EXPECTED` is a unit-owned, in-file
pre-registration: the pin fixes the outcome **vocabulary**
(`WELD3-FOUND-<map>` / `WELD3-EMPTY-<obstruction>` /
`WELD3-BLOCKED-AT-<object>`) but not the 18 per-cell fates. That is the same
trust boundary as m1 — declaration and measurement live in one file — and it
is disclosed by construction, since every row publishes its own
`declared_fate`. I record the boundary rather than charge it.

*Repair (liftable, ~15 lines).* Type the weld template a second time inside
`reconstruct`, exactly as arena and geometry already are, and derive the
outcome word there from `rec["weld"]["fate_distribution"]` rather than from a
shared helper. Then correct §10 to say which segments are re-typed.

**M2 — the paper's verdict heads are outside the numeral gate.**
`paper_coverage` runs `re.sub(r"`[^`]*`", " ", text)` before scanning, which
removes **all six fenced verdict blocks**. 79 of the paper's 506 numerals —
including *every numeral of all three verdict strings, twice over* — are never
scanned by `G-PAPER-NUMERAL-COVERAGE`.

Demonstrated end to end, not at the function level: I built a paper carrying
`ISOS=4242|QUOTIENT-MAPS=4242`, `FIBERS=1/1/7`,
`CEILING 9 ATTAINED at 73 of 21952001`, `FORCED 999 of 1040`,
`DET-SPECTRUM 4 VALUES ON 197568001 CELLS` and `SITE-FIBER=61` inside its six
verdict blocks, and ran the instrument's own `--verify-paper` against it:

```
[PASS] G-PAPER-CLAIMS              claims 15, missing none
[PASS] G-PAPER-NUMERAL-COVERAGE    scanned 427, allow-listed 427, unregistered none
[PASS] G-PAPER-CLAIM-POLARITY      polarity rows 3, violations none
[VERIFY-PAPER] … -- 62 gates, all passed
```

`scanned 427` is the *same* count the clean paper produces, which is the
finding in one number: the corrupted numerals were never in the scan at all.
The
controls are healthy and prove the gates are otherwise live: the *same*
corruption placed in prose (`1,296 → 1,297`) is caught twice, at
`G-PAPER-NUMERAL-COVERAGE` and at claim `C11`; and a head outcome-word flip
(`WELD3-FOUND → WELD3-EMPTY`) is caught by polarity `P1`. So the head's
**word** is gated and the head's **numbers** are not.

This is an instrument gap, not a paper error: I compared all six fenced blocks
against `R["verdict"]` character for character and they are exact — 168 + 173
+ 842 characters, reproduced twice each.

*Repair (3 lines).* Add
`G-PAPER-HEAD-VERBATIM`: `all(match_needle(paper_text, R["verdict"][k]) for k
in R["verdict"])`. `canon` whitespace-normalises, so the fenced multi-line
block matches the single-line receipt string; I verified this holds on the
committed paper. That one gate binds all 1183 head characters.

**M3 — three of the four walls are self-declarations wearing a gate's
clothes.** `G-WALL-BHS`, `G-WALL-KR` and `G-WALL-DIAGONAL` take their entire
input from the mutant flag: `ran_boost = mut("MUT-WALL-BHS")`, `took_dim =
mut("MUT-WALL-KR")`, `cosmo = mut("MUT-WALL-COSMO")`. Nothing scans the paper
or the run for what they assert. The evidence that a scan was intended and
left unwired is in the file: **`boost_terms = ("boost", "rapidity", "sprinkl",
"frame", "lorentz")` at line 3063 is assigned and never read** — the only
dead local in `full_run` that is not a loop throwaway. Consequently §6's "no
sprinkling, no boost, no rapidity and no frame appears in any measurement
above" and "this unit takes no dimension reading at all" are **unmeasured
assertions**, and their three declared mutants falsify the flag rather than
the property.

By contrast the two walls that *do* read the paper bite properly: `G-WALL-L1`
matched the retracted sentence's absence, and `G-WALL-LORENTZ-NAMED` fails
when I delete the naming paragraph. Those two are measurements — **but their
falsifiers are not.** `MUT-WALL-L1` is declared as "injects the retracted L-1
sentence into the paper under test, LINE-WRAPPED AND BLOCKQUOTED in house
style"; its implementation is `if mut("MUT-WALL-L1"): banned_here = True`. It
never injects anything and never exercises the #125 normaliser. Same shape at
`MUT-WALL-LORENTZ` (`named = False`). So five falsifiers — the four walls plus
`MUT-SELFTEST-WRITES` — set the gate's boolean instead of moving the thing the
gate measures; the other 54 corrupt a measured quantity. I performed the
injection `MUT-WALL-L1` describes, in 30 renderings, myself (see m4).
*Second repair:* make `MUT-WALL-L1` actually inject its sentence into
`ptext` — three lines — so the mutant tests the detector it advertises.

*Repair.* Wire `boost_terms` and a dimension-term list against the
**measurement layer** — the receipt's own keys and the gate statements — not
against prose (the paper legitimately contains "Lorentz" in the mandatory
naming sentence and in the L-1 wall). One conjunction per wall.

### MINOR

**m1 — the seal's totality is measured against a declaration the same file
owns.** Dropping `SEAL-WELD` from the taken rows *and* from `SEALED_PATHS`
*and* appending `"weld"` to `DECLARED_UNSEALED` ships a corrupted weld row (I
shipped `isomorphisms: 999999`). The only trace is disclosure:
`seal_manifest.declared_unsealed` gains a fifth entry and `totals.seals` falls
26 → 25. The *silent* drop — the shape the declared mutant tests — dies
correctly. *Repair:* freeze `DECLARED_UNSEALED` by content against a constant
and gate its length; refuse to declare unsealed any key a paper claim reads.

**m2 — the mutant sweep's execution is not bound.** A delivery in which the
59-mutant loop never ran ships: `mutant_sweep: []` next to `coverage.mutants:
59` and 59 reachability rows, every gate passing, artifacts written.
`SWEEP_GATE` is declared into the coverage denominator by constant rather than
read off the ledger, and unlike the two LATE gates it is **not** in
`G-ARTIFACT-INTEGRITY`'s `late_ok` conjunction. *Repair (1 line):* add
`SWEEP_GATE` to `late_ok` and gate `len(R["mutant_sweep"]) == len(MUTANTS)`.

**m3 — 18 of 20 verbatim anchors' `consumer_gate` is a declaration, not a
binding.** By AST, only `V10` (`G-I7-READOUT`) and `V17` (`G-WALL-L1`) are
actually consumed at the gate they name; the other 18 needles are matched once,
at `G-VERBATIM`, against their pinned source. Nothing checks that a named
consumer exists, was evaluated, or touches the needle. (All 20 names do happen
to be real gates that ran — I checked against the registry and the ledger.)
§10's "each name the gate that consumes them" is true of the naming and untrue
of the binding. *Repair:* assert `consumer_gate ∈ GATE_REGISTRY` and present in
the run's ledger — two lines — and, better, have each consumer re-match its
needle.

**m4 — #125 normalisation stops at the markdown layer.** The pin's walls hold
against everything markdown can do: **19 of 19** evasions of the retracted L-1
sentence are caught — line-wrapped at width 40 and 12, blockquoted, nested
blockquote, `>`-without-space, `-`/`*`/numbered lists, blockquote+bullet mixed,
bolded, back-ticked, table cell, heading, 4-space indent, tabs, double spaces,
nbsp, em-dash folding, curly apostrophe. **8 non-markdown evasions are not
caught**: zero-width characters, soft hyphens, interleaved `<em>`/`<span>`,
HTML comments, HTML entities (`&#39;`), backslash escapes, footnote markers.
*Repair:* in `canon`, drop Unicode category `Cf` plus U+00AD, strip HTML
tags/comments and decode entities, drop backslash escapes.

**m7 — the directed comparator is carried but not reported.** §5.1 says
"Admissibility is undirected on the kill side and the admit side alike, for
weld 2's reason; **the directed comparator is carried and reported**." The
reading is disclosed; the number is not. It is in the receipt and it is
**0 at every one of the nine arenas**, the two FOUND rows included: undirected
1296 / directed 0 at `R3-SAT`, undirected 72 / directed 0 at the crystal
control. FOUND therefore holds at the undirected reading only, and the directed
comparator separates nothing anywhere — which is why reporting it moves no
verdict, and also why omitting it costs the paper nothing but the sentence's
accuracy. The pinned precedent does better: weld 2 puts both numbers in prose
("…the undirected one returns **72**. Adopting the directed reading as the
…"). If "reported" was meant as "reported in the receipt", say so; otherwise
put the zero in §5.1. *Repair:* one clause.

**m6 — a sealed warrant asserts something the artifacts disprove.**
`closing_gates.warrant` — sealed as `SEAL-CLOSING`, so it ships inside the
receipt with a digest on it — ends "…and **the transcript carries both rows in
full**". It does not. `emit_report` runs after `finish` has already serialized
`text`, and `G-ARTIFACT-INTEGRITY` is evaluated after the transcript string is
built, so the archived `r3_weld_output.txt` stops at `G-SEAL-COMPLETE`: it
carries **67 of the 68** gate rows and omits `G-ARTIFACT-INTEGRITY`, and it is
8 lines shorter than the console transcript (234 vs 242 — the missing lines are
that gate's row and the TOTALS block). The receipt's own `gates` snapshot
carries 66 and omits both closers. So **neither delivered artifact records the
terminal integrity gate's verdict.** The warrant's *compensating* argument
stands untouched and is correct — a run that fails a gate writes nothing, so
the artifacts' existence is that verdict's record — and I independently
confirmed the gate passes (my off-tree console transcript carries the row:
"corrupted probe detected True, sealed objects broken on disk none, transcript
head matches True"). It is the factual clause that is wrong. *Repair:* one
sentence — say that the transcript carries `G-SEAL-COMPLETE`'s row and that
`G-ARTIFACT-INTEGRITY`'s verdict is carried by the artifacts' existence; or
append a two-line sidecar after `os.replace`.

**m5 — CLI: mode flags silently override, so a flag can be a no-op.**
`--verify-paper --mutant MUT-HEAD` parses to mode `mutant` with
`--verify-paper` consumed as nothing; `--numbers --no-write` → no-write;
`--selftest --list-gates` → list-gates. §10's "no flag is a no-op" is not met
under a hostile vector. Nothing unsafe follows (see below). *Repair:* reject a
second mode flag.

---

## 3. THE INJECTIONS TABLE

| # | injection | run | caught | survived |
|---|---|---|---|---|
| 1 | post-gate head flip (`verdict.weld`) | 1 | G-SEAL-COMPLETE | — |
| 2 | census-row move (fate flipped post-seal) | 1 | G-SEAL-COMPLETE | — |
| 3 | control-under-label (walk control renamed) | 1 | G-SEAL-COMPLETE | — |
| 4 | silent seal-drop | 1 | G-SEAL-COMPLETE | — |
| 5 | extra unsealed receipt key | 1 | G-SEAL-COMPLETE | — |
| 6 | gate-registry drift | 1 | G-COVERAGE | — |
| 7 | waiver stripped | 1 | G-COVERAGE | — |
| 8 | transcript-head preset | 1 | no surface (head derived in `finish`) | — |
| 9 | coherent seal-drop (row + declaration + unsealed) | 1 | — | **SHIPPED (m1)** |
| 10 | sweep never ran | 1 | — | **SHIPPED (m2)** |
| 11 | **`weld_string` outcome forgery → WELD3-EMPTY** | 1 | — | **SHIPPED (M1)** |
| 12 | paper head numerals corrupted (6 sites) | 2 | — | **SHIPPED (M2)** |
| 13 | paper prose numeral corrupted (control) | 1 | G-PAPER-NUMERAL-COVERAGE + C11 | — |
| 14 | paper head outcome word flipped (control) | 1 | G-PAPER-CLAIM-POLARITY P1 | — |
| 15 | naming sentence deleted (control) | 1 | G-WALL-LORENTZ-NAMED | — |
| 16 | retracted L-1 sentence, 30 evasive renderings | 30 | 22 | 8 (m4) |
| 17 | real one-byte corruption of a pinned source | 1 | G-PROVENANCE, exit 1, nothing written | — |
| 18 | `--break-anchor` × all 13 sources | 13 | G-PROVENANCE ×13, exit 1, nothing written | — |
| 19 | hostile argv vectors | 34 | 15 malformed → exit 2; 0 reach the writer | — |
| 20 | post-write receipt corruption (1/2/3-edit) | 4 | 1-edit ×2 signals, 2-edit ×1, 3-edit by external hash | — |
| 21 | the 59 declared mutants, **cold cache, out of process** | 59 | 59 at the named gate, 54 distinct gates, exit 1, nothing written | 0 |

---

## 4. THE CLI VERDICT — **PASS, with m5**

34 argument vectors exercised at the parser and 21 end to end. Every malformed
vector exits 2: unknown flag, short form `-n`, underscore form, upper case,
`--flag=value` form, truncated prefix `--no-wri`, bare `--`, empty string,
whitespace-only string, trailing positional, missing flag argument, unknown
mutant name, unknown anchor name, lower-cased mutant/anchor names, a flag
where a NAME is required.

The strong property, and it is worth stating plainly: **no non-empty argv
reaches the writer.** Every recognised flag reassigns the mode away from
`deliver`, so mode `deliver` — the only mode that calls the writers — is
reachable only by the bare invocation. I verified this over all 34 vectors and
statically against the mode table. `--list-gates` prints exactly the 68-entry
registry and `--list-mutants` exactly 59 rows, matching the run's own
`registry_drift: []`.

`--selftest`: dies at `G-PROVENANCE`, exit 1, artifacts untouched — verified
with my own corruptions, not only the code's flag. All 13 `--break-anchor`
names exit 1 at `G-PROVENANCE` writing nothing; and, the harder test, a
genuine one-byte append to a pinned source (`paper-13-weld2-carrier-census.md`)
kills the run at `G-PROVENANCE` with exit 1 and leaves no artifact. Only m5
(silent mode override) is charged against §10's contract wording.

---

## 5. COVERAGE, REACHABILITY, AND THE SWEEP

`#34` with an honest denominator holds: **68 gates evaluated = 68 in
`GATE_REGISTRY`**, `registry_drift: []`, **54 falsified by at least one of 59
declared mutants + 14 waived = 68**, `uncovered: []`. I recomputed the
partition and confirmed the registry-equals-evaluated-set claim is the strong
form (symmetric difference, so a gate present in the registry but never run
also dies). Removing one waiver or appending one phantom registry entry both
kill the run at `G-COVERAGE`, as they should.

All 14 waivers carry a forcing and each forcing is honest on inspection; the
three self-referential ones (`G-COVERAGE`, `G-REACHABILITY`,
`G-MUTANTS-ON-TARGET`) are genuinely unfalsifiable-from-inside, and
`G-PROVENANCE`'s waiver is discharged by a real flag which I exercised 14
times.

Reachability: every one of the 59 mutants names a gate the delivery run
evaluates, and the three LATE gates are handled correctly — `G-SEAL-COMPLETE`
and `G-PAPER-COVERAGE-FINAL` are evaluated before `finish` returns even under
`write=False`, so mutants naming them really do reach them in a mutant
sub-run, while `G-ARTIFACT-INTEGRITY` (which a no-write run never reaches)
carries no mutant and is waived. That split is precisely the "pipeline-shape
asymmetry" class the worker reports having fixed, and the code carries the
accounting for it explicitly rather than narratively.

### The four claimed sweep catches — verified as fixes, not narrative

1. **The cached-list mutant.** Present and fixed in the code:
   `MUT-UNIT-GRADE` does `ufield = dict(ufield)` **before** writing
   `ufield[(I7_LINKS[2], SITES[4])] = 2`. Without that copy the mutant would
   poison the shared field for every later in-process pipeline. I scanned every
   in-place mutation inside a `mut(...)` block: 11 sites, and each either
   copies first or writes a key only its own mutant reads
   (`CACHE["notforced"]`). No mutant leaks into a clean run.
2. **The two inert mutants.** Verified by outcome, not by history: an inert
   mutant returns `killed_at is None ≠ gate` and fails
   `G-MUTANTS-ON-TARGET`. That gate passes at **59 of 59** and I reproduced it
   byte-identically off-tree. No mutant is inert today.
3. **The three shape asymmetries.** Verified structurally: `SWEEP_GATE`,
   `LEDGER_GATES` and the `LATE_GATES[:2]` / `LATE_GATES[2]` split each carry
   an in-code warrant for why they cannot be read off the ledger, and each is
   individually correct. This is what a repaired accounting looks like. The
   residue is m2 — the sweep gate is declared into the denominator but its
   *execution* is not verified, unlike the two LATE gates.

**One structural observation, declared rather than hidden.** `BUILD_CACHE` and
`DETECT_CACHE` are module-level and persist across the 60 in-process
pipelines, keyed on the schedule alone; `driven()`'s own docstring says so
("cached, mutant-independent: the record is a property of the schedule"). It
means the 59 mutant sub-runs inherit the clean run's driven records, so every
mutant must bite downstream of the drive. The right test is a **cold-cache,
out-of-process** run of each mutant, which is the sweep in row 21 of the
injections table.

**External cold-cache sweep result: 59 of 59 on target.** I ran every declared
mutant `--mutant NAME` in its **own process**, in a scratch mirror, from a cold
cache. Every one exits **1** — the intended kill — and every one dies at the
gate it names, hitting **54 distinct gates**. The kill gate is **identical to
the in-process sweep's for all 59**, so the shared `BUILD_CACHE`/`DETECT_CACHE`
masks nothing. **Zero artifacts were written**: the mirror still holds exactly
its 15 files. The cached-list class is dead in both directions — warm and cold.

---

## 6. COMPARATOR INDEPENDENCE, ANCHORS, AND THE THREE-WAY SWEEP

**The head derivation** — §2/M1 above. Offline, the comparator reproduces all
three delivered segments from the receipt exactly; the arena and geometry
templates are demonstrably live under perturbation; the weld template is
shared. 71.2 % of the head is not independently derived.

**Anchors (#62).** Re-verified with my own normaliser, my own file reads and
my own hashing, taking nothing from the instrument: **13 of 13** source
`sha256-12` exact; **20 of 20** verbatim needles present in the source they
name; the shortest canonical needle is 33 characters against a declared floor
of 30, so the floor binds with 3 characters to spare. The `V04` needle only
matches once `ℓ → l` and `− → -` are folded, and the instrument's `_FOLD`
carries both — the fold is doing legitimate work, not hiding a miss. The 6
numeric anchors are real reads: I located `66/12/18` and `102/18/30` in
`d66_arbitration_crystal_exact.out`, and weld-2's committed `1296`, `72` and
site-fiber `6` in `paper-13-weld2-carrier-census.md`. Charged: m3, the consumer
binding is nominal for 18 of 20.

**Per-row binding (#87).** The 18 census rows are each compared against
`EXPECTED[(arena, reading)]`, a typed pre-registration of all 18 fates — a
cell, never an aggregate. The 72-stratum rows are bound per object too:
`G-SAT-ARENA-IDENTITY` drives all 72 I7-STRICT triples, requires
`maxhits == 1` and `divisions == 9` of **each**, and requires the set of
co-division relation signatures over all 72 to have cardinality 1. The 31
stratum cells each carry a driven witness checked FORCED individually.

**Three-way sweep (paper ↔ receipt ↔ transcript).** 103 targeted
recomputations, **zero disagreements** — all 10 rows of the positive-definite
distribution (including the empty cell at 8, which the receipt encodes as
`empty_posdef_cells: [8]` and the paper renders as an explicit zero row), all
9 det-spectrum rows, all 6 stabilizer rows, the whole R = 2 back-anchor
(78 400 / ceiling 3 / wall 6 / 18 incidences / 747 non-degenerate / strict
empty), and 78 further scalars. Every one of the paper's 113 distinct numeral
tokens occurs in the receipt or the transcript; the only two apparent misses,
`1/2` and `9/4`, are artefacts of my own regex splitting a Unicode minus and
are present as `-1/2` and `-9/4`. All six fenced heads are character-identical
to the three receipt verdict strings.

**The headline combinatorics, re-derived from nothing.** Not strictly my row,
but it costs nothing and it is the cheapest way to test whether the instrument
is measuring what it says. From the paper's prose definitions alone, in my own
code, with no import of the instrument and no constant taken from it, on
Z_3^2: **280** partitions of the nine sites into three triples (matching
9!/(3!³3!)); **21,952,000** ordered grouping triples; **36** partitions all of
whose nine pairs are I7 pairs; **72** I7-STRICT ordered triples in **12**
multisets carrying **1,417,176** schedules; of those 12 multisets **exactly 1**
has all its conflict groups on lines of AG(2,3) and **11** do not; and the
coordinate-free saturating class is **72 per missing parallel class, 288 in
total = 4 × 72**. Every one of those is the paper's number.

**The rigidity theorem, re-derived as a proof rather than a census.** Three
rounds deposit 27 pairs, so Σ_ℓΣ_x n_ℓ(x) ≤ 27 with equality iff no ANT pair is
deposited. From `q_of`, det > 0 forces n₁n₂ > 0 and n₃ = 0 gives
det = −(n₁−n₂)²/4 ≤ 0, so a positive-definite site needs all three counts ≥ 1,
i.e. ≥ 3 incidences. Nine positive-definite sites therefore force ≥ 27, hence
exactly 27, hence n ≡ 1 — so **I7-STRICT = POSDEF-9 = FIELD-IDENTICALLY-1 is a
theorem, and its class is the 72 I enumerated exhaustively myself.** §4.2 is
sound and the ceiling number is independently confirmed.

**The census's own arithmetic closes.** sum(posdef_site_distribution) =
21,952,000 = the triple count; sum(det_spectrum) = 197,568,000 = 9 × triples =
`det_cells`; sum(nz_distribution) = 21,952,000 with `nz["9"] =
nondegenerate_at_9 = 715,755`; and posdef[9] = triples_at_ceiling =
i7_strict_ordered_triples = 72. A 300,000-triple independent random sample
reproduces the receipt's posdef distribution at every cell to within sampling
error (0.19787 vs 0.197759 at k = 0, 0.394637 vs 0.394299 at k = 1, …,
4 observed at k = 7 against an expected 3.6) and finds **zero** at k = 8. The
empty cell at 8 is corroborated, not proved, here — proving it is K2's
exhaustive column, not mine.

**Twenty-three arithmetic closures of the paper's own numbers**, all clean,
including several the paper does not spell out and which therefore test that
its numbers were computed rather than assembled: 280 × 27 = 7560 and
7560³ = 432,081,216,000; 432,081,216,000 // 1040 = 415,462,707, the disclosed
ratio; **1040 = 136 × 2³ − 6 × 2³**, i.e. the window is the 136 scanned
grouping triples at two transversals per round *minus* the six orderings of
the single all-parallel-class multiset that W3-CLASS and W3-SAT share — which
independently ties §2.3's window size to §4.2's "one of twelve multisets";
8424 × 18 = 151,632 and 18 = 9 arbitrations × 2 seats; 72 × 81 = 5832 and
81 = 3 rounds × C(3,2) × 9 sites; 72 × 27³ = 1,417,176; 288 − 72 = 216;
9 × 21,952,000 = 197,568,000; 280² = 78,400; 18//3 = 6 and 27//3 = 9 for the
two walls; 84³ = 592,704 and 9!/(3!)³ = 1680; 1680 + 4 × 561 = 3924.

**Exactness and isolation, verified independently.** No float literal, no
`float()` call, no true division, no subprocess-class import, no
`os.system`/`popen`/`fork` anywhere in the 3 972-line instrument; `exec` and
`compile` appear at exactly the two declared AST-extraction sites, over
hash-pinned bytes, with module-level statements filtered out; `open()` with a
mode argument appears at exactly four sites, two of them the writers inside
`finish`, which is what `selftest_shape` asserts. An independent JSON parse of
the delivered receipt finds no float on any path.

**Byte-identity and repo state.** My off-tree run reproduced both artifacts
byte for byte under a different hash seed. Repo object hashes at the close of
this review are unchanged from its opening.

---

## 7. WHAT I DID NOT FIND

No false number. Nothing in the paper's measured layer moved under any of my
recomputations. The controls are two-way and they flip: the crystal control
returns FOUND with weld-2's own 72, the declared falsifier returns UNMOTIVATED
at site-fiber 6 — weld-2's committed value, read not typed — the walk is
ARITY-DEAD at 2 objects against 9, the crystal at I7 is STRUCT-DEAD with the
diagonal zero at 9 of 9, and this unit's own falsifier is STRUCT-DEAD. The
`SMUGGLED = 0` qualifier is stated honestly as structural. The window is
disclosed inside the arena verdict string, and the three exhaustive columns
really are exhaustive over objects the window does not cap. The three
qualifications travel in the head, where a reader cannot miss them.

The FOUND verdict is not weakened by anything in this review. What is weakened
is one sentence in §10 about how the head is checked, one about the walls, and
one about the anchors' consumers.

---

## 8. THE LIFT

| # | repair | size |
|---|---|---|
| M1 | re-type the weld template inside `reconstruct`; derive the outcome word from the receipt's fate multiset; correct §10 | ~15 lines |
| M2 | add `G-PAPER-HEAD-VERBATIM` matching each `R["verdict"][k]` into the paper | 3 lines |
| M3 | wire `boost_terms` and a dimension-term list against the measurement layer | ~6 lines |
| m1 | freeze `DECLARED_UNSEALED` by content and gate its length | 2 lines |
| m2 | add `SWEEP_GATE` to `late_ok`; gate `len(mutant_sweep) == len(MUTANTS)` | 2 lines |
| m3 | assert each `consumer_gate` is in the registry and in the run's ledger | 2 lines |
| m4 | strip `Cf`/U+00AD, HTML tags/comments/entities and backslash escapes in `canon` | ~6 lines |
| m5 | reject a second mode flag in `parse_args` | 2 lines |
| m6 | correct the `closing_gates` warrant's last clause (or emit a sidecar after `os.replace`) | 1 line |
| m7 | put the directed comparator's zero into §5.1 | 1 clause |
| M3b | make `MUT-WALL-L1` actually inject its sentence into the paper text | 3 lines |

None of these changes a measured number. M2 and m2 are the two I would insist
on before terminal: M2 because the head is the sentence the corpus will quote,
and m2 because the sweep is the instrument's own warrant.

---

## 9. THE FORM

**Grade: AWF.** **Executions: 101** processes — 1 off-tree plain delivery run
(60 pipelines inside it), 59 external cold-cache mutant runs, 13
`--break-anchor` runs, 2 `--selftest` runs, 1 plain run against a genuinely
corrupted source, 1 `--verify-paper` against a head-corrupted paper, 2 attack
harnesses carrying 12 injections, 1 timing run, 5 CLI probes, 16 offline
analysis scripts. **Recomputations: 735**, of which the load-bearing blocks are
103 targeted three-way, 113 paper numeral tokens, 68 off-tree PASS rows, 68
coverage-partition checks, 59 external mutant outcomes, 30 evasion renderings,
34 argv vectors, 29 seal recomputations, 23 arithmetic closures, 20 verbatim
anchors, 16 first-principles combinatorial results, 13 provenance hashes and 10
sampled distribution cells.

**Findings: 3 MAJOR (M1 head comparator, M2 head numerals, M3 the three
unmeasured walls), 7 MINOR (m1–m7).** Every one is liftable; the whole lift is
under fifty lines and moves no measured number.

**False numbers found: none.** No number in the paper, the receipt or the
transcript moved under any recomputation I ran, including sixteen results
re-derived from first principles with no constant taken from the instrument.

Object hashes at the close of this review — paper `c669ab35e12a`, code
`7a84aa27de8d`, output `76ef29488b60`, receipt `03670731ba1c`, pin
`20fba9b15f5e` — identical to the opening. Scratch only, at
`…/scratchpad/r3w-in/`. One repo write: this file.
