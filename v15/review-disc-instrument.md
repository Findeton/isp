# DISC (paper-47) — K3 INSTRUMENT review

**Seat:** K3, instrument (the era audit: seal, coverage, injections, CLI, #91 at
its own hands). **Unit:** DISC, v15, paper-47. **Panel:** three seats.
**Standing:** between delivery and adjudication every headline below — the
unit's and this review's — is a **candidate reading**.

**Object, hash-verified at open and again at close (five, unchanged across the
whole audit):**

| object | sha256-12 open | sha256-12 close |
|---|---|---|
| `v15/paper-47-disc.md` | `b12c4c67bac8` | `b12c4c67bac8` |
| `v15/code/disc_exact.py` | `1d98d618c6bc` | `1d98d618c6bc` |
| `v15/code/disc_output.txt` | `dc79343de5d0` | `dc79343de5d0` |
| `v15/code/disc_receipt.json` | `c745ef39fded` | `c745ef39fded` |
| `v15/note-disc-pin.md` (pin) | `dbe7b26bb0d0` | `dbe7b26bb0d0` |

**Authority:** HANDOFF-PROMPT.md §4/§9; RUNBOOK.md §6 verdict vocabulary and the
engraving stack through E-33 (binding text `v14/tpl_runbook_addenda.md`
`e46c1abf25b2`); `v14/TEMPLATE.md` + `v14/code/era_template.py` (`d04a3eb58fbc`);
TPL-2's five registered items (`v15/PLAN.md:21`).

**Execution:** all runs off-tree, git-less, in `.../scratchpad/disc_k3/`
(1.1 G). Repo touched read-only except this file. Recomputations counted
honestly: **148** — 36-recipe sweep **36**, injection sandboxes **34**,
baseline/byte-identity **3**, hostile argv **13**, mode + tree-hash **5**,
independent move-proofs **9** (1 clean + 8 mutants), in-process verdict and
anchor proofs **4**, arithmetic re-derivations **44**.

**Injection roster: 34 designed, 14 survived at exit 0.** Twenty died — six at
`G-PAPER-CLAIMS`, two at `G-PAPER-REFERENTS`, two at `G-PAPER-WALLS`, one at
`T-NO-TYPED-COUNTS`, one at `T-READ-SET`, one at `T-SEAL-PROMOTION`, one at the
transcript read-back, and six more on the wrong leg or confounded and re-run.
The fourteen survivals are the substance of §3.

---

## GRADE: ACCEPT-WITH-FIXES

The measurement layer is sound and I could not move a number. Every figure I
re-derived independently came back exact; the run byte-reproduces off-tree and
git-less; the falsifier harness is real and I re-proved eight of its move-proofs
outside it with my own digest function.

