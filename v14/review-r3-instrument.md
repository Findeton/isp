# R3 — HOSTILE REVIEW, INSTRUMENT LENS (the relativity rung, paper-03)

**Protocol:** `v14/note-r3-hostile-protocol.md` (`c575340216fc`), K5 primary, all
kill-shots at instrument depth.  **Pin:** `v14/note-r3-relativity-pin.md`
(`a2ac89687a65`).  **Object:** the frozen R3 delivery, hashes verified before any
work and re-verified after all of it — paper `00850cc796d0`, code `bbcc9a1aa7de`,
output `d54142292980`, receipt `1c8beb16c8a2`: **all four unchanged.**  The
pinned anchor targets are unchanged too (`e9d2bedff244`, `542b8735daf0`,
`ee295ac1bb68`, `08b2140f46ae`, `a4b0e71819be`, `f286ba10d2d9`, `d44cb72f8ee9`).
**Discipline:** scratch-only; nothing imported from the unit; subprocess
invocation of its CLI only; every mutant, injection and plain run on a scratch
mirror; read-only git; `v14/paper-04..08-*`, `v14/code/r6a_*`, `cra_*`, `crb_*`,
`crc_*`, `crd_*` and the other reviews never opened.  This file is my single repo
write.

**GRADE: ACCEPT-WITH-FIXES.**

The measurement is right everywhere I could reach, and the reach was long.  A
from-scratch re-implementation written from the paper's declared spec — importing
nothing, using a dense loop with no support reasoning, an adjugate matrix
inverse, and a full-pivot Gaussian elimination for the coefficient solve —
reproduces **317 census and coefficient cells across four (arena, lapse-scope)
combinations, 1 585 field comparisons, zero mismatches**: every `nonzero_pairs`,
every `total_pairs`, every `closes` flag, every `max|ρ|` and every coefficient
class.  Every derived denominator in the receipt reproduces from the arena
declaration by hand (476, 21 012, 644, 3 096, 2 280, 120 969, 198, 21 420,
4 128, 320, the four chart-group orders, the 25-member translate family).  The
paper's §8 L-sweep table — 64 hand-written cells, the one substantive table the
prose gate does *not* cover — matches the receipt cell for cell.  **All 60
declared mutants die at exit 1 on exactly their declared gate, with zero
tracebacks and no artifact written.**  Two plain runs on a scratch copy are
byte-identical to the committed artifacts, stdout included.  The verdict rebuilds
from the receipt alone, **byte-identically**, under my own reconstructor, and all
**14 of 14** segments flip under perturbations of my own design.  The
solve-for-c step is a real existence test: fed a crafted commutator with no
consistent coefficient it reports `NOT-EXTRACTABLE` and does not fabricate.
**Zero false numbers by value anywhere in the paper** — I traced all 14 rendered
claims, all 64 L-sweep cells and all 25 remaining hand-written numerals.

What fails is the **protection**, one **anchoring hole**, and two **false
mechanism claims**.

