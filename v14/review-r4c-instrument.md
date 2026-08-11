# R4c / paper-22 — INSTRUMENT-LENS HOSTILE REVIEW (seat K3)

**Protocol:** v14 ledger #200, row K3. **Object:** commit `4f89135`.
**Grade: AWF** — accept with fixes. No verdict-bearing number moves; the
head `R4C-STATISTICS-BOTH-ADMITTED` is independently reproduced. Four
MAJOR instrument defects and twelve MINOR ones are listed below, each
with a liftable repair, and two of the paper's §11 sentences about the
instrument are false as implemented. The sharpest is MAJOR-4: an
injection that leaves the delivered receipt asserting `65 of 64
generators`, sealed, at exit 0, with every gate green.

## 0. Hash discipline

| object | declared at #200 | at start | committed, at end | worktree, at end |
|---|---|---|---|---|
| `v14/paper-22-multi.md` | 1b4ac134e727 | 1b4ac134e727 | 1b4ac134e727 | 1b4ac134e727 |
| `v14/code/r4c_multi_exact.py` | deb0c1c83a76 | deb0c1c83a76 | deb0c1c83a76 | **e36191a2af4a** |
| `v14/code/r4c_multi_output.txt` | 45866a3ed5e3 | 45866a3ed5e3 | 45866a3ed5e3 | 45866a3ed5e3 |
| `v14/code/r4c_multi_receipt.json` | 5c058006db78 | 5c058006db78 | 5c058006db78 | 5c058006db78 |
| `v14/note-r4c-pin.md` (pin) | 162553b03ca9 | 162553b03ca9 | 162553b03ca9 | 162553b03ca9 |

**All five committed objects are unchanged** at `4f89135` and at `HEAD`,
and I wrote to none of them. **But the instrument's working-tree copy
moved while I was writing this review**, at 14:29:23, to
`e36191a2af4a` — a repair, by another seat, that visibly answers findings
from this review: it adds `G-SEAL-PROVENANCE` (my MAJOR-4 repair, under
the name I proposed), a literal #62 consumer binding for the pin's four
walls (MAJOR-1), a `LATE_GATES` register with `G-CLI-WHITELIST` added to
`FORCINGS` (MINOR-2), and parse-time rejection of a non-existent
`--verify-paper` path (MINOR-6). Its own source comment cites this
review's INJ-11 verbatim — *"one silently failed restore() deliver a
sealed receipt asserting 65 of 64 generators at exit 0"*.

**This review is of the pinned object `deb0c1c83a76`, and nothing in it
was measured against the successor.** I checked: all 45 out-of-process
mutant results were written before 14:29:23, zero after; every other
execution had completed earlier; and I stopped the residual sweep the
moment I noticed the change rather than let it mix two objects. Any
re-measurement against `e36191a2af4a` is the next seat's work, not this
one's. Every execution below ran read-only against the repo or inside
`…/scratchpad/r4c-in/`. Files belonging to concurrent siblings are
disclaimed.

**Counts.** Executions: **122 separate processes** — 1 full `--no-write`
delivery run, 45 out-of-process `--mutant` runs, 48 `--break-anchor`
runs, 16 hostile-argv runs, 3 off-tree mirror runs, 2 further `--mutant`
timing runs (one of them, `MUT-PAPER-NUMERAL`, is the 46th distinct
mutant verified out of process), 2 source-edit falsifications, 1
`--selftest`, 1 bare-copy, 1 real byte-drift, 1 path-drift, 1 helper —
plus **6 in-process probe scripts**
driving 13 further `build_state` calls, 18 `verify_paper` calls and five
custom census recomputations. **Independent recomputations: 96** (probe 3:
20; the single-excitation census + fold probe: 8; the third-path window:
3; receipt↔paper spot checks: 36; arithmetic identities: 17; numeral
licensing re-derived from scratch: 1; pre-verify state reconstruction
fidelity: 1; anchor/gate/seal/consumer maps: 4; claim-occurrence census:
15 — minus 11 double-counted). **Zero false computed numbers found.**
Every number I recomputed agreed with the receipt.

---

## 1. The two self-caught defects: both repairs verified, and the diseases swept

### 1a. The memo cache that leaked mutant injections — REPAIRED, but the
### gate that was bought is under-bound (MAJOR-3)

The repair is real and I could not defeat it. `raw_defect_census` hands
back `copy_census(...)`, a per-field copy (`set(v)/dict(v)/list(v)`), and
every in-census mutant writes into the copy:

- `MUT-PREDICATE` → `C["wedge_nz"].add(("XX","YY"))` — the copy.
- `MUT-DISCRIMINATION`, `MUT-GENUINE-ZERO`, `MUT-FOLD`,
  `MUT-DERIVATION`, `MUT-VALUE-MULTISET` — all rebind or write copies.

**The sibling sweep (my own audit of every other cache).** There are six
further memo families keyed into the same `CENSUS_CACHE` —
`raw_exchange`, `raw_leak`, `raw_distinguishable`, `raw_overlap`,
`raw_motion`, `raw_contact`. None of them returns a defensive copy; all
six are protected instead by their *consumers*:

| cache | returns | consumer's protection | live pollution? |
|---|---|---|---|
| `raw_exchange` | the cached list | `rows = [dict(r) for r in …]` | none |
| `raw_leak` | the cached list | builds fresh dicts | none |
| `raw_distinguishable` | `(int,int)` | immutable | none |
| `raw_overlap` | 8-tuple | `list/set/dict`-copies coins, links, res, per_pair | none |
| `raw_motion` | the cached dict | `set(M["failpairs"])`; `sp2 = sp2[:-1]` rebinds | none |
| `raw_contact` | the cached dict | `dict(K)` + `set(K["moved_set"])` | none |

I could construct no in-place write to a cached object from any of the 56
declared mutants: every consumer copies before it writes, and every
in-census mutant either rebinds or writes a copy. The disease is not
live, by exhaustive reading of all seven cache families and all 56 mutant
bodies — **and the empirical sweep confirms it**: I fingerprinted every
one of the run's **7 `CENSUS_CACHE` entries** before and after each of
the 56 in-process mutant runs, and **not one entry moved** under any
mutant. The repair holds under measurement, not only under reading.

**But the gate that was bought is weaker than the paper says.** Three
separate findings, all MAJOR-3:

1. **`MUT-CACHE-DIRTY` is synthetic.** Its code is
   `dirty = ["INJECTED"] if mut("MUT-CACHE-DIRTY") else […]`. It never
   pollutes the cache; it hands the gate a canned answer. The gate's
   *detection capability* is therefore not exercised by any declared
   falsifier — an E-23 "green badge for a capability never demonstrated".
2. **`census_digest` covers 7 of the 11 cached fields, and I injected
   real in-place pollution into five of them to find out what happens.**
   It digests `single_nz, wedge_nz, sym_nz, tensor_nz, differing,
   len(deriv_fail), len(fold_fail)`; it does **not** digest `rows`,
   `wvals`, `svals`, `onevals` — and `wvals/svals/onevals` are published
   verbatim as `defect_values`. Writing into the cached object in place,
   then running:

   | field polluted | digested? | outcome |
   |---|---|---|
   | `wedge_nz` | yes | DIED at **`G-TWO-EXCITATION-PREDICATE`** |
   | `wvals` | no | DIED at `G-SECOND-CODE-PATH` |
   | `onevals` | no | DIED at `G-PARENT-VALUE-MULTISET` |
   | `svals` | no | **SURVIVED — exit 0** |
   | `rows` | no | **SURVIVED — exit 0** |

   Two of the five deliver at exit 0 with a polluted cache, and `svals`
   is a *published* table (`defect_values/symmetric`): nothing catches
   it, because `G-DEFECT-RATIONAL` tests only the keys and the paper's
   `CL-VALUES` claim tests only `len`.

   **And note which gate never appears in that column.**
   `G-CACHE-UNPOLLUTED` did not fire on a single one of the five. The
   three that die, die at earlier measurement gates; the two that live,
   live. The gate sits near the end of `build_state`, after every gate
   that would have caught the pollution anyway, so on this instrument it
   is inert against real pollution — its only trigger is its own
   synthetic mutant.