The **vouching** layer is where this unit is weaker than it says. Four MAJORs,
two of them named recurrences of already-engraved diseases (RUNBOOK §13
addendum, v13 #313: *"A recurrence of an already-engraved disease is a MAJOR by
default and is named as a recurrence in the review"*). The unit's central
methodological claim — *S-1 by construction* — does not hold at either of the
two places it is asserted: the verdict comparator is the builder, and the
disjointness gate is defeated by a one-line alias.

No finding below moves a delivered number. All are repairable in place and each
carries an exact liftable repair.

---

## 1. WHAT PASSED, MEASURED

| battery | result |
|---|---|
| plain run, off-tree, git-less, artifact-deleted tree, seed A, `--run` | exit 0, 36/36 PASS |
| same, seed B, independent tree | exit 0, byte-identical to A |
| both vs committed artifacts | `disc_output.txt` `dc79343de5d0`, `disc_receipt.json` `c745ef39fded` — **reproduce the delivered digests exactly** |
| hostile argv, 13 forms (`--RUN`, `--Run`, `--run=`, `--run --no-write`, empty, `-h`, `--help`, `--mutant`, `--mutant NOPE`, `--mutant MUT-S1 extra`, `--selftest --run`, `--verify-paper`, `--render extra`) | **13/13 exit 2** |
| `--selftest` | exit 0; three legs fatal (forged transcript row → `T-TRANSCRIPT-BOUND`; post-seal add → `T-SEAL-PROMOTION`; sealed value edit → `T-SEAL-PROMOTION`) |
| `--selftest` writes nothing, by **whole-tree sha256** over 380 files | tree `f7d0b539fab01480` identical before and after |
| `--no-write`, `--render`, `--list-gates`, `--list-mutants` write nothing, same tree hash | **4/4 unchanged** |
| full 36-recipe sweep, **out of harness, one process each**, in a pristine tree | **36/36** died at the declared gate, target moved, hook used; **36/36 artifacts unchanged**; **0 anomalies** on `declared == died ∧ moved ∧ hook_used` |
| independent move-proof re-derivation (my own sha512-16 digest, my own bookkeeping, `run_mutant` not called) on 8 recipes spanning 8 families | **8/8** re-proved: died-at == declared, target moved, hook used |

**Counts, every one verified from the live registries, not from the paper:**

| quantity | claimed | measured | source of truth |
|---|---|---|---|
| gates | 36 | **36** | `--list-gates` 36 ∥ transcript rows 36 ∥ `receipt.transcript.gate_rows` 36 ∥ selftest "36 gates" |
| recipes | 36 | **36** | `--list-mutants` |
| sealed keys | 36 | **36** | `seal_manifest.sealed` |
| declared-unsealed | 3 | **3** | `paper`, `rendered`, `seal_manifest`, each with a reason |
| receipt top-level keys | — | **39 = 36 + 3** | totality is total, recomputed at the door |
| anchors | 12 | **12** located, **12** consumed, 10 distinct consumer gates | `anchors_located` / `anchors_consumed` |
| S-1 regions | 5/16/8 | **5/16/8** (29 prefixed functions) | AST region map |
| walls / legs | 3 / — | **3 walls, 25 legs** (9+2, 4+1, 6+3) | `walls` |
| reads | — | **13 reads, 8 distinct** | `reads` |
| paper surface | — | **92 rows, 18 prose claims, 1 fence, 337 numerals scanned** | `paper_claims` / `paper_coverage` |
| measured names | **56** | **57 (receipt) / 58 (transcript)** — see MINOR-1 | `typed_counts.measured_names` vs the ledger evidence string |

**Physics spot-check, re-derived from the paper's own site tables by hand
(K1's territory, but it bears on whether the instrument's numbers are real):**
both §6 distributions sum to 1 exactly (19683/19683 and 59049/59049); the
displaced probability sums to zero on both planes (−512−512+1024 = 0;
+6144+2000−10144+2000 = 0); TV = ½Σ|Δ| gives **1024/19683** and **10144/59049**,
matching the paper; and the shot counts are exactly ⌈100/δ²⌉ — **36948** and
**3389** — matching §11. Nothing moved.

---

## 2. TEMPLATE CONFORMANCE, PER FAMILY

Adoption is **used, not copied**, and I verified that rather than accepting it:
`disc_exact.py:68` imports `era_template` and calls **19** of its names
(`Anchor AnchorSet CheckFail Claims CountRegistry FAMILIES Falsifier
FalsifierHarness Ledger ReadSet ReferentRegistry Seal SemanticWall Transcript
bytes_digest canon digest promote require_object`), covering the class of every
one of the nine families. **No family is carried unused** — each of the nine
CHECK ids is reachable on the delivery path as a live gate or enforcement.

| # | family / check | verdict | leg probed, and what it did |
|---|---|---|---|
| a | SEAL-INTEGRITY / `T-SEAL-PROMOTION` | **PRESENT** | post-seal add, sealed-value edit and post-promotion transcript edit all die; totality recomputed from the live key set at the door; partition constrained. NOTE-1 on the receipt's post-promotion window. |
| b | TRANSCRIPT-BOUND / `T-TRANSCRIPT-BOUND` | **PRESENT** | forged row dies; ledger chained; whole transcript digested and compared with the promoted bytes, with rollback. E-26 records this family as having *no closed instance in any of thirty-nine instruments* — DISC closes it. It then leaves the closing gate itself unfalsified (MAJOR-5) and publishes one of its counts twice over (MINOR-1). |
| c | SEMANTIC-WALLS / `T-WALL-SEMANTIC` | **PRESENT, under-controlled** | I wrote two paraphrases of the banned ablation-as-prediction reading in a paper's voice, sharing no pattern with the wall; **both died at `G-PAPER-WALLS`**. So the wall bites. But 2 of the 3 walls carry no control in either leg (MINOR-4). |
| d | VERBATIM-ANCHORS-CONSUMED / `T-ANCHOR-CONSUMED` | **PRESENT, partial** | phantom consumer dies (`MUT-CONSUMER`), needle located in parent and paper, occurrence exactly one. **8 of 12** anchors extract a value into a predicate; **4 are tautologies** (MINOR-2). |
| e | CLAIMS-BY-EQUALITY / `T-CLAIMS-EQUAL` | **PRESENT, strong** | six injections, six deaths: cross-table header swap, row transplant between the two same-header site tables, twin verdict-fence forgery, a TV fraction altered, `MODEL-ABLATION-BENCHMARK` deleted from the head, `7`→`3` inside the head fence, and one census ruling flipped in-table. Keyed by table; headers are rows; fences by multiset. |
| f | REFERENT-BINDING / `T-REFERENT-BOUND` | **PRESENT, but 1.6 % of its surface** | the cross-universe plant *"294 of 372 fiber points"* dies correctly. But only **3 of 182 prose numerals** are in scope (MAJOR-1). |
| g | NO-TYPED-COUNTS / `T-NO-TYPED-COUNTS` | **PRESENT, partial** | the TPL-2 **%-format** subspecies is caught at the statement door. The TPL-2 **integer-offset** subspecies is **not** (MINOR-3). |
| h | FALSIFIERS-POISON / `T-FALSIFIER-POISONS` | **PRESENT, strong** | move-proofs are genuine: digest-before/after on the *sealed* object, death required **at** the declared gate, plus a `hook_used` check that kills an unreferenced recipe. 36/36 in-harness, 8/8 re-proved out of harness. Tail exemption at MAJOR-5. |
| i | READ-SETS / `T-READ-SET` | **PRESENT, tail window** | audit hook unbypassable — an unpinned read of `v15/LOG.md` placed before the gate dies at `T-READ-SET`. The gate fires third-from-last (MINOR-5). |

---

## 3. FINDINGS

### MAJOR-1 — the paper's primary headline is bound by nothing. Five inversions delivered at exit 0. *(recurrence of E-30, the SPC disease, verbatim)*

E-30's own citation: *"at SPC … the §4 headline contrast inverted from 2-of-30
to 30-of-30 and **CARRIED THROUGH A FULL DELIVERY** at 46/46 gates passed with
the corrupted paper's digest sealed into the receipt."* That is what happens
here.

| injection | edit | result |
|---|---|---|
| `FLIP-TITLE` | the §-head, *"**Seven** of the Ten Tested Results Are Reproduced Exactly"* → *"**Three** …"* | **exit 0, 36/36 PASS** |
| `FLIP-S1` | §1 *"**Seven** of the ten rows … come back exactly"* → *"**Three** …"* | **exit 0** |
| `FLIP-SEVEN` | §2 *"**Seven** rulings of reproduction"* → *"**Three** …"* | **exit 0** |
| `FLIP-S12` | §12 *"**Seven** of the ten tested results are reproduced exactly"* → *"**Three** …"* | **exit 0** |
| `FIVE-STRUCTURES` | §7 *"**Five** structures, **zero** adjustable numbers"* → *"**Nine** structures, **four** adjustable numbers"* | **exit 0** |

`FLIP-TITLE` re-run with `--run`: both artifacts written; the receipt seals the
corrupted paper at `e275be03304b`; the receipt's own `q155_census` still reads
`reproduced: 7`; `disc_output.txt` is **byte-identical** (`dc79343de5d0`) to the
clean run. The two published artifacts contradict the paper's headline and the
transcript carries no signal at all.

**Mechanism, measured.** `G-PAPER-COVERAGE` asks only *is this numeral some
value the run measured* — and `three`, `nine`, `four` all are, elsewhere.
`G-PAPER-REFERENTS` is the mechanism that would bind a numeral to *its own
sentence's* universe, but its universes declare the nouns `sealed result`,
`census row`, `fiber point`, `declared observable`, `declared modulus`,
`covariant coin`, `link coin` — and **none of the sentences that state this
unit's headline uses any of them**. They say *rulings*, *rows this unit put to
the null*, *tested results*, *structures*. Result: **3 of 182 prose numerals
are checked**; 179 are free.

**Repair (liftable).** Add to `RR.universe("the census", …)` the nouns the paper
actually uses — `"ruling"`, `"rulings"`, `"tested result"`, `"tested results"`,
`"row this unit put to the null"`, `"rows this unit put to the null"` — and
declare a `"the price"` universe with nouns `"structure"`, `"structures"`,
`"adjustable number"`, `"adjustable numbers"`, values `{5, 0}` and pair
`(0, 5)`. Then add a standing gate that the count of prose occurrences the
referent gate resolves is ≥ a floor computed from the paper's own noun
inventory, so the coverage of this family can never silently fall back to 3.
Re-run the five injections above as declared recipes.

### MAJOR-2 — `G-VERDICT-EQUALITY` compares `f(R)` with `f(R)`. *(recurrence of S-1, TEMPLATE.md §11's first-named shape, in the unit that claims S-1 by construction)*

`disc_exact.py:2317-2331`:

```
head = k_rebuild_head(R)
...
R["verdict"] = {"head": head}
SEAL.seal("verdict", R["verdict"], "G-VERDICT-EQUALITY")
rebuilt = k_rebuild_head(R)
gate("G-VERDICT-EQUALITY", REG.stmt("the delivered head and an independent
     reconstruction over the receipt payload are compared for string
     equality, so a stale head cannot be delivered"), head == rebuilt, …)
```

The head is **built by the comparator** and then "independently reconstructed"
by the same function, on the same payload, eight lines later. I proved by AST
that `k_rebuild_head` never reads `payload["verdict"]` — the only key that
changes between the two calls — so `head == rebuilt` is an **algebraic
identity**, true for every input.

Demonstrated in-process: with the payload corrupted (`reproduced` 7→3,
`structures` 5→9) the head reads
`PRIMARY=…REPRODUCES-3-OF-10-TESTED-RESULTS` and
`PRICE=ISP-CARRIES-9-STRUCTURES…`, and the gate's predicate `head == rebuilt`
is **still `True`**. The corruption was caught downstream by the paper's fence
multiset, not by the comparator; an author regenerating the paper alongside the
code removes even that.

TEMPLATE.md §11 names this shape first and cites it verbatim: *"The 'rebuild'
is the same function on the same payload."* The paper asserts the opposite in
two places — §"S-1 by construction" and the head paragraph's *"compared for
equality against an independent reconstruction … re-renders every segment with
its own format strings"*.

Second defect in the same function: the segment
`REPRODUCED=PERIMETER-LAW+CLOSED-FORM+GAP+PLAQUETTE+QUARTIC-SIGN+COIN-REGISTER-RESTRICTION+THE-FIRST-TWO-TICKS`
is a **typed literal**. With `reproduced` forced to 3 the head still lists seven
names — the head can publish an internally contradictory verdict and the
comparator agrees with itself. (E-31: head segments interpolate from the live
registry.)

**Repair.** Build the head from the payload in the *builder's* region under its
own name, and let `k_rebuild_head` be the only comparator — one function must
not do both. Derive the `REPRODUCED=` name list from
`q155_census["rows"]` by filtering on `ruling == "REPRODUCED"` and joining the
row keys, so it moves when a ruling moves. Add a recipe that corrupts a payload
value the head renders *after* that value's own gate, and require
`G-VERDICT-EQUALITY` — not the seal, not the fence gate — to be the gate that
dies.

### MAJOR-3 — `G-S1-DISJOINT-CODE` is a name check, and three ways past it pass

The predicate classifies functions by the prefixes `n_`/`i_`/`k_` and flags two
edges only: `k→n|i` and `n→i`. Three injections, all at exit 0, all with the
gate's own evidence unchanged at `regions 5/16/8 offences none`:

| injection | edit | result |
|---|---|---|
| `S1-ALIAS-CALL` | `_NULLSTEP = n_step_ring` at module level; the comparator `k_agreement_checks` **calls `_NULLSTEP(...)`** | **exit 0, offences none** — the callee name is not in the region map, so `cpre is None → continue` |
| `S1-SHARED-HELPER` | a helper `shared_kernel` outside the prefix scheme, called by **both** `n_step_ring` and `k_first_difference` | **exit 0, offences none** — S-2 ("two routes through one shared component") walks straight through S-1's own gate |
| `S1-ISP-READS-NULL` | `i_coin_apply` calls `n_step_ring` — *the ISP arm reading the null's state* | **exit 0, offences none** — the `i→n` edge is **not an offence by the predicate at all** |

The paper's opening sentence, *"Three code regions are disjoint by machine
check"*, is stronger than what is checked. Its next sentence is accurate about
the two edges, which makes the first sentence the one to fix.

**Repair.** Resolve callees through the module's own binding table (walk
`ast.Assign` for aliases and compare against the region map's *objects*, not its
names); make **every** cross-region edge an offence including `i→n`, or state
the asymmetry in the paper; and add a *fourth* class for functions in no region
that are called from more than one region, which is the shared-component
offence. Ship all three injections above as recipes.