1. **The delivery reads an unanchored, live repo file, and its verdict is a
   function of it.**  `v14/LOG.md` is read at run time and is load-bearing for
   the `L-GATE` verdict segment.  It carries no anchor row.  Appending one
   ordinary ledger sentence to it changes the emitted verdict from
   `INHERITED-FRACTIONS-RECOMPUTED=3` to `=5` and changes **both artifact
   hashes**, at **exit 0 with 81/81 gates green and 0 prose claims missing**
   (measured).  And the gate that consumes it says the fractions are "found in
   [the R2 adjudication's] text": measured, **all three matched fractions occur
   zero times in the R2 adjudication note** and only in `v14/LOG.md`.
2. **Ten injection classes survive undetected** at exit 0 with 81/81 gates green
   and both artifacts written — including the R6a **Y1 defect-zeroing class**,
   which erases 3 095 of the 3 096 defect values and inverts **all four** of the
   unit's four defect findings while every defect gate stays green; the R1
   **INJ_D post-gate receipt-corruption class**; and a **#219 shared-component
   corruption** that moves the closure census by 20 cells with the "two
   independent routes" gate reporting zero disagreements.
3. **The verdict comparator is a self-comparison for 5 of its 14 segments** — a
   #219 recurrence at the very gate whose compliance row asserts #219
   compliance.  Proven by three injections.
4. **Two false mechanism claims**, one in the paper and one inside a receipt
   disclosure: the non-extractable cells are *not* "exactly the architecture-B
   rules" (they are exactly the `B-all` cells, **36 of 108** arch-B cells), and
   the boundary test's "degenerate probe carried alongside as the test's own
   death certificate" **does not exist** — the receipt's
   `degenerate_probe_sums_to_zero: true` is a typed Boolean and none of the 3 096
   probes is the zero field.

The waiver census is a genuine advance on R6a in one respect and not in another:
**no gate is shadowed** (the plain run evaluates all 81), but **27 of the 29
never-falsified gates are demonstrably falsifiable** — I killed every one of them
— so their "SAME-MECHANISM … not separately targeted" is a statement about
economy, not about forcing, and one of the two waiver texts carries a false typed
count.

Every repair below is definite.

---

## Execution counts

| | |
|---|---|
| plain delivery runs on the scratch mirror | **3** (all `d54142292980` / `1c8beb16c8a2`, identical to the committed artifacts, byte-identical stdout) |
| working-directory contract probe (M9) | **1** |
| CLI-contract probes (`--list-mutants`, unknown arg, unknown mutant, `--mutant` with no name) | **4** |
| independent 60-mutant falsifier audit (my own runs, not `--selftest`) | **60** |
| `--selftest` (1 top-level + 60 spawned subprocesses) | **61** (60/60 DEAD, exit 0, artifacts byte-unchanged) |
| waiver-kill injections (20 path-value rows + 6 file-byte rows) | **26** |
| crafted source-patch injections, phase 1 | **15** |
| the same injections re-run with the paper's affected sentences regenerated (phase 2, two runs each) | **16** |
| unanchored-input drift probe (`v14/LOG.md`) | **1** |
| **total process-level executions of the unit's CLI** | **187** |
| independent programs written from the declared spec | **3** (a from-scratch census/coefficient implementation, a from-receipt verdict reconstructor, an injection harness) |
| census + coefficient cells recomputed independently | **317** cells → **1 585 field comparisons, 0 mismatches** |
| derived denominators recomputed by hand from the arena declaration | **21** (0 mismatches) |
| paper numbers traced by value | **14** rendered claims + **64** L-sweep cells + **25** hand-written numerals |
| verdict rebuilds from the receipt alone | **1** (byte-identical) + **14** segment flips |

---

# FINDINGS, most severe first

## M1 (MAJOR) — the delivery reads an UNANCHORED live repo file and its verdict is a function of it; and the gate that consumes it makes a false claim about where its evidence came from

`run()` calls

```python
lg = l_gate_reason(adj, read_text("v14/LOG.md"))
```

and `l_gate_reason` scans **both** the (anchored) R2 adjudication note and the
(**unanchored**) `v14/LOG.md` for every `\d+/\d+` substring, intersects them with
the six recomputed overlap fractions, and returns the matches.  The count of
matches is emitted as a verdict segment:

```
L-GATE=…;INHERITED-FRACTIONS-RECOMPUTED=3
```

and is a must-pass condition of `G-L-GATE-INHERITED-FACTS`
(`len(matched) >= 3`).

**Measured, three ways.**

- The three matched fractions are `64/120`, `324/351`, `768/2016`.  Occurrences
  in `v14/note-r2-adjudication.md`: **0, 0, 0**.  Occurrences in `v14/LOG.md`:
  **2, 2, 2**.  So the gate's statement — *"the locality fractions the R2
  adjudication states for this lattice are RECOMPUTED here and found **in its
  text**"* — and the receipt field name
  `fractions_recomputed_and_matched_in_the_r2_adjudication` are **both false**:
  every match comes from the ledger, none from the adjudication.
- `v14/LOG.md` appears in **no** anchor row.  The paper §12 says *"The arena
  arrives through 7 file-byte anchors and 32 (path, value) anchors, plus one
  anchor whose expected hash is read out of the pinned receipt itself"* — a
  complete enumeration that omits a file the run reads and depends on.
- **Injection (proven-executed).**  I appended one sentence of ordinary ledger
  prose to a scratch copy of `v14/LOG.md`:
  `"#37 … complete at 36/36 pairs; the d=2 L=5 lattice draws 100/300."`
  Result: **exit 0, 81/81 gates PASS, 0 prose claims missing, both artifacts
  written**, with the verdict segment now
  `INHERITED-FRACTIONS-RECOMPUTED=5` and artifact hashes `212946a168b7` /
  `80c5fbad0940` instead of `d54142292980` / `1c8beb16c8a2`.

The consequences are three.  (a) The delivery's byte-reproducibility is
contingent on the current contents of a file that **every adjudication in this
cycle appends to**, with three other units live in the same repo; the
byte-identity re-verification at v14 #35 was luck of content, not a property of
the instrument.  This is not hypothetical: **`v14/LOG.md` changed during this
review** — `91f5eb0512db` when I began, `4af35fd8cf7c` when I finished, **7 972
bytes appended by a concurrent worker**.  I re-ran the plain delivery against the
new file: it still emits `d54142292980` / `1c8beb16c8a2`, but only because none
of the appended 7 972 bytes happens to contain one of the six matching fraction
patterns.  The frozen delivery survived a live edit to one of its inputs by
coincidence of wording.  (b) The §15 declared-arena discipline is broken: an input that
moves the verdict is not in the declared arena.  (c) The v14 #20 path-value
engraving is bypassed at its widest point — this is not a path drift inside a
pinned artifact, it is an *unpinned artifact*.

**Repair (definite).** (i) Delete the `read_text("v14/LOG.md")` argument
entirely; the R2 adjudication is the anchored source and the ruling is what
`A-R2-ADJ` binds.  (ii) If the ledger really is wanted as corroboration, add it
as an anchor row with its own sha and its own falsifier, and rename the receipt
field to name both sources.  (iii) Replace the substring scan with a
**path-value** anchor: read the fractions the R2 terminal receipt states at their
JSON paths (`A-R2-RECEIPT` is already anchored) and gate equality against the
recomputed ones; a prose-substring intersection over two long documents is not a
measurement of agreement, it is a coincidence test — `2/3` would not match, but
`36/36` matches anything that happens to write it.  (iv) Restate the gate to say
what it checks.

---

## M2 (MAJOR) — ten injection classes survive undetected, including the R6a Y1 defect-zeroing class (which inverts all four of the unit's defect findings), the R1 INJ_D class, and a #219 shared-component corruption

Each row is a complete plain run of a patched scratch mirror: **exit 0, 81/81
gates PASS, 0 FAIL, no traceback, both artifacts written, `never_falsified` still
29**.  "paper regenerated" means I also rewrote the paper's affected rendered
sentences — exactly what a repair worker does, and the only reason the run is not
stopped by `G-PROSE-RENDERS-FROM-THE-RECEIPT`.  Two of the ten need no paper
regeneration at all.

| id | corruption | delivered result | paper regenerated? |
|---|---|---|---|
| **I1** | zero the defect field at every probe but the first, inside `dh_defect_field` (the **R6a Y1 class**) | verdict ships `NONZERO-AT-1-OF-3096-PROBES; … LATTICE-SUM-ZERO-AT-3095-OF-3096; VANISHES-ON-THE-HOMOGENEOUS-SECTOR-AT-2279`. **All four** of §6's "four separate measurements" inverted — it now vanishes almost everywhere, it now *is* a boundary term, and it now *does* switch off on the homogeneous sector — with `G-DEFECT-MEASURED`, `G-BOUNDARY-TERM-STATUS` and `G-DH-BRACKET-CENSUS` all green | yes (1 sentence) |
| **I8** | corrupt seven receipt cells after every gate, at the top of `deliver()` (the **R1 INJ_D / R6a S1 class**) | `census_rows[0].max_abs = 999`, `nonzero_pairs = 4242`, `defect_rows[0].lattice_sum_zero = 11`, `controls.chart_group[0].order = 7`, `coefficient_rows[0].coefficient.class = "FABRICATED"` — all reach **both** `output.txt` and the receipt | **no** |
| **I7** | truncate `S["trajectory"]` to two rows after the L-sweep gates | `LSWEEP=d2L4/B:26-of-99-close,d2L4/T:26-of-99-close;COEFFICIENT-CLASS-CONSTANT-ALONG-L=TRUE` — six of the eight arena rows vanish from the verdict and the L-stability claim is asserted on two rows | **no** |
| **I11b** | zero the diagonal-link column inside **`gap_matrix`** — the component *both* census routes share | `closing_cells` 140 → **160**, `defecting_cells` 336 → 316, and `two_route.dense_disagreements = []`: `G-CENSUS-TWO-ROUTES` green | yes (2) |
| **I4** | flip 31 of the 32 `METRIC-READING-SITE-VARYING` cells to `METRIC-READING-CONSTANT` inside `type_coefficient` | `COEFFICIENT=…METRIC-READING-SITE-VARYING:1…SITE-VARYING-ON-THE-INHOMOGENEOUS-RECORDS-AT-1-OF-120`. The unit's positive finding reduced to a single cell, `G-COEFFICIENT-TYPING` green | yes (2) |
| **I2** | drop one (rule, record) defect row inside `run_census` | `defect_probes` 3096 → **3036** in the summary, the totals and the verdict; no gate carries a derived denominator for the defect census | yes (1) |
| **I3** | drop one (rule, record, realisation) `{D,H}` row | `dh_brackets` 21012 → **20858**, tally `D-REG/IDENTITY 10352`; `G-DH-BRACKET-CENSUS` only checks `> 0` | yes (1) |
| **I5** | overwrite `rec_out["closure_cells_compared"]` / `["sector_cells_compared"]` after the recovery gates | `RECOVERY=CLOSURE-99999-OF-99999;SECTOR-88888-OF-88888` — the machinery-recovery control's denominators fabricated, and the "independent reconstruction" agrees | yes (1) |
| **I6** | truncate `ctl["chart_group"] / ["positive"] / ["negative"]` after the control gates | `CONTROLS=CHART-GROUP-CLOSES-AT-1-OF-1-ARENAS;TRANSLATION-EQUIVARIANT-AT-768-OF-768;SCRAMBLED-VIOLATES-AT-384-OF-768` | yes (2) |
| **I10c** | add a diagonal-link component to `A-chart`'s weight at one site | `not_extractable_cells` 36 → **92**; the arch-B mechanism story in §4/X05 now covers an arch-A rule, and nothing notices | yes (2) |

**Died as they should** (protection that works, each proven by injection):
`I9` — making a second convention combination match everywhere → **exit 1 at
`G-CONVENTION-SWEEP`**; `I12` — corrupting only the dense route → **exit 1 at
`G-CENSUS-TWO-ROUTES`**; `I10b` — the same non-axis weight at the *positive
control* → **exit 1 at `G-COEFFICIENT-EXTRACTION`**.

Three named diseases recur.

- **#219 (v13, RUNBOOK §14 addendum), twice.**  `G-CENSUS-TWO-ROUTES` claims the
  support-restricted and dense routes "agree on every field of every cell".  They
  do — but both build their residual from the same `gap_matrix(rule, rec, x)`;
  the routes differ only in *which sites they visit*, which is exactly what the
  gate statement says and exactly not what the compliance row "13(5) two
  independent routes" means.  **I11b** proves it.  And the verdict comparator is
  a self-comparison on five segments (M3).
- **#10 / #13-addendum (v14, render from the gated object).**  **I8** shows the
  corrupted-`R` path is still open: `render_text` and `jsonable` both render from
  `R` *after* the last gate, and `render_check` runs before that.
- **#24 (counts computed, never typed).**  `degenerate_probe_sums_to_zero: True`
  is a typed Boolean standing in for a measurement that does not exist (M5), and
  the path-anchor waiver contains a typed count that is wrong (M6).

**Repairs.** (a) Give `G-DEFECT-MEASURED` and `G-BOUNDARY-TERM-STATUS`
predicates with **derived denominators**: `vanishing_probes == 0` and
`lattice_sum_zero == 0` against a probe count derived from
`len(adm) × len(rules) × DEFECT_PROBE_LAPSES × d` per arena, and add the
matching cell-completeness gate — `< probes` is satisfied by one surviving
probe out of 3 096.  (b) Add cell-completeness gates with derived denominators to
the `{D,H}`, `{D,D}` and defect tables, as `G-CENSUS-CELL-COMPLETE` already does
for the closure census.  (c) Gate `inhomogeneous_site_varying_metric` against a
derived expectation (which rules × which records are expected to realise it), not
against `> 0`.  (d) Give the two census routes genuinely disjoint residual
constructions — one from `W − B`, one assembling `Δ` from the literal four-map
composition and subtracting `hda_generator` — and add a mutant that perturbs
`gap_matrix` itself.  (e) Re-verify the receipt payload after `jsonable()`:
re-run `render_check` and a hash of the gated subtree at write time, so a
post-gate mutation of `R` cannot ship.

---

## M3 (MAJOR) — the verdict comparator is genuinely independent for 9 of its 14 segments and a self-comparison for the other 5; the compliance sweep's #219 row is false in part

`G-VERDICT-STRING-EQUALITY` states the comparator "shares no code and no input
with the builder, so it can disagree".  For nine segments that is true and it is
good work — `reconstruct_verdict_from_receipt` re-aggregates ARENA, HH-BRACKET,
COEFFICIENT, HH-RESIDUAL, DH-BRACKET, DEFECT, CONVENTION, DD-BRACKET and
REALISATION from the receipt's **raw rows** while `build_signatures` reads the
**summary**, and all seven verdict-injection mutants (five R1 classes,
`verdict-pair-swap`, `head-constant`) die on it.

For five segments it is false, in two different ways:

| segment | builder reads | comparator reads | verdict |
|---|---|---|---|
| `RECOVERY` | `rec_out[…]` | `R["recovery"][…]` — the same object, same expressions | **self-comparison** (I5 proves it) |
| `CONTROLS` | `ctl[…]` | `R["controls"][…]` — the same object, **character-for-character the same aggregation code** | **self-comparison** (I6 proves it) |
| `LSWEEP` | `S["trajectory"]` | `R["summary"]["trajectory"]` — the same object | **self-comparison** (I7 proves it) |
| `LAPSE` | `S["lapse_coordinate_moves"]` | `R["summary"]["lapse_coordinate_moves"]` — the same object | **self-comparison** |
| `L-GATE` | `lg[…]` + `CENSUS_L_MIN` | `R["l_gate"][…]` + `min(L)` — same object, one derived field differs | **self-comparison in substance** |

`R["recovery"] is rec_out`, `R["controls"] is ctl` and `R["summary"] is S` are
literal object identities, not copies.  So for these five the comparator cannot
disagree with the builder for any input whatever — the #219 definition of vacuous
by construction.  The compliance sweep's row *"219 comparators can disagree —
APPLIED — G-VERDICT-STRING-EQUALITY"* is therefore false for 5 of 14 segments,
and per the #313 addendum this is a recurrence of an engraved disease and a
MAJOR by default.

**Aggravating.** Unlike R6a, **the verdict string appears in neither the paper
nor the rendered prose claims** (measured: `claims` has 14 keys, none of them the
verdict; 0 of 14 segment texts occur in `paper-03`).  In R6a the frozen paper
acted as a *de facto* verdict anchor and eight of twelve survivors had to have the
paper regenerated.  Here **two of ten survivors (I7, I8) and the M1 drift probe
need no paper change at all** — the verdict is the least protected object in the
delivery.

**Repair.** (i) Rebuild RECOVERY, CONTROLS, LSWEEP, LAPSE and L-GATE in the
comparator from the receipt's **raw rows** (`census_rows` for the trajectory,
`controls.chart_group/positive/negative` re-derived from a second pass, the
recovery tables re-counted against the pinned I7 tables), never from `summary`
or from the same dict the builder used.  (ii) Deep-copy `R`'s sub-objects at
receipt-assembly time so object identity cannot be mistaken for agreement.
(iii) Add `claims["verdict"] = R["verdict"]["full"]` to `paper_prose()` and print
the full string in the paper, as R6a does — one line, and it closes I7, I8 and
the M1 drift.

