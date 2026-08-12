# REVIEW — OCC (paper-31), SEAT K3: THE INSTRUMENT LENS

**Protocol:** v14 ledger #256, row K3 (the era disease sweep; 50 mutants
outside the harness; the 40 seals at value-close; the 8 verbatim anchors;
injections; the two-route independence; E-24; argv; byte ×2; the
212-numeral sweep).  **Era:** post-engraving-native — E-22, E-23, E-24 in
force with no excuses.

**The object, sha256-12, verified at start AND at end of this review:**

| artifact | declared (#256) | at start | at end |
|---|---|---|---|
| `v14/paper-31-occ.md` | 1b140f7973d4 | 1b140f7973d4 | 1b140f7973d4 |
| `v14/code/occ_exact.py` | e96c1e14a0b6 | e96c1e14a0b6 | e96c1e14a0b6 |
| `v14/code/occ_output.txt` | 63d98f4ee6f0 | 63d98f4ee6f0 | 63d98f4ee6f0 |
| `v14/code/occ_receipt.json` | 46e757ef9c47 | 46e757ef9c47 | 46e757ef9c47 |
| `v14/note-occ-pin.md` (pin) | 145db72ce547 | 145db72ce547 | 145db72ce547 |

All twelve pinned SOURCES re-hashed independently against their declared
digests at commit 7ab2f21: 12/12 match.  Repo objects unchanged by this
work; git read-only; every execution off-tree in
`…/scratchpad/occ-in/`.  Sibling working-tree dirt (smu/perr/sig) is
disclaimed and was not touched.  One repo write: this file.

**GRADE: AWF — ACCEPT WITH FIXES.**  Six MAJOR findings, eight MINOR.
None moves the head: `OCC-CEILING-OPEN` survives every attack, and I
re-derived the whole leak layer from scratch with my own ring arithmetic
and found **zero** disagreements with the receipt.  The findings are of
one family: **the measurement is right and part of the evidence for it is
not evidence.**  Three of the six MAJOR repairs are written out below and
verified to (a) leave the pristine object passing and (b) kill the
injection that found them.

**Executions: 163.  Independent recomputations: 282** (including 441,774
exact Z[ω] element evaluations in a from-scratch leak rebuild).

---

## 1. THE DISEASE SWEEP (every current entry, PRESENT/ABSENT, with a
## demonstration either way)

| # | disease | verdict | the demonstration |
|---|---|---|---|
| 1 | phantom consumers | **ABSENT** | 8 verbatim consumers + 16 path-value consumers + 40 `sealed_at_gate` values = 64 names, every one in the 56-gate registry **and** in this run's 54-row evaluated snapshot.  50 mutant gates likewise, the only two exceptions being `MUT-SEAL-DROP`/`MUT-SEAL-BROKEN` → `G-SEAL-COMPLETE`, a *declared* post-snapshot gate covered by `G-REACHABILITY`'s named `LATE_GATES` and re-verified by `G-ARTIFACT-INTEGRITY`'s `late_ok`. |
| 2 | constant-boolean falsifiers; E-23 three-legged honesty | **PRESENT (legs 1–2)** | 15 of the 50 shipped declarations read by hand against their AST hook sites: **15/15 correct**, symbol and value both whole tokens.  But the *checks* are substring tests: I shipped a falsifier declaring `leaking_cited → 4` while the code moves it to `47`, in both the code leg and the prose leg, and the run **exited 0** (MINOR-1).  Leg 3 (sweep-binding) is solid — see row 10. |
| 3 | seal windows / the 54+2 snapshot | **ABSENT** | All 40 seals taken at **value-close**: for every sealed path, the last write to `R[path]` precedes its `SEAL.take`, and the only post-seal write in the file is `MUT-SEAL-BROKEN`'s own hook.  Three closing objects (`gates`, `closing_gates`, `transcript_head`) are *assembled* after `G-PAPER-COVERAGE-FINAL` and sealed on the next lines — value-close, not late-sealing.  Mid-window forgeries die: I corrupted `p1/carrier_cells`, `leaks/carrier_grain_antisymmetric_leak_cells` and `arms[0]/word` immediately after their seals — 3/3 died (`G-PAPER-CLAIMS`, `G-PAPER-CLAIMS`, `G-VERDICT-RECONSTRUCTED`), artifacts byte-unchanged.  A post-snapshot gate cannot be dropped silently: deleting `G-SEAL-COMPLETE`, deleting `G-ARTIFACT-INTEGRITY`, and lifting the writes above the terminal gate each killed the run, with three independent guards (the sweep's on-target binding, `late_ok`, and `G-WRITER-SHAPE`'s pre-snapshot AST list). |
| 4 | read-back before `os.replace` | **ABSENT** | Four post-write corruptions of the **staged** files, injected after the write and before the read-back: the verdict word in the JSON, a transcript line, a deep sealed leak count, and the declared-unsealed chain leg.  **4/4 died at `G-ARTIFACT-INTEGRITY`**; the delivered artifacts stayed at 63d98f4ee6f0 / 46e757ef9c47.  Nothing is promoted.  (One residue: the `.tmp` files survive — MINOR-2.) |
| 5 | E-22: fences by TRUE multiset; all table rows; inline spans; no blanket whitelists | **PRESENT** | **MAJOR-1**: the fence gate is containment-with-counts, not multiset equality — an *extra* forged `OCC-CEILING-FORCED<…>` block appended to the paper survives at exit 0, and so does the E-22 named disease itself (clean copy + forged twin).  Table rows: 23 rendered (not 20), all 23 present exactly once; **8 cell-level swaps across the leak table, the control-arm table and the grain table all died** at `G-PAPER-TABLES`; pure row *reorders* survive but are semantically null (every row is self-keyed by its first column).  Inline spans: 39 spans / 10 numerals, live — an injected `999999` in a span died.  Whitelists: no blanket suppression, but see MINOR-5 and MINOR-6. |
| 6 | vacuous clauses (`all(True…)`-shaped; stamps a failing row could hide under) | **PRESENT** | **MAJOR-3** (the declaration fiber is a self-comparison) and **MAJOR-6** (the refusal count's predicate ignores the completion).  Also `all(g["passed"] for g in LD.rows)` in `G-PAPER-COVERAGE-FINAL` is structurally always true, since `Ledger.gate` raises on failure (MINOR-8).  No stamp was found under which a *failing* row could hide: every stamp I probed is accompanied by a live predicate. |
| 7 | the two-route leak agreement (48/48) — independence | **PRESENT, QUALIFIED** | The two routes share everything but their last line: `t1`, `t2`, the admissible/forbidden construction and the loop are one and the same; route 2 differs only in testing `t1≠0 or t2≠0` instead of `t1±t2≠0`.  It is therefore a **cancellation probe, not an independent recomputation** — which is exactly what the gate text and §6 say ("they can differ only where BOTH products are nonzero").  It is not vacuous: 405 both-nonzero cells exist across the run, so the agreement has something to fail on.  I supplied the missing independence myself — see §3. |
| 8 | verbatim anchors: perturbed-and-must-not-locate | **ABSENT** | Re-run by me, not read off the receipt: 8/8 located after #125 normalisation; the shipped perturbation (last content token + `ZQ`) absent 8/8; two further hostile perturbations (first token, middle token) absent 8/8.  Two probes of mine located — both my artifacts (a *prefix* of a 2-token needle; reversing a needle with no spaces), not defects. |
| 9 | E-24: counts COUNTING-ONLY; denominators re-counted | **PRESENT** | The stamp is present, sealed, and falsified (`MUT-COUNTING`), and no measure is declared anywhere — E-24's own requirement is met.  But **MAJOR-5**: §10 claims "every published ratio's denominator is re-counted from the construction it claims to enumerate", and **4 of the 22 published `X-OF-Y` head ratios** are.  I re-counted six denominators by hand: coins 6 ✓, admissible 216 = C(27,2)−135 ✓, forbidden 135 = 9·C(6,2) ✓, leak rows 48 = 6·4·2 ✓, selection rows 24 = 6·4 ✓, comparisons 53,460 = 6·C(4,2)·(27+729+729) ✓, parent split 48+16=64 ✓ from paper-22's own committed rows. |
| 10 | the 50-mutant sweep OUTSIDE the harness | **ABSENT** | 50 separate process launches: **50/50 exit 1 and die at the gate they name**, zero off-target.  Whole-tree hash before and after: `4c918207fcf0…` = `4c918207fcf0…`; `occ_output.txt`/`occ_receipt.json` untouched. |
| 11 | CLI; `--selftest` writes nothing | **ABSENT** | 25 hostile argv vectors — unknown flags, arity errors on both flags that take a value, second-mode flags in both orders, `--verify-paper --mutant`, repeated flags, case variants, `---no-write`, `--no_write`, trailing space, bare `x`, empty string — **25/25 exit 2**.  6 legal shapes behave per the disclosed conventions.  `--selftest` corrupts `A-COUPREC`, dies at `G-PROVENANCE`, exits 1; whole-tree hash across the entire battery **identical**, so "writes nothing" is proved by my tree hash and not by the program's own claim. |
| 12 | byte ×2 across hash seeds; bare-copy loud abort | **ABSENT** | Three off-tree, git-less deliveries at `PYTHONHASHSEED` 0, 98765 and 1 (the last from `/` as CWD): all three byte-identical to the committed artifacts.  A bare copy of `occ_exact.py` alone aborts loudly at `G-PROVENANCE :: a pinned source is not at its path :: v14/note-occ-pin.md`, exit 1, and writes **nothing** (the bare tree contains one file after the run). |
| 13 | the 212-numeral paper↔output↔receipt sweep | **PRESENT** | My recount reproduces the published split exactly: 212 = 144 prose + 58 fenced (3 blocks) + 10 inline (39 spans), unlicensed = none.  Claims 15/15 and table rows 23/23 occur exactly once; the output's `TOTALS` line matches all 12 receipt fields.  But **MAJOR-2**: only 143 of the 212 numeral occurrences sit inside a string this run *renders*; 69 are merely *licensed*, and four load-bearing corruptions in the abstract and §2 survive at exit 0.  Also: the three head segments occur in the paper and in the receipt but **not in `occ_output.txt`** (MINOR-3). |

---

## 2. MAJOR FINDINGS

### MAJOR-1 — E-22's fence gate is containment-with-counts, not multiset equality; an extra forged verdict block survives

`run_paper_gates`:

```python
multiset_ok = all(blockmap.get(k, 0) == v for k, v in want.items())
```

`want` is the multiset of *derived* segments.  The predicate asks only
that each derived segment appear the declared number of times; the
paper's own block multiset may carry **any number of additional
blocks**, unexamined.

Demonstrated, both at exit 0:

- appending a fourth fenced block reading
  `OCC-CEILING-FORCED<… P2=STRUCTURAL-EXCLUSION …>` — the inverted
  headline, in a verdict fence, in the delivered object;
- the E-22 *named* disease verbatim: the clean `OCC-CARRIER<…>` block
  followed by a twin with `CARRIER-CELLS=26`.

Neither carries a new numeral, so `G-PAPER-NUMERAL-COVERAGE` is blind to
both, and no polarity needle names an outcome word.  Only an exact
duplicate of a derived segment dies.  The engraving's own sentence — "a
paper carrying a clean copy and a forged twin satisfies containment with
the clean one" — is printed in the gate statement while the gate does the
thing it warns against.

**Repair (verified):**

```python
multiset_ok = (blockmap == want)
```

The delivered paper has exactly 3 fenced blocks and 3 derived segments,
so equality holds on the pristine object.  Verified: pristine passes;
both survivals above now die at `G-PAPER-HEAD-VERBATIM`; the exact-
duplicate case still dies.

### MAJOR-2 — 69 of the paper's 212 numerals are licensed but unbound; four load-bearing corruptions survive at exit 0

The paper instrument has two layers: 41 strings *rendered* from this run
(15 claims + 23 table rows + 3 head segments) and a licensing scan over
every numeral.  The first binds meaning; the second only asks that a
numeral be *some* measured value.  Measured: **143 of the 212 numeral
occurrences lie inside a rendered string; 69 do not.**  The residue is
not decorative — it contains `53460` ×4, `216` ×4, `135` ×2, `81` ×2,
`27` ×4, `36`.

The abstract ("What rides what") states the unit's four headline numbers
in *paraphrase*, so the claim strings match only the §-body copies.  All
four of these edits to the delivered paper passed at exit 0:

| edit (in the abstract / §2) | result |
|---|---|
| `216` admissible ↔ `135` forbidden, swapped | exit 0 |
| `53,460 of 53,460` → `216 of 216` | exit 0 |
| carrier-grain leak `81` cells → `864` | exit 0 |
| §2 `36 solutions over the ring` → `37` | exit 0 |
| §3 "it reaches **9** of the 27" → "**8** of the 27" | exit 0 |

Each replacement numeral is licensed by some other measured value (or by
the structural whitelist), which is all the coverage gate asks.

**Repair (verified):** extend `paper_claims` with the abstract's own
wordings, anchored so each occurs exactly once —

```python
("C16", "they give %s distinct two-excitation theories, and their "
        "one-excitation restrictions agree, as objects, at %s of %s "
        "comparisons" % (…)),
("C17", "the old mechanism works: the symmetric shape leaks at %d cells "
        "at %d of the %d coin classes and the antisymmetric shape leaks "
        "at %d" % (…)),
("C18", "is a sentence -- both shapes leak at %d of %d coin classes, "
        "every one of the %d admissible configurations leaks, and every "
        "one of the %d forbidden configurations is reached" % (…)),
("C19", "%d solutions over the ring, %d classes up to a global phase"
        % (po["ring_solutions"], po["classes_up_to_phase"])),
```

Verified: pristine paper passes at 19 claims; all four corruptions above
now die at `G-PAPER-CLAIMS`.

**And the general fix, which I recommend engraving:** publish and gate
the *binding* census — the count of scanned numerals that lie inside a
rendered string versus those merely licensed — so the unbound residue is
a sealed number that cannot grow silently.  Today it is 69 and nothing
in the run knows it.

### MAJOR-3 — "53,460 of 53,460 comparisons" is an object compared with itself

`p2_fiber`:

```python
for did in DECLARATION_IDS:
    objs[did] = one_excitation_object(W)
```

and

```python
def one_excitation_object(W):        # <- takes no declaration
```

The four "declaration-restricted" one-excitation objects are four
evaluations of the same expression on the same argument.  Measured: the
number of distinct objects across the four declarations is **1**, by
construction; `va != vb` is unreachable; `one_excitation_disagreements`
is a constant 0 and `restrictions_agree_as_objects` a constant `True`.
The arithmetic confirms the shape: 53,460 = 6 coins × C(4,2) pairs ×
(27 + 729 + 729) entries — every one of them a self-comparison.

End-to-end blindness, demonstrated: I gave `D-ACTOR-1` a genuinely
different one-excitation content (it now forbids one cell outright, so
its space drops to 200 while the others stay at 351/378) and the
published row did not move — `one_excitation_comparisons: 53460`,
`one_excitation_disagreements: 0`,
`restrictions_agree_as_objects: True`.

This is load-bearing prose.  §4: "because every declaration restricts to
the same one-excitation object, no measurement at one excitation … could
have distinguished them"; the head field
`P2-ONE-EXCITATION-RESTRICTIONS-AGREE=53460-OF-53460`; claim C05; the
abstract.  The *statement is true* on this arena — I verified it with the
repaired construction — but the instrument did not measure it, and
`MUT-FIBER` falsifies only the gate-layer variable, never the
construction.

**Repair (verified):** derive each declaration's one-excitation sector
from its own declared space —

```python
def one_excitation_object(W, grain, ceiling):
    space = set()
    for sh in SHAPES:
        for cfg in admissible_configs(grain, ceiling, sh):
            space |= set(cfg)
    cs = tuple(sorted(space))
    return {"configs": cs,
            "matrix": tuple(tuple(W[i][j] for j in cs) for i in cs),
            "born": tuple(tuple(absq(W[i][j]) for j in cs) for i in cs)}
```

with `objs[did] = one_excitation_object(W, grain, ceiling)` from each
declaration's own row.  Verified: **on the clean arena the published
numbers do not move** (53,460 comparisons, 0 disagreements — so the head
and the paper are untouched), and under the injection above the repaired
form reports 52,818 comparisons and **54 disagreements**.

### MAJOR-4 — the set equality is with the same-SITE set (27), not the same-ACTOR set (135); the receipt key, the head field and three paper sentences say "actor"

`build_census`:

```python
"carrier_grain_sources_are_the_same_actor_configurations":
    (r_carrier["source_set"] == same_site_cfgs   # <- same_SITE
     if r_carrier["leak_cells"] else None),
```

`same_actor_cfgs` is built two lines above and used only for the weaker
subset test.  Recomputed independently: **cells sharing a site = 27;
cells sharing an actor = 135**; and at every one of the 5 leaking coin
classes the carrier-grain leak source set is **equal to the 27 same-site
set and a proper subset of the 135 same-actor set**.

So the delivered sentence, in the abstract, in §6, in §9 and in claim
C09 —

> "the configurations that leak are exactly the 27 whose two excitations
> sit on cells sharing an actor"

— cannot be true as written: the set of configurations on cells sharing
an actor has 135 members.  The head field carries the same error:
`CARRIER-GRAIN-LEAK-SOURCES-ARE-THE-SAME-ACTOR-CONFIGURATIONS=5-OF-5`.

The numbers 27 and 5-of-5 are **right**; the characterisation is wrong.
The paper's own mechanism sentence in §6 states it correctly ("a row of
the walk operator is supported on the three cells of one site, so the
only sources … are pairs drawn from those three"), and the load-bearing
inference — every carrier-grain leak source is forbidden by the
actor-grain declaration — is **true** and is separately measured as
`carrier_grain_sources_share_an_actor: true`.

**Repair:** rename the receipt key and the head field to
`…-ARE-THE-SAME-SITE-CONFIGURATIONS`, and reword the three paper
instances to "exactly the 27 whose two excitations sit on two of the
three cells that meet at one site", keeping the (true) subset sentence
that carries the two-grains inference.  The 27 and the 5-of-5 do not
move.

### MAJOR-5 — E-24's denominator re-count covers 4 of 22 published ratios, and §10 says it covers all

`R["counting_only"]["enumerations"]` re-counts four denominators (coins,
actor-grain admissible, actor-grain forbidden, selection rows).  The head
publishes **22** `X-OF-Y` ratios; the paper publishes more.  §10:

> "and every published ratio's denominator is re-counted from the
> construction it claims to enumerate."

That is false at 4/22.  The E-24 engraving itself is satisfied (the
COUNTING-ONLY stamp is present, sealed and falsified, and no measure is
declared) — the defect is the instrument's description of its own reach.

**Repair:** either extend `enums` to every `pair(a, b)` field in
`field_spec` (each names two receipt paths; the denominator's
enumerating construction is already in the file for all of them), or
reword §10 to name the four.  The first is preferable and cheap.

### MAJOR-6 — "0 of 3 completions refuse a division" is decided by a predicate that ignores the completion (#87)

`p3_closure`:

```python
refusals = sum(1 for cid, field, _why in completions
               if sum(qocc) == 0)
```

`sum(qocc)` does not depend on `cid` or on `field`; the three
completions' emission fields **for the doubly occupied state Q are never
built** (E1/E2/E3 are built from P's occupation only).  The row is
therefore 0-or-3 by construction, and #87 is explicit: a per-object
obligation may not be discharged by a predicate that never sees the
object.  This is a head field
(`P3-COMPLETIONS-THAT-REFUSE-A-DIVISION=0-OF-3`), claim C07, and §5's
"all three keep the menu of a doubly occupied carrier nonempty".

**Repair:** build `qE1/qE2/qE3` from `qocc` exactly as `E1/E2/E3` are
built from `occ`, publish each completion's own Q-side total and
support, and set
`refusals = sum(1 for (cid, f) in zip(ids, (qE1, qE2, qE3)) if sum(f) == 0)`.
The published 0-of-3 is very unlikely to move, but it will then be
measured.

---

## 3. THE INDEPENDENCE THE TWO ROUTES DO NOT SUPPLY — supplied here

Because the delivered "two routes" share `t1`, `t2` and their loop
(row 7), I rebuilt the leak layer from nothing: my own Z[ω] as
polynomials mod x²+x+1, my own admissibility construction, my own zero
test, and the sector element read off an explicit 2×2 submatrix rather
than the delivered expression.  Taking only the six walk operators as
the object under test:

- **48 of 48 leak rows recomputed; ZERO mismatches** against the
  receipt's `leak_cells`, `leaking_sources`, `targets_reached` and
  `both_products_nonzero` (441,774 exact element evaluations).
- arena, independently: 27 cells, 27 distinct co-division pairs, 9
  actors in exactly 6 cells, 27 cells with exactly 2 actors, C(27,2) =
  351, same-site 27, same-actor 135, 216 = 351 − 135.
- pool, independently: 36 ring solutions, 6 classes, 1 Grover, the six
  coin names identical to the receipt's.
- paper-22's split recomputed from `afa46ffaf651`: 48 leaking + 16
  closed = 64 generators, 0 antisymmetric — matching the citation
  exactly, and `ceiling_is_anchored: false`.

**The measured physics of this unit stands.**  Every MAJOR above is
about how a true number is evidenced, not about the number.

---

## 4. MINOR FINDINGS

1. **E-23's mechanical and prose legs are substring tests.**
   `code_ok = any(declared[0] in s and declared[1] in s …)` and
   `prose_ok = moves in why and to in why`.  I shipped a falsifier whose
   declaration and prose both say it moves `leaking_cited` **to 4** while
   the code moves it to **47**; the run exited 0.  (The control — a wrong
   *symbol* name — dies.)  All 15 shipped descriptions I read by hand are
   correct; it is the certifier that is weak.  *Repair:* compare the
   declared value against `ast.unparse` of the `pick()` call's third
   argument, and match the prose on a word boundary.
2. **The staged `.tmp` files survive a terminal-gate failure.**  §10 and
   the docstring say "A run that fails any gate writes nothing and
   promotes nothing"; in the four post-write injections
   `occ_receipt.json.tmp` and `occ_output.txt.tmp` were left on disk.
   *Repair:* `try/finally` unlink on `GateFail`, and reword to "writes no
   delivered artifact and promotes nothing".
3. **The three verdict segments never appear in `occ_output.txt`.**  The
   paper says the head is "quoted exactly as the instrument emits it" —
   true against the JSON receipt only.  The human-readable transcript,
   which is the artifact a reader opens, does not carry the head it
   certifies.  *Repair:* `say()` the segments in `emit_report`.
4. **"three load-bearing tables" is four.**  `paper_tables` renders 23
   rows from the pool (6), the arms (6), the declarations (4) and the
   choice inventory (7); the gate statement and §10 both say three and
   name only the first three.  Coverage is *wider* than claimed, but the
   sealed statement is wrong.
5. **`STRUCTURAL_NUMERALS` is a 54-entry blanket whitelist of which 36
   are never used by this object** (the whole 13–34 range, the sixteen
   engraving numbers, 1296, 2026).  Only three paper numerals — `7`, `8`,
   `1/3` — actually need it, and it is the structural licence for `8`
   that let the §3 corruption "9 of the 27 → 8 of the 27" pass.  *Repair:*
   trim to what the object uses, and gate the unused set at zero.
6. **Licensing-pool self-description pollution.**  The pool is built from
   the whole receipt, so it includes the twelve sources' *byte lengths*
   and the eight anchors' *character counts* and ledger numbers embedded
   in provenance prose.  Demonstrated: `47` (a needle's char count — one
   away from the parent split), `3888` (a source's byte length) and `249`
   (the pin's ledger number) all pass as free prose numerals.  Digest
   exclusion is correctly implemented and is not the leak; the leak is
   that the instrument's *self-description* licenses physics numerals.
7. **P3's verdict word is a typed constant.**
   `"verdict": "SILENT-AND-VACUOUSLY-SATISFIED"` occurs exactly once in
   the file — in the return dict — and no gate re-derives it, unlike P2's
   word, which is derived and compared (`p2_verdict == p2_derived`).  It
   is a head field and a column in all six arm rows.  §10's careful
   wording ("the turning premise's own word is derived") is technically
   honest but the reader will generalise.  *Repair:* derive it from the
   three legs and add the comparison, mirroring `G-P2-TURNING`.
8. **Two aggregate-shaped predicates.**  `all(g["passed"] for g in
   LD.rows)` in `G-PAPER-COVERAGE-FINAL` is structurally always true
   (`Ledger.gate` raises on failure), and `G-ARMS-REACHABILITY` binds
   `len(words_seen) >= 4` where the per-object form is
   `words_seen == set(OUTCOMES)` (equivalent here, since |OUTCOMES| = 4,
   but #87-shaped).  Also: the CLI contract block does not disclose the
   exit codes of `--mutant` (on-target → 1) or `--break-anchor`, though
   it does for `--selftest`.

---

## 5. THE INJECTIONS TABLE

Every row executed off-tree against the delivered bytes.  "died" = exit
1 at the named gate with the delivered artifacts byte-unchanged.

| # | injection | result |
|---|---|---|
| I-01 | extra forged `OCC-CEILING-FORCED` fenced block | **SURVIVED (MAJOR-1)** |
| I-02 | exact duplicate of a derived head block | died `G-PAPER-HEAD-VERBATIM` |
| I-03 | clean head block + forged twin (`CARRIER-CELLS=26`) | **SURVIVED (MAJOR-1)** |
| I-04 | I-01/I-03 after the `blockmap == want` repair | died `G-PAPER-HEAD-VERBATIM` (pristine still passes) |
| I-05 | coin-table cell swap (monomial class made to leak 81) | died `G-PAPER-TABLES` |
| I-06 | control-arm table: `OCC-CEILING-FORCED`↔`OCC-CEILING-OPEN` between C1 and C2 | died `G-PAPER-TABLES` |
| I-07 | arms table: A1/A2 P4 verdicts `SELECTS`↔`NO-SHAPE-CLOSES` | died `G-PAPER-TABLES` |
| I-08 | declaration (grain) table: 378↔351 within a row | died `G-PAPER-TABLES` |
| I-09 | choice table: `verdict_determining` no→YES | died `G-PAPER-TABLES` |
| I-10 | coin / arm / declaration table pure row reorders (×3) | survived — semantically null (rows self-keyed) |
| I-11 | inline span `D-CARRIER-2`→`D-CARRIER-999` | died `G-PAPER-TABLES` |
| I-12 | unlicensed `999` in prose | died `G-PAPER-NUMERAL-COVERAGE` |
| I-13 | unlicensed `999999` in a new inline span | died `G-PAPER-NUMERAL-COVERAGE` |
| I-14 | unlicensed `999999` in a new fenced block | died `G-PAPER-NUMERAL-COVERAGE` |
| I-15 | polluted `47` / `3888` / `249` in prose | **SURVIVED ×3 (MINOR-6)** |
| I-16 | abstract: 216↔135 swapped | **SURVIVED (MAJOR-2)** |
| I-17 | abstract: `53,460 of 53,460` → `216 of 216` | **SURVIVED (MAJOR-2)** |
| I-18 | abstract: carrier-grain leak `81`→`864` | **SURVIVED (MAJOR-2)** |
| I-19 | §2: `36 solutions`→`37` | **SURVIVED (MAJOR-2)** |
| I-20 | §3: "reaches 9 of the 27"→"8 of the 27" | **SURVIVED (MAJOR-2)** |
| I-21 | I-16..I-19 after the C16–C19 repair | died `G-PAPER-CLAIMS` (pristine still passes) |
| I-22 | staged JSON verdict word corrupted after write | died `G-ARTIFACT-INTEGRITY` |
| I-23 | staged transcript line appended after write | died `G-ARTIFACT-INTEGRITY` |
| I-24 | staged JSON deep sealed leak count corrupted | died `G-ARTIFACT-INTEGRITY` |
| I-25 | staged JSON declared-unsealed chain leg corrupted | died `G-ARTIFACT-INTEGRITY` |
| I-26 | mid-window forgery of `p1/carrier_cells` after its seal | died `G-PAPER-CLAIMS` |
| I-27 | mid-window forgery of a sealed leak count | died `G-PAPER-CLAIMS` |
| I-28 | mid-window forgery of `arms[0]/word` | died `G-VERDICT-RECONSTRUCTED` |
| I-29 | `G-SEAL-COMPLETE` call deleted from `finish` | died `G-MUTANTS-ON-TARGET` |
| I-30 | `G-ARTIFACT-INTEGRITY` call deleted | died `G-MUTANTS-ON-TARGET` |
| I-31 | `os.replace` lifted above the terminal gate | died `G-MUTANTS-ON-TARGET` |
| I-32 | extra `open(...)` inside `finish` | died `G-SELFTEST-WRITES-NOTHING` |
| I-33 | falsifier declares `to = 4` while the code moves to `47` | **SURVIVED (MINOR-1)** |
| I-34 | falsifier declares a wrong symbol name | died `G-MUTANTS-ON-TARGET` |
| I-35 | declarations made to differ genuinely at one excitation | **published row unchanged (MAJOR-3)** |
| I-36 | I-35 after the `one_excitation_object` repair | 54 disagreements; clean arena unmoved |
| I-37 | `--break-anchor` × 12 sources | died `G-PROVENANCE` 12/12 |
| I-38 | 50 declared mutants, separate processes | died at their named gate 50/50 |
| I-39 | 25 hostile argv vectors | exit 2, 25/25 |
| I-40 | bare copy, no pinned sources | loud abort `G-PROVENANCE`, wrote nothing |

---

## 6. THE SEAM RULING

The seam this seat is asked to rule on is between **what the instrument
measures** and **what the paper says it measures**, and the ruling is
that the seam is real but narrow and one-directional: in every case the
paper claims *more instrument* than exists, and in no case did I find a
measured number that was wrong.  I attacked the numbers hardest — a
from-scratch rebuild of the entire leak layer in a different arithmetic
— and got 48/48 agreement and zero mismatches.

Three of the six MAJORs are the same defect wearing three coats: a
predicate that cannot fail (`multiset_ok` over a one-sided multiset;
`va != vb` over one object; `sum(qocc) == 0` over three identical
evaluations).  In each the *conclusion* is true and the *evidence* is
circular, and in each the repair is short and leaves the published value
where it is.  That is the shape of an AWF, not an R.

The two remaining MAJORs are of a different kind and matter more for the
adjudication: MAJOR-4 puts a **false characterisation into a delivered
head field and three paper sentences** (the equality is with the 27
same-site configurations, not with the 135 same-actor ones), and MAJOR-2
shows the paper's **abstract is outside the instrument** — the four
sentences a reader will quote are the four I was able to corrupt at exit
0.  Both should be repaired before terminal, and MAJOR-4 changes a
sealed head field name, so it is a re-delivery, not an erratum.

Nothing here touches the verdict.  `OCC-CEILING-OPEN` is supported by P2
alone (`NOT-AVAILABLE` ⟹ OPEN in the head law, on both routes), and the
P2 word is the one word in the unit that *is* derived from its legs and
gate-compared against that derivation.  The two-way control does what
the pin asked: the same instrument returns `OCC-CEILING-FORCED` on the
subset carrier and `OCC-CEILING-OPEN` on the multiset one, and I
verified both arms' words are computed by the same `head_law` and
re-derived by the comparator.

**Grade: AWF.**  Repair orders R-OCC-K3-1..6 = the six MAJOR repairs
above (three verified in place), plus the eight MINORs, of which 2, 3, 4
and 8 are wording-and-one-line fixes and 1, 5, 6, 7 are small mechanical
ones.