### MAJOR-4 — the pre-registration is re-declarable post-hoc at exit 0

`G-NULL-RULE-TOTAL` binds the **cardinality** of `NULL_RULE` (7), the two dropped
structure names (read from the pin anchor), the spatial dimension (read from the
pin), and `len(shared)` where `shared` is a **typed list** in the source. It
binds **no rule's text**.

| injection | edit | result |
|---|---|---|
| `PR3-POST-HOC-B` | PR3 rewritten from *"the null carries the **SAME** coin … the discriminator may not be won by changing the coin"* to *"the null carries a coin of its **OWN** choosing, picked after the sweep from whichever member of the census makes the comparison come out; the coin is tuned to the result"*, in code **and** paper | **exit 0**, `G-NULL-RULE-TOTAL :: rules 7 shared 6 … missing none` |
| `PR7-SWAP` | datum word `MEASURE` → `TUNING`; text replaced with an explicit admission of post-hoc tuning | **exit 0** |

In the `PR3` run the head still publishes
`SHARED-WITH-ISP=ARENA-REGISTER-**COIN**-SHIFT-STATE-HORIZON` while PR3 now says
the null picks its own coin after the sweep — because `shared` is typed, not
derived from the rule table. The unit's anti-strawman guarantee, which §3 calls
*"the reading to hold on to"*, is carried by prose alone.