---

## M4 (MAJOR) — §4's mechanism sentence and disclosure X05 are false: the non-extractable cells are exactly `B-all`, not "the architecture-B rules" — 36 of 108

§4 states, and §10's disclosure table repeats:

> The inconsistent cells are exactly the architecture-B rules: their commutator
> carries diagonal-link brackets, so its displacement is not of the axis-covector
> form at all, and no $d\times d$ coefficient can reproduce it.

and X05, carried in the receipt as a forced-clause disclosure:

> THE ARCH-B CELLS' NON-EXTRACTABILITY IS FORCED.  Architecture B's commutator
> displacement carries diagonal-link bracket components …

Measured, from the delivered receipt and confirmed by my own implementation:

| rule | arch | cells | `NOT-EXTRACTABLE` |
|---|---|---|---|
| `B-all` | B | 36 | **36** |
| `B-axis` | B | 36 | **0** (12 `CONSTANT-NON-METRIC`, 16 `METRIC-READING-CONSTANT`, 4 `METRIC-READING-SITE-VARYING`, 4 `SITE-VARYING-NON-METRIC`) |
| `B-chart` | B | 36 | **0** (32 `CONSTANT-NON-METRIC`, 4 `METRIC-READING-CONSTANT`) |

**36 of the 108 architecture-B cells fail, not 108.**  The mechanism is right for
`B-all` and wrong for the class it names: `B-axis` puts $\lambda_\ell = 1/n_\ell$
on the **axis links only** and `B-chart` puts $\lambda_\ell = 1$ on the axis links
only, so neither carries any diagonal-link bracket, and both are extractable at
every one of their 72 cells — indeed four `B-axis` cells are themselves
`METRIC-READING-SITE-VARYING`, which is the unit's headline class.  The count 36
is correct; the class it is attributed to is not.  This is the same shape as the
R6a M1 finding: a true theorem stated outside its scope, with the load-bearing
sentence drawn from the wrong scope.