3. **The gate inspects one cache entry of seven.** Its predicate filters
   `if k == pk`, and `CENSUS_DIGESTS` is written only in
   `raw_defect_census`. The receipt's own detail line says so:
   `"1 cached censuses, 0 polluted"` — while the run's cache holds
   **seven** entries, measured.

The paper's §11 sentence — *"the cache hands back defensive copies and a
gate re-checks the cached census's digest on every build, so no
injection, this run's or an earlier run's, can reach the next run through
it"* — overstates on both halves: one of seven caches copies, and the
digest covers part of one of them. **This is a false prose claim about
the instrument.**

**Repair (liftable, small).**
(a) Replace `MUT-CACHE-DIRTY` with a mutant that genuinely writes into
    `CENSUS_CACHE[pool_key(circ)]["svals"]` in place before the gate, and
    keep the synthetic one as a second row.
(b) Fingerprint every cache entry, not one: at creation store
    `CENSUS_DIGESTS[k] = digest(repr(v))` in *all six* `raw_*` functions
    and let the gate iterate the whole dict.
(c) Give the six non-copying caches the same `copy_*` discipline so the
    §11 sentence becomes true as written.

### 1b. The seal taken over objects that afterwards moved — REPAIRED at
### the late seals only; the same disease is still open at the other
### twenty-four (MAJOR-4)

The repair is present and correct **where it was applied**. In `main()`
the order is: `G-PAPER-COVERAGE-FINAL` → `totals["gates"]`/`gates_passed`
recomputed → `S["gates"] = LD.rows` → **then** `SEAL.take` for the six
`SEALS_LATE` → `S["seals"]` → the seal-count cross-check → `render` →
`payload` → `SEAL.close(S, payload)`, which re-verifies **all thirty**
seals before digesting the payload. Nothing mutates `S` after the late
seals; `render()` only reads. `MUT-SEAL-BROKEN` (mutate a sealed object
after its seal) dies at `G-SEAL-COMPLETE`, on target, in my own full
delivery run. That half is sound and I could not defeat it.

**But the twenty-four `SEALS_IN_RUN` are not taken at their gates
either.** They are taken in one loop at the very end of `build_state` —
after every measurement gate, and after `verify_paper`. And
`verify_paper`'s polarity test runs
`perturb(S, path)` / `restore(S, path, old)` over thirteen **sealed**
paths in that window.

**INJ-11, the demonstration.** I neutered `restore()` for the first claim
only — one silently failed restore, the smallest possible fault.

```
INJ11-restore-neutered   SURVIVED-EXIT-0   gates=60
  counts/single_nonzero = 588
  exchange_census/antisymmetric_admitted = 65      <-- there are 64 generators
  verdict string still says  BOTH-SECTORS-CLOSED-UNITARY-STOCHASTIC=64-OF-64
  SEAL-EXCHANGE  sha256_12 = d65ee74d6650  (delivered: 4f62dd5c49e2)
                 sealed_at_gate = G-PUBLISHED-ROWS-BOUND   <-- no such gate
  SEAL.verify broken: []
```

Every gate passes. The seal is taken **over the corrupted object** and
verifies perfectly, because it was minted after the corruption. The
receipt is delivered internally inconsistent — `counts.pool = 64` beside
`exchange_census.antisymmetric_admitted = 65`, and a verdict string,
built earlier, that contradicts both. Nothing cross-checks the verdict
string against the receipt fields it was rendered from, and the seal's
own provenance column names a gate that never ran (MAJOR-1).

This is the same #119/#148 defect the unit caught in itself, repaired at
six seals out of thirty, and left open at the other twenty-four. The
paper's §11 sentence — *"Every object the unit vouches for … is digested
at the moment its gate passes"* — is false, and INJ-11 shows it is
load-bearing.

**Repair.** (a) Move each `SEAL.take` to the line after its gate passes;
the `SEALED_PATHS` table already names the intended gate. (b) Add
`G-SEAL-PROVENANCE`: every `sealed_at_gate` value must be in `LD.ids`
*and* must have been evaluated before its digest was taken. (c) Make
`perturb`/`restore` non-destructive — run the polarity test on
`copy.deepcopy(S)` — so the delivery state is never mutated at all.
(d) Add a cheap cross-check that every numeral interpolated into the
verdict string still equals its receipt field at seal time.

---

## 2. MAJOR-1 — thirty published rows name a gate that does not exist

This is the largest finding and it is squarely in-era.

`G-VERBATIM-ANCHORS`, `G-PATH-VALUE-ANCHORS` and the seal ledger each
publish a *consumer* column. Checking those names against the run's own
63-gate ledger:

| ledger | rows | rows naming a phantom gate |
|---|---|---|
| `verbatim_anchors` | 12 | **12** |
| `path_value_anchors` | 24 | **3** |
| `seals` | 30 | **15** |

Twelve distinct phantom names are published and sealed:
`G-PUBLISHED-ROWS-BOUND` (13 seals), `G-RECEIPT-SCHEMA` (2 seals),
`G-MARKOV-INHERITED`, `G-R4B-CONVENTION-INHERITED`,
`G-PIN-QUESTION-IS-THE-PARENTS`, `G-SECTOR-IS-NEW`,
`G-DEFECT-DEFINITION`, `G-CONNECTIVE-VERBATIM`, `G-R5-PRECEDENT-CITED`,
`G-NO-TRANSPORT-NUMBER-INHERITED`, `G-NO-PARTICLE-NAMING`,
`G-DEFECT-WITNESS`. None appears in `LD.rows`.

This is exactly the class the §14 amendment of **v14 #62** was engraved
for: *"every consumer gate must exist, be non-literal, and be falsified
by a declared mutant. An anchor whose consumer is an unread label binds
existence, not meaning."*

**What it costs, measured.** The anchors still bind *bytes* — I perturbed
all 48 and all 48 killed the run (§5) — so quote fidelity against the
parents is genuinely discharged. What is *not* discharged is the meaning
the consumer name promises:

- **The pin's no-particle-naming wall has no instrument.** `VB-PIN-SHAPES`
  quotes the wall out of the pin and names `G-NO-PARTICLE-NAMING`, which
  does not exist; nothing scans this paper for banned words. INJ-16
  rewrote the paper's own wall sentence to *"A particle is named.
  Fermion and boson are particle words"* and the run passed all paper
  gates at 52 numerals, 0 unlicensed.
- **The connective clause is not compared to its anchor.** `VB-CONNECTIVE`
  pins `CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1))` in the
  *parent's* bytes; this unit then types the same string as a literal
  into its own SCOPE segment and prints it in an inline span in §2. No
  gate compares the three. INJ-1 altered the §2 span to `LINK-(1,2)` and
  the run passed.
- **The R4b convention inheritance is anchored and unconsumed.**
  `PV-R4B-TIE` (`"TIE-AVERAGED"`) and `PV-R4B-STENCIL`
  (`["FORWARD","BACKWARD"]`) name `G-R4B-CONVENTION-INHERITED`, absent;
  `motion/convention` is a typed literal
  (`"FORWARD-DIFFERENCE-WITH-TIE-AVERAGED-INHERITED-AS-DECLARED"`) that
  no gate ties to those values. The *numbers* are reproduced
  (`G-R4B-CONVENTION-REPRODUCED`, which I confirmed independently); the
  *convention word* is not.
- **`VB-SEED-DEFECT` is decorative.** Its needle is the four characters
  `"Born"`, hunted in `v12/paper1-composition-defect.md`, and the
  40-character floor is explicitly waived for it *inside the gate's own
  predicate* (`if r["anchor"] != "VB-SEED-DEFECT"`). The published detail
  reads `"12 windows, floor 50 chars"`, which conceals it; only the row's
  own `chars: 4` discloses it. Its consumer `G-DEFECT-WITNESS` does not
  exist. This anchor binds nothing.

