# ARITY (paper-44) — K3 INSTRUMENT review

**Seat:** K3, instrument (seal, coverage, injections, CLI, #91 at its own
hands). **Unit:** ARITY, v15, paper-44. **Panel:** three seats.
**Standing:** between delivery and adjudication every headline below — the
unit's and this review's — is a **candidate reading**.

**Object, hash-verified at open and again at close (five, unchanged across the
whole audit):**

| object | sha256-12 open | sha256-12 close |
|---|---|---|
| `v15/paper-44-arity.md` | `177560920b33` | `177560920b33` |
| `v15/code/arity_exact.py` | `d0044766fcd8` | `d0044766fcd8` |
| `v15/code/arity_output.txt` | `95414a8d2824` | `95414a8d2824` |
| `v15/code/arity_receipt.json` | `c1354b632733` | `c1354b632733` |
| `v15/note-arity-pin.md` (pin) | `89b35dad3219` | `89b35dad3219` |

All four pinned sources recomputed live and matched: `89b35dad3219`,
`e2293b8c3858`, `29216cea946f`, `4fe88602280c`.

**Authority:** RUNBOOK.md through E-33 (E-22 … E-33; binding text
`v14/tpl_runbook_addenda.md`); `v14/code/era_template.py`; TPL-2's registered
items (`v15/PLAN.md`); and the recurring-disease catalogue in
`v15/review-contract-instrument.md` §2, `v15/review-disc-instrument.md` §3 and
`v15/review-autoglue-instrument.md` §4/§5 — **every entry of all three was
probed against this unit**, and the results are recorded whether the disease
was present or absent.

**Execution:** every run off-tree, git-less, from artifact-deleted trees, from
an **alien working directory** (`…/arity_k3/alien`, `…/alien2`), at absolute
paths, in `…/scratchpad/arity_k3/` (1.2 G peak). Only this seat's own PIDs
were signalled; no `pkill`. The repository was touched read-only except this
file, which is this seat's **sole repository write**.

**Recomputations, counted honestly: 170** — object digests open+close **10**;
pinned-source digests **4**; 34-recipe sweep, one process each **34**; byte
reproduction ×2 seeds **2**; injection sandboxes **25**; hostile argv **24**;
mode + whole-tree-hash write-nothing **5**; in-process instrument probes **6**;
independent arithmetic re-derivations off the receipt **58**; ledger-chain
recomputations **2**.

**Injection roster: 25 executed, 19 survived at exit 0.** Six died — three
correctly at their own gate (`G-WALLS`, `G-PAPER-CLAIMS`, `G-PAPER-COVERAGE`),
one correctly but *after* the artifacts had already been replaced on disk
(M9), and two only *collaterally*, at `G-FALSIFIERS`, because one recipe
hard-codes the sentence they moved (M5). The nineteen survivals are §4.

---

## GRADE: ACCEPT-WITH-FIXES

**The measurement layer is sound and I could not move a delivered number.**
Fifty-eight independent arithmetic re-derivations off the receipt — the
packing counts, the Bell number, `C(15,a)`, the maximum cut of `K_a`, the
event universes `C(9,a)`, the ladder modulus `27/gcd(27,w)`, `|S_9|`, the
window size `C(9,2)+2C(9,3)`, every `unique + non_unique = histories`, every
`offset = time − floor` — all reproduce exactly. Both artifacts byte-reproduce
off-tree, git-less, from artifact-deleted trees, under two hash seeds, from
two different alien working directories. **All 34 declared recipes die at
their declared gate, one process each, out of harness, with the tree
byte-unchanged after every one.** The falsifier harness is real: it digests
each recipe's target before and after and requires the move, which closes
AUTOGLUE MAJOR-7 outright.

**The vouching layer is where this unit is weaker than it says.** Nine MAJORs,
six of them named recurrences of already-engraved diseases (RUNBOOK §13
addendum, v13 #313: *a recurrence of an already-engraved disease is a MAJOR by
default and is named as a recurrence*). Three are not recurrences, and they
are the three that matter: **the verdict-equality comparator is a
set-membership test with a dead leg**, so five inverted head numerals — two of
them headline readings — reach both delivered artifacts at exit 0; **the
falsifier-coverage result is computed and discarded**, so eleven gates can
lose their recipe and the run still delivers; and **a post-close edit is
detected only after `os.replace` has already put the forged artifacts on
disk**, with no rollback and no ledger row.

No finding moves a delivered number. **M1, M2 and M9 should be fixed before
adjudication**; the rest are liftable in place.

---

## 1. WHAT HELD, MEASURED

- **The 34-recipe sweep, out of harness, one process each, in 34 pristine
  minimal trees.** 34/34 refuse at the declared gate, `rc=1`, `declared ==
  died`, tree hash identical before and after every run. Zero survivors, zero
  deaths at a wrong gate, zero anomalies.
- **`T-FALSIFIER-POISONS` is genuinely implemented.** `run_falsifiers` takes
  `digest(f.apply())` clean, then again under the flag, and requires the two to
  differ; the nested run's ledger, seal, registry, receipt, read log and memo
  counters are saved and restored around each recipe. This is the family
  AUTOGLUE carried in name only; ARITY closes it.
- **Byte reproduction ×2.** Seed A (`PYTHONHASHSEED=1`, full mirror tree, alien
  cwd A) and seed B (`PYTHONHASHSEED=99999`, independent tree, alien cwd B),
  both with both artifacts deleted and no `.git` anywhere, produced
  `arity_output.txt = 95414a8d2824` and `arity_receipt.json = c1354b632733` —
  byte-identical to the delivered pair.
- **Write-nothing, by whole-tree sha256 over the corpus, not by the unit's own
  two-artifact check.** `--list-gates`, `--render`, `--no-write`, `--selftest`
  and a refusing `--verify-paper` each leave the tree hash unchanged at
  `87d9e177f4ee4bfb`. 5/5.
- **The argv contract is a real loop, not an `argv[1]` whitelist.** Every
  position is checked; `--bogus`, `--RUN`, `--Run`, `--run`, `--run=`, `-h`,
  `--help`, `""`, `--mutant`, `--mutant NOPE`, `--mutant MUT-ARENA extra`,
  `--list-gates extra`, `--render extra`, `--verify-paper` (bare),
  `--list-mutants`, `--numbers` — **16/16 exit 2**. CONTRACT MAJOR-9 is
  **ABSENT**. (But see m5.)