**Repair (definite).**  Replace both sentences with the measured one:
*"The inconsistent cells are exactly the `B-all` cells — 36 of the 108
architecture-B cells.  `B-all` is the one declared rule that weights **every**
link, so its commutator carries diagonal-link brackets and its displacement is
not of the axis-covector form; `B-axis` and `B-chart` weight only the axis links
and are extractable at all 72 of their cells."*  Restate X05 the same way, and
add a gate that the `NOT-EXTRACTABLE` set equals the set of cells whose weight
matrix has a nonzero diagonal-link column — computed, not asserted.

---

## M5 (MEDIUM) — the boundary test's "death certificate" does not exist: `degenerate_probe_sums_to_zero` is a typed Boolean and none of the 3 096 probes is the zero field

§6 states:

> **It is not a boundary term.**  On a periodic lattice a total finite difference
> sums to zero; this one does not, at any probe.  The degenerate probe — the zero
> field, which does sum to zero — is carried alongside as the test's own death
> certificate, so the boundary test is not vacuous.

Measured: the string `degenerate` occurs in the source exactly twice — once
inside the gate's own statement, once as

```python
{"lattice_sum_zero": …, "probes": …, "degenerate_probe_sums_to_zero": True}
```

a **typed literal in the gate's value dict**.  No zero field is ever constructed
and no probe's lattice sum is ever compared against one: all 238 defect rows
report `lattice_sum_zero: 0`, so the probe set contains no degenerate member.
The non-vacuity of the test *is* in fact demonstrated — by the `boundary-lax`
mutant, which forces every field to sum to zero and dies here — but that is a
different argument from the one the paper and the receipt make, and the sentence
describes a measurement the instrument does not perform.  #24 applied to a
Boolean.

**Repair.**  Add the zero field (and, better, an explicit total-finite-difference
field $f(x+e_j)-f(x)$ built from a declared $f$) to the probe set as a *labelled
degenerate row*, measure its lattice sum, and gate
`degenerate_row.lattice_sum_zero == degenerate_row.probes` alongside
`lattice_sum_zero == 0` on the real rows.  Then the sentence becomes true and the
gate acquires the death certificate it claims.

---

## M6 (MEDIUM) — the waiver audit at the #34 standard: no gate is shadowed, but 27 of the 29 waived gates are demonstrably falsifiable, and both waiver texts contain a false claim

The unit's census is honest about its denominator — **29 of 81 gates carry no
declared falsifier, 29 waived, 0 unwaived** — and, unlike R6a, **no waived gate
is dead code**: the plain run evaluates all 81, and under `ha-code-drift` every
one of the 26 waived anchor rows is reached and passes.  That is a real advance.
The waiver *texts* do not hold up.

Method: gate registration order read from the delivered receipt and from the
source; every named mutant run and its death gate compared; then a targeted
injection per waived gate to test the implied "not worth targeting".

