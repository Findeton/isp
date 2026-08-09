# R6a — HOSTILE REVIEW, INSTRUMENT LENS (R3)

**Protocol:** `v14/note-r6a-hostile-protocol.md` (`02d249f22f6f`), K5 primary, all
kill-shots at instrument depth.  **Pin:** `v14/note-r6a-refinement-grammar-pin.md`
(`a22582f67168`).  **Object:** the frozen R6a delivery, hashes verified before any
work and re-verified after all of it — paper `af5b7f26e427`, code `ea914c6b55aa`,
output `a04b97d2b7bc`, receipt `022c3f488a93`: **all four unchanged.**  The five
byte-anchor targets are also unchanged (`a22582f67168`, `e9d2bedff244`,
`542b8735daf0`, `f286ba10d2d9`, `d44cb72f8ee9`).  **Discipline:** scratch-only;
nothing imported from the unit; subprocess invocation of its CLI only; read-only
git; `v14/paper-03-*` and `v14/code/r3_*` never opened.  This file is my single
repo write.

**GRADE: ACCEPT-WITH-FIXES.**

The measurement is right and it is right everywhere I could reach.  A from-scratch
re-implementation written from the paper's declared spec, importing nothing and
using different algorithms (BFS decompositions, closed-form 2×2 algebra),
reproduces the record family and both rejection modes, the readout determinant,
record-IS-metric at 81 of 81, the lapse-bracket ranks, the min axis cycle sums,
the whole move census including every tally cell, the 16/12 completion sweep, the
single-interval arithmetic, the d = 3 gap, 972/972 and 324/324, all 36 build rows,
every split fiber (raw and admissible) and every equivariant fiber, the 361/261/1
count-lattice census, 54 of 108, the 64 witnesses, the full 11 088-cell
commutation-defect census (7 112 / 3 976, the four-class support table, the
per-rule table, the 49 896/49 896 closed form), 30 of 81, 0 of 207, the iteration
table and the growth table: **624 receipt/paper cells recomputed independently,
zero mismatches, and zero false numbers by value anywhere in the paper.**  Three
plain runs on a scratch copy are byte-identical to the committed artifacts.  All
**34** declared mutants die at exit 1 on **exactly** their declared gate, with
zero tracebacks and both artifacts byte-unchanged after each.  The verdict rebuilds
from the receipt alone, byte-identically, and all twelve segments flip under my own
targeted receipt perturbations.  Three genuine advances over R2 are worth naming:
the verdict comparator really is independent (all six verdict injections die on
it), the flippability gate tests the *reconstructor at the measurement* rather
than string concatenation, and the new prose gate works.

What fails is again the **protection**, and one substantive claim.

1. **The no-potential theorem's mechanism sentence is false.** Five of the nine
   admissible records — exactly the $q_{12}=0$ ones, including `G-FLAT`,
   `G-CURVED` and `G-DIAG2` — **are** coboundaries of an explicit site function on
   the universal cover $\mathbb Z^2$.  For `G-DIAG2` that potential, interpolated
   by the very rule §6.1 derives as dynamics-forced, yields a **fully admissible
   canonical refinement with fiber 1** which restricts exactly to the coarse
   record — and which the unit already builds, and classifies as class-(iii) with
   fiber 19 683.
2. **Twelve injection classes survive undetected** at exit 0 with 48/48 gates
   green and both artifacts written, including two recurrences of #219 and a
   recurrence of #24.  Under eight of them the *only* thing that stops delivery
   against the frozen paper is `G-PROSE-RENDERS-FROM-THE-RECEIPT` — a consistency
   check against a file the repair worker regenerates.
3. **The waiver table is mostly false.**  Fifteen of the twenty waivers assert
   coverage by a named mutant.  In **0 of 15** does that mutant falsify the gate it
   is said to cover: ten are shadowed (the gate is never evaluated under it), five
   reach the gate and pass.  I killed eleven of the twenty waived gates with
   targeted injections, so their implied "cannot fail" is false too.

Every repair below is definite.

---

## Execution counts

| | |
|---|---|
| plain delivery runs on the scratch copy | **3** (all `a04b97d2b7bc` / `022c3f488a93`, identical to the committed artifacts) |
| CLI-contract probes (`--list-mutants`, unknown arg, unknown mutant, `--mutant` with no name) | **4** |
| independent 34-mutant falsifier audit (my own runs) | **34** |
| `--selftest` (1 top-level + 34 spawned subprocesses) | **35** |
| crafted injections (source patches, source-file corruptions, paper regenerations) | **40** |
| **total process-level executions of the unit's CLI** | **116** |
| independent programs written from the declared spec | **6** |
| receipt/paper cells recomputed independently | **624** (0 mismatches) |
| commutation-defect census cells recomputed from scratch | **11 088** (×2, corrupted variant included) |
| split-triple enumerations recomputed | **9 records × 9 sites + 361-vector box** |
| anchors traced (5 file-bytes + 17 path-value + 10 verbatim text) | **32** |
| verdict rebuilds from the receipt alone | **1** (12 segments, byte-identical) + 12 flips + 2 head reachability probes |

---

# FINDINGS, most severe first

## M1 (MAJOR) — the no-potential theorem is true only on the periodic lattice, and the sentence it is used for is false: five of nine records DO carry a potential on the cover, and for `G-DIAG2` it forces the split

§2 states, unqualified:

> **The no-potential theorem.** No record's counts are the coboundary of a site
> function.

and then draws the load-bearing consequence:

> There is no such $\varphi$, so the splitting datum a refinement needs is exactly
> the datum the record does not carry.

and §5.3 leans on it again ("by §2's no-potential theorem it cannot be").