- **The seal partition is total and the counts are exactly as the manifest
  says:** 26 sealed + 3 declared-unsealed + `seal_manifest` = 30 payload keys,
  recomputed from the live key set at the door, and re-verified **from the
  promoted file on disk** — a leg neither CONTRACT nor AUTOGLUE has.
- **The paraphrase battery is real and it bites.** Six plants written against
  the disease, run through the whole wall set exactly as the delivery runs it,
  6/6 caught. My own six *unlicensed* paraphrases (INJ-09), written from the
  disease and sharing no wording with any pattern, died at `G-WALLS` on three
  different walls — two of them on the **licence leg**, which is the mechanism
  CONTRACT MAJOR-5 asked for and this unit built.
- **Table and coverage attacks are caught.** A cell moved between `T-SEC2` and a
  true value from `T-SUBSTRATE` (INJ-19) died at `G-PAPER-CLAIMS`, stray in one
  bag and missing in the other. An unlicensed numeral planted in prose
  (INJ-20) died at `G-PAPER-COVERAGE`.
- **The transport decision procedure is discriminated, not asserted.** Six
  synthetic laws, one forced to each word at each slot plus an all-infeasible
  one, all emit the forced word; a procedure short-circuited to its first word
  dies on them (`MUT-TRANSPORT`).
- **`G-VERDICT-EQUALITY`'s *word* leg is a genuinely independent route.** The
  comparator re-decides `LAW-IN-A / NEEDS-3 / BREAKS` from `parent_value` and
  the per-arity `measured` list by its own arithmetic
  (`C(a,2)+v−C(3,2)` versus the constant reading) and compares Counters with
  the builder's. That leg is real and I could not defeat it. It is the
  *numeral* leg that is not (M1).
- **The anchor family is the strongest here.** Eight verbatim anchors, each
  located in the pinned source *and* in the paper under #125 canonicalisation
  at exactly one occurrence, readable only through an accessor that records
  the read, with a 24-character floor; consumption verified against gates that
  actually ran and actually read them. 8 reads, 0 unconsumed, 0 phantom.
  `MUT-ANCHOR` and `MUT-ANCHOR-USE` both bite.

---

## 2. COUNTS, VERIFIED FROM LIVE REGISTRIES

| quantity | claimed | live | source of truth |
|---|---|---|---|
| gates | 34 | **34** | `len(GATE_ORDER)` ∥ `--list-gates` "gates 34" ∥ 34 `[PASS]` rows ∥ `receipt.totals.gates` ∥ `G-CLOSE` fired 34 = declared 34 |
| **rows in the published ledger** | — | **32** | `len(receipt.ledger)` — `G-SEAL-TOTALITY` and `G-CLOSE` are absent (M3) |
| **published `ledger_head`** | one number | **two, plus a third on stdout** | receipt `7ff8a990f4b541c5` (32 rows) = transcript's last line; stdout prints `3ea48cfe71ef3cc9` (34 rows) (M3) |
| falsifier recipes | 34 | **34** | `len(FALSIFIERS)`; sweep 34/34 |
| gates with no recipe | — | **1** (`G-FALSIFIERS`) | computed by the run itself, published, **not gated** (M2) |
| waivers | — | **0** — no waiver mechanism exists | grep: no `WAIVER` anywhere |
| sealed / declared-unsealed / payload keys | — | **26 / 3 / 30** | `seal_manifest`, recomputed |
| sources | "exactly five" (docstring) | **4** | `len(SOURCES)`; the paper's own §2 table says 4 (m7) |
| path-value anchors | 8 | **8** | `PATH_ANCHORS`; all 8 read at declared JSON paths |
| verbatim anchors | 8 | **8** located, **8** consumed, 4 consumer gates | `anchors` / `G-ANCHORS-CONSUMED` |
| reading walls | "FOUR" (docstring) | **7** | `len(build_walls())` (m7) |
| wall controls | — | **18**, 18 caught | `sum(len(w.controls))` |
| **walls with a live licence leg** | "a paraphrase … is caught whatever words it chooses" | **4 of 7** | 3 walls declare no `subject` and no `policed`, so `licence_leg` returns immediately (M4) |
| paraphrase plants | ≥5 | **6**, 6 caught | `PARAPHRASE_PLANTS`, floor 5 |
| referent universes / sentences checked | — | **7 / 23** | `RR.universes`, `ref_sentences` |
| **reflexive `(X, X)` referent pairs** | — | **5** | `(4,4)`, `(36,36)`, `(126,126)`, `(315,315)`, `(945,945)` (M6) |
| paper surface | — | **11 tables, 9 fences, 6 prose claims, 456 numerals, 44 distinct, 0 uncovered** | `paper_claims` / `paper_coverage` |
| head | "every numeral … re-derived" | **148 numerals, 44 distinct values licensed** | `G-VERDICT-EQUALITY` — and that ratio *is* the defect (M1) |
| declared reads | — | **6 distinct**, 0 undeclared, 0 never-read | `read_set` — published as counts only, **no path list, no paper digest** (M8) |
| gate `G-TEMPLATE-EXERCISED` | named in the source comment at line 370 | **does not exist** | not in `GATE_ORDER`, not in the ledger (m7) |

---

## 3. TEMPLATE-CONFORMANCE VERDICT, PER FAMILY

The nine families are implemented in-file rather than imported (deliberately,
and correctly — importing would make another unit's file a runtime input and
break the off-tree reproduction that this unit demonstrably has).

