# SEC-2 (paper-40) — INSTRUMENT REVIEW (K3)

**Seat:** INSTRUMENT (K3) — the era audit: seal, coverage, injections, CLI,
#91 at its own hands, the seam ruling.
**Object:** `v14/paper-40-sec2.md` `aeeeb6757715` · `v14/code/sec2_exact.py`
`4cb4011cfa05` · `v14/code/sec2_output.txt` `57c98674b479` ·
`v14/code/sec2_receipt.json` `b66fdfaacc33` · pin `v14/note-sec2-pin.md`
`bfe5c66be9ec`. **All five verified at open and re-verified at close.**
**Authority:** HANDOFF-PROMPT §4/§9; RUNBOOK E-22/E-23/E-24; ledger #267,
#119-as-amended-at-#348, #301, #322, #332, #350.

> Between delivery and adjudication every reading here is a **candidate**.
> This review is candidate until the joint adjudication rules on it.

---

## GRADE: ACCEPT-WITH-FIXES

**No measured quantity is wrong.** Every headline number of all four
segments reproduces under an independent construction that shares no code
path with the builder, including a full **455-group census run with no orbit
reduction at all**. Byte reproduction is exact at **two hash seeds**,
off-tree, git-less, from artifact-deleted trees. The 38-mutant sweep is 38/38
on target out of harness, one process each, artifacts byte-identical. The
ledger chain recomputes from bytes. All 25 sealed digests match their
published values and totality holds on the delivered receipt.

**The perimeter is the problem.** Forty-four live injections and probes:
**13 correctly refused, 2 legitimate changes correctly accepted, and 29
corruptions accepted at exit 0** — including two header swaps
between published tables, two rows transplanted from one table into another,
a fabricated ninth verdict fence, the deletion of the entire §9 verdict
block, five prose direction flips (`IRREDUCIBLE`→`SELECTED`,
`216 of 288`→`288 of 288`, `MOTIVATED at 0`→`MOTIVATED at all`, `not among
them`→`the unique one among them`, `forbids`→`selects`), three
cross-universe referent swaps, an unbacked six-digit numeral, a capitalised
polarity negation, a stray read of the very file the pin forbids, and — both
forms — **THE ACT DISEASE**.

Thirteen majors, eleven minors. **Ten of the thirteen majors are
TEMPLATE-SHAPED**, not SEC-2-shaped, and belong to the #267 corpus sweep;
three are this unit's own.

---

## 1. WHAT IS VERIFIED CLEAN

| leg | result |
|---|---|
| five object hashes, open and close | 5/5 |
| 5 sources at their pinned sha256-12 | 5/5, recomputed from the tree |
| 4 declared #301 SEC objects vs the real commit `88e4a83` | 4/4 by `git show`; commit confirmed as the #301 SEC delivery |
| `--verify-sec` on the git-shown objects / on a tampered digest / on an absent dir | 0 mismatched exit 0 / 1 mismatched exit 1 / 4 mismatched exit 1 |
| 8 verbatim anchors, located and read in context | 8/8, hits == 1 each, all clear the 40-char floor; all 8 are genuine quotes, checked against their sources by hand |
| 38-mutant sweep **out of harness**, one process each | 38/38 ON TARGET, zero survivors |
| artifacts + paper + code after the sweep | **byte-identical, 4/4 files** |
| byte reproduction ×2, off-tree, git-less, artifacts deleted, `PYTHONHASHSEED=1` and `987654` | `57c98674b479` / `b66fdfaacc33` at **both seeds** — **IDENTICAL**, `cmp` clean, zero `.git*` in either tree |
| ledger chain recomputed from the receipt's own bytes | 42/42 row digests, 42/42 chain links, head `a72a3ae7f7c3e91d` **MATCH** |
| 25 sealed digests vs the values they seal, on the delivered receipt | **25/25 MATCH** |
| totality on the delivered receipt | 33 keys ⊆ 34 covered, uncovered = none |
| hostile argv, 22 forms | every unknown flag / unknown argument / missing argument / second mode flag exits 2 |
| write-nothing by **full tree hash** (`--numbers`, `--no-write`, `--selftest`, `--break-anchor`, `--verify-paper`, `--list-*`, `--verify-sec`, `--mutant`) | UNCHANGED at every mode |
| `--selftest` | 8/8 anchors die at G-ANCHORS, artifacts unchanged |
| read-back before `os.replace` | present in code, verified |
| the verdict comparator, run **by me** on the delivered receipt (the thing MUT-VERDICT never exercises) | `reconstruct(R)` == `R["verdict"]` **4/4 segments**; the paper's 8 fences are exactly the 4 segments twice each; all four appear verbatim in the transcript. The three artifacts agree on the head. |
| E-24 | COUNTING-ONLY stamped in `standards.measure`; every published ratio carries its denominator |

### 1.1 The measured layer, recomputed independently

I rebuilt the k=3 aligned union from `AG(2,3)` and ran the fate of **all 455
three-actor groups with no orbit reduction**, plus the inventory of every
lawful one:

```
total_groups 455 | seam_spanning 288 | alive_at_delivered 54 (401 STRUCT-DEAD)
lawful_at_matched 216 | dead_at_matched 72 | dead_that_open_a_within_pair 72/72
MOTIVATED lawful groups found: 0 of 216
```

