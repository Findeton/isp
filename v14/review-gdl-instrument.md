# GDL (paper-25) — K3 INSTRUMENT REVIEW

**Seat:** K3 INSTRUMENT, hostile. **Protocol:** v14 ledger #222, row K3;
HANDOFF-PROMPT.md §4 + §9; RUNBOOK E-22 / E-23 / E-24 and the §13/§14 tail.
**Era:** post-engraving-native — no birth-date excuses taken or offered.
**Object at 4c85ca4.** Read-only git; scratch-only execution; one repo write
(this file).

## GRADE: **AWF** (accept with fixes)

Five MAJOR and thirteen MINOR findings, every one with a liftable repair.
**No false measured number was found.** Every delivered value I recomputed —
including all fifteen cells of the §5 relation grid, all seven rows of the §9
fiber table, all fourteen anchor rows, both mechanism tables, the separation
ladder and every domination witness — came back exact. The verdict word is
right, the frozen exclusion is right, the mechanism is real and honestly
bounded, and the artifacts reproduce byte-for-byte off-tree at two hash seeds.
What the MAJORs are about is what the **instrument can certify**, not what it
measured: five forgeries I planted passed `--verify-paper` at exit 0, and one
planted forgery passed the whole measurement layer at exit 0. R is not
warranted (it would need a false number or an unsupported headline; there is
neither). A is not warranted either: three of the five survivals are in
classes the corpus has already engraved (E-22, #87), and one gate's sealed
statement asserts an immunity the code does not have.

---

## 0. Identity, verified at the start and at the end

| object | declared sha256-12 | worktree | `4c85ca4:` |
|---|---|---|---|
| `v14/paper-25-gdl.md` | `e98003841378` | = | = |
| `v14/code/gdl_exact.py` | `81595d600575` | = | = |
| `v14/code/gdl_output.txt` | `39128fafc7bf` | = | = |
| `v14/code/gdl_receipt.json` | `b87016e96285` | = | = |
| `v14/note-gdl-pin.md` | `fe9533371046` | = | = |

`git hash-object` of each worktree file equals `git rev-parse 4c85ca4:<path>`
for all five. Re-verified after all work: unchanged. HEAD moved under me
(082e61b → 39f04ca, a concurrent seat's commit); none of my five objects moved.
Sibling working-tree modifications (`r4c_multi_exact.py`, `r4dec_exact.py`,
`paper-21-r4dec.md`, the untracked `smu_*` / `review-perl-instrument.md`) are
disclaimed — not mine, not touched.

## 1. The reproduction battery

**111 executions of `gdl_exact.py`, all off-tree, in a provisioned copy holding
only the 11 declared sources + this unit's code + paper, with no `.git`
anywhere.**

| run | result |
|---|---|
| delivery, `PYTHONHASHSEED=0` | exit 0, 63/63 PASS; **both artifacts byte-identical to the committed ones** |
| delivery, `PYTHONHASHSEED=987654`, clean tree | **byte-identical again** (byte ×2 across seeds discharged) |
| bare copy, no repository present | exit 1, `GATE FAILED: G-PROVENANCE :: declared source not present ... this run is under-provisioned and writes nothing`; directory unchanged — **loud abort, wrote nothing** |
| `--selftest` | dies at `G-PROVENANCE`, exit 1; **verified independently** by taking the full file list, every sha256 and every mtime/size of the whole tree before and after: identical, and no `.tmp` residue |
| 27 argv vectors | 25 malformed → exit 2 with a named reason; `--list-gates` → 63 lines, `--list-mutants` → 56 lines; artifacts untouched |
| 56 `--mutant NAME`, **one process each, outside the harness** | **56/56 died at their declared gate**, exit 1 each; `shasum` of both artifacts unchanged; **no new files** in `v14/code/` (no `.tmp` residue) |
| 12 `--verify-paper` on injected papers | 7 died at a named gate, **5 survived at exit 0** (§5) |
| 12 patched-instrument probes | 6 died, **4 survived at exit 0**, 2 caught by the file's own AST self-scans before they could execute (§6) |

The in-run sweep's honesty is confirmed from outside: my 56 independent
processes agree with `mutant_sweep` row for row.

## 2. My rows, answered

### 2.1 THE VACUOUS STAMPING — *a genuinely failing cell CAN hide as VACUOUS*

Measured first: the 15 coupled VACUOUS cells are exactly the `RES-STEP`
column — 5 objects, 5 classes, 0 non-singleton classes, per cell — and the
frozen grid carries 6 more (the `G5` column at `RES-BRANCH` and at `RES-STEP`).
No delivered VACUOUS row carries a non-zero failure count. **The delivered
stamping is sound**, and it is sound by construction: inside `fdep`, a class
with one object carries one D-value, so `nonsing == 0` implies `bad == []` as a
theorem. Nothing hides in the delivered run.

The gate that is supposed to certify that is one conjunct short of certifying
it. `G-RELATION-CENSUS`'s per-row predicate is

```
(w == "VACUOUS" and row["nonsingleton_classes"] == 0)
```

— it never requires `failing_classes == 0`; and `nonsingleton_classes` is the
one census number the independent second pass does **not** recount. So the
VACUOUS stamp rests entirely on a number produced by a single code path and
checked against itself.

**Probe P1 (executed).** One genuinely PARTIAL cell
(`RES-BRANCH / G3-RECORD-LINK / D1`, 24 failing classes) restamped `VACUOUS`
with `nonsingleton_classes` forced to 0, **failure counts left truthful**:

- `G-RELATION-CENSUS` — PASS, "cells whose word disagrees with their census: none"
- `G-VACUITY-DECLARED` — PASS, and its own statement printed **"16 of the 45
  coupled cells ... are vacuous by construction"** — the run counted the forged
  cell as vacuous and said so
- `G-FAILURE-CENSUS` — PASS, "cells whose recount disagrees: 0"
- exit 0, 46/46 gates evaluated.

Probe P2 (the same forgery with the failure counts zeroed too) dies at
`G-FAILURE-CENSUS` (2 cells). So the only thing standing between the head's
"15 VACUOUS AND STAMPED VACUOUS RATHER THAN PASSED" and a mis-stamp is the
recount of a number the mis-stamp need not touch. Is singleton-ness itself
gated? **No** — it is asserted by `fdep` and compared with `fdep`.
→ **MAJOR-1.**

### 2.2 THE FAILURE-CENSUS SECOND PASS — *independent, and it bites*

`recount()` is a genuinely different code path, not the same function twice:
`fdep` builds `dict[g] → set` plus a `Counter` and flags on `len(set) > 1`;
`recount` builds `dict[g] → list` and flags on `any(v != vals[0])`, counting
objects by `len(vals)`. It reads no intermediate of `fdep`. It shares only the
*input pool* — which is what a recount must share, and is not the #82 failure
mode (that one is a comparator re-reading the builder's *product*).

Scope, measured: it recomputes **2 of the 7** published per-cell numbers
(`failing_classes`, `objects_in_failing_classes`) over **90 of 90** cells —
so the paper's "every failure set recounted" *understates* the coverage of the
cells and *overstates* the coverage of the fields. Both recounted numbers are
load-bearing in the paper ("3740 of 4080", "7,498 of 10,954").

**Probes P5 and P5b (executed).** Moving `fdep`'s failing-object count by one
→ dies at `G-FAILURE-CENSUS` with 66 cells caught; dropping one failing class
→ dies with 23 caught. The second pass has real teeth. **Not an E-23-family
finding.** The gap is only what it does not recount (`nonsingleton_classes`),
which is MAJOR-1.

### 2.3 THE FIBER DISCIPLINE — *disclosed, correct, not gated in the paper*

The fibers really are axes: 6 coin members at reading A plus the non-delivered
reading at the delivered coin = **7 runs covering 8 declared member ids**, and
`G-FIBER-EXECUTED` binds the executed ids to the declared ids **by set
equality**, not by a cardinality. I re-derived all seven rows from the receipt
and they match the paper exactly (10954/10954/11935/10045/11935/9043/11941,
frozen 5 throughout, one signature `da4248b1a55b`).

Could a reader think 6 × 2 = 12 combinations ran? Not from this paper: §9 says
"run as declared **axes**, not as a product", the table has seven rows, the
cross-product is explicitly disclaimed, and claim C13 says "all 7 executed
fiber members". **But the disclosure is not gated**: `axes_not_a_product` lives
in the receipt and is sealed, and nothing requires the sentence to be in the
paper — unlike the Diósi–Penrose, Lorentzian and hexagonal naming sentences,
which each have a mandatory-presence gate. Deleting §9's disclaimer leaves the
run green. → **MINOR-5.**

### 2.4 THE 56-MUTANT SWEEP OUTSIDE THE HARNESS, AND E-23

**56/56 on target in 56 separate processes**, artifacts and directory
byte-unchanged. The raising-gate parse is unambiguous: three gates are raised
outside the `Ledger` (`G-PROVENANCE` in `read_bytes`, `G-VERBATIM` in
`match_needle`, `G-ARTIFACT-INTEGRITY` in `Seal.close`) and **no mutant
declares any of the three**, so no falsifier can be credited with a death at a
gate that never ran.

E-23 descriptions vs code: I read **20 of the 56** hook sites in full against
their declared `(symbol, value)` and prose — the mechanism, relation, fiber,
exclusion, seal and paper falsifiers — and **every one is faithful**. All 56
have exactly one located hook site. So the delivered registry is honest.

The **gate** that certifies that honesty is much weaker than its statement:
both legs are substring containment. 23 of the 56 declared values are ≤2
characters; for 9 of those an alternative value string is also present in the
same hook segment; and `MUT-BLIND-D1`'s declared value `"1"` is a substring of
its own name `MUT-BLIND-D1`, which appears in the segment — the code leg for
that row is satisfied by the mutant's own name.

**Probe P3b (executed).** `MUT-UNITARY` re-declared as moving `uviol` to `0`
(both in the tuple and in the prose) while the code still writes `1`:
`G-FALSIFIER-HONESTY` **PASSES** — "declarations not matching their code:
none". **Probe P4 (executed).** `MUT-BLIND-D1`'s description rewritten to say
the opposite of what it does, keeping the symbol and value substrings:
`G-FALSIFIER-HONESTY` **PASSES**. → **MAJOR-3.**
(Probe P3 — value moved but prose left inconsistent — *is* caught, at
`G-MUTANTS-ON-TARGET`, because five late-gate mutants then die at
`G-FALSIFIER-HONESTY` instead of their own gates. A nice emergent property,
but it fires on the inconsistency, not on the falsehood.)

**The blindness numbers.** `0 / 164,310`: guarded by `G-BLINDNESS-D1` with
`d1_moves == 0` — a zero-aggregate, which is equivalent to a per-object
predicate, so #87 is satisfied in substance; falsified by `MUT-BLIND-D1`.
`54,593 / 54,770`: guarded three ways — `G-COOCCUPANCY` (`cooc_bad == 0`,
again a zero-aggregate), claim C8 assembled from the receipt, and the five
per-field table rows rendered from the receipt (whose D2 column sums to
54,593). Well guarded. But two things about that census are **claims with no
gate**: that the five count fields are *foreign* ("fields this run never
generates"), and the denominator itself (§2.10, MAJOR-4). I measured the first
myself — see §7 — and it is true.

### 2.5 E-22 INJECTIONS — five of twelve forgeries survive

The table is in §5. The three that matter:

**A duplicated-and-forged verdict fence passes at exit 0.** The gate reads

```
want = Counter(canon("```\n%s\n```" % s) for s in segs)
mult_bad = [k for k, v in want.items() if blockmap.get(k, 0) != v]
```

— containment in the `want → have` direction, never `have → want`. An *extra*
fenced block is invisible. My INJ-02 appended a second copy of the third head
segment reading "3 EXACT, 27 PARTIAL" beside the clean "2 EXACT, 28 PARTIAL".
The run **saw it** — its own coverage line printed "**4 fenced blocks**" and
"**67 fenced numerals**" against the clean paper's 3 and 49 — and passed:
`G-PAPER-HEAD-VERBATIM` PASS, "multiset mismatches 0", 53/53 gates, exit 0.
The gate's sealed statement says "the fenced blocks are gated by MULTISET
EQUALITY (E-22) rather than by containment, **so a duplicated block cannot
shadow a forged twin**". That is the exact scenario E-22 was bought for and the
exact scenario that survives. → **MAJOR-2.**

**Table row swaps survive in three of the paper's tables.** `paper_tables()`
renders 16 rows: the separation ladder, the mechanism census, the co-occupancy
ladder and the dominations. It does **not** render the §5 relation grid (the
unit's central result), the §2 anchor table, the §9 fiber table or the §12
choice inventory. Swapping two entries within an unrendered table leaves every
numeral registered, so coverage passes too: INJ-03 (relation grid, D2 and D3
entries of the `G1` row exchanged), INJ-09 (anchor table, A-FROZEN and
B-COUPLED ladders exchanged) and INJ-10 (fiber table, `w/3`'s object count
moved from 11935 to another member's 10045) all pass at exit 0, 53/53 gates.
E-22: "Tables render as claims." Four of eight do not. → **MAJOR-2.**

**A fabricated numeral passes the coverage scan — and it is the falsifier's own
needle.** INJ-06 put `123456789` into §2's prose. `G-PAPER-NUMERAL-COVERAGE`
scanned 314 numerals and reported "unregistered numerals: **none**". Cause:
`known = receipt_numbers(R) | ...` serializes the **whole** receipt, including
the instrument's self-description — and `R["mutants"]` publishes
`MUT-PAPER-NUMERAL`'s declared corrupted value, which is `123456789`. **The one
numeral the declared falsifier uses to test the coverage gate is the one
numeral the gate can never flag**, and the falsifier only appears to work
because it bypasses the scan with `pick(..., cov["unregistered"],
["123456789"])`. Its published description — "an unregistered numeral" — is
false of this run. Attributed pollution, measured: **123 of the 400 known
tokens (33 of them ≥4 digits) come from non-measured keys** —
`seal_manifest` +53 (the seal digests' digit runs), `gates` +35,
`provenance` +29 (the source sha256-12s), `verbatim_anchors` +11,
`transcript_head` +9, `mutants` +3. → **MAJOR-4… (numbered MAJOR-3 below is
E-23; this is MAJOR-2's sibling — see the numbered list).**

The seven that die, die correctly and at named gates — including the #125
case: the retracted L-1 sentence, line-wrapped **and** blockquoted, dies at
`G-WALL-L1`. Anchors' consumers: all 11 distinct consumer gates named by the 12
verbatim anchors are in the declared registry, evaluated in the run, and
falsified by a declared mutant. **No phantoms** (the paper-22 lesson holds).

### 2.6 E-24 — every published fraction is measure-labelled

I swept all 313 numerals of the paper and traced every fraction to its receipt
key. The rationals in §2 (both inverse participations, both exit probabilities)
live under `rebuild`; those in §8 (the domination witnesses and the step-1..3
values `1`, `11/27`, `619/2187`, `0`, `0`, `128/729`) live under `prediction`;
both keys declare **THE BRANCH MEASURE**, spelled out as the emission law's own
product measure over the branching tree with level masses measured to be
exactly 1. The counting layers — `relation`, `forcedness`, `mechanism`,
`prediction`'s step indices, `counts`, `walls` — are stamped **COUNTING-ONLY**.
`measure_scan` finds 3 keys carrying fractions and 0 undeclared. **E-24 is met
for the delivered content.** The scan itself is narrow (MINOR-9), and the ℓ₁
pricing has a scope consequence the paper does not state (MINOR-11).

### 2.7 SEALS — total, gate-time, and the post-write path really is closed

34 seals + 2 declared-unsealed = **36 = every top-level receipt key**; the two
unsealed keys are frozen as a tuple, measured to intersect neither the sealed
paths nor the measured keys, and chained after read-back. `SEAL.close` verifies
all 34 before the payload is built (so no sealed value moved after its seal),
and the terminal gate corrupts all 34 in turn on a read-back copy and catches
34/34.

**Seal window, audited by AST**: for each of the 34 `SEAL.take` sites I located
the nearest preceding `LD.gate` and compared it with the declared
`sealed_at_gate`. **27 match; 7 do not** — `SEAL-REBUILD`, `SEAL-FUNCTIONALS`,
`SEAL-GROWTH`, `SEAL-RELATION`, `SEAL-FORCEDNESS`, `SEAL-MECHANISM`,
`SEAL-PREDICTION` are taken after a *block* of gates and declare the block's
**first** gate. That is the safe direction (the value survived more gates, not
fewer) and no value moves in between — but the manifest's published
`sealed_at_gate` is inaccurate for those 7 rows. Not the #148 late-seal shape.
→ **MINOR-2.**

**Post-write corruption (probe P6d, executed).** Corrupting the staged payload
on disk between the write and the terminal gate: `G-ARTIFACT-INTEGRITY` FAILS
with "sealed objects broken on disk **['SEAL-COUNTS']**", `os.replace` never
runs, **both real artifacts byte-unchanged**. The `os.replace`-after-the-gate
order does what it claims. Two earlier attempts to instrument that path (P6,
P6b) were caught *first* by the file's own AST self-scans — `selftest_shape`
saw a third `open()` in `finish`, `writer_shape` saw a third `.replace` — which
is a genuine strength of the writer perimeter. One residue: the failing run
**leaves `gdl_receipt.json.tmp` and `gdl_output.txt.tmp` on disk**. Nothing is
promoted, but "failing runs write nothing" is not literally true.
→ **MINOR-10.** And a corrupt-but-unparseable staged payload raises
`JSONDecodeError` from `json.loads(read_text(tmp_j))` instead of failing the
integrity gate (measured in probe P6c: traceback, exit 1, artifacts still
untouched). → **MINOR-12.**

### 2.8 CLI

27 vectors. All 25 malformed ones exit 2 with a named reason, including every
arity case (`--mutant` bare, `--break-anchor` bare, `--mutant NOPE`,
`--mutant X EXTRA`, `--verify-paper a b`), abbreviation (`--no-writ`),
`=`-form (`--no-write=1`, `--mutant=NAME`), case (`--NO-WRITE`), trailing space,
empty string, bare `--`, repeated flag, and five second-mode compositions.
`--list-gates` prints exactly the 63 registry names, `--list-mutants` exactly
56. Artifacts unchanged throughout.

The in-run gate exercises **10** malformed vectors (the last three second-mode)
and 9 legal shapes — but it calls `parse_args` and catches `CliError`; it never
observes an exit code, while its statement says the vectors "are all rejected
**with exit code 2**". The mapping is one line in `main`, and `main(argv)`
returns 2 for a parse error without touching the census, so the gate could
measure what it says for free. → **MINOR-6.** `--selftest` is likewise never
executed by the delivery run: `G-SELFTEST-WRITES-NOTHING`'s predicate is the
AST probe's value, which the statement discloses ("and the predicate is the AST
probe's own value"). I executed it externally: exit 1, wrote nothing.

### 2.9 BYTE ×2, OFF-TREE, GIT-LESS

Done twice at two `PYTHONHASHSEED` values in two independently provisioned
trees with no `.git`: both artifacts byte-identical to the committed ones both
times. The one `sorted(..., key=repr)` in the file (`fdep`'s `bad`) is over a
dict's keys and is consumed only by `len` and `sum`, so it cannot carry an
ordering; the #160 v10 tie-break rule does not bind this unit (it drives no v10
grammar layer) and the underlying risk is discharged empirically anyway.

### 2.10 THE PAPER ↔ OUTPUT ↔ RECEIPT SWEEP, AND THE CHECKER ITSELF

I re-implemented the scanner independently and got **exactly 313** — prose 127,
fenced 49 (in 3 fenced blocks), inline 137 (in 221 inline spans) — matching the
receipt's `paper_coverage` field for field, with 0 unregistered.

I then asked what the scanner *misses*. Of 522 raw digit-runs in the file, 155
escape the regexes; I classified every one, and **all 155 are identifier or
digest digits** — `D1`, `G2`, `F11`, `l_1`, `S3`, `L-1`, `paper-20`,
`sha256-12`, `fe9533371046`, `da4248b1a55b`, `w/3`, and the Gram matrix's
`-1/2`. No measured claim numeral escapes. The lookbehinds are doing exactly
the right work.

Discriminating power, measured: over the 52 distinct ≥3-digit tokens, **95.0%**
of single-character corruptions (1,998 of 2,103) would be flagged; 5.0% would
be accepted because the corrupted value is some *other* measured number. That
is the right order for a coverage gate — coverage is not identity. Identity is
carried by claims, rendered tables and the head; and there I measured the real
number: **118 of the paper's 308 canonical numerals (38%) sit inside an
identity-bound string**; the other 190 are coverage-only, and they include the
whole §2 anchor table, the whole §5 relation grid and the whole §9 fiber table
— which is why INJ-03/09/10 survive.

**The one denominator error.** `mechanism.checks = 164,310 = 5 fields ×
10,954 objects × 3 functionals`. D1's own census is **54,770**. Claim C7, §7's
sentence and `G-BLINDNESS-D1`'s evidence all say the inverse participation
"does not move once in **164,310** checks" — counting D2's and D3's checks as
evidence for D1. The same file already computes the right denominator for D2
(`me["checks"] // len(D_SHORT)` in C8), so §7 shows **two different
denominators for the same census in adjacent sentences**: 164,310 for D1 and
54,770 for D2. The head's "AT 164,310 CHECKS" is fine (it labels the whole
census). → **MAJOR-5**, and the only finding that requires a change to the
delivered paper text besides MINOR-8.

---

## 3. MAJOR findings

**MAJOR-1 — the VACUOUS stamp is certified against itself; a failing cell
passes as VACUOUS.** Demonstrated (probe P1, exit 0, 46/46 gates, the gate
itself printing "16 of the 45 coupled cells ... are vacuous").
*Repair, two lines.* (a) In `G-RELATION-CENSUS`, make the VACUOUS clause
`(w == "VACUOUS" and row["nonsingleton_classes"] == 0 and
row["failing_classes"] == 0)`. (b) Have `recount` return a third number,
`sum(1 for g, vals in byg.items() if len(vals) > 1)`, and compare it against
`row["nonsingleton_classes"]` in `G-FAILURE-CENSUS`. (c) Add a falsifier for
the direction that matters — one that stamps a PARTIAL cell VACUOUS with its
counts intact — since `MUT-VACUITY` only tests EXACT-on-a-vacuous-test.

**MAJOR-2 — E-22 is met in name and not in mechanism, twice.**
(a) The fenced-block leg is containment, not multiset equality: an extra forged
fence passes (INJ-02, exit 0), and the gate's sealed statement asserts immunity
to exactly that. *Repair:* `mult_bad` over `set(want) | set(blockmap)`, i.e.
`blockmap == want` as Counters (this paper's fences are exactly its three head
segments, so full equality is the right predicate); declare any non-head fence
set explicitly if one is ever needed. Re-point `MUT-PAPER-BLOCK` at the
*extra-block* direction.
(b) Four of the paper's eight tables are not rendered from the receipt, and a
swap inside any of them passes (INJ-03, INJ-09, INJ-10, all exit 0). *Repair:*
extend `paper_tables()` with the §5 grid rows (`"| \`%s\` | %s, \`%d\` of
\`%d\` ... |"` built from `grid_coupled`), the §2 anchor rows (from
`rebuild.anchor_rows`) and the §9 fiber rows (from `forcedness.rows`) — the
machinery already exists and the delivered paper's text already matches those
values exactly, so the repair is additive and cannot move a number.

**MAJOR-3 — the E-23 honesty gate cannot detect a false or inverted
declaration.** Both legs are substring containment: `declared[0] in seg and
declared[1] in seg` for the code, `moves in why and to in why` for the prose.
Demonstrated: a falsifier declared to move `uviol` to `0` while its code writes
`1` passes (P3b); a description inverted in meaning passes (P4). 23 of 56
declared values are ≤2 chars; `MUT-BLIND-D1`'s declared value is a substring of
its own name. *Repair:* parse the hook's AST rather than its text — require the
declared symbol to be an assignment **target** in the enclosing statement and
the declared value to be the source of the `pick(...)` third argument
(`ast.unparse(call.args[2])`), compared as a string. That is exact, cheap, and
kills both P3b and P4.

**MAJOR-4 — the coverage gate's allowlist is polluted by the instrument's own
self-description, including the falsifier's own needle.** Demonstrated
(INJ-06, exit 0, "unregistered numerals: none" over 314 scanned). 123 of 400
known tokens come from non-measured keys. *Repair:* build `known` from
`receipt_numbers({k: R[k] for k in MEASURED_KEYS}) | NUMREG | NUM_ALLOW |
head_numbers(R)`. **Verified liftable: under that tighter set the delivered
paper still has zero unregistered numerals, while `123456789` becomes
unregistered.** Then make `MUT-PAPER-NUMERAL` plant its numeral in the paper
text rather than in the gate's input.

**MAJOR-5 — the D1 blindness claim's denominator is the three-functional census
total, not D1's own.** 164,310 vs 54,770; the paper shows both denominators for
the same census in adjacent sentences of §7. *Repair:* in `paper_claims`, C7 →
`com(me["checks"] // len(D_SHORT))`; in `G-BLINDNESS-D1`'s evidence,
`com(bl_checks // len(D_SHORT))`; in §7, "does not move once in **54,770**
checks — 5 declared foreign count fields at every one of the 10,954 coupled
objects". The head needs no change. **No measured value moves.**

**(A sixth, argued and left as MINOR-1 rather than MAJOR because its content is
redundantly covered per object: `G-FUNCTIONALS-DECLARED` is a one-object probe
— see below.)**

## 4. MINOR findings

1. **`G-FUNCTIONALS-DECLARED` is a `#87` one-object probe.** `probe =
   C["co"][-1]`: the three declared specifications are checked at 1 of 10,954
   objects, and two of the three legs re-type the constructor's own expression
   on the constructor's own intermediate (`D1 == sum(x*x for x in p)`,
   `D3 == sum(D3row)`). D2's leg is redundantly covered per object by
   `G-PURITY-SPLIT`; D1's by `ID-RATE-IS-BORN` + `ID-D1-IS-SQUARED-RATE`;
   **D3's is covered nowhere else** — the only record-reading functional and the
   carrier of the prediction row. *Repair:* run the three comparisons over
   `C["co"] + C["fz"]` (32,877 checks, negligible cost) and publish the count.
2. **7 of 34 seals declare a `sealed_at_gate` that is not where they were
   taken** (§2.7). *Repair:* an AST self-check in the file's own idiom —
   for each `SEAL.take` site require the nearest preceding `LD.gate` name to
   equal the declared gate — and either move the takes or re-declare the block's
   last gate.
3. **The "axes, not a product" disclosure is not gated in the paper** (§2.3).
   *Repair:* a fourth mandatory-sentence gate beside DP/Lorentz/hex, or a claim
   `C15` assembled from `forcedness.axes_not_a_product`.
4. **`G-LAW-KERNEL`'s headline count includes a leg that cannot fire.**
   `law_kernel` computes `M = sum(qrow)` and `G1 = sum(qrow)` on the next line,
   so `G1 != M` is identically false; that leg is `law_native` = **296,784 of
   the published 1,479,176 (20.1%)**. The other two legs (`sum(k) == 1`,
   `qrow[i] == k[i]*M`) are contingent on what `law_kernel` returns and would
   fire on a wrong kernel, and the real evidence for the law-native normaliser
   is `G-PARENT-REPRODUCED`. *Repair:* derive `G1` from an explicit terminal
   condition (`sum(qrow[i] * G0[shift(x,i)])` with `G0` a computed vector of
   ones) or drop the leg from the count.
5. (see MINOR-3 above — fiber disclosure.)
6. **`G-CLI-WHITELIST` asserts an exit code it does not measure** (§2.8).
   *Repair:* `codes = [main(list(v)) for v in malformed]`, require all `== 2`.
7. **"located verbatim" is token-wise, and for one anchor row it is vacuous.**
   `locate_in_parent` requires each numeral of the row to appear in a JSON-ish
   context, not the row's own string. Measured: perturbing any multi-digit token
   breaks location (`284079`, `10528`, `11045`, `9752`, a perturbed
   24-digit numerator all fail to locate), but the max-cell ladder
   `[2, 2, 3, 3, 4]` is all single digits and `[2, 2, 3, 3, 5]` locates just as
   well. 1 of the 14 location rows carries no information; its equality leg is
   exact, so nothing is at risk. *Repair:* search the row's rendered string, or
   require a per-token length floor.
8. **Denominator labels in §5.** "PARTIAL, `3740` of `4080` classes" uses the
   **non-singleton** class count as the denominator (there are 6,856 classes);
   the same table's EXACT cell already says "non-singleton classes". 4,080 is
   the right denominator — only a non-singleton class can fail — it just needs
   its name. Likewise "45 cells per arm ... 2 exact, 28 partial, 15 vacuous" is
   the **coupled** arm's census; the frozen arm's is 1 / 38 / 6 and is never
   summarised.
9. **E-24's scan is narrow.** `measure_scan` matches only values that are
   *exactly* `^-?\d+/\d+$`, so a fraction inside a sentence is invisible to it,
   and 11 of the 14 `MEASURE_LEDGER` entries are never consulted (`functionals`
   is labelled BRANCH_MEASURE though its contents are counts). No effect on the
   delivered content — I traced every published fraction to a declared key.
   *Repair:* scan for the fraction pattern anywhere inside a string.
10. **A failing terminal gate leaves both `.tmp` files on disk** (§2.7).
    *Repair:* `try/finally` around the stage-gate-promote block with
    `os.unlink` on failure.
11. **No D2 verdict transfers to the ℓ₁ form, and the paper does not say so.**
    D2 is `Σ_{x≠y}|ρ_xy|²`, which is not a monotone function of `Σ_{x≠y}|ρ_xy|`,
    so neither the D2 domination flip nor D2's separation step is inherited by
    the ℓ₁ functional the head says D2 stands in for. The pricing is disclosed
    (§3, F6, the head); the non-transfer is not. One sentence in §3.
12. **`json.loads(read_text(tmp_j))` is unguarded** (§2.7): an unparseable
    staged payload raises rather than failing `G-ARTIFACT-INTEGRITY`.
13. **`writer_shape` counts any `.replace(...)` in `finish` as an `os.replace`**
    (it matches on `n.func.attr` alone). Conservative, not a hole — it caught my
    own probe — but it should match `os.replace` specifically.
    **Two grain slips worth one line each:** §7 and `G-COOCCUPANCY` say D2 moves
    "at not one **pair** whose occupied-link sets meet in at most one link",
    while the measurement is per **object** (an object none of whose site pairs
    co-occupy) — the head gets this right; and §12's closing sentence says every
    declared item's execution "is bound by set equality against the declared
    member ids", which is true of F2 and F3 and is a cardinality binding for
    F5/F7/F8/F10.

## 5. The injections table (12, all via `--verify-paper`, 53 paper-side gates)

| # | injection | outcome |
|---|---|---|
| INJ-01 | backticked numeral `10954` → `10944` (inline span) | **DIED** `G-PAPER-NUMERAL-COVERAGE` — "unregistered numerals: ['10944']" |
| INJ-02 | third verdict fence duplicated, twin forged to "3 EXACT, 27 PARTIAL" | **SURVIVED** exit 0 — run saw 4 fences / 67 fenced numerals, "multiset mismatches 0" |
| INJ-03 | §5 relation grid, `G1` row's D2/D3 entries swapped | **SURVIVED** exit 0, 53/53 |
| INJ-04 | separation ladder forged, `D3` at 3 → 4 | **DIED** `G-PAPER-TABLES` — "['\| `D3` \| 3 \|']" |
| INJ-05 | head fence numeral `27 OF 27` → `26 OF 27` | **DIED** `G-PAPER-HEAD-VERBATIM` |
| INJ-06 | prose numeral `123456789` | **SURVIVED** exit 0 — 314 scanned, "unregistered: none" |
| INJ-07 | polarity flip, "the record **does not** determine the decoherence" | **DIED** `G-PAPER-CLAIM-POLARITY` |
| INJ-08 | §7 mechanism table, STALE/ALL-TWO rows exchanged | **DIED** `G-PAPER-TABLES` |
| INJ-09 | §2 anchor table, A-FROZEN/B-COUPLED ladders exchanged | **SURVIVED** exit 0, 53/53 |
| INJ-10 | §9 fiber table, `w/3` objects 11935 → 10045 | **SURVIVED** exit 0, 53/53 |
| INJ-11 | retracted L-1 sentence appended, line-wrapped + blockquoted | **DIED** `G-WALL-L1` (#125 holds) |
| INJ-12 | "collapse rate in kilogram" in the paper's own text | **DIED** `G-WALL-NO-SI` — "['collapse rate in kilogram', 'kilogram']" |

## 6. The probes table (12 patched-instrument runs)

| probe | what it forges | outcome |
|---|---|---|
| P1 | PARTIAL cell stamped VACUOUS, `nonsingleton_classes`→0, counts truthful | **SURVIVED** exit 0 |
| P2 | same, with the failure counts zeroed too | DIED `G-FAILURE-CENSUS` (2 cells) |
| P5 | `fdep`'s failing-object count moved by one | DIED `G-FAILURE-CENSUS` (66 cells) |
| P5b | `fdep`'s failing-class list short by one | DIED `G-FAILURE-CENSUS` (23 cells) |
| P3 | `MUT-BLIND-D1`'s declared value 1→0, prose unchanged | DIED `G-MUTANTS-ON-TARGET` (5 late mutants displaced) |
| P3b | `MUT-UNITARY` declared **and described** as writing 0 while the code writes 1 | **SURVIVED** exit 0 — `G-FALSIFIER-HONESTY` PASS |
| P4 | `MUT-BLIND-D1`'s description inverted, symbol and value kept | **SURVIVED** exit 0 — `G-FALSIFIER-HONESTY` PASS |
| P7 | the 56-mutant sweep fabricated — no mutant executed, all rows `on_target` | **SURVIVED** exit 0 — `G-MUTANTS-ON-TARGET` "56 of 56", `G-SWEEP-BOUND` PASS |
| P6 | staged payload corrupted after the write (via a new `open`) | DIED `G-SELFTEST-WRITES-NOTHING` — the AST probe caught the tampering first |
| P6b | same, via `os.open` but using `str.replace` | DIED `G-WRITER-SHAPE` — the AST probe caught it again |
| P6c | same, corruption not valid JSON | uncaught `JSONDecodeError`, exit 1, artifacts untouched, `.tmp` left |
| P6d | same, length-preserving and valid JSON | **DIED `G-ARTIFACT-INTEGRITY`** — "sealed objects broken on disk ['SEAL-COUNTS']"; `os.replace` never ran; **artifacts byte-unchanged**; `.tmp` left |

**P7 deserves its own line.** `G-SWEEP-BOUND`'s statement is "THE SWEEP'S
EXECUTION IS BOUND, NOT DECLARED", and its predicate is `len(sweep_rows) ==
len(MUTANTS) and all(on_target) and SWEEP_GATE in ran_here` — all three
properties of the rows' **content**. A delivery-level run that executes no
mutant at all publishes a complete on-target sweep at exit 0. The delivered
sweep is genuine — my 56 out-of-harness processes confirm it row for row —
but the gate cannot tell, and an external seat had to supply that. I count this
inside MAJOR-3's family (falsifier machinery certified by its own declarations);
*repair:* have `run_mutant` record the `GateFail` evidence string it actually
caught and require every sweep row to carry a non-empty evidence string naming
its gate, sealed with the row.

## 7. Things I tried to break and could not

- **The frozen collapse and the object counts.** An independent 30-line
  record-only walk sharing only the module's primitives reproduces
  11,044 → 10,954 with per-level 1/3/27/486/10,437; 9,751 → **5**, one per
  level; 12,181 → 11,941 on the record menu; and **6,856 distinct records**,
  which is exactly the `G1` class count of the `RES-BRANCH` grid.
- **"Fields this run never generates."** Measured, not assumed: none of the
  five foreign count fields is among the 6,856 records the run generates, and
  exactly two are inadmissible. The paper's claim is **true** — and **ungated**;
  a one-line predicate (`field in {o["n"] for o in C["co"]}`) would close it.
- **The mechanism's arithmetic.** 54,770 − 54,593 = 177 non-movers; 31 objects
  carry no co-occupancy pair, i.e. 155 (object, field) pairs; the residual 22
  are co-occupying objects whose D2 still did not move. So co-occupancy is
  **necessary and not sufficient** — which is exactly, and only, what §7 claims
  ("Co-occupancy is *necessary*").
- **Every unrendered table.** §5's fifteen cells (3740/4080, 4074, 4041; 104/120,
  116, 117; 24/31, 25, 31; 2/4, 2, 3; EXACT 130, 128, 129), the coarsening
  series 7498 / 10599 / 10905 / 10923, the cell-grain triple 7498 / 8166 / 8100,
  55,140 site-rows, §9's seven rows, §2's fourteen anchor rows, §7's two tables
  and §8's dominations and witnesses: **all exact against the receipt.**
- **The frozen exclusion.** 2 coupled EXACT cells, both excluded, 0
  gravitational. The `RES-BRANCH` leg is carried by the per-object identity
  (the frozen partition test there is VACUOUS, which decides nothing) and **the
  paper says so** in §6. Honest.
- **The seal and the writer perimeter.** 34/34 probes caught; 34 seals verified
  at close and again from disk; the two AST self-scans caught two of my three
  tampering attempts before they could run.
- **The head.** Derived twice — the comparator is handed a JSON round-trip of
  the twelve measured blocks, types its own templates, and re-derives the
  outcome word and the fiber agreement (`_agree`) from the rows. Forging a
  numeral in the head dies at the comparator (`MUT-VERDICT-VALUE`, on target)
  and forging it in the paper dies at `G-PAPER-HEAD-VERBATIM` (INJ-05).

## 8. Era-compliance table (full standard)

| standard | verdict | evidence |
|---|---|---|
| candidate readings between delivery and adjudication | **met** | stated at the top of the paper and specifically for §7 |
| #82 CLI contract | **met with MINOR-6** | 27 external vectors; 10 in-run; real `--selftest` (exit 1, wrote nothing, verified externally over the whole tree); `--mutant NAME` harness, 56/56 outside the harness |
| #82 comparator independence | **met** | JSON round-trip boundary, own templates, own accessors, outcome word and `_agree` re-derived; shared literals are template prose only |
| #87 gates bind objects | **met except one gate** | unitarity, kernel, rates, purity split, identities, coin admissibility, relation cells all per object; **`G-FUNCTIONALS-DECLARED` is a one-object probe** (MINOR-1); the zero-aggregates (`d1_moves`, `cooc_bad`, violation counts) are per-object-equivalent |
| #91 no moving refs / off-tree / git-less | **met** | 11 sha256-pinned sources, every read gated; byte-identical off-tree and git-less at two seeds; bare copy aborts loudly |
| #160 v10 tie-break | **N/A** | no v10 grammar layer; hash-seed independence measured anyway |
| #119 + totality + vouching | **met with MINOR-2** | 34 + 2 = 36 = every key; gate-time seals; disk-vs-seal integrity proven by P6d; vouching layer inside the seal; 7 `sealed_at_gate` labels inaccurate |
| #125 text gates as written | **met** | INJ-11 (line-wrapped + blockquoted banned sentence) dies; whitespace + ASCII-fold + markdown-prefix normalisation on both sides; polarity is case-insensitive on top |
| #20 + fenced blocks | **met** | 313 numerals incl. 49 fenced and 137 inline, independently reproduced; escapes are identifier digits only |
| E-22 inline spans | **met** | INJ-01 dies |
| E-22 blocks by multiset | **NOT met** | MAJOR-2(a), INJ-02 survives |
| E-22 tables render as claims | **partly met** | 4 of 8 rendered; MAJOR-2(b), INJ-03/09/10 survive |
| E-23 falsifier honesty | **descriptions honest; gate NOT met** | 20 read in full, all faithful; P3b and P4 pass — MAJOR-3; P7 — the sweep is certified by its own rows |
| E-24 measure relativity | **met with MINOR-9** | every published fraction under a BRANCH-MEASURE key; counting layers stamped COUNTING-ONLY; 0 undeclared |
| #34 honest denominators + reachability + waivers | **met except one denominator** | 56 falsifiers all reach their gates, 0 dead; 11 waivers each with a forcing; 52/63 gates mutant-covered, 0 uncovered, registry drift 0; **MAJOR-5** |
| §15 declared-arena-as-data | **met** | scope paragraph, §13, and the prediction row all name the arena, the horizon and both declared axes; forcedness measured across them |
| single-threaded, no silent caps, counts computed, head derived + rendered | **met** | no correction narrative; every published count comes from `reg()`/the receipt; head rendered and matched verbatim; three gate cardinalities named rather than conflated |
| failing runs write nothing | **met in substance, MINOR-10 in letter** | nothing promoted (P6d); two `.tmp` files remain |

## 9. Counts

- **111 executions** of `gdl_exact.py` (2 deliveries, 1 bare, 1 selftest,
  27 argv, 56 mutants, 12 injections, 12 probes), all off-tree, plus 2
  module-importing analyses of my own.
- **613 recomputations and structural checks**, counted honestly: 15 object
  identities, 4 byte comparisons, 14 cardinalities, 34 seal-window sites,
  8 scanner reimplementation counts, 6 allowlist measures, 2 identity-bound
  measures, 60 §5 grid checks, 28 fiber-table, 23 anchor-table, 21 mechanism,
  22 co-occupancy, 29 separation/domination, 16 identity-census and coarsening,
  13 identity/exclusion, 5 machine-count decompositions, 16 independent-walk
  values, 11 foreign-field checks, 56 + 56 + 20 E-23 checks, 4 E-24, 11 waivers,
  12 anchor-location probes, 27 CLI outcomes, 3 write-nothing comparisons,
  12 + 12 + 58 outcome checks, 39 measurement-layer/coverage checks.
- **Zero false numbers found** in the paper, the receipt or the transcript.
- Findings: **5 MAJOR, 13 MINOR**, all with liftable repairs; none moves a
  delivered value.

## 10. What I did not do

I did not touch `LOG.md`, `STATUS.md`, `RUNBOOK.md` or any object outside this
file. I did not re-run the physics beyond the two independent record-only walks
described in §7 — the operator seat (K1) owns the rebuild. I did not weigh the
head's *grammar* (GDL-PARTIAL vs GDL-DECOUPLED-AT-THE-GRAVITATIONAL-BAR); that
is K2's row, and nothing I measured bears on it except to confirm that
`gravitational_cells = 0` is what the instrument computed and published.