| family | engraving | verdict | what the probe did |
|---|---|---|---|
| `T-SEAL-PROMOTION` | E-25 | **PARTIAL** | totality recomputed from the live key set at the door; the partition is genuinely constrained; add *and* edit both die (`MUT-SEAL-ADD`, `MUT-SEAL-EDIT`); and — better than either sibling — the seals are verified **again from the promoted file**. But that verification fires *after* `os.replace`: INJ-11 left a forged `union_carriers: 99` on disk beside its own pristine gate-time digest, and the process died with a raw traceback (M9). |
| `T-TRANSCRIPT-BOUND` | E-26 | **PARTIAL** | the transcript is parsed back out of the bytes to be promoted and reconciled with the ledger as a **multiset, evidence included**, and `transcript_head` is carried in the receipt — genuinely stronger than CONTRACT and DISC. But the regex sees only `[PASS]/[FAIL]` rows: INJ-12 promoted a forged narrative line at exit 0 (M7-adjacent, recurrence of AUTOGLUE MAJOR-4). And the ledger the receipt publishes is not the ledger the transcript was bound to (M3). |
| `T-WALL-SEMANTIC` | E-27 | **DEFEATED** | 7 walls, positive legs, non-vacuity on empty text, a no-self-licensing constructor check, 18 independent controls all caught, and a licence leg that killed two of my six unlicensed paraphrases. All four live licence legs are then defeated by one hedging token (M4), and one positive leg is discharged by the unit's own fence (m1). |
| `T-ANCHOR-CONSUMED` | E-28 | **CONFORMS** | one accessor, read-before-locate refused, occurrence exactly one in source *and* paper, 24-char floor, consumption checked against gates that ran and read. Phantom consumer dies. The strongest family here. |
| `T-CLAIMS-EQUAL` | E-29 | **CONFORMS, one hole** | keyed by table, both directions, header as a row, fences by multiset, prose at exact occurrence counts with both sides case-folded, unclaimed-table check. Transplant died. The hole is that the *claim template's own numerals* are outside the AST leg (M5/m3). |
| `T-REFERENT-BOUND` | E-30 | **PARTIAL** | per-occurrence, prose only, fences/tables/blockquotes stripped first, universe chosen by the *earliest* matching noun (an improvement on CONTRACT MINOR-4), and an `A of B` pair check. But it is membership-only, digit-only, and carries five reflexive pairs (M6). |
| `T-NO-TYPED-COUNTS` | E-31 | **PARTIAL** | a real AST leg over the module, both TPL-2 subspecies (string numerals *and* integer literals) inside statement-builder subtrees; `MUT-TYPED` bites; no float anywhere, checked twice. But `callers = ("stmt",)` only — `claim`, `table`, `fence` and `measured` are unaudited (M5, m3). |
| `T-FALSIFIER-POISONS` | E-32 | **CONFORMS on the move-proofs, FAILS on coverage** | 34/34 real move-proofs by digest, nested runs fully isolated, out-of-harness 34/34. But the coverage result is computed and thrown away (M2). |
| `T-READ-SET` | E-33 | **PARTIAL** | recorded at the audit hook, unbypassable, exemptions registered where the read happens and required to be used, `MUT-READ` bites. But the gate is fourth-from-last against a statement that says "at the last measurement gate" (m2), and the hook is REPO-scoped (m4). |

---

## 4. MAJORS

### MAJOR-1 — `G-VERDICT-EQUALITY` is a set-membership test, and the one leg that would bind a head numeral to its own position is a literal `pass`. Five inverted head numerals delivered at exit 0.

The gate statement, the paper §11 and the comparator's own docstring all say
the same thing: *"a comparator that shares no code, no input and no typed
literal with the builder parses every one of them back and **re-derives it
from the receipt's own row lists by its own arithmetic**"*. What
`head_audit` actually does with the head's **148** numerals is collect them
into `seen` and test `seen ⊆ lic`, where `lic` is a union of **44** distinct
values gathered from every row list in the receipt. No numeral is ever
compared against the value belonging to *its own position*.

The one leg that would have done so is written and then discarded
(`arity_exact.py:3265-3268`):

```python
for w, c in own_num.items():
    pat = r"%d %s" % (c, w)
    if w != "LAW-IN-A" and c and pat not in blob.replace(",", ""):
        pass
```

The comparator computes exactly the quantity that catches a direction flip in
the head — the rendered `"<count> <word>"` string against its own recomputed
count — and the body of the test is `pass`.

Five injections, each an edit to the builder with the paper's fence
regenerated alongside it (the DISC MAJOR-2 scenario), **all at exit 0, both
artifacts written**:

| injection | head, as delivered | truth |
|---|---|---|
| INJ-01 | `THE NUMERAL LEVEL RETURNS **7** LAW-IN-A, 2 NEEDS-3 AND 5 BREAKS` | 0 LAW-IN-A |
| INJ-05 | `**2** OF THE STATEMENTS TRANSPORT AND **4** BREAK` | 4 transport, 2 break |
| INJ-02 | `OPENING NO PAIR AND DOUBLING NOTHING **36\|36\|36\|36**` | `36\|0\|0\|0` |
| INJ-03 | `THE OFFSET IS **1\|0\|0\|1**` | `0\|1\|1\|0` |
| INJ-21 | `ITS **21147** SURVIVORS OVER THE COMPLETE LATTICE OF **6**` | 6 survivors, lattice 21147 |

INJ-01 is the worst: `0 LAW-IN-A` is the unit's title result — *no parent
numeral follows the declared a-only rule* — and `7 LAW-IN-A` says every one of
them does, in the first fence of the paper, while §11's `T-NUMERALS` table
three pages below still says `NEEDS-3` twice and `BREAKS` five times. INJ-02
publishes the create-nothing row for every arity, three sections above the
`T-SEC2` table that states the truth. Every numeral I substituted is
"licensed" because it is *some* value the run measured somewhere: `7` is
`len(transport.numerals)`, `36` is `obstruction_free` at `a=2`, `1` and `0`
are offsets, `21147` and `6` are each other's neighbours in the same segment.

Two further sentences of the paper are false as written: §11's *"shares no
code, no input and no typed literal with the builder"* — `verdict_segments`
and `head_audit` are both handed `rec`, the same object, which is the only
input either has — and *"re-deciding the verdict words by its own arithmetic"*,
which is true of the **words** and of nothing else.

*Repair (exact).* Give the head a positional field table, as CONTRACT
MAJOR-1's repair does: emit each segment through a `(field_name, value)` list,
have the comparator parse `key=value` positions and require **every parsed
position to equal the receipt leaf it names**, with a stray-key check so the
scan is total by construction. At minimum, restore the discarded leg — replace
the `pass` with a `findings.append(...)` — and extend it to `LAW-IN-A` and to
the statement counts. Ship INJ-01, INJ-02, INJ-03, INJ-05 and INJ-21 as
declared recipes requiring `G-VERDICT-EQUALITY` to die.

### MAJOR-2 — the falsifier-coverage result is computed, published as evidence and left out of the predicate. Eleven gates lose their recipe and the run still delivers. *(recurrence of DISC MAJOR-5, in a sharper form)*

`closing_battery` computes

```python
uncovered = sorted(g for g in gates if g not in covered)
```

against the **declared** gate list — the right denominator, and a deliberate
improvement on DISC, whose denominator was the gates fired so far. It then
publishes `uncovered` in the evidence and gates on

```python
LD.gate("G-FALSIFIERS", not sent and not wrong and not unreached, …)
```

