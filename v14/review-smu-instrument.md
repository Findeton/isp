# SMU (paper-27) — K3, THE INSTRUMENT LENS — HOSTILE REVIEW

**Seat:** K3, INSTRUMENT. **Protocol:** v14 ledger #235, row K3.
**Object at 6d8582e:** paper `d14689919289`, code `394cbfca621c`, output
`0bf6cc0502e6`, receipt `808aca088ff6`; pin `a1fca5e7b238`. **All five
hashes verified at the start of this review and again at the end; all five
unchanged.** Sibling worktree modifications (papers 22/25/28, the gdl / perl /
r4c code) disclaimed — none touched. Read-only git throughout; every
execution off-tree in `scratchpad/smu-in/`, in git-less directory trees
provisioned by `git show 6d8582e:`; one repo write, this file.
**Era: post-engraving-native. No birth-date excuse is applied anywhere below.**

## GRADE: **AWF** — accept with fixes

Four MAJOR findings, all demonstrated by execution, all repairable inside
mechanisms the instrument already contains. **No computed number is wrong**:
324 independent recomputations of published quantities, zero mismatches, no
number moved. The verdict string, its head, and the head's two derivations
are sound and the comparator is genuinely independent. What fails is the
*guarding*, in four places: the paper's tables and quotations are ungated; the
census seal is taken fifteen gates after the values it vouches; a refusing
artifact-integrity gate leaves both corrupted artifacts promoted on disk; and
fifteen of the forty-two falsifiers corrupt no object, two of them because
their gate cannot fail on any object at all.

**Counts.** 92 executions of the instrument (42 mutant runs as separate
processes out of harness; 20 injection runs covering 15 distinct injections,
**five of them — every code-side one — reproduced in a second independent
sandbox with identical outcomes**; 6 off-tree byte-reproduction runs across
four hash seeds; 23 CLI invocations; 1 bare-copy abort), plus 3 corrupted
runs inside `--selftest`. 324 independent recomputations of
published quantities, zero mismatches. 350 paper numerals classified
for gate-protection; 42 falsifiers classified for object-corruption power; 71
anchor-consumer and seal-gate names resolved against the ledger.

---

## 1. THE DISEASE SWEEP

Every disease this era's panels found live in a sibling, checked here.

| # | disease | verdict here | evidence |
|---|---|---|---|
| 1 | **phantom consumers** | **ABSENT** | 42 anchor `consumer` names + 29 seal `gate` names = 71, all resolve in the 57+2 ledger. Zero phantoms. |
| 2 | **constant-boolean falsifiers** | **PRESENT** | 15 of 42 plant no object; 15 gates have no object-corrupting falsifier; 2 of those gates are entailed by predecessors. **MAJOR-4.** |
| 3 | **E-23 semantic dishonesty** | **PRESENT, minor** | 2 published descriptions assert a corruption that does not occur; 2 more marginal. **MINOR-6.** |
| 4 | **containment fences** | **ABSENT** | the gate is `blocks == [wsnorm(verdict)]` — *list* equality, stronger than multiset. Duplicating the **clean** fence dies (INJ06); a forged twin dies (INJ07). |
| 5 | **unrendered tables** | **PRESENT** | 0 of 3 data tables rendered as claims. Two row swaps delivered at exit 0. **MAJOR-1.** |
| 6 | **blanket whitelists** | **PRESENT, small** | `STRUCTURAL` forgives 0–27 unconditionally but only `17`,`21`,`22` are not otherwise in the pool; 30 pool entries come only from sha256 digests. **MINOR-5.** |
| 7 | **seal windows** | **PRESENT** | 54 published fields forged after their gates closed and delivered at exit 0 under a total, self-consistent seal. **MAJOR-2.** |
| 8 | **VACUOUS / stamp clauses** | **PRESENT** | 3 vacuous constructs inside gate predicates, 2 typed booleans in a published object, 2 entailed gates. **MAJOR-4 / MINOR-4.** |
| 9 | **fabricable sweeps** | **ABSENT in the instrument** | every in-run census is a real loop (640×640 products, 640×16 plaquettes, 343 chains, 55 targets, 4 head-law probes, 18 gated instances). The paper's "all mutants dead" sentence is external-only. **MINOR-8.** |

---

## 2. THE INJECTION TABLE

Every injection ran the **plain delivery run** in its own pristine off-tree
sandbox rebuilt from `6d8582e`, with both artifacts present beforehand so
that "wrote nothing" is measurable. **15 ran live** — the five code-side ones
(INJ12–INJ16) twice each, in independent sandboxes, with identical outcomes
down to the bytes left on disk; 4 are marked
REPLICA-PREDICTED and were **not** run live — those come from an offline
re-implementation of the four paper gates which I validated against the
pristine paper and which agreed with **all eleven** live paper runs, 11/11.

