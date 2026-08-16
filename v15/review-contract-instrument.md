# K3 INSTRUMENT — THEORY-CONTRACT (paper-43), hostile review

**Seat.** K3, the instrument seat, of the three-seat panel on v15 unit 1.
**Object, verified at open AND at close (unchanged across the review):**

| object | sha256-12 |
|---|---|
| `v15/paper-43-contract.md` | `a0caabea6566` |
| `v15/code/contract_exact.py` | `d7f4c15e7704` |
| `v15/code/contract_output.txt` | `2f1933c09b8f` |
| `v15/code/contract_receipt.json` | `9b3638b796ae` |
| `v15/note-contract-pin.md` | `438586c11db5` |

All sixteen pinned sources recomputed live and matched. Execution was
scratch-only, at absolute paths, under
`.../scratchpad/contract_k3/` (35 MB peak). This review file is the seat's
only repository write.

## GRADE: ACCEPT-WITH-FIXES (AWF)

**Every measured number I could reach reproduces, and the four verdict words
stand. What does not stand is the instrument's own account of why they should
be believed.** Twenty-one live injections were run, one process each, off-tree
and git-less; **twelve survived at exit 0**, including two that put an inverted
headline into the delivered artifacts. Nine of the eleven surviving classes are
failures of a guarantee the paper states in its own words. No false physics
number is published in the pristine run; one false *bookkeeping* number is
(`receipt_leaves = 0`, MAJOR-8).

Between delivery and adjudication this grade and every finding below is a
**candidate reading**.

---

## 1. WHAT HOLDS (verified, not taken on trust)

These are strengths, established by measurement, and they are substantial.

- **The full 34-recipe sweep, out of harness, one process each.** All 34
  mutants died at their named gate (`rc=1`), and the working tree was
  byte-unchanged after every one (tree hash before/after). Zero survivors,
  zero deaths at a wrong gate.
- **`--selftest` writes nothing, proved by tree hash.** Tree digest identical
  before and after (`9c0ae679f8c11e9f`); 34/34 rows `target moved True`;
  `description offenders 0`; coverage `{gates 35, falsified 34, waived 1,
  waiver_forced True}`. The coverage waiver's forcing is genuinely
  machine-checked (`_coverage_forcing` hands the harness a gate no recipe
  targets and requires a raise).
- **Byte reproduction ×2, off-tree and git-less, from artifact-deleted trees.**
  Two seeds at different paths, no `.git` anywhere, artifacts never copied in;
  the second under `PYTHONHASHSEED=random`. Both produced
  `contract_output.txt = 2f1933c09b8f` and `contract_receipt.json =
  9b3638b796ae`, byte-identical to the delivered pair.
- **The seal partition is total and the counts are exactly as claimed:** 184
  sealed + 4 declared-unsealed = 188 payload keys, 189 receipt keys with the
  manifest. Recomputed from the manifest, not read off the paper.