**Repair.** Anchor the seven rules to the pin: either move PR1–PR7 verbatim into
`v15/note-disc-pin.md` (which is already hash-pinned at `dbe7b26bb0d0` and
already read through the anchor accessor) and gate each rule's text against the
pinned bytes, or add a `SOURCES`-style digest over `NULL_RULE` frozen in the
pin. Derive `shared` from `NULL_RULE` by rule id instead of typing it. Add a
recipe that rewrites one rule's text and requires `G-NULL-RULE-TOTAL` to die.

### MAJOR-5 — one gate has neither falsifier nor waiver, and is invisible to the coverage gate

Measured from the live registries:

- ledger gates **36**; recipes **36**; distinct gate names targeted **34**, of
  which one (`T-SEAL-PROMOTION`) is a seal check and not a ledger gate.
- ledger gates with no recipe: `G-READS-DECLARED` (waived, forced),
  `G-SCOPE-DECLARED` (waived, forced), and **`G-TRANSCRIPT-BOUND` — neither**.
- `T-FALSIFIER-COVERAGE` reports `gates 34 falsified 34 waived 2`. Its
  denominator is `set(ledger.names()) | {itself}` taken *at call time* = 34.
  **Two gates fire after it** — `G-TEMPLATE-ADOPTED` and `G-TRANSCRIPT-BOUND` —
  and are outside the denominator by ordering alone.