| # | what / where | caught by | exit | wrote nothing |
|---|---|---|---|---|
| INJ01 | §6 spread table: `NON-COMMUTING` and `DEFECT-CARRYING` mass rows exchanged | **NOTHING** | **0** | no — both artifacts written |
| INJ02 | §4 census table: rows (c) and (d) exchanged (fibres 6↔2, measures NEW↔counting) | **NOTHING** | **0** | no — both artifacts written |
| INJ03 | §8: two Wilson expectation values exchanged | `G-PAPER-CLAIMS` | 1 | yes *(REPLICA-PREDICTED; the live patch mis-matched a line wrap)* |
| INJ04 | one digit of the backticked sha `c9edf97a5533` | `G-PAPER-NUMERAL-COVERAGE` | 1 | yes |
| INJ05 | the paper's two `paper-18` provenance digests exchanged (instrument ↔ receipt) | **NOTHING** | **0** | no — both artifacts written |
| INJ06 | the **clean** verdict fence duplicated verbatim | `G-PAPER-VERDICT-EQUALITY` | 1 | yes |
| INJ07 | a forged twin fence (`SPREAD-27/130`) beside the clean one | `G-PAPER-VERDICT-EQUALITY` | 1 | yes |
| INJ08 | §4.1 prose: "336 closed classes" → "208 closed classes" | **NOTHING** | **0** | no — both artifacts written |
| INJ09 | §2 prose: "16 sites" → "12 sites" | **NOTHING** | **0** | no — both artifacts written |
| INJ10 | "…follows an area law, and the string tension is the coefficient" planted in §8 | `G-MUST-NOT-VOCABULARY` | 1 | yes |
| INJ11 | the same, **line-wrapped and emphasised** (`**area\nlaw**`, "confining regime", "quark potential") — the exact form that defeated U4 | `G-MUST-NOT-VOCABULARY` | 1 | yes |
| INJ12 | 3 published fields on all 18 instance records edited **after** their `G-INSTANCE-*` and after `G-DECLARED-DYNAMICS-CENSUS` | **NOTHING** | **0** | no — receipt carries the forged values |
| INJ13 | a sealed object edited **after** `SEAL.take` (`wilson.range…maximum` → "9") | `G-PAPER-CLAIMS` (before `G-SEAL-INTEGRITY` could fire) | 1 | yes |
| INJ14 | the receipt corrupted **on disk** between `os.replace` and read-back (`"coins": 640`→`641`) | `G-ARTIFACT-INTEGRITY` | 1 | **no — both artifacts left promoted, receipt on disk carries `"coins": 641`** |
| INJ15 | an unstamped expectation-valued key planted at depth (`relativity.wilson_expectation_over_the_carrier`) | `G-WILSON-LICENCE` | 1 | yes |
| INJ16 | a real float literal (`_TOLERANCE = 1e-9`) planted in the instrument's source | `G-EXACT-ARITHMETIC-BY-AST` | 1 | yes |
| INJ17 | a verbatim anchor's needle made non-verbatim ("needs"→"requires") | `G-VERBATIM-ANCHORS` | 1 | yes *(REPLICA-PREDICTED)* |
| INJ18 | the paper misquotes its parent inside a blockquote ("needs a dynamics" → "needs a declared dynamics, and a carrier") | **NOTHING** | **0** | no *(REPLICA-PREDICTED)* |
| INJ19 | the paper **inverts** R5's definition it quotes ("the ordered product" → "the unordered sum") | **NOTHING** | **0** | no *(REPLICA-PREDICTED)* |

Six survivals. Two of them (INJ01, INJ02) are E-22 violations; two (INJ08,
INJ09) are load-bearing prose numbers; two (INJ18, INJ19) are misquotations
of the parents the whole inheritance apparatus exists to bind. INJ12 is the
seal window. INJ14 is the promotion order.

---

## 3. FINDINGS

### MAJOR-1 — E-22's "tables render as claims" is not satisfied; two row swaps and a misquote deliver at exit 0

**Measured.** `build_claims` renders 33 claims: 21 prose sentences and one per
Wilson expectation row. It renders **no table**. I mapped every claim
occurrence, the verdict fence and the four polarity fragments back onto the
paper's raw bytes, using a re-implementation of `mnorm` verified character-
identical to the instrument's own normaliser on the delivered paper:

- **350 numerals; 139 bound by a claim, the fence or a polarity fragment; 211
  bound by nothing but the coverage pool.**
- **All 24 cells of the §6 dynamics-relativity table**, every cell of the §4
  census table, and every numeral of the §1 pre-registered-outcome table are
  in the unbound 211.
- **0 of the paper's 12 quotations of its parents are bound.** The verbatim
  anchors gate the *parent's* bytes; nothing gates the paper's rendering of
  them. INJ19 shows the consequence: the paper can print "the holonomy is the
  **unordered sum** of the four link operators" as a blockquote attributed to
  R5, while `G-VERBATIM-ANCHORS` passes on the correct sentence in R5's own
  file.

The one table-shaped object the instrument *does* render — the twelve Wilson
rows — is exactly the one that is protected (INJ03).

**Repair R-K3-1 (liftable, same pattern as the Wilson loop already in the
file).** In `build_claims`, add one rendered claim per row of every delivered
table, built from the receipt and never typed:
- §6 — for each `S["relativity"]["rows"][i]`, the row as the paper writes it,
  over `set`, `configurations_COUNTING_ONLY`, and the four named
  `mass_by_declared_dynamics` columns, at occurrence count 1;