- **The post-close seal leg is real.** INJ-07 planted an edit between read-back
  and `os.replace` via `promote`'s tamper hook; it died at `T-SEAL-PROMOTION ::
  post-close edit reached disk: ['arena_cells']`.
- **Every table attack was caught.** Census-table header swap (INJ-13), a
  parameters row transplanted into the outcomes table (INJ-14), and a
  duplicated SEAM row (INJ-15) each died at `G-CLAIMS-EQUAL`. All twelve paper
  tables are rendered and bound; `loose` catches any table bound by nothing.
- **Pre-bind transcript forgery is caught.** INJ-08B inserted a `[PASS]` row for
  a gate that never ran, carrying no numeral to avoid the typed-count trap; it
  died at `T-TRANSCRIPT-BOUND :: stray ['G-A-GATE-THAT-NEVER-RAN']`.
- **The wall positives are defended in depth.** All eleven standing sentences
  sit inside registered `CLAIM_TEXTS`, so deleting one dies at `G-CLAIMS-EQUAL`
  (gate 26) before `G-WALLS` (gate 28) can miss it.
- **The region reachability audit is genuinely transitive** through plumbing
  helpers, and my independent AST scan confirms no `b_*` function calls an
  `r_*` or `k_*` function (the unpoliced direction is empty in fact).
- **`--render` cannot be passed off as delivery on its face.** It writes
  nothing (tree hash identical), emits zero `[PASS]`/`[FAIL]` lines, and prints
  only `<<<TABLE …>>>` / `<<<FENCES>>>` / `<<<CLAIMS>>>` blocks with no
  receipt/transcript digest line. (But see MINOR-6 on its exit code.)
- **The arithmetic reconciles everywhere I checked it.** C(36,2)=630=24+606;
  5856=72+5184+600 with 5784 distinct; 180−39=141 vanishing; |Aut(K₃,₃,₃)|=6³·6
  =1296; |AGL(2,3)|/4 = 432/4 = 108; 1296/108 = 12 = splittings; 9!/(3!³·3!)=280;
  C(9,3)=84; 27·2/9=6; 36=6·6; 10=6+4; 21=13+2+3+1+2; 23=20+3.

---

## 2. MAJORS

### MAJOR-1 — `G-HEAD-REBUILT` is not total: eight of the head's numerals are ungated, and both §2 headline fractions live there. (INJ-09, DELIVERED GREEN)

The paper §8 says: *"**Every numeral position** in the four segments is parsed
back out of the emitted string … and compared, as an integer, against the
receipt leaf it names."* It is not.

The head carries **47 count numerals**. `HEAD_FIELDS` declares **39**
positions. The missing eight are exactly the two halves of each of the four
compound `A-OF-B` fields:

| field | emitted | in `HEAD_FIELDS`? | parsed back? |
|---|---|---|---|
| `EQUAL-RESIDUE-PAIRS-AGREEING` | `24-OF-24` | no | first half only |
| `DISTINCT-RESIDUE-COLLISIONS` | `0-OF-606` | no | first half only |
| `HISTORIES-SURVIVING` | `17-OF-5784` | no | first half only |
| `FIELDS-SURVIVING` | `12-OF-36` | no | first half only |

`k_parse_head`'s regex `([A-Z0-9\-]+)=([0-9][0-9,]*)` stops at the hyphen, so
the second half is never read at all; and the four keys it *does* recover are
absent from `HEAD_FIELDS`, so `g_head` never compares them. `head_fields_parsed
= 39` is `sum(len(f) for f in HEAD_FIELDS)` — the size of the expectation
table, not a coverage measurement.

**INJ-09** replaced those four `%d` arguments with `0, 999, 606, 0` and matched
the paper's fence. Result: **exit 0, artifacts written**, delivering

```
EQUAL-RESIDUE-PAIRS-AGREEING=0-OF-999; DISTINCT-RESIDUE-COLLISIONS=606-OF-0
```

— the total inversion of §2's sufficiency result (the state does *not* screen
the history; every distinct-residue pair collides) — while the transcript
carried `[PASS] G-STATE-SCREENS-THE-HISTORY :: equal-residue pairs 24 agreeing
24 distinct-residue pairs 606 colliding 0` and `[PASS] G-HEAD-REBUILT ::
segments 4 fields parsed 39 mismatches 0`. This is the E-22 species at
paper-19 (79 of 506 numerals unscanned), relocated into the head itself.

*Repair (exact).* Add the four compound fields to `HEAD_FIELDS` as pairs, e.g.
`("EQUAL-RESIDUE-PAIRS-AGREEING", ("state_equal_residue_agreements",
"state_equal_residue_pairs"))`; extend `k_parse_head` to
`([A-Z0-9\-]+)=([0-9][0-9,]*)(?:-OF-([0-9][0-9,]*))?` and return the pair; and
make `g_head` **total by construction** — parse the segment, and fail on any
`key=` position present in the string that is absent from `HEAD_FIELDS`
(a stray-key check, not only a missing-key check). Then compute
`head_fields_parsed` from what was parsed, not from the table's length.

### MAJOR-2 — the second artifact is promoted unbound: a forged transcript reaches disk beside a byte-identical clean receipt. (INJ-05, DELIVERED GREEN)

`full_run` computes `bound = tr.bind(led, text)` and then, on the write path,
**discards `bound`** (it is used only in the `--no-write` branch). `ET.promote`
writes `side_text` and returns `bytes_digest` of whatever it was handed; nothing
compares the promoted bytes to the ledger-bound digest, and no transcript digest
is carried in the receipt (I checked: the receipt has no such key).

**INJ-05** mutated `text` *after* `tr.bind` and before `promote`. Result: **exit
0**, and `contract_output.txt` on disk carries

```
  [PASS] G-Q58-VERDICT (forged after binding) :: …
  [PASS] G-WALLS-FORGED :: walls 7 patterns 53 standing sentences 11
