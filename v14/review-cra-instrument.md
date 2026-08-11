# CR-A HOSTILE REVIEW — SEAT K3, THE INSTRUMENT LENS

**Unit under review:** CR-A, paper-05-accumulation (v14 ledger #41, delivered
and committed as-is 2026-08-09 at `94df5ad`; adjudicator-verified #44).
**Protocol:** v14 ledger #174, row K3 — the era audit at BIRTH-DATE FAIRNESS
(the U4b precedent).
**Objects, sha256-12, verified against the tree at review start and again at
review end:** `v14/paper-05-accumulation.md` `af0058432b79`;
`v14/code/cra_accumulation_exact.py` `e289d3afc852`;
`v14/code/cra_accumulation_output.txt` `f398959da079`;
`v14/code/cra_accumulation_receipt.json` `5f68bac811bd`;
pin `v14/note-cr-batch-pins.md` `1cfee4fc0891`.
**Repo writes by this seat:** this file only. No LOG/STATUS/RUNBOOK edit. All
execution in
`…/scratchpad/cra-in/`. Git read-only throughout.

---

## GRADE: **AWF** — ACCEPT WITH FIXES

The measured content is clean. Off-tree and git-less byte-identity reproduces
both committed artifacts exactly; 39 of 39 declared mutants die at exit 1 at
their **declared** gate with artifacts byte-unchanged, and — re-measured
outside the selftest harness — **39 of 39 are correctly attributed**, so the
receipt carries no false waiver; the paper↔output↔receipt sweep found **zero
false numbers** across 109 value-level checks. The verdict apparatus is ahead
of its era.

Two defects are judgeable **at CR-A's own era** and are held against it
(MAJOR-1, MAJOR-2). Both are exactly liftable. Everything else this seat found
is **seam**: the price of an instrument generation that ended before the seal
era, measured and reported, not charged.

**Executions:** 72 top-level CLI invocations + 39 exactly-counted nested
selftest subprocesses + ≈51 nested runs inside three deliberately-killed
selftests ≈ **162 instrument executions**.
**Recomputations / independent comparisons:** **373**
(109 paper↔output↔receipt value checks; 19 resolution recomputations;
45 gate-predicate vacuity classifications by AST; 43 run-mode-branch locus
classifications; 78 gate/anchor never-falsified set-membership decisions;
39 mutant declared-vs-actual attributions; 14 blockquote coverage
classifications; 26 artifact-hash comparisons across 13 runs), plus a separate
10,000-point measurement of the paper-number sweep's admission set.

---

## 1. WHAT THE ERA WAS

CR-A's pin froze at v14 #30; its four artifacts were committed at #41
(`94df5ad`, 2026-08-09 17:38:48). The RUNBOOK at that commit carried every
engraving through **#34** — including, added the same day and therefore
binding on this unit, *"waiver claims are gate claims"* and *"verbatim-text
anchors adopted"*. `git diff 94df5ad -- RUNBOOK.md` is exactly **twelve
engravings**, all later:

| # | engraving | in force at birth? |
|---|---|---|
| #46 | no unanchored runtime inputs | no |
| #62 | verbatim-text anchors, corrected spec | no |
| #62 | provenance by committed sha | no |
| #82 | the CLI-contract minimum | no |
| #82 | comparator independence, strengthened | no |
| #87 | gates bind objects, not cardinalities | no |
| #91 | no moving refs + off-tree/git-less byte-reproduction | no |
| #119 | the gate-to-disk seal | no |
| #125 | text gates match text as written | no |
| #148 | the seal manifest is total | no |
| #160 | the v10-layer tie-break gate | no |
| #168 | paper coverage includes fenced blocks | no |

**The fairness ruling of this seat:** CR-A is judged against the first column
of that table's complement — everything through #34 — and the twelve rows above
are measured, reported, and **not held against it**. Where the unit
nevertheless satisfies a later rule, that is recorded as credit.

---

## 2. THE BASIC BATTERY AT ITS ERA

Run on a scratch tree containing only the five pinned files plus `RUNBOOK.md`
— **no `.git`, no repository, outside the tree.**

| test | result |
|---|---|
| plain run, off-tree + git-less | exit 0, 23.9 s, 47 gates / 31 anchors / 0 failures |
| byte-identity vs committed | `f398959da079` / `5f68bac811bd` — **exact, both artifacts** |
| `--selftest` | exit 0, **39/39 DIED-CORRECTLY**, artifacts byte-unchanged, writes nothing |
| mutant attribution (re-measured outside the harness) | **39/39 correctly attributed, 0 misattributed** |
| hostile argv, 17 cases | 0 artifact movements; exit 2 on every unknown leading token |
| soft gates | **none** — all 47 gates are must-pass |
| gate predicate vacuity (AST, 45 call sites) | **1 tautology found** (MAJOR-1) |
| gate-registering functions reading run-mode identity | **0** — independently confirmed by my own AST pass |

The #91 byte-reproduction leg — *off-tree AND git-less* — **passes at birth,
before the rule existed.** That is the strongest single result in this audit.

### The CLI verdict at its era: CONFORMANT, and ahead of it

At birth the standing rule was v13 #238 (confirm the argv handler in source
before invocation). I did that first: the handler is a four-branch whitelist at
lines 2975–2999. The #82 CLI-contract minimum did not yet exist, yet CR-A
already ships all four of its limbs — argv whitelist with exit 2, a real
`--selftest` that hashes both artifacts before and after and writes nothing,
`--mutant NAME` with exit 2 on an absent or unknown name, and
`--list-mutants`.

