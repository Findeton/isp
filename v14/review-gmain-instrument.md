# Γ-MAIN (paper-12) — HOSTILE REVIEW, REVIEWER R3 (INSTRUMENT LENS)

**Protocol:** `v14/note-gmain-r4-protocols.md` PANEL A, sha256-12
`a3a39813e5b5` (verified).  **Pin:** `v14/note-gmain-pin.md`
`8529ddc4a319` (verified).  **Object — all four delivery hashes
verified at open and re-verified at close:** paper `d85a629a9378`,
code `51c3b4cf3f3c`, output `b2b45be500b7`, receipt `974f36b1251a`.
**Interpreter:** `/opt/homebrew/bin/python3.13`.  All mutant and
injection work on scratch copies; one repo write (this file); no git
write; no import of the unit (subprocess execution only).

---

## GRADE: AWF — ACCEPT WITH FIXES

The physics artefacts are clean and reproduce exactly.  Two plain runs
byte-identical; the delivered `gmain_output.txt` reproduced
**byte-for-byte**; all 23 byte anchors and all 9 path-value anchors
independently recomputed with **zero mismatches**; and **zero false
numbers in 69 distinct hand-written prose numerals** — the campaign's
four-false-prose-numbers record is not extended here.  The delivered
head is honest and conservative: PARTIAL, with the failed link named,
and the arena declares as PRIMARY the readout that MISSES the targets.

The instrument's *self-certification* does not survive the audit.
"88 gates · 36 mutants · 36 killed · never-falsified 2 · unwaived 0 ·
ten engravings APPLIED" is true only under the unit's own coverage
predicate, which measures **naming, not reach**.  At the #34/#62
standards the honest denominator is **15 of 88 gates (17.0 %)**.
Three MUST gates — including **the pre-registered holonomy gate** and
**the settlement gate** — are analytically forced and cannot fail for
any input.  Two more take a hard-coded literal as their "measured"
input.  The gate the #10 engraving created compares the verdict
against a syntactic copy of itself: a recurrence of the
already-engraved #219/#20 disease, which §13 (v13 #313) makes a MAJOR
by default.  **Four proven-executed injections survive undetected**,
two of which move a delivered claim.  And the clean 36/36 sheet is
*contingent on the verdict coming out PARTIAL*: forcing the holonomy
link True makes the unit's own falsifier survive and three MUST gates
fail (INJ12).

Every finding is repairable without re-deriving any physics.  The unit
should not be marked terminal until the repairs are re-run and
re-reviewed; this is a substantial fix pass, not a cosmetic one.

---

## 1. EXECUTION LOG