The *proof* is correct and does name periodicity ("a coboundary sums to zero
around every cycle of the periodic lattice").  The *statement* and the mechanism
sentence do not.  Measured, over the nine admissible records: the counts are a
coboundary of a site function on the universal cover $\mathbb Z^2$ **exactly when
$q_{12}=0$**, which holds at five of the nine:

| record | cover potential $\varphi$ | $q_{12}$ |
|---|---|---|
| `G-FLAT` | $x_1+x_2$ | 0 |
| `G-DIAG2` | $2x_1+2x_2$ | 0 |
| `G-ANISO` | $x_1+4x_2$ | 0 |
| `G-ANISO2` | $4x_1+9x_2$ | 0 |
| `G-CURVED` | $\tfrac{x_1(x_1+1)}2+\tfrac{x_2(x_2+1)}2$ | 0 |
| `G-CURVOFF`, `G-OFFDIAG`, `G-OFFDIAG2`, `G-OFFNEG` | none (curl obstruction) | 1, 1, 2, −2 |

Each was verified by checking the unit-plaquette curl and the two-step diagonal
consistency at all nine sites, and the two explicit $\varphi$ above were checked
against the record cell by cell.

The sharp consequence.  Take `G-DIAG2` $(2,2,4)$, lift $\varphi=2x_1+2x_2$ to the
refined lattice by the count-weighted interpolation — **the same interpolation
§6.1 derives as the unique dynamics-compatible lift** — i.e. $\Phi(z)=z_1+z_2$ on
$(\mathbb Z_6)^2$.  Then, measured:

- the refined counts are $(1,1,2)$ at **every** one of the 36 refined sites;
- **0 of 36** refined sites are inadmissible;
- the coarse record is recovered at **9 of 9** sites;
- the split is $(1,1)$ on every axis interval and $(2,2)$ on every diagonal —
  **fiber 1**, determined by the record's own counts up to the one interpolation
  declaration;
- and this object is **already in the unit's build set**: it is exactly
  `G-DIAG2 @ floor + minimal`, which §4's table reports as admissible.

So for at least one record of the declared family the record *does* carry the
splitting datum, and the unit builds the canonical refinement without recognising
it.  The verdict is not necessarily overturned — class (i) demands a *named pinned
declaration*, and the cover potential is not named in I7 — but §2's mechanism
sentence, §5.3's appeal to it, and §11 Open 2 ("a grammar in which they are … would
be a different substrate") are all wrong as written, because the counts of five
declared records already are.

**Repair (definite).**  (a) Restate the theorem with its scope: *"No record's
counts are the coboundary of a site function **on the periodic lattice $X$**."*
(b) Replace the mechanism sentence with the measured one: *"On the universal cover
the counts of five of the nine admissible records — exactly those with $q_{12}=0$
— are coboundaries; what the periodic record fails to carry is not a potential but
a potential's **value at the interior site**, and supplying one is the count-weighted
interpolation of §6.1, integral only when the interval count is even."*  (c) Add
`G-DIAG2`'s canonical refinement to §5.1 as the exhibited case and say why it is
still class (iii) under the unit's own classification rule (no pinned declaration
names the interpolation for the *geometry* record — only §6.1's dynamics argument
does, for the *front*).  (d) Add a gate: measure the cover-potential census (curl +
diagonal consistency per record) and print it; it is nine cheap checks and it is
the honest form of the theorem.  This is K1's answer at instrument depth and I hand
the adjudication of (c) to the operator and effectus lenses.

---

## M2 (MAJOR) — twelve injection classes survive undetected; every substantive census gate is green under corruptions it was written to catch. Two #219 recurrences and one #24 recurrence

Each row below is a complete plain run of a patched scratch copy: `exit 0`,
**48/48 gates PASS, 0 FAIL, 0 tracebacks, both artifacts written**, `never_falsified`
still 20.  "paper regenerated" means I also updated the paper's affected rendered
claim(s) — exactly what a repair worker does, and the only reason the run is not
stopped by `G-PROSE-RENDERS-FROM-THE-RECEIPT`.