| # | waived gates | waiver's stated forcing | measured verdict |
|---|---|---|---|
| 1–6 | `A-PIN-R3`, `A-R0-PIN`, `A-R2-ADJ`, `A-R2-RECEIPT`, `A-R2-CODE`, `A-HA-PAPER` | "SAME-MECHANISM: identical in construction to **A-R0-I7 and A-HA-CODE**, both of which carry declared falsifiers (`anchor-hash`, `ha-code-drift`, `anchor-skip`)" | **FALSE IN TWO PARTS, ROWS ALL FALSIFIABLE.** (a) `A-HA-CODE` is *not* identical in construction: it is built by a different function (`derive_ha_code_anchor`), has a different `kind` (`derived-file-bytes`), derives its expectation from the receipt, and resolves a **CWD-relative** path (M9). (b) `anchor-skip` falsifies neither named row — it dies at `G-ANCHOR-COUNT`. (c) I killed **all six** rows by byte-corrupting each pinned file in a mirror: each → exit 1 on **exactly its own gate**, no traceback |
| 7–26 | the 20 path-value rows `P-I7-D`, `P-I7-DEXT`, `P-I7-LINKS3`, `P-I7-RECORDS3`, `P-I7-INHOMOG`, `P-I7-WEIGHT`, `P-I7-WEIGHTFLIP`, `P-I7-RULES3`, `P-I7-BROKEN`, `P-I7-POSCTL`, `P-I7-VERDICT`, `P-I7-CLOSURE-AXIS-OFFD`, `P-I7-CLOSURE-INSERT-CURVOFF`, `P-I7-SECTOR-CHART-CURVED`, `P-I7-LATTICE`, `P-I7-DETECTOR-CF`, `P-R2-SCHEMA`, `P-R2-HEAD`, `P-R2-GRIDRULES`, `P-R2-LOCCOUNT` | "SAME-MECHANISM: identical in construction to **the eight rows** carrying declared path-drift and path-value falsifiers" | **FALSE COUNT, ROWS ALL FALSIFIABLE.** There are **twelve** such rows, not eight (32 path anchors − 20 waived = 12; `path-drift`, `path-drift-links`, `path-drift-closure` and nine `path-value-*`). A typed, wrong number inside a waiver — #24 at the surface #34 was engraved for. And the generic falsifier `path-value-<NAME>` is **already implemented** in `verify_path_anchors`; only the `MUTANTS` declarations are missing. I declared all twenty in a mirror and ran them: **20 of 20 → exit 1 on exactly their own gate, zero tracebacks** |
| 27 | `G-CENSUS-TWO-ROUTES` | "NAMED, no waiver claimed" (the default string) | **HONEST BUT UNPROTECTED.** The gate has real teeth: **I12** (drop one ordered pair inside `census_cell_dense` only) → exit 1 here. It should carry that mutant, and the compliance row "13(5) two independent routes" should not rest on a gate with no falsifier |
| 28 | `G-CONVENTION-RULE-INDEPENDENT` | "FORCED (#208): the bracket's front sector contains no drag weight, so the per-rule rows cannot differ" | **CANNOT FAIL — BUT NOT FOR THE STATED REASON.** The predicate is `all(c["brackets"] % len(rules) == 0)`, and `brackets = len(base) × len(tgens) × len(adm) × len(rules)` by construction: it is a **divisibility tautology**, true for any input the arena admits. The stated forcing (rule-independence of the front sector) is never machine-checked anywhere, and it is the premise the convention sweep's whole denominator rests on (M7). Per #208 a forced clause belongs in `disclose()`, not in must-pass position |
| 29 | `G-DEFERRED-GATES-EVALUATED` | "WAIVED: a bookkeeping gate … its falsifier would be a gate that never ran, which the gate itself reports" | **GENUINE** |