Every one of these is the delivered number, obtained without the orbit
reduction the paper uses. Separately, from the paper's own tables:
49 seam rows summing to **132,273** shared sites; 16 census rows summing to
**45,010** = Σ C(9,k)·9!/(9−k)!; 455 = C(15,3); 630 = C(36,2); 7,140 =
C(36,3); min posdef **31**; exactly **13** rows where admissible == posdef;
exactly **1** parity-stable row; 162 table rows. **Zero disagreements.**

### 1.2 Every claimed count, re-derived from the live registries

| claimed | measured here | verdict |
|---|---|---|
| 42 gates | receipt ledger **42**, chain over 42 — but the transcript shows **45**, `--list-gates` **34**, `coverage.gates` **34** | count correct, **four different numbers published** → MAJOR-9 |
| 38 mutants, 38/38 in-run | `mutant_sweep` 38 rows, 38 `on_target`; my out-of-harness sweep 38/38, one process each | **CONFIRMED** |
| 5 sources at pinned shas, read set gated at the I/O layer | 5/5 shas correct; the gate is a helper-level check fired once | count correct, **claim false** → MAJOR-2 |
| 8 verbatim anchors bound to named consumers | 8/8 located once, in context, over the floor; consumer names are real gates | count correct, **binding unmachine-checked** → MINOR-3/4 |
| 25 sealed + 9 declared-unsealed | 25 + 9; all 25 digests match their values; totality 33 ⊆ 34 | **CONFIRMED** |
| 162 claims ⟷ 162 rows, multiset **both ways** | 162 claims, 162 paper rows | count correct, **"both ways" false** → MAJOR-3 |
| 1,018 numerals | my independent scan of the same regex: **1,018**; permissive digit-runs present: **1,180** | count correct, **162 unscanned** → MAJOR-5 |
| 8 fences | 8 blocks, 4 distinct verdict segments × 2 | count correct, **multiset false** → MAJOR-4 |
| 5 polarity rows | 5, each with its own negation | count correct, **case-sensitive** → MAJOR-10 |
| 1 spelled numeral | `twenty-two`, appearing 3×, backed by the 22 declared SEC values | **CONFIRMED** |
| ledger chain `a72a3ae7f7c3e91d` | recomputed from receipt bytes: 42/42 digests, 42/42 links | **CONFIRMED** |
| `--verify-sec` 4/4 vs git-shown #301 objects | 4/4 at commit `88e4a83`, exit 1 on tamper and on absence | **CONFIRMED** |
| "three mis-targeted falsifiers repaired in-construction (disclosed)" | six sentinel-shaped falsifiers remain; the disclosure names none and lives only in the ledger | **NOT DISCHARGED** → MAJOR-7, MINOR-2 |

---

## 2. MAJORS

### MAJOR-1 — THE ACT DISEASE, BOTH FORMS. Promotion-time totality is not recomputed; the "integrity check against the gate-time seal" is a write-time re-derivation. [TEMPLATE]

`write_artifacts` computes `seal_out`/`seal_rec` **from the payload at write
time** and compares the disk read-back against those. The per-key digests in
`SEAL.seals` — the gate-time seals — are **never** compared against what is
promoted. `G-SEAL-COMPLETE` fires inside `finish()`; nothing re-checks
totality at promotion.

**Injection (through the instrument's own functions, disposable tree):**
after `finish()` returned, I mutated a value inside a *sealed* key and added
an undeclared top-level key, then called `write_artifacts`:

```
write_artifacts RETURNED NORMALLY -- no integrity objection
  promoted receipt: lawful=288 word=GLUING-EVENT-LAWFUL-AT-EVERY-EXTENSION
  forged key on disk: True | top keys now 34
  manifest still says sealed=25 unsealed=9
  recomputed digest of the promoted lawfulness : 03f7a8e1a1eefb8f
  digest published in the manifest             : 9e1c5f7d271afaf4
  SEAL vs PROMOTED VALUE: *** MISMATCH, PROMOTED ANYWAY ***
  rendered transcript now says: 'lawful at the matched extension: 288 of 288'
```

The receipt lands on disk **self-contradicting** — its own manifest publishes
a digest that does not match the value beside it — and the instrument raises
nothing. This is precisely what the #119 addendum engraved at #348 (the SPC
ACT ruling) requires be closed.

