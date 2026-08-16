# AUTOGLUE (paper-45) — K3 INSTRUMENT review

**Seat:** K3, instrument (the era audit: seal, coverage, injections, CLI, #91 at
its own hands). **Unit:** AUTOGLUE, v15, paper-45. **Panel:** three seats.
**Standing:** between delivery and adjudication every headline below — the
unit's and this review's — is a **candidate reading**.

**Object, hash-verified at open and again at close (five, unchanged across the
whole audit):**

| object | sha256-12 open | sha256-12 close |
|---|---|---|
| `v15/paper-45-autoglue.md` | `09ee568a4bba` | `09ee568a4bba` |
| `v15/code/autoglue_exact.py` | `d750a64f153c` | `d750a64f153c` |
| `v15/code/autoglue_output.txt` | `1a287adcaead` | `1a287adcaead` |
| `v15/code/autoglue_receipt.json` | `34606049f1ef` | `34606049f1ef` |
| `v15/note-autoglue-pin.md` (pin) | `88c04df52c19` | `88c04df52c19` |

**Authority:** RUNBOOK.md through E-33; `v14/TEMPLATE.md` +
`v14/code/era_template.py` (`d04a3eb58fbc`, verified as read by the instrument
itself); TPL-2's registered items (`v15/PLAN.md`); and the recurring-disease
catalogue in `v15/review-contract-instrument.md` §2 and
`v15/review-disc-instrument.md` §3, every entry of which was probed against
this unit.

**Execution:** all runs off-tree, git-less, from artifact-deleted trees, in
`.../scratchpad/autoglue_k3/` (peak 0.4 G). The repo was touched read-only
except this file. Two repo files carry uncommitted edits at close
(`v15/code/contract_exact.py` 09:42, `v15/code/disc_exact.py` 09:38) — those
are the sibling seats' repair work, not this seat's; the five objects above
re-verify byte-for-byte.

**Recomputations counted honestly: 121** — 44-mutant sweep, one process each
**44**; injection sandboxes **23**; baseline byte-identity ×2 seeds **2**;
hostile argv **19**; mode + whole-tree-hash write-nothing **7**; in-process wall
and comparator probes **14**; arithmetic re-derivations off the receipt **12**.

**Injection roster: 23 designed, 14 survived at exit 0.** Nine died — three at
`G-PAPER-CLAIMS`, two at `G-DETERMINISM`, two at `G-WALL-SEAMCONFINED`, one at
`G-PAPER-REFERENT`, one vacuous and re-run. The fourteen survivals are §3.

---

## GRADE: ACCEPT-WITH-FIXES

This is the strongest instrument the v15 panel has seen. It closes, by
construction and not by assurance, five of the nine diseases the two prior
reviews engraved: the CLI is a real argv loop and not an `argv[1]` whitelist;
the coverage denominator contains the gates that fire after it; spelled
numerals are generated rather than whitelisted; the transcript's gate rows are
reconciled with the ledger twice, the second time against the bytes that will
be promoted; and the parent's 216 is *parsed out of the parent's own sentence*
rather than typed. **All 44 declared mutants die at their declared gates, one
process each, out of harness.** Both artifacts byte-reproduce off-tree under two
hash seeds from artifact-deleted trees. The `--selftest` and all four read-only
modes write nothing, verified by whole-tree hash rather than by the two
artifacts the instrument checks itself.

The measurement layer held. I could not move a delivered number: the 108, the
216, the 162, the 468, the 29791, the 77 and the 0-overlap all re-derive from
the receipt's own per-object censuses by my arithmetic.

The **vouching** layer is where it is weaker than it says. Seven MAJORs, five of
them named recurrences of already-engraved diseases (RUNBOOK §13 addendum,
v13 #313: *a recurrence of an already-engraved disease is a MAJOR by default and
is named as a recurrence*). The two that are not recurrences are the two that
matter most: a sealed value can be forged **after the last gate** and reaches
the receipt beside its own pristine gate-time digest; and one of the nine
families is carried in name with no mechanism behind it at all.

No finding below moves a delivered number. All are repairable in place.
**M2 and M7 should be fixed before adjudication**; the rest are liftable.

---

## 1. WHAT HELD, MEASURED

- **The 44-mutant sweep, out of harness, one process each.** 44/44 refuse at
  their declared gate. (43/44 in my minimal tree: `MUT-READ` targets
  `RUNBOOK.md`, absent there, and died with a raw `FileNotFoundError`; in a tree
  carrying that file it refuses correctly at `G-READ-SET`. Recorded as m8.)
- **Byte reproduction.** `PYTHONHASHSEED=1` and `PYTHONHASHSEED=99999`, two
  independent off-tree trees with both artifacts deleted → `1a287adcaead` and
  `34606049f1ef`, identical to each other and to the in-repo bytes.