VERDICT (forged after binding)
```

while the receipt's `ledger_head` is the *pristine* `32471e88823f5fb4` and
`transcript_stray` reads `0`. A forged gate row and a forged verdict header
were promoted next to an unforged receipt. This is EPR K3 MAJOR-6's mechanism
with the staging step removed.

*Repair (exact).* Seal the transcript: `seal.seal("transcript_digest", bound,
"G-TRANSCRIPT-BOUND")` at gate time, put `transcript_digest` in the payload, and
in `promote` compare `bytes_digest(ttxt)` against that seal before `os.replace`;
extend `Seal.verify_after_promotion` to re-read the side path as well as the
receipt. Equivalently: never let `text` be rebindable between `bind` and
`promote` — bind and promote the same immutable object and assert identity.

### MAJOR-3 — `G-TEMPLATE-EXERCISED` matches TEXT, not a live call; eight of nine families are satisfiable by a class that is never instantiated. (INJ-03, DELIVERED GREEN)

The paper §8 says each family's identifier *"is matched to a **live call** in
this module and that match is gated."* The implementation is
`re.search(TEMPLATE_CALLS[cid], src)` — a regex over the module's own source
text.

`class Run` (source lines 1778–1810) is **dead**: `Run(` appears nowhere in the
file. Its `__init__` alone contains `ET.Seal`, `ET.Transcript`,
`ET.SemanticWall`, `ET.AnchorSet`, `ET.Claims`, `ET.ReferentRegistry`,
`ET.CountRegistry`, `ET.ReadSet` — **eight of the nine family patterns**.
Worse, the ninth, `T-FALSIFIER-POISONS` (`ET\.FalsifierHarness`), has its only
two occurrences inside `run_falsifiers()` and `_coverage_forcing()`, both
reachable **only from `--selftest`**: in the `--run` delivery path that family
is not exercised at all, yet the gate publishes `template families 9 exercised
9`. Three families (`T-ANCHOR-CONSUMED`, `T-CLAIMS-EQUAL`, `T-REFERENT-BOUND`)
have their *call-site* alternative (`anchors\.verify_consumption`,
`claims\.gate`, `ref\.gate`) fail to match the real call sites at all — those
are written `CTX["anchors"].verify_consumption(…)` etc. — so only the
constructor alternative, present in dead code, matches.

**INJ-03** rewrote both real `ET.FalsifierHarness(` calls as
`getattr(ET, "Falsifier" + "Harness")(` and left the token in a **comment**.
Result: **exit 0, `template families 9 exercised 9`**.

This is precisely the TPL-2 item v15/PLAN.md orders applied *first*
("carried-not-used families forbidden").

*Repair (exact).* Replace the regex census with an execution census: wrap each
family's entry point in a counter (`CTX.setdefault("fam", collections.Counter())
["T-CLAIMS-EQUAL"] += 1` at the call site, or a `sys.settrace`/decorator on the
nine `ET` entry points), and gate `all(fam[cid] > 0 for cid in ET.FAMILIES)`
**in the mode being delivered**. If a family genuinely cannot run in `--run`
(the falsifier harness), declare it explicitly as selftest-only rather than
counting it exercised. Delete `class Run` and `_measured_register` (also dead).

### MAJOR-4 — S-1 "by construction" is defeated by a one-line alias route. (INJ-01, DELIVERED GREEN)

`module_call_graph` records `ast.Call` func `id`/`attr` and every `ast.Name`.
A builder reached by *name assembly* leaves neither.

**INJ-01** added to the comparator `k_census_word`:

```python
_leak = globals()["b_" + "raw_census"]()["parts"]
```

Result: **exit 0**, `[PASS] G-S1-DISJOINT-CODE :: regions 5 offences 0`. A
comparator calling a builder is invisible. `getattr(sys.modules[__name__], …)`
and `importlib` routes are equally invisible.

Two related gaps, from my independent scan:
- The paper says *"Four code regions"*; the gate reports **five**. The fifth,
  `plumbing`, holds **79 of 132** top-level functions and is exempt from the
  rule (`if region_of(name) not in ("reconstructor","comparator"): continue`).
  Reachability *through* plumbing is caught, so this is presentational — but
  the census builder `census_rows()` (whose product the comparator consumes) is
  a plumbing function and sits outside the four named regions entirely.
- The module docstring says the builder is *"the only region that may name a
  declared-side constant."* This is **not machine-checked and is violated
  twice**: `r_direction_splittings` names `B_ARITY`, and `s_coordinate` names
  `DIM`. `region_of` is case-sensitive, so `B_ARITY` classifies as plumbing.
  The affected published quantity is `DIRECTION-SPLITTING = 12`, classed
  RECONSTRUCTED — mitigated only because `g_invariance_groups` independently
  requires it to equal `inv_direction_index = 1296/108`.

*Repair (exact).* Add a second S-1 leg over the AST: inside any `r_*`/`k_*`
subtree, forbid `globals()`, `getattr(`, `sys.modules`, `importlib`,
`eval`/`exec`, and any string constant matching `^(b_|s_)\w+$`; and add a
declared-constant leg that flags any `ast.Name` in an `r_*`/`s_*`/`k_*` subtree
whose id is in an explicit `DECLARED_CONSTANTS` frozenset (case-insensitively).
Either derive the arity in `r_direction_splittings` from the block sizes or
reclassify DIRECTION-SPLITTING's backing.

### MAJOR-5 — the two standing walls are defeated by re-voicing, in the paper's own voice. (INJ-10, INJ-11, DELIVERED GREEN)

`W-RECONSTRUCTION-IS-NOT-DERIVATION` and `W-INVARIANCE-IS-NOT-GAUGE` are
eight- and ten-pattern lists over fixed subject/verb frames. Both are
paraphrasable without touching a pattern, and the positives remain present so
the self-seal leg is silent.

**INJ-10** (W1), inserted as prose before §7 — **exit 0**:

> The records derive nine actors: the cast follows from the blocks alone, so
> the actor count is obtained from the record rather than assumed, and the
> reconstruction therefore establishes that the points of the arena are an
> output of the writing and not an input to it.

Every pattern misses: the wall's frames are `the record**s**`-blind
(`\bthe record derives the (?:cast|actors)\b`), and `obtained`/`follows from`/
`establishes that … an output` are not in the derivation vocabulary
(`\bthe actor count is derived from the record\b` requires the word *derived*).

**INJ-11** (W2), likewise — **exit 0**:

> The round law's stabilizer is gauge: its 1,296 elements are unobservable in
> principle, the quotient by them carries the whole physical content, and the
> remaining 108 are the only relabellings an experiment could ever see.

`\bthe stabilizer is the gauge group\b` requires "the gauge **group**";
`\bis therefore gauge\b` requires "therefore"; `\bthe gauge quotient is\b`
requires that exact order. The referent gate is silent because 1,296 and 108
are both legitimate members of THE-INVARIANCE.

This is EPR K3 MAJOR-7's species (a blacklist defeated by re-voicing) reaching
the two walls this programme engraved for itself.

*Repair (exact).* Make both walls **frame-general** rather than
subject-specific:
`r"\brecords?\b[^.]{0,60}\bderiv\w*\b[^.]{0,40}\b(?:actors?|cast|points)\b"`,
`r"\b(?:actors?|cast)\b[^.]{0,60}\b(?:output|not an input|obtained from|follow\w* from)\b[^.]{0,40}\brecords?\b"`,
and for W2
`r"\b(?:stabilizer|invariance|relabellings?|orbit|quotient)\b[^.]{0,60}\b(?:is|are)\b[^.]{0,20}\bgauge\b"`,
`r"\bunobservable in principle\b"`, `r"\bcarries the whole physical content\b"`.
Then add a **licence leg**: give both walls `policed=("gauge","derive","derives",
"derived")` so that every sentence containing a policed word must carry a
rendered claim string — the mechanism `SemanticWall._licence_leg` already
implements and this unit passes `(), ()` for all seven walls, leaving it
switched off everywhere.

### MAJOR-6 — spelled-out numerals are outside every numeral gate; the Q58 headline can be inverted in the paper's own summary. (INJ-12, DELIVERED GREEN)

`ReferentRegistry.NUM` matches digits only. The paper's prose carries **92
spelled numerals** (`one`×37, `two`×19, `four`×12, `three`×9, `nine`×8,
`five`×4, `six`×3), several of them load-bearing counts, none registered as a
claim.

**INJ-12** made two edits — **exit 0, all 34 gates PASS**:

- §"The short of it": *"Run through nine, it holds at **five** and refuses at
  **four**"* → *"holds at **four** and refuses at **five**"* — the direct
  inversion of the unit's Q58 result, sitting three paragraphs above the table
  that states the truth.
- §1: *"**Three** rows are citations rather than computations"* → *"**Seven**
  rows …"*, contradicting the census's own `cited 3`.

*Repair (exact).* (a) Register every prose sentence carrying a spelled count as
a `CLAIM_TEXT` rendered from the payload through the existing `SPELLED` map
(the unit already has `SPELLED` and uses it for the REC-CARRIER anchor); or
(b) extend `ReferentRegistry.NUM` with a spelled-numeral alternation
(`one|two|…|twelve`), mapping to integers before the universe test. (a) is
stronger and is the house style: counts computed, never typed.

### MAJOR-7 — a typed, unbacked cited cardinality publishes green; the anchor that "backs" it constrains nothing. (INJ-02/INJ-02B, DELIVERED GREEN)

In `census_rows`, twenty-two of twenty-three cardinalities come from a measured
key `R[...]`. One is a literal: `("TICK", "DECLARED", S, 1, …)`. It is invisible
to both typed-count legs, because the literal is not inside a statement-builder
call — it reaches `claims.table` through `com(r["cardinality"])`.

Its declared backing is the HOR-TICK anchor, whose consuming predicate in
`g_census` is `"One Site a Tick" in tick`, where `tick` is the anchor's own
needle constant. **That predicate is constant-True for every payload.** Four of
the thirteen anchors are consumed this way — the operand is the module literal
and the test is a fragment of that same literal:

| anchor | consumer | predicate | binds a measurement? |
|---|---|---|---|
| `HOR-TICK` | G-OBJECT-CENSUS | `"One Site a Tick" in tick` | **no** |
| `NDEP-CARRIED` | G-PARAMETERS | `"NO TESTED NUMERAL IS REPRODUCED" in a` | **no** |
| `PLAN-WALLS` | G-WALLS | `"derivation" in order and "gauge" in order` | **no** |
| `EPR-MULTIPARTITE` | G-ARENA-REBUILT | `"degree six" in a` | **no** (degree is bound arithmetically elsewhere) |

The remaining nine are properly numeral-bound. The paper §8's general sentence —
*"verbatim anchors consumed by predicates that take numerals out of the located
text and compare them with measurements"* — is therefore false for four of
thirteen, and the harm is reachable: **INJ-02B** changed TICK's cardinality to
`5` in both code and paper and delivered **exit 0**, publishing
`| TICK | DECLARED | 5 | SEALED-CITATION | one scheduling convention; the
emergent speed is one site a tick |` in the paper and `'cardinality': 5` in the
receipt, under `[PASS] G-OBJECT-CENSUS :: rows 23 computed 20 cited 3 backed
23`.

*Repair (exact).* Replace the literal with a measured key
(`R["cited_tick_sites"] = 1`, measured from the anchor: `anchor_numerals` finds
none, so bind it to `SPELLED`-inverse — `1 if "One Site a Tick" in tick else 0`
is still tautological; instead cite the parent's numeric sentence). Where an
anchor carries no numeral, either (i) choose a needle that does carry the
number being cited, or (ii) stop calling the row *backed* and add a
`BACKING_ALPHABET` value `SEALED-CITATION-NON-NUMERIC`, gated so that no such
row may carry a cardinality the run did not compute. And in §8 replace the
universal sentence with the measured split (9 numeral-bound, 4 word-bound).

### MAJOR-8 — six payload keys are published as measurements but are typed constants, and one of them is false.

Assigned once and never recomputed:

| key | value | recomputed? | consequence |
|---|---|---|---|
| `receipt_leaves` | `0` | never | **published count is false** — the walk visits every leaf of a 188-key payload |
| `receipt_type_offences` | `[]` | never | `G-RECEIPT-TYPES`'s predicate `not P[...]` is **constant-True** |
| `receipt_type_offence_count` | `0` | never | evidence numeral is typed |
| `head_mismatches` | `0` | never | `g_head` computes `bad` locally and never writes it back |
| `transcript_stray` | `0` | never | two of `G-TRANSCRIPT-BOUND`'s three conjuncts are **constant-True** |
| `transcript_missing` | `0` | never | as above |

Each reaches `fmt(...)` → `cr.measured(name, value, "computed by this run")`,
so the CountRegistry's own doctrine — *"a constant that was never measured
cannot be published as a measurement"* — is defeated by routing the constant
through the payload. The delivered transcript line
`[PASS] G-RECEIPT-TYPES :: receipt leaves 0 type offences 0` publishes a false
count under a gate that cannot fail.

The substance is not undefended: `receipt_type_walk(P, bad)` runs after the
ledger closes, and the seal's `json.dumps` refuses opaque values. **INJ-17**
planted a `set` in the payload and the process did die (`rc=1`) — but with a
raw `TypeError` traceback out of `json.encoder` inside `Seal.seal`, **not** a
`CheckFail` at `G-RECEIPT-TYPES`, and not as a ledger row.

*Repair (exact).* Move the walk in front of its gate:
```python
bad = []; receipt_type_walk(P, bad)
P["receipt_type_offences"] = bad
P["receipt_type_offence_count"] = len(bad)
P["receipt_leaves"] = <leaves counted by the walk>
```
(have `receipt_type_walk` return a leaf count), and likewise write
`P["head_mismatches"] = len(bad)` from `g_head` and
`P["transcript_stray"]/["transcript_missing"]` from `tr.parse()` versus
`led.rows` **before** `g_transcript` evaluates them. Then `G-TRANSCRIPT-BOUND`
binds content and not only a cardinality (RUNBOOK #87).

### MAJOR-9 — the #82 CLI contract holds only at `argv[1]`; a mutant name after a mode flag yields a clean delivery at exit 0. (CLI battery)

`main()` whitelists `argv[1]` and ignores `argv[2:]` for every mode except
`--mutant`. Measured:

| argv | rc | effect |
|---|---|---|
| `--bogus` | 2 | usage ✓ |
| `--mutant` / `--mutant NOPE` | 2 | usage ✓ |
| `--run --extra` | **0** | full delivery, artifacts written |
| `--run --mutant MUT-ARENA` | **0** | **clean delivery**, 34/34 PASS, transcript says `mutant none`, receipt `9b3638b796ae` — byte-identical to the pristine |
| `--selftest --run` | 0 | selftest; `--run` ignored |

A battery or a reviewer invoking `--run --mutant NAME` receives a green
delivery that looks like a mutant run. The RUNBOOK's phrasing is "argv
whitelist; unknown flags/mutants exit 2".

*Repair (exact).* At the top of `main`: reject any `argv` whose length exceeds
the arity of its flag (`--mutant` takes exactly one operand, every other flag
takes none), returning 2.

---

## 3. MINORS

- **MINOR-1 — seals are attributed to gates that never evaluated them.** Only
  **27 of 34** gates take a seal. `gate_of_key`'s prefix map routes
  `state_equal_residue_*` to `G-STATE-COMPONENTS` (tested at
  `G-STATE-SCREENS-THE-HISTORY`), `q58_split_is_triangularity` to `G-Q58-ARMS`
  (tested at `G-Q58-VERDICT`), `class_cast_residue` to
  `G-CAST-UNIQUE-IN-THE-CLASS` (tested at `G-CAST-RESIDUE`), `arena_menu` to
  `G-ARENA-REBUILT` (tested at `G-MENU-LAW-SELECTED`), and `inv_local_*` /
  `inv_direction_*` to `G-INVARIANCE-GROUPS` (tested at `G-LOCAL-ARITY-GROUP` /
  `G-DIRECTION-INVARIANCE`). Integrity is preserved (the seal is taken before
  the testing gate, so a later mutation is still caught), but the manifest's
  `sealed_at_gate` column mis-states provenance for seven gates' worth of keys,
  and E-25's "sealed at the moment **its** gate passes" is not what happens.
  *Repair:* seal from the gate function's own key list, not from a prefix map.
- **MINOR-2 — the second AST scan is defeated at a distance.** `audit_typed_deep`
  inspects only literals *inside* a builder-call subtree. **INJ-06** added a
  module constant `_K3_TYPED_CELLS = 27` and wrote
  `tr.say("… cells " % … + str(_K3_TYPED_CELLS))`. Result: **exit 0**, the
  promoted transcript's second line reads `mode --run   mutant none   cells 27`,
  and the gate reports `statement builders audited 8 offences 0`. Note the scan
  *is* effective for direct literals: my first attempt (INJ-08, a forged
  transcript row containing "42") was killed by it. *Repair:* taint-track
  int-valued module constants and `str()`/`format()` of non-registry names into
  the eight callers, or route every `say`/`row` string through `cr.stmt`.
- **MINOR-3 — after-gate reads are free.** **INJ-04** added a raw `open()` of
  `v14/paper-19-r3-weld.md` after `G-READS-DECLARED` fires. Result: **exit 0**,
  `stray 0`. The `ReadSet` audit hook is live for the whole process; only the
  gate's position is early. *Repair:* re-evaluate the read set immediately
  before `promote` and fail there (the check is cheap and the hook is already
  installed).
- **MINOR-4 — the referent registry is membership-only and mis-routes by first
  matching noun.** `_universe_of` returns the first universe in insertion order
  (THE-INVARIANCE first). **INJ-19** delivered **exit 0** on: *"Under the gauge
  relabellings the nine mechanism arms recover 1,296 casts between them, and 108
  of those recoveries survive the orbit."* — an invariance noun launders
  invariance numerals into a sentence about the arms, whose true values are 5 and
  4. **INJ-16** separately delivered **exit 0** on an in-universe inversion
  (*"holds at 4 and refuses at 5"*), the known EPR K3 MINOR-7 species.
  *Repair:* score all matching universes and require the numeral to belong to
  every matched universe (or fail on ambiguity), and pair-bind the arms
  fractions as `(recovering, total)` / `(refusing, total)`.
- **MINOR-5 — a failing gate's published evidence contradicts the failure.**
  In roughly ten of the 34 mutant runs the evidence line reports the *unmoved*
  count because only the list key is planted and the paired count key is not
  recomputed — e.g. `MUT-FLOAT died at G-NO-FLOAT :: float literals 0 in the
  module`, `MUT-SOURCE … :: sources 16 mismatches 0`, `MUT-HEAD … :: mismatches
  0`, `MUT-REGION … :: offences 0`, `MUT-TYPED … :: offences 0`. Harmless in
  delivery (all gates pass), but the transcript row is not a faithful rendering
  of the predicate's inputs. *Repair:* derive every `*_count` key from
  `len(list)` at render time, and gate `len(P[list]) == P[count]`.
- **MINOR-6 — `--render` exits 0 without the paper gates or the totality
  check.** It skips the four paper gates by design (documented) *and* skips the
  seal-totality promotion check (`if uncovered and mode != "--render"`). Its
  stdout is unmistakable, so it cannot be read as a delivery — but an
  exit-code-only harness would score it green. *Repair:* have `--render` exit
  with a distinct non-zero-but-benign code, or print a `DIAGNOSTIC-ONLY: 4 gates
  skipped` banner on stdout and stderr.
- **MINOR-7 — the falsifier denominator is not the honest one.** `coverage`
  reports `gates 35` = 34 `G-*` + `T-FALSIFIER-COVERAGE`. The nine template
  `T-*` checks are load-bearing kill paths, are outside the ledger, and have
  neither a recipe nor a waiver — and three of them (`T-TRANSCRIPT-BOUND`,
  `T-SEAL-PROMOTION`, and the post-ledger `receipt_type_walk`) are the *only*
  real defence behind gates MAJOR-8 shows to be vacuous. The honest denominator
  is 44. Mitigation: the era's own `era_template` demos falsify them upstream.
  *Repair:* state the 35/44 split explicitly, or import the template's demo
  legs into this unit's coverage.
- **MINOR-8 — dead code and a stale typed count in the vouched surface.**
  `class Run` (33 lines), `_measured_register`, `s_type_walk` (only
  self-recursive) and `B_ARITH_SEVEN = 7` are all unreachable. `SEAL_AT` defines
  the key `"inv_"` twice. And the module docstring states *"it refuses four of
  **eight** declared generating mechanisms"* where the measured value is
  **nine** (`q58_arms_total = 9`), a typed count in the instrument's own
  vouching prose. *Repair:* delete the dead code; fix the docstring to cite the
  count by name or drop the numeral.

### One observation outside the instrument's control

`v14/paper-41-rec.md` is pinned at `c5fbc9acbd76`, which is the **working-tree**
state; `HEAD` carries `58b08940d04c`, and `v14/code/rec_exact.py` +
`v14/paper-41-rec.md` are uncommitted with a concurrent repair in flight. The
run fails loudly if the digest moves (`G-SOURCES-PINNED`), so this is not a
silent hazard — but under #91 a pin whose target exists only in an uncommitted
tree is not reproducible from the repository, and any `git checkout` breaks the
delivery. Worth an orchestrator decision before the seal commit.

---

## 4. COUNTS, VERIFIED FROM LIVE REGISTRIES

| claimed | verified | how |
|---|---|---|
| 34 gates + 1 waiver, machine-checked forcing | **YES** | `--list-gates` = 34; `coverage {gates 35, falsified 34, waived 1, waiver_forced True}`; `_coverage_forcing` raises on a gate no recipe targets |
| 34/34 recipes with real move-proofs | **YES** | out-of-harness sweep, one process each: 34/34 `rc=1` at the named gate, tree unchanged; `--selftest` 34/34 `target moved True`, `description offenders 0` |
| 184 sealed / 4 declared-unsealed / 188 published, totality at the door | **YES** | manifest recomputed: 184 + 4 = 188 payload keys, 189 with `seal_manifest`; unsealed = `gates`, `ledger_head`, `mode`, `mutant` |
| 13 anchors / 10 consumer gates / 0 unconsumed / 0 phantom | **YES as counts** | recomputed from `ANCHORS`; but see MAJOR-7 — the parenthetical *"consumers parse numerals from located text"* holds for **9 of 13**, not 13 |
| 9/9 template families matched to live calls (gated) | **NO** | match is textual; 8/9 satisfiable by dead `class Run`; `T-FALSIFIER-POISONS` unexercised in `--run` (MAJOR-3) |
| S-1 four disjoint regions, 0 offences | **PARTLY** | 0 offences on the implemented predicate, and no `b_→r_/k_` edge exists; but the gate reports **5** regions (79/132 functions in unpoliced `plumbing`), and the predicate is alias-blind (MAJOR-4) |
| a second AST scan catching the TPL-2 subspecies | **PARTLY** | catches direct `%`-format and integer-offset literals in builder subtrees (demonstrated: it killed INJ-08); defeated at one remove (MINOR-2) |
| walls W-RECONSTRUCTION-IS-NOT-DERIVATION and W-INVARIANCE-IS-NOT-GAUGE with the PLAN engraving consumed at `6ba8621d4ec7` | **PARTLY** | digest correct and the anchor is located in `v15/PLAN.md` and in the paper; the consumption predicate is a tautology (MAJOR-7) and both walls are re-voiceable (MAJOR-5) |
| head parsed back at 39 numeral positions | **YES, and that is the defect** | 39 declared positions against **47** count numerals in the head (MAJOR-1) |

## 5. TEMPLATE-CONFORMANCE VERDICT, PER FAMILY

| family | engraving | verdict |
|---|---|---|
| T-SEAL-PROMOTION | E-25 | **PARTIAL** — totality recomputed at the door and the post-close leg is real (INJ-07 died); but seals are attributed to non-evaluating gates (MINOR-1) and the second artifact is outside the seal (MAJOR-2) |
| T-TRANSCRIPT-BOUND | E-26 | **FAIL** — content binding happens (INJ-08B died) but only for the pre-bind text; the promoted bytes are unbound (MAJOR-2) and the gate's own row is two-thirds constant (MAJOR-8) |
| T-WALL-SEMANTIC | E-27 | **FAIL** — positives, self-seal and non-vacuity all present and the positives are claim-backed; negatives defeated by re-voicing on both standing walls, and the licence leg is switched off on all seven walls (MAJOR-5) |
| T-ANCHOR-CONSUMED | E-28 | **PARTIAL** — 13 located in digest-pinned sources and in the paper, 0 phantom, 0 unread; 4 of 13 consumed by tautologies (MAJOR-7) |
| T-CLAIMS-EQUAL | E-29 | **PASS** — the strongest family here. Header swap, row transplant and duplicated row all died; all 12 paper tables bound; fences by multiset; prose at exact multiplicity |
| T-REFERENT-BOUND | E-30 | **PARTIAL** — per-occurrence and prose-only as specified; membership-only, mis-routes on first matching noun, blind to 92 spelled numerals (MAJOR-6, MINOR-4) |
| T-NO-TYPED-COUNTS | E-31 | **PARTIAL** — two AST legs, both live, and they bite; defeated at one remove (MINOR-2), and six payload keys plus one census cardinality are typed constants published as measurements (MAJOR-7, MAJOR-8) |
| T-FALSIFIER-POISONS | E-32 | **PASS on the recipes, FAIL on scope** — 34/34 move their target and die at their named gate, out of harness, writing nothing; but every recipe is a *payload* plant, so no detector (`audit_no_floats`, `audit_regions`, `audit_typed_deep`, `receipt_type_walk`) is ever itself falsified — which is exactly why MAJOR-4, MINOR-2 and MAJOR-8 were reachable |
| T-READ-SET | E-33 | **PARTIAL** — the audit hook is on the `open` event and `MUT-READS` bites; the gate is positionally early, so after-gate reads are free (MINOR-3) |

## 6. INJECTION LEDGER (21 live injections, one process each, off-tree)

| id | what | result |
|---|---|---|
| INJ-01 | comparator reaches a builder via `globals()["b_"+…]()` | **SURVIVED** exit 0 |
| INJ-02 / 02B | TICK census cardinality 1 → 5, code + paper | **SURVIVED** exit 0, written |
| INJ-03 | template family token left only in a comment | **SURVIVED** exit 0, 9/9 |
| INJ-04 | raw `open()` of a repo file after `G-READS-DECLARED` | **SURVIVED** exit 0 |
| INJ-05 | transcript forged after `tr.bind`, before `promote` | **SURVIVED** exit 0, written |
| INJ-06 | typed numeral into `tr.say` via a module constant | **SURVIVED** exit 0, written |
| INJ-07 | post-close edit to the staged receipt | caught — `T-SEAL-PROMOTION` |
| INJ-08 | forged `[PASS]` row carrying "42" | caught — `G-NO-TYPED-COUNTS` |
| INJ-08B | forged `[PASS]` row, no numerals | caught — `T-TRANSCRIPT-BOUND` |
| INJ-09 | forge the four `A-OF-B` head fields, code + paper | **SURVIVED** exit 0, written |
| INJ-10 | W1 re-voiced ("the records derive nine actors") | **SURVIVED** exit 0 |
| INJ-11 | W2 re-voiced ("the stabilizer is gauge") | **SURVIVED** exit 0 |
| INJ-12 | spelled-numeral inversion of the Q58 headline + §1 count | **SURVIVED** exit 0 |
| INJ-13 | census-table header swap | caught — `G-CLAIMS-EQUAL` |
| INJ-14 | parameters row transplanted into the outcomes table | caught — `G-CLAIMS-EQUAL` |
| INJ-15 | duplicated SEAM row planted | caught — `G-CLAIMS-EQUAL` |
| INJ-16 | in-universe referent inversion (4/5 swapped) | **SURVIVED** exit 0 |
| INJ-17 | opaque (`set`) leaf planted in the payload | died, but as a raw `TypeError`, not at `G-RECEIPT-TYPES` |
| INJ-19 | cross-universe referent laundering via an invariance noun | **SURVIVED** exit 0 |
| CLI-A | `--run --mutant MUT-ARENA` | **SURVIVED** exit 0, clean delivery written |
| CLI-B | `--render` | writes nothing, no `[PASS]` lines — not passable as delivery |

Direction flips requested by the brief, as measured: `13 FREE → 3 FREE`,
`0 law-selected → 7`, `WITHHELD` deleted and `RECONSTRUCTED-CONDITIONALLY →
DERIVED` are all **caught** — every one of them lives inside a rendered fence
or a rendered table cell, and `G-CLAIMS-EQUAL`'s two-way equality kills them
(demonstrated by the table family INJ-13/14/15 and by `MUT-CLAIM`). The flips
that *do* pass are the ones that live where nothing renders: the compound head
fields (MAJOR-1), the spelled prose counts (MAJOR-6), and the transcript after
binding (MAJOR-2).

## 7. RECOMPUTATIONS

**141**, counted honestly: 10 object digests (open + close), 16 pinned-source
digests, 2 byte reproductions, 34 mutant recipes, 2 selftest legs, 21
injections, 8 argv forms, 2 mode probes, 13 anchor-consumption predicates, 9
template-family provenance traces, 7 static AST scans, and 17 arithmetic
reconciliations of published counts. **No published physics number moved under
any of them.** The one false published value found is `receipt_leaves = 0`
(MAJOR-8), a bookkeeping leaf, not a measurement of the theory.

## 8. WHAT THE PANEL SHOULD DO WITH THIS

The census, the state definition, the invariance measurements, the cast
uniqueness, the nine-arm Q58 split and the parameter count are, on everything I
could reach, correct and correctly worded — including the four careful
withholdings (`GAUGE-WORD=WITHHELD`, `RECONSTRUCTED-CONDITIONALLY`,
`CARRIER-CANDIDATE` rather than EXCITATION, `FREE-ROWS-A-LAW-SELECTS=0`). The
unit's judgement about *what it may say* is sound. Its machinery for *proving it
cannot say otherwise* has nine holes, and two of them (MAJOR-1, MAJOR-2) let an
inverted headline reach the delivered artifacts at exit 0.

Recommended: a repair pass over MAJOR-1 … MAJOR-9, a re-run, and a re-seal
before adjudication. Four sentences of §8 must change with the code — the
"every numeral position" sentence, the "live call" sentence, the "anchors …
parse numerals" sentence, and the "four code regions … through an alias"
sentence — each of which is, as written, a false claim about the instrument.

*Between delivery and adjudication every headline here — including this grade —
is a candidate reading.*