It misses the #82 minimum on **one** point, and #82's own text names it:

> `--selftest EXTRA`, `--list-mutants EXTRA`, `--mutant NAME EXTRA` and
> `--mutant NAME --selftest` all **silently ignore the trailing tokens**.

Only the leading token is whitelisted (`argv[:1] == [...]`, then `argv[1]`,
with `argv[2:]` unread). Artifacts never moved in any of the 17 cases. This is
seam, not charge (MINOR-1).

---

## 3. THE INJECTIONS TABLE — THE SEAM, MEASURED

Every row is a patch against a scratch copy, run to delivery. **"artifacts"
compares the delivered bytes against the committed `f398959da079` /
`5f68bac811bd`.**

| # | injection | where | exit | gates | artifacts | caught? |
|---|---|---|---|---|---|---|
| INJ-1 | **post-gate head flip** — `verdict` → `CRA-RESCALED-CONVERGES` after the last gate | source, before the write | **0** | 47/47 | both moved; **the flipped head is published in `output.txt` AND `receipt.json`** | **NO** |
| INJ-2 | **census-row move** — `census.admissible` 1232→1, `advancing`→1, `class_iii`→1, `commuting_advancing`→7 | source, after the last gate | **0** | 47/47 | **`output.txt` BYTE-IDENTICAL to committed**; receipt's census table now contradicts its own verdict string and its own rendered prose | **NO** |
| INJ-3 | **post-write corruption** — rewrite both artifacts on disk after `json.dump` | source, after the write | **0** | 47/47 | both moved; head flipped, `admissible: 7` | **NO** (by construction — nothing runs after the write) |
| INJ-4 | **control-under-label** — the compliance row "RUNBOOK 14 (symmetry self-test)" retargeted from `G-CHART-ACTION-NONTRIVIAL` to `G-FLOATGUARD` | source | **0** | 47/47 | `output.txt` byte-identical; receipt asserts the symmetry self-test is discharged by the float guard | **NO** — `G-COMPLIANCE-CLAIMS-ARE-GATE-CLAIMS` tests name-membership only |
| INJ-5 | **false waiver** — `float-leak`'s `expected_gate` retargeted at `G-CENSUS-TWO-ROUTES-BIL` | source | **0** | 47/47 | never-falsified census silently trades `G-CENSUS-TWO-ROUTES-BIL` out for `G-FLOATGUARD`; **the count stays 42**, so a count check is blind | **plain run: NO. `--selftest`: YES** |
| INJ-6 | **paper table column swap** — §4 LIN/BIL `admissible` and `probe cells` exchanged (1209↔23, 1010↔809) | paper | **0** | 47/47 | **BOTH BYTE-IDENTICAL TO COMMITTED** | **NO** — every swapped number is in the receipt's token set |
| INJ-7 | **theorem polarity flip** — §6 "Then **NO** admissible advancing mover … commutes" → "Then **SOME** …" | paper | **0** | 47/47 | **BOTH BYTE-IDENTICAL TO COMMITTED** | **NO** — no numeral changed |
| INJ-8 | **the paper's own verdict block** — `COMMUTING-ADVANCING=0-AT-9-OF-11-RULES` → `=4-…` | paper | **0** | 47/47 | **BOTH BYTE-IDENTICAL TO COMMITTED** | **NO** — `4` is in the receipt's token set |
| ENV-1 | `RUNBOOK.md` absent from the tree | environment | 1 | — | none written | uncaught `FileNotFoundError` traceback, **not a gate** |
| ENV-2 | one engraving paragraph **re-wrapped by one word** in `RUNBOOK.md` | environment | 1 | — | none written | **YES**, `G-ENGRAVINGS-PRESENT` — but see MINOR-2 |
| ENV-3 | `RUNBOOK.md` grown by the twelve later engravings (the actual repo today) | environment | 0 | 47/47 | **byte-identical** | n/a — presence is monotone under append |