- **Write-nothing, by tree hash.** `--selftest`, `--no-write`, `--numbers`,
  `--list-gates`, `--list-mutants`, `--list-families` and a refusing
  `--verify-paper` each leave the whole tree hash unchanged at
  `8876738c8de4d063`. The instrument's own selftest checks only the two
  artifacts; the stronger check passes too.
- **The cross-universe referent plant is ABSENT.** Target (1)'s "pair 108 with
  162 falsely" — `INJ-14` planted *"ready for 108 of the 162"* and died at
  `G-PAPER-REFERENT` with the pair named in evidence. The per-occurrence pair
  mechanism is real and is this unit's best paper gate.
- **Census-table swaps and transplants are ABSENT.** `INJ-15` moved one cell of
  `TBL-INVENTORY` (`108`→`72`, a true value elsewhere) and died at
  `G-PAPER-CLAIMS`: stray in one table, missing in another, exactly as §13
  claims.
- **Wall paraphrases written from the disease are caught — when they carry no
  licence token.** `INJ-13` planted six novel paraphrases, one per wall, none
  copied from any pattern. All six walls fired. (What defeats them is M3.)
- **Phantom consumers are ABSENT** (`MUT-CONSUMER` dies at
  `G-ANCHOR-CONSUMPTION`); all 9 anchors are read through the one accessor, both
  QUOTED anchors are located paper-side as well as source-side.
- **Post-close seal *addition* is caught** (`MUT-SEAL` → `G-SEAL-TOTAL`,
  totality recomputed at the door from the live key set). It is *mutation* that
  is not — M2.
- **Vacuous modes are ABSENT.** `--verify-paper` refuses an empty paper and a
  directory at rc 2; every wall fails on empty text by construction
  (`Wall.scan`'s first branch); `G-PAPER-COVERAGE` requires
  `len(numerals(ptext)) > 0`.
- **No typed head numeral.** The AST leg over the source is real and
  `MUT-TYPED` dies at it. The head's 30 numeral positions are all interpolated.
- **The equivalence-class disclaimer is honest.** CROSS-ONLY and ALL-NEW do
  admit the same 162; I re-derived it from `incidence_census` ∩ `form_census`.

## 2. COUNTS, VERIFIED FROM LIVE REGISTRIES

| quantity | claimed | live | source of truth |
|---|---|---|---|
| gates | 42 | **42** | `receipt.totals.gates`, `len(receipt.ledger)`, `[PASS]` rows in the transcript — one number, three places, consistent |
| falsifier recipes | "42/42 mutants" | **44** | `--list-mutants`; `len(FALSIFIERS)` |
| `--list-gates` rows | — | **44** | two gates carry two recipes each: `G-ARENA` (`MUT-ARENA`, `MUT-AUT`), `G-INCIDENCE-CENSUS` (`MUT-RULE-PEEK`, `MUT-RULE-CROSS`) |
| gates with no recipe | 0 | **0** | `covered` ⊇ `gates_declared`; `WAIVERS` is empty — no waiver anywhere |
| families | 9, set-equal | **9, set-equal** | parsed live out of `era_template.py`'s own `FAMILIES` block; `tpl_ids == mine_ids` |
| walls | 6 | **6** | `len(WALLS)` |
| wall controls | 30 | **30** | `sum(len(w.controls))`, 5 per wall, all caught |
| anchors | — | **9** | 7 PARSED, 2 QUOTED |
| sources | 6 | **6** | all authenticate at pinned shas |
| payload keys | — | **40** (29 sealed, 11 unsealed) | `Seal.verify` at the door |
| head numeral positions | "every numeral" | **30** | 9 / 9 / 4 / 8 across the four segments |

**One correction to the delivery claim.** The seat brief reads *"42 gates; 42/42
mutants at named gates."* The live registry carries **44 mutants at 42 gates**.
Both totals are internally consistent and nothing is over-claimed — 44/44 die —
but the two numbers are not one number, and E-26's rule (*the row count, the
gate count, the `--list-gates` output and any published total are ONE number*)
is the reason to say so. `--list-gates` prints 44 rows for 42 gates without
saying which it is counting.

## 3. TEMPLATE-CONFORMANCE VERDICT, PER FAMILY