- §4 — for each family, `fibre_axis`, `fibre`, `irreducible`,
  `closed_classes`, `measure_name` from `census.instances` + `fibre.rows`;
- §1 — the five outcome rows from `preregistered_heads`.

**Repair R-K3-2 (the general form E-22 actually asks for).** Add
`G-PAPER-TABLES-AND-QUOTES-ARE-BOUND`: (a) every markdown table row carrying
a numeral must be covered by a rendered claim, so a table added later cannot
arrive unbound; (b) every `> ` blockquote line must be located inside one of
the 12 pinned verbatim windows. (b) closes INJ18/INJ19 outright.

### MAJOR-2 — the census seal window: 54 published fields forged after their gates, delivered at exit 0 under a total seal

`SEAL.take` is called at the end of the producing function and names the last
gate that function closed. For the largest published object the gap is
fifteen gates: the 18 instance records are gated at `G-INSTANCE-*` (#12–#29)
and `G-DECLARED-DYNAMICS-CENSUS` (#30), and sealed only at
`G-HEAD-DERIVED-TWICE` (#45), as part of `census`.

**INJ12, live.** Immediately after `G-DECLARED-DYNAMICS-CENSUS` closed I set,
on **all eighteen** records, `aperiodic_by_self_loop =
"EDITED-AFTER-ITS-GATE"`, `class_size_profile = [["FORGED", 1]]` and
`communicating_classes = 7`. The run **exited 0**. The delivered receipt
carries all 54 forged fields; all 57 gates passed; the gate chain is intact;
the seal manifest is total and **every one of the 29 seals recomputes**,
because the seal digested the edited object. This is precisely the failure
mode #119 was engraved against — "#234 satisfied at gate time, vacated at
delivery time" — relocated from delivery to the gap between the gate and the
seal.

Four more objects are digested after their named gate closed, two of them
before the object existed:

| object | named gate (#) | digested after gate | note |
|---|---|---|---|
| `census` (18 instance records) | 45 | 45 | records gated at #12–#30 — **15-gate window** |
| `ledger_shape` | 45 | 51 | did not exist when #45 closed |
| `mutants`, `falsifier_totals` | 48 | 50 | `S["mutants"]` assigned after #48; the gate evaluated a local `reg` |
| `paper_claims`, `paper_polarity` | 52 / 55 | 56 | assigned after #56 |
| `wilson` | 43 | 43 | the gate evaluated `rows` only; `range_over_the_invariant_simplex`, `distinct_values_over_the_carrier`, `normalisation_fibre`, `loop_families_grown`, `plaquettes_checked` are built after it and sealed under its name |

**Repair R-K3-3.** Seal each instance record at its own `G-INSTANCE-*`
(`SEAL.take("INSTANCE " + rec["instance"], …)`) and let `census` seal only
the aggregate fields; move the `mutants` / `falsifier_totals` /
`paper_claims` / `paper_polarity` / `ledger_shape` assignments **above** their
gates so the gate evaluates the object it vouches; fold the Wilson range into
`G-WILSON-LICENCE`'s predicate (or give it its own gate — MINOR-3) before
sealing it. A cheap standing guard: after the last gate, re-take a digest of
every sealed object and compare — one loop, and INJ12 dies.

### MAJOR-3 — a refusing `G-ARTIFACT-INTEGRITY` leaves both corrupted artifacts promoted

`seal_and_write` writes `p + ".tmp"` and `os.replace`s **both** artifacts into
place, and only then reads the receipt back and compares against the
gate-time seals. The gate is real and it fires — but by then the promotion
has happened.

**INJ14, live, in two independent sandboxes with byte-identical outcomes.**
Corrupting the receipt on disk between `os.replace` and the read-back: the
run refused at `G-ARTIFACT-INTEGRITY` with exit 1, and **both** sandboxes were
left holding `smu_receipt.json` containing `"coins": 641`
(sha `c7c4c7c0ca10`) and a replaced `smu_output.txt` (sha `3e4edb2f9aec`),
neither equal to the committed artifacts. No `.tmp` was left in either, so
there is no recovery path either. The unit's own standard — the pin's "failing runs write
nothing", and §10's "exits … 1 on any refusal, writing nothing" — is violated
at exactly the gate built for the disk boundary.

**Repair R-K3-4.** Invert the order: write **both** temporaries, run the
disk-vs-seal check **against the temporaries**, and `os.replace` both only
after it passes; on failure unlink the temporaries. Two moved lines, and the
disclosed exit convention becomes true without exception.

### MAJOR-4 — 15 of 42 falsifiers corrupt no object; 15 gates have none that does; 2 of those gates cannot fail on any object

Reading every one of the 42 branches:

- **27 of 42** corrupt a real object — including the two strongest forms in
  the corpus, `MUT-GHOST-FUNCTION` and `MUT-REGISTRY-EVASION`, which plant
  real text into the instrument's own source text.
- **8 of 42** assign a constant to the gate's own predicate variable:
  `MUT-VERBATIM` (`ok = False`), `MUT-WELD` (`same32 = False`),
  `MUT-MONOMIAL` (`carries = False`), `MUT-QUASI` (`agree = True`),
  `MUT-CARRIER` (`carrier_ok = False`), `MUT-SIMPLEX-DIM` (`ok = not ok`),
  `MUT-WILSON-GAUGE-INVARIANCE` (`gauge_inv = False`), `MUT-POLARITY`
  (`pol[0]["ok"] = False`).
- **7 of 42** fabricate a failure list or invert a counter without touching
  the object it counts: `MUT-AST-BLIND`, `MUT-CLAIM`, `MUT-COVERAGE`,
  `MUT-MUST-NOT`, `MUT-DIMENSION-THEOREM`, `MUT-SURJECTION`,
  `MUT-WILSON-OBSERVABLE`.

Fifteen gates therefore have no falsifier demonstrating object-detection
power. I supplied real objects for five and **all five bit**:
`G-EXACT-ARITHMETIC-BY-AST` (INJ16), `G-PAPER-NUMERAL-COVERAGE` (INJ04),
`G-MUST-NOT-VOCABULARY` (INJ10), `G-PAPER-CLAIMS` (INJ03),
`G-VERBATIM-ANCHORS` (INJ17). Ten remain undemonstrated by anything:
`G-CARRIER-…`, `G-GAUGE-WALK-CLASSES-…`, `G-GAUGE-WALK-SIMPLEX-…`,
`G-MONOMIAL-WALK-CARRIES-…`, `G-PAPER-POLARITY`, `G-PRICE-IS-CONSERVED`,
`G-QUASI-DERIVATION-ARM-…`, `G-SIMPLEX-DIMENSION-THEOREM`,
`G-WILSON-OBSERVABLE-IS-GAUGE-INVARIANT`, `G-WILSON-OBSERVABLE-REBUILT`.

**Two of them cannot fail on any object — proved from the ledger order:**

1. **`G-CARRIER-IS-THE-PARENTS-PRIMARY-CARRIER` (#5).** Predicate:
   `len(coins) == pv["PV-SLICE"] == pv["PV-FIXLOC"]`. `G-PATH-VALUE-ANCHORS`
   (#2) has already forced `PV-SLICE == 640` and `PV-FIXLOC == 640`, and
   `G-ARENA-REBUILT` (#4) has already forced `len(coins) == PV-COINS == 640`.
   The predicate is `640 == 640 == 640`. Only `carrier_ok = False` reaches it;
   an actual carrier corruption (`MUT-ARENA`) dies one gate earlier.
2. **`G-GAUGE-WALK-SIMPLEX-IS-THE-PARENTS-SIMPLEX` (#35).** Predicate:
   `simplex_dimension == PV-SIMP32/128`. `G-GAUGE-GROUP-REBUILT` (#8) forced
   `|O4| = 208`, `|O8| = 120`; `G-GAUGE-WALK-CLASSES-ARE-THE-PARENTS-ORBITS`
   (#34) forced the closed classes equal to those orbits **as sets**, so
   `simplex_dimension = len(closed) - 1` is 207/119; `G-PATH-VALUE-ANCHORS`
   forced `PV-SIMP32 = 207`, `PV-SIMP128 = 119`. The predicate is
   `207 == 207 and 119 == 119`. Only `ok = not ok` reaches it.

A third is half-vacuous: `G-IRREDUCIBILITY-IS-THE-CRITERION`'s second
conjunct `all(r["closed_classes"] == 1 for r in der)` is definitional —
`verdict == "DERIVES"` is *assigned* from `len(closed) == 1`. Its first
conjunct `len(der) == len(irr)` is substantive and is what
`MUT-IRREDUCIBILITY` falsifies, so the gate survives.

This is why §10's "0 are uncovered" reads better than the object it
describes: coverage there is defined over *falsifier-targeting*, not over
*falsifiability by an object*, so two gates that cannot fail count as fully
covered.

**Repair R-K3-5.** Per the paper-28 precedent (its seven constant-False
falsifiers were converted to object-corrupting ones, with a
`G-FALSIFIER-HONEST` gate re-verifying every description in-run), convert the
15. Per gate: `MUT-VERBATIM` should perturb the window *text*; `MUT-WELD`
should drop one element from one class of `cls32`; `MUT-MONOMIAL` should
remove one coin from `monoset`; `MUT-WILSON-GAUGE-INVARIANCE` should perturb
one `tb[i]` inside an orbit; `MUT-POLARITY` should plant a negator in the
scanned text; `MUT-DIMENSION-THEOREM` / `MUT-SURJECTION` should corrupt one
enumerated chain / one target rather than inverting `bad`;
`MUT-WILSON-OBSERVABLE` should perturb one `W` cell; `MUT-CLAIM` /
`MUT-COVERAGE` / `MUT-MUST-NOT` should corrupt `paper_text` (they already
operate on a copy).

**Repair R-K3-6.** Give the two entailed gates content independent of their
predecessors — compare the carrier **element-wise** against the parent's
fixed locus rather than by cardinality, and take the simplex dimension from
the kernel **rank** rather than from a class count already forced equal — or
retire them into the gates that carry the content and say so in the waiver
ledger.

---

## 4. MINOR FINDINGS

### MINOR-1 — `--quiet` silently changes the published artifacts at exit 0

`say()` gates `LOG.append` behind `if not QUIET`, so a **writing** delivery
run invoked with `--quiet` publishes a different `smu_output.txt` (3,492
bytes against the committed 5,622 — the 24-line provenance/arena/census
transcript gone, verdict only) and a different `smu_receipt.json`
(`transcript_head` `957bcc9e881b` instead of `deaabcc28161`), at **exit 0**,
with all 57 gates green including `G-ARTIFACT-INTEGRITY` — which cannot
notice, because it compares disk against what *this* run emitted. Measured
across two seeds: `transcript_head` is the **only** differing receipt key,
and the quiet form is itself byte-stable, so nothing else in the run changes. `USAGE` lists `--quiet` with no
note, and §10's "no flag is a no-op" says nothing about a flag that changes
the delivered bytes. This is a live byte-reproducibility hazard for any
battery that quiets its background runs.

**Repair R-K3-7 (two lines).** Move `LOG.append(msg)` outside the `if not
QUIET`, so `--quiet` suppresses the terminal echo only; or refuse
`--quiet` together with a writing run at exit 2.

### MINOR-2 — the elimination cap is published as a claim but no gate enforces it

`ELIMINATION_CAP = 208` is used at exactly one place (line 1556) — to *choose*
`ROUTE-CLASS` vs `ROUTE-LUMP`. No predicate compares `quotient_size` or
`largest_class_solved` against it, yet the fence publishes
`ELIMINATION-CAP=208-EVERY-EXACT-SOLVE-AT-OR-BELOW-IT`. Measured: the claim is
**true** — the twelve lumped solves are at 208 (eleven) and 4 (one), the six
class-route solves at 1, 4, 4, 8, 128, 128. **Repair:** add
`max(rec.get("quotient_size", 0), rec.get("largest_class_solved", 0)) <=
ELIMINATION_CAP` to the per-instance gate.

### MINOR-3 — the Wilson range is a headline with no gate, no falsifier and a typed flag

`range_over_the_invariant_simplex` is computed **after** `G-WILSON-LICENCE`
closes; no gate evaluates it and no mutant targets it. It carries
`"both_endpoints_are_extreme_points_of_the_simplex": True` as a **typed
constant** — with extremal orbits of size 3 it would still read true. §8's
headline ("covariance pins the expectation nowhere") rests on it. The
neighbouring `"derives_given_the_declared_dynamics": True` is likewise typed
on every row (the licence itself *is* properly enforced, by looking the
verdict up in the run's own census — so that one is misleading, not unsound).

Independently checked and consistent: the block trace runs 0…4 over the 208
orbits; both extremes sit on orbits of measured size 1; all 12 expectations
lie in [0,4]; solving three law-native rows for the sector means gives
DIAG = 2, ANTI = 1, BAL = 5/4, which then **predicts** the other three
law-native expectations and the counting expectation exactly.

**Repair:** gate the range (min/max equal to the extremes of `tb` over the
orbits; both attained on orbits of measured size 1; every published
expectation inside `[min, max]`), derive the extreme-point flag from the
measured orbit sizes, seal at that gate, and add one falsifier that perturbs
an orbit value.

### MINOR-4 — three vacuous clauses inside gate predicates

1. `per_dir_closed = all(True for _ in states)` (line 1263) is the constant
   `True` for any `states`, empty included. It sits in
   `G-CHART-128-ENLARGEMENT`'s predicate and is named for — and the gate's
   claim text describes — the direction-class-constancy property. The property
   *is* enforced, but by the `bad`/`continue` branch inside the closure loop,
   not by anything the gate reads. The gate's only real content is
   `len(states) > len(coins)`.
2. `free_with_fibre_one = [r for r in rows if r["fibre"] == 1 and
   r["status"].startswith("GENUINELY")]` (line 2565) is always empty: no
   inventory status begins "GENUINELY" (they are `FORCED`, `FORCED-BY-COST`,
   `DECLARED-AND-DISCLOSED`, `DECLARED-AND-SWEPT`). `not free_with_fibre_one`
   is a constant `True` inside `G-FIBRE-INVENTORY`.
3. `swept_ok` binds only rows with `isinstance(r["fibre"], int)` **and**
   `status == "DECLARED-AND-SWEPT"` — 5 of 11. The 4 typed rows
   (`THE-LATTICE-AND-ITS-SIZE`, `THE-COIN-FAMILY`, `THE-CARRIER`,
   `THE-ELIMINATION-CAP`: status, fibre and `instances_built` all hard-coded)
   and the 2 string-fibre rows (`WHICH-INVARIANT-TARGET` at fibre
   `THE-INVARIANT-SIMPLEX-ITSELF` with 3 instances; `WHICH-TARGET-THE-CONTROL`
   at `THE-WHOLE-SIMPLEX` with 1) are exempt. §10's "every declared dynamics
   axis is DECLARED-AND-SWEPT, with the number of instances built equal to the
   fibre at every one of them" is therefore gated **only on the rows where it
   is true**; the two rows where it is false are silently filtered out by a
   type test. (The paper is honest about the simplex-sized fibre elsewhere —
   §4.6, §7, §11 — so this is a gate/sentence mismatch, not a false claim.)
   **This is the answer to "can a failing row hide under a stamp?": yes — a
   mis-stated fibre on any of the six unbound rows is invisible, and
   `MUT-FIBRE` only touches `rows[-1]`, a bound one.**

**Repair:** delete (1); replace (2) with a real check or delete it; in (3)
evaluate every row and require a string-valued fibre to carry an explicit
`SWEEP-NOT-POSSIBLE` reason the gate reads, so the exemption is declared
rather than implied.

### MINOR-5 — the numeral licensing pool is polluted by sha256 fragments

The pool is 231 strings. Isolating contributions: `provenance` uniquely
licenses 16 numerals, the `verbatim_anchors` window digests 25, and
`code_sha256_12` 3 — **30 numerals whose only origin is a hash**
(`353385905`, `5533`, `7684`, `793`, `98`, `97`, `621`, `394`, `54`, `58`, …).
These are identifiers, not values the run computed. The `STRUCTURAL` blanket
over 0–27 is real but nearly redundant — only `17`, `21`, `22` are licensed
by it alone.

In practice the pollution is *not* the dominant hole: MAJOR-1 is, because a
row swap uses only legitimately computed values. But INJ05 — exchanging the
two `paper-18` digests in the paper's own inheritance sentence, so R5's
receipt digest is credited to R5's instrument and vice versa — **passed at
exit 0**, and hash fragments are part of why.

**Repair:** exclude digest-valued fields from `harvest`, and bind the paper's
inheritance digests as claims rendered from `SOURCES` — one
`("(`%s`)" % sha, 1)` per source.

### MINOR-6 — E-23 semantic honesty: two descriptions assert a corruption that does not occur

`G-FALSIFIER-DESCRIPTIONS-ARE-HONEST` checks that the published `plants`
token appears in the branch's own eight source lines. That is a *textual*
check, and two descriptions pass it while misdescribing the branch:

- `MUT-WILSON-OBSERVABLE` — "**plants a plaquette-dependent cell in the loop
  observable**". It plants no cell; it sets the *count* `dep = 1`. The
  observable is untouched.
- `MUT-CLAIM` — "**plants a rendered claim that the paper does not carry**".
  It plants no claim; it replaces the `miss` list with a fabricated record.
  The claim set and the paper are untouched.

Marginal, same shape: `MUT-MUST-NOT` ("plants a must-not vocabulary hit" —
plants a *hit*), `MUT-COVERAGE` ("plants an unmatched numeral" — plants an
*entry*). Twenty-seven descriptions are exact, and `MUT-AST-BLIND` is a model
of the honest form: it discloses both halves ("empties the float-literal list
**and** plants a banned import").

**Repair:** either make the four branches do what they say (R-K3-5), or
reword them to name the variable they set. The machine-checkable form of "a
falsifier corrupts an object" is: require the planted token to occur inside
an assignment whose target is **not** the gate's own predicate variable.

### MINOR-7 — the bare-copy abort is an unhandled traceback

`smu_exact.py` alone in an empty tree exits 1 and creates **no file at all**
(whole-directory listing compared before and after) — but through an uncaught
`FileNotFoundError` in `read_bytes`, so the disclosed "1 = a gate refused"
convention is satisfied by accident. **Repair:** wrap `load_sources` so a
missing pinned source fails `G-SOURCE-BYTES` with the path named.

### MINOR-8 — "42 declared mutants, all dead" is prose the delivery run cannot back

The Status block and §10 assert the sweep result; the receipt records
`declared_falsifiers: 42` and nothing about outcomes. The claim is **true** —
I ran all 42 out of harness as separate processes — but it is not
receipt-backed. **Repair:** publish a `mutant_sweep` receipt key written by an
actual `--all-mutants` execution, or mark the sentence as an external-battery
result the way the byte-identity sentence already is.

### MINOR-9 — eight inherited declaring exemptions are inert

Of the 12 `DECLARING` strings, 8 do not occur in this paper. They are whole
precise sentences, so they hide nothing today (the pool removes 207 of 40,078
characters — 0.5%), but they are latent exemptions carried from paper-23.
**Repair:** gate that every declaring string is located, or drop the ones that
are not.

---

## 5. WHAT HELD

**Anchors and consumers (row 1).** 9 file-bytes + 30 path-value + 12 verbatim
= 51, recounted from source and receipt. Every anchor row names a `consumer`,
every seal row names a `gate`; **all 71 names resolve — zero phantoms.** 16
distinct consumer gates, busiest `G-ARENA-REBUILT` (8).

**The seal as an object.** The manifest is TOTAL: 29 sealed + 14
declared-unsealed = 43 = every top-level receipt key, none uncovered, none
spurious. All 29 seal digests recompute exactly; the 57 chained gate digests
recompute exactly from `GENESIS` with no break, no duplicate id, every row
passed; `transcript_head`, `code_sha256_12` and `paper_sha256_12` recompute
against the delivered files; the `totals` block recomputes in all 10 fields.
`MUT-SEAL` (a genuine post-gate edit) dies on target; INJ15 dies at the
licence; INJ16 dies at the AST gate.

**E-22 fences and spans (row 4).** `blocks == [wsnorm(verdict)]` is *list*
equality — stronger than multiset. Duplicating the **clean** fence dies
(INJ06); a forged twin dies (INJ07). Inline code spans are genuinely inside
the coverage scan (`scan = paper_text`, nothing stripped): one corrupted digit
of a backticked sha dies (INJ04). Paper fence, output verdict line and
`receipt["verdict"]` are one 3,490-character string; `verdict_head` is its head
prefix and equals `census.head`.

**The confinement MUST_NOT sweep (row 8).** Tight. All 5 raw must-not hits in
the paper lie inside declaring sentences; the declaring pool removes 0.5% of
the text. Planting "an area law … and the string tension is the coefficient"
dies (INJ10). #125 normalisation holds under the wrapped-and-emphasised form.

**The conditional stamps (row 7).** Enforced per row, not per table: each of
the 12 rows names its dynamics, that dynamics' verdict is looked up in the
census *this run computed*, and the stamp is checked literally; then the whole
payload is walked to the bottom for any `wilson|expectation|loop_average|
loop_mean` key at any depth, and anything outside `/wilson` is fatal — INJ15
confirms. All 12 rows carry the stamp; `licensed_rows` = 12 = the number of
deriving instances.

**The lumping license (row 6) — sound, on three independent legs.** A wrong
lumping cannot pass, and the full-size verification is independent of the
lumped computation:
1. lumpability is *measured* block by block; a non-zero `fails` leaves
   `vectors` empty, which fails `verified_at_full_size`, which fails the
   per-instance gate;
2. the blocks are the orbits of a group **measured transitive on each block**,
   gated per instance;
3. the accepted vector is verified by `verify_stationary(P, v, n)` —
   `πP = π`, `Σπ = 1`, `π ≥ 0` — against the **original 640-state chain**,
   never against the quotient. The lumping only *proposes*.

Uniqueness likewise never comes from the quotient: `len(closed) == 1` from the
full chain's own support, read through an identity verified exhaustively on
343 three-state chains. Measured: 6 instances by `ROUTE-CLASS` (largest class
1, 4, 4, 8, 128, 128), 12 by `ROUTE-LUMP` (quotient 208 ×11, 4 ×1),
`lumpability_failures = 0` and transitivity true at every one.

**No fabricable sweep.** Every in-run census is a real loop: the 640×640
multiplication table entry by entry (278,528 of 409,600 staying, both anchored
to paper-23's receipt at named paths), 640×16 plaquette checks, 343
exhaustively enumerated three-state chains, 55 exhaustively enumerated
invariant targets (I re-derived the 55 from the declared denominator
independently), 4 head-law probes actually invoked, 18 instances each with its
own gate. `G-HEAD-LAW-REACHABILITY` runs the head law on synthetic tables
*inside* the delivery run, so a head law collapsed to a constant dies in-run.

**Comparator independence (#82).** `reconstruct_verdict` re-reads the
**serialized** receipt, derives the head by `second_head_law`, and re-renders
every segment. Of 67 string constants shared with `build_verdict`, 56 are
receipt key names — the addresses both must use — leaving 11: five separators,
three instance identifiers, `'NONE'`, and the two polarity words
`'FURTHER'`/`'LESS-FAR'`. `head_law` and `second_head_law` share exactly two
constants. This is not "the same concatenation written twice".

**The mutant machinery.** **42 of 42 dead on target**, run out of harness as
42 separate processes, with both artifacts byte-unchanged individually and
across the whole sweep. No gate predicate anywhere references `mut()` —
checked on the syntax tree over all 43 `LD.gate` call sites; 42 have literal
ids and the one computed id is the one the registered forcing
machine-checks. The registry is checked total against the AST in both
directions and a computed mutant name is fatal rather than forgiven.

**Byte reproduction (#91, row 11) — byte ×4 across four seeds.** Off-tree, in
git-less directory trees provisioned from `git show 6d8582e:`: the plain
delivery run reproduced **both committed artifacts byte-for-byte at
`PYTHONHASHSEED=0`, at `987654321`, at `1`, and at `random`** — four seeds,
eight files, every one identical to the committed bytes. Two further runs in
the `--quiet` form came out **identical to each other** across two seeds as
well. There is therefore **no hash-seed dependence anywhere in this unit**:
the v10-layer tie-break hazard (#160) does not bite, and the immunity is
measured rather than argued. The quiet pair differed from the committed bytes
only through MINOR-1, and only in `transcript_head`.

**CLI (row 10).** 20 hostile argv forms, every one **exit 2**: unknown long
flag, unknown short flag, bare positional, `--mutant` with no name (arity),
`--mutant BOGUS`, `--mutant` given a flag as its name, a bogus flag trailing a
valid `--mutant NAME`, the empty string, bogus flags trailing `--selftest`,
`--verify-paper` and `--help`, an extra positional after `--list-gates`, the
`--mutant=NAME` equals form, wrong case, and `--mutant MUT-SEAL --mutant`.
`--help`, `--list-gates`, `--list-mutants` exit 0 and are informational. The
inverted exit conventions are disclosed in three places — module docstring,
`USAGE`, receipt `exit_conventions` — and every one matches observed
behaviour. **The argv handler was read in source before any of this was run.**

**Write-nothing, verified independently of the instrument's own report.**
`--selftest` reports "FATAL AT EVERY ANCHOR CLASS … artifacts unchanged True";
I hashed **every file in the tree** before and after and the whole tree was
byte-identical — the claim confirmed by a route the instrument does not
control. `--no-write` and `--verify-paper` likewise left both artifacts
untouched. **No `.tmp` file was left anywhere by any of the 84 runs.**

**Bare copy (row 11).** `smu_exact.py` alone in an empty tree: exit 1, and a
whole-directory listing before and after shows **no file was created at all**.

**The 350-numeral three-way sweep (row 12).** Paper ↔ output ↔ receipt: the
paper's fence, the output's verdict line and `receipt["verdict"]` are the same
string; the 18 output census rows match the receipt at 4 fields each with 0
mismatches; all 44 distinct fence numerals trace to a receipt field; and 13
headline groups (6/18, 12/6, 10, 51, 9/30/12, 29, 42, 57+2, 52, 18, 23, 11/5,
34/16/0) match the receipt exactly. The receipt's own `paper_coverage`
figures — 350 numerals, 25 inline spans carrying a numeral, 2 fence markers —
reproduce under my independent scan.

**The disclosed own-check bug's residue (row 12).** Ledger #234 discloses
"one own-check bug corrected and disclosed" among ~22 pre-instrument
recomputations. Its residue, if any, would be a wrong delivered number. I
looked for siblings by recomputing the affected families from primitives
rather than by re-reading the worker's check: the four spread rows and both
widest spreads from the mass table; the counting column against `count/640`
at all four sets; the six law-native expectations and the counting expectation
from a three-parameter sector-mean solve using only three of them (four
predictions, four exact hits); the law-native measure's normalisation; the 55
exhaustive targets from the declared denominator. **No residue: 324
recomputations, zero mismatches, no number moved.**

---

## 6. THE SEAM RULING

The seam is **not** at the numbers. Everything I could reach independently
reproduced.

The seam is at the **paper as a text, and at the gap between a gate and its
seal**. The instrument's grip on its own prose is 33 rendered claims, one
fence, four polarity fragments and a 231-member numeral pool — total over the
fence and the sentences it renders, and *nil* over three tables and twelve
quotations. Its grip on its own receipt is a gate-time seal that, for the
largest published object, is taken fifteen gates after the values were
gated. Two row swaps, two prose numbers, two misquotations and 54 forged
receipt fields pass at exit 0 and are written to disk. **Nothing false is in
the delivered artifacts** — I checked all 350 numerals three ways and
recomputed 324 published quantities — but the machine that would catch it if
something were is absent for 211 numerals, 12 quotations and 54 fields.

Two things are *above* the era's standard: the registry is checked total
against the AST in both directions with computed mutant names fatal, and two
falsifiers plant real text into the instrument's own source. The licence is
enforced on the product at every depth. The lumping route — the one place a
reader might reasonably suspect a shortcut — is verified against the original
640-state chain and not against its own quotient.

**Ruling: the instrument is sound where it measures and blind where it
renders and where it seals late.** All four MAJORs are repairable inside
existing mechanisms — `build_claims` already renders one table correctly, the
falsifier conversions are one line each, the promotion order is two moved
lines, and the seal moves are local. None touches a measurement, a verdict
segment, or the head. The headline
`SMU-DYNAMICS-RELATIVE-SPREAD-153/380-OVER-12-DERIVING-INSTANCES` is
untouched by anything in this review.

## 7. WHAT I DID NOT DO

- I did not rebuild the 640-coin family, the chart/gauge actions, the
  holonomy or the 18 transition laws from the parents' definitions — that is
  K1's row; my Wilson cross-check reaches those numbers only through internal
  consistency.
- I did not rule on the surjection theorem, on whether the law-native family
  is motivated or declared, or on the paper-23 annotation question — K1 and
  K2's rows.
- Four injections (INJ03, INJ17, INJ18, INJ19) are marked REPLICA-PREDICTED
  and were **not** run live — the machine was carrying two sibling seats'
  batteries at load ~250 on 8 cores and each delivery run cost ~100 s of CPU.
  The replica agreed with the pristine paper and with all eleven live paper
  runs (11/11), but they are labelled so a reader can discount them. The two
  that matter most for MAJOR-1 (INJ18, INJ19, the misquotations) are also
  established structurally: `build_claims` renders no blockquote, and the
  verbatim anchors read the parents' files, never the paper.
- The `--no-write` and `--verify-paper` write-nothing checks were run with
  `--quiet`; that flag is irrelevant there because neither writes, and the
  byte-identity checks were run **without** it.

---

**Hashes re-verified at completion:** paper `d14689919289`, code
`394cbfca621c`, output `0bf6cc0502e6`, receipt `808aca088ff6`, pin
`a1fca5e7b238` — all unchanged. No repo object was modified by this review
except this file.