**Eight surviving injections. Three of them (INJ-6/7/8) leave both delivered
artifacts byte-identical to the committed ones** — a reader auditing by
"exit 0, 47/47 green, artifacts byte-match" gets a full green light while the
paper states the inverse of the theorem, the inverse of the §4 census, or a
verdict its own receipt contradicts.

**Seam width.** Of the twelve later engravings: **six bite** (#46, #62, #82,
#87, #119/#148, #125); **three are already satisfied at birth without the rule**
(#91's byte-reproduction leg, #168's substance — the paper has no fenced code
blocks and the sweep reads the whole file, #62's byte-anchor core); **three are
not applicable** (#160 — no v10 layer; #82's comparator-independence
strengthening is satisfied in substance, see §5; #148 is subsumed by #119
here). **Every one of the eight surviving injections requires write access to
the source or the paper. None changes a measured number, and none is reachable
from the pinned inputs.** CR-A's verdict does not depend on any of them.

---

## 4. FINDINGS

### MAJOR-1 — the never-falsified census is short by three, and its gate is a tautology *(judged AT ITS ERA)*

`G-NEVER-FALSIFIED-CENSUS` (line 2737) has the predicate

```
isinstance(never, list)
```

and `never = sorted(set(allg) - killed)` is unconditionally a list. **The gate
cannot fail.** It is one of the 47 must-pass gates the paper counts.

Worse, `allg` is built from `R["gates"]` — the live `GATES` list — **before the
run's last four gates register**. Measured:

- true never-falsified set at the full denominator (47 must-pass gates ∪ 31
  anchors, minus the 33 distinct declared `expected_gate` names): **45**
- what the receipt publishes: **42**
- omitted, each an unfalsified must-pass gate:
  `G-NEVER-FALSIFIED-CENSUS`, `G-DEFERRED-GATES-EVALUATED`, `G-FINAL-COUNTS`

The paper's §11 table row "never-falsified gates and anchors | 42, named in the
receipt" therefore understates the unit's own honest denominator. The pin
(#30) required a never-falsified census in the receipt "from delivery one", and
#34 — engraved *before* this commit — makes a census entry a gate claim. This
is CR-A's era, and the finding stands.

*Not a false number:* 42 is the correct cardinality of the set the code
computes. The defect is the denominator that set is computed over, and the
tautological gate that fails to notice.

**Repair R-CRA-I2 (≈6 lines).** Seed `allg` with `DEFERRED_GATES`; replace the
predicate with `set(never) == (set(mp_gates) | set(anchor_names)) - killed`
and a hard `len(never) == 45`; add one mutant that drops a name from the
census.

### MAJOR-2 — §11's coverage sentence is false as written *(judged AT ITS ERA)*

The paper claims, in §11:

> "Every numeric sentence quoted in blockquote form above is rendered by the
> instrument from the receipt object and gated to appear verbatim in this file."

Measured over the paper's 14 blockquote passages:

| blockquote | lines | numerals | rendered from the receipt? |
|---|---|---|---|
| **the verdict block** | 13–19 | **17** | **NO** |
| §1 frozen-geometry | 68 | 4 | yes |
| §4 census | 151 | 3 | yes |
| §5 C-FROZEN source quote | 175–177 | 0 | n/a |
| §5 forced set | 181 | 2 | yes |
| §5 per-link stabilizer | 194 | 4 | yes |
| §6 closure fiber | 249 | 4 | yes |
| **§6 Theorem (static geometry)** | 262–269 | **2** | **NO** |
| §6 two-route commutation | 299 | 2 | yes |
| §7 trajectories | 341 | 7 | yes |
| §7 normalization | 363 | 2 | yes |
| §7 mover-blind limit | 379 | 2 | yes |
| §8 foreign control | 416 | 3 | yes |
| §9 discriminator | 438 | 2 | yes |

**Two of thirteen numeral-bearing blockquotes are not rendered and not gated —
and one of them is the paper's own verdict, carrying 17 numerals, the
highest-stakes numerals in the document.** INJ-7 and INJ-8 exploit exactly
these two, at exit 0 with byte-identical artifacts.

The mechanism's weakness is separately measured. `G-PAPER-NUMBERS-IN-RECEIPT`
is a **set-membership test with no position, no polarity and no per-claim
binding**:

- paper numeric tokens swept: **191 (58 distinct)** — the whole file, fenced
  blocks included (there are none), so #168's blindness does not apply here
- of the 58 distinct tokens, **27** are pinned by a rendered prose sentence and
  **31 are token-checked only**
- the admission set derived from the receipt admits **85 of the integers
  0–9999**, including **43 of 0–99** and **71 of 0–999** — permissive enough
  that INJ-6's four-way column swap and INJ-8's `0`→`4` both pass
- the token regex `(?<![\w/.-])\d+(?:/\d+)?(?![\w.-])` **cannot see negative
  fractions at all**: `(1/27, -1/54, 1/27)` tokenises as `['1/27','1/27']`, so
  the paper's headline limit value `-1/54` is outside the sweep entirely

The unit's own §11 sentence is the claim under test, and it is not true of the
delivered paper. #20 ("prose renders from the receipt") was in force at birth
and the unit implements it well for eleven sentences; the false part is the
word *"Every."*

**Repair R-CRA-I3 (paper + ≈20 lines).** Render the §4/§5/§6 tables, the §6
theorem sentence, and the verdict block FROM the receipt; gate them verbatim
under whitespace + markdown-prefix normalisation (#125's form); then rewrite
§11's sentence to the coverage actually achieved. Kills INJ-6/7/8.

### MAJOR-3 — no gate-to-disk seal *(SEAM — measured, NOT charged)*

`deliver()` ends with two bare `open(…,"w")` calls. There is no staged write,
no `os.replace`, no gate-time digest of the published object, and no
disk-vs-seal integrity check. INJ-1, INJ-2 and INJ-3 all deliver at exit 0
with 47/47 green.

**In mitigation, and it matters:** the unit implements its era's version of
this protection *faithfully and well*. `G-RENDER-FROM-GATED-OBJECT` digests
nine named tables before and after `post_gate_injection()` and compares — that
is precisely the v14 #10 window — and two declared mutants (`traj-corrupt`,
`limit-typed`) die there, confirmed in my attribution pass. The unit's
protected window simply **ends where #119's begins**: it closes the gap
between the gates and the render, and #119 closes the gap between the render
and the disk. #119 postdates CR-A by 78 ledger entries, #148 by 107.
**Not held against the unit.**

**Repair R-CRA-I1 (≈15 lines), only if modernisation is ordered.** Digest every
published key into a TOTAL manifest at gate time; write staged from the sealed
objects via `os.replace`; final gate compares DISK BYTES against the gate-time
seal (never a re-derivation). Add three mutants: post-gate head flip, post-gate
table move, post-write byte edit.

### MINOR-1 — CLI trailing-argument slop *(SEAM)*

See §2. Four subcommand forms silently ignore trailing tokens. Zero artifact
movements across 17 hostile cases. **R-CRA-I5 (≈10 lines):** reject any argv
beyond the declared arity; add three hostile-argv cases to the selftest.

### MINOR-2 — `RUNBOOK.md` is an unpinned runtime input, and the run is hostage to its line wrapping *(SEAM)*

`read_text("RUNBOOK.md")` at line 1443 is the **only** repository read not
covered by a hash anchor: `SRC_ROWS` pins five files, and RUNBOOK is not among
them. Its product *is* consumed by a gate (`G-ENGRAVINGS-PRESENT`), so the
#91 "products gated" half is satisfied; the "pinned shas" half is not. Three
measurements:

- **ENV-3:** RUNBOOK has in fact grown by twelve engravings since birth and the
  run still byte-reproduces — presence is monotone under append, and no
  RUNBOOK byte reaches the artifacts. **Exposure to verdict-flip: none.**
  This is materially better than the R3 M1 class.
- **ENV-1:** with RUNBOOK absent, the delivery dies on an uncaught
  `FileNotFoundError` traceback rather than a named anchor. A recipient
  reproducing from the five pinned files alone cannot run the unit.
- **ENV-2:** the eight `ENGRAVING_ROWS` quotes embed RUNBOOK's **hard line
  breaks**. Re-wrapping one engraving paragraph by one word — a cosmetic edit
  to an append-only file CR-A does not own — kills the delivery at exit 1.
  **CR-A's reproducibility is hostage to the line wrapping of a file it does
  not pin.**

**R-CRA-I4 (≈8 lines):** either add RUNBOOK as a sixth `SRC_ROWS` entry at a
declared sha, or (better, per #62-provenance) carry the eight engraving texts
as the unit's own frozen declaration with the RUNBOOK sha as provenance, and
drop the read.

### MINOR-3 — the source's run-mode-locality comment is false

Lines 355–358 assert: *"EVERY run-mode branch in this file lives in one of
these helpers; none of them registers a gate or an anchor."* Measured by AST:
**22 of the 42 real `MUTANT` branches live outside the declared accessor block
(lines 360–501)** — in `float_guard`, `post_gate_injection`, the weight memo,
`build_verdict`, `rebuild_verdict_from_receipt`, `render_prose` and eight
measurement routines.

The **paper's** claim is different and is TRUE: §11 says "no *gate-registering
function* reads `MUTANT`, a delivery-run flag, or `sys.argv`", and my
independent AST pass confirms **zero** functions both register a gate/anchor
and read `MUTANT`. The defect is confined to the source comment.
**R-CRA-I7 (2 lines).**

### MINOR-4 — a quoted string in §3 is not verbatim

§3 says the pinned answers are *"quoted verbatim and gate-verified against the
files on disk."* Of the eight gated clauses, three are reproduced in the paper
(`C-FROZEN`, `C-NOLAW`, `C-OPEN`) and **all three are faithful** modulo
whitespace and bold-marker normalisation. The fourth, presented inside
quotation marks in §3, is not:

- pinned source: `$n(x+e)-n(x)$`
- CR-A §3:      `$n(x+e) - n(x)$`

`G-CLAUSES-VERBATIM` verifies the **code's** copy against the source, never the
**paper's** rendering. The mechanism gap is #62/#125 and postdates birth; the
word *"verbatim"* is a claim at any era. **R-CRA-I3 covers it.**

### MINOR-5 — two aggregate-keyed gates *(SEAM, #87)*

- `G-VERDICT-SEGMENTS-FLIPPABLE` perturbs **every** receipt field for **every**
  segment index, so it proves each segment moves under a *global* perturbation,
  not that segment *i* tracks field *i*. A segment wired to the wrong receipt
  field would still pass.
- The never-falsified census is compared by **count** in the receipt
  (`counts.never_falsified: 42`), which is exactly why INJ-5's one-for-one
  trade is invisible to it.

**R-CRA-I6 (≈12 lines):** flip one field at a time and require exactly the
owning segment to move; and make the selftest compare the **identity** of the
failing gate rather than substring-test `expected_gate` against the whole of
stdout+stderr.

---

## 5. WHAT THE UNIT DOES BETTER THAN ITS ERA REQUIRED

Recorded because the adjudication needs both sides.

1. **Off-tree, git-less byte-identity at birth** — reproduced here from a
   scratch tree with no `.git`, both artifacts exact. #91 did not exist.
2. **39/39 mutants correctly attributed.** I re-ran every declared mutant
   outside the selftest and parsed the gate that actually raised. Zero
   misattribution ⇒ **zero false waivers**, the #34 failure mode that cost R6a
   twelve entries.
3. **All 47 gates must-pass; no soft gates, no silent caps.**
4. **The verdict apparatus.** Derived in-gate; complete-string equality (never
   containment) against `rebuild_verdict_from_receipt`, which takes a
   *different input* (the receipt object vs. a flat payload) and uses a
   *different construction* (string concatenation vs. `%`-formatting); all
   three registered heads shown reachable from the **same** derivation on
   synthetic payloads; every segment proved non-inert; five verdict-injection
   classes declared and all five killed. Under #82's *strengthened* comparator
   rule the shared segment-label literals would now be a seam item — under
   #10/#20, the standard at birth, this is full compliance and then some.
5. **verify-paper runs INSIDE the plain run** — both the prose gate and the
   number sweep, in `deliver()`, before the write. The #20 discipline honoured
   ahead of its formalisation.
6. **The precheck discipline (#314) is honoured**: the frozen-geometry
   observation gates which candidates are censused and is disclosed as
   X-PRECHECK; the verdict-naming facts are measured on the censused objects.
7. **Honest self-disclosure.** Deviations 9 and 10 name, in advance, the two
   never-falsified classes this seat would otherwise have found (the four
   source-hash anchor rows; the BIL gates sharing the LIN code path), and
   X-FORCED-CLAUSES names the three analytically-forced gates and pairs each
   with a per-link positive control that is *not* forced and does move.

---

## 6. PAPER ↔ OUTPUT ↔ RECEIPT SWEEP — **ZERO FALSE NUMBERS**

109 value-level checks. Every initial mismatch resolved to agreement:

- **11 rendered prose sentences** appear verbatim in both the paper and
  `output.txt` — 22/22.
- **The verdict**: the paper's seven-line blockquote reassembles to the
  receipt's string **exactly** under whitespace normalisation. (My first pass
  flagged it; the flag was my harness joining the wrapped lines without the
  break space. Paper correct.)
- **§4 census table** (hand-typed): LIN 4096/1752/1209/1010, BIL
  4096/1224/23/809, totals 8192/2976/1232, product 3888 — all 14 checks agree,
  and the family sums close (1209+23=1232, 1752+1224=2976).
- **§5 inventory** (0/0/1232, forced 2, per-link 262144/133120/4096) — 7/7.
- **§6 selectors** (2976/1232/4096/4/0/0/0, 9 of 11 rules, 2916 cells,
  0 disagreements, 4 closure members, 2 count-blind rules) — all agree. The
  paper's *"exactly three read-link sets"* is correct against the receipt's
  `read_link_table`: ∅ at `A-chart`/`B-chart` (2 rules), `{e₁,e₂}` at
  `A-axis`/`B-axis` (2 rules), all three links at the remaining 7. The receipt's
  `distinct_read_link_sets` stores only the two **nonempty** sets, matching the
  paper's own sentence "the measurement covers both nonempty sets."
- **§7 trajectories** (972/531/117/108/216, 27 classes, 216 flips, horizon 20;
  341 orbit nodes; the 90-cell blind class; recheck 648 cells at t=40 with 0
  disagreements) — all agree; the last four live in `s_frozen.orbit_nodes`,
  `trajectory_summary.limit_classes` and the `G-TRAJ-CLASSIFICATION-CERTIFIED`
  gate value respectively.
- **§8/§9** (1/1 foreign, 7 coupled, 36 pairs, 29 separated, 7 unseparated) —
  all agree.
- **§11 receipt table** (31 anchors, 47 gates, 39 mutants, 6 disclosures,
  0 failures; memo 138195 hits / 13140 misses / 486 bypasses / 486 fresh
  comparisons / 0 disagreements) — all agree. **The single exception is the
  "42 never-falsified" row: correct as a cardinality, short as a denominator —
  MAJOR-1.**
- **All 8 pinned clause quotes are verbatim in the pinned source** (8/8), which
  is what `G-CLAUSES-VERBATIM` asserts.

---

## 7. THE REPAIR LIST — LIFTABLE, PRIORITISED

For the adjudication to decide whether modernisation is worth ordering on a
unit that is superseded in spirit.

| id | repair | buys | size | priority |
|---|---|---|---|---|
| **R-CRA-I2** | never-falsified census: full denominator, non-tautological predicate, `len == 45`, one new mutant | closes **MAJOR-1** | ~6 lines | **P1 — era-judgeable** |
| **R-CRA-I3** | fenced/total paper coverage: render the §4/§5/§6 tables, the §6 theorem and the verdict block from the receipt; gate verbatim with #125 normalisation; correct §11's sentence and re-space the §3 quotation | closes **MAJOR-2** and MINOR-4; kills INJ-6/7/8 | paper + ~20 lines | **P1 — era-judgeable** |
| R-CRA-I1 | the gate-to-disk seal: total manifest at gate time, staged `os.replace` write, disk-vs-seal integrity gate, three new mutants | kills INJ-1/2/3 | ~15 lines | P2 — seam |
| R-CRA-I4 | pin `RUNBOOK.md` at a declared sha, or freeze the eight engraving texts as the unit's own declaration | removes the only unpinned runtime input and the line-wrap hostage | ~8 lines | P2 — seam |
| R-CRA-I5 | CLI: reject argv beyond the declared arity; three hostile-argv selftest cases | closes MINOR-1 | ~10 lines | P3 — seam |
| R-CRA-I6 | per-object binding: one-field-at-a-time segment flips; selftest compares the failing gate's identity | closes MINOR-5; kills INJ-4/5 in the plain run | ~12 lines | P3 — seam |
| R-CRA-I7 | correct the run-mode-locality source comment | closes MINOR-3 | 2 lines | P3 |

### This seat's recommendation on modernisation

**Order R-CRA-I2 and R-CRA-I3. Do not order I1/I4/I5/I6 unless CR-A is being
carried to publication.**

The reasoning is measured, not stylistic. Every one of the eight surviving
injections requires write access to the source or the paper; none is reachable
from the pinned inputs; none changes a measured number; and the verdict
`CRA-BLOCKED-AT-STATIC-GEOMETRY` does not depend on any of them — it rests on
the census, the choice inventory and the static-geometry theorem, all of which
this seat reproduced byte-for-byte and found unmoved. A full seal retrofit on a
unit whose named gap the Γ campaign has since filled buys process consistency,
not truth. The two P1 repairs are different: one is a false coverage sentence
in a delivered paper, and one is a receipt row that understates the unit's own
honesty. Those are cheap, and they are CR-A's own era.

---

## 8. HOUSEKEEPING

- **Repo hashes after this seat's work, re-verified:** `af0058432b79`,
  `e289d3afc852`, `f398959da079`, `5f68bac811bd`, pin `1cfee4fc0891`,
  `RUNBOOK.md` `cf92e511fe72` (unchanged across the whole review),
  `v13/code/ha_successor_receipt.json` `542b8735daf0`,
  `v13/paper-ha-successor.md` `f286ba10d2d9`,
  `v13/code/ha_successor_exact.py` `d44cb72f8ee9`. **All unchanged.**
- HEAD advanced `d55571d` → `afd7f96` during the review, and
  `v14/review-cra-effectus.md` / `v14/review-cra-operator.md` appeared:
  **concurrent workers, disclaimed.** This seat wrote one file.
- Between delivery and adjudication every headline is a candidate reading,
  including this one.