| family | verdict | note |
|---|---|---|
| `T-SEAL-PROMOTION` | **DEFEATED** | gate-time digests, totality at the door and a second verify are all real — and all of it happens before the payload is serialised. M2. |
| `T-TRANSCRIPT-BOUND` | **PARTIAL** | gate rows bound twice, in both directions, against the promoted bytes. Every non-gate line of the transcript is bound to nothing. M4. |
| `T-WALL-SEMANTIC` | **DEFEATED** | six walls, a positive leg, a self-licensing check, and 30 independent controls — all defeated by one common word. M3. |
| `T-ANCHOR-CONSUMED` | **CONFORMS** | one accessor, consumption verified against gates that ran, both sides for QUOTED, operands parsed out of the anchors' own bytes. The strongest family here. |
| `T-CLAIMS-EQUAL` | **CONFORMS, one leg unused** | tables two-way by multiset keyed by table, headers as rows, fences at declared multiplicity, unrendered-table check. The prose-claim leg is never called. m6. |
| `T-REFERENT-BOUND` | **CONFORMS, with a hole** | per-occurrence pairs over prose only, fences and tables stripped first. Two *reflexive* pairs in the declared set open M1. |
| `T-NO-TYPED-COUNTS` | **PARTIAL** | AST leg over the source, both TPL-2 subspecies — inside statement builders only, not at the registry door. m3. |
| `T-FALSIFIER-POISONS` | **NOT IMPLEMENTED** | no move-proof by digest exists anywhere in the file. M7. |
| `T-READ-SET` | **PARTIAL** | recorded at the audit hook, not in a helper — but REPO-scoped, and gated fourth-from-last against a family description that says "after the last gate". m1, m2. |

---

## 4. MAJORS

### MAJOR-1 — the paper's own §3 headline is invertible in its own prose. Five inversions delivered at exit 0. *(recurrence of E-30 / DISC MAJOR-1, verbatim)*

The sentence the whole unit turns on is §3: *"Read the second row first.
**CROSS-ONLY reaches 216 of 288.** That is the parent's number."*

| injection | edit (prose only) | result |
|---|---|---|
| `INJ-23` | §3 *"CROSS-ONLY reaches **216** of 288"* → *"reaches **288** of 288"* | **exit 0, 42/42 PASS, both artifacts written** |
| `INJ-10` | §11 read-out *"does so at **108** of the 288 events that cross"* → *"at **288** of the 288"* | **exit 0** |
| `INJ-09` | §4.2 *"**256** successors at 81 … and **512** at the other 27"* → *"**8** … and **4**"* | **exit 0** |
| `INJ-11` | §5.1 heading *"motivation and lawfulness are disjoint"* → *"coincide"*; body *"**The two sets share nothing**"* → *"**The two sets are one and the same**"* | **exit 0** |
| `INJ-12` | §1 *"what is measured is EVENT-CONDITIONED CREATION … and **not autonomous dynamics**"* → *"is **AUTONOMOUS DYNAMICS** … and the process selects the event too, so the update is self-driving at this arena"* | **exit 0** |

`INJ-23` is the worst of the five: the delivered paper states the create-nothing
result for the create-cross rule, three lines above the table that states the
truth, and the head, the receipt and the transcript all still read 216.

**Mechanism, measured.** Four gates could have caught it and none does.
`G-PAPER-COVERAGE` asks only *is this numeral some integer the run produced* —
its universe is `collect_ints` over the **entire receipt**, every census cell
included, so 288, 8, 4 and 72 are all resolvable anywhere. `G-PAPER-REFERENT` is
the real mechanism, and it binds only `\d+ of (the )?\d+`; its 24 declared pairs
include **two reflexive pairs**, `("events", n_spanning, n_spanning)` = (288,288)
and `("readings", n_fourth_reads, n_fourth_reads)` = (468,468), which license
*"288 of 288"* and *"468 of 468"* in any sentence in the paper. `INJ-09`'s and
`INJ-11`'s edits are not `A of B` at all, so the referent gate never sees them.
`G-PAPER-POLARITY` is five literal alternations; *"the two sets are one and the
same"* matches none of them (`\bthe motivated events are (the |)lawful\b`), and
neither does *"is AUTONOMOUS DYNAMICS … self-driving"*. No wall polices any of
the five.

**Repair (exact).** (a) Split the reflexive pairs out of `PAIRS` into a separate
`SELF_PAIRS` set, and require that any prose occurrence of `X of X` sit in a
sentence that also carries the wall-style qualifier that makes it a total
(`all`, `every one of`); or drop them and render those two head positions as
*"all 288"* / *"every one of the 468"* so no `A of B` form exists to imitate.
(b) Register the five load-bearing prose sentences as `C.claim(...)` strings
rendered from the payload — the mechanism is already built and is currently
unused (m6); `INJ-23`, `INJ-09` and `INJ-11` all die immediately once §3's
sentence, §4.2's multiplicity sentence and §5.1's disjointness sentence are
rendered claims. (c) Add the five injections above as declared recipes.

### MAJOR-2 — a sealed value edited after the last gate reaches the receipt, beside its own pristine gate-time digest

`promote()` verifies the seals twice — `G-SEAL-TOTAL` at the last gate and
`G-INTEGRITY` "against the objects that will actually be written". Both fire
**before** `blob = json.dumps(R, …)`. The payload stays mutable in between.

**`INJ-19`** inserted one line immediately above the serialisation:

```python
R["motivation"] = dict(R["motivation"], overlap=77, lawful=77)
```

Result: **exit 0, 42/42 PASS, both artifacts written.** The promoted receipt
carries

```
"motivation": {"lawful": 77, "motivated": 77, "overlap": 77, ...}
```