**Honest scope:** the *delivered* artifacts are clean. I verified all 25
sealed digests against their published values (25/25 match) and totality
(33 ⊆ 34, uncovered none). The disease here is a **latent mechanism gap, not
a live corruption**. Note also that the #348 addendum and this delivery
(#350) are the same day, and the pin froze at #332 — the amendment postdates
construction. It is still owed.

**Repair.** In `write_artifacts`, before staging: recompute
`digest(R[k])` for every `k` in `SEAL.seals` and compare; recompute
`set(R) - {"seal_manifest"} <= set(SEAL.seals) | set(SEAL.unsealed)`; raise
`G-INTEGRITY` on either failure. Emit both as real ledger rows.

### MAJOR-2 — The read set is NOT gated at the I/O layer, and the gate fires once. The pin's own prohibited file walks straight in. [SEC-2-SHAPED]

`READLOG` is appended inside the helper `read_bytes`; there is no
`builtins.open` hook and no `sys.addaudithook`. `G-SOURCES` compares
`sorted(READLOG)` against the declared set **at one instant**, before the
anchor loop; nothing re-checks it afterwards, and three later
`READLOG.pop()` calls quietly remove reads from the log.

The pin says of the #301 objects: *"the worktree copies are UNDER REPAIR, do
not read them"*. I planted a read of exactly that file,
`v14/code/sec_exact.py` (still `M` in the worktree), three ways:

| injection | result |
|---|---|
| `read_bytes("v14/code/sec_exact.py")` **before** `G-SOURCES` | **rc=1, dies at G-SOURCES** ✓ |
| the same call **after** `G-SOURCES` | **rc=0, SURVIVES** ✗ |
| a raw `open(...).read()` of it, anywhere | **rc=0, SURVIVES** ✗ |

The gate's own statement — *"the read set recorded at the actual I/O layer is
exactly the declared set, so a stray read fails the gate"* — and paper §2.1 —
*"the read set recorded at the I/O layer is gated to be exactly this set"* —
are both false as written. Two of three routes to the forbidden file are open.

**Repair.** Install an `open`/audit hook that records **every** read; re-run
the read-set comparison at the last gate, not the first; replace the three
`READLOG.pop()` calls with a declared-exemption list checked at that gate.

### MAJOR-3 — The claims gate is TABLE-BLIND and one-way: a header swap between two published tables passes, and so does a row transplanted from one table into another. [TEMPLATE]

`paper_claims` builds `(cid, cells)` and then throws `cid` away:
`want = Counter(t for _i, t in C)`. Table identity, row order and table
membership are all discarded, and `stray` tests `k not in want` (membership),
never `got[k] > want[k]`.

| injection | result |
|---|---|
| swap the **header row of the price table with the header row of the blindness table** | **rc=0 PASS** ✗ |
| swap the **header row of the seam table with the header row of the census table** | **rc=0 PASS** ✗ |
| insert the census row `\| (3, (0, 0, 3)) \| 54 \| 15 \| 54 \| 0 \|` into the **blindness** table | **rc=0 PASS** ✗ |
| insert the grid row `\| NONE \| 0 \| 1 \| LAX \| POSITIVE \| ALIVE \| ALIVE \|` into the **seam** table | **rc=0 PASS** ✗ |
| duplicate a legitimate price row | **rc=0 PASS** ✗ |
| a *genuinely new* blindness row `\| 4 \| 8000 \| 20 \| not run \| SIGHTED \|` | rc=1, G-PAPER-CLAIMS ✓ |
| swap two currency verdicts (IGNORES↔FAVOURS) | rc=1, G-PAPER-CLAIMS ✓ |
| forge one seam cell 31→32 | rc=1, G-PAPER-CLAIMS ✓ |

Two header pairs and two row transplants, four independent table pairs, all
at exit 0.

So the gate catches *invented content* and misses *misplaced content*. Paper
§11's *"compared as a multiset in both directions"* is true only in the
`missing` direction. A paper can present a fabricated fourth blindness row
and a swapped price header and pass its own instrument.

**Repair.** Key the claim multiset by table: compare per-table row multisets
(`cid` prefix ↔ the table the row was parsed from), and make `stray` test
`got[k] > want[k]`.

### MAJOR-4 — E-22 is not met: the fence gate is two-sided **containment**, not multiset equality. A ninth fence passes, and deleting §9's four fences passes. [TEMPLATE, E-22 NAMED]

`paper_fences`: `missing = [k for k in want if got[k] < want[k]]`,
`stray = [k for k in got if k not in want]`. With `want` a Counter over 4
distinct verdict strings and `got` a Counter over 8 blocks, any count ≥ 1
satisfies it.

| injection | result |
|---|---|
| append a **9th fence** that duplicates a legitimate verdict segment | **rc=0 PASS** ✗ |
| **delete the whole §9 Verdict block** (4 of the 8 fences) | **rc=0 PASS** ✗ |
| a forged fence with different content, all numerals backed | rc=1, G-PAPER-FENCE ✓ |
| a direction flip inside both copies of a fence | rc=1, G-PAPER-FENCE ✓ |

E-22 says in terms: *"Fenced blocks are gated by MULTISET EQUALITY, not
containment."* This gate is containment in both directions. The paper could
ship with its Verdict section emptied and still pass.

**Repair.** `got == want` after normalising, with the expected multiplicity
declared (here 2 per segment: the head and §9).

### MAJOR-5 — The numeral scanner is blind to any numeral that ends a sentence. A six-digit unbacked number passes. [TEMPLATE]

`NUM_RE = (?<![\w./-])\d[\d,]*(?:/\d+)?(?![\w.])`. The trailing `(?![\w.])`
rejects a numeral followed by `.` — i.e. **every sentence-final numeral in
the paper**.

The decisive pair, same numeral, one character apart:

| injection | result |
|---|---|
| `so the kernel is 4. The forged total is 778899.` | **rc=0 PASS** ✗ |
| `so the kernel is 4. The forged total is 778899 exactly.` | rc=1, **G-PAPER-COVERAGE** ✓ |
| `so the kernel is 4. The stray count is 91237.` | **rc=0 PASS** ✗ |

Blind spots mapped exactly: a numeral followed by `.`, or preceded by `-`,
`/` or `.`, is never scanned. The prefix exclusions are deliberate (they buy
digest immunity, which I confirmed is structural rather than a whitelist —
good). **The suffix exclusion is an accident and it is the load-bearing
one.** 162 digit-runs in the paper are entirely unscanned; the claimed
1,018 is what the regex sees, of 1,180 present.

**Repair.** `(?![\w])(?!\.\d)` — allow a following period unless it begins a
decimal.

### MAJOR-6 — Four of the 42 published gates carry NO falsifier at all: no mutant, no waiver. G-COVERAGE exempts itself by a snapshot. [TEMPLATE, E-23 NAMED]

`gates = LD.names()` is taken **before** `G-COVERAGE` is appended, so
`G-COVERAGE` is not in its own uncovered check. `LATER_GATES` then exempts
the rest without a stated forcing.

Ledger gates (42) minus mutant targets (38) minus WAIVERS:

| gate | mutant? | waiver? | how it escapes |
|---|---|---|---|
| G-COVERAGE | none | none | snapshotted before it fires |
| G-PAPER-FENCE | none | none | `LATER_GATES` |
| G-PAPER-POLARITY | none | none | `LATER_GATES` |
| G-PAPER-SPELLED | none | none | `LATER_GATES` |

E-23: *"a row with neither is unguarded no matter how many times it ran."*
These are exactly the three gates that guard the verdict blocks, the
direction words and the spelled numerals — the highest-stakes paper gates —
plus the gate that certifies coverage itself. And MAJOR-4/5/10 below are
live demonstrations that three of the four are in fact weak.

**Repair.** Add MUT-FENCE, MUT-POLARITY, MUT-SPELLED; move `G-COVERAGE` after
its own snapshot or give it a machine-checked forcing; make `LATER_GATES`
exempt from *ordering* only, never from falsification.

### MAJOR-7 — Six falsifiers are sentinel-shaped: their published description names a corruption their code never performs. [TEMPLATE, E-23 NAMED]

E-23 requires the description be verified against the code. The instrument
checks only that `mut("NAME")` or `pick("NAME"` **occurs** in the source
(38/38 do). I ran the third leg — description vs code — by hand on all 38.
Thirty-two are honest. Six are not:

| mutant | published description | what the code does |
|---|---|---|
| MUT-VERDICT | "one verdict segment is **edited after the builder**, so the independent comparator disagrees" | `same[0] = False` — forces the comparison result; `reconstruct()` is never exercised |
| MUT-PAPER-CLAIM | "one rendered table row is **corrupted**" | replaces the whole `cl` dict with a hand-written failing dict; `check_claims` is never exercised |
| MUT-QUOT-POS | "one QUOTIENT+POSITIVE **fate is forged**" | `same = False` — forces the agreement flag |
| MUT-EXACT-FLOAT | "the AST scan is **handed a float constant**" | `floats = floats + ["injected"]` — appends a *string* |
| MUT-PRICE-FLAT | "the two-sided cross budget **drops one sign**" | `flat = flat + ["injected"]` |
| MUT-FISCHER | "the determinant comparison is **inverted**" | `fisch = fisch + ["injected"]` |

All six report ON TARGET in my out-of-harness sweep — they prove the gate
raises when handed a `False`, not that it detects the corruption it advertises.
MUT-VERDICT and MUT-PAPER-CLAIM are the serious two: the verdict comparator's
independence and the paper-rendering machinery are the corpus's two most
load-bearing instruments and **neither has a falsifier that touches it**.

The ledger records "three mis-targeted falsifiers repaired in-construction
and disclosed". Six of the class remain; the disclosure names none of them,
and — see MINOR-2 — the descriptions are not published anywhere the seal
reaches.

**Repair.** Rewrite all six to corrupt the measurement: edit `V[0]` after
`build_verdict`; corrupt one `R["completion_lattice"]` row before
`check_claims`; forge a real fate; inject `ast.Constant(value=0.5)`; drop a
sign in the two-sided budget; invert the `dets` comparison.

### MAJOR-8 — Two declared modes pass vacuously with no paper: `--verify-paper` on an empty file prints PASS, and `--no-write` with the paper deleted passes every wall. [SEC-2-SHAPED]

`G-PAPER-PRESENT` is guarded by `PAPER_REQUIRED[0]`, which is set `True`
**only inside `run_mutant`**. It is `False` in `--verify-paper`, `--no-write`
and `--numbers`.

```
$ sec2_exact.py --verify-paper /…/empty.md
VERIFY-PAPER PASS: /…/empty.md          rc=0
```

Every paper gate was skipped. And with the paper deleted:

```
$ sec2_exact.py --no-write        # paper-40-sec2.md removed
    G-PAPER-PRESENT     PASS
    G-SWEEP-EXECUTED    PASS
    G-SEAL-COMPLETE     PASS
    G-DECLARED-LATER    PASS          rc=0
```

G-PAPER-CLAIMS/COVERAGE/FENCE/POLARITY/SPELLED are silently absent, and all
three walls (G-WALL-EXTENSION, G-WALL-SEAMCONFINED, G-WALL-SCAN) pass
vacuously on `""`. `G-DECLARED-LATER` drops the paper gates from `want_late`
when `ptext` is empty, so it too passes. The docstring says `--no-write` will
"run every gate". The delivery run is protected **only** because `run_mutant`
leaves `PAPER_REQUIRED[0] = True` set as a side effect and never resets it.

**Repair.** Set `PAPER_REQUIRED[0] = True` in `--verify-paper`, `--no-write`
and the delivery path; make the three walls fail, not pass, on empty text.

### MAJOR-9 — The transcript is bound to nothing. A forged PASS line, a forged measured number and a wholly invented gate row all survive. And the published ledger is 42 rows while 45 gates fire. [TEMPLATE, #267 NAMED]

The string `sec2_output` occurs **0 times** in `sec2_receipt.json`. No digest
of the transcript is published, and no mode verifies one.

**Injection.** In a disposable tree I edited `sec2_output.txt`:
`G-SEAL-COMPLETE PASS` → `FAIL`; `lawful at the matched extension: 216 of
288` → `288 of 288`; and inserted a fabricated row
`G-TOTALLY-INVENTED-GATE PASS 0000000000000000`. Then:

```
--no-write       rc=0
--verify-paper   rc=0
```

Worse, the transcript and the receipt disagree about the instrument itself.
`R["ledger"]` is snapshotted **before** the last three gates fire:

| source | gate count |
|---|---|
| `--list-gates` | **34** |
| `receipt.coverage.gates` | **34** |
| `receipt.ledger` / `receipt.totals.gates` | **42** |
| `sec2_output.txt` | **45** |

`G-SWEEP-EXECUTED`, `G-SEAL-COMPLETE` and `G-DECLARED-LATER` appear in the
transcript and in **no published ledger row and no chain**. The chain
`a72a3ae7f7c3e91d` — which I recomputed exactly, 42/42 — covers everything
*except* the three gates that certify the seal. `G-INTEGRITY` is never a
ledger row at all; it exists only as an exception string.

**Repair.** Move the `R["ledger"]`/`ledger_chain`/`totals` assignment after
the last gate; seal a `transcript` key carrying the output's digest and line
count; add `--verify-transcript`; make `--list-gates` run `finish()`.

### MAJOR-10 — The polarity gate is case-sensitive: a negation at the start of a sentence is invisible. [TEMPLATE]

`canon()` folds whitespace, ASCII and markdown but **does not lowercase**;
`locate()` is a case-sensitive substring count. Every POLARITY needle is
lowercase, so a negation capitalised as a sentence opener never matches.

| injection | result |
|---|---|
| `One might say the freedom is reducible after all.` | rc=1, **G-PAPER-POLARITY** ✓ |
| `The freedom is reducible after all.` | **rc=0 PASS** ✗ |
| `The freedom is reducible, on the stronger reading.` | **rc=0 PASS** ✗ |

The gate that exists to catch the paper asserting its own inverse is defeated
by a capital letter. **Repair:** casefold both sides in `locate`.

### MAJOR-11 — Five prose direction flips pass. The verdict words are gated only where they sit inside a fence. [TEMPLATE, targets the #267 "paper-scanning walls" family]

| injection | site | result |
|---|---|---|
| `` `SEAM-DECLARATION-IRREDUCIBLE` `` → `` `SEAM-DECLARATION-SELECTED` `` | §3.4, inline span | **PASS** ✗ |
| "seam-spanning groups, **216** leave the dictionary alive" → **288** | §4.5 | **PASS** ✗ |
| "And **not one** of the 216 is MOTIVATED." → "And **every one** of the 216 is MOTIVATED." | §4.5 | **PASS** ✗ |
| "the direct sum is **not** among them" → "the direct sum is **the unique** one among them" | §3.5 | **PASS** ✗ |
| "the measured crossing **forbids**" → "the measured crossing **selects**" | §3.5 | **PASS** ✗ |

All five invert a delivered finding in the paper's own voice. None is a table
row, none is inside a fence, none is a POLARITY needle, and all their numerals
are backed — so nothing looks at them. Note the third flip inverts
`MOTIVATED at 0`, which is one of the two clauses the pin's outcome vocabulary
turns on.

**Repair.** Extend POLARITY to cover every headline direction word, including
the outcome tokens `IRREDUCIBLE`/`SELECTED`, `216 of 288`, `MOTIVATED at 0`,
`EXCLUDES the direct sum`, and gate the inline verdict spans against the
receipt's `lawfulness.word` / `seam_selection` rows.

### MAJOR-12 — No referent binding: numerals are backed by one global registry, so a count from one universe validates a claim about another. [TEMPLATE, #267 shape]

`paper_coverage` flattens every integer in the receipt into one set. A numeral
is "backed" if it appears **anywhere**, about anything.

| injection | result |
|---|---|
| "so the kernel is **455**" (a group count used as a matrix kernel) | **PASS** ✗ |
| "**455** seam types over 132,273 shared sites" | **PASS** ✗ |
| "evaluated on every one of the **132,273** composites" (should be 45,010) | **PASS** ✗ |

The unit runs six live universes — 49 seam types, 132,273 shared sites, 455
groups, 288 seam-spanning, 216 lawful, 45,010 gluings — and any of their
numerals will validate any other's sentence.

**Repair.** Bind key numerals to referent-tagged needles (the #267 checklist
already requires this of AID; SEC-2 has none).

### MAJOR-13 — `union_min = 1` is a typed constant published as a measurement, and it is the whole of criterion 3. [TEMPLATE — the #267 "typed totals-counts" family]

```python
union_min = 1
ceiling = (union_min).bit_length() - 1
```

It is never computed from the family. It is published in the ledger evidence
as `"union_min_count": union_min`, asserted in paper §3.3 (*"The union's
minimum count is 1 at every gluing in the family"*) and carried in the head
(`MIN COUNT 1, CEILING 0`) — where **both** the builder and the comparator
type it, so `G-VERDICT-RECON` cannot see it either. MUT-REFINEMENT perturbs
`ceiling` directly, so no falsifier reaches the constant by measurement.

The claim is *true* (I checked: `d ≤ 3` of 54 pairs are doubled at every
gluing, so a count of 1 always exists) — but "refinement stability is EMPTY at
this record", one of the three legs of M1's verdict, currently rests on a
typed literal. **Repair:** compute `union_min = min(rel.values())` over the
family, gate it, and let MUT-REFINEMENT move the measurement.

---

## 3. MINORS

1. **The seal partition is unconstrained.** I popped `lawfulness` out of
   `SEAL.seals` and re-declared it unsealed with the free-text reason
   `"forged reason: measured elsewhere"`; the run passed at exit 0 with the
   manifest still reading TOTAL (24/10). Totality constrains the union, never
   the split — any measured key can be moved to the unsealed side at will.
2. **Mutant descriptions are outside the sealed surface.** `R["coverage"]`
   publishes names only; `mutant_sweep` rows carry `{mutant, declared,
   died_at, on_target}`. No description string appears in the receipt, the
   transcript or the paper. E-23 calls the published description part of the
   sealed surface; here it exists only in the source and in `--list-mutants`.
3. **Phantom consumers are unchecked.** I renamed one anchor's consumer to
   `G-NO-SUCH-GATE-AT-ALL`: rc=0, PASS. Nothing verifies the named gate
   exists. (I checked by hand: all 8 delivered consumer names *are* real
   gates — the field is honest, just unguarded.)
4. **Seven of the eight anchors are located and then discarded.**
   `texts[sid]` is consumed by exactly one gate besides `G-ANCHORS`
   (`G-LEGS`), and even there through a *separate* typed literal rather than
   the anchor itself. "bound to the gate that consumes it" (§11) is a
   declaration, not a mechanism.
5. **Two waiver forcings overstate the code.** `G-SWEEP-EXECUTED`'s waiver
   says the forcing is "a sweep whose **row count equals the declared mutant
   count**" — the gate checks only the boolean `swept`, never a row count;
   and in `--no-write` the harness passes `swept = swept or not write`, i.e.
   `True` with no sweep at all. `G-SEAL-COMPLETE`'s waiver says "checked by
   **set equality**"; the code checks `keys <= covered` (subset).
6. **`G-INTEGRITY` is declared in `LATER_GATES` and `WAIVERS` but is never a
   gate.** It is only a `GateFail` string raised inside `write_artifacts`;
   `G-DECLARED-LATER` does not require it in `want_late`.
7. **Artifact promotion is not atomic across the two files.**
   `write_artifacts` fully replaces `sec2_output.txt` before it stages
   `sec2_receipt.json`; a read-back failure on the second leaves a promoted
   transcript beside a stale receipt. Staging cleanup (`os.unlink(tmp)`) is
   correct on the read-back path only.
8. **The spelled-numeral whitelist is a self-list of 26 words.** Nineteen
   ordinary above-twelve forms are unscannable; I planted `sixty-three` and
   it passed (`two hundred and sixteen` died only because `two hundred` is
   listed and 200 is unbacked). This is LOR M6's disease.
9. **The choice inventory (§8) and the arena row (§2) are typed
   self-lists.** `R["choices"]`'s fibers (`"45010"`, `"31 at the all-simple
   seam"`, `"1 or 3"`, `"1, 3 or 9"`) and `standards.arena`'s counts are
   hand-typed strings; the claims gate then verifies the paper copies them.
   21 of the 162 claim rows are literal-vs-literal. The RSQ standard reads §8,
   so its fibers should be derived from `R["inventories"]` and the window.
10. **Typed counts inside sealed gate statements.** `G-LAWFUL` states "at 216
    of the 288 seam-spanning groups", `G-PRICE-LAWS` "45,010", `G-REFINEMENT`
    "48 of the 49", `G-INVENTORY` "three … two". They are published in the
    ledger and go stale silently.
11. **The orbit-invariance control is weaker than the aggregate it licenses.**
    Only `orb[0]` vs `orb[1]` is compared, and only on
    `(|foreign|, |within|, |doubled|)` — never on the *fate*, which is what
    the orbit size multiplies into 216 and 288. (I closed this by running all
    455 groups directly; the aggregates are right. The control should still
    check the fate.)

---

## 4. THE NINE PROBES — PRESENT / ABSENT

| # | probe | verdict | evidence |
|---|---|---|---|
| 1 | header swaps + fabricated rows (price / blindness tables) | **PRESENT** | header swaps price↔blindness **and** seam↔census both rc=0; census row transplanted into the blindness table and grid row into the seam table both rc=0; duplicated price row rc=0. A *genuinely new* row and a swapped verdict cell both die → MAJOR-3 |
| 2 | direction flips | **PRESENT (5 of 6)** | `IRREDUCIBLE`→`SELECTED`, `216 of 288`→`288 of 288`, `MOTIVATED at 0`→`at all`, `not among them`→`the unique one`, `forbids`→`selects` all rc=0. **ABSENT** for the five currency verdicts — swapping those dies at G-PAPER-CLAIMS → MAJOR-11 |
| 3 | THE ACT DISEASE, both forms | **PRESENT, both** | post-seal *mutation* of a sealed key and post-seal *added* key both promoted, manifest unchanged, seal-vs-value MISMATCH ignored; a measured key de-sealed and re-declared unsealed passes totality. Delivered artifacts verified clean → MAJOR-1, MINOR-1 |
| 4 | the read-set gate — real? plus `--verify-sec` | **PRESENT (the gate); ABSENT (verify-sec)** | the prohibited `sec_exact.py` read dies only if planted *before* the gate; the same read after it, and any raw `open()`, survive. `--verify-sec` is sound: 4/4 on the real git-shown objects, exit 1 on a tampered digest and on an absent dir → MAJOR-2 |
| 5 | transcript integrity + forged PASS lines | **PRESENT** | forged `PASS`→`FAIL`, forged measured number and an invented gate row all survive; `sec2_output` appears 0× in the receipt; 42 published rows vs 45 fired gates → MAJOR-9 |
| 6 | phantom consumers | **ABSENT in fact, PRESENT in mechanism** | all 8 delivered consumers are real gates and all 8 anchors are genuine in-context quotes; but a fabricated consumer name passes, and 7 of 8 anchors are never read again → MINOR-3, MINOR-4 |
| 7 | read-back before `os.replace`; staging cleanup; write-nothing | **ABSENT (defended)** | read-back present and verified; `os.unlink(tmp)` on refusal; write-nothing confirmed by **full tree hash** at all 9 modes. One residue: promotion is not atomic across the two artifacts → MINOR-7 |
| 8 | the 1 spelled numeral; plant `thirty-one` | **ABSENT (defended) / PRESENT (the whitelist)** | the single spelled numeral is `twenty-two`, correct and backed (22 declared SEC values). `thirty-one` passes **correctly** — 31 is measured. But `sixty-three` passes because it is not on the 26-word list → MINOR-8 |
| 9 | referent binding across the many universes | **PRESENT** | `kernel is 455`, `455 seam types`, `132,273 composites` all rc=0 → MAJOR-12 |

### Additionally requested

- **E-22 fence multiset, both directions:** **FAILS BOTH.** A forged 9th
  fence duplicating a legitimate verdict passes; deleting §9's four fences
  passes. Content-different fences do die → MAJOR-4.
- **E-23, all 38 descriptions vs code, three-legged:** leg 1 (declared gate)
  38/38; leg 2 (injection site exists) 38/38, and the instrument checks this
  itself; **leg 3 (description matches code) 32/38** → MAJOR-7.
- **Full 38-mutant sweep out of harness, one process each, at declared
  gates:** **38/38 ON TARGET**, zero survivors, and the four tracked files
  (`paper`, `code`, `output`, `receipt`) **byte-identical** before and after.
- **≥8 novel corruptions:** 44 injections and probes run (13 correctly
  refused, 2 legitimate changes correctly accepted, 29 corruptions accepted at
  exit 0), 23 of them novel to this seat
  (two cross-table header swaps, two cross-table row transplants, duplicated
  row, fence duplication, fence-block deletion, sentence-final unbacked
  numeral, capitalised polarity negation, post-gate stray read, raw-`open`
  bypass, post-seal mutation, post-seal add, de-sealed key, phantom consumer,
  forged transcript, invented gate row, empty-paper verify, paper-deleted
  `--no-write`, unlisted spelled numeral, and three cross-universe referent
  swaps).
- **Hostile argv:** 22 forms; every unknown flag, unknown mutant/anchor
  argument, missing argument, second mode flag and case variant (`-no-write`,
  `--no-write=1`, `--NO-WRITE`) exits 2 with the tree unchanged. A clean
  nine-mode re-run in an isolated tree confirms `tree=UNCHANGED` at
  `--numbers`, `--no-write`, `--selftest`, `--break-anchor` (rc=1),
  `--verify-paper`, `--list-gates`, `--list-mutants`, `--verify-sec` (rc=1 on
  an empty dir) and `--mutant MUT-LAWFUL`.
- **Byte ×2, off-tree, git-less, from artifact-deleted trees:**
  `PYTHONHASHSEED=1` **and** `PYTHONHASHSEED=987654` each reproduce
  `57c98674b479` / `b66fdfaacc33` **byte-identically** (`cmp` clean, zero
  `.git*` present in either tree). #91 holds at its own hands.
- **The ledger chain recomputed from bytes:** 42/42 digests, 42/42 links,
  head `a72a3ae7f7c3e91d` — **MATCH**.

---

## 5. THE SEAM RULING (#267)

**Ten of the thirteen majors are TEMPLATE-SHAPED, not SEC-2-shaped**, and
reproduce LOR's #267 families almost exactly:

| #267 family | here |
|---|---|
| paper-scanning walls | MAJOR-8 (walls pass on empty text), MAJOR-11 (prose flips unscanned) |
| full-table rendering | MAJOR-3 (table-blind claims) |
| typed totals-counts | MAJOR-13 (`union_min`), MINOR-9, MINOR-10 |
| transcript-full-integrity + digest-token whitelists | MAJOR-9, MINOR-8 |

New families this seat would add to the standing list: **(a)** containment-
masquerading-as-multiset (MAJOR-4, and the same bug in the claims gate);
**(b)** the case-sensitive polarity needle (MAJOR-10); **(c)** the
sentence-final numeral (MAJOR-5); **(d)** the sentinel falsifier that poisons
a gate's verdict variable instead of its measurement (MAJOR-7); **(e)** the
coverage gate that snapshots the gate list before appending itself (MAJOR-6).

**SEC-2's own** are MAJOR-2 (the read-set overclaim, sharp here because the
pin explicitly forbids the file that walks in) and MAJOR-8 (the vacuous
`--verify-paper`). MAJOR-1 is template but sharpened by timing: the #348
addendum that names it is the same day as this delivery.

I recommend the adjudication treat MAJOR-3/4/5/6/7/9/10/11/12/13 as the
**#267 sweep's first concrete work list** rather than as SEC-2 repairs alone —
every one of them is a two-to-six-line fix that should land in the shared
template.

---

## 6. DISCLOSURES AND LIMITS

- Every run was executed in
  `…/scratchpad/sec2_k3/` on copies; **no repo file was written except this
  review.** Scratch peaked at 566 MB (a full rsync mirror, since deleted) and
  closed at 4.2 MB. Per-run trees were deleted after each injection.
- **Honest execution note:** the box carried load averages of 105 → 335
  throughout (other agents' workers), so wall-clock times below are not
  informative. The first attempt at the second byte seed was killed by a
  signal (exit 143) mid-sweep; I relaunched it in a fresh artifact-deleted
  tree and it completed. **Both seeds are now measured and identical** — the
  leg is closed, not carried. Recorded because the killed run is in my
  scratch.
- **Recomputation count, honest:** 42 ledger digests + 42 chain links + 25
  seal digests + 8 anchors + 5 source shas + 4 #301 shas + 20 table and
  closed-form identities + 6 all-455 aggregates + 11 regex probes + 38 sweep
  targets = **201 independent recomputations**, plus the 455-group census
  (955 detector/inventory evaluations) and an independent scan of all 1,018
  numerals. **Zero disagreements with any delivered number.**
- **Executions:** 118 (1 baseline, 2 delivery, 38 out-of-harness mutants, 31
  `--verify-paper` injections, 5 code-injection runs, 1 seal/write probe, 3
  `--verify-sec`, 31 argv forms across two batteries, 4 vacuity/transcript
  probes, 1 all-455 census, 1 gate-list comparison).
- **I did not** re-derive the seam completion lattice or the price laws from
  first principles — those are the OPERATOR seat's, and I take them as given.
  My arithmetic checks on them are consistency checks, not reconstructions.
- One earlier argv battery collided with its successor on a shared directory
  and produced a spurious `tree=CHANGED` for `--numbers`. I killed it, re-ran
  in an isolated tree, and the correct reading is **UNCHANGED**. Recorded
  because the discarded run is in my scratch.

---

## 7. THE FIXES, LIFTABLE

**R-SEC2-K3-1** (MAJOR-1) — in `write_artifacts`, before staging: re-verify
every `SEAL.seals[k]` against `digest(R[k])` and re-verify totality; raise
`G-INTEGRITY` on either; emit both as ledger rows.
**R-SEC2-K3-2** (MAJOR-2) — record reads at an `open`/audit hook; re-run the
read-set comparison at the last gate; declare the three `READLOG.pop()`
exemptions.
**R-SEC2-K3-3** (MAJOR-3) — key the claim multiset by table; make `stray`
test `got[k] > want[k]`.
**R-SEC2-K3-4** (MAJOR-4) — `got == want` on fences with declared
multiplicity.
**R-SEC2-K3-5** (MAJOR-5) — `(?![\w])(?!\.\d)` in `NUM_RE`.
**R-SEC2-K3-6** (MAJOR-6) — MUT-FENCE / MUT-POLARITY / MUT-SPELLED; fix the
`G-COVERAGE` snapshot; `LATER_GATES` exempts ordering only.
**R-SEC2-K3-7** (MAJOR-7) — rewrite the six sentinel falsifiers to corrupt
measurements; publish the descriptions in the sealed `coverage` key.
**R-SEC2-K3-8** (MAJOR-8) — `PAPER_REQUIRED[0] = True` in `--verify-paper`,
`--no-write` and the delivery path; the three walls fail on empty text.
**R-SEC2-K3-9** (MAJOR-9) — move `R["ledger"]`/`ledger_chain`/`totals` after
the last gate; seal a `transcript` key; add `--verify-transcript`; make
`--list-gates` run `finish()`.
**R-SEC2-K3-10** (MAJOR-10) — casefold both sides in `locate()`.
**R-SEC2-K3-11** (MAJOR-11) — POLARITY rows for every headline direction
word; gate the inline verdict spans against `lawfulness.word`.
**R-SEC2-K3-12** (MAJOR-12) — referent-tagged needles for the six universes.
**R-SEC2-K3-13** (MAJOR-13) — measure `union_min` from the family and gate it;
re-aim MUT-REFINEMENT at the measurement.
**R-SEC2-K3-14** (MINORs 1, 5, 6) — constrain the seal partition (a key that
was measured may not be declared unsealed); make the two waiver forcings
match their code; make `G-INTEGRITY` a real gate.
**R-SEC2-K3-15** (MINORs 9, 11) — derive §8's fibers from `R["inventories"]`
and the window; extend the orbit control to the fate.

---

**Verdict: ACCEPT-WITH-FIXES.** The physics is measured and it holds — I
could not move a single delivered number, and I tried from outside the
instrument with an independent 455-group census. What I could move, at exit
0, was the paper's account of that physics: twenty-nine corruptions passed,
including five that invert a delivered finding in plain prose and four that
put fabricated rows and swapped headers into published tables. The seal is
total at the gate and unenforced at the door. Those are perimeter defects,
liftable in the listed lines, and mostly the corpus's rather than this
unit's — which is exactly what the #267 sweep exists to collect.

---

## CLOSE

All five objects re-verified against their opening digests, unchanged by this
review:

| object | sha256-12 |
|---|---|
| `v14/paper-40-sec2.md` | `aeeeb6757715` |
| `v14/code/sec2_exact.py` | `4cb4011cfa05` |
| `v14/code/sec2_output.txt` | `57c98674b479` |
| `v14/code/sec2_receipt.json` | `b66fdfaacc33` |
| `v14/note-sec2-pin.md` | `bfe5c66be9ec` |

Sole repo write: `v14/review-sec2-instrument.md`. Scratch closed at 4.5 MB;
every per-run tree deleted.

**K3 seat verdict: ACCEPT-WITH-FIXES — 13 majors, 11 minors, 15 lifted
repairs R-SEC2-K3-1..15. CANDIDATE UNTIL ADJUDICATION.**