`uncovered` is not in the predicate. There is no waiver mechanism anywhere in
the unit.

**INJ-22** deleted ten recipes (`MUT-PACKING`, `MUT-FIDELITY`, `MUT-ORDER`,
`MUT-NAMING`, `MUT-FLOOR`, `MUT-MENU`, `MUT-LADDER`, `MUT-FORCING`,
`MUT-SEC2-THEOREM`, `MUT-CRYSTAL`) — every recipe that falsifies a *law* gate.
Result: **exit 0, both artifacts written**, and the delivered transcript reads

```
[PASS] G-FALSIFIERS :: {"declared_gates": 34, …,
 "gates_with_no_falsifier": ["G-CONSTRUCTOR-FIDELITY", "G-FALSIFIERS",
 "G-FIDELITY-FIRST", "G-LAW1-NAMING", "G-LAW2-CRYSTALLIZATION",
 "G-LAW2-SHARPENED", "G-LAW3-MENU", "G-LAW4-LADDER", "G-LAW5-FORCING",
 "G-LAW6-SEC2", "G-SUBSTRATE-CENSUS"], …}
```

Eleven of thirty-four gates uncovered, printed in the gate's own evidence,
under `[PASS]`. In the pristine run the same key reads
`["G-FALSIFIERS"]` — the coverage gate is the one gate nothing falsifies, and
nothing declares it exempt.

*Repair (exact).* Put `not uncovered` into the predicate, and add a `WAIVERS`
map with a machine-checked forcing (CONTRACT's `_coverage_forcing` is the
reference implementation: hand the harness a gate no recipe targets and
require a raise). Waive `G-FALSIFIERS` explicitly, or give it a recipe — a
sentinel recipe whose `apply` returns a constant is one line and the harness
already detects it.

### MAJOR-3 — the receipt publishes a 32-row ledger and a chain head over 32 rows, while the transcript carries 34; the chain is not verifiable from the receipt at all; and the gate that says otherwise says it in terms.

`payload["ledger"]`, `payload["ledger_head"]` and `LD.recompute_chain()` are
all taken at `arity_exact.py:4538-4552`, **before** `G-SEAL-TOTALITY` and
`G-CLOSE` fire at 4562 and 4583. Measured:

| where | ledger rows | head |
|---|---|---|
| `receipt.ledger` / `receipt.ledger_head` | **32** | `7ff8a990f4b541c5` |
| `arity_output.txt` `[PASS]` rows / last line | **34** | `7ff8a990f4b541c5` |
| stdout, `gates %d ledger head %s` | 34 | **`3ea48cfe71ef3cc9`** |
| `receipt.totals.gates` | **34** | — |

Three numbers for one quantity, against E-26's *"the row count, the gate
count, the `--list-gates` output and any published total are ONE number,
computed after the last gate."* The two rows the receipt drops are exactly the
two that certify the seal and the gate inventory.

`G-CLOSE`'s own statement asserts the opposite: *"the ledger, its chain and
the transcript digest are all built after this row, so nothing that certifies
the seal sits outside the object that publishes it."* The source comment three
lines above it names the disease precisely — *"a ledger snapshotted before the
gates that certify the seal publishes a chain covering everything except
them"* — and describes what the code does.

Second defect, same object. `ledger` is declared unsealed with the reason
*"the chained ledger is verified by recomputing its own chain, not by a digest
of itself."* It cannot be. `Ledger.recompute_chain` digests a body containing
`statement`, and `payload["ledger"]` drops `statement`. I recomputed: row 1
already fails to reproduce its own `row_digest` from the published fields. A
reader can chain the published `row_digest`s (that does reproduce
`7ff8a990f4b541c5`) but cannot check that any `row_digest` belongs to its row.
The declared-unsealed reason is therefore not available to anyone holding the
receipt.

*Repair.* Move `ledger_rows`, `payload["ledger"]`, `recompute_chain()` and
`ledger_head` *after* `G-CLOSE`; print the same head on stdout that the
artifacts carry; and either keep `statement` in the published rows or digest a
body that omits it.

### MAJOR-4 — every wall with a live licence leg is defeated by one hedging token, and three of the seven walls have no licence leg at all. *(recurrence of AUTOGLUE MAJOR-3)*

Two mechanisms are supposed to stop a re-voiced breach. Both are opened by the
same class of word.

**The negative leg** suppresses a pattern hit whenever the match's own
sentence carries a negation before it: `NEG = \b(?:not|never|nor|no|cannot|
neither|without|whether|refuses?|denies)\b`. **The licence leg** requires any
sentence that names a wall's subject near a policed form to carry a licence —
and four of the seven walls list bare negations or bare hedges as licences:

| wall | licence leg | bare-negation / hedge licences |
|---|---|---|
| `W-NO-SELECTION` | live | `\bnot\b`, `\bnever\b`, `\bwould\b`, `\bnothing measured\b`, `\bwithout the arena\b` |
| `W-NO-RECONSTRUCTION-AS-DERIVATION` | live | `\bnot\b`, `\bnever\b` |
| `W-NO-INVARIANCE-AS-GAUGE` | live | `\bwould\b`, `\bno sentence\b` |
| `W-EXTENSION-SCOPE` | live | `\bnot\b`, `\bnever\b`, `\bwould\b` |
| `W-NO-PROBABILITY` | **dead** — no `subject`, no `policed` | — |
| `W-NO-CARRIER-OVERREACH` | **dead** | — |
| `W-NO-MOTIVATION-CLAIM` | **dead** | — |

**INJ-09B** planted five sentences, one per live-licence wall, each making that
wall's banned claim as flatly as its own control does, each carrying that
wall's cheapest licence:

> The arena **determines** the event size once the nine actors are laid down,
> and that is **not** in doubt. Three actors is what this arena **requires** of
> a division event, and no other size is admissible; that is **not** a
> conditional reading. That the parent's structure is **recoverable** from its
> own records **derives** the event size, and **not** merely illustrates it.
> The **corpus** at four actors admits every seam-spanning group free of
> charge, and **not** one of them is priced. The menu's value **would** be
> called **physical** by any reader, since it is **invariant** under the whole
> sweep.

Result: **exit 0, 34/34 PASS, and both artifacts byte-identical to the
pristine delivery** (`95414a8d2824`, `c1354b632733`). Every standing wall of
this unit — including `W-NO-SELECTION`, which carries the whole Q17/Q19
withholding, and `W-EXTENSION-SCOPE`, which carries the scope discipline the
paper turns on — was breached in one edit, and the receipt records `ok` for
all seven.