— the unit's second headline inverted, motivation and lawfulness now *identical*
rather than disjoint — while the same receipt's `seal_manifest` publishes

```
"motivation": {"digest": "de5ce106226690f3", "sealed_at_gate": "G-MOTIVATED-DISJOINT"}
```

which is the **pristine** gate-time digest, and the head and the transcript both
still read `THE TWO SETS SHARE 0`. The seal manifest in the delivered receipt is
a certificate for a value the delivered receipt does not contain.

The byte-level defences do not reach this: the staging read-back proves the
bytes written equal the bytes intended, not that they equal the sealed values.
This is CONTRACT MAJOR-2's mechanism relocated from the transcript to the
receipt, and it is the one finding here with no engraved precedent.

**Repair (exact).** Serialise first, verify second: build
`blob = json.dumps(R, …)`, then re-parse it and run `SL.verify(json.loads(blob),
LDg, "at the bytes")` as the true final gate, so the object verified is the
object promoted. Cheaper equivalent: make `R` immutable after `G-INTEGRITY`
(`types.MappingProxyType`, or a deep-freeze that raises on `__setitem__`) and
assert identity of the dict handed to `json.dumps`. Add a recipe that edits a
sealed row between `G-INTEGRITY` and the serialisation and requires
`G-INTEGRITY` — not the transcript check — to die.

### MAJOR-3 — all six walls are defeated by one licence token in the offending sentence *(recurrence of CONTRACT MAJOR-5, in its licence-leg form)*

The licence leg is this unit's answer to the CONTRACT K2 finding, and it is
sound in design: a sentence making a policed *kind* of claim is refused unless
that same sentence carries a qualifier from a declared set. The defect is the
sets. Five of the six licence lists contain a **bare negation**:

| wall | licence set contains |
|---|---|
| `WALL-SEAMCONFINED` | `\bnever\b`, `\bnot\b` |
| `WALL-NO-METRICAL-READING` | `\bnot\b` |
| `WALL-RECONSTRUCTION-NOT-DERIVATION` | `\bnot\b`, `\bnothing\b`, `\bneither\b` |
| `WALL-RELATION-NOT-LAW` | `\bnot\b`, `\bnever\b`, `\bcannot\b` |
| `WALL-COUNTING-ONLY` | `\bnot\b` |
| `WALL-DECLARATION` | `\bnot the\b`, `\bnot used\b`, `\bcandidate\b`, `\bscope\b` |

**`INJ-20`** planted six sentences in the paper, each making that wall's banned
claim as explicitly as its own control does, each ending in that wall's cheapest
licence token:

> This update gives the theory its dynamics, though **not the** whole of it.
> Once the event has fired the next state is determined, and **not** before.
> The completion is a consequence of the record it faces, and **not** otherwise.
> A sector's own links are moved by the neighbour's events, which is **not** in doubt.
> The cross block is the metric datum the geometry carries, and **not** a tally.
> Most crossings are lawful at this arena, and **not** merely some.

Result: **exit 0, 42/42 PASS**, and the receipt publishes `ok: true` for **all
six walls**. Every standing wall of this unit — including
`WALL-SEAMCONFINED`, which carries the parent adjudication's ruling, and
`WALL-DECLARATION`, which carries W1 — was breached in one edit.

Isolated per-wall probe (no other text): six for six pass.

The 30 controls do not catch this because **not one of the 30 contains a
negation**. They are therefore systematically weaker than the disease they
stand for: the control set proves the patterns match unqualified assertions,
which is the easy half.

**Repair (exact).** Remove every bare-negation pattern from every `licence`
list. A licence must be a *positive commitment to scope*, not a negation:
`\bcandidate\b`, `\bat (this|one) arena\b`, `\bgated\b`, `\bdeclar\w+\b`,
`\bcounting-only\b`, `\breproduc\w+\b`, `\bnot the (theory|law|dynamics)\b`,
`\bno law selects\b`. Then add a **negation-control** to each wall: the wall's
existing control plus `, and that is not in doubt`, required to be caught. That
one addition converts all 30 controls into 60 and would have caught `INJ-20`
before delivery.

### MAJOR-4 — the promoted transcript's narrative is bound to nothing; a forged census publishes green *(recurrence of CONTRACT MAJOR-2)*

`G-TRANSCRIPT-BOUND` reconciles `[PASS|FAIL] <gate> <chain>` triples with the
ledger, twice, the second time against the exact bytes to be promoted — and
that is genuinely stronger than the parent unit. But the regex sees only gate
rows. Every `say(...)` line is outside it, and no transcript digest is carried
in the receipt.

**`INJ-03`** changed one format argument in the §3 census printer. Result:
**exit 0, 42/42 PASS**, and `autoglue_output.txt` on disk carries

```
  creation rule        events alive   seam-spanning alive   refused
  CROSS-ONLY                270            288            185
```