E-32 closes the self-exemption (the coverage gate does count itself, correctly);
the *tail* exemption survives. The uncovered gate is `G-TRANSCRIPT-BOUND` — the
family-(b) gate, i.e. precisely the mechanism E-26 records as having **no closed
instance anywhere in thirty-nine instruments**. The unit's one novel family
implementation is the one gate nothing falsifies.

The two published gate totals also disagree: `36` (transcript, `--list-gates`,
`receipt.transcript.gate_rows`) and `34` (coverage denominator), against E-26's
*"the row count, the gate count, the `--list-gates` output and any published
total are ONE number, computed after the last gate."*

**Repair.** Move `T-FALSIFIER-COVERAGE` to last, or have it take its denominator
from the declared gate list rather than from what has fired. Add a recipe for
`G-TRANSCRIPT-BOUND` (a dropped ledger row, or a reordered one, which its chain
should catch), or a waiver with a machine-checked forcing.

### MINOR-1 — the same quantity is published as 57 in the receipt and 58 in the transcript *(E-26)*

`disc_exact.py:2658-2670`. `R["typed_counts"]["measured_names"] = len(REG.values)`
is taken and **sealed** at 57; the next line registers `measured_names` itself,
raising the registry to 58; the evidence string then re-reads
`len(REG.values)` = 58. Sealed receipt **57**, gate statement **57**, transcript
evidence **58**. E-26's cited disease is exactly this shape (*"the transcript
read `unique 99` where the receipt read `unique 45`"*), here on a
self-referential count rather than a headline. Neither number is the **56** the
delivery summary claims.