**Honest denominators.**  81 gates; 52 falsified by 60 mutants naming 52 distinct
gates (the shipped `falsifier_map` lists only 50 — see below); 29 never falsified,
29 waived, 0 unwaived, **0 shadowed**.  Of the 29
waivers: **1 genuine** (#29), **1 cannot-fail-but-misstated** (#28), **1
honest-but-unprotected** (#27), **26 false in part** (the two SAME-MECHANISM
texts).  Of the 29 waived gates, **27 are demonstrably falsifiable** (26 killed
by me, plus `G-CENSUS-TWO-ROUTES` by I12), **1 cannot fail on any admissible
input** (#28), **1 is bookkeeping** (#29).

There is also a **dead waiver entry**: `waiver_for()` carries a bespoke string
for `G-RECOVERY-ANCILLARY`, but that gate *is* falsified (`general-d-drift`), so
the branch is unreachable and the string never surfaces.  Same class as R6a's
stale `G-ANCHOR-CELL-COMPLETE` entry.

And the shipped **`falsifier_map` is stale and disagrees with the census printed
beside it**: it carries **50** keys while `gates_with_a_declared_falsifier` says
**52** (= 81 − 29).  `finalise()` rebuilds `never_falsified`, the counts, the
denominator and the waivers three times but never rebuilds `falsifier_map`, so
the two gates registered after the map was first assembled —
`G-NEVER-FALSIFIED-CENSUS` and `G-COMPLIANCE-CLAIMS-ARE-GATE-CLAIMS`, both of
which *do* carry declared falsifiers (`falsifier-census-hide`,
`compliance-claim-unbacked`) — are absent from it.  `G-NEVER-FALSIFIED-CENSUS`'s
own predicate checks only `29 + 52 == 81` and so cannot see it.  Rebuild
`falsifier_map` in the final pass and gate
`len(falsifier_map) == gates_with_a_declared_falsifier`.

**Repair.**  (a) Declare the twenty `path-value-<NAME>` mutants — the mechanism
already exists, this is twenty lines and it takes the never-falsified count from
29 to 9.  (b) Add six byte-corruption falsifiers for the file-byte rows, or one
parameterised `anchor-hash-<NAME>`.  (c) Fix the two waiver texts: compute the
"eight"/"twelve" from `len(fmap)` restricted to `P-` rows, and stop naming
`A-HA-CODE` and `anchor-skip` as evidence for rows they do not cover.  (d) Add
the shadowing-arithmetic gate R6a's review asked for: for every waiver naming a
mutant, assert that mutant's `expected_gate` equals the waived gate.  (e) Move
`G-CONVENTION-RULE-INDEPENDENT` to `disclose()` and replace its predicate with
the measurement it claims (M7).  (f) Drop the dead `G-RECOVERY-ANCILLARY` entry
and gate the waiver dict against keys outside `never_falsified`.

---

## M7 (MEDIUM) — the convention sweep is measured at ONE record with no rule dependence and then MULTIPLIED UP; "measurement rather than argument" and "at every bracket in the census" are not what happened

§5 says the instrument *"decides that by measurement rather than argument,
sweeping both factor orders against both finite-difference directions"* and
concludes that the front sector reproduces the deformation content *"at every
bracket in the census"* — with the receipt reporting `21126 of 21126`.

The code:

```python
rec0 = recs[adm[0]]                       # ONE record
for (lname, N) in base:
    for tv in tgens:
        for order in BRACKET_ORDERS:
            fr = dh_front_closed(rec0, N, v, order)
            for (cname, cfn) in LIE_CONVENTIONS:
                if all(fr[x] == lv[x] for x in rec0.S):
                    conv_hits[(order, cname)] += 1
…
ok  = conv_hits[(order, cname)] * len(adm) * len(rules)     # multiplied up
tot = len(base) * len(tgens)   * len(adm) * len(rules)      # multiplied up
```

Measured: the actual front-sector evaluations number **685** distinct
(lapse, translation) probes across the four arenas (38 + 56 + 204 + 387), each at
2 orders × 2 conventions, all at the alphabetically first admissible record and
with no rule entering at all.  The reported 21 126 is that count multiplied by
`len(adm) × len(rules)` — 9 × 11 at d = 2 and 5 × 4 at d = 3 — two axes along
which nothing was varied.  I verified the arithmetic: 19·2·9·11 + 28·2·9·11 +
68·3·5·4 + 129·3·5·4 = 3 762 + 5 544 + 4 080 + 7 740 = **21 126**.

The extrapolation is in fact *sound* — `dh_front_closed` and both
`lie_lapse_*` functions read only $N$ and $v$, never the record's counts or the
drag rule — and a genuine partial cross-check exists (`conv_literal_cells = 320`
compares the front closed form against the literal composition at two records and
two rules).  But the licence the instrument cites for the multiplication is
`G-CONVENTION-RULE-INDEPENDENT`, whose predicate is a divisibility tautology
(M6 #28), and **no gate anywhere tests record-independence**, which is the larger
of the two multiplied factors.  A count derived by multiplying a 1-of-99 sample
by 99 is an argument, presented in the receipt and the paper as a census.

**Repair.**  Either (i) run the sweep over all records and rules — it is cheap,
the front computation touches no record data — and let 21 126 be measured; or
(ii) report the honest denominator (685 probes × 4 combinations) and carry the
extrapolation as a **disclosure** with a gate that actually measures it: compute
the front sector at ≥ 2 records and ≥ 2 rules per arena and gate that the
per-record and per-rule rows are identical.  Then rewrite §5's "at every bracket
in the census" to match whichever route is taken.

---

## M8 (MINOR) — three gate statements overclaim what their predicates check

- `G-DEFECT-MEASURED` states *"it does NOT vanish on any declared sector"*.  Its
  predicate is `defect_probes > 0 and defect_vanishing_probes < defect_probes`.
  `defect_vanishes_on_homogeneous` appears in the value dict and **in no
  predicate**.  I1 ships `VANISHES-ON-THE-HOMOGENEOUS-SECTOR-AT-2279` green.
- `G-SYMMETRY-SELFTEST` states *"FRESH-EVALUATED"*.  In
  `translation_covariance_of_the_residual` the **base** residual reaches
  `lambda_of` through the memo under the key `("A-chart"/"A-axis", "G-CURVOFF",
  2, 4, 0, x)` — the very key the census populated; only the translated records
  (keys `"G-CURVOFF@(u)"`) are fresh.  The comparison fresh-vs-memo is meaningful,
  but "fresh-evaluated" is not what the base side is, and the §14 addendum
  (v13 #185) asks for exactly this to be explicit.
- `render_check`'s verdict clause is `if s["text"] not in R["verdict"]["full"]` —
  a **containment** check inside `G-RENDER-FROM-GATED-OBJECT`, the #10 disease in
  miniature.  Harmless only because `G-VERDICT-STRING-EQUALITY` does the real
  comparison; it should be an ordered join equality.

**Repair.**  Put `defect_vanishes_on_homogeneous == 0` in the predicate; clear
`_LAMBDA_CACHE` (or pass `fresh=True`) on both sides of the symmetry self-test
and gate its miss count; rebuild the verdict inside `render_check` by joining the
segment texts and compare for equality.

---

## M9 (MINOR) — one anchor resolves a CWD-relative path: the instrument only runs from the repo root, and elsewhere dies by traceback rather than by gate

Every file-byte anchor joins `ROOT`; `derive_ha_code_anchor` does not:

```python
got = sha12("v13/code/ha_successor_exact.py")     # relative to the CWD
```

Measured: invoked from `v14/code/`, the plain run dies with
`FileNotFoundError: 'v13/code/ha_successor_exact.py'` and a **traceback**, not a
named gate — the one failure mode `--selftest` explicitly forbids for mutants,
and the one the delivery contract ("any gate failure aborts before any artifact
is written") does not cover.  It also means the run's provenance check silently
depends on the working directory: a repo-root-shaped CWD elsewhere on disk would
be hashed instead.

**Repair.**  `sha12(os.path.join(ROOT, "v13/code/ha_successor_exact.py"))`, and
wrap the anchor reads so a missing file fails a named gate.

---

## M10 (MINOR) — `cache-lax` kills `G-CACHE-EXERCISE` by the wrong clause; the substantive clause has no falsifier

`cache-lax` sets `tested = 0`, so the gate fires on `compared > 0` — not on
`disagreements == 0`, the clause that carries the meaning ("every memoised weight
is recomputed with the memo bypassed and compared against it").  The
disagreement counter is unexercised by any declared falsifier.  R6a's M9,
recurring.

**Repair.**  Add a mutant that returns a *wrong* fresh value (or serves another
arena's cached weight) so the death certificate is `disagreements > 0`.

---

# What I could not break — confirmations

- **The CLI contract is exactly as documented, verified in code before use.**
  No args → delivery, both artifacts written, exit 0, and every gate runs before
  either `open(…, "w")` in `deliver()`.  `--mutant NAME` → exit 1 on a named gate
  with no write; a survivor would return 3 with `MUTANT … SURVIVED` (never
  observed).  `--list-mutants` → **60** names, exit 0.  Unknown argument, unknown
  mutant and `--mutant` with no name → **exit 2** each.  Artifacts absent before
  and after all 60 mutant runs.
- **The 60-mutant table is honest to the row.**  My own 60 independent runs:
  every mutant **exit 1**, **zero tracebacks**, each dying on **exactly** the gate
  its row declares, and no artifact written by any of them.  The unit's own
  `--selftest` agrees: 60 spawned subprocesses, **60/60 DEAD**, exit 0,
  `named_gate=True` and `artifacts_unchanged=True` on every row, and the two
  artifacts still `d54142292980` / `1c8beb16c8a2` afterwards.  No gate predicate
  references mutant identity (the injections all sit in the *measurement*, never
  in a predicate), so #208 is met.
- **Two-run byte-identity, reproduced.**  Two plain runs on the scratch mirror
  emit `d54142292980` / `1c8beb16c8a2` — identical to the committed artifacts —
  with byte-identical stdout.  A third run, taken at the end of all work against
  the mid-review-updated `v14/LOG.md` (`4af35fd8cf7c`), also reproduces — see M1
  for why that is coincidence rather than reproducibility.
- **The verdict rebuilds from the receipt alone, byte-identically, and all 14
  segments flip.**  I wrote my own reconstructor from the delivered string's
  grammar, reading only the receipt's measured rows; it reproduces
  `R["verdict"]["full"]` **character for character**.  I then flipped **14 of
  14** segments with perturbations of my own design (a census row's record name,
  a matched fraction, a recovery denominator, the positive control's `closes`
  flags, a coefficient class, a `max_abs`, an `IN-CONSTRAINT` tally, a
  `vanishing_probes`, a `front_matches`, a `closing`, a lapse-move row, a new
  tally class, a trajectory row, a chart-group `closes`).  Every segment is a
  genuine function of measured values.  All seven verdict-injection mutants
  (`verdict-typed-segment`, `verdict-append-text`, `verdict-typed-coefficient`,
  `verdict-fully-typed`, `verdict-inert-segment`, `verdict-pair-swap`,
  `head-constant`) die on `G-VERDICT-STRING-EQUALITY`.
- **The coefficient pipeline reports; it does not fabricate.**  Fed a crafted
  weight with a diagonal-link component at one site — a commutator for which no
  $d\times d$ coefficient on the axis covectors exists — the solve returns the
  inconsistent branch and the cell is typed `NOT-EXTRACTABLE` (36 → 92 cells,
  exactly the 56 cells of the perturbed rule).  At the *positive control* the
  same crafted input makes `G-COEFFICIENT-EXTRACTION` fire.  The
  over-determination is real: the elimination stores independent rows per site and
  declares `NONE` on an inconsistent row, `NON-UNIQUE` on rank deficiency.  My own
  full-pivot Gaussian implementation agrees with the unit's on the class of all
  317 cells I recomputed.
- **The metric-typing comparator is genuinely two-route on the metric.**  The
  extracted coefficient reaches $q$ through `q_from_counts` (the exact linear
  solve); `type_coefficient`'s comparator reaches it through
  `q_from_counts_closed` (the closed form).  Those share no code.  They do share
  `inv_exact`, so a corruption of the inverse routine would move both sides — a
  residual #219 exposure worth a mutant, but not the same-object-different-route
  failure the protocol asks about.  `G-RECORD-IS-METRIC-TWO-ROUTES` compares
  81 of 81 cells and `readout-local` dies on it.
- **The machinery-recovery control compares against the pinned artifact, not
  against itself.**  `rank_matches_pin`, `readout_matches_pin`,
  `general_d_matches_pin`, `lattice_matches_pin` are equality against
  `rec7["tables"][…]` read from `542b8735daf0`; the closure and sector
  denominators 99 and 72 equal the pinned tables' own lengths (verified:
  `len(tables.closure) == 99`, `len(tables.sector_law) == 72`) — typed rather
  than derived, but correct.
- **Every number reproduces.**  1 585 independent field comparisons over 317
  cells, zero mismatches.  In particular, from my own implementation: 9
  admissible records at d = 2 (`G-SINGULAR` and `G-INDEF` rejected) and 5 at
  d = 3; 99 cells and 26 closing at every d = 2 arena/scope with max |ρ| = 9 at
  L = 4 and 16 at L = 5; 20 cells and 9 closing at d = 3 with max |ρ| = 8; the
  full class census (46 / 21 / 5 / 9 / 9 / 9 at d = 2, 8 / 6 / 3 / 3 at d = 3);
  the 25-member translate family at d = 2, L = 4; and by hand from the arena
  declaration: 476 census cells, 342 ordered pairs at d2L4/BASE, 21 012 `{D,H}`
  brackets (7 524 + 11 088 + 1 200 + 1 200), 10 506 / 10 506 by realisation,
  644 `{D,D}` brackets (324 + 320), 3 096 defect probes (2 376 + 720), 2 280
  homogeneous probes (1 848 + 432), 120 969 equivariance cells
  (768 + 1 875 + 24 576 + 93 750), chart-group orders 32 / 50 / 384 / 750 = |X|·d!,
  198 dense cells, 21 420 literal compositions, 4 128 `{D,H}` literal
  cross-checks, 320 convention cross-checks, and 40 = 7 + 32 + 1 anchors.
- **Zero false numbers in the paper, by value.**  All 14 rendered claims appear
  verbatim and are correct; all 64 cells of §8's hand-written L-sweep table match
  the receipt's trajectory exactly (including `128/9` and `48`); all 25 remaining
  hand-written numerals are right (7 file-byte + 32 path-value + 1 derived = 40
  anchors; 81 gates; 60 mutants; 14 verdict segments; 7 disclosures; the 5-record
  diagonal sector; the readout determinant 2; the 99/72 recovery denominators;
  the (2,4),(2,5),(3,4),(3,5) arenas; 36 of 36 pairs on 9 sites).  The paper's
  defects are the two *class* claims of M4 and M5, not a value.
- **The anchors are live.**  All 40 verify; a byte change to any of the six
  waived pinned files dies on its own row; a path drift on any of the twenty
  waived path rows dies on its own row; `A-HA-CODE`'s expectation really is
  derived from the pinned receipt's `source_sha256`.
- **The `{D,D}` control and its scrambled negative both bite.**
  `commutator-machinery` flips `G-DD-TRANSLATION-CONTROL`; `scramble-inert` flips
  `G-SCRAMBLE-CONTROL-NEGATIVE`; `covariance-break` flips `G-SYMMETRY-SELFTEST`;
  the covariance rows all carry a nonzero `nonzero_base_cells` non-vacuity count.
- **No gate is dead code.**  All 81 registered gates are evaluated on the plain
  run; the 29 never-falsified rows are all reached and pass under at least one
  declared mutant.  This is the R6a shadowed-gate defect **not** recurring.

---

# K1–K5 at instrument depth

**K1 — what carries the HDA claim.**  *(a) Is the solve well-posed and its
over-determination a real existence test?*  **Yes, measured.**  The system
$\Delta^i(x)=\sum_j c^{ij}(x)\omega_j(x)$ is assembled over every ordered lapse
pair on the support and reduced exactly; consistency is decided per site with an
explicit inconsistent branch, and my crafted counterexample (a weight with a
diagonal-link column at one site) makes it report `NOT-EXTRACTABLE` rather than
fabricate.  Uniqueness is real: the realised bracket covectors reach rank $d$ at
every site (`ranks: [2]` at d = 2, `[3]` at d = 3 in the receipt), reproduced by
my own elimination.  *(b) Is the metric-typing comparator independent (#219)?*
**Same object, two genuinely different routes** — the linear solve
`q_from_counts` on the extraction side, the closed form
`q_from_counts_closed` on the comparator side; they share only `inv_exact`,
which is a residual exposure worth a mutant, not a self-comparison.  *(c) Are the
coefficient classes themselves forced?*  Partly, and the unit says so: X03
discloses that at `A-insert` the *value* is forced.  What my recomputation adds
is that the **class census is not** forced — six classes appear across the eleven
rules, and the two site-varying classes are realised only where the record is
inhomogeneous; the 32/120 is a measurement about which (rule, record) pairs
realise the signature, and it is robust: **5 per d = 2 arena/scope and 3 per
d = 3 arena/scope, identically at L = 4 and L = 5 and identically at BASE and
TRANSLATES**, in my implementation as in the unit's.  *(d) Is SITE-VARYING
trivially inherited from record inhomogeneity?*  **No** — and the instrument
shows why: of the 120 inhomogeneous-record cells only 32 are
`METRIC-READING-SITE-VARYING`; 48 are `SITE-VARYING-NON-METRIC` (site-varying but
not the metric) and the rest are constant or unextractable.  Inhomogeneity is
necessary, not sufficient; the discrimination the paper claims is real.

**K2 — the defect's reality.**  The closed form
$w[N,(S_{-v}-1)(n-N)] - w[S_vN-N,n]$ reproduces the literal four-map composition
at all 4 128 sampled brackets and 320 front cross-checks; nonvanishing is
3 096/3 096, lattice-sum-nonzero 3 096/3 096, homogeneous vanishing 0/2 280, all
reproduced from the receipt's own 238 rows by my reconstructor.  The instrument's
caution is the same one R6a's Y1 raised and it is sharper here: **I1 shows that
erasing 3 095 of the 3 096 defect values leaves every defect gate green and
inverts all four of §6's bullet points in the emitted verdict.**  The
"characterised, not just reported" standard is met by the *presentation*, not by
the *protection*.  The realisation census (D-REG vacuous, D-TOT nontrivial) is a
declaration question for the operator lens; I record only that both realisations
are censused at every cell and that `decomposition-basis-drop` flips the
classification gate.

**K3 — the HDA correspondence.**  Instrument contribution only: the split the
correspondence rests on is `METRIC-READING-SITE-VARYING` vs
`METRIC-READING-CONSTANT`, and it is sharp in the code — `metric` and `const` are
independent exact predicates over all $|X|$ sites, and `distinct_values` is
carried per cell.  The closing sector is 26 of 99 at d = 2 and 9 of 20 at d = 3,
constant in $L$ and in the lapse scope (my recomputation agrees at all four
combinations I ran).  I note for the adjudicator that `B-axis` contributes 4
`METRIC-READING-SITE-VARYING` cells, so the signature is not confined to the
metric-inserted architecture — a fact M4's false class sentence obscures.

**K4 — scope.**  The five worker flags are printed and gated as claimed
(X06/X07 disclosed, `DENSE_ARENAS`, `LITERAL_PROBE_LAPSES = 6`,
`DH_LITERAL_PROBE = 4`, `DEFECT_PROBE_LAPSES = 6`, `DH_PROBE_DELTAS = 6` all
declared, printed in the receipt's `two_route` block, never silent).  On the
L-stability question the instrument's answer is: `G-LSWEEP-STABILITY` measures it
(`per_d` tuples collapse to one per $d$) and `lsweep-instability` flips it — but
**I7 shows the trajectory can be truncated to two rows after that gate with the
verdict still claiming `COEFFICIENT-CLASS-CONSTANT-ALONG-L=TRUE`**, so the claim
is protected at the gate and not at the render.  One scope flag the paper does
*not* carry: the convention sweep's record and rule axes are not swept at all
(M7).

**K5 — instrument.**  (a) CLI contract confirmed in code, then exercised: **187
process-level executions**; **60/60** mutants dead on their declared gate with no
traceback and no write; two-run byte-identity reproduced.  (b) **The waiver audit
at the #34 standard: 29 of 81 never falsified, 29 waived, 0 shadowed (an advance
on R6a), but 27 of the 29 demonstrably falsifiable — I killed every one — and
both SAME-MECHANISM texts false in part, one of them carrying a wrong typed
count ("eight" for twelve).**  (c) **Ten injection classes survive
proven-executed** (M2), including the Y1 defect-zeroing class, the S1/INJ_D
post-gate class, a shared-component #219 corruption at the "two independent
routes" gate, and drops in three census tables that carry no derived denominator;
three injections die correctly.  (d) Verdict rebuilt from the receipt alone
byte-identically with **14 of 14 segments flipped**; the unit's own comparator is
independent for 9 segments and a **self-comparison for 5** (M3), and the verdict
string is anchored in neither the paper nor the prose claims.  (e) The
coefficient pipeline reports `NOT-EXTRACTABLE` on a crafted inconsistent system;
the metric comparator is two genuinely different routes to $q$ sharing only the
inverse.  (f) Paper↔output↔receipt: **1 585 recomputed field comparisons plus 21
derived denominators plus 103 traced paper numbers, zero mismatches and zero
false numbers by value** — R3 joins R6a as a clean prose surface *by value*; its
two prose defects are class claims (M4, M5).  (g) All repo hashes re-verified
unchanged after all work; `git status` shows only other workers' files and this
one.

---

# Required fixes (ranked)

1. **M1** — remove `v14/LOG.md` from the run, or anchor it; replace the prose
   substring intersection with a path-value read from the anchored R2 terminal
   receipt; restate the gate and rename the receipt field, which currently claim
   evidence from a document in which the evidence does not occur.
2. **M2** — derived denominators and cell-completeness gates for the defect,
   `{D,H}` and `{D,D}` tables; `vanishing_probes == 0` and `lattice_sum_zero == 0`
   as predicates; a second, disjoint residual route so `G-CENSUS-TWO-ROUTES` can
   see a `gap_matrix` corruption, with a mutant that perturbs it; re-verify the
   payload after `jsonable()` so the post-gate `R` mutation cannot ship.
3. **M3** — rebuild RECOVERY, CONTROLS, LSWEEP, LAPSE and L-GATE in the
   comparator from raw rows; deep-copy the receipt sub-objects; add the full
   verdict string to `paper_prose()` and print it in the paper.
4. **M4** — replace §4's and X05's "exactly the architecture-B rules" with
   "exactly the `B-all` cells — 36 of the 108 architecture-B cells", and gate the
   `NOT-EXTRACTABLE` set against the computed set of rules with a nonzero
   diagonal-link weight column.
5. **M5** — build the degenerate probe and measure its lattice sum; delete the
   typed `degenerate_probe_sums_to_zero: True`.
6. **M6** — declare the twenty `path-value-*` mutants (the mechanism already
   exists) and six anchor-byte falsifiers; correct both waiver texts; add the
   shadowing-arithmetic gate; move `G-CONVENTION-RULE-INDEPENDENT` to
   `disclose()`; drop the dead `G-RECOVERY-ANCILLARY` waiver.
7. **M7** — sweep the conventions over records and rules (cheap), or report the
   685-probe denominator and carry the extrapolation as a gated disclosure; fix
   §5's "at every bracket in the census".
8. **M8** — put `defect_vanishes_on_homogeneous == 0` in its gate's predicate;
   bypass the memo on both sides of the symmetry self-test and gate its miss
   count; make `render_check`'s verdict clause an equality.
9. **M9–M10** — `os.path.join(ROOT, …)` in `derive_ha_code_anchor`; give
   `G-CACHE-EXERCISE` a mutant that dies on `disagreements > 0`.

None of these impeaches a measured number.  I recomputed 1 585 of them
independently and every one is right; the paper's prose surface is clean by
value, and the two claims that are wrong (M4, M5) are wrong about *what was
measured*, not about *what the measurement said*.  M1 is the finding that would
survive a repair of everything else: an instrument whose verdict is a function of
a file no anchor binds is not reproducible, and the delivery's byte-identity check
passed because nobody had written to the ledger in between.