**INJ-10** shows the negative leg falling to the same word on its own. The
sentence

> There is **no** doubt that the event size **is selected** by the arena's own
> subgroup lattice, and **not** by any declaration a unit of this corpus ever
> made.

matches `W-NO-SELECTION`'s negative pattern
`(?:the )?(?:event size|arity|a)\b[^.]{0,40}\bis (?:uniquely )?selected\b`
verbatim. The lead `there is no doubt that the ` trips `NEG`, the hit is
dropped, and `\bnot\b` licenses the licence leg. **Exit 0, artifacts
byte-identical.**

The 18 controls do not catch any of this because **not one of them contains a
negation** — they are all flat affirmatives, which is the easy half.

*Repair (exact).* Delete every bare-negation and bare-hedge pattern from every
`licences` list; a licence must be a positive commitment to scope
(`\bcandidate\b`, `\bwithin the declared extension family\b`, `\bconditional\b`,
`\bcounting-only\b`, `\bidentifiability\b`, `\bat this arena\b`). Restrict the
`NEG` guard to negations that stand *between* the subject and the policed form,
not anywhere earlier in the sentence. Give `W-NO-PROBABILITY`,
`W-NO-CARRIER-OVERREACH` and `W-NO-MOTIVATION-CLAIM` real `subject`/`policed`
sets so their licence legs run. And add a **negation control** to each wall —
its existing control plus `, and that is not in doubt` — required to be caught;
that alone converts 18 controls into 36 and would have caught INJ-09B and
INJ-10 before delivery.

### MAJOR-5 — the fidelity pre-registration is re-declarable post-hoc: five substrate counts become three, delivered at exit 0, with the paper's own sentence still saying five. *(recurrence of DISC MAJOR-4 / AUTOGLUE MAJOR-6)*

The pin says the run is *"fidelity-gated at a=3 against the committed
substrate counts before any new-a row runs"*. It names no count, no path and
no cardinality. The set of five lives entirely in `PATH_ANCHORS` and in the
`want` dict — Python literals in the unit's own source — and the sentence the
paper stakes on it, *"the five substrate counts agree with the committed
anchors 5 of 5"*, is rendered by `CL.claim` with a `%d of %d` whose template is
**outside the AST leg** (`audit_module` is called with `callers=("stmt",)`).

**INJ-16B** dropped `strict_triples` and `window` from `want` and held the
claim's rendered text stable. Result: **exit 0, both artifacts written.** The
delivered head reads

```
AGREES WITH THE COMMITTED SUBSTRATE 3 OF 3 BEFORE ANY OTHER ROW IS TAKEN
```

while §2 of the delivered paper still reads *"**the five substrate counts
agree with the committed anchors 5 of 5**"*, and `G-PAPER-CLAIMS` passes,
because the claim's numerals are now typed rather than rendered. The paper's
own §2 sentence and the paper's own first fence contradict each other in the
same delivery.

The first version of this injection (INJ-16), which regenerated the claim text
too, *was* stopped — but at `G-FALSIFIERS`, with
`falsifiers_dying_elsewhere: ["MUT-CLAIM"]`, and for an accidental reason:
`paper_under("MUT-CLAIM", …)` appends the literal string *"The five substrate
counts agree with the committed anchors 5 of 5."* to the paper, and once the
registered claim no longer reads that, the recipe's plant lands nowhere and
`MUT-CLAIM` survives. Per LOR #269 a kill on the wrong leg is not evidence;
this one is also a **typed count in the vouched surface**, invisible to the AST
leg because `paper_under` is not a statement builder. INJ-23 (the same claim
typed to a false `4 of 5`) died the same collateral death.

*Repair (exact).* Move the five substrate row names and their committed values
verbatim into `v15/note-arity-pin.md` — already hash-pinned at `89b35dad3219`
and already read through the anchor accessor — and gate `set(want.keys())`
and each value against the pinned bytes. Derive the claim's `five` from
`len(want)` through the existing `SPELLED`-style route rather than typing it.
Add `claim`, `table` and `fence` to `audit_module`'s `callers`. Ship INJ-16B
as a recipe requiring `G-CONSTRUCTOR-FIDELITY` to die.

### MAJOR-6 — the referent registry carries five reflexive pairs and is blind to spelled numerals; four prose inversions delivered at exit 0. *(recurrence of E-30 / DISC MAJOR-1 / AUTOGLUE MAJOR-1)*

`ReferentRegistry.NUM` matches digits only, and `paper_coverage` uses the same
digit-only token. Every spelled count in the paper — and there are many, several
load-bearing — is outside both gates. Separately, five of the 34 declared pairs
are reflexive:

| universe | reflexive pairs |
|---|---|
| `crystallization` | `(4, 4)` |
| `union` | `(36, 36)` |
| `factorization` | `(126, 126)`, `(315, 315)`, `(945, 945)` |

Each licenses an `X of X` fraction in **any** sentence of that universe.

| injection | edit (prose only) | result |
|---|---|---|
| INJ-06 | §10, spelled: *"**Three of the five** principles fail to admit the parent's arity at all, and only **two** of them are even evaluable at **nine** candidate event sizes"*; §9, spelled: *"At three actors it is **four**"* (truth: one) | **exit 0, artifacts byte-identical** |
| INJ-07 | §8: *"At the parent's arity the discrete partition likewise stands alone at **315 of 315** histories"* (truth: 276 of 280) | **exit 0** |
| INJ-08 | §4: *"the census's non-unique rounds number **0**; at two, four and five actors it is **4**"* — the direct inversion of Law 1's numeral result | **exit 0, artifacts byte-identical** |
| INJ-18 | §12's standing disclaimer *"and nothing measured here selects it without the arena"* deleted | **exit 0** |

INJ-06 sits three lines below the bold sentence it contradicts. INJ-08 inverts
`0|4|0|0` in the prose while the fence and `T-FORCING` both still print it
correctly. INJ-07 is licensed purely by `(315, 315)`.

*Repair (exact).* Split reflexive pairs into a `SELF_PAIRS` set and require any
`X of X` occurrence to sit in a sentence carrying a totality qualifier (`all`,
`every one of`), or render those positions as *"all 315"* so no `A of B` form
exists to imitate. Extend `NUM` with a spelled alternation (`one|two|…|twelve`)
in both `ReferentRegistry` and `paper_coverage`. Register §4's numeral
sentence, §8's census sentence and §9's forced-pair sentence as `CL.claim`
strings — the mechanism is already built and already used six times.