| id | corruption | delivered result | paper regenerated? |
|---|---|---|---|
| **S1** | 7 receipt cells corrupted after their gates (R1's INJ_D class) | `no_potential.G-FLAT = 99` (true 3), `split_fibers.G-CURVOFF.admissible_at_images = 7` (true 64 562 400 000), `stabilisers.G-DIAG2.order = 1` (true 18), `per_rule.B-all.nonzero = 1` (true 672), closed form → `"D = 0 at 1 of 2 cells"`, `admissible_builds = 99` (true 28), `iteration.G-ANISO2.ceiling = 9` (true 2) — **all seven reach the receipt AND `output.txt`** | no |
| **W1** | drop one hyperplane locus **inside** `declared_moves()` | `CLASSES=…\|BLOCKED:2` — an entire move class silently absent, `G-MOVE-CENSUS-CELL-COMPLETE` green | yes |
| **X1** | drop the last admissible triple inside `site_admissible_triples()` | `SPLIT-FIBER=MIN-512-MAX-1207269217792000000000` (true 19 683 / 1.2576e21), `G-FIBER-COMPUTED` green | yes |
| **Y1** | zero the defect on the all-odd parity class inside `commutation_defect()` | `MID-(1, 1):0-OF-99792` — **16 079 nonzero defect values erased** — and `G-DEFECT-NONZERO`, `G-DEFECT-CLOSED-FORM`, `G-DEFECT-CHARACTERISED`, `G-DEFECT-SPLIT-DEPENDENCE` **all green** | yes |
| **Y2** | halve the IMAGE row of the support tally before both `sup_sig` and the receipt | `SUPPORT-IMAGE:5600-OF-99792` (true 16 296), `G-DEFECT-CHARACTERISED` green | yes |
| **W5** | `ceiling+1` and `steps+1` together in `iteration_probe()` | `ITERATION=FAMILY-FINITE-CEILING-3-ATTAINED-3`, `G-ITERATION-CEILING` green | yes |
| **W2** | the typed literal `"candidates_per_interval": 2` → 5 | `BLOCKED-AT=…-5-CANDIDATES` | yes |
| **W3** | the hand-written `targets` dict gains a second `True` | `REFUSED-AT=…LINK-TARGETS-2-OF-3` | yes |
| **W4** | the typed literal `"infinite_family": {"witnesses": 64}` → 999 | `FREE-LINKS=54-OF-108-FIBER-INFINITE-WITNESSES-999` | yes |
| **S2** | a waiver's text replaced by a false statement | receipt ships `"G-DEFECT-CLOSED-FORM": "FULLY FALSIFIED by three independent mutants; no coverage gap"` | no |
| **S3b** | one mutant's `expected_gate` retargeted + one waiver line moved | `falsifier_map` ships `G-CACHE-EXERCISED: ['cache-alias']` — a mutant that in fact dies on `G-CACHE-FRESH-EQUALS-MEMO` — with `never_falsified` still 20 | no |
| **T1** | the pinned sentence's **meaning** inverted in the source, needle preserved (see M5) | 10/10 verbatim-text anchors green | no |

A thirteenth, **V5** (one record silently dropped from the forced part →
`ADDITIVITY-810-OF-810`, `RESTRICTION-270-OF-270`), passed `G-ADDITIVITY-FORCED`,
`G-RESTRICTION-COMMUTES`, `G-FIBER-COMPUTED` and `G-STABILIZER-MEASURED` and died
only at the paper; I did not regenerate its (larger) claim set, so I do not count
it as a survivor — but there is no cell-completeness gate over the record family,
and that is the same hole W1 exhibits over the move family.

The three named diseases:

**#219 recurrence, twice** (RUNBOOK §14 addendum, v13 #219: *"a gate clause that
compares an object against a copy of itself routed through the very component under
test verifies nothing"*).  Per the #313 addendum a recurrence of an engraved disease
is a MAJOR by default and must be named as a recurrence.

- `G-FIBER-COMPUTED` claims "the admissible fiber equals **an independent
  recomputation** of the product over coarse sites of that site's admissible split
  triples".  It is not independent: `split_fibers()` computes
  `len(site_admissible_triples(row, links))` and multiplies; the "recomputation"
  computes `len(site_admissible_triples(a.counts[x], a.links))` and multiplies.
  Same function, same input.  X1 proves it.  The declared `fiber-typed` mutant dies
  only because it perturbs the value *after* the shared call returns.  **This is the
  gate the protocol's K5(d) names, and it does not have the property claimed.**
- `G-MOVE-CENSUS-CELL-COMPLETE` gates `len(rows) == len(declared_moves(d, L))`,
  where `rows` came from `declared_moves(d, L)`.  W1 proves it.  The declared
  `census-drop` mutant dies only because it filters *after* the call.
- `G-DEFECT-CHARACTERISED` gates `sup_sig == sig_check`, where both are the same
  join expression over the same `support_tally`.  Y2 proves it.  The declared
  `defect-support-lax` mutant dies only because it replaces the string *after* the
  table is built.

The compliance sweep's #219 row is therefore false as a compliance claim.  It reads
"APPLIED — the restriction test's comparator is the coarse record's own q, built by
a route the restriction does not touch" (which I verified and is true) and omits
the three gates above.

**#24 recurrence** (*counts computed, never typed*).  Four load-bearing numbers are
typed literals with no measurement behind them: `"candidates_per_interval": 2`
(the census *does* compute `ncand` per interval and stores it in the rows, then the
summary types it), `targets = {"axis-along-the-split": True}` giving
`declared_link_targets_defined_at_the_new_site = 1`, `"infinite_family":
{"witnesses": 64}`, and `"mutant_survivors": 0`.  W2/W3/W4 ship each of them at
exit 0.  (All four values happen to be *correct* — I verified every one — but they
are asserted, and the paper's verdict segments carry them.)  A fifth, the prose
template's typed **"six"** in `"…over the six records that admit the move…"`, is
covered under M7.

**Repairs.**  (i) `G-FIBER-COMPUTED`: build the comparator by a genuinely different
route — e.g. count, for each coarse site, the lattice points of the admissible
region $\{(a,b,c): 1\le a<n_1,\ 1\le b<n_2,\ 1\le c<n_3,\ 4ab>(c-a-b)^2\}$ by a
closed-form/summation argument over $c$ — and gate the two against each other; add
a mutant that perturbs `site_admissible_triples` itself.  (ii)
`G-MOVE-CENSUS-CELL-COMPLETE`: gate the census against a *declared constant*
(`1 + L + 1 + 1` classes at $d=2$, computed from $L$, not from the constructor) and
against the declared per-class denominator; add a mutant that drops a class inside
`declared_moves`.  (iii) `G-DEFECT-CHARACTERISED`: rebuild the support totals from
a second pass over the stored defect fields, not from the accumulator; add a mutant
that perturbs `support_tally`.  (iv) Compute the four typed constants
(`max(r["candidates"] for r in ambiguous rows)`; the link-target count by actually
testing whether `add(y, lk)` lands in the declared site set; the witness count from
the loop's own successes; the mutant survivor count by running the table).  (v) Add
a record-family cell-completeness gate to the forced part (`len(splittable) +
len(unsplittable) == len(adm_names)` **and** `additivity_checks ==
len(splittable) * |SPLIT_RULES| * |FREE_RULES| * ncoarse`).

---

## M3 (MAJOR) — the waiver audit: 15 of 20 waivers claim coverage by a named mutant and 0 of 15 hold; 11 of the 20 waived gates are demonstrably falsifiable

The unit's census is honest about its denominator — **20 of 48 gates carry no
declared falsifier, all 20 waived** — and that is a real advance on R2 (which
carried no census at all).  The waivers themselves do not hold up.

Method: gate registration order read from the delivered receipt; each named mutant
run and its death gate compared; then a targeted injection per waived gate to test
"cannot fail on any input".

| # | waived gate | idx | waiver's stated forcing | measured verdict |
|---|---|---|---|---|
| 1 | `G-NO-MUTANT-IDENTITY` | 1 | "self-validating: the detector is proved able to fire by two synthetic injections inside the gate" | **GENUINE** — and the gate itself fires: **P1** (a second function reading `MUTANT`) → exit 1 on this gate |
| 2 | `A-R0-PIN` | 3 | "the anchor-hash channel is falsified at three of the five rows … and at this unit's own pin" | **GENUINE at channel level** (4 of 5 rows have a mutant). The row itself works: **P8** (byte-corrupt the founding pin) → exit 1 on `A-R0-PIN`. `anchor-skip` reaches this gate and passes |
| 3 | `G-RECORD-FAMILY-REPRODUCES-I7` | 10 | "exercised by readout-det, rank-lax and lattice-drop" | **FALSE** — all three reach the gate and **pass**; none can falsify it. The gate has real teeth: **P4** (corrupt `curvoff_rule`) and **P6** (corrupt the readout matrix coefficient) both → exit 1 here |
| 4 | `G-RECORD-IS-METRIC` | 12 | "covered by readout-det (the same readout)" | **FALSE — SHADOWED**: `readout-det` dies at `G-READOUT-REENCODING` (idx 11); this gate is never evaluated. I could exhibit **no** input that reaches it: every readout/solver corruption dies at idx 10 or 11 first. It is a third check on an object already checked twice |
| 5 | `G-BLOCK-IS-REAL` | 18 | "covered by incidence-lax at the paired gate" | **FALSE — SHADOWED** (`incidence-lax` dies at idx 17). Predicate `dis > 0` is forced: over the 16 declared completions the condition is $f_0\neq f_1$, true at 12. **P2** kills it only by editing the predicate |
| 6 | `G-DIMENSION-EXTENSION` | 19 | "analytically forced … a disclosure, not a must-pass falsifiable gate (#208)" | **REASON GENUINE, FORM WRONG** — the waiver cites #208 to excuse a gate that #208 says must not be must-pass, and `record()` exists in the source and is called **zero** times. The gate does have teeth: **P3** (add the body diagonal at $d=3$) → exit 1 here |
| 7 | `G-UNSPLITTABLE-RECORDS` | 22 | "covered by fiber-typed (the same counts)" | **FALSE** — `fiber-typed` reaches this gate and **passes** (it dies at idx 23). The `all(min_count()==1)` clause is a tautology for positive integers; only `len(unsplittable) > 0` has content, and that is a property of the anchored family |
| 8 | `G-FREE-LINKS-INFINITE` | 25 | "covered by fiber-typed (the same fiber object)" | **FALSE — SHADOWED** (idx 23 < 25). `wit == 64` is forced: $\det q = 3b>0$ for all 64 trials. **P9** kills it only by editing the loop bound |
| 9 | `G-LIFT-GRID-CELL-COMPLETE` | 26 | "covered by forcedlift-lax at the paired gate" | **FALSE** — `forcedlift-lax` reaches this gate and **passes** (dies at idx 27). Real gate: **P5** (make `lift_profile` ignore `mode`) → exit 1 here |
| 10 | `G-DEFECT-CLOSED-FORM` | 29 | "covered collaterally by defect-suppress (which moves the same field)" | **FALSE TWICE** — SHADOWED (idx 28 < 29), *and* `defect-suppress` moves the nonzero **cell counter**, not `image_equals_coarse_drag`. Y1 shows the gate passes with a quarter of the defect erased |
| 11 | `G-DEFECT-SPLIT-DEPENDENCE` | 31 | "covered collaterally by fiber-typed and additivity-violation, both of which move the split fiber this gate probes" | **FALSE TWICE** — both SHADOWED (idx 23, 20 < 31), *and* neither touches this gate's probe, which builds its own splits. Real gate: **P13** → exit 1 here |
| 12 | `G-INVENTORY-TREND` | 33 | "the growth law is arithmetic in the arena's volume factor; iteration-lax falsifies the neighbouring ceiling gate" | **FIRST HALF GENUINE** (`inventory_growth` is closed-form arithmetic in $L,d$ and reads no measurement); second half SHADOWED and decorative |
| 13 | `G-CACHE-EXERCISED` | 35 | "covered by cache-alias at the paired gate" | **FALSE as coverage** (`cache-alias` reaches and passes; it dies at idx 36) but the predicate is structurally forced. **P10** kills it only by disabling the memo |
| 14 | `G-MOTIVATION-QUALIFIER-COMPUTED` | 38 | "pure function of the class counts … a separate injection would test the same arithmetic twice" | **GENUINE** — the predicate is a tautology given the line above it |
| 15 | `G-VERDICT-SEGMENTS-FLIPPABLE` | 40 | "covered by verdict-inert-segment" | **FALSE TWICE** — SHADOWED (idx 39 < 40), *and* that mutant perturbs the **builder** while this gate tests the **reconstructor**. Real gate: **P11** (hard-code one segment field in `reconstruct_verdict_from_receipt`) → exit 1 here |
| 16 | `G-VERDICT-ALL-HEADS-REACHABLE` | 41 | "covered by head-constant" | **FALSE TWICE** — SHADOWED (idx 39 < 41), and `head-constant` pins the builder's head, not the reconstructor's. Real gate: **P12** (constant head in the reconstructor) → exit 1 here |
| 17 | `G-NO-FLOATS-IN-RECEIPT` | 43 | "covered by float-leak at the source-level gate" | **FALSE as coverage** — SHADOWED (idx 0 < 43) — but genuinely forced downstream of `G-FLOATGUARD` |
| 18 | `G-DEFERRED-GATES-EVALUATED` | 44 | "an arithmetic consistency check on the ledger" | **GENUINE** (tautology) |
| 19 | `G-FALSIFIER-CENSUS-HONEST` | 45 | "registers itself after it evaluates … an arithmetic consistency check … carries no separate injection" | **UNDERSTATED** — it is *not* a consistency check, it is a live gate: **S2b** (remove one waiver) and **S3** (retarget a mutant without moving its waiver) both → exit 1 here. It should carry a mutant |
| 20 | `G-FINAL-GATE-COUNT` | 47 | "an arithmetic consistency check on the ledger" | **GENUINE** (tautology) |

**Honest denominators.**  48 gates; 28 falsified by 34 mutants naming 28 distinct
gates; 20 never falsified, 20 waived, 0 unwaived.  Of the 20 waivers: **6 genuine**
(#1, #2, #12-first-half, #14, #18, #20), **1 reason-genuine/form-wrong** (#6),
**1 understated** (#19), **12 false or false-in-part**.  Of the 20 waived gates,
**11 are demonstrably falsifiable** (I killed each: P1, P3, P4/P6, P5, P8, P10,
P11, P12, P13, and #19 via S2b/S3) and therefore have no forcing at all — they are
simply unprotected; **8 cannot fail on any input the anchors admit** (#5, #7-in-part,
#8, #13, #14, #17, #18, #20) and belong in `record()` as disclosures under #208;
**1** (#4) cannot be reached by any falsifier at all.

There is also a **dead waiver entry**: `NEVER_FALSIFIED_WAIVERS` carries
`"G-ANCHOR-CELL-COMPLETE": "covered by anchor-skip"`, but that gate *is* falsified
by `anchor-skip`, so the entry never surfaces in the receipt.  Nothing gates the
waiver dict against extraneous keys.

**Repair.**  (a) Rewrite every waiver to state what is *measured*, in one of exactly
three forms: `FALSIFIED-AT <gate> BY <mutant>` (only when the mutant's death gate
**is** this gate), `FORCED: <the algebraic reason it cannot fail>`, or
`UNPROTECTED: no falsifier`.  (b) Add a gate that checks the shadowing arithmetic
itself: for every waiver of the form "covered by X", assert that X's
`expected_gate` equals the waived gate.  That single gate turns twelve of the false
rows into failures.  (c) Add falsifiers for the eleven falsifiable waived gates —
I supplied a working injection for each above.  (d) Gate the waiver dict against
keys that are not in `never_falsified`.

---

## M4 (MEDIUM) — the falsifier census is a claim about declared strings, never about measured deaths; the delivery run runs no mutant

`finalise_census()` builds `falsifier_map` from `MUTANTS[*]["expected_gate"]` —
strings a worker types — and `R["totals"]["mutant_survivors"] = 0` is a typed
literal.  `--selftest` does run the table (I confirmed: 34/34 DEAD, exit 0,
artifacts byte-unchanged), but it writes nothing into the artifacts.  A reader of
`r6a_refinement_receipt.json` has no evidence that any mutant was ever run.  This
is R2's M9 recurring with a new surface: the census that R2's review asked for now
exists, and it is denominated over *declarations*.

Measured: **S3b** retargets `cache-alias`'s `expected_gate` to `G-CACHE-EXERCISED`
and moves one waiver line; the delivery ships at exit 0 with
`falsifier_map["G-CACHE-EXERCISED"] = ["cache-alias"]`, `never_falsified_count`
still 20 — while the mutant in fact dies on `G-CACHE-FRESH-EQUALS-MEMO`.  **S2**
ships an arbitrary false waiver string; nothing compares waiver text to anything.

**Repair.**  Run the mutant table in-delivery (guarded by `if not MUTANT`), record
per-mutant exit code and the gate actually named in the death certificate, and
gate `actual_gate == expected_gate` for every row.  Then `falsifier_map` becomes a
measurement and the paper's "34 mutants, no survivors" is carried by the artifacts.

---

## M5 (MEDIUM) — the verbatim-text anchor, first deployment: it binds EXISTENCE only. Recommendation: ADOPT WITH MODIFICATION

The mechanism is `probe in open(pinned_source).read()` for each of ten
load-bearing sentences.  Three measurements:

- **T3 — source drift without rehash.**  Alter the quoted sentence in the pinned
  HA paper: `exit 1` on **`A-HA-PAPER`** (idx 5), never reaching `G-TEXT-ANCHORS`
  (idx 9).  Because both text-anchor sources (`v13/paper-ha-successor.md`,
  `v14/note-r6a-refinement-grammar-pin.md`) are *also* byte-anchored and their
  byte anchors are evaluated first, **no drift in a pinned source can ever reach
  the text anchor.**  Against source drift the ten text anchors add nothing to the
  two byte anchors.
- **T2 — needle removed, byte anchor updated.**  `exit 1` on `G-TEXT-ANCHORS`.
  The gate works when it is reachable.
- **T1 — meaning inverted, needle preserved, byte anchor updated.**  I rewrote the
  pinned source to read *"we explicitly REPEAL the requirement that the interval
  cardinality $n_\ell(x)\in\mathbb Z_{>0}$ and allow zero and negative counts"*.
  Result: **exit 0, 48/48 gates green, 10/10 verbatim-text anchors green**, verdict
  unchanged.  The unit's entire count-1-unsplittability argument, its ceiling
  theorem and its no-potential theorem all rest on that sentence, and every one of
  them survives the sentence's repeal.

So the anchor's real content is: *the unit has not paraphrased its own quotation*
— a guard against the **instrument** drifting, not against the **source** drifting
and not against the sentence meaning something else.  It binds existence, not use.
Nothing in the unit connects `T-COUNTS-POSITIVE` to the code that enforces
`n \ge 1`, or `T-COUNTS-SEMANTIC` to the additivity constraint.

**Recommendation for the era: ADOPT WITH MODIFICATION.**  The kind is worth
keeping — it is cheap, it is the only anchor that quotes rather than paraphrases,
and it makes the grammar auditable by a reader.  Three modifications make it carry
weight:

1. **Order it before the byte anchors, or exempt its sources from byte-anchoring.**
   As shipped it is unreachable by source drift.  Evaluating `G-TEXT-ANCHORS`
   *before* `verify_anchors()` costs nothing and makes a sentence-level drift die
   with a sentence-level message.
2. **Bind each anchor to a USE.**  Every text-anchor row should name the gate or
   the code predicate it licenses, and that pairing should be gated: e.g.
   `T-COUNTS-POSITIVE → G-UNSPLITTABLE-RECORDS`, `T-COUNTS-SEMANTIC →
   G-ADDITIVITY-FORCED`, `T-FRONT → G-FORCED-LIFT-NON-INTEGRAL`.  A row with no
   named consumer is decoration.
3. **Anchor the sentence's local context, not a fragment.**  Quote enough
   surrounding text (or anchor a *window* hash: the sha of the 200 bytes centred on
   the needle) that a negation or a repeal cannot be inserted around it.  T1 is
   defeated by this alone.

Without (1) and (3) the kind is strictly weaker than the byte anchor it sits behind;
with them it is the first anchor in the programme that would catch a source whose
*bytes* changed legitimately but whose *claim* changed with them.

---

## M6 (MEDIUM) — §3.2's "measured, not argued" is false: the SINGLE-INTERVAL refusal is a hand-written table

§3.2 reads: *"The refusal is arithmetic and it is measured, not argued: the
direction-0 cycle lengths become [4, 3, 3], 10 sites is not divisible by the
longest cycle 4, and only 1 of the 3 declared link displacements has a target at
the new site."*

`single_interval_arena_probe()` constructs no arena and tests no displacement:

```python
cycles = [L + 1] + [L] * (L ** (d - 1) - 1)          # typed formula
targets = {"axis-along-the-split": True}             # the answer, written down
for lk in link_set(d)[1:]:
    targets[str(lk)] = False
have = sum(1 for v in targets.values() if v)         # == 1 by construction
```

Every number in the sentence is asserted.  I verified all three by hand and they
are **correct** (inserting one site into one direction-0 link gives row lengths
4, 3, 3; $10 \bmod 4 \ne 0$; at the new site only the axis link along the split has
a target).  But **W3** ships `LINK-TARGETS-2-OF-3` at exit 0 by adding one `True`
to that dict, which is the definition of a typed count.

**Repair.**  Build the site set explicitly ($X \cup \{y\}$ with $y$ interior to one
link), compute the direction-0 orbit lengths from the successor relation, and count
link targets by testing membership of $y + \ell$ in the site set for each declared
$\ell$.  Twelve lines, and then the sentence is true.

---

## M7 (MEDIUM) — three scope/denominator mislabels, two of them inside the prose-render templates (so they survive any repair that does not touch the template)

The paper carries **zero false numbers by value** — I traced every one, rendered and
hand-written (see "Confirmations").  Three are attached to the wrong scope:

1. **`forced_lift` claim, FALSE DENOMINATOR LABEL.**  *"n divides n_1 at 0 of the
   **207 splits of the declared family**."*  Measured: 207 is
   $\sum_{x,\ell}(n_\ell(x)-1)$ for **`G-ANISO2` alone** ($9\times(3+8+12)$).  Over
   the six splittable records the figure is **650**.  Replacement sentence:
   *"…and $n\mid n_1$ holds at 0 of the 207 splits of `G-ANISO2`, the record at
   which the forced lift is censused."*
2. **`split_fiber` claim, TYPED COUNT inside the template.**  `"…over the six
   records that admit the move…"` — "six" is a literal in `paper_claims()`, not
   `len(fp["splittable_records"])`.  Under any change to the family the sentence
   would still say six.  Replacement: `"…over the %d records that admit the
   move…" % len(fp["splittable_records"])`.
3. **`forced_lift` claim, UNSCOPED CELL COUNT.**  *"the dynamics-forced front lift
   is non-integral at 30 of 81 cells."*  81 = 3 fronts × 9 sites × 3 links at
   **one record and one split rule** (`G-ANISO2` at `floor`), whereas §6's preamble
   describes the census as running over "both drag architectures, every declared
   rule, every declared lapse, a declared front family and both declared lifts",
   which invites reading 30/81 as family-wide.  Replacement: *"…non-integral at 30
   of the 81 (front, site, link) cells of `G-ANISO2` at the balanced split."*

Also note `forced_lift_universal()`'s predicate `n1 % n == 0` for `1 <= n1 < n`,
which is false for every integer — the "0 of 207" is a tautology, not a search.
The paper is honest about this in §6.1 ("which is impossible"), but the receipt
presents it as a census; it should be a `record()` disclosure.

---

## M8 (MINOR) — #208 is cited but never applied: `record()` is implemented and called zero times, and nine forced clauses sit in must-pass position

`record()` exists ("A RECORDED (non-must-pass) measurement.  Disclosed, never
load-bearing") and the receipt reports `48 must-pass, 0 recorded`.  Meanwhile the
following are analytically forced and registered as raising gates:
`G-BLOCK-IS-REAL`, `G-FREE-LINKS-INFINITE`, `G-UNSPLITTABLE-RECORDS` (the `all`
clause), `G-MOTIVATION-QUALIFIER-COMPUTED`, `G-INVENTORY-TREND`,
`G-NO-FLOATS-IN-RECEIPT`, `G-DEFERRED-GATES-EVALUATED`, `G-FINAL-GATE-COUNT`, and
the `splits_with_n_dividing_n1 == 0` clause of `G-FORCED-LIFT-NON-INTEGRAL`.
`G-DIMENSION-EXTENSION`'s waiver *names* #208 while leaving the gate must-pass.
Same class as R2's M10, one step less honest because the machinery is present.

**Repair.**  Move the nine to `record()`, and let the gate count fall; the
`G-FINAL-GATE-COUNT` arithmetic and the paper's rendered "48 gates" follow
automatically.

---

## M9 (MINOR) — the `cache-alias` mutant kills its gate by the wrong clause; the substantive clause is unexercisable

`cache-alias` rewrites the lookup key to `("ALIAS", rule, x)`, which is **absent**
from the memo, so `memo is None`, `compared` stays 0, and
`G-CACHE-FRESH-EQUALS-MEMO` fires on `compared > 0` — not on `disagreements == 0`.
The mutant's description ("serves one arena another arena's cached weight") is not
what is tested.  And it cannot be: the comparison loop runs over a single arena
`a0`, so `disagreements` is a dead counter.

**Repair.**  Make the alias serve a *different arena's* stored value
(`(id(other), other.name, rule, x)` for a second admissible record) and run the
comparison loop over ≥ 2 arenas, so `disagreements > 0` is the death certificate.

---

## M10 (MINOR) — `render_check`'s docstring claims a totality it does not have; and one stale ledger line

The docstring reads *"TOTAL render check: every rendered field is rebuilt from the
gated object and compared — not a chosen subset."*  It compares the move-census
rows, the inventory names and fibers, the presence of the verdict line, and the
defect-support lines — four of roughly twenty rendered blocks.  Untouched: the
record-family table, the no-potential line, the blocked/refused branch numbers, the
$d=3$ line, all six forced-part totals and all 36 build rows, the split-fiber
table, the count-lattice line, the census header, the closed-form line, the split
dependence, the lift grid, the forced-lift line, the whole iteration and growth
tables, the control comparison, and the instrument totals.

The *exposure* is genuinely lower than R2's, because `render_text()` and the
receipt both render from the one object `R` — there is no bypass path, only a
corrupt `R` (which S1 exploits and which `render_check` could not detect either).
The claim is nonetheless false and should be softened to name what it covers, or
made total by iterating the rendered blocks.

Stale: the dead `G-ANCHOR-CELL-COMPLETE` waiver entry (M3).

---

# What I could not break — confirmations

- **The CLI contract is exactly as documented, verified in code before use.**  No
  args → delivery, both artifacts written, exit 0, and every gate runs before any
  write (`open(OUT_TXT,"w")` is the penultimate statement of `deliver()`).
  `--mutant NAME` → exit 1 on a named gate with no write; a *surviving* mutant
  would return 3 with `MUTANT … SURVIVED` on stderr (never observed).
  `--list-mutants` → 34 names, exit 0.  `--selftest` → 34 subprocesses, all DEAD,
  artifacts byte-unchanged, exit 0.  Unknown argument, unknown mutant, and
  `--mutant` with no name → exit 2.
- **The 34-mutant table is honest to the row.**  My own 34 independent runs: every
  mutant exit 1, **zero tracebacks**, each dying on **exactly** the gate its row
  declares, and both on-disk artifacts byte-unchanged after each.  No gate predicate
  references mutant identity — the AST gate is real and self-validating, and **P1**
  proves it fires.
- **Two-run (three-run) byte-identity, reproduced.**  Three plain runs on the
  scratch copy emit `a04b97d2b7bc` / `022c3f488a93` — identical to the committed
  artifacts — with byte-identical stdout, including a run taken after the whole
  34-mutant audit and the selftest.
- **The verdict gate is genuinely independent — the R2 defect is repaired.**
  `reconstruct_verdict_from_receipt()` reads only the receipt object; it shares no
  code and no input with `build_verdict()`.  All five declared injection classes
  plus `head-constant` die on it.  I rebuilt all twelve segments from the receipt
  alone with my own code and got the delivered string **byte-identically**; I then
  flipped **12 of 12** segments with perturbations of my own design, and confirmed
  both other heads (`R6A-MOTIVATED-REFINEMENT-EXISTS` from an inventory with no
  class-(iii) item, `R6A-BLOCKED-AT-GRAMMAR-SOURCE` from a census with no admissible
  class).  `G-VERDICT-SEGMENTS-FLIPPABLE` tests the reconstructor **at the
  measurement**, not by appending to a string — the R2 vacuity is gone.  The
  verdict string appears verbatim in both the paper and `output.txt`.
- **The prose gate is new and it works within its scope.**  15 of 15 rendered
  claims appear verbatim in the paper, the paper's sha is carried in the receipt,
  and the `prose-claim-drift` mutant dies.  Because `claims["verdict"]` is the whole
  verdict string, the frozen paper acts as a *de facto* verdict anchor: eight of my
  twelve surviving injections had to have the paper regenerated to get through.
  That is real protection at delivery time — and it is consistency, not truth: it
  binds the receipt to the paper, and the worker writes the paper.
- **Every number reproduces.**  624 independently recomputed cells, zero
  mismatches.  In particular, from my own implementation: 9 admissible records with
  `G-SINGULAR` singular and `G-INDEF` non-positive-definite; readout determinant 2;
  record-IS-metric 81/81; lapse-bracket rank 2 at all nine sites; min axis cycle
  sums (min 3); the census 0/27/0/0, 21/3/3/0 ×3, 21/0/0/6 with shapes 6×6, 4×3,
  6×3; the ambiguous displacement is indeed $(2,1)$ with 2 decompositions and 2
  interiors; 16 completions, 12 disagreeing; cycles [4,3,3], 10 sites, 1 of 3
  targets; $d=3$: 216 sites, 27 images, 162 interiors, 27 unreached at parity
  $(1,1,1)$; 972/972 and 324/324; 36 builds, 28 admissible, with the eight failures
  and their exact inadmissible-site counts (`G-OFFDIAG2 @ floor` → **9** sites, as
  §5.1 says); all nine raw and admissible fibers; all six equivariant fibers (min
  3); 361/261/1 with the unique vector $(2,2,2)$; 54 of 108; 64 witnesses; the lift
  grid (matched pairs commute, mixed do not); 30 of 81; 207; the full 11 088-cell
  defect census 7 112 / 3 976 with support 16 296 / 20 706 / 18 438 / 16 079 of
  99 792 each, the per-rule table (644 for all eight A-rules and for `B-axis` and
  `B-chart`, **672** for `B-all` — §6.2's "slightly more" is right, and `A-insert`
  does equal `A-chart`), and the closed form at **49 896 of 49 896** image cells;
  ceiling 2 attained on `G-ANISO2` (min count 4), two of six splittable records
  halted by inadmissibility (`G-CURVOFF`, `G-OFFDIAG2`); 54/108 → 108/432 →
  216/1728.
- **Zero false numbers in the paper, by value.**  This is the first unit in the
  campaign with a clean prose surface.  I checked all 15 rendered claims and 24
  hand-written numeric statements (the 18-element chart group, 81 of 81, 361, the
  smallest cycle sum 3, every cell of the §3 census table, the $(2,1)$
  displacement, "three axis links and three positive diagonals" at $d=3$, 36/28,
  the whole §5 inventory table, "nine refined sites non-positive-definite on
  `G-OFFDIAG2`", "counts 3, 5, 9 and 13", the §6.2 support table, "`B-all` carries
  slightly more", "`A-insert` … the same defect count as `A-chart`", "minimum count
  is 4", "two of the six splittable records", "54 of 108, then 108 of 432, then 216
  of 1728", "forces 0 … where the dyadic move forces 27 … loses 6 of the 27",
  "48 gates … 32 anchors … 34 mutants", "five injection classes plus a head-pinning
  injection", "twelve segments", "three pre-registered heads", "depth of 2").
  Every one is right.  The only defects are the three scope labels of M7.
- **The anchors are live.**  A byte change to any pinned source dies on its row
  (`P8` for the one row with no declared mutant); path-value drift and null values
  die on `G-PATH-ANCHORS`; all 17 path-value rows match the pinned receipt, and
  every value the unit actually *reads* from I7 ($d$, $L$, $d_{ext}$, both record
  tables, the count box, the lapse family, the readout determinant, the
  sites-verified count, the identifiability rank) is among them.
- **The restriction test's comparator is genuinely independent.**  The coarse
  record's own $q$ is built by `q_from_counts` on the coarse counts; the restricted
  route sums refined counts and re-applies the readout.  The refinement is not in
  the comparator's path.  This is the one place the #219 discipline is met, and the
  compliance sweep is right about it.

---

# K1–K5 at instrument depth

**K1 — the coboundary theorem.**  *What kills the gate?* `potential-lax` alone,
and it kills it by rewriting the measured minimum to 0; the predicate
`min_axis_cycle_sum > 0` is otherwise forced (counts $\ge 1$, cycle length 3, so
the sum is $\ge 3$ for every admissible record — measured minimum 3, at `G-ANISO`
and `G-FLAT`).  *Grammar or family?*  The argument is grammar-level: it holds for
any strictly positive count field on any periodic lattice, so no admissible record
inside I7's grammar can carry a coboundary **on $X$** — the gate's nine records are
a sanity check, not the proof, and the paper is honest about that.  *Could an
admissible record carry coboundary counts?*  **On $X$, no — proved.  On the
universal cover, yes, and five of the nine do** (M1): the obstruction is exactly
$q_{12}\neq0$, and the five with $q_{12}=0$ carry explicit potentials.  *Is it the
mechanism?*  **No.**  It does not imply the split-fiber counts — those come from an
independent enumeration of admissible triples — and it rules out only one candidate
forcing route.  Worse, for `G-DIAG2` the cover potential plus the unit's own §6.1
interpolation produces a canonical, admissible, restriction-exact refinement of
fiber 1 that the unit itself builds.  §2's "This is the *mechanism* of everything
that follows" must be retired.

**K2 — the classification hunt, instrument contribution.**  I did not run the full
hunt (operator/effectus lens), but the instrument yields one candidate the unit did
not consider and one measurement that constrains it.  Candidate: the cover-potential
route above, which is class-(i)-shaped (fiber 1, determined by the record's own
counts) modulo one interpolation declaration — and integral exactly when the
interval counts are even, which among the declared family holds only for
`G-DIAG2` $(2,2,4)$.  Constraint: the measured stabilisers are `G-DIAG2` 18 /
2 orbits, `G-OFFDIAG` 18 / 2, `G-ANISO2` 9 / 3, `G-OFFDIAG2` 9 / 3, `G-OFFNEG`
9 / 3, `G-CURVOFF` 2 / 15 — reproduced exactly — and no equivariant fiber is 1
(minimum 3), so the symmetry route is genuinely closed, as the unit says.  The
19 683 … 1.2576e21 span, the equivariant minimum 3, and the 1-of-361
lattice-forced vector $(2,2,2)$ all reproduce; note that $(2,2,2)$ is precisely a
$q_{12}=-1$ vector, i.e. *not* of the cover-potential class, so the two routes to
fiber 1 are different and neither subsumes the other.

**K3 — the dynamics claims.**  All recomputed from scratch: 7 112 of 11 088
nonzero and 3 976 identically zero (the positive control is real — my own census
finds the same 3 976); the four-class support table exactly; the closed form
$D(\iota(x)) = w^{\mathrm c}[N,n](x)$ at **49 896 of 49 896** left-lift image
cells, and I confirm it is *analytically forced* (under the left lift the refined
front is constant on each cell, so both the axis tilts and the link tilts vanish at
image sites and the refined drag is identically zero — for both architectures);
lift-relativity at images (left split-independent, right not) reproduced;
rule-blindness reproduced with `B-all` the sole outlier at 672.  30 of 81 and 0 of
207 reproduce, with the two scope labels of M7.  The instrument-level caution: Y1
shows that **zeroing an entire parity class of the defect leaves all four defect
gates green**, so the "characterised, not just reported" standard is met by the
*presentation*, not by the *protection*.

**K4 — the move census and the head.**  Reproduced: the hyperplane block (3 cut
diagonals at displacement $(2,1)$, 2 decompositions, 2 interiors, 16 completions
disagreeing at 12, identical at all three loci); the single-interval refusal (M6:
correct but typed); the $d=3$ gap (27 of 216, exactly the all-odd parity class);
the count-1 floor (3 of 9, including `G-FLAT`); the ceiling 2, attained.  The
control's discriminating failure is real and I verified **both** fingerprints
independently: `R1-COPY` gives 21 / 0 / 0 / 6 against `DYADIC`'s 0 / 27 / 0 / 0 —
it forces zero additivity constraints and loses six coarse intervals, a different
failure mode from `DYADIC`'s four class-(iii) freedoms.  Head composition is an
adjudication question, not an instrument one; I record only that all three heads
are reachable from the reconstructor and that the per-class table is present in
both the receipt and the verdict's `CLASSES` segment, so either choice is
renderable without new measurement.

**K5 — instrument.**  (a) CLI contract confirmed in code, then exercised: 116
process-level executions; 34/34 mutants dead on their declared gate; three-run
byte-identity reproduced.  (b) Coverage/waiver audit in M3 — **20 of 48 never
falsified, 20 waived, 12 of the 20 waivers false or false-in-part, 0 of the 15
"covered by X" claims holding, 11 of the 20 waived gates demonstrably falsifiable.**
(c) The new anchor kind audited in M5 — **binds existence only; ADOPT WITH
MODIFICATION** (order it ahead of the byte anchors, bind each row to a named
consumer gate, anchor a context window rather than a fragment).  (d) The five
verdict injection classes plus the head pin all die on a genuinely independent
comparator — this engraving is met in substance, not only in letter; the residual
blind spot is upstream measurement corruption, which is the correct division of
labour and is where M2 lives.  The split-fiber in-gate recomputation is **not**
independent (X1) — #24/#219 compliance fails at exactly the gate the protocol
names.  (e) Verdict rebuilt from the receipt alone, byte-identical, 12 of 12
segments flipped by my own perturbations, both alternative heads reached.
(f) Paper↔output↔receipt: 624 cells, **zero false numbers in the receipt and zero
false numbers by value in the paper**; 15/15 rendered claims verified present and
correct; 24 hand-written numeric statements verified by value; three scope labels
wrong (M7).  (g) All repo hashes re-verified unchanged after all work; `git status`
shows only my single new file and another reviewer's.

---

# Required fixes (ranked)

1. **M1** — scope the no-potential theorem to the periodic lattice, replace the
   mechanism sentence, add `G-DIAG2`'s cover-potential refinement to §5.1 as a
   measured exhibit, and gate the cover-potential census (nine curl checks).
2. **M2** — give `G-FIBER-COMPUTED`, `G-MOVE-CENSUS-CELL-COMPLETE` and
   `G-DEFECT-CHARACTERISED` genuinely independent comparators and a mutant each
   that perturbs the *shared component*; compute the four typed constants; add a
   record-family cell-completeness gate.
3. **M3** — rewrite all 20 waivers in the three permitted forms; add the
   shadowing-arithmetic gate (`waiver names X ⇒ X.expected_gate == this gate`);
   add falsifiers for the eleven falsifiable waived gates; gate the waiver dict
   against extraneous keys.
4. **M4** — run the mutant table in-delivery and gate `actual_gate ==
   expected_gate` per row, so the falsifier census measures deaths rather than
   declarations.
5. **M5** — the three verbatim-anchor modifications; adopt the kind for the era on
   that basis.
6. **M6** — build the single-interval arena and measure its cycle lengths and link
   targets instead of typing them; then §3.2's sentence becomes true.
7. **M7** — the three scope labels: "207 splits of **`G-ANISO2`**"; compute "six"
   from `len(splittable_records)`; scope "30 of 81" to one record and one split
   rule.
8. **M8** — move the nine forced clauses to `record()`; stop citing #208 in a
   waiver for a must-pass gate.
9. **M9–M10** — make `cache-alias` alias a real second arena and run the memo
   comparison over ≥ 2 arenas; correct `render_check`'s docstring or make it total;
   drop the dead waiver entry.

None of these impeaches a measured number: I verified 624 of them independently and
every one is right, and the paper's prose surface is the cleanest the programme has
produced.  M1 is more than a protection defect — it is a stated theorem used
outside its scope and a mechanism claim that a record of the declared family
refutes.  M2 and M3 are protection, but M3 is the era's own standard applied to a
census this unit was the first to carry: the census is right, and the waivers under
it are mostly not.