**Repair.** Register `measured_names` **before** building the payload dict, and
interpolate the evidence from `REG.values["measured_names"]` rather than
re-reading `len(REG.values)`.

### MINOR-2 — 4 of the 12 anchors are consumed by a tautology *(E-28 obligation 6)*

Eight anchors take a value into a predicate: `d=2` from the pin, `Z_3`→3,
`n mod 3`, `m = 2` twice, `gap 1/2`, `11` and `13/10`, and the exponent `fourth`.
Four are `phrase in canon(anchor_text)` where the phrase is a **substring of the
needle itself**, so the predicate is `True` for every input:

| anchor | predicate | needle contains it |
|---|---|---|
| `A-COUP-FROZEN` | `"counts that never update" in canon(a_frozen)` | yes, by construction |
| `A-POT-PERIMETER` | `"takes the same value" in canon(a_per)` | yes |
| `A-ACT-QUARTIC` | `"single value zero" in canon(a_q1)` | yes |
| `A-PIN-EXPRESSIBILITY` | `all(w in canon(a_expr) for w in ("MEASURABLE","DEFINITIONAL"))` | yes |

The paper's §13 says each anchor is *"consumed for its content"* and then names
six value consumptions — accurate for those six, and eight in total; the
blanket "each" over-reads. This is also RUNBOOK §14 addendum v13 #219 ("an
object compared against a copy of itself … verifies nothing").

**Repair.** Re-class the four as `EXISTENCE-ONLY` in the receipt and in §13, or
give each a real value predicate (e.g. take the *count* of shared attributes out
of `A-COUP-FROZEN`'s sentence and compare it with the control's measured record
state, which the run already has).

### MINOR-3 — the TPL-2 integer-offset typed-count subspecies is ungated

| injection | result |
|---|---|
| `%`-format: `REG.stmt("… over all %d receipt keys" % 39)` | **dies at `T-NO-TYPED-COUNTS`** ✔ |
| integer offset: `REG.measured("wall_extra", len(WALLS) - 3 + 7, "a typed integer offset")`, published as `{wall_extra}` in the `G-PAPER-WALLS` statement | **exit 0** |
| integer offset on a live name: `REG.measured("record_words", len(record_vocab) - 7 + 12, …)` | **exit 0**; the statement publishes *"any of the 12 declared record words"* while the evidence reads `record words 7` and the truth is 7 |