against the receipt's own `spanning_alive_by_rule: {"CROSS-ONLY": 216, ...}` and
the paper's `TBL-INCIDENCE`, both of which read 216 and both of which pass their
gates. The transcript is the artifact a reader opens first, and 17 of its 103
lines — the arena summary, the four-row incidence census, the seam line, the
preparedness line, the two-step line, the price table, the eight extremal rows —
are promoted vouched by nothing.

**Repair (exact).** Render the narrative from the payload rather than from live
locals: `say(fmt_row(R["incidence_summary"], nm))`, and add a
`G-TRANSCRIPT-NARRATIVE` leg that re-parses every numeral in the non-gate lines
of `body` and requires each to equal the payload leaf it names — the same
discipline `G-PAPER-CLAIMS` already applies to the paper's tables, applied to
the instrument's own. Cheapest sufficient fix: seal
`transcript_digest = bdigest(body)` and put it in the payload, so the two
artifacts bind each other.

### MAJOR-5 — `G-VERDICT-RECON` is not an independent route for 10 of the head's 30 numeral positions *(recurrence of DISC MAJOR-2, in reduced form)*

§13 and the gate statement both say the comparator *"reads only the receipt's
per-object censuses … and re-derives every number in the head by its own
arithmetic."* For 20 of the 30 positions that is exactly true and I verified it
by hand — the census tallies over `incidence_census`, `form_census`,
`inventory_census` and `fourth_direction` are a genuinely disjoint route, and
this is far better than the parent unit's `f(R) == f(R)`.

For the other **10** it is not. The comparator reads these straight from the
same payload keys the builder's own values were written to:

| head position | builder | comparator |
|---|---|---|
| segment 2 `{st}` 29791 | `len(L0) ** len(SHARED)` | `prep["states"]` |
| segment 2 `{bs}` 9 | `bestn` | `prep["best"]` |
| segment 2 `{zr}` 20100 | `cover[0]` | `prep["coverage"]` |
| segment 4 `{la}` 31 | `len(L0)` | `seam["lattice"]` |
| segment 4 `{ct}` 8 | `cutsizes[0]` | `R["cut_size"]` |
| segment 4 `{dr}` 0 | `ds_realises` | `R["ds_realises"]` |
| segment 4 `{dc}` 0 | `ds_in_cut` | `R["ds_in_cut"]` |
| segment 4 `{da}` 4 | `detrow[...]` | `detr[...]`, the same `extremal` row |
| segment 4 `{tv}` 1 | `len(twosided)` | `R["two_sided_values"]` |
| segment 4 `{os}` 1 | `len(matches)` | `R["one_sided_matches"]` |

Segment 4 is therefore 7/8 self-comparison.

**`INJ-07`** moved the one of the ten that is only weakly gated elsewhere:
`"selects after, most"` for the maximum-determinant row, `max(post)` →
`max(post) + 5`, with the paper regenerated alongside (the DISC MAJOR-2
scenario). `G-EXTREMAL`'s predicate is `detrow["selects after, most"] > 1`, so it
passes. Result: **exit 0**, the head publishes `THE SAME CRITERION IS 9-VALUED`
against a true value of 4, and `G-VERDICT-RECON` reports

```
{"equal": true, "first_difference": null}
```

The gate whose whole purpose is to be the independent route agrees with the
corruption.

**Repair (exact).** Derive all ten in the comparator from the primitive tables
that are already in the receipt: `len(R["extremal"])` for the functional count;
the max-determinant row located by `max(r["selects after, most"] …)` over
`extremal` is still the same object, so instead publish the per-functional
post-event fibers as a table and have the comparator take the maximum itself;
publish the cut census as a per-index table (`{index: surviving}`) and let the
comparator compute `cut_size`, `ds_in_cut`, `ds_realises`, `two_sided_values`
and `one_sided_matches` from it; publish the completion lattice's own row count
and the shared-site count so `states = lattice ** shared` is re-derived. Then
correct §13's "every number" to the measured split, or make it true.

### MAJOR-6 — the pre-registration is re-declarable post-hoc *(recurrence of DISC MAJOR-4, verbatim)*

The two outcome words are Python literals built at `full_run` line 2310 —
**after every measurement in the unit**. `G-OUTCOME-FEASIBILITY` binds the two
*witnesses* (`== n_groups`, `== span`) and the booleans' type, and binds nothing
about the words or the stated reasons. Nothing ties either to
`v15/note-autoglue-pin.md`, which is hash-pinned at `88c04df52c19` and already
read through the anchor accessor.

| injection | edit | result |
|---|---|---|
| `INJ-08` | `"BLOCKED-AT-THE-DECLARED-DATUM"` → `"AUTONOMOUS-DYNAMICS-ESTABLISHED"`, reason replaced by an explicit admission of post-hoc selection — **code only** | dies at `G-PAPER-CLAIMS` (`TBL-OUTCOMES` no longer matches) |
| `INJ-18` | the same edit with the paper's `TBL-OUTCOMES` row regenerated alongside | **exit 0, 42/42 PASS** |