### MAJOR-7 — the transcript's non-gate lines are bound to nothing. *(recurrence of AUTOGLUE MAJOR-4 / CONTRACT MAJOR-2)*

`Transcript.bind` reconciles `[PASS|FAIL] <gate> :: <evidence>` triples with the
ledger as a multiset — evidence included, in both directions, against the exact
bytes that will be promoted, with `transcript_head` sealed into the receipt.
That is the strongest instance of family (b) on the panel. But the regex sees
only gate rows.

**INJ-12** added one `TR.say(...)` line inside `promote()`. Result: **exit 0**,
and `arity_output.txt` on disk carries

```
  summary: seam-spanning groups doubling nothing 36|36|36|36 at a=2|3|4|5
```

directly above a `VERDICT` block whose own segment reads `36|0|0|0`, with
`transcript_head` in the receipt certifying the forged bytes because the digest
is taken *of* them.

The delivered transcript happens to carry only two non-gate lines today, so the
realised exposure is small — but the mechanism is unbounded and the receipt's
`transcript_head` gives a reader false assurance that it is not.

*Repair.* Add a `G-TRANSCRIPT-NARRATIVE` leg that re-parses every numeral on
the non-gate lines of the bound text and requires each to equal the payload
leaf it names — the discipline `G-PAPER-CLAIMS` already applies to the paper's
tables, applied to the instrument's own.

### MAJOR-8 — the object under test has no digest anywhere in either artifact.

The receipt's `provenance` lists the four `SOURCES`. `read_set` publishes
`{"distinct_reads": 6, "undeclared": [], "declared_never_read": [],
"unused_exemptions": []}` — counts, no paths. The string `paper-44-arity` does
not occur anywhere in `arity_receipt.json`. There is no `paper_sha`, no
`object_under_test`, no rendered path.

The consequence is measured and it is the reason so many rows of §6 read
"artifacts byte-identical": **INJ-06, INJ-08, INJ-09B, INJ-10, INJ-13 and
INJ-14 each delivered a modified paper or a modified process and produced
`arity_output.txt = 95414a8d2824` and `arity_receipt.json = c1354b632733` —
the delivered digests, bit for bit.** A reader holding the committed pair
cannot tell which paper text it certified, and the seal commit's own digests
do not discriminate. DISC, by contrast, seals the paper (its INJ ledger records
`e275be03304b` for the corrupted text); ARITY does not.

*Repair.* Seal `paper_sha256_12` and the paper's repository-relative path into
the payload at `G-PAPER-CLAIMS`, and publish `read_set["paths"]` as the sorted
multiset the gate already computed.

### MAJOR-9 — a post-close edit is detected only after `os.replace`; the forged artifacts are on disk and stay there, and the process dies as an unhandled traceback.

`promote` verifies the seals at the door and then, uniquely on this panel, **re-reads the promoted receipt from disk** and verifies again. That leg is real
and it fired.

**INJ-11** inserted one line above the serialisation:

```python
body["law6_sec2"] = dict(body["law6_sec2"]); body["law6_sec2"]["union_carriers"] = 99
```

Result: `rc=1` — but the failure sequence is `os.replace(tmp_r, OUT_JSON)` →
`os.replace(tmp_t, OUT_TXT)` → `SEAL.close()` → raise. After the run:

```
arity_receipt.json on disk:  "union_carriers": 99
seal_manifest["law6_sec2"]:  {"digest": "6e98367e9a2d899b", …}   ← pristine
```

Both artifacts were written, the receipt carries the forged value beside a
certificate for the value it does not contain, and nothing removed them. In the
repository this replaces the committed artifacts before failing. The exception
also escapes `main`'s `try` (which wraps `run_measurements`, not `promote`), so
the operator sees a Python traceback, not `REFUSED:`, and no ledger row — the
CONTRACT MAJOR-8 / AUTOGLUE m8 shape, on the seal's own final leg.

*Repair (exact).* Verify then replace: serialise, re-parse the blob,
`SEAL.verify_at_promotion(json.loads(blob), LD, "seal_manifest")` on the parsed
bytes, and only then `os.replace`. Keep the from-disk leg as a belt, wrap
`promote` in `main`'s `try`, and on failure restore the previous artifacts (or
never replace them: write, verify the staged file, replace last).

---

## 5. MINORS

**m1 — one wall positive leg is discharged by the unit's own verdict fence,
not by any sentence the paper writes.** `SemanticWall.scan` canonicalises the
whole paper; `canon` does not strip fenced blocks. Measured over the delivered
paper: `W-NO-SELECTION`'s positive `implicit in a constructor` occurs **once in
the whole text and zero times outside the fences** — it exists only in the head
segment the run itself renders. Four more positives occur twice, once in prose
and once in a fence, so deleting the prose half leaves the wall satisfied;
INJ-18 demonstrated exactly that at exit 0. The gate's statement — *"a POSITIVE
leg the paper must satisfy so that deleting the wall's own standing sentence is
itself a violation"* — is not true of that positive. *Repair:* scan the walls
over `prose_only(paper_text)` as the referent family already does, or register
each positive as a `CL.claim` so its deletion dies at `G-PAPER-CLAIMS` first.

**m2 — the read-set gate fires fourth-from-last; the tail window is open.**
*(E-33, recurrence of DISC MINOR-5 and AUTOGLUE m1.)* `G-READ-SET` is gate 31
of 34. INJ-13 planted `open(REPO/"RUNBOOK.md")` as the first line of
`promote()`: **exit 0, artifacts byte-identical**. The same read before the gate
dies, so the hook is sound and only the ordering is wrong — and the statement
says *"compared HERE, at the last measurement gate"*, which is a narrower claim
than the family's *"at the LAST gate"* and still not what happens. *Repair:*
re-check the read log inside `promote()` after the seal legs, with the two
artifact paths and the two `.tmp` paths declared as exemptions.

**m3 — the TPL-2 integer-offset subspecies is ungated at the registry door.**
*(recurrence of DISC MINOR-3 / AUTOGLUE m3.)* `audit_module` walks only calls
named `stmt`. INJ-15 wrote `CR.measured("n_walls", len(walls) - 7 + 12,
"counted")`: **exit 0**, and the `G-WALLS` statement publishes *"12 reading
walls scan the paper"* against seven walls in `receipt.walls`. Harm is bounded
only because gate statements reach neither artifact (m6). *Repair:* add
`measured`, `claim`, `table` and `fence` to `callers`, and flag any `ast.BinOp`
with an int `ast.Constant` operand in a `measured` value argument.