`CountRegistry.measured` accepts any value with a non-empty provenance string,
and the AST leg inspects only string constants handed to `stmt`/`gate`/`claim`.
Neither sees arithmetic at the registry door. TPL-2 item 2 is therefore half
implemented, against the docstring's *"no %-format or integer-offset typed
counts"*.

Realized harm is bounded because gate **statements never reach either artifact**
(NOTE-2). Repair: extend the AST leg to flag any `ast.BinOp` with an
`ast.Constant` int operand in an argument to `REG.measured`, mirroring
`contract_exact.py`'s `audit_typed_deep`.

### MINOR-4 — 2 of 3 walls have no control in either leg, and the source says otherwise

`disc_exact.py:1087-1089` states: *"each control below was written before the
pattern it exercises (TPL-2: wall controls written independently)."* There are
no controls below — `ET.SemanticWall` takes no `controls` argument and the
receipt's `walls` key carries only `negative`, `positive`, `licences`. The whole
control surface is two recipes, and **both exercise wall #1**:
`MUT-WALL` plants a sentence matching two negative patterns of
`W-NO-EXHAUSTIVE-NULL-CLASS`, and `MUT-WALL-POSITIVE` deletes that same wall's
standing sentence. `W-PARAMETER-FREE-IS-RELATIVE` and
`W-ABLATION-NOT-PREDICTION` are never exercised in either leg.