The delivered receipt then carries, as a *pre-registered outcome*:

> `AUTONOMOUS-DYNAMICS-ESTABLISHED` — *"the outcome word was picked after the
> census was read, from whichever reading made the answer come out"*

§2.3's "a verdict either way was available before anything was measured" is
carried by the rendered table alone, i.e. by an author who does not regenerate
the paper.

**Repair (exact).** Move the two outcome words and their feasibility reasons
verbatim into the pin, and add them to `VERBATIM` as PARSED anchors whose
consumer is `G-OUTCOME-FEASIBILITY`, gating each string against the pinned
bytes — the mechanism this unit already uses nine times and uses well. Add
`INJ-18` as a recipe requiring `G-OUTCOME-FEASIBILITY` to die.

### MAJOR-7 — `T-FALSIFIER-POISONS` is carried in name: no move-proof by digest exists anywhere in the instrument *(recurrence of CONTRACT MAJOR-3 / TPL-2 "carried-not-used families forbidden")*

Three places say the move is proved:

- `FAMILIES["T-FALSIFIER-POISONS"]`: *"every falsifier **moves its named target
  by digest** and dies at its declared gate"* — and this string is published in
  the receipt at `families.roles`.
- `class Falsifier`'s docstring: *"the harness **proves the move by digest** and
  requires death at the declared gate, not before."*
- the module docstring, TPL-2 clause: *"falsifier **move-proofs taken by
  digest**."*

`G-FALSIFIER-HONESTY` checks four things: that the literal string `mut("NAME")`
or `pick("NAME"` occurs in the file; that `f.gate` is in the declared gate set;
that `target` and `description` are non-empty; and that no recipe body is a bare
boolean assignment (the sentinel scan, which is a good check and finds 0).
**No digest of any target is taken. There is no harness.** `FALSIFIERS` is
otherwise iterated only to build the coverage set and by the two `--list-*`
printers. `WAIVERS` is empty, so nothing is even declared as exempt.

The consequence is that the unit's headline claim — 44 recipes each dying at its
own gate — is, inside the delivered run, an unexecuted assertion. It happens to
be **true**: I ran all 44 out of harness, one process each, and 44/44 die
exactly as declared. But the instrument does not know that, and a recipe that
silently stopped moving its target would publish `template families 9` and
`G-FALSIFIER-HONESTY :: PASS` forever. This is the family-satisfied-by-text
disease the two prior reviews both raised, in the one unit that declares the
family natively.

**Repair (exact).** Add the harness the docstring describes, in `--selftest`:
for each `f in FALSIFIERS`, run `full_run` under `MUTANT = f.name` with
`WRITE = False`, require a `GateFail` whose `.check == f.gate`, and — the move
half — take `digest()` of the payload key `f.target` names before and after and
require it to differ. Publish `moves_proved` and `deaths_at_declared_gate` as
measured counts and gate them at `len(FALSIFIERS)`. If the full sweep is too
slow for a delivery run, gate it in `--selftest` and say so in §13 and in
`FAMILIES` rather than claiming it of the delivery.

---

## 5. MINORS

**m1 — the read-set gate fires fourth-from-last; the tail window is open.**
*(E-33, recurrence of DISC MINOR-5.)* `G-READ-SET` is followed by
`G-SEAL-TOTAL`, `G-TRANSCRIPT-BOUND` and `G-INTEGRITY`. `INJ-04` planted
`read_text("v14/TEMPLATE.md")` — an undeclared repo file — as the first line of
`promote()`: **exit 0**. The same read placed before the gate dies, so the hook
is sound and only the ordering is wrong. Sharper than at DISC: `FAMILIES`
publishes *"reads … gated **after the last gate**"*, and it is not; and the
delivery path's own `open()` calls on `autoglue_output.txt`,
`autoglue_receipt.json` and both `.tmp` staging files are themselves logged
after the gate that would have judged them. *Repair:* re-check the read log
inside `promote()` after `G-INTEGRITY`, with the artifact paths and the two
`.tmp` paths declared as exemptions.

**m2 — the I/O accessor is REPO-scoped, so a read outside the repo is
invisible.** `Reads.install`'s hook keeps only paths under `REPO`. `INJ-05`
opened `/etc/hosts` mid-run and read it: **exit 0**, `distinct_paths` unchanged.
§2.1's *"every `open` this run performs is seen whoever calls it"* is false as
written. *Repair:* log every path and classify, rather than filter — record
out-of-repo reads under an `EXTERNAL` bucket that must be empty.

**m3 — the TPL-2 integer-offset subspecies is ungated at the registry door.**
*(recurrence of DISC MINOR-3.)* `Meas.audit` walks `stmt`, `gate`, `claim`,
`fence` and `segment` arguments; it does not walk `Meas.m`. `INJ-06` wrote
`M.m("n_walls", len(WALLS) - 6 + 11, "the declared walls")`: **exit 0**, and the
receipt publishes `measured.n_walls = 11` with provenance *"the declared walls"*
against six walls in `receipt.walls`. Harm is bounded only because gate
statements reach neither artifact (m7). *Repair:* add `m` to the audited call
names and flag any `ast.BinOp` with an int `ast.Constant` operand in its value
argument — the leg already exists two lines away.

