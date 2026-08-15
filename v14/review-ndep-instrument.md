# NDEP (paper-39) — K3 INSTRUMENT-LENS REVIEW

**Seat:** K3, instrument lens, three-seat hostile panel.
**Verdict:** **ACCEPT-WITH-FIXES (AWF).**
**Status of every finding below: candidate until adjudication.**

**The object, sha256-12 verified at open and again at close (unchanged
across the review; every mutation ran in a mirror under scratch, absolute
paths, per-run trees deleted, peak scratch 753 MB then 524 KB):**

| object | sha256-12 | lines |
|---|---|---|
| `v14/paper-39-ndep.md` | `25bea1eddd3a` | 381 |
| `v14/code/ndep_exact.py` | `d83df6c1e07d` | 3658 |
| `v14/code/ndep_output.txt` | `efa2987ef6a7` | 177 |
| `v14/code/ndep_receipt.json` | `3f5639a9146d` | 2653 |
| `v14/note-ndep-pin.md` (pin) | `2ff14505f18f` | 10 |

**Counts.** 175 process executions; 112 live injections of my own design,
plus the 27 declared falsifiers swept twice (in harness and one-process-each
out of harness) = 54 falsifier verdicts; ~340 recomputations, of which 23
are load-bearing physics/structure quantities recomputed on a foreign route
(nothing imported from `ndep_exact.py`). Repo writes: this file only.

**Why AWF and not R.** No measured quantity is wrong. Twenty-three published
numbers were re-derived from scratch by independent combinatorics — Bell(4)=15,
the subgroup counts 5 / 6 / 67 and the 7 F₄-subspaces, 16!/(4!⁴·4!)=2,627,625,
|S₁₆|, the 1,240-permutation window and its 21,080 comparisons, C(539,2)=144,991
and both of its mod-m splits, 2q−1 = 3|5|7, ⌈log₂n⌉ = 2|4|4, and the sharpened
weight floor reimplemented from the paper's own prose, which reproduces 2|4|6 at
all three arena points — **23 of 23 agree, zero mismatches**. Byte identity holds
off-tree, git-less, from artifact-deleted trees, under two hash seeds. The CLI is
clean at 21 hostile argv forms. All 27 falsifiers die at their declared gates out
of harness with the tree byte-unchanged. The fidelity leg is genuinely
three-legged. **What fails is the paper-facing half of the instrument**: ten
majors below, of which eight are template-shaped rather than NDEP-shaped.

**Why R was considered and rejected.** The ACT hole (MAJOR-1) puts a forged
finding on disk at exit 0 under a gate that prints "the seal manifest is TOTAL",
and the transcript hole (MAJOR-2) lets the human-readable artifact carry
different numbers from the sealed receipt. Either is a rejection-grade defect in
a unit whose *findings* were in doubt. They are not here: the head is
reconstructed, the sealed paths are sound, the physics recomputes, and every
hole is a hole in the *reporting perimeter* rather than in a measurement. AWF
with binding repair orders is the right instrument.

---

## 1. WHAT HOLDS (verified, not assumed)