**m4 — the audit hook is REPO-scoped, so a read outside the repository is
invisible.** *(recurrence of AUTOGLUE m2.)* `ReadSet.install`'s hook keeps only
paths under `REPO`. INJ-14 opened and read `/etc/hosts` mid-run: **exit 0**,
`distinct_reads` unchanged at 6, artifacts byte-identical. The docstring's
*"every open() this process performs is recorded"* is false as written.
*Repair:* record every path and classify, with an `EXTERNAL` bucket required to
be empty.

**m5 — CLI mode resolution is last-wins with no conflict detection, and the
selftest's exit code inverts under it.** *(CONTRACT MAJOR-9 residue / AUTOGLUE
m5.)* The argv loop itself is clean (16/16 rejections). But:

| argv | rc | effect |
|---|---|---|
| `--selftest --list-gates` | **0** | selftest **silently discarded**; prints the gate list |
| `--list-gates --selftest` | 1 | selftest runs; `--list-gates` discarded |
| `--mutant MUT-ARENA --selftest` | 1 | **the mutant is silently discarded**; a selftest runs |
| `--selftest --mutant MUT-ARENA` | 1 | same |
| `--mutant A --mutant B` | 1 | last wins, no diagnostic |

A passing `--selftest` returns **1**; a *discarded* `--selftest` returns **0**.
An exit-code-only harness therefore scores a genuine selftest as a failure and
a silently skipped one as a pass. Separately, there is **no `--run` flag at
all** — delivery is a bare invocation, and `--run` exits 2, so a battery
written against the sibling units' CLI scores this unit as broken. *Repair:*
track which flag set the mode and return 2 on a second one; reject a repeated
`--mutant`; accept `--run` as an explicit no-op alias; and make a passing
selftest exit 0.

**m6 — gate statements reach neither artifact.** *(recurrence of DISC NOTE-2 /
AUTOGLUE m7.)* `payload["ledger"]` rows keep `n, gate, passed, evidence, prev,
row_digest` and drop `statement`; the transcript prints only `[PASS] <gate> ::
<evidence>`. Every `CR.stmt(...)` — where most of this unit's self-description
lives, including all four sentences MAJOR-1, MAJOR-2, MAJOR-3 and m2 quote — is
unpublished, so a reader cannot check the instrument's claims against either
artifact. It is also why `row_digest` is unverifiable (M3). *Repair:* keep
`statement` in the published ledger rows.

**m7 — three false self-descriptions in the vouched surface.** *(E-23 third
leg.)* (a) The module docstring: *"Exactly **five** files are read as SOURCES"*
— `len(SOURCES)` is **4**, and the paper's own §2 table says 4. (b) The
section-1 comment: *"the TPL-2 prohibition on carried-not-used families is a
gate here (**G-TEMPLATE-EXERCISED**), not a claim"* — **no such gate exists**;
it is in neither `GATE_ORDER` nor the ledger, and no family-exercise check runs
anywhere. DISC's NOTE-3 cited this gate as the thing to lift *from this unit*.
(c) `build_walls`'s docstring: *"**FOUR** READING WALLS"* — there are **seven**.
*Repair:* correct all three; build the family-exercise gate the comment
promises, or delete the sentence.

**m8 — `MUT-READ` targets a file the minimal corpus need not contain.**
*(AUTOGLUE m8.)* The recipe reads `REPO/RUNBOOK.md`. It is written correctly —
the audit hook records the path before the open is attempted, and the recipe
catches `OSError` — so it does refuse at `G-READ-SET` off-tree. Recorded as
handled, not as a defect, because this unit fixed the shape AUTOGLUE flagged.

**m9 — `--verify-paper` on any path outside the repository fails at
`G-FALSIFIERS`, attributed to a recipe.** *(AUTOGLUE m9.)* Given a valid copy
of the paper at an out-of-repo path, the run refuses with
`G-FALSIFIERS :: falsifiers_dying_elsewhere: ["MUT-CLOSE", …]` — a mode
limitation reported as a falsifier anomaly, which is the most misleading
possible attribution. *Repair:* reject an out-of-repo paper path at rc 2 with a
usage message, or exempt it explicitly.

---

## 6. INJECTION LEDGER (25 executed, one process each, all off-tree, alien cwd)

| # | injection | target | result |
|---|---|---|---|
| 01 | `FLIP-LAWINA` | head `0 LAW-IN-A` → `7`, fence regenerated | **exit 0**, written (M1) |
| 02 | `FLIP-OBSTRUCTION` | head `36\|0\|0\|0` → `36\|36\|36\|36` | **exit 0**, written (M1) |
| 03 | `FLIP-OFFSET` | head offset `0\|1\|1\|0` → `1\|0\|0\|1` | **exit 0**, written (M1) |
| 04 | `SCOPE-DELETED` | `WITHIN THE DECLARED EXTENSION FAMILY` removed from the head | **exit 0**, written (M1) |
| 05 | `FLIP-STATEMENTS` | `4 TRANSPORT AND 2 BREAK` → `2 … 4` | **exit 0**, written (M1) |
| 06 | `SPELLED` | spelled fraction *"three of the five principles"* + spelled inversion | **exit 0**, artifacts byte-identical (M6) |
| 07 | `REFLEXIVE-PAIR` | *"315 of 315"* asserted of the parent arity | **exit 0** (M6) |
| 08 | `INUNIVERSE-INVERT` | §4 non-unique `4` ↔ `0` | **exit 0**, byte-identical (M6) |
| 09 | `WALLS-UNLICENSED` | six paraphrases, no licence token | died `G-WALLS` — 3 walls fired, 2 on the licence leg ✔ |
| 09B | `WALLS-LICENSED` | five licensed breaches, one per live-licence wall | **exit 0**, byte-identical (M4) |
| 10 | `NEG-GUARD` | negative pattern matched, in-sentence `no` before it | **exit 0**, byte-identical (M4) |
| 11 | `POSTCLOSE` | sealed value edited before serialisation | detected — but after `os.replace`, as a traceback, artifacts poisoned on disk (M9) |
| 12 | `TRANSCRIPT-NARRATIVE` | forged non-gate line in the promoted transcript | **exit 0**, written (M7) |
| 13 | `READ-AFTER-GATE` | undeclared repo read inside `promote()` | **exit 0**, byte-identical (m2) |
| 14 | `READ-OUTSIDE` | `/etc/hosts` read mid-run | **exit 0**, byte-identical (m4) |
| 15 | `TYPED-DOOR` | integer offset at `CR.measured` | **exit 0**, written (m3) |
| 16 | `FIDELITY-REDECLARE` | 5 → 3 counts, claim + paper regenerated | died `G-FALSIFIERS` — **collaterally** (M5) |
| 16B | `FIDELITY-REDECLARE` | 5 → 3 counts, claim text held stable | **exit 0**, written (M5) |
| 17 | `PREREG-REWRITE` | `NEEDS-3`'s feasibility replaced by an admission of post-hoc fitting | **exit 0**, written (M5-adjacent) |
| 18 | `POSITIVE-VIA-FENCE` | §12's standing wall disclaimer deleted | **exit 0**, written (m1, M6) |
| 19 | `TABLE-TRANSPLANT` | true value moved between two paper tables | died `G-PAPER-CLAIMS` ✔ |
| 20 | `UNLICENSED-NUMERAL` | `787877` planted in prose | died `G-PAPER-COVERAGE` ✔ |
| 21 | `HEAD-POSITION-SWAP` | `survivors` ↔ `lattice` swapped in the head | **exit 0**, written (M1) |
| 22 | `COVERAGE-DEAD-LEG` | ten recipes deleted | **exit 0**, 11 gates uncovered, `G-FALSIFIERS` PASS (M2) |
| 23 | `CLAIM-TYPED` | claim template typed to a false `4 of 5` | died `G-FALSIFIERS` — **collaterally** (M5) |