**m4 — `G-DETERMINISM`'s first leg is a literal token scan over a line-text
whitelist.** `repr_lines` is the set of stripped source lines containing the
substring `key=repr`, and `SAFE_REPR_SORTS` whitelists eight exact line texts.
Two consequences, both measured: `INJ-02` added a new function whose body is a
verbatim copy of an already-whitelisted line — invisible, because `repr_lines` is
a **set** (**exit 0**); and `INJ-21` replaced `ekey` with `(len(e), hash(e))`, a
hash-seed-dependent key carrying no `key=repr` token, which **passed
`G-DETERMINISM`** and ran on to gate 33. Credit where due: the gate's *second*
leg is real and caught my first attempt — `INJ-01` set `ekey` to `repr(set(e))`
and died on `shuffle_ok`. And I could **not** produce seed-divergent artifacts:
`INJ-21` was stopped downstream at `G-PAPER-CLAIMS`, and `INJ-22`, which added a
`hash()` tiebreak to the incidence census sort, was vacuous (the sort key is
already total — both seeds reproduced `34606049f1ef`). So the gate is weaker
than its statement, the harm is currently unrealised, and the claim *"a gate
reads the source to prove no other exists"* should be narrowed to what it does.
*Repair:* replace the substring scan with an AST leg — flag any `keyword(arg=
"key")` whose value is `Name('repr')`, an `Attribute` ending `.repr`, or a
`Lambda` whose body calls `repr`; and whitelist by `(function, lineno)` rather
than by line text.

**m5 — CLI mode resolution is last-wins with no conflict detection.**
*(CONTRACT MAJOR-9 residue.)* The argv loop is a genuine improvement — every
position is whitelisted, `--bogus`, `--run`, `--mutant NOPE`, `--list-gates
extra` and a bare `--verify-paper` all exit 2. But flags silently override each
other:

| argv | rc | effect |
|---|---|---|
| `--selftest --numbers` | **0** | `--selftest` **silently discarded**; a battery reads exit 0 as a passed selftest |
| `--mutant MUT-ARENA --list-gates` | **0** | the mutant is silently discarded; prints the gate list |
| `--mutant MUT-ARENA --mutant MUT-SEAL` | 1 | last wins; dies at `G-SEAL-TOTAL`, attributed to the wrong recipe |
| `--list-families --list-mutants` | 0 | prints mutants |

*Repair:* track which mode flag set `mode` and return `None` (rc 2) on a second
one; reject a repeated `--mutant`.

**m6 — `Claims.claim` is never called, and the receipt publishes the result of a
check that never ran.** `self.prose` is empty at every run, so `prose_bad` is
unconditionally `[]`, and `receipt.paper_report.prose_mismatch: []` reads as
*prose claims were compared and none mismatched*. Carried-not-used, TPL-2.
*Repair:* use it — MAJOR-1's repair (b) is exactly this — or delete the method
and the key.

**m7 — gate statements reach neither artifact.** *(recurrence of DISC NOTE-2.)*
`R["ledger"]` keeps `gate`, `passed`, `evidence`, `chain` and drops `statement`;
the transcript prints only `[PASS] <name> <chain>`. Every `M.stmt(...)` — where
most of this unit's self-description lives, including the sentences MAJOR-3 and
MAJOR-7 quote — is unpublished, so a reader cannot check the instrument's claims
against either artifact. *Repair:* add `statement` to the ledger rows in the
receipt.

**m8 — `MUT-READ`'s target is an undeclared file whose existence is
unchecked.** The recipe calls `read_text("RUNBOOK.md")`. In a tree without that
file the process dies with a raw `FileNotFoundError` traceback at rc 1, not at
`G-READ-SET` and not as a ledger row — the CONTRACT MAJOR-8 `INJ-17` shape. In a
full tree it refuses correctly. *Repair:* have the recipe open a path it creates,
or one of the pinned sources under a second, undeclared alias.

**m9 — `--verify-paper` on any path outside the repo always dies at
`G-READ-SET`.** `main` falls back to the raw path when `full` is not under
`REPO`, so the declared read set can never contain it: `--verify-paper
/tmp/anything.md` reports `declared_never_read` regardless of content. The mode
works correctly on in-tree relative paths. *Repair:* exempt an out-of-repo paper
path explicitly, or reject it at rc 2 with a usage message rather than failing a
family gate.

---

## 6. INJECTION LEDGER (23 designed, one process each, all off-tree)