| leg | result |
|---|---|
| **Byte reproduction (#91)** | Plain run from a 5-file off-tree tree with **no `.git` anywhere** and both artifacts deleted reproduces `ndep_receipt.json` `3f5639a9146d` and `ndep_output.txt` `efa2987ef6a7` **exactly**, under `PYTHONHASHSEED=11` and `=987654`. The only stdout difference between seeds is the absolute path in the two closing lines. |
| **Reads (#46/#91)** | 3 SOURCE reads + 1 SELF + 1 paper, all hash-pinned, no subprocess, no repository read outside the declaration. Confirmed by the 5-file tree running to completion. |
| **CLI (#82)** | 21 hostile argv forms: `--bogus`, `-h`, `--help`, `--selftest --bogus`, bare `--mutant`, `--mutant NOPE`, doubled `--mutant` in both spellings, empty string, `--mutant ""`, `--mutant=NAME extra`, case variants `--MUTANT` / `mut-head`, `--selftest=1`, `--sweep=true`, a bare positional, `--`, `--mutant --sweep`. **All exit 2, tree byte-unchanged.** No silent flag-ignoring anywhere. |
| **`--selftest` writes nothing** | Proven **by full-tree hash**, not by inspection: tree hash identical before and after; all three anchors die at `G-PROVENANCE`, artifacts unchanged. |
| **Falsifier sweep, out of harness** | 27/27, **one process each, artifacts present on disk**, every one dying at the gate its registry row names, tree byte-unchanged after all 27. In-harness `--sweep` agrees: 27 mutants, 0 off-target. |
| **Registry counts, all from live objects** | gates **42** (29 main + 15 closing − 2 declared outside both artifacts; 0 duplicate names), seals **34** (34 unique paths, gate names verified), falsifiers **27** (27 unique, all with a real code hook), windows **9** (**6 entire / 3 partial, each partial carrying its reason in its own declaration text**), anchors **3 byte + 10 path-value + 6 verbatim**, walls **5**, referent bindings **5**, polarity axes **5** (all live, both directions), control arms **13** (5 transport + 8 leg, each forced to its expected value, legs driven true *and* false), tables **4**, claims **13**, numerals **355 scanned of 355 reference** + **104 spelled**, **0 unbacked**. Every one of these matches the delivery's claim. |
| **The fidelity leg (target 4)** | **Three independent legs, 15/15 kills.** Corrupting each of the five q=3 substrate counts in the mirror: (a) byte anchor alone → `G-PROVENANCE` dies on `A-AIDREC` ×5; (b) with the declared sha updated → `G-PARENT-ANCHORS` dies naming the exact anchor (`P-PARTS`/`P-SAT`/`P-STRICT`/`P-FLAT`/`P-WINDOW`) ×5; (c) with the path-value anchor also updated → **`G-CONSTRUCTOR-FIDELITY` itself dies**, per object, reporting "rows agreeing 4 of 5" and naming the disagreeing row ×5. The licence gate binds on its own. |
| **Sealed-path integrity (#119)** | Post-seal overwrite of `verdict/head` → dies (`SEAL-VERDICT`). Post-seal add *nested under a sealed key* (`counts/forged_extra`) → dies (`SEAL-COUNTS`). Dropping the `counts` seal while declaring it unsealed → dies. Tampering the staged transcript *after* the write-time digest → `G-ARTIFACT-INTEGRITY` refuses and promotes nothing. |
| **E-22 span and multiset legs** | Inline-code-span numerals are genuinely scanned: a backticked `999` dies at `G-PAPER-COVERAGE`. A **duplicated** verdict fence dies on multiset inequality. Both legs real. |
| **The two parent constants the seat was told to press** | **Both genuinely computed-cross-checked, not typed.** FAC's 6 (`subgroup_coset_partitions`) → `G-LAW3-PARENT` dies with "declared 7, enumerated at q = 3 6, q + 3 6", the enumeration being an independent closure-of-generators subgroup count. The ladder's rung 3 (`first_rung_at_n9`) → `G-LAW4-LADDER` dies, cross-checked against `Arena(3).L`. |
| **Reading walls scan the paper** | Unlike LOR MAJOR-1, all five wall patterns *are* run against the paper text (`re.findall(pat, canon(text))`). The template disease of a wall that never sees its object is **fixed here**. What survives is a different defect — see MAJOR-6. |

---

## 2. MAJORS

### MAJOR-1 — THE ACT DISEASE, LIVE: a forged top-level receipt key reaches disk at exit 0 under a gate that reports "the manifest is TOTAL"

`G-SEAL-TOTALITY` computes `published`, `missing`, `extra` and `unsealed`
*inside the gate*, and `SEAL.close()` afterwards verifies only the digests of
paths **already in the manifest**. Nothing enumerates the payload's keys against
the manifest at close time. Any top-level key added after the gate therefore
travels to disk unsealed and undeclared.

Injection (one line, inserted after `G-SEAL-TOTALITY` runs):

```
R["forged_finding"] = {"NDEP-PORTABLE": "5-OF-5", "smuggled": 999}
```

Result: **exit 0, both artifacts promoted**, and on disk
`ndep_receipt.json` carries `"forged_finding": {"NDEP-PORTABLE": "5-OF-5",
"smuggled": 999}`. The transcript's own line is the smoking gun — it reports
`seals 34 over 35 published keys, missing none` while the file it is describing
has 36 published keys. Reproduced at a second insertion point (immediately
before `SEAL.close`), same outcome. The declared falsifier `MUT-SEAL-DROP`
covers only the *other* direction (a declared seal not taken) and cannot see
this.

**Repair.** Recompute `published` from `R` **at `SEAL.close` time** and refuse
promotion unless every key is sealed or declared-unsealed; make the closing
figure in the evidence line the post-close count, not the gate-time snapshot.

### MAJOR-2 — THE TRANSCRIPT IS NOT BOUND TO THE RECEIPT: the reader's artifact can carry different numbers from the sealed one

`G-TRANSCRIPT-INTEGRITY` checks exactly one thing: that the substring
`"[PASS] <gate>"` occurs in the staged text, for each gate. It never compares the
transcript's rendered *evidence* with the receipt's `evidence` field, and the
only gate-time seal touching the transcript is `transcript_head =
digest(LINES[:40])` — **40 of 177 lines, 23 %** — which is published but never
compared against anything. `seal_t` is taken at write time from the same
in-memory string it is about to write, so it certifies only "the bytes I wrote
are the bytes I meant to write".

Injection (one line in `Ledger.gate`'s rendering):

```
say("         evidence: %s" % str(evidence).replace("45", "99"))
```

Result: **exit 0, both artifacts promoted, `G-ARTIFACT-INTEGRITY` PASS.**
Transcript line 108 reads `evidence: unique 99, non-unique 3, histories 48`;
the receipt's `G-LAW5-CENSUS` row reads `unique 45`. The two published
artifacts contradict each other on the unit's own headline census and nothing
notices.

**Repair.** Bind the transcript to the ledger: for every gate row, require the
rendered `evidence` string to equal the receipt's `evidence` for that gate, and
seal the **whole** transcript at gate-close rather than its first 40 lines.

### MAJOR-3 — THE HEAD IS NOT DERIVED TWICE BY DISJOINT CODE: the comparator catches 2 of 22

`independent_head` is claimed to share "no code, no inputs and no typed literal"
with `verdict_segments`. Measured, it shares both of the engraved failure modes:

- **Same inputs.** Both read `R["law1_naming"]`, `R["law2_crystallization"]`,
  `R["law3_coset_menu"]`, `R["law4_mod_motif"]`, `R["law5_division_forcing"]`,
  `R["n16_window"]` — the comparator re-reads the builder's product rather than
  deriving from primitives.
- **Same concatenation written twice.** Every fixed prose fragment of all seven
  segments is typed verbatim in both functions; the difference is `%`-formatting
  versus `+`-concatenation.

**Measurement.** I forged 22 leaf values across the five law objects and
`n16_window` and recorded which gate fired. `G-VERDICT-RECONSTRUCTED` caught
**2** — `law3['actor_lattice']` and `corpus['histories']`, exactly the two whose
two paths read *different* receipt keys (`counts/actor_lattice_n4` and
`counts/histories_n4` on the publishing side). The other **20** passed the
comparator and died later, at `G-PAPER-COVERAGE`, only because the paper still
contained the old numeral.

**The consistent adversary defeats the remaining defence.** A worker who
mis-derives a number renders it consistently. Forging the receipt value *and*
the paper together — `route_prefixes_compared` 53→45, `forced` 45→44,
`route_window_positive` 2,064→2,065 — gives **exit 0, artifacts written, head
byte-equal, coverage clean** in all three cases. In the `forced` case the
delivered receipt is internally contradictory (`law1_naming/forced = 44` beside
`counts/forced_n4 = 45`) and no gate compares them.

**Repair.** The comparator must derive from measured primitives (`HIST`, `LAT`,
the corpus objects) and must not read any law object the publishing path reads;
or, minimally, cross-check every receipt key that appears in two places.
Separately: `verdict_segments` carries the typed literal `com(2627625)` while the
comparator computes it — the typed side should be the one removed.

### MAJOR-4 — ALL SIX VERBATIM ANCHORS ARE PHANTOM CONSUMERS

The delivery claims "6 verbatim anchors each with a named non-literal consumer".
The consumer gates *name* their anchors in prose — "This is the gate the
parent's quotation V-YOUNG names", "The parent's V-TIME quotation fixes the
n = 9 value at 5" — but **no gate predicate reads a quotation's text**. The
quantities those sentences attribute to the quotes come from the *path* anchors
(`P-TIME`, `P-FLOOR`) instead.

**Proof by receipt-leaf diff.** I replaced V-TIME's needle with a completely
different but still-true sentence from the same pinned parent. The run passes,
and the receipt differs from the committed one in exactly **3 leaves**:
`verbatim_anchors/3/chars` (64→52) and the two digests derived from it. **Not one
measured quantity moves.** The anchors are inert decoration downstream of
`G-VERBATIM`.

(The consumer *name* is checked: retargeting a consumer to a non-existent gate
dies at `G-SEAL-TOTALITY`'s phantom-name leg. Name-checked, not consumption-checked.)

**Repair.** Either make each consumer gate parse its quotation and compare the
parsed content with the measurement, or demote the anchors to declared
provenance and stop claiming a consumer.

### MAJOR-5 — 5 OF 23 TABLE ROWS ARE UNBOUND: the entire §2.1 corpus table

`markdown_table_rows` finds 23 non-separator rows in the paper. `paper_tables`
renders 4 tables totalling 18 (`G-PAPER-TABLES` evidence: "tables 4, rows bound
18"). The missing 5 are the whole corpus table — header plus C1/C1FAN/C2/C3.
Three injections, all **exit 0**:

- header swapped (`schedules`/`rounds` transposed) — **byte-identical to the
  committed artifacts**;
- `| C3 | 34 | 3 | 6 |` → `| C3 | 15 | 3 | 6 |`, a false published schedule
  count — **byte-identical**;
- a wholly fabricated fifth row `| C4 | 5 | 2 | 4 |` — admitted, merely
  re-counted (`table_rows` 23→24).

The four bound tables are bound properly: header swaps on T-WORDS and T-LADDER,
a forged T-SUBGROUPS cell, a flipped T-WORDS word and a forged T-LADDER modulus
all die at `G-PAPER-TABLES` naming the row.

**Repair.** Render the corpus table from `R["corpus"]["corpora"]` and bind it;
add a gate that `markdown_table_rows(paper)` is *exhausted* by the rendered
tables, so a future unrendered table is a failure rather than a silence.

### MAJOR-6 — THE READING WALLS AND POLARITY NEGATIVES ARE LITERAL-PHRASE TRAPS; 4 OF 5 NATURAL VIOLATIONS PASS

Each wall's positive control is the pattern's own sentence, so every probe fires
by construction and proves only that a regex matches the string it was written
from. Against violations phrased as a paper would phrase them:

| planted sentence | wall owed | result |
|---|---|---|
| "The actor count nine is not a declaration at all; it is selected by the geometry." | WALL-NINE-DERIVED | **passes** |
| "Nine actors are structurally necessary, and the arena selects that count." | WALL-NINE-DERIVED | **passes** |
| "Nine is an arbitrary choice with no content." | WALL-ARBITRARY | **passes** |
| "The nine-actor numbers are recomputed here from scratch." | WALL-N9-REDERIVED | **passes, byte-identical** |
| "The n = 16 enumeration is exhaustive and complete, not a window." | WALL-N16-COMPLETE / POL-WINDOW | **passes, byte-identical** |
| "There is a 90 per cent chance a given law transports." | WALL-PROBABILITY / POL-MEASURE | dies — **but on `90` as an unbacked numeral, not on the wall** |

The last two invert the paper's own scope sentences with no trace in either
artifact. This is LOR #269's caveat — "a green sweep is not evidence a wall
holds" — now measured on the paper leg it was routed to.

**Repair.** Widen each pattern to its semantic family (`selected|necessary|
required|not a declaration`; `census|corpus|enumeration|window`;
`chance|per cent|probability|likelihood|likely`), and require each wall's
positive control to be a sentence **not** derived from its own pattern —
ideally three controls per wall, at least one written by a different hand.

### MAJOR-7 — THE REFERENT BINDINGS ARE SATISFIED INSIDE THE MACHINE-DERIVED VERDICT FENCES

`noun_bindings` asks whether *some* occurrence of a numeral sits within three
words of its noun — `any(re.search(...))` over the whole paper. Four of the five
bindings match inside the gate-locked verdict fences (`48 DRIVEN HISTORIES`,
`53 DISTINCT PREFIXES`, `21,080 COMPARISONS`, `144,991 PAIRS`), which the run
itself renders and `G-PAPER-HEAD-VERBATIM` / the multiset gate hold fixed. The
binding therefore tests the machine's own output against itself, and the prose
is unbound. Cross-universe plants, all **exit 0 and byte-identical**:

- "That is **48** driven histories" → "That is **15** driven histories";
- "there are **53** distinct prefixes" → "there are **48** distinct prefixes";
- "21,080 **comparisons** in all" → "21,080 **partitions** in all";
- "all 15 **partitions** of the four actors" → "all 15 **histories** of the four actors".

Each is a count attached to the wrong universe — the precise disease the gate
names — surviving because a fence elsewhere satisfies the existential.

**Repair.** Bind **per occurrence**, over the prose only (`prose_only()` already
exists and is unused by this gate), and require every occurrence of a registered
headline numeral to sit beside its own noun. This is #87 for prose: a gate on
"there exists a correct occurrence" is an aggregate predicate.

### MAJOR-8 — `G-PAPER-CLAIMS` NEVER SCANS THE PAPER; PROSE DIRECTION FLIPS PASS

`paper_claims` builds 13 sentences from receipt values and then checks only
`c["supported"]` — a predicate over the receipt. **The sentence strings are
never searched for in the paper.** Nothing binds the paper's prose to the
measurement outside the fences and the four rendered tables. Injections, all
**exit 0**:

| flip | result |
|---|---|
| "21,080 comparisons in all, **0 mismatches**" → "**3 mismatches**" | byte-identical |
| "The theorem transports." → "The theorem **does not** transport." | byte-identical |
| "**Three** of the five laws are portable" → "**Five** of the five laws are portable" | byte-identical |
| "The pair's word is the weakest leg's: **NEEDS-3**." → "**LAW-IN-N**." | passes |
| §1's definition inverted: "It is **NEEDS-3** when that reading fails" → "**LAW-IN-N**" | passes |

The third and fourth contradict the head fence one screen away, and the fifth
inverts the paper's own definition of its two verdict words.

**Repair.** Make `G-PAPER-CLAIMS` a *paper* gate: require each of the 13
rendered sentences to occur in the paper under the #125 normalisation, with the
polarity partner absent — the same contract the fences already have.

### MAJOR-9 — A FORGED EXTRA VERDICT FENCE IS ADMITTED (E-22 gates only the required segments)

`fence_multiset_equal` checks `found[seg] == 1` for each of the **7 required**
segments. `fences_in_paper` is measured (7) and **never gated**. An eighth fence
whose numerals happen to be backed passes:

```
NDEP-EXTRA<PORTABLE AT ALL 5 OF 5; THE COUNT IS LAW-IN-N; 48 HISTORIES>
NDEP-SUMMARY<ALL 5 OF 5 LAWS ARE LAW-IN-N; 0 NEEDS-3>
```

Both **exit 0**, both directly contradicting the head. (Duplicating a *required*
fence correctly dies — the multiset leg works in the direction it was written
for.)

**Repair.** Gate the fence multiset in **both** directions: every fence in the
paper must be a required segment, and every required segment must appear
exactly once.

### MAJOR-10 — E-23: ONE FALSIFIER'S DESCRIPTION IS INVERTED, ONE IS A CONSTANT INJECTION

All 27 registry rows have a real code hook (no dead text). Checking each
description against its hook, three-legged (description ↔ hook ↔ declared gate):

- **`MUT-TABLE` — description inverted.** It reads "one published table's HEADER
  row is **dropped from the binding**, so a table whose columns were renamed
  would pass". The code does the opposite: `t["header"][1:]` **truncates** the
  header so it mismatches and the gate fires. The described disease, tested
  honestly (suppress the header check, then rename T-WORDS' header in the
  paper), gives **exit 0, byte-identical**. The mutant's green badge certifies
  an obligation the instrument does not discharge — and MAJOR-5 shows the
  disease is live for the corpus table.
- **`MUT-SEAL-GATE` — a constant injection.** It replaces the detector's
  computed output with a hard-coded `["FORGED"]` rather than creating the
  described condition. It proves only `if seal_phantom: fail`, which is true by
  construction. I tested the honest condition (point `SEAL-SCHEMA` at a gate
  that never runs, and separately point a verbatim anchor's consumer at one) —
  **both die correctly**, so the gate is sound; the falsifier is a false badge.
- **`MUT-SEAL-DROP` exempts the leg it should exercise.** `not (_m and not
  mut("MUT-SEAL-DROP"))` disables the manifest-gap leg for exactly the mutant
  that creates a gap. The leg is sound under an honest injection (dropping the
  `counts` seal fires it), but it has **no falsifier of its own**.

The other 24 descriptions match their hooks and their declared gates.

**Repair.** Rewrite `MUT-TABLE` to drop the header from the binding (and let it
die because the paper's header no longer needs to match — which requires
MAJOR-5's repair first); rewrite `MUT-SEAL-GATE` to actually retarget a seal;
remove the `MUT-SEAL-DROP` exemption and give the `_m` leg its own falsifier.

---

## 3. MINORS

**m1.** `G-SWEEP-BOUND` passes **vacuously in the delivered receipt**:
`mutant_sweep` is `[]` and `totals/sweep_rows` is 0, because the committed run
was made without `--sweep`. `all([])` is `True`. The 27/27 claim is true (I
verified it twice) but **is not carried by the committed artifacts** — a reader
of the receipt sees "sweep rows 0, off-target none". Either publish the sweep or
stamp the row NOT-RUN-IN-THIS-ARTIFACT.

**m2.** **2 of 6 frozen FAC constants are ungated**, contradicting §2's sentence
"Every frozen constant is cross-checked against a value this unit computes
independently." Isolated one at a time: `subgroup_coset_partitions` (6) →
`G-LAW3-PARENT`; `unique_at` (5,852) and `non_unique_at` (4) → `G-LAW5-PARENT`;
`first_rung_at_n9` (3) → `G-LAW4-LADDER`. But `actor_lattice` (21,147) and
`leg1_equals_the_subgroup_cosets` (`True`) **survive corruption at exit 0** —
neither is cross-checked anywhere. (21,147 is in fact Bell(9); the value is
right, the discipline claim is not.) `leg1_geometry_survivors` (6) is caught only
by the paper's head string, not by a cross-check gate.

**m3.** Spelled-numeral coverage has **no reference count**, unlike the numeral
leg (`numerals_scanned == reference_numerals_in_whole_paper`). `words_scanned`
is reported (104) with nothing to compare it to, so a scan-narrowing change
confined to the spelled leg would be invisible.

**m4.** Because coverage is an allow-list over the receipt's *number set*, a
spelled numeral backed by an unrelated quantity passes in a false sentence:
"Four questions are left open and named" → "**Twelve**" / "**Twenty**" both pass
byte-identically (12 and 20 are backed elsewhere), while "seventeen",
"nineteen" and "hundred" are correctly caught. This is the structural limit of
an allow-list; the referent-binding gate is what should close it, and MAJOR-7
explains why it does not.

**m5.** `verdict_segments` carries the typed literal `com(2627625)`; the
comparator derives it. The right direction, but the builder should not type a
number the run can compute.

**m6.** Polarity negatives are literal-phrase traps of the same species as the
walls — POL-WINDOW's negative `"exhaustive at n = 16"` misses "The n = 16
enumeration is exhaustive and complete". Same repair as MAJOR-6.

**m7.** `_FOLD` defines `"≠"` twice (harmless; the second wins with the same
value).

---

## 4. THE NINE TARGET PROBES — PRESENT / ABSENT

| # | probe | verdict |
|---|---|---|
| 1 | header swaps + fabricated rows | **PRESENT for the 4 rendered tables** (5 kills, each naming the row); **ABSENT for the §2.1 corpus table** — header swap, forged count and a fabricated row all pass (MAJOR-5) |
| 2 | direction flips | **PRESENT in fences and rendered tables** (head `3-OF-5`→`5-OF-5` dies; T-WORDS cell flip dies; `{3,6}`→`{3,6,9}` dies in both table and fence); **ABSENT in body prose** — "0 mismatches"→"3", "transports"→"does not transport", "Three of the five"→"Five of the five", law 2's word flipped (MAJOR-8) |
| 3 | ACT, both forms | **ABSENT for post-seal top-level adds** (forged key on disk at exit 0, two insertion points; MAJOR-1); **PRESENT for declared-unsealed forgeries and for edits under sealed paths** (all die) |
| 4 | fidelity gate leg — corrupt one of the five q=3 substrate counts | **PRESENT, three-legged, 15/15.** The licence gate dies on its own once the two anchors are neutralised, per object |
| 5 | transcript integrity + forged PASS | **ABSENT.** The transcript is not bound to the receipt (MAJOR-2). A forged-PASS *renderer* alone cannot green a failed gate (the raise is unconditional) — but the rendered evidence is free, and 137 of 177 transcript lines carry no gate-time seal |
| 6 | phantom consumers — are all 6 verbatim anchors subscripted? | **ABSENT.** Named, never consumed; proven by a 3-leaf receipt diff (MAJOR-4). The consumer *name* is checked to be a running gate |
| 7 | read-back / staging / write-nothing by tree hash | **PRESENT.** `--selftest` leaves the tree hash identical; staged-then-promoted with the check before `os.replace`; tampering after the write-time digest refuses and promotes nothing; the one-byte-flip control rejects |
| 8 | spelled numerals (104 claimed — plant one) | **PRESENT but allow-list-bounded.** "seventeen", "nineteen", "hundred" all die naming the word; "eleven", "twelve", "twenty" pass because those integers are backed by unrelated quantities (m4). No reference count for the leg (m3) |
| 9 | referent binding (48-histories / 15-partitions / 53-prefixes cross-universe) | **ABSENT.** Four cross-universe plants pass, all byte-identical, because the bindings are satisfied inside the machine-derived fences (MAJOR-7) |

---

## 5. THE STRENGTHENED GATES, RE-PROBED

The delivery disclosed eight first-sweep off-target mutants closed by
strengthening gates. Re-probing those gates directly:

| strengthened gate | re-probe verdict |
|---|---|
| `G-PAPER-COVERAGE` (spans, spelled, multiset, reference count) | **genuinely strengthened.** Backticked `999` dies; the reference count is taken over the *pristine* text so a scan-narrowing mutation cannot move both sides; duplicate fences die. Residual: m3, m4, and MAJOR-9's one-directional multiset |
| `G-PAPER-TABLES` (headers bound "on the same terms as the data rows") | **strengthened in form, not in coverage.** True for the 4 rendered tables; the 5-row corpus table is bound by nothing (MAJOR-5), and the mutant that certifies the header obligation is description-inverted (MAJOR-10) |
| `G-SEAL-TOTALITY` (phantom gate names) | **the new leg is sound** (honest phantom injections die) **but its falsifier is a constant injection**, and the totality claim itself is defeated upstream by MAJOR-1 |
| `G-NOUN-BINDING` (numeral within three words of its noun) | **strengthened in form, vacuous in fact** — the adjacency is satisfied by the run's own fences (MAJOR-7) |
| `G-WALLS-SCAN-THE-PAPER` (walls scan the paper; positive controls) | **the LOR MAJOR-1 disease is genuinely fixed** — the patterns do run against the paper. The controls are self-referential and the patterns are literal traps (MAJOR-6) |
| `G-PAPER-CLAIM-POLARITY` (both directions, liveness) | axes live and both-directional, but the negatives are literal traps (m6) |
| `G-VERDICT-RECONSTRUCTED` (head derived twice) | **2 of 22** (MAJOR-3) |
| `G-CONSTRUCTOR-FIDELITY` (per object, never as a total) | **fully verified** — 15/15, per object, three legs |

Pattern: the strengthening was **structural** (the gate now exists and runs)
rather than **binding** (the gate now discriminates). Five of eight strengthened
gates pass a re-probe of their own stated obligation only in the direction their
mutant tests.

---

## 6. THE SEAM RULING

**Eight of the ten majors are TEMPLATE-SHAPED, not NDEP-shaped.** MAJOR-1
(post-seal adds), MAJOR-2 (transcript unbound to receipt), MAJOR-3 (comparator
re-reads the builder's product), MAJOR-4 (phantom verbatim consumers), MAJOR-5
(unrendered tables), MAJOR-6 (literal-trap walls), MAJOR-7 (fence-satisfied
referent bindings) and MAJOR-8 (claims that never scan the paper) are all
properties of the shared closing-battery template, not of anything this unit
measures. MAJOR-5, MAJOR-6 and MAJOR-7 are recurrences of LOR MAJOR-2, the LOR
#269 wall caveat, and the LOR MAJOR-4/M6 family respectively — i.e. **the #267
corpus-sweep recommendation was not fully absorbed**, and three of the four
template diseases routed to the in-flight workers are alive here in new dress.

MAJOR-9 and MAJOR-10 are NDEP-local (a one-directional multiset gate; two
falsifier rows).

**Recommendation:** the corpus sweep of sibling units recommended at #267 should
now be treated as **owed rather than recommended**, and the four repairs that
generalise — post-seal totality at close time, transcript-evidence binding,
per-occurrence prose referent binding, and claims-scan-the-paper — should be
made in the template before being made here, so the next unit does not buy them
a fourth time. I do **not** recommend engraving new RUNBOOK rules from this seat
before that sweep: E-22, E-23 and #119 already say what was violated; what
failed was compliance, not doctrine. The one candidate genuinely not covered by
an existing engraving is **"a seal manifest is total only if totality is
recomputed at promotion time"** — MAJOR-1's mechanism — which the adjudicator
may wish to add as a #119 addendum.

---

## 7. WHAT THIS SEAT DOES NOT CONTEST

The headline `NDEP-PORTABLE-3-OF-5` and its five per-law words are consistent
with every measurement I could reproduce, and the transport procedure is a pure
function of its rows driven through 13 control arms that force all three words
plus the UNDISCRIMINATED stamp and the no-feasible-row refusal. The
`UNDISCRIMINATED` stamp on the offset leg, the unscored q = 4 coset-menu row,
the `COUNTING-ONLY` stamp under E-24, and the honest declaration of the n = 16
window (3 of 9 windows marked not-entire, each with its reason in its own text)
are all real and all correctly gated. The q = 3 fidelity leg is stamped
FIDELITY-LEG-ONLY everywhere it appears and no n = 9 law value is recomputed.
The sharpened weight floor — the unit's own contribution — reproduces 2 | 4 | 6
on my independent implementation.

**Every finding above is a candidate reading until adjudication.**