To the unit's credit this is a documentation and coverage defect, not a dead
wall: I wrote two `W-ABLATION-NOT-PREDICTION` paraphrases from the disease
rather than from the pattern and **both died at `G-PAPER-WALLS`**. But when I
deleted that wall's three standing sentences, the run died at `G-PAPER-CLAIMS`
— the **wrong leg** (LOR #269: *"a kill on the wrong leg is not evidence"*), so
its positive leg remains undemonstrated.

**Repair.** Add per-wall `controls` (negative and positive) to the local wall
object as `arity_exact.py:614` and `autoglue_exact.py:499` already do, gate that
every control is caught, and correct or delete the source comment. Order the
positive-leg recipe so the wall gate is reached before the claims gate, or
delete a wall sentence that no rendering claims.

### MINOR-5 — the read-set gate fires third-from-last; the tail window is open *(E-33)*

`G-READS-DECLARED` is gate 33 of 36. An unpinned read of `v14/PLAN.md` inserted
**after** it (`READ-AFTER-GATE-CLEAN`, touching no payload key) runs at **exit
0**. The same read placed **before** the gate dies at `T-READ-SET`, so the audit
hook itself is sound — only the ordering is wrong. E-33: *"compared … at the
LAST gate, not the first."*

**Repair.** Move `G-READS-DECLARED` after `G-TRANSCRIPT-BOUND`, or re-check the
read log at close.

### MINOR-6 — the CLI's own self-description is false *(E-23 third leg)*

The usage text printed on a bad argv (`disc_exact.py:3004`) reads: *"`--render`
and `--list-gates` are PARTIAL modes: they return before the paper gates."*
Both call `full_run` in full. `--list-gates` prints **36** names including
`G-PAPER-CLAIMS`, `G-PAPER-REFERENTS`, `G-PAPER-WALLS`, `G-PAPER-COVERAGE` and
both closing gates; `PARTIAL` is only a dict holding the payload for the mutant
harness. The error is conservative — it understates coverage — but it invites a
reviewer to skip verifying two modes.

**Repair.** Delete the sentence.

### NOTE-1 — receipt vs transcript post-promotion asymmetry

`main()` re-reads the promoted **transcript**, compares it with the gate-time
seal and **rolls back** on mismatch; the injection `SEAL-POSTCLOSE-OUT` proves
this fires. The **receipt** gets only `ET.promote`'s internal
`verify_after_promotion`, so an edit landing after `full_run` returns
(`SEAL-POSTCLOSE-DISK`, which set `q155_census.reproduced` to 3) ships at exit 0
with the receipt's own manifest publishing `4d69cff9fc20` beside the changed
value — the SEC-2 shape E-25 cites. This is graded NOTE, not MAJOR: the probe
requires code in the delivery path, and the window exists in every instrument.
Worth recording because DISC **closed** the side-artifact window that HOR
registered as an open TPL-2 charge, and closed it for the transcript only.
Repair: mirror the transcript's read-back-and-rollback for the receipt.

### NOTE-2 — gate statements reach neither artifact

The receipt carries no ledger and no statements; the transcript prints only
`[PASS] GATE :: evidence`. The `statement` field — the surface E-31 polices and
on which E-32's descriptions live — is unpublished. This is TEMPLATE.md §11's
registered extension *"the closing gates' verdicts appear in neither artifact"*
and it bounds MINOR-3's harm. Consider publishing statements as a sealed key.

### NOTE-3 — `G-TEMPLATE-ADOPTED` resolves names, it does not prove exercise

The gate checks that the nine CHECK ids resolve to `era_template` classes. TPL-2
item 5 ("carried-not-used families forbidden") is not gated by it. I verified
by hand that all nine **are** exercised, so conformance holds in fact; the gate
that vouches it is weaker than the claim. `arity_exact.py` gates this natively
as `G-TEMPLATE-EXERCISED`; lifting that is a one-line repair.

### NOTE-4 — environment hazard during this audit

My first 36-recipe sweep was terminated mid-run by a **concurrent session** in
this repo issuing `pkill -f "sweep.sh"` while working on `autoglue_exact.py`.
I restarted under a non-colliding name and re-verified all five object digests
immediately afterward — unchanged. Flagging for the orchestrator: concurrent
workers are using broad `pkill` patterns that reach other seats' processes.

---

## 4. WHAT I COULD NOT BREAK

Recorded so the adjudicator can price the walls that held: the coin census, the
parent-fidelity ladders, the discriminant values, the modulus descent and the
five lattice legs all resisted every recipe and every probe, and their numbers
re-derive exactly by hand. The claims family (e) took six independently designed
forgeries and killed all six. The falsifier harness's move-proofs are the real
thing — digest-on-the-sealed-object, death-at-the-declared-gate, and a
`hook_used` check that no sentinel survives — and eight of them re-prove outside
the harness with a different digest function. The seal's totality is recomputed
at the door and the partition is genuinely constrained. The argv contract is
clean at 13/13. The self-test writes nothing, proved by tree hash rather than by
its own report.

The unit also self-found and repaired a defective recipe before delivery
(`MUT-WALL-POSITIVE`, case sensitivity) and says so in the source. That is the
behaviour the era wants.

---

## 5. REPAIR ORDER, SUGGESTED PRIORITY

1. **MAJOR-1** — extend the referent universes to the paper's own nouns; add a
   coverage floor for the family; ship the five headline flips as recipes.
2. **MAJOR-2** — separate builder from comparator; derive the `REPRODUCED=`
   list; add a payload-corruption recipe that must die at `G-VERDICT-EQUALITY`.
3. **MAJOR-3** — resolve aliases and shared helpers; decide and gate the `i→n`
   edge; ship the three S-1 injections as recipes.
4. **MAJOR-4** — anchor PR1–PR7 to the pin; derive `shared` from `NULL_RULE`.
5. **MAJOR-5** — re-order or re-base the coverage denominator; cover
   `G-TRANSCRIPT-BOUND`; publish one gate count.
6. **MINOR-1…6** and **NOTE-1…3** as written above.

None of these requires a re-measurement. If the repairs are applied, I expect
every delivered number in `disc_output.txt` and `disc_receipt.json` to be
byte-identical, and the paper to change only where MAJOR-1 and MINOR-2 touch its
sentences.

---

*Between delivery and adjudication every headline in the unit under review, and
every verdict in this review, is a candidate reading.*