| # | injection | target | result |
|---|---|---|---|
| 01 | `INJ-01-EKEY` | `ekey` → `repr(set(e))` | died `G-DETERMINISM` (shuffle leg) |
| 02 | `INJ-02-WHITELIST` | duplicate a whitelisted repr-sort line | **exit 0** (m4) |
| 03 | `INJ-03-NARRATIVE` | forged census row in the transcript | **exit 0** (M4) |
| 04 | `INJ-04-READ-AFTER` | undeclared repo read inside `promote()` | **exit 0** (m1) |
| 05 | `INJ-05-READ-OUTSIDE` | `/etc/hosts` read mid-run | **exit 0** (m2) |
| 06 | `INJ-06-TYPED-DOOR` | integer offset at `Meas.m` | **exit 0** (m3) |
| 07 | `INJ-07-RECON-SHARED` | max-det post-fiber 4 → 9, paper regenerated | **exit 0** (M5) |
| 08 | `INJ-08-PREREG` | outcome word rewritten, code only | died `G-PAPER-CLAIMS` |
| 09 | `INJ-09-P-256` | §4.2 `256`/`512` → `8`/`4` | **exit 0** (M1) |
| 10 | `INJ-10-P-288` | §11 `108 of the 288` → `288 of the 288` | **exit 0** (M1) |
| 11 | `INJ-11-P-IDENTICAL` | §5.1 disjoint → *one and the same* | **exit 0** (M1) |
| 12 | `INJ-12-P-NOTAUTO` | §1 NOT-AUTONOMOUS deleted and inverted | **exit 0** (M1) |
| 13 | `INJ-13-P-WALLS` | six unlicensed paraphrases from the disease | died `G-WALL-SEAMCONFINED`, all six walls fired |
| 14 | `INJ-14-P-REFERENT` | cross-universe plant *108 of the 162* | died `G-PAPER-REFERENT` |
| 15 | `INJ-15-P-TRANSPLANT` | one cell moved between census tables | died `G-PAPER-CLAIMS` |
| 16 | `INJ-16-P-LICENSED` | five licensed breaches + one unlicensed | died `G-WALL-SEAMCONFINED` (only `WALL-DECLARATION` fired; the other five passed) |
| 17 | `INJ-17-DET-LIVE` | lambda-wrapped `key=repr` | died `G-DETERMINISM` (token present) |
| 18 | `INJ-18-PREREG2` | outcome word rewritten, paper regenerated | **exit 0** (M6) |
| 19 | `INJ-19-POSTCLOSE` | sealed value edited after the last gate | **exit 0** (M2) |
| 20 | `INJ-20-P-LICENSED6` | six licensed breaches, one per wall | **exit 0**, all six walls `ok: true` (M3) |
| 21 | `INJ-21-DET-HASH` | `ekey` → `(len(e), hash(e))` | passed `G-DETERMINISM`; died `G-PAPER-CLAIMS` (m4) |
| 22 | `INJ-22-DET-RECEIPT` | `hash()` tiebreak on the census sort | vacuous — sort key already total; both seeds `34606049f1ef` |
| 23 | `INJ-23-P-216` | §3 *CROSS-ONLY reaches 216 of 288* → *288 of 288* | **exit 0** (M1) |

Plus the 44-mutant sweep (44/44 at declared gates), a 19-invocation hostile argv
battery, six read-only modes checked by whole-tree hash, and an in-process
six-wall licence probe.

---

## 7. WHAT I COULD NOT BREAK

- Any delivered number. The 108, 216, 162, 288, 455, 468, 29791, 20100, 9, 77,
  31, 8 and the 0-overlap all re-derive from the receipt's per-object censuses.
- The anchor family. Nine anchors, one accessor, consumption verified against
  gates that ran, operands parsed out of the anchors' own bytes; the parent's
  216 and 288 are read out of the parent's sentence and never typed.
- The referent pair mechanism, against a cross-universe plant.
- The two-way keyed table multiset, against a transplant.
- The unrendered-table check, the fence multiplicity, the seal partition, the
  totality-at-the-door recomputation, the coverage denominator's inclusion of
  the gates that fire after it, the sentinel scan, the `G-NO-POSTHOC` rule-body
  scan, and the equivariance and blindness legs.
- Byte reproduction, under two hash seeds, off-tree, from artifact-deleted
  trees.

## 8. REPAIR ORDER, SUGGESTED

1. **M2** (post-close seal) — serialise then verify. One function move.
2. **M7** (falsifier move-proofs) — build the harness or narrow all three claims.
3. **M3** (wall licences) — delete the bare negations, add 30 negation-controls.
4. **M1** (paper headline) — split the reflexive pairs, register the five prose
   sentences as claims via the already-built `C.claim`.
5. **M4** (transcript narrative) — seal a transcript digest into the payload.
6. **M6** (pre-registration) — move the outcome words into the pin as anchors.
7. **M5** (comparator independence) — publish the primitive tables segment 4
   needs, or narrow §13.
8. m1–m9 in place; m3, m5 and m6 are one line each.

Every finding above is a candidate reading until adjudication.