**Direction flips requested by the brief, as measured.** `0 LAW-IN-A → 7`:
**PRESENT** (INJ-01). `36/0/0/0 → 36/36/36/36`: **PRESENT** (INJ-02). The
offset row inverted: **PRESENT** (INJ-03). `WITHIN THE DECLARED EXTENSION
FAMILY` deleted from a verdict word: **PRESENT** (INJ-04). All four reach both
delivered artifacts at exit 0 whenever the paper's fence is regenerated
alongside the builder — and the fence is the only thing that has to move,
because `G-VERDICT-EQUALITY` is a membership test (M1).

**The nine families on this unit, as probed:** reflexive referent pairs
**PRESENT** (5, M6); post-final-gate seal window **PRESENT in effect** —
detected, but only after the forged bytes are on disk, with no rollback (M9);
payload-blind verdict route **PRESENT** (M1: 148 numerals, 0 positionally
bound; and both routes read the same `rec`); name-based S-1 **N/A** — there is
no S-1 gate in this unit, and the docstring's *"S-1 is met by construction"* is
carried by prose alone; post-hoc pre-registration **PRESENT** (M5, INJ-16B and
INJ-17); bare-negation licence tokens **PRESENT** (M4, 4 of 4 live walls);
spelled-fraction blindness **PRESENT** (M6, INJ-06); argv-position CLI holes
**ABSENT** as CONTRACT MAJOR-9, **PRESENT** as AUTOGLUE m5 last-wins (m5);
typed offsets **PRESENT** at the registry door (m3).

---

## 7. WHAT I COULD NOT BREAK

Recorded so the adjudicator can price the walls that held.

- **Any delivered number.** The 945/280/315/126, the 21147, the 868480 and
  3981934, the 105/455/1365/3003, the 36/288/1113/2751, the 15 carriers and 54
  realised pairs, the 6|5|5|4 and 6|4|4|4, the moduli 3 and 27, the 4782969 and
  the cap 100000 all re-derive by my own arithmetic, 58 for 58.
- **The 34 recipes.** All die at their declared gate out of harness, and the
  move-proofs are genuine digests taken on the probe's own output.
- **Byte reproduction**, twice, under two hash seeds, off-tree, git-less, from
  artifact-deleted trees, from alien working directories.
- **The anchor family**, against a broken needle, a phantom consumer, a
  read-before-locate and a below-floor needle.
- **The claims family**, against a cross-table transplant.
- **The coverage scan**, against an unlicensed numeral.
- **The transport decision procedure**, against a short-circuit.
- **The paraphrase battery**, which caught three of my six *unlicensed*
  paraphrases on two different legs — including two on the licence leg, the
  mechanism CONTRACT MAJOR-5 asked for.
- **The seal partition and totality**, against add and edit, at the door and
  again from disk.
- **The argv whitelist**, at 16/16 rejections in every position.
- **`--selftest`, `--render`, `--no-write`, `--list-gates` and a refusing
  `--verify-paper`**, all write-nothing by whole-tree hash.

The unit also does three things no sibling on this panel does: it verifies the
seals **from the promoted file**, it takes its falsifier denominator from the
**declared** gate list rather than from the gates already fired, and its
referent registry picks the universe by the **earliest** matching noun rather
than by insertion order. Each of those is a named repair from an earlier review,
lifted and working.

---

## 8. REPAIR ORDER, SUGGESTED

1. **M1** — make the head positional and total; restore the discarded `pass`
   leg; correct §11's *"shares no input"* and *"re-derives every numeral"*.
   Ship INJ-01/02/03/05/21 as recipes.
2. **M9** — verify the parsed blob before `os.replace`, wrap `promote` in
   `main`'s try, and never leave a forged artifact on disk.
3. **M2** — put `uncovered` into the `G-FALSIFIERS` predicate and add a
   machine-forced waiver for `G-FALSIFIERS` itself.
4. **M3** — build the ledger, its chain and the head *after* `G-CLOSE`; publish
   one ledger head everywhere; keep `statement` so the chain is checkable.
5. **M4** — delete every bare-negation and hedge licence; narrow the `NEG`
   guard; give the three inert walls a live licence leg; add 18
   negation-controls.
6. **M5** — anchor the five substrate row names and values to the pin; derive
   the claim's *five*; widen `audit_module`'s `callers`. Ship INJ-16B.
7. **M6** — split the reflexive pairs; add spelled numerals to both scans;
   register §4/§8/§9's numeral sentences as claims.
8. **M8** — seal the paper's digest and path into the receipt.
9. **M7**, then **m1 … m9** in place; m3, m6 and m7 are one line each.

None of these requires a re-measurement. If they are applied I expect every
delivered number in `arity_output.txt` and `arity_receipt.json` to be
unchanged except for the ledger rows M3 adds, and the paper to change only
where M1's §11 sentences, M5's §2 sentence and m7's docstrings touch it.

---

*Between delivery and adjudication every headline in the unit under review, and
every verdict in this review, is a candidate reading.*