**Birth-date ruling: NOT excused.** Three independent reasons. (i) The
governing engraving is #62, long before this unit's launch at #174.
(ii) The unit's own byte-pinned parent — `r4b_momentum_receipt.json`,
which this instrument reads as `R4B-RECEIPT` — publishes 14 verbatim,
20 path-value and 8 byte anchors with **zero** phantom consumers and 18
seals with **zero** phantom `sealed_at_gate`. (iii) A contemporaneous
sibling shipped the explicit gate: `G-ANCHOR-CONSUMERS` is present in
`v14/code/coupling_exact.py` at commit `9b1860e` (v14 **#179**), sixteen
entries before this unit's delivery.

**Repair (a straight port).**
(a) Add `G-ANCHOR-CONSUMERS` verbatim from `coupling_exact.py` §"#62's
    consumer binding", extended to cover `PATH_VALUES` and
    `SEALED_PATHS`, with a mutant that injects a phantom name.
(b) Build the four consumer gates that carry real content:
    `G-NO-PARTICLE-NAMING` (scan this paper against a declared banned-word
    list, with a mutant that inserts one), `G-CONNECTIVE-VERBATIM`
    (require the anchored clause, character for character, in the SCOPE
    segment *and* in the paper), `G-R4B-CONVENTION-INHERITED` (derive
    `motion/convention` from `PV-R4B-TIE` + `PV-R4B-STENCIL` instead of
    typing it), `G-R5-PRECEDENT-CITED` (bind
    `overlap_census/r5_rows_cited_not_rerun == 18` to `VB-R5-EIGHTEEN`).
(c) Either rename `G-PUBLISHED-ROWS-BOUND`/`G-RECEIPT-SCHEMA` to the
    gates that actually precede those digests, or construct them.
(d) Replace `VB-SEED-DEFECT`'s needle with a ≥40-character window from
    v12 paper 1 carrying the defect *definition*, and delete the
    exemption clause from `G-VERBATIM-ANCHORS` so the published floor is
    the true floor.

---

## 3. MAJOR-2 — the paper instrument is set-membership over a 218-element
## pool; twelve of seventeen injections survive at exit 0

### 3a. What it does bind (and does bind well)

`numerals()` scans the **raw** paper bytes — no fence stripping, no span
stripping — so E-22's *coverage* half is satisfied by construction and
exceeded: inline code spans and fenced blocks are scanned. Three
injections of an unlicensed numeral (in an inline span, in a duplicated
fence, in prose) all died at `G-PAPER-NUMERAL-COVERAGE`. Deleting a claim
died at `G-PAPER-CLAIMS`. Forging the head *inside the single fence* died
at `G-PAPER-VERDICT-BLOCK`. Independently re-implementing the licensing
from the receipt, I get the same **52 numerals, 0 unlicensed**.

### 3b. What it does not bind — the injections table

Run through the instrument's own `verify_paper` on a state reconstructed
from the published receipt; fidelity proved first (the reconstruction
reproduces the published `paper_coverage` row exactly on the pristine
paper).

| # | injection | where | caught by | exit | wrote |
|---|---|---|---|---|---|
| 1 | inline span `LINK-(1,1)` → `LINK-(1,2)` | §2 backticked span | **nothing** | 0 | nothing |
| 2 | inline span `(1,1)` → `(1,7777)` | §2 backticked span | `G-PAPER-NUMERAL-COVERAGE` | die | nothing |
| 3 | verdict fence duplicated, twin `1764→588` | fenced block | **nothing** | 0 | nothing |
| 4 | verdict fence duplicated, twin `1764→4242` | fenced block | `G-PAPER-NUMERAL-COVERAGE` | die | nothing |
| 5 | overlap table rows 0/1 swapped | table | **nothing** | 0 | nothing |
| 6 | sector table `588`↔`1764` swapped | table | **nothing** | 0 | nothing |
| 7 | prose `1764` → `9999` | prose | `G-PAPER-NUMERAL-COVERAGE` | die | nothing |
| 8 | prose `1764` → `588` (one of three copies) | prose | **nothing** | 0 | nothing |
| 9 | head forged in the fence | fenced block | `G-PAPER-VERDICT-BLOCK` | die | nothing |
| 10 | claim sentence deleted | prose | `G-PAPER-CLAIMS` | die | nothing |
| 12 | arena table head words swapped | table | **nothing** | 0 | nothing |
| 13 | arena table lives/dies inverted | table | **nothing** | 0 | nothing |
| 14 | verdict fence duplicated verbatim | fenced block | **nothing** | 0 | nothing |
| 15 | **second fence: `R4C-STATISTICS-FORCED-ANTISYMMETRIC<…GENUINE-TWO-BODY=0>`** | new fenced block | **nothing** | 0 | nothing |
| 16 | the no-particle wall inverted | prose | **nothing** | 0 | nothing |
| 17 | overlap-2 positive control zeroed (`360 360 360` → `0 0 0`) | table | **nothing** | 0 | nothing |
| 18 | the paper's headline sentence inverted | prose | **nothing** | 0 | nothing |
| 11 | `restore()` neutered for one claim (§1b) | instrument | **nothing** | 0 | nothing |

Of the seventeen **paper** injections, 5 die and **12 survive**; INJ-11
(an instrument injection, §1b) is listed here for completeness and also
survives. Every paper survivor reports the clean paper's own
coverage row: `52 numerals, 0 unlicensed, 15 claims, 0 polarity
failures`. Injections 1–10 and 11 were run through the instrument's full
`build_state` path (60 gates) on the off-tree mirror; 12–18 were run
through `verify_paper` on a state reconstructed from the published
receipt, whose fidelity was proved first by reproducing the published
`paper_coverage` row exactly. Injections 1–10 give identical outcomes on
both routes, which is the cross-check on the reconstruction.

### 3c. The three mechanisms

1. **Licensing is set membership over a 218-element pool**, and 39 of
   those members are supplied by the sha256-12 digest strings alone.
   Fifteen of the paper's fifty-two numerals — `0 1 2 3 4 5 6 7 8 9 10 12
   14 18` and, notably, **`256`** — would still be licensed if every
   measured value were deleted from the receipt, because a hex digest
   supplies them. And because the test is set membership, any licensed
   value may be written anywhere in the paper.
2. **Claim matching is containment, and eleven of the fifteen claim
   strings occur two to five times in the paper** (`CL-PARENT` five
   times, `CL-ADMITTED` four, `CL-DECOMP`/`CL-LEAK`/`CL-TWOEXC`/
   `CL-GENUINE` three each). Corrupting any single instance leaves the
   claim satisfied by its twins — injection 8.
3. **Fenced blocks are gated by containment, and tables are not claims at
   all.** `vs in norm` is satisfied by one clean copy no matter what
   else the paper carries — injections 3, 14, 15. No table cell renders
   from a receipt path — injections 5, 6, 12, 13, 17.

### 3d. Birth-date ruling — split

- **The multiset/table half is birth-date-fair.** E-22 was bought at
  #187, thirteen entries after this unit's launch at #174; the machinery
  that answers it (`block_multiset`, `paper_tables`, `SEAL-PAPER-TABLES`,
  `G-PAPER-TABLES`, and the `trows`/`blockmap` mutants) first exists in
  `coupling_exact.py` at **#198**, three entries *after* paper-22 was
  delivered. Injections 3, 5, 6, 12, 13, 14, 17 are excused as gaps and
  charged as repairs.
- **Injection 15 is NOT excused.** The #20 addendum at **#168** —
  pre-birth — names its own demonstrated failure: *"a paper with a forged
  head (ISOS=4242, FORCED-999) passed verify-paper with the clean paper's
  scan count."* Injection 15 reproduces that sentence exactly: a second
  fenced block asserting `FORCED-ANTISYMMETRIC` and
  `GENUINE-TWO-BODY=0` passes with the clean paper's scan count. The unit
  fixed the mechanism #168 named (it does scan fences) without closing
  the failure #168 demonstrated.
- **Injections 16 and 18 are NOT excused** — they are MAJOR-1's phantom
  consumers biting, under the #62 amendment.
- **Injection 8 is NOT excused** — #125 ("text gates match text as
  written", #125, pre-birth) and #20's "prose renders from the receipt"
  both bear on it; a claim gate that a duplicate can shadow is the same
  defect #125 was engraved against, in a different coordinate.

**Repair.** Port `block_multiset` and `paper_tables` from
`v14/code/coupling_exact.py` (they are written for exactly this); render
the three tables as claim rows and seal them; change `G-PAPER-CLAIMS`
from `t in norm` to `norm.count(t) == expected`, with the expected count
derived, not typed; drop digest strings from the license set and license
only measured integers, declared value-strings and `STRUCTURAL`; add a
banned-word scan for the walls and bind the paper's prose head to
`verdict/head`.

---

## 4. The full 56-mutant sweep, outside the harness

Every mutant was run in its own cold process, `--mutant NAME`, against
the repo, with the three artifacts hashed before and after each run and a
check for stray `.tmp`/`.probe` files.

**Result on the 46 completed: 46 of 46 — every one killed, every death at
its declared target gate, `rc=1`, the three artifacts byte-UNCHANGED
after each run, zero stray `.tmp`/`.probe` files, zero off-target, zero
survivors.** The raising gate was parsed out of each run's own
`MUTANT … died at …` line and compared to the registry row. The 46 span
every stage of the pipeline: the anchor phase (`MUT-VERBATIM-FRAGMENT`,
`MUT-PATH-ANCHOR`, `MUT-ARENA-SIZE`, `MUT-SHELL-IMPORT`), the rebuild
(`MUT-GAUGE-ORBIT`, `MUT-ALPHABET`, `MUT-REBUILD-DROP`,
`MUT-CONTROL-COUNT`, `MUT-INVARIANT`, `MUT-POOL-COUNT`,
`MUT-MONOMIAL-LIST`), the exchange and occupancy censuses
(`MUT-SECTOR-DIM`, `MUT-EXCHANGE-COMMUTE`, `MUT-BOTH-ADMITTED`,
`MUT-LEAK-ZERO`, `MUT-CEILINGS`, `MUT-REGISTER`), the four arenas
(`MUT-A3-DIM`, `MUT-A3-LIVES`, `MUT-A4-COMMUTE`), the defect census
(`MUT-PARENT-COUNT`, `MUT-PREDICATE`, `MUT-DISCRIMINATION`, `MUT-FOLD`,
`MUT-VALUE-MULTISET`, `MUT-GENUINE-ZERO`, `MUT-DERIVATION`,
`MUT-IRRATIONAL`, `MUT-SECOND-PATH`), the overlap census
(`MUT-COIN-ALPHABET`, `MUT-THREE-SITE`, `MUT-OVERLAP-LAW`,
`MUT-COIN-PAIR`, `MUT-OVERLAP-BITE`), motion (`MUT-EIGENPHASE`,
`MUT-ADDITIVITY`, `MUT-SPECTRUM-SPLIT`, `MUT-R4B-REPRO`,
`MUT-VELOCITY-ADD`, `MUT-SPEED-CEILING`), the contact handle
(`MUT-CONTACT-BLIND`, `MUT-CONTACT-SET`), the third route
(`MUT-THIRD-PATH`), the stamps and waivers (`MUT-STAMP-DROP`,
`MUT-WAIVER-UNFORCED`) and the paper gates (`MUT-PAPER-NUMERAL`).

**The remaining 10 did not finish inside the review window** — this
machine was carrying a load average above 200 from the concurrent seats
throughout, and a single cold `--mutant` run that reaches the paper gates
costs about eight CPU-minutes. They are:
`MUT-CACHE-DIRTY, MUT-HEAD-PRENAME, MUT-HEAD-TYPED, MUT-PAPER-CLAIM, MUT-PAPER-POLARITY, MUT-PAPER-VERDICT, MUT-PAYLOAD-PATH, MUT-RECEIPT-FLOAT, MUT-SEAL-BROKEN, MUT-SEAL-TOTAL`.
**This is a disclosed protocol shortfall, not a
finding**: all 10 are covered in-process four times over — by the committed
receipt's own sweep and by my independent full `--no-write` delivery run
(21 m 45 s, from the committed source), which reported
`ALL GATES PASSED (63/63); ALL MUTANTS DEAD (56/56)` at exit 0 with the
repo artifacts untouched, and by both off-tree mirror runs.
**Order-independence checked separately:** running the whole in-process
sweep in REVERSED registry order also put **56/56 on target**, so no
mutant's verdict depends on what ran before it.
Nothing in the 46 that did run gives any reason
to expect the other 10 to behave differently out of process; the sweep
should nonetheless be completed before terminal.

**`--list` is not a flag this unit ships**, so ledger row #24's registry
cross-check was done directly against the source and the receipt, and it
is exact:

- `len(MUTANTS)` = 56 = `len(receipt.mutants)` = `totals.mutants` =
  `totals.mutants_killed` = `totals.mutants_on_target`.
- Every receipt row equals its registry tuple **in order**, on all three
  fields — name, target gate and published description.
- `died_at == target` on all 56 rows; 55 distinct target gates, the one
  repeat being `G-ARENA-TWO-WAY` (legitimately targeted from two
  different arenas by `MUT-A3-DIM` and `MUT-A3-LIVES`).
- The other totals are self-consistent too: 63 gate rows = `totals.gates`
  = `totals.gates_passed`; 12 + 24 + 12 = 48 = `totals.anchors`; 30 seal
  rows = `totals.seals`.

### 4a. E-23 — falsifier descriptions against their code (20 audited)

Seventeen of twenty descriptions are accurate. Three drift:

| mutant | declared | code | verdict |
|---|---|---|---|
| `MUT-SPEED-CEILING` | "widens the two-excitation speed spectrum" | `sp2 = sp2[:-1]` — **narrows** it | **description inverted** (MINOR-3) |
| `MUT-CACHE-DIRTY` | "reports a polluted cache" | fabricates the report; never pollutes | **capability never exercised** (MAJOR-3) |
| `MUT-IRRATIONAL` | "claims an irrational defect value" | flips a boolean; injects no value | drift, harmless |

None purchases a false green badge except `MUT-CACHE-DIRTY`, which does.

### 4b. E-23 — every load-bearing row's falsifier or forced waiver

Of the 63 gates, 55 are a declared mutant's target and 3 are DISCLOSUREs
with waivers. **Five have neither a mutant, nor a waiver, nor an entry in
the `FORCINGS` register**: `G-BYTE-ANCHORS`, `G-NO-FLOAT`,
`G-MUTANT-SWITCH-CLEAN`, `G-HEAD-LAW-EXERCISED`, `G-CLI-WHITELIST`.
I falsified three of them myself, so they do bind:

- `G-BYTE-ANCHORS` — `--selftest` (exit 1, writes nothing), all 12
  `--break-anchor` runs, and a **real on-disk byte drift** on a mirror
  (one appended newline in `paper-15-momentum.md`) all kill it.
- `G-NO-FLOAT` — inserting `_PROBE = 1.5` into a mirror copy of the
  source kills it at that gate.
- `G-MUTANT-SWITCH-CLEAN` — putting `mut("MUT-NOPE")` inside a gate
  predicate kills it at that gate.
- `G-HEAD-LAW-EXERCISED` — **it binds, and I demonstrated it**: I
  collapsed `head_law` so that two of the four arenas return the same
  pre-registered name, and the run died at `G-HEAD-LAW-EXERCISED`. It is
  the unit's #34 reachability discharge and it works; what it lacks is a
  *registered* falsifier, because the three arena mutants all die
  earlier at `G-ARENA-TWO-WAY`/`G-A4-NEITHER-REACHED`. One-line repair:
  add `MUT-HEAD-LAW-FLAT` targeting it.
- `G-CLI-WHITELIST` is the only gate for which I have **no demonstrated
  falsifier at all**, and it is also missing from `FORCINGS`.

**The `FORCINGS` register is incomplete.** It declares three gates as
unreachable-by-mutant (`G-MUTANTS-ON-TARGET`, `G-ARTIFACT-INTEGRITY`,
`G-PAPER-COVERAGE-FINAL`) and I verified all three forcings are sound.
But `G-CLI-WHITELIST` is evaluated in `main()` after `build_state` and is
equally unreachable by any in-process mutant, and it is neither in
`FORCINGS` nor a mutant's target — while `cli_probes` is a sealed,
published row (`SEAL-CLI`). Under E-23 that row is unguarded.

### 4c. The three disclosures, and their forcings audited

| gate | forcing | is the forcing machine-checked? |
|---|---|---|
| `G-EXCHANGE-COMMUTES` | *P(U⊗U)P⁻¹ = U⊗U for every U* — an identity of the free lift | the *claim* is measured per generator (`matmul(P,T)==matmul(T,P)`, 64/64, reproduced independently); the forcing itself is prose. Sound. |
| `G-HARDCORE-ANTISYMMETRIC-CLOSED` | *the wedge carries no doubly-occupied configuration* | **no.** The row `antisymmetric_hardcore_closed` is the **typed constant `True`** on all 64 rows, and there is no mutant. (MINOR-4) |
| `G-EIGENPHASES-ADD` | *the sectors are functors* | the claim *is* measured as an exact matrix identity at 6960 + 7888 cells with 0 failures; `MUT-ADDITIVITY` kills it. Sound. |

`G-WAIVERS-VERIFIED` checks only `len(forcing) > 80` and set-equality
against the DISCLOSURE gates; #34's "machine-checked forcings" is met in
substance for two of three. **Repair for the third is one line:** compute
`hardcore_leak(wedge(U))` per generator instead of typing `True`, and add
`MUT-WEDGE-LEAK` to falsify it.

---

## 5. The 48 anchors, the 30 seals, manifest totality, post-write corruption

**Anchors — all 48 perturbed, not a sample.** Every anchor was broken
individually via `--break-anchor` and every one killed the run at its own
gate: 12/12 byte → `G-BYTE-ANCHORS`; 24/24 path-value →
`G-PATH-VALUE-ANCHORS`; 12/12 verbatim → `G-VERBATIM-ANCHORS`. All 48
runs `rc=1`, repo artifacts UNCHANGED. In addition, a *real* on-disk
drift of an anchored parent (not the in-memory switch) killed the run at
`G-BYTE-ANCHORS` and wrote nothing.

**Seals.** 30 rows; `G-SEAL-COMPLETE` verifies the 24 in-run seals
(`MUT-SEAL-BROKEN` kills it); `SEAL.close` re-verifies all 30 before the
payload digest; the published `totals.seals` is cross-checked against
`len(SEAL.rows)` and raises if they disagree. **Manifest totality
holds**: the artifact publishes exactly 29 keys, 28 sealed and `seals`
declared unsealed with its reason, and the writing path re-checks the
on-disk key set against `FINAL_KEYS`. `MUT-SEAL-TOTAL` kills it. The
defects are the *provenance* of the seals (MAJOR-1) and the *timing* of
the in-run batch (MINOR-1), not the mechanism.

**Post-write corruption injection — the gate fires.** I patched an
off-tree mirror so the bytes written to `r4c_multi_receipt.json` differ
from the sealed payload by exactly one trailing space. The run reached
`ALL GATES PASSED (63/63); ALL MUTANTS DEAD (56/56)` and then died:

```
G-ARTIFACT-INTEGRITY :: the bytes on disk are not the sealed bytes
rc=2
```

The check is genuine and two-way by construction: it compares
`digest(on_disk_json)` against `SEAL.payload_sha` — the gate-time seal,
never a re-derivation from disk — *and* writes a deliberately corrupted
`payload + "X"` to a `.probe` path, re-reads it and requires the
corruption to be detected, *and* re-checks the on-disk key set against
`FINAL_KEYS`. A one-byte difference is caught.

**MINOR-5, now demonstrated rather than read: the corrupted artifact is
left on disk.** After the failed check, the mirror's
`r4c_multi_receipt.json` is **108,114 bytes** (the correct payload is
108,113), sha256-12 `95ad699a5c4a`, with the injected trailing space
still in place — and `r4c_multi_output.txt` was written beside it. So an
integrity failure exits 2 having already promoted the bad bytes to their
final path, leaving a receipt and a transcript on disk that do not
correspond. **Repair:** write both `.tmp` files, verify both against the
seal, and only then `os.replace` both.

---

## 6. The three-code-path window (the declared 144-pair window)

The declaration is honest and the window is alive; the residual issue is
that no invariance across windows is measured.

- The window is `circ[:12]` = `C000…C011`, the first twelve generators in
  **the parent's own naming**, 12² = 144 ordered pairs. The gate detail
  publishes `144 ordered pairs, 24 distinct values`, the receipt carries
  `defect_values/third_path_window_pairs = 144`, and the paper says "a
  declared window — the first twelve generators in the parent's own
  naming, 144 ordered pairs — and agrees there". Honest denominator
  (#34): the window is 144 of 3364, and it is never presented as the
  census.
- **The window bites.** I recomputed it independently: 4 of the 12 are
  monomial, 8 non-monomial, so the predicate forecasts 8² = 64 nonzero
  pairs — and 64 of 144 measure nonzero, with 24 distinct values over
  69,888 compared cells. The third route (`defect_crossterm`, the
  explicit interference sum) agrees with the definitional route on the
  whole window under my own re-implementation.
- **The route really is structurally independent**: it forms no composite
  matrix and no product of Born matrices, and the identity
  `B(A₂A₁) − B(A₂)B(A₁) = Σ_{m≠m′}` is exact. Its comparator re-derives
  `defect()` rather than reading `C["wvals"]`, which is the right shape
  for #82.
- **MINOR-11:** no invariance across window choices is gated (§15 asks
  for arena-relative claims to be stamped as such). One disjoint second
  window, or a gate requiring the window to contain at least one pair of
  each predicate class, closes it.
- **MINOR-10:** `defect_crossterm` skips its diagonal by *object
  identity* (`if u is v: continue`) rather than by index. It is correct
  here only because every product is a freshly allocated tuple (`ZERO` is
  filtered out before the list is built) — which I measured: over
  **136,704** accumulator cells, **zero** carry a duplicate object
  identity. One index loop removes the fragility.

---

## 7. CLI

**Hostile argv sweep — 15 of 16 clean.** `--nope`, `-h`, `--help`, the
empty string, `--mutant` (trailing arity), `--mutant NOPE`,
`--mutant MUT-CACHE-DIRTY --mutant` (trailing arity after a valid pair),
`--break-anchor` (trailing arity), `--break-anchor NOPE`,
`--verify-paper --nope`, `--no-write extra`,
`--selftest --no-write extra`, `--no-write --no-write --nope`,
`--MUTANT MUT-FOLD` (case), `--mutant=MUT-FOLD` (equals form) — all
**exit 2** with a whitelist error and write nothing.

**MINOR-6, the sixteenth.** `--verify-paper /nonexistent/paper.md` is not
validated at parse time: the run performs the entire ~8-minute census and
then dies at `G-PAPER-PRESENT` with an **uncaught `GateFail`
traceback** (exit 1). The same shape appears twice more: a **bare copy**
of the instrument in an empty tree dies with a `FileNotFoundError`
traceback (exit 1, writes nothing, no stray files — the death is correct,
the *form* is not a gate), and a mirror with one anchored source removed
dies the same way. **Repair:** validate the `--verify-paper` path in
`parse_args` (exit 2), and wrap the `SOURCES` read so a missing path
raises `GateFail("G-BYTE-ANCHORS :: …")`. Also catch `GateFail` in
`main()` and print the mutant path's `died at …` line so a plain-run gate
failure is not a traceback (MINOR-13).

**`G-ARTIFACT-INTEGRITY` disk-vs-seal probe re-run:** on the clean mirror
runs the gate printed
`disk bytes == gate-time seal (payload …, transcript …); a corrupted
probe was detected` and exited 0; on the corrupted mirror it exited 2
(§5).

**`--list` counts:** no such flag. Registry ↔ receipt cross-check done
directly (§4).

---

## 8. Byte reproduction off-tree, git-less, across hash seeds

A provisioned mirror was built at
`…/scratchpad/r4c-in/mirror` containing only the instrument, this unit's
paper and pin, and the twelve anchored sources at their repo-relative
paths. **No `.git` anywhere.**

**CONFIRMED, and three ways rather than two.** `PYTHONHASHSEED=0` and
`PYTHONHASHSEED=12345`, two independent copies of the mirror, both ran to
`EXIT 0` at `ALL GATES PASSED (63/63); ALL MUTANTS DEAD (56/56)` and
printed
`G-ARTIFACT-INTEGRITY passed: disk bytes == gate-time seal (payload
5c058006db78, transcript 45866a3ed5e3); a corrupted probe was detected.`

| artifact | mirror, seed 0 | mirror, seed 12345 | committed |
|---|---|---|---|
| `r4c_multi_output.txt` | `45866a3ed5e3` | `45866a3ed5e3` | `45866a3ed5e3` |
| `r4c_multi_receipt.json` | `5c058006db78` | `5c058006db78` | `5c058006db78` |

`cmp` confirms all four pairings byte for byte: seed-0 ≡ seed-12345, and
each ≡ the committed artifact. So the delivered bytes reproduce **off
the tree, with no `.git` anywhere in the mirror (verified: zero found),
under two different hash seeds, on a machine that was simultaneously
running eight other jobs** — and they reproduce *the committed bytes*,
not merely each other, which is the stronger claim.

- Supporting: the payload is gated byte-identical across two
  serializations and free of absolute paths
  (`G-PAYLOAD-DETERMINISTIC`; `MUT-PAYLOAD-PATH` kills it), and `ROOT` is
  derived from `__file__` so nothing is tied to this checkout.
- Incidental but worth recording: the in-process 56/56 mutant sweep has
  now been reproduced **four independent times** — the committed
  receipt's own, my repo `--no-write` run, and both mirrors.
- The run consults no version-control state; `G-NO-VERSION-CONTROL-NO-SHELL`
  scans for `subprocess`/`shutil`/`socket` imports and
  `system`/`popen`/`run`/`check_output` calls, and `MUT-SHELL-IMPORT`
  kills it out of process.
- **Bare-copy death writes nothing**: the instrument alone in an empty
  tree exits 1, leaves exactly the one file it was given, and creates no
  `.tmp` or `.probe`.
- I read the determinism surface by hand as well: every sort is over
  ordered tuples of integers or strings, every digest goes through
  `json.dumps(sort_keys=True)`, and there is no `sorted(key=repr)` over
  an unordered container (the v10-layer tie-break class of #160 does not
  arise — this unit reads `v13/code/ha_successor_receipt.json` as
  anchored values only and drives no d60 constructor). The only two
  hash-order-dependent expressions in the file, `set(list(…)[:-1])`, sit
  inside the bodies of `MUT-DISCRIMINATION` and `MUT-CONTACT-SET`; both
  gates are set equalities, so *which* element is dropped cannot change
  the outcome, and a mutant run reaches no writer.

---

## 9. Paper ↔ output ↔ receipt numeral sweep

The claim of **52 numerals, 0 unlicensed** is verified, and verified
twice: once by the instrument, once by an independent re-implementation
of `numerals`/`licensed_numerals` over the receipt keys that existed when
`verify_paper` ran. Both give 52 and 0.

Thirty-six receipt↔paper spot checks agree exactly, and seventeen
arithmetic identities behind the headline numbers hold: 58² = 3364,
58·57 = 3306, 42² = 1764, 58 − 16 = 42, 1764 − 588 = 1176,
3364 − 588 = 2776, 2·3364 = 6728, 16² = 256, 16·17/2 = 136, 16·15/2 = 120,
136 − 120 = 16, 32760 + 10080 = 42840, +360 = 43200 = 3·120²,
58·16·2 = 1856, 58·16·2·16 = 29696, 58·120 = 6960, 58·136 = 7888.

Independent recomputations of the load-bearing censuses. **The honest
scope of my independence:** I re-implemented the *census bookkeeping* —
the loops, the predicates, the set algebra, the lift table, the velocity
and tie counting, the separation-profile fold, the swap matrix, the
contact phase, the sample selection — over the instrument's own
exact-arithmetic and sector primitives (`fmul`, `matmul`, `born`,
`wedge`, `symsq`). I did **not** rebuild the field or the sectors from
the definitions; that is the K1 operator seat's job, and my numbers do
not corroborate those primitives. What they do corroborate is every
counting, matching and set-equality step between the primitives and the
published rows — which is where an instrument review's exposure lies.

| quantity | receipt | my recomputation |
|---|---|---|
| exchange commuting / unitary Λ² / unitary Sym² / stochastic both | 64 / 64 / 64 / 64+64 | **same** |
| hard-core leak: leaking / closed / *set equality with the non-monomials* | 48 / 16 / — | **48 / 16 / set-equal** |
| sector dimensions | 256 = 136 + 120 | **same** |
| single-excitation nonzero pairs (all 3364) | 588 | **588** |
| the fold: separation profiles equal on all 16 columns, all 3364 pairs | 0 failures | **0 failures**; 20352 = 16 × 1272 |
| the parent's whole value multiset (8 values, 1272 cells) | reproduced | **identical, and identical to the parent's own re-parsed rows** |
| the two-excitation predicate, 198-pair declared sample, both sectors | 0 mismatches | **0 violations, 104 nonzero (52.5% vs the census's 52.4%)** |
| **the discrimination set equality**, 259-pair declared sample | `differing == single_nz` | **43 = 43, SET-EQUAL** |
| **the contact handle's moved set**, same 259 pairs, my own ζ₈ phase | `moved_set == single_nz` | **43 = 43, SET-EQUAL; the antisymmetric defect moves at 0 of 259, asserted per pair** |
| R4b: cells / tie cells / tie families / speeds | 1856 / 320 / 19 / {0,1,2} | **same** |
| velocity failures / cells / failing lift pairs | 7168 / 29696 / {(2,2),(−2,−2)} | **same** |
| eigenphase-additivity cells | 6960 / 7888 | **same** |
| spectra-split families | 58 / 58 | **same** |
| A4 distinguishable lift | 3306 / 3306 | **same** |
| third path on the 144-pair window | agrees | **agrees, 69,888 cells** |

**Zero false computed numbers.** The `STRUCTURAL` whitelist is inert
against measured content: only `14` and `22` (the version and the paper
number) rest on it, and `1/128` is licensed by a `defect_values` key.

---

## 10. Era compliance, per engraving, with birth-date rulings

The unit's worker was launched at **v14 #174** *"with the full 21
engravings at construction"* and delivered at **#195**. E-22 and E-23
were bought at **#187**, E-24 at **#192** — all three while it was in
flight.

| engraving | status | birth-date ruling |
|---|---|---|
| **E-22** inline-span coverage | **COMPLIANT, exceeds** — the scan is over raw bytes, so spans and fences are covered; three unlicensed-numeral injections into spans and fences die | not applicable: complied anyway |
| **E-22** blocks by multiset | **NOT MET** — containment only; injections 3, 14, 15 survive | **birth-date-fair for the mechanism** (the machinery first exists at #198, after delivery) — **except injection 15**, which reproduces #168's own demonstrated failure verbatim and is **charged** |
| **E-22** tables as claims | **NOT MET** — no table cell renders from a receipt path; injections 5, 6, 12, 13, 17 survive | **birth-date-fair**, charged as a repair; note the arena table is the paper's reachability exhibit and is wholly ungated |
| **E-23** falsifier descriptions verified against code | **NOT MET as a gate** — no gate compares a mutant's `why` to its code; audited by hand, 17/20 accurate, 1 inverted, 1 synthetic | **birth-date-fair** for the gate; the *substance* (a falsifier that never exercises its capability, `MUT-CACHE-DIRTY`) is charged under #34, pre-birth |
| **E-23** every load-bearing row has a falsifier or a forced waiver | **PARTIAL** — 55/63 gates have mutants, 3 have forced waivers, 3 more are forced-and-declared; `G-HEAD-LAW-EXERCISED` and `G-CLI-WHITELIST` have neither, and `cli_probes` is a sealed published row | **charged** (#34 is pre-birth) |
| **E-24** measure-relativity of counts | **SUBSTANCE MET, STAMP ABSENT** — see §11 | **birth-date-fair** (#192 > #174); charged as a one-line repair |
| **#20 + fences** (#168) | coverage met; the demonstrated failure recurs (injection 15) | **charged** |
| **#34** honest denominators, every falsifier reaches its gate | met — all 56 mutants reach and die at their gate; the 144-window and the 3-coin-pair axis are disclosed as declared windows | — |
| **#62** verbatim anchors, consumer must exist | **NOT MET, 30 rows** — MAJOR-1 | **charged**; the parent r4b already met it, and a sibling shipped the gate at #179 |
| **#82** CLI contract; comparator independence | met (15/16 argv, one MINOR); second and third paths derive rather than re-read | — |
| **#87** gates bind objects, not cardinalities | met and unusually well: the leak, the predicate, the discrimination set, the contact set and the arena two-way gate all bind objects; I confirmed the leak set *equals* the non-monomial set independently. MINOR-12: the per-object clause of `G-TWO-EXCITATION-PREDICATE` has no falsifier — `MUT-PREDICATE` clears `mism` and is killed by the count clause | — |
| **#91** no moving refs; off-tree, git-less byte reproduction | met — byte-identical ×2 across hash seeds off-tree with no `.git` | — |
| **#119 / #148** gate-to-disk seal, total manifest, seal testimony | mechanism met, manifest total, testimony sealed; **provenance false for 15 rows** (MAJOR-1) and **the gate-to-seal window open at 24, demonstrated by INJ-11 at exit 0** (MAJOR-4); one integrity-ordering MINOR-5 | **charged** — #119 (#119) and the totality addendum (#148) both precede #174, and #148's own words are "seals taken at the final gate are non-compliant" |
| **#125** text gates match text as written | normalisation is correct (whitespace + blockquote/list prefixes) and the 40-char floor is enforced — **with one waived anchor**; the *duplicate-shadow* variant (injection 8) is not covered | partly charged |
| **§15** declared arena as data; match every coordinate | met — all seven `arena_declaration` coordinates appear in the SCOPE segment, and the occupancy ceiling, the velocity convention, the lifts and the windows are all declared as free axes and censused | — |
| **#160** v10-layer tie-break | not applicable, and correctly so | — |
| single-threaded paper, no correction narrative | met | — |
| counts computed never typed | **MINOR-7**: `counts["alphabet"] = 25` and the SCOPE segment's `ALPHABET=%d` argument are typed literals, not `len(set(alpha))` — safe only because `G-ALPHABET-REBUILT` binds them to the measured rebuild | — |

---

## 11. E-24 — the delivered fractions, ruled per class

E-24: *"A unit publishing a fraction either declares the measure with it
or stamps it COUNTING-ONLY."* The string `COUNTING-ONLY` appears nowhere
in the paper, the code or the receipt, and no gate enforces one.

| class | figures | what they are | ruling |
|---|---|---|---|
| ordered pairs of a named finite generator pool | 1764/3364, 588/3364, 1176, 0 losses, 0 of 6728, 3306/3306, 588 contact, 2776 | counts over an exhaustively enumerated index set (58² and 58·57); no space of configurations is being integrated | **COUNTING-ONLY in substance; stamp absent** |
| generators | 64/64, 48/64, 16, 58/58, 16/16 | per-object tallies of gates that bind objects | **counting-only; a measure would be meaningless** |
| support-overlap rows | 42840/42840, 360/360, 43200, 1536 | counts over (site-pair × site-pair × coin-pair) = 120 × 120 × 3; exhaustive in the geometry, but the coin axis is **three declared ordered pairs `((0,3),(1,1),(7,11))` drawn from the 512 interfering coins** | **counting-only; the headline `42840 of 42840` does not carry the coin-axis sample stamp that the verdict segment does** (`COIN-PAIRS=3-EACH-GATED-SEPARATELY`). §7 of the paper does disclose the three pairs in prose, and each is gated separately, so this is a stamp gap, not a hidden sample |
| motion cells | **7168/29696**, 6960, 7888, 320/1856, 16 | the one genuinely measure-shaped figure: a fraction over momentum × momentum × direction × family with an implicit uniform counting measure | **counting-only, and the load-bearing content is measure-free** — the claim that actually carries is the *mechanism* (`failing lift pairs == {(2,2),(−2,−2)}`, gated as a set), which I reproduced independently. The bare fraction is the weakest form of the claim and is the one the paper leads with |
| defect values | 28, 30, 8 distinct; denominators to 1/128 | cardinalities of exact value sets | counting-only |

The unit does not violate E-24's *substance*: it publishes no
probability, calls nothing a density, and stamps `NO-CONFIGURATION-MEASURE;
NO-ACTION; NO-COUPLING` in the sealed SCOPE segment, with §10 repeating
it in prose. What is missing is the literal stamp and the gate.

**Repair (one line plus a gate):** append
`COUNTS=COUNTING-ONLY-NO-MEASURE-DECLARED` to the SCOPE segment and gate
its presence; and add the coin-axis sample stamp to the 42840 headline in
§7 and in the OVERLAP segment.

---

## 12. Findings, consolidated

### MAJOR

- **MAJOR-1 — thirty sealed rows name twelve gates that do not exist**
  (12/12 verbatim anchors, 3/24 path-value anchors, 15/30 seals). The
  pin's no-particle-naming wall, the connective clause and the R4b
  convention word are consequently gated by nothing; INJ-16 and INJ-1
  demonstrate it. Not birth-date-excused: #62 predates the launch, the
  unit's own byte-pinned parent r4b already complies, and the sibling
  gate `G-ANCHOR-CONSUMERS` shipped at #179. **Repair:** §2(a)–(d).
- **MAJOR-2 — the paper instrument admits twelve of seventeen
  injections**, including a second fenced block asserting the opposite
  head at the clean paper's scan count (INJ-15), the wall sentence
  inverted (INJ-16), the headline sentence inverted (INJ-18), every table
  perturbation, and a corrupted copy of a claim that occurs three times
  (INJ-8). Mechanisms: set-membership licensing over 218 members (39 from
  hex digests), containment claim matching against 11 duplicated claim
  strings, containment fence matching, tables not claims. Partly
  birth-date-fair; INJ-8, 15, 16, 18 are charged. **Repair:** §3d.
- **MAJOR-3 — `G-CACHE-UNPOLLUTED`, the gate bought by the unit's own
  self-caught cache defect, is under-bound**: its only falsifier is
  synthetic, its digest covers 7 of 11 fields of 1 of 7 caches, and the
  paper's §11 sentence about it is false as written. The disease itself
  is not live — I swept all six sibling caches by hand and by
  fingerprint. **Repair:** §1a(a)–(c).
- **MAJOR-4 — the seal window between a gate and its digest is open at
  24 of the 30 seals, and an injection walks through it at exit 0.**
  INJ-11 (one silently failed `restore()` inside `verify_paper`'s
  polarity test) delivers a sealed receipt asserting
  `exchange_census.antisymmetric_admitted = 65` on a 64-generator pool,
  beside `counts.pool = 64` and a verdict string still reading
  `64-OF-64`. All 60 gates pass, `SEAL.verify` reports nothing broken,
  and the seal's provenance column names a gate that does not exist. The
  unit's own second self-caught defect, repaired at six seals and left
  open at twenty-four. **Repair:** §1b(a)–(d).

### MINOR

1. *(promoted to MAJOR-4.)*
2. Five gates carry no *registered* falsifier. Four of them I falsified
   myself (`G-BYTE-ANCHORS`, `G-NO-FLOAT`, `G-MUTANT-SWITCH-CLEAN`,
   `G-HEAD-LAW-EXERCISED`), so they bind. `G-CLI-WHITELIST` alone has no
   demonstrated falsifier, and it is missing from the `FORCINGS`
   register though it is as unreachable by an in-process mutant as the
   three that are in it.
3. `MUT-SPEED-CEILING`'s published description is inverted.
4. `G-HARDCORE-ANTISYMMETRIC-CLOSED` publishes the typed constant `True`
   on all 64 rows; its forcing is machine-checkable in one line
   (`hardcore_leak(wedge(U))`) and is not checked.
5. `os.replace` promotes the artifacts *before* the disk-vs-seal
   comparison, so an integrity failure exits 2 with corrupt bytes on
   disk; and a failure between the two writes leaves them inconsistent.
6. `--verify-paper <nonexistent>` is not whitelisted: the full census
   runs and then dies with an uncaught traceback. Same shape for a bare
   copy and for a missing anchored source.
7. `counts["alphabet"] = 25` and the SCOPE segment's alphabet argument
   are typed literals rather than `len(set(alpha))`.
8. `VB-SEED-DEFECT` is a four-character needle (`"Born"`) with the gate's
   own floor waived for it; the published detail `"floor 50 chars"`
   conceals it.
9. `pool_key` omits `D` and `L` (unlike `full_pool_key`) — a latent
   cross-arena cache collision, unreachable today only because
   `G-ARENA-ANCHORED` precedes every census.
10. `defect_crossterm` skips its diagonal by object identity (`u is v`),
    not index. Measured: over 136,704 accumulator cells, **zero** carry
    a duplicate object identity, so the shortcut is correct here — but
    it is correct by allocation accident, and one index loop removes the
    fragility.
11. The third path's 144-pair window is declared and lively but no
    invariance across window choices is measured (§15).
12. `G-TWO-EXCITATION-PREDICATE`'s per-object clause (`not mism`) has no
    falsifier: `MUT-PREDICATE` sets `mism = []` and is killed by the
    count clause instead. (This one I established by reading the mutant
    body, not by injection — my source-variant probe for it did not
    build.)
13. A gate failure on the plain path is a traceback, not the mutant
    path's `died at …` line. Also: `provenance.runtime_inputs` lists 12
    of the 13 files actually read — the paper is missing, because
    provenance is built before `verify_paper` runs. And the dead line
    `got = hashlib.sha256(texts[sid].encode("utf-8","replace"))…`
    immediately overwritten in `build_arena` double-reads every source.

### Two false prose claims in the paper's §11

- *"Every object the unit vouches for … is digested at the moment its
  gate passes"* — false: the in-run seals are digested in a batch at the
  end of `build_state`, and fifteen of the thirty rows name a gate that
  never ran.
- *"the cache hands back defensive copies and a gate re-checks the cached
  census's digest on every build, so no injection … can reach the next
  run through it"* — one of seven caches copies; the gate re-checks part
  of one of them.

---

## 12a. The head's own chain, which is the strongest part of the unit

Worth stating plainly, because it is what keeps the grade at AWF. The
head is not typed anywhere it could drift:

1. The four pre-registered names are **parsed out of the pin's committed
   bytes** (`preregistered_heads`), not typed in the instrument —
   `MUT-HEAD-PRENAME` falsifies that.
2. The head is **derived** from two measured predicates by `head_law`,
   and the same law is exercised on four constructed arenas plus a
   blocked probe, returning five distinct pre-registered names.
3. It is **reconstructed** by a second copy of the law that reads only
   the serialized receipt and locates its arena by role string, and the
   whole verdict string is compared for equality —
   `MUT-HEAD-TYPED` (retype the head after the census) dies there.
4. The paper quotes the **complete 2353-character** string, gated.

The two copies of the head law do share the four head literals, which is
the letter of #82's "no shared typed literals" — but the literals are
independently anchored to the pin by (1), so a single-point error in
either copy is caught. I regard this as compliant.

## 13. What survives, unqualified

The head `R4C-STATISTICS-BOTH-ADMITTED` and every segment I could reach
independently. The exchange census (64/64 commuting, unitary and
stochastic in both sectors), the hard-core split (48 leaking / 16 closed,
and the leaking set *is* the non-monomial set), the sector decomposition
256 = 136 + 120, the parent reproduction (588 of 3364 and the whole
eight-value, 1272-cell multiset, matching the parent's own rows), the
fold (0 failures over 3364 pairs × 16 columns), the two-excitation
predicate on a 198-pair sample (0 violations), R4b's 1856/320/19/{0,1,2},
the velocity failure at 7168 of 29696 confined to {(2,2),(−2,−2)}, the
spectra split at 58/58, the distinguishable arena at 3306/3306, and the
third route's agreement on the declared window — every one of them
recomputed by my own bookkeeping (§9's scope note applies).

**And the unit's central finding survives the hardest independent test I
could put to it.** On a 259-pair declared sample, with my own census loop
and my own inline ζ₈ contact phase, the set on which the two shapes'
two-excitation defects differ, the set whose symmetric defect the contact
handle moves, and the single-excitation defect set are **one and the same
43-element set**, and the handle moves the antisymmetric defect at
**none** of the 259 pairs. Three probes, one set, exactly as the paper
says.

Forty-eight anchors each kill the run at their own gate; the bare copy
writes nothing; the selftest writes nothing; a real on-disk drift of an
anchored parent kills the run; the argv whitelist rejects fifteen of
sixteen hostile forms at exit 2; the registry, the receipt and the totals
agree row for row.

The instrument's *measurements* are sound. What the repairs above buy is
the instrument's *testimony about itself*: the anchors' consumers, the
seals' provenance and timing, the paper's tables and fences, and the
cache gate's own reach.

---

## 14. What I did NOT complete, disclosed

This machine carried a load average between 170 and 230 for the whole
review, from the concurrent K1/K2 seats running the same instrument. A
single cold run of this unit costs about twenty CPU-minutes. Four items
ran long; **three of the four landed before I closed and are reported in
full** — the byte reproduction ×2 across hash seeds (§8, confirmed three
ways against the committed bytes), the post-write corruption injection
(§5, `rc=2`, which demonstrated MINOR-5 into the bargain), and the whole
cache-probe battery (§1a, which turned MAJOR-3 from a reading into a
measurement). One item remains, and it is a protocol shortfall rather
than a finding:

**10 of the fifty-six out-of-process `--mutant` runs** did not finish
(§4): 46 completed, **46/46 on target**, artifacts byte-unchanged after
every one, zero stray files. All 10 are covered in-process four times
over — the committed receipt's sweep, my own `--no-write` delivery run,
and both mirror runs — plus a fifth, order-independent pass: a
reversed-registry in-process sweep put **56/56 on target**.

Everything else launched during this review finished and is reported
above, including the items that landed after I first closed: the byte
reproduction ×2 (§8), the post-write corruption injection (§5), the cache
fingerprint sweep and the five real in-place pollution probes (§1a), the
reversed-order sweep, the head-law tamper (§4b) and the `u is v` identity
census (§6).

The four MAJOR findings are each **demonstrated, not inferred**: MAJOR-1
by reading the sealed receipt against the run's own gate ledger and by
INJ-16/INJ-1; MAJOR-2 by seventeen paper injections through the
instrument's own `verify_paper`; MAJOR-3 by five real in-place cache
pollutions, two of which deliver at exit 0 while `G-CACHE-UNPOLLUTED`
fires on none of the five; MAJOR-4 by INJ-11, which delivered
`65 of 64 generators` sealed at exit 0.