| # | run | result |
|---|---|---|
| 1 | plain run 1 (scratch copy, write paths redirected) | exit 0; 101 `[PASS]`, 0 `[FAIL]`, 0 `ANCHOR-FAIL`, **36 `[KILLED]`, 0 `[SURVIVED]`**, 0 tracebacks |
| 2 | plain run 2 | **byte-identical** to run 1 (`out.txt`, `receipt.json`, stdout) |
| 3 | reproduction vs delivery | `gmain_output.txt` **byte-identical to the committed artefact**; `gmain_receipt.json` differs in **exactly one field**, `source_sha256` (`c8ca40e36b8b` = the scratch file's own hash) |
| 4–19 | 16 injection runs | §5 |

**Total: 18 full program executions.**  The protocol's "run all 36
declared mutants" is discharged by the plain runs themselves — all 36
rows are evaluated in-process on every run, each printed with its
named gate target, totals `mutants 36 / mutants_killed 36`, exit 0,
no tracebacks.  What cannot be done is running one in isolation (§2).

**The scratch patch, declared.**  The delivered file writes with
`open(os.path.join(REPO, 'v14/code/gmain_output.txt'), 'w')` and the
same for the receipt — hard-coded to the repo, unconditional, with no
`--dry-run` and no argv.  A reviewer cannot execute this unit without
clobbering the delivery.  The only change in every scratch copy is
those two string literals → `os.environ[...]`.  Line count, division
sites and float-literal count are unchanged, so the AST guard and
every emitted line are unaffected; the single receipt delta above is
the proof.

**Repo hashes re-verified after all work** — paper `d85a629a9378`,
code `51c3b4cf3f3c`, output `b2b45be500b7`, receipt `974f36b1251a`,
`RUNBOOK.md` `3781cbce4e42`, pin `8529ddc4a319`, protocol
`a3a39813e5b5`: **all unchanged**.  An 87-file pre/post snapshot of
`v14/*.md`, `v14/code/*` and `RUNBOOK.md` shows my only write is this
file.  (Other deltas in the snapshot are other reviewers' single-file
writes and a `v14/LOG.md` edit, none of them mine.)

---

## 2. THE CLI CONTRACT, IN CODE FIRST (the #238 discipline)

**`gmain_exact.py` has no input channel at all.**  AST scan of the
delivered source: `sys.argv` — **0**; `os.environ` — **0**;
`os.getenv` — **0**; `input()` — **0**.  No `--mutant`, no
`--list-mutants`, no `--selftest`, no `--dry-run`.

1. **Unknown flags are not rejected — they are unreadable.**  The
   Γ-prep disease in its maximal form: `gprep_foundation_exact.py`
   at least parses `ARGV = set(sys.argv[1:])`, and every other v14
   unit (`cra`, `crb`, `crc`, `crd`, `r3`, `r4`, `r6bp`) ships a
   `--mutant` harness.  This one accepts anything and does the same
   thing — the full delivery, overwriting the committed artefacts,
   exit 0.  No execution can differ, because no argument is read.
2. **There is no per-mutant execution path.**  The 36 "mutants" are 36
   `mutant(...)` rows evaluated inside the single delivery run.  No
   mutant is ever run against a *mutated program*.
3. **`mutant()` hard-codes `reaches_target=True`.**  The helper writes
   that field into every row without measuring anything, so the
   receipt serialises **36 unmeasured reach claims** — precisely what
   §14 (v14 #34) forbids: *"the named mutant must reach and be killed
   by the gate."*

---

## 3. THE COVERAGE AUDIT (K5, at the #34/#62 standards)

### 3.1 The claim under attack

`gmain_output.txt:330` prints, as the mutant section header:

> `MUTANTS -- every declared falsifier reaches its gate and dies by the gate's own predicate, evaluated blind`

**False for 18 of the 36 rows.**

### 3.2 The 36 declared falsifiers, classified by their `killed` expression

Extracted by AST (argument 4 of each `mutant(...)` call), then read.

**Class A — a mutated object is built and a predicate is re-evaluated
on it (18):** `MUT-ANCHOR-DRIFT`, `MUT-PATH-DRIFT`, `MUT-QUOTE-DRIFT`,
`MUT-LAYER-DRIFT`, `MUT-MISNORMALIZED`, `MUT-QUOTIENT-SCRAMBLE`,
`MUT-REC-CORRUPT`, `MUT-HOLONOMY-DRIFT`, `MUT-TARGET-DRIFT`,
`MUT-READOUT-SWAP`, `MUT-PRUNE-LAX`, `MUT-SCREEN-FLIP`,
`MUT-BLOCK-MERGE`, and the five `MUT-VERDICT-*` rows.

**Class B — the boolean measures the DELIVERED, unmutated object; the
mutation exists only in the prose `injects=` field (10):**

| row | `killed` expression | what it actually asserts |
|---|---|---|
| `MUT-BLINDNESS-FLIP` | `CNT1 != CNT2 and WGT1 == WGT2` | the delivered measurement |
| `MUT-LEG-PATTERN` | `('p','d','p','r') not in PAT1` | the delivered `PAT1` — the mutated `_lp` is built on the line above and **never used** |
| `MUT-F8-MECHANISM` | `_cmp_after_d == _tot_d and _cmp_after_n == 0` | the delivered measurement |
| `MUT-CK-CORRUPT` | `all(… CKR) and any(… _live)` | the delivered CK census |
| `MUT-PADDING-DROP` | `DIMS_M[1] != DIMS_M[2]` | a conjunct of `T4-PADDING`'s own predicate, unmutated |
| `MUT-CRB-COLLAPSE` | `not _crb_flat` | the delivered `CNT1 != CNT2` |
| `MUT-44-MERGE` | `len(_desc) == 44` | the delivered census |
| `MUT-RENEWAL-CORRUPT` | `len(_cols) == 1` | the delivered census |
| `MUT-SCRAMBLE-EQ` | `obstruction == 44 and closes == 1402` | the delivered carrier reading |
| `MUT-SETTLEMENT-LAX` | `not all(SETTLEMENT.values())` | that *this* run came out PARTIAL — see M8 |

Class B is not a theoretical worry: **INJ02 flipped three of these
rows to `[SURVIVED]` in a single run** (`MUT-BLINDNESS-FLIP`,
`MUT-READOUT-SWAP`, `MUT-CRB-COLLAPSE`), and **INJ12 flipped
`MUT-SETTLEMENT-LAX`** — because they read the delivered state, they
invert whenever the delivered state moves.

**Class C — tautologies, or properties absent from the named gate's
predicate (8):**

| row | `killed` expression | why it cannot fail |
|---|---|---|
| `MUT-WAIVER-FALSE` | `all(g['name'] in {x['name'] for x in GATES} for g in GATES)` | every name is in the set of names — **true for every input**; sole falsifier of `G-NEVER-FALSIFIED` |
| `MUT-CENSUS-LAX` | `len(GATES) > len(_all_must)` | true whenever any non-MUST gate exists (53 anchors); never evaluates `G-CENSUS-CLOSED`'s predicate |
| `MUT-FLOAT-LEAK` | `isinstance(ast.parse('x = 0.5')…value, float)` | a property of CPython, not of the audited source; no float is injected |
| `MUT-INVENTORY-DROP` | `not any(id=='I-READOUT' for r in _inv_drop)`, `_inv_drop` **being** the inventory minus I-READOUT | true by construction |
| `MUT-COMPLIANCE-FALSE` | `len([r for r in COMPLIANCE if r['computed'] is None]) == 0` | `G-COMPLIANCE`'s predicate never inspects `computed` — **proven not to reach, INJ09** |
| `MUT-PAPER-DRIFT` | `'9999' not in PAPER_TEXT` | tests a string absent from `G-PAPER-CLAIMS`'s predicate |
| `MUT-WCROSS-CLAIM` | `len(_claims) == 0` | `_claims = []` is a **literal** (L1919), never appended to |
| `MUT-CRA-BRIDGE` | `_shared == 0` | `_shared = 0` is a **literal** (L1889), never reassigned |

### 3.3 The coverage predicate measures naming, not reach

```python
covered = g['name'] in _killed_names or any(m['killed'] and m['mutant'] in g['falsifiers'])
```
`_killed_names` is the set of mutant `target` **free-text strings**
split on `' / '`.  Nothing checks that the mutant touches the gate.

* `anchor()` hard-codes `falsifiers=['MUT-ANCHOR-DRIFT']` on **every**
  anchor row.  That mutant perturbs exactly one expected digest
  (`A-S-D74N`).  **52 of the 53 anchors are declared falsified by a
  mutant that never reaches them** (23 byte + 9 path-value + 21 inline
  anchors, minus the one it does reach).
* One mutant target names no gate at all: `MUT-QUOTE-DRIFT →
  'V-TARGETS'`, a VERBATIM row id.  **The 13 verbatim rows are not in
  the gate ledger** — they are enforced by an inline `sys.exit(1)` and
  are invisible to both never-falsified censuses.  The "88 gates"
  denominator excludes them.

### 3.4 THE COVERAGE TABLE — honest denominators

| tier | gates | meet the #34 standard | do not | why not |
|---|---|---|---|---|
| ANCHOR | 53 | **1** (`A-S-D74N`) | 52 | the single anchor mutant reaches one row |
| MUST, Class-A falsifier, gate can fail | 12 | **12** | — | genuine |
| MUST, analytically forced | 3 | 0 | 3 | `T2-HOLONOMY`, `G-VERDICT-EQUALITY`, `G-SETTLEMENT` |
| MUST, Class-B-only falsifier | 10 | 0 | 10 | falsifier asserts the delivered object |
| MUST, Class-C-only falsifier | 8 | 0 | 8 | falsifier tautological or off-predicate |
| THEOREM-PASS | 2 | **2** | — | both waivers machine-checked (§3.5) |
| **total** | **88** | **15 (17.0 %)** | **73 (83.0 %)** | |

The 12 genuine MUST gates: `G-PATH-VALUE-STABILITY`,
`G-LAYER-SINGLE-SOURCE`, `G-KERNEL-POSITIVE`, `G-BLOCK-DECOMPOSITION`,
`G-COLUMN-STOCHASTIC`, `G-KERNEL-DOES-NOT-DESCEND`, `T2-D74-ANCHOR`,
`T2-REC-FLAT`, `T1-PRUNE-GATE`, `T1-TARGETS`, `T1-MULTIPLICITY`,
`T3-SCREEN`.

Class-C-only MUST gates: `G-FLOATGUARD`, `T6-CRA`, `T7-WCROSS`,
`T8-ATOMS`, `G-NEVER-FALSIFIED`, `G-COMPLIANCE`, `G-PAPER-CLAIMS`,
`G-CENSUS-CLOSED`.
Class-B-only MUST gates: `T1-3EVENT-LAW`, `T1-F8`, `T1-F8-MECHANISM`,
`T1-QUARTER-BLINDNESS`, `T4-RENEWAL-POSITIVE`, `T4-CK`, `T4-PADDING`,
`T5-CRB`, `T9-44`, `C-SCRAMBLE`.

### 3.5 The two never-falsified rows — the waivers ARE verified

Both claimed theorem-passes hold; I machine-checked the forcings:

* `G-KERNEL-PROPER`: `k_r(e|h) = q(e|h)·G(h+e,r−1)/G(h,r)` with
  `G(h,r) := Σ_e q(e|h)·G(h+e,r−1)`, so `Σ_e k_r(e|h) = G(h,r)/G(h,r)
  = 1` for every admissible input given `G > 0`.  The unit correctly
  splits out the substantive companion `G-KERNEL-POSITIVE` (strict
  positivity, measured, Class-A falsified).  **This pattern — disclose
  the identity, gate the substantive companion — is the model the
  repairs below should follow.**
* `G-CUT-ADDITIVITY`: `W(h) = μ(h)·G(h,4−|h|)/G(root,4)` and
  `Σ_{|h|=d} μ(h)·G(h,4−d) = G(root,4)` by induction on the same
  identity.  Forced.

Also verified by hand: `w(h)·k_r(e|h) = w(h+e)` — the class law's
exactness — is an identity, since `μ(h+e) = μ(h)·q(e|h)` and the
horizon index decrements with depth.

### 3.6 Shadowed gates

**None in the dead-code sense** — 35 `gate(...)` call sites + 53
`anchor(...)` rows = 88 ledger entries, every call site at module
level and executed (contrast R6a's 10 shadowed gates).  The shadowing
here is temporal and semantic:

* `G-NEVER-FALSIFIED` is evaluated at **84 gates / 33 mutants** —
  before `MUT-COMPLIANCE-FALSE`, `MUT-PAPER-DRIFT` and
  `MUT-CENSUS-LAX` exist.  Proven by INJ09: it printed
  `[PASS] … mutants 33, killed 33` in the same run in which a declared
  mutant printed `[SURVIVED]`.
* `G-CENSUS-CLOSED` (gate 88) sits outside its own 87-gate census —
  disclosed by the unit, but its declared falsifier is the tautology
  above (proven by INJ10: the gate FAILED while `MUT-CENSUS-LAX`
  still printed `[KILLED]`).

---

## 4. THE GATES THAT CANNOT FAIL

### 4.1 `T2-HOLONOMY` — the pre-registered holonomy gate

```python
T2_VERDICT = ('AGREE' if (_agree_k and _agree_g) else
              'DEVIATE-AT-' + ('BOTH' if not _agree_k and not _agree_g
                               else ('K' if not _agree_k else 'GAMMA')))
gate('T2-HOLONOMY', 'MUST', …,
     T2_VERDICT in ('AGREE','DEVIATE-AT-K','DEVIATE-AT-GAMMA','DEVIATE-AT-BOTH'), …)
```

The predicate tests that a variable lies in the set of values its own
definition can produce: **true for every possible input**.  The pin
§3.2 says of this gate, *"Without this gate 'Γ-main lands' is
unfalsifiable (the effectus ruling)."*  As implemented it is the
unfalsifiable object it was created to prevent.  `MUT-HOLONOMY-DRIFT`
names it as a target and cannot kill it.  (The live content is
elsewhere and genuine: `T2-D74-ANCHOR`, measured and Class-A
falsified; and the settlement conjunct
`holonomy_consistent = (T2_VERDICT == 'AGREE')`, which INJ12 flips.)

**Repair.** Gate the content: rebuild `T2_VERDICT` from the four
measured booleans by an independent expression and compare for
equality; add `_k_contains and _g_contains`; ship a mutant that
perturbs `_k['primes']` and shows the emitted verdict moves.

### 4.2 `G-VERDICT-EQUALITY` — a RECURRENCE of #219 at the gate #10 created

```python
VERDICT = f"{HEAD}-<{SEG_CARRIER} -- {SEG_REQ} -- {SEG_MOT} -- " \
          f"{SEG_SCOPE} -- {SEG_SETTLE}>"
REBUILD = (HEAD + "-<" + SEG_CARRIER + " -- " + SEG_REQ + " -- "
           + SEG_MOT + " -- " + SEG_SCOPE + " -- " + SEG_SETTLE + ">")
gate('G-VERDICT-EQUALITY', 'MUST', …, VERDICT == REBUILD and len(VERDICT) == len(REBUILD), …)
```

The "segment-by-segment rebuild from the measured values" is the same
concatenation of the same six variables in the same order, written
twice.  `VERDICT == REBUILD` is an identity.  The five `MUT-VERDICT-*`
rows corrupt *other* strings and compare those against `REBUILD`;
they show a corrupted string differs from the rebuild — which no one
doubted — not that the gate can fail, because it cannot.

This is §14 (v14 #20) verbatim: *"a compliance gate whose comparator
cannot disagree with the object under test is vacuous by construction
(the R2 verdict-gate recurrence of #219, at the very gate the #10
engraving created)."*  It has recurred at the same gate.  Under §13
(v13 #313), **a recurrence of an already-engraved disease is a MAJOR
by default and is named as a recurrence.**  So named.

**Repair.** Build the comparator from a different object — serialise
`RECEIPT['verdict_segments']` first and rebuild by joining that list,
or rebuild each segment from the receipt's own `tests` / `settlement`
sub-dicts — then add a mutant that alters `VERDICT` after
construction and show the gate fails.

**Enabled by the same vacuity:** six assertions inside the
REQUIREMENTS segment are hard-coded string literals, not rendered from
measurements — `D74-{2,3}-RANK-2-REPRODUCED`,
`REC-FLAT-AT-ALL-THREE-READINGS`,
`KERNEL=INDUCED;N-INDEXED-AT-OCCUPANCY;LEG-INDEXED-AT-COUNT`,
`MOVER=BLOCKED-AT-REFERENT-NO-SHARED-CARRIER-WITH-H_a[N]`,
`-REC-EXACTLY-LUMPABLE`, `-NOT-A-LOOP`; plus
`I-READOUT=GENUINELY-FREE-FIBER-2-AND-TARGET-SELECTING` in the
MOTIVATION segment.  The SCOPE segment is literal end to end apart
from two integers.  Five of the six have a separate MUST gate that
would exit 1; the MOVER clause rests on the literal `_shared = 0`
(§4.4).  §13 (v13 #234) wants the printed verdict derived inside a
gate from the measured counts.

### 4.3 `G-SETTLEMENT`

```python
SETTLED = all(SETTLEMENT.values())
_failed_links = [k for k, v in SETTLEMENT.items() if not v]
gate('G-SETTLEMENT', 'MUST', …,
     SETTLED == all(SETTLEMENT.values())
     and set(_failed_links) == {k for k, v in SETTLEMENT.items() if not v}
     and (SETTLED or len(_failed_links) > 0), …)
```

Conjuncts 1 and 2 restate the definitions immediately above them;
conjunct 3 follows from conjunct 2.  Forced.  The four conjuncts of
the settlement itself **are** genuinely input-driven — I flipped three
of them by targeted input (§5, §6) — so the settlement *line* is
honest; the *gate over it* is empty.

**Repair.** Compare `SETTLEMENT` against a dict rebuilt from the
independent sources (`T1_VERDICT` string, `T2_VERDICT` string,
`len(ANCHOR_FAIL)`, the INVENTORY class census), and ship a mutant
that desynchronises one of them.

### 4.4 Two MUST gates fed by a literal

```python
_shared = 0        # L1889, never reassigned   →  T6-CRA
_claims = []       # L1919, never appended to  →  T7-WCROSS
```

* `T6-CRA`'s detail prints *"shared carrier with H_a[N]: 0 declared
  maps"* as though measured; the verdict segment
  `MOVER=BLOCKED-AT-REFERENT-NO-SHARED-CARRIER-WITH-H_a[N]` rests on
  it.  Its live content is `_moving > 0` plus the CR-A path-value
  anchor.
* `T7-WCROSS`'s statement says *"the count of curvature ⇒ quantum
  claims in this unit is measured and is zero"*, and paper §5.7 says
  *"the count is gated rather than promised."*  **Both are false**:
  the count is a literal empty list.  The live conjunct is
  `len(_wc) >= 2`, which does measure the U2 note.

**Repair.** Either scan this unit's own emitted text / paper for a
declared claim-pattern and gate the measured count, or reclass both
conjuncts as DISCLOSURES and change "measured" to "declared", per §14
(v13 #208).

---

## 5. INJECTIONS — 16 RUNS, ALL PROVEN-EXECUTED

All on scratch copies; exit code, failing gates and surviving mutants
read from the produced artefacts; **no tracebacks in any run**.

| # | injection | class | exit | died at / result |
|---|---|---|---|---|
| INJ01 | targets `(3/7,1/7,3/7)` → `(1/2,0,1/2)` | target-law corruption | 1 | **KILLED** at `T1-TARGETS` (verdict TARGETS-MISSED) and `T1-MULTIPLICITY` — the `(m+1)/(2m+3)` clause genuinely binds the target constant to the measured multiplicity |
| INJ02 | occupancy numbers published under the COUNT label | readout swap | 1 | **KILLED** — but at `T1-QUARTER-BLINDNESS` and `T5-CRB`, **not** at `T1-TARGETS`, which printed `[PASS] verdict TARGETS-HIT-AT-THE-OCCUPANCY-READOUT` with `targets_hit = True`.  Three Class-B falsifiers flipped to `[SURVIVED]` |
| INJ03 | non-descent census 4/13 → 0/13 | census corruption | 1 | **KILLED** at `G-KERNEL-DOES-NOT-DESCEND` |
| INJ04 | eq-22 negative entries counted as 0 | interpolant-sign | **0** | **SURVIVED UNDETECTED** — all four triples flip PSEUDO-STOCHASTIC/REFUTED → STOCHASTIC, at 33/33 must-pass, 36/36 killed, 0 anchor failures |
| INJ05 | every screen row declared S-PASS | screen-verdict flip | 1 | **KILLED** at `T3-SCREEN` (census `{S-PASS: 10}`) |
| INJ06 | `I-GRAIN` GENUINELY-FREE → FORCED | inventory reclass | **0** | **SURVIVED UNDETECTED** — verdict segment moves to `MOTIVATION-FORCED-5|STABILIZER-FIXED-1|GENUINELY-FREE-4`, settlement line to "6 motivated of 10"; exactly 4 output lines change; every gate passes |
| INJ07 | Γ-prep sha `0f5d57eef77f` → `264cb54` | sha-provenance drift | 1 | **KILLED** at the `V-LADDER` verbatim row; the short-circuit fired before a single byte anchor |
| INJ08 | Γ-holonomy prime 389 → 390 on the rendered path | holonomy-value corruption | 1 | **KILLED — but at `G-PAPER-CLAIMS`**, not at any holonomy gate: caught only because `gprimes` happens to be one of the 13 `PAPER_CLAIMS` keys |
| INJ09 | one compliance row `computed = None` | compliance falsifier | 1 | `G-COMPLIANCE` printed **`[PASS]`**; its own row still printed *"MUT-COMPLIANCE-FALSE … reaches it and dies by its own predicate"*; two lines later that mutant printed **`[SURVIVED]`**.  Exit 1 came from the downstream `G-CENSUS-CLOSED` |
| INJ10 | unfalsified, unwaived MUST gate injected | shadow gate | 1 | `G-CENSUS-CLOSED` **FAILED** while `MUT-CENSUS-LAX` still printed `[KILLED]`; `G-NEVER-FALSIFIED` printed `[PASS] … mutants 33, killed 33`, blind to it |
| INJ11 | float literal into the audited source | float leak | 1 | `G-FLOATGUARD` **FAILED** (`float literals [2003]`) while `MUT-FLOAT-LEAK` still printed `[KILLED]` |
| INJ12 | settlement conjunct 3 forced True | settlement flip | 1 | verdict became `SETTLEMENT=SETTLED`; `MUT-SETTLEMENT-LAX` **`[SURVIVED]`**; `G-NEVER-FALSIFIED` (`killed 32`), `G-COMPLIANCE` (`mutant-falsified 12 of 13`) and `G-CENSUS-CLOSED` all **FAILED** |
| INJ13 | motivation inventory emptied | settlement flip | 1 | `T8-ATOMS` FAILED; `motivation_non_empty = False` |
| INJ14 | one negative Γ entry | settlement flip | 1 | `G-COLUMN-STOCHASTIC` and `T4-CK` FAILED; head flipped to **`GMAIN-BLOCKED-AT-THE-CARRIER`**, `constructed = False` |
| INJ15 | quotation-meaning inversion in the paper (quotes kept verbatim, surrounding prose asserts the opposite) | the #62 corrected-spec test | **0** | **SURVIVED UNDETECTED — output byte-identical to the clean run.**  13/13 verbatim rows PASS, `G-PAPER-CLAIMS` PASS |
| INJ16 | three hand-written prose numbers falsified (512→777, 1546→1547, "3 orbits"→"9 orbits") | prose-number drift | **0** | **SURVIVED UNDETECTED — output byte-identical to the clean run** |

**Survive-undetected (proven executed): 4 — INJ04, INJ06, INJ15,
INJ16.**  Two of them (INJ04, INJ06) move a delivered claim; two
(INJ15, INJ16) corrupt the paper with the instrument entirely blind.

**All four settlement conjuncts flipped by targeted input:**
`constructed` (INJ14), `targets_hit` (INJ01 → MISSED; INJ02 → hit at
the other readout), `holonomy_consistent` (INJ12), `motivation_non_empty`
(INJ13).  The settlement line is genuinely derived.

---

## 6. VERDICT REBUILD FROM THE RECEIPT ALONE

I rebuilt the emitted verdict from `gmain_receipt.json` alone: head
from `verdict_head`, the five segments from `verdict_segments`, joined
by `" -- "` inside `-<…>` — reproduces `RECEIPT['verdict']`
character for character, and that string is what
`gmain_output.txt:370` prints and what paper §6 block-quotes.  The
**render-from-the-gated-object** chain is intact.

Each segment was then flipped by targeted input: `SEG_CARRIER` (INJ14,
head flips), `SEG_REQ` (INJ01/02/03/05/08/12 — targets, holonomy and
screen sub-fields all moved), `SEG_MOT` (INJ06/INJ13), `SEG_SETTLE`
(INJ12/13/14).  `SEG_SCOPE` is literal apart from two integers and was
not flippable by any input short of editing it.

---

## 7. PAPER ↔ OUTPUT ↔ RECEIPT — THE FALSE-NUMBER SWEEP

Method: strip the verdict block-quote (which renders verbatim from the
receipt), enumerate every remaining numeral in the paper, trace each to
the receipt, the output, or a committed source.

### **69 distinct prose numerals traced.  FALSE NUMBERS: 0.**

Checks that could have gone wrong and did not:

| paper claim | independent recomputation |
|---|---|
| COUNT law (3/7, 1/7, 3/7) at leg 1 | from the receipt's own pattern census: slot totals 1536 / 512 / 1536 of 3584 ✓ |
| COUNT law (4/9, 1/9, 4/9) at leg 2 | 32768 / 8192 / 32768 of 73728 ✓ |
| multiplicity 2 → 3; `(m+1)/(2m+3)` = 3/7, 4/9 | 2048/1024 = 2, 49152/16384 = 3 ✓ |
| "exactly eight self-loops at 64/65 and 65/64" | 52 − 44 = 8; values 64/65: 6, 65/64: 2 ✓ |
| "1402 squares closing … 416 non-unit of 1402" | 1546 closed − 144 non-closing = 1402 ✓ |
| "473 of 473" on REC | 1546 − 1073 = 473; Γ spectrum `{1: 473}` ✓ |
| "fails at all 4 triples … at 34, 112, 12 and 12 cells" | CK rows with `cut > 0` ✓ |
| Γ spectrum on the 44 `{1/4:2, 1/3:8, 8/13:2, 13/8:6, 3:24, 4:2}` | sums to 44; matches `gamma_spectrum_on_curvature` ✓ |
| "5161 R-SIG, 1365 menu-exact, blocks {(1,1):1365,(2,2):3788,(2,3):4,(3,2):4}" | Γ-prep receipt at `0f5d57eef77f`: `rsig_count 5161`, `rsig_menu_exact 1365`, identical profiles ✓ |
| "G(·,2) … more than one value on 4 of the 13 classes" | `horizon_potential_multivalued.MENU` row `[2, 4, 13]` ✓ |
| "n = 4 … 3 orbits, simplex dimension 2, transitivity False" | CR-B receipt at `fbc3a81`: `pinned_orbits 3` — a hand-carried number **not** in this unit's receipt, and it is right ✓ |
| "U3's own committed `ARMC2-8x8`" | U3 note at `f40f5e1` line 68: "`ARMC2-8x8` is `J/8`" ✓ |
| "order-comparable at 512 of 512" | `pdp_comparable 512 / pdp_total 512` ✓ |
| every §9 totals-table entry | matches `totals` exactly ✓ |

### But three FALSE CLAIMS ABOUT THE INSTRUMENT appear in the paper

1. **§5.7** *"the count is gated rather than promised"* — the count is
   the literal `_claims = []` (§4.4).
2. **§6** *"with five verdict falsifiers … each proving the derivation
   can fail"* — the gate they attach to cannot fail (§4.2).
3. **§3** *"Each is bound to a named consumer gate that exists, is
   non-literal, and dies to a declared mutant"* — 9 of the 13 consumer
   gates do not meet that standard, and 2 (`T2-HOLONOMY`,
   `G-SETTLEMENT`) cannot fail at all.

And one in the delivered output: `gmain_output.txt:330`, *"every
declared falsifier reaches its gate and dies by the gate's own
predicate, evaluated blind"* — false for 18 of 36 rows.

### 7.1 How much prose is actually gated

`G-PAPER-CLAIMS` renders 13 values and requires each as a **substring**
of the paper: **13 of 69 numerals bound**, one of them the
one-character string `'4'` (`ck_fail`), which any paper satisfies — so
**12 substantive bindings**.  Presence only: a paper asserting both
"4 of the 10" and "7 of the 10" passes.  And the gate short-circuits
to PASS on an absent paper (`len(_missing) == 0 or PAPER_TEXT == ''`).
INJ16 is this gap, executed.

---

## 8. THE TEN ENGRAVINGS, TESTED UNDER ATTACK

The committed RUNBOOK (`3781cbce4e42`) carries **13** addenda dated
2026-08-09; **10** are v14-origin.  The sweep filters on the literal
`'2026-08-09, from v14'` and gates `== 10`; the three v13-origin ones
(repair propagation #313, boundary parity #313, precheck doctrine
#314) are outside it, and the source docstring's "all ten 2026-08-09
engravings" is imprecise as stated.

| engraving | unit's status | verdict under attack |
|---|---|---|
| #10 containment is not equality | APPLIED | **VIOLATED IN SUBSTANCE** — the comparator is a syntactic copy of the audited object (§4.2); recurrence of #219/#20 |
| #10 render from the gated object | APPLIED | **HOLDS** — verdict rebuilt from the receipt alone (§6); the row's "computed" status is prose, not a measurement |
| #20 prose renders from the receipt | APPLIED | **PARTIAL** — 13 of 69 numerals bound, one vacuously; INJ16 survives |
| #20 compliance claims are gate claims | APPLIED | **VIOLATED** — INJ09: the shipped falsifier cannot fail the gate |
| #20 path-value anchoring | APPLIED | **HOLDS** for the 9 anchored rows (all recomputed, 0 mismatches); **fails for the one unanchored probe** (D2) |
| #34 waiver claims are gate claims | APPLIED | **VIOLATED** — coverage measures naming, not reach; 52 anchors + 18 non-reaching rows (§3) |
| #34 verbatim anchors adopted | APPLIED | **HOLDS on form** — 13 rows, mean window 103 chars (context, not fragments), evaluated before the 23 byte anchors, short-circuit real (INJ07) |
| #46 no unanchored runtime inputs | APPLIED | **ONE EXCEPTION** — the unit's own paper is read from the worktree, unhashed (D1); the row's "LOG.md / STATUS.md read: 0" is a hard-coded literal, not a measurement (I verified it true independently: the process opens only `SELF` and the paper, and shells out only to `git show <sha>:<path>`) |
| #62 verbatim anchors, corrected spec | APPLIED | **VIOLATED IN SUBSTANCE** — "consumers … mutant-falsified 13 of 13" holds only under the unit's own coverage predicate; only 4 of 13 meet the #34 standard, 2 cannot fail, and **INJ15 reproduces the R6b′ T1 meaning-inversion the #62 amendment was written to close** |
| #62 provenance by committed sha | APPLIED | **HOLDS, cleanly** — exactly one `subprocess.run(['git','show', f'{sha}:{path}'])`; no `git show HEAD:`; no worktree read for any source; 23/23 byte anchors, 9/9 path-value anchors, 3/3 stability rows verified; a sha drift dies (INJ07) |

Two standing rules outside the ten also bear:

* **§14 symmetry self-tests.**  The central object is a holonomy and
  the rule exists because of a gauge-variant one.  The square ratio
  `rq = qA·qB2/(qB·qA2)` and the edge orientation
  `(V[h+(eB,eA)], V[h+(eA,eB)], x)` fix a direction convention; the
  reported `selfloop_values` **multiplicities** (64/65: 6 vs 65/64: 2;
  1/2: 26 vs 2: 10) are convention-dependent while the counts, the
  obstruction and the generated group are not.  **No declared
  orientation mutant, no invariance self-test.**  The convention is in
  fact pinned — `A-D74-SPECTRUM` anchors the asymmetric split
  {1/2: 70, 2/3: 2, 3/2: 6, 2: 10} against D74's committed value, so a
  global flip would die there — but incidentally, not by declaration.
* **§13 (v13 #314) precheck doctrine.**  Compliant in kind: the leg-2
  prune selects candidates and the verdict-naming facts are measured
  on the censused objects.  But the unpruned agreement gate covers
  **3 of 256 bases, 864 of 73,728 legs (1.2 %)** — in the receipt, not
  in the paper's sentence.

---

## 9. FINDINGS, RANKED, WITH EXACT REPAIRS

### MAJOR

**M1 — `G-VERDICT-EQUALITY` is a self-comparison: a RECURRENCE of the
already-engraved #219/#20 disease, at the very gate the #10 engraving
created.** §4.2.  Repair: rebuild the comparator from
`RECEIPT['verdict_segments']`; add a post-construction verdict mutant.
Named as a recurrence per §13 (v13 #313) — MAJOR by default.

**M2 — `T2-HOLONOMY`, the pre-registered holonomy gate, cannot fail
for any input.** §4.1.  The pin created it precisely so "Γ-main lands"
would be falsifiable.

**M3 — `G-SETTLEMENT` cannot fail for any input.** §4.3.  (The four
conjuncts under it are genuine — I flipped all four.)

**M4 — the interpolant-sign result is ungated and a corruption of it
survives with a perfectly clean instrument (INJ04).**  `negs = 0`
flips all four eq-22 readings from PSEUDO-STOCHASTIC/REFUTED to
STOCHASTIC — inverting paper §5.4's *"at every depth-cut triple with a
non-degenerate first cut, no interpolant of eq. 22's form exists"* —
at exit 0, 33/33 must-pass, 36/36 killed.  `T4-PADDING`'s predicate
never reads a sign.  Repair: add `T4-EQ22` gating
`all(r['negatives'] > 0 for r in EQ22 if r['invertible'])` against the
recorded `most_negative` values; ship a sign-flip mutant; put
`negatives` into `PAPER_CLAIMS`.

**M5 — the motivation inventory's classification column is ungated;
reclassing a genuinely-free choice as FORCED survives (INJ06).**
`T8-ATOMS` checks only `len(INVENTORY)==10`, the presence of the
`I-READOUT` id, and `forced+stabilizer > 0`.  This is the RSQ standard
the pin calls "a first-class head".  Repair: gate `cls` against a
machine-computed fiber for every item that has one (I-CARRIER already
computes `_rung_fiber`; I-READOUT's fiber is the two measured
readouts; I-PRUNE's is the unpruned agreement); mutate a class.

**M6 — the coverage claim rests on naming, not reach: 52 of 53 anchors
are declared falsified by a mutant that never touches them, and 18 of
36 rows never build a mutated object.** §3; honest denominator 15 of
88.  Repair: make `mutant()` *measure* `reaches_target` (evaluate the
named gate's predicate on the mutated object, record pre- and
post-values), require every target string to be a ledger gate name,
and give anchors a per-row drift loop.

**M7 — the declared falsifier of `G-COMPLIANCE` cannot fail it
(INJ09).**  Direct violation of §14 (v14 #20).  Repair: add
`all(r['computed'] is not None for r in COMPLIANCE)` to the predicate.

**M8 — the instrument cannot emit a SETTLED verdict without failing
three of its own MUST gates (INJ12).**  `MUT-SETTLEMENT-LAX`'s
`killed` is `not all(SETTLEMENT.values())`, so it survives exactly
when the unit settles: forcing the holonomy link True produced
`SETTLEMENT=SETTLED` **and** `[SURVIVED] MUT-SETTLEMENT-LAX`, failing
`G-NEVER-FALSIFIED`, `G-COMPLIANCE` and `G-CENSUS-CLOSED` — exit 1.
The clean 36/36 sheet is **contingent on the verdict coming out
PARTIAL**; the instrument is structurally biased toward the negative
verdict, and a positive Γ-main would have had to be shipped through an
instrument repair.  Repair: `MUT-SETTLEMENT-LAX` must evaluate a
*three-of-four rule* on a mutated copy of `SETTLEMENT` and compare it
against the four-of-four rule, not report the delivered state.  The
same fix applies to the other nine Class-B rows.

### MODERATE

**D1 — one unanchored mutable runtime input: this unit's own paper.**
`committed(f40f5e1, 'v14/paper-12-gamma-main.md')` returns `None`
(verified: the path does not exist at that commit), so `PAPER_TEXT`
falls through to `open(os.path.join(REPO, PAPER_PATH))` — worktree
bytes read at run time, with **no hash gate binding them to
`d85a629a9378`**.  It feeds the 13 verbatim `in_paper` predicates and
`G-PAPER-CLAIMS`.  INJ15/INJ16 are the consequence.  Repair: anchor
the paper's sha256-12 as a byte anchor, or state the exception
explicitly in the #46 compliance row.

**D2 — a declared path-value probe into Γ-prep's receipt does not
resolve, and the failure is swallowed.**  `PV-GPREP-DELTA`, path
`armB/atoms/0/delta_matched_primary`: Γ-prep's receipt is a **flat
dict with no `armB` key**; the δ* fact lives at `B2_best_delta = 1`.
`pv()` raises, the `except` writes `'<<PATH DOES NOT RESOLVE>>'`, and
because `want is None` the row is filed as an unanchored probe with
`anchored=False`.  **It is not printed in `gmain_output.txt` at all**,
and `totals.path_value = 9` counts only the anchored rows.  So the
unit's single read of the Γ-prep δ*=1 datum the pin names as inherited
reads nothing, silently.  Repair: `want=None` probes must still gate
that the path RESOLVES; point it at `B2_best_delta` and anchor 1.

**D3 — `G-NEVER-FALSIFIED` is evaluated before three of the mutants
exist** (proven, INJ09/INJ10).  Repair: move it after the final
census, or evaluate twice with the second authoritative.

**D4 — `T1-TARGETS` is readout-blind, proven (INJ02).**  Publishing
the occupancy law under the COUNT label leaves it `[PASS]` with
`targets_hit = True`; only `T1-QUARTER-BLINDNESS` catches the swap,
and three declared falsifiers flip to `[SURVIVED]` in the process.
Given the arena declares OCCUPANCY primary and the targets are hit at
COUNT, the settlement's `targets_hit` conjunct does not know which
readout it is crediting.  Repair: make the conjunct
`T1_VERDICT == 'TARGETS-HIT-AT-THE-COUNT-READOUT-MISSED-AT-THE-OCCUPANCY-READOUT'`
(or carry the readout name into the conjunct).

**D5 — `G-PAPER-CLAIMS` passes vacuously on an absent paper, tests
substring presence only, and one of its 13 bindings is `'4'`.** §7.1.
Repair: drop the `or PAPER_TEXT == ''` disjunct; require ≥ 3-character
values or bind value-with-label; extend `PAPER_CLAIMS` to the headline
numbers with no binding (1402, 44+44, 52, 416, 473, 34/112/12/12, the
eq-22 negatives, the motivation census).

**D6 — no orientation/direction perturbation in the mutant table for
the holonomy instrument (§14).** §8.  Repair: add a mutant inverting
`rq` globally, record that `A-D74-SPECTRUM` dies, and self-test that
obstruction, self-loop count and the generated group are invariant
under the flip while the value multiplicities are not.

**D7 — `T6-CRA` and `T7-WCROSS` present hard-coded literals as
measurements, and the paper repeats the claim.** §4.4.

**D8 — the block decomposition's carrier-scope bite is not disclosed.**
`G-BLOCK-DECOMPOSITION` measures **689 carrier R-SIG points in 2
blocks over 9 of 113 MENU classes**; paper §4 prints only the depth ≤ 5
anchor census (5161 / 1365 / four blocks).  True, denominator 9.
Repair: print the carrier-scope triple in §4.

**D9 — the "ten engravings" is a v14-origin subset of thirteen.** §8.

**D10 — the unit cannot be run without clobbering its own delivery.**
No argv, no `--dry-run`, writes hard-coded to `REPO`.  Repair: derive
the output directory from `os.path.dirname(SELF)` or accept
`--out-dir`, and reject unknown flags.

### MINOR

* `T3-SCREEN` gates only "≥ 1 of each verdict class"; the screen
  census is a verdict segment with no gate on its composition.
* `_cons_literal` ("non-literal consumer") only checks
  `g['detail'] in ('True','False')` — a very weak notion.
* The prune-gate subsample size (3 of 256 bases) is in the receipt and
  not in the paper.
* The mid-run line "anchors covered by MUT-ANCHOR-DRIFT: 0" reads as
  though no anchors needed covering; in fact all 53 were covered
  through the falsifier route and the anchor-specific branch was empty.
* INJ08 shows the paper-claims gate is doing holonomy-integrity work
  by accident; the holonomy values not in `PAPER_CLAIMS` (the
  self-loop split, the Γ spectrum multiplicities) have no such
  backstop.

### WHAT IS SOLID — do not disturb in repair

* Reproduction is exact and byte-identical; the wall-clock discipline
  (stderr only) works.
* Provenance by committed sha is the cleanest instrument I have
  audited in v14: one git call, no HEAD, no worktree source, 23/23
  byte anchors and 9/9 path-value anchors independently recomputed
  with zero mismatches, path-value stability 3/3.
* The verbatim short-circuit is real and bites (INJ07).
* Both THEOREM-PASS waivers are correct, and the
  `G-KERNEL-PROPER` / `G-KERNEL-POSITIVE` split is exactly right.
* Exact arithmetic: 0 float literals, 0 numpy/math names, verified by
  my own AST pass; `G-FLOATGUARD` itself bites (INJ11).
* Leg 1 is genuinely unpruned; leg 2's prune is gated, not assumed.
* No shadowed gate in the dead-code sense: all 88 ledger entries come
  from executed call sites.
* The head is conservative and the caveats are stated before use (the
  q-group "is not a discriminating statistic", U3's degeneracy
  qualifier, the padding declared a CONVENTION).
* **Zero false numbers in 69 traced prose numerals.**

---

## 10. K1–K5 AT INSTRUMENT DEPTH

**K1 — construction fidelity.**  Cut dims [1, 5, 13, 45, 113], 113
classes over 3969 histories, column-stochastic exactness over all 20
transfers of both quotients (`_cs_bad = 0`, `_neg = 0`, flippable —
INJ14), the class law `w(h)·k_r = w(h+e)` verified as an identity, the
23-sha provenance verified artefact by artefact, and the non-descent
measurement `G(·,2)` multi-valued on **4 of 13** depth-2 classes —
which is what forces the readout.  **Sound**, with the two properness
identities correctly disclosed rather than claimed as evidence.

**K2 — the targets under readout-relativity.**  COUNT hits both
targets exactly; I reproduced both laws independently from the
receipt's own pattern census.  OCCUPANCY gives (3/8, 1/4, 3/8) at both
legs and the quarter-law cause is measured.  The unit is honest — the
head names the readout and the I-READOUT entry says the targets select
COUNT.  Two instrument reservations: `T1-TARGETS` is readout-blind
(D4, proven), and the I-READOUT class is an ungated hand-written
string (M5, proven).  No pinned fact forces either readout, and the
unit says so.

**K3 — the holonomy deviation.**  q reproduces ⟨2,3⟩ exactly
(`T2-D74-ANCHOR`, measured, Class-A falsified); the k-enlargement is 8
self-loops at 64/65 and 65/64 adding the primes 5 and 13; Γ's group is
rank 7; REC is flat at all three readings and `MUT-REC-CORRUPT`
genuinely kills it; the scramble control is real and its caveat is
stated before use.  **But the pre-registered gate over all of this
cannot fail (M2)**, a prime corruption is caught only by the
paper-claims gate (INJ08), and there is no orientation self-test (D6).

**K4 — the quantum-shape claims.**  The eq-22 refutation is the
weakest-instrumented headline: **no gate reads a sign and a corruption
survives (M4)**.  The non-Markov census (4 of 10 triples;
34/112/12/12 cells) is genuinely measured with the record chain
exactly lumpable as the control.  The U3 screen is a faithful
re-implementation with its omission declared where it is made, and the
single S-PASS is the known degenerate J/8 with U3's own certificate
verified in exact integer arithmetic — the unit correctly refuses to
make anything of it.  The 44 + 44 result is measured on both halves.
At citable scope the "no curvature ⇒ quantum claim" limitation is
right — but the *count* backing it is a literal (D7), so the claim
about the claim is not measured.

**K5 — instrument.**  §§2–9.  88 gates vs 36 mutants resolves to
**15 of 88 at the #34/#62 standards**; three MUST gates cannot fail;
two more are fed by literals; the two theorem-pass waivers are
genuine; no dead-code shadowing but `G-NEVER-FALSIFIED` is temporally
shadowed and gate 88 sits outside its own census; four proven-executed
injections survive undetected; the paper↔output↔receipt sweep is clean
on numbers and dirty on three instrument claims; two plain runs
byte-identical and the delivered output reproduced byte-for-byte; repo
hashes unchanged after all work.

---

## 11. RECOMPUTATION LEDGER

| what | count |
|---|---|
| full program executions (2 plain + 16 injections) | 18 |
| sha256 verifications of protocol / pin / delivery / RUNBOOK / Γ-prep | 8 |
| byte anchors independently recomputed from committed blobs | 23 |
| path-value anchors independently recomputed | 9 |
| gate-coverage rows recomputed independently (both routes) | 88 |
| mutant `killed` expressions extracted and classified | 36 |
| gate predicates extracted and analysed for vacuity | 35 |
| paper prose numerals traced | 69 |
| arithmetic reproductions of delivered quantities | 15 |
| Γ-prep receipt field cross-checks | 5 |
| CR-B receipt rows cross-checked | 12 |
| RUNBOOK engraving census (13 dated, 10 v14-origin) | 1 |
| AST scans (input channels, `open`/`subprocess`, floats) | 3 |
| repo hash snapshots (87 files each) | 3 |
| **total discrete recomputations** | **~325** |

**False numbers produced by me: 0** — every count above is machine-
derived and re-derivable from the scratch artefacts.

**Repo state at close:** paper `d85a629a9378`, code `51c3b4cf3f3c`,
output `b2b45be500b7`, receipt `974f36b1251a`, `RUNBOOK.md`
`3781cbce4e42` — unchanged.  Single repo write: this file.
