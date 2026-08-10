# R4 (paper-10) — HOSTILE REVIEW, REVIEWER R3: THE INSTRUMENT LENS

**Unit:** R4, the QFT rung — `v14/paper-10-defect-on-the-stage.md`.
**Panel:** Γ-MAIN + R4 protocols, PANEL B (`v14/note-gmain-r4-protocols.md`,
sha256-12 `a3a39813e5b5`, v14 ledger #75). **Lens:** instrument (K5 primary).
**Reviewer:** R3. **Frozen:** 2026-08-10.

**Object, hashes verified at the start of work and re-verified unchanged at
the end:**

| artifact | declared | measured (start) | measured (end) |
|---|---|---|---|
| `v14/paper-10-defect-on-the-stage.md` | `f3e8cc1618f8` | `f3e8cc1618f8` | `f3e8cc1618f8` |
| `v14/code/r4_defect_stage_exact.py` | `b079bb3b8d55` | `b079bb3b8d55` | `b079bb3b8d55` |
| `v14/code/r4_defect_stage_output.txt` | `58ec08893526` | `58ec08893526` | `58ec08893526` |
| `v14/code/r4_defect_stage_receipt.json` | `3214f4da3af2` | `3214f4da3af2` | `3214f4da3af2` |
| pin `v14/note-r4-qft-pin.md` | `1582cea5df51` | `1582cea5df51` | `1582cea5df51` |

**Discipline confirmations.** All hostile work was performed on a scratch
mirror (`…/scratchpad/r4inst/`), never in the repository; no imports from the
unit (the CLI was driven by `subprocess`); git was read-only (`git status`,
`git log`, `git show`); this file is my single repository write. The only
worktree modification present at close is `v14/code/gmain_exact.py`, which
belongs to the concurrent Γ panel and is not mine.

**Disclosure — the RUNBOOK moved under this review.** RUNBOOK.md was
`3781cbce4e42` when I began and `f5adab0c479d` when I finished: commit
`685d483` (v14 #82, the Γ-main adjudication) added two §14 items, *the
CLI-contract minimum* and *comparator independence, strengthened*. Both
postdate R4's delivery (#54) and R4's protocol freeze (#75), so neither binds
R4 under §13/#246 (rules bind at delivery). I read them, I judge against them
only as repair targets, and I record that the second one already names
"R4's MAJOR-6" — a finding of one of my two panel colleagues, whose reviews
(`review-r4-effectus.md` #77, `review-r4-operator.md` #78) I deliberately did
**not** open, to keep this lens independent. Where my findings coincide with
that engraving I say so; the numbering below is my own.

---

## GRADE: **ACCEPT-WITH-FIXES**

The delivered *numbers* survive: I recomputed 329 numeric facts independently
from the receipt and from first principles and found **zero false numbers** in
the paper, the output or the receipt, and the delivered verdict string is
exactly the string the instrument derives. The two plain runs are
byte-identical to the committed artifacts — reproduced from a different
absolute repository root, so no path leaks into the artifacts. All 82 declared
mutants die externally, every one at its declared target gate, exit 1, no
tracebacks. All 34 anchor perturbations die by name.

What fails is *coverage*, and it fails at the top of the object. The verdict's
**head** — the single token that says DEFECT-PRESENT rather than
DEFECT-ABSENT — is outside the complete-string equality gate, and I flipped it
to `R4-DEFECT-ABSENT-MARKOVIAN-COLLAPSE` and to a name outside the pin
entirely, at exit 0 with 77/77 gates passed and 82/82 mutants dead. The pin's
*mandatory* realization-census gate verifies no individual classification; one
reclassification moves 588→645 and 150→93 undetected. The Y1 lesson the paper
claims to have learned is implemented on 12 of 588 rows, and zeroing the other
576 takes the census from 588 to 205 undetected. Of 77 injections of my own
design, **34 survived undetected**. The instrument's own compliance prose
("every numeric claim of the paper is … checked verbatim by `--verify-paper`")
is false: twelve false paper numbers and three quotation-meaning inversions all
pass it at exit 0.

None of that moved a delivered number, and the unit's positive machinery is
strong and often better than its claims. That is why this is
ACCEPT-WITH-FIXES and not REJECT. But F1 and F2 are at the boundary, and the
grade is conditional on repairs to F1–F6 before terminal.

---

## FINDINGS, RANKED

### F1 — MAJOR (at the FATAL boundary). The verdict head is outside the complete-string equality gate; a polarity flip and an off-pin head both survive at exit 0.

`reconstruct_verdict_from_receipt(R)` — the object the paper advertises as "an
*independent reconstruction* built from the serialized receipt alone, by a
function that shares no helper with the builder" — does not reconstruct the
head. It reads it:

```python
    hd = R["verdict"]["head"]
    ...
    return hd + "<" + "|".join(parts) + ">"
```

Every one of the nine segments is rebuilt from `R["counts"]`; the head is
copied. `G-VERDICT-STRING-EQUALITY` therefore compares
`head + segments(counts)` against `head + segments(counts)` for the head
factor — the #219 shape (an object compared against a copy of itself) at the
one place where it matters most. `G-VERDICT-HEAD-DERIVED` and
`G-VERDICT-PREREGISTERED` both run *earlier*, inside `build_state`, so nothing
re-checks the head after the verdict object exists.

Proven by execution, three injections placed immediately after
`S["verdict"] = {...}` (i.e. after every verdict gate has been built but before
any of them evaluates the emitted object):

| injection | emitted head | outcome |
|---|---|---|
| `INJ-HEAD-POST-GATE` | `R4-BLOCKED-AT-NOTHING` | **exit 0, 77/77 gates, 82/82 mutants dead** (full delivery run) |
| `INJ-HEAD-ABSENT-VARIANT` | `R4-DEFECT-ABSENT-MARKOVIAN-COLLAPSE` | **exit 0** |
| `INJ-HEAD-OUTSIDE-PIN` | `R4-QUANTUM-FIELD-CONFIRMED` | **exit 0** |

The full-delivery run of `INJ-HEAD-POST-GATE` emitted, verbatim:

```
R4-BLOCKED-AT-NOTHING<DEFECT=588-OF-3364-PAIRS-AT-MAXIMAL-TRANSPORT-FULL;…>
```

— a BLOCKED head sitting on a census of 588 nonzero defects, and the
instrument printed `ALL GATES PASSED (77/77); ALL MUTANTS DEAD (82/82)`.

One flip *is* caught, and only by accident: `INJ-HEAD-ABSENT-EXACT`
(head → exactly `R4-DEFECT-ABSENT`) dies at
`G-PRECHECK-DOES-NOT-NAME-THE-VERDICT`, whose predicate happens to compare
`derive_head(counts with the census zeroed)` against `S["verdict"]["head"]`.
Any ABSENT *variant* escapes that coincidence, as the table shows.

This is exactly the failure mode engraved the same day at #82 ("a verdict
comparator shares NOTHING with its builder — neither code, nor inputs, nor
typed literals"), reached here independently by injection.

**Repair.** `reconstruct_verdict_from_receipt` must derive the head from
`R["counts"]` by its own copy of the head law (not by calling `derive_head`),
and must re-assert pre-registration against the pin text from inside the
comparator. The gate must then compare the *emitted* `S["verdict"]["string"]`
against that full rebuild. Ship three new declared mutants — a post-build head
retype, an ABSENT-variant flip, and an off-pin head — each killed by
`G-VERDICT-STRING-EQUALITY`.

### F2 — MAJOR. The realization-census gate — the pin's mandatory gate — verifies no individual classification; a single reclass moves four verdict numbers undetected.

`G-REALIZATION-LEVELS` claims: "every generator declares which fields it
transports, measured: occupation by the translation stabiliser, axis by full
covariance, phase register by equivariance of the coefficient label." Its
predicate is

```python
            set(levels.values()) <= set(LEVELS)
            and len(levels) == len(pool)
            and len(set(levels.values())) >= 3,
```

— the level names are legal, there is one per generator, and at least three
distinct names occur. No generator's classification is checked against
anything. The declared falsifier `MUT-REALIZATION-PROMOTE` promotes *all* 64
generators, collapsing the distinct-name count to 1, and dies on the `>= 3`
clause alone.

`INJ-RECLASS-OCC-TO-FULL` promotes exactly one OCC generator (the scrambled
control `S063`, a singleton class, so `G-CLASS-INVARIANTS` cannot notice):
**exit 0, 77/77, 82/82**, with the verdict now reading

```
DEFECT=645-OF-3481-PAIRS-AT-MAXIMAL-TRANSPORT-FULL … NONLOCAL=429-OF-1273 …
REALIZATION=…;EXCLUDED-NONZERO=93
```

against the delivered `588-OF-3364`, `372-OF-1188`, `EXCLUDED-NONZERO=150`.
Four headline numbers move together and nothing bites. The pin (§3.5) makes
this gate mandatory and says "defects enter verdict segments only at the
maximal declared transport"; the gate enforces the *routing* but not the
*classification the routing depends on*.

**Repair.** Add a gate that recomputes each generator's level by an
independent route (e.g. recompute the translation stabiliser from the matrix
and the equivariance orbit from the coefficient map, in a function sharing no
helper with the classifier) and compares the two label vectors elementwise;
declare a single-generator promotion and a single-generator demotion as
mutants against it.

### F3 — MAJOR. The Y1 defect-zeroing lesson is implemented on 12 of 588 rows; zeroing the other 576 is undetected.

The paper states the claim explicitly (§4.3): "a mutant that zeroes only the
*censused* defect cells, leaving every count intact, dies at the value census,
because the defect gates are bound to the exact values and not merely to a
count." That is true — `MUT-DEFECT-CENSUS-ZERO` dies at
`G-DEFECT-VALUE-CENSUS`. The converse is the hole. `DEFECT_VALUE_CENSUS_ROWS
= 12`; the value census binds the first twelve nonzero circulant rows by name
(`sorted(nz_circ, key=lambda r: (r["V"], r["U"]))[:12]`, 28 cells). Nothing
binds the remaining 576 nonzero rows to any value.

Two injections zero `dc` for circulant pairs chosen to miss the twelve
censused rows, the stride-5 route check and the stride-7 cross-term check:

| injection | delivered | injected | outcome |
|---|---|---|---|
| `INJ-Y1-PARTIAL-ZERO` | `DEFECT=588`, `LOCAL=216`, `NONLOCAL=372` | `475 / 199 / 276` | **exit 0** |
| `INJ-Y1-FULL-ZERO-OUTSIDE-CENSUS` | as above | `205 / 77 / 128` | **exit 0, 77/77, 82/82** (full run) |

`INJ-MARKOV-FREE-SILENT-ZERO`, which silently zeroes 100 free-pair rows at the
census level, likewise survives (588→490, free-nonzero 738→638). The
"Markovian control gated in both directions" is one-directional in practice:
injecting a nonzero into a Markovian pair dies
(`INJ-MARKOV-NONZERO-CENSUS` → `G-MARKOV-ZERO`), but silently losing free
nonzeros does not.

**Repair.** Bind the census by value at scale, not by 12 sampled rows: gate the
full multiset `{value → cell count}` (the delivered eight-value table with
counts 24/108/336/144/192/24/108/336) against an independent recomputation by
the dense route, and gate the zero-sum identity
`Σ value×cells = 0` on it. Add a mutant that zeroes an uncensused stratum.

### F4 — MAJOR. Eighteen of the twenty-seven measured values the verdict carries have no flip test, and the flip test that exists measures responsiveness, not correctness.

`G-VERDICT-SEGMENTS-FLIPPABLE` probes exactly one receipt field per segment:

```python
            keymap = {"DEFECT": "nonzero_at_maximal", "TWO-POINT": "separations",
                      "CLASSES": "classes_extended", "LOCALITY": "local_nonzero",
                      "MARKOV": "markov_pairs", "REALIZATION": "nonzero_excluded",
                      "STATE": "state_distinct", "SCALE": "admissible_scales",
                      "SCOPE": "pool"}
```

Nine probes for twenty-seven measured values. And the probe only shows that the
comparator *moves* when the field moves — it cannot show the field is right,
because emitter and comparator read the same field. `INJ-CLASS-22-TO-21`
corrupts `classes_extended`, which **is** one of the nine probed fields, and
still survives: the segment moved, consistently, in both paths.

Proven freely corruptible at exit 0, each emitting a changed verdict:

| value | delivered | injected | injection |
|---|---|---|---|
| `CLASSES=EXTENDED` | 22 | 21 | `INJ-CLASS-22-TO-21` (full run) |
| `EXCLUDED-NONZERO` | 150 | 0 | `INJ-EXCLUDED-150-TO-0` |
| matched agreements | 616 | 999 | `INJ-MATCHED-616-TO-999` (full run) |
| `OBSERVABLE-MOVES-AT-…` | 18 | 17 | `INJ-STATE-DISTINCT-18-TO-17` |
| `EQUAL-TIME` | 15/256 | 1/1000 | `INJ-EQUAL-TIME-VERDICT-FIELD` |

plus, via F2 and F3, `nonzero_at_maximal`, `pairs_at_maximal`,
`all_rational_rows`, `local_nonzero`, `nonlocal_nonzero`, `nonlocal_pairs`.

Related, and the same shape as the #82 engraving: the SCOPE segment's
`D=2;L=4;FIELD=Q(ZETA-8)` and the TWO-POINT segment's
`LIGHTCONE=ONE-NEIGHBOURHOOD-PER-STEP` are **typed string literals written
identically in `build_segments` and in the comparator**. They are structurally
incapable of disagreeing. `L` itself is typed at the census
(`L = 4` at line 1089), downstream of `G-UNIQUE-SCALE`, whose predicate is the
typed anchor `admissible == [4]`; the only thing standing between a wrong
lattice and a verdict that still says `L=4` is an `IndexError`
(`INJ-TYPED-LATTICE-SIZE` at L=5 and `INJ-TYPED-LATTICE-L2` at L=2 both die by
traceback at line 1190, not by a named gate).

**Repair.** Give every measured value in the verdict its own flip probe, drive
`L` and `d` into the SCOPE segment from the measured `admissible_scales` and
the anchored `d`, and add a gate asserting `L == admissible_scales[0]` so the
census scale is *bound* to the scale the precheck selected.

### F5 — MAJOR. `MUT-PRECHECK-NAMES` is killed by a mutant-identity test laundered past the very AST scan the unit ships to enforce #208.

```python
    precheck_head = (derive_head_from_precheck_only(S["counts"])
                     if mut("MUT-PRECHECK-NAMES") else None)
    ...
    LD.gate("G-PRECHECK-DOES-NOT-NAME-THE-VERDICT", …,
            zeroed != S["verdict"]["head"] and precheck_head is None, …)
```

`precheck_head` is `None` on every non-mutant path, so `precheck_head is None`
is an analytically-forced clause whose only possible falsifier is the named
mutant. `G-NO-MUTANT-IDENTITY-IN-GATES` does not see it, because it searches
for `mut(` *inside gate call nodes* and the `mut(` call is one statement
upstream.

Proven by execution. With that conjunct deleted and nothing else changed,
`--mutant MUT-PRECHECK-NAMES` **survives** (`PROBE-PRECHECK-CLAUSE-REMOVED`,
exit 0); the unmodified control dies (`PROBE-PRECHECK-CONTROL`, exit 1 at that
gate). The gate's *other* conjunct is a real measurement and does bite (it is
what catches `INJ-HEAD-ABSENT-EXACT`), so the gate is not vacuous — but its
declared falsifier does not die blind, and the waiver ledger consequently
records this gate as FALSIFIABLE on a falsifier that tests the mutant's name.
The compliance row "#208 no gate predicate may reference mutant identity —
APPLIED via G-NO-MUTANT-IDENTITY-IN-GATES" is false in substance.

**Repair.** Replace the flag test with a measurement: make the mutant actually
substitute `derive_head_from_precheck_only` for `derive_head` in the head
derivation and let the gate detect the substitution by its *output* (as
`MUT-VERDICT-HEADS` already does correctly). Extend the AST scan to flag any
gate predicate reading a name whose only assignment site is guarded by `mut(`.

### F6 — MAJOR. The `#20` compliance claim is false: twelve false paper numbers and three quotation-meaning inversions pass `--verify-paper` at exit 0.

The receipt's compliance sweep asserts:

> "#20 prose renders from the receipt — APPLIED — **every numeric claim of the
> paper** is emitted here as `paper_claims.rendered` and checked verbatim by
> `--verify-paper`."

`paper_claims()` renders **13** strings. The paper carries 336 numeral
occurrences over 63 distinct numerals, in eight tables. I corrupted twelve
paper numbers and three quotations and ran the real CLI on each:

| paper corruption | `--verify-paper` |
|---|---|
| free pairs 2304 → 2305 | exit 0, 13 claims, 0 missing |
| matched agreements 616 → 916 | exit 0 |
| order-collapse table 24/48 → 26/46 | exit 0 |
| eight-value table 336 → 436 (both signs) | exit 0 |
| five-point 34,925/121 → 44,925/921 | exit 0 |
| realization census 5/0 → 3/2 | exit 0 |
| equal time 15/256, −1/256 → 17/256, −3/256 | exit 0 |
| locality table offsets 15 → 17 | exit 0 |
| class table C009 size 2 → 3 | exit 0 |
| "Seventy-five gates" → "Seventy-seven" | exit 0 |
| "Sixteen … monomial" → "Twelve" | exit 0 |
| radius profiles 18/33 → 19/43 | exit 0 |
| **meaning inversion** of the anchored definition ("the failure … to equal" → "the agreement … with") | exit 0 |
| **meaning inversion** of the annihilator theorem ("annihilate" → "amplify") | exit 0 |
| **meaning inversion** of the 2×2 witness ("the defect vanishes" → "is maximal") | exit 0 |
| *control:* corrupt one of the 13 rendered strings | **exit 1, 1 missing** |

The mechanism works precisely on its 13 strings and on nothing else. Worse,
three of those 13 are **typed constants**, not rendered from `R`:
`unique_scale` ("L = 4 is the only lattice size …"), `ord_collapse`, and
`ord4_generators` ("72 distinct unitary generators, 48 of them non-monomial,
in **9 gauge classes**"). The last is the only place the number 9 appears, and
`--verify-paper` verifies the paper against a hard-coded string rather than
against the measurement. (The value is correct — 72/8 = 9, and axis (0,1)
carries exactly 9 pool representatives — but it is verified by me, not by the
instrument.)

The three quotation inversions are the #62 failure class exactly: R4's
verbatim anchors test `w in src_text[sid]` — that the *instrument's own
declared window* occurs in the pinned source. They never read the paper. The
#62 amendment ("the anchor kind binds QUOTE FIDELITY — the paper's quotations
against the source's committed bytes") postdates R4's delivery and does not
bind it, but the disease it was engraved against reproduces here verbatim.

**Repair.** Render every numeric claim of the paper — every table cell — from
`R`, and make `--verify-paper` a must-pass gate of the delivery run rather
than an opt-in mode. Bind the paper's quotations, not the instrument's, to the
source bytes.

### F7 — MAJOR (recurrence of a registered disease, fourth instance). The CLI silently ignores unknown flags and writes the delivered artifacts while doing so.

```python
    args = sys.argv[1:]
    write = True
    if "--no-write" in args: write = False
    if "--mutant" in args: MUT = args[args.index("--mutant") + 1]; write = False
    …
```

There is no argument whitelist and no unknown-flag rejection. Measured on the
scratch mirror:

- `--selftest` (unrecognised) → **exit 0, a full plain delivery run, and both
  artifacts written**. This is the #66 Γ-prep incident reproduced in R4: an
  adjudicator or reviewer typing a plausible flag receives
  `ALL GATES PASSED (77/77)` from a run that performed no self-test, and
  overwrites the delivered artifacts on the way. (Here the write is
  byte-identical because the unit is deterministic; the epistemic damage is the
  same.)
- `--mutant MUT-DOES-NOT-EXIST` → **exit 0**, printing
  `MUTANT/BREAK SURVIVED -- no gate killed it.` A typo'd mutant name produces
  the exact output signature of an instrument failure. Same for
  `--break-anchor A-NOPE`.
- `--mutant` / `--break-anchor` / `--verify-paper` with no argument →
  `IndexError` traceback (exit 1, loud, but not the unit's own failure
  protocol).

Under §13/#246 this is not a discipline violation — the CLI-contract minimum
was engraved at #82, long after R4's delivery at #54 — but R4 is the **fourth**
instance of the disease (Γ-prep, R6b′-partial, Γ-main, R4) and the only one I
have checked where the silent-ignore path *writes*.

**Repair.** Adopt the #82 minimum verbatim: argv-parsed, unknown flags exit 2,
`--mutant NAME` validated against `MUTANTS` (exit 2 on an unknown name),
`--break-anchor NAME` validated against `SOURCES`, a real `--selftest`, and
missing-argument handling that exits 2 with a message.

### F8 — MAJOR. `DEFECT-INDIFFERENT-AT-MATCHED-COORDINATES=616-OF-1024` is 1024 comparisons against **25 distinct** non-local pairs.

`G-LOCALITY-LIKE-FOR-LIKE` claims the §15 addendum's standard: "the
local/non-local contrast is read at matched coordinates — same coefficient
class, same axis order, same gauge fixing." Its predicate is `matched > 0`.
The matching itself is

```python
            partner_v = [h for h in nl4 if coefclass(h) == coefclass(gv)]
            …
            b = defect_conv(partner_v[0]["coef"], partner_u[0]["coef"], sites, subv)
```

where `coefclass` is the sorted multiset of coefficient *values*, discarding
which offset carries which value. I recomputed the matching: `loc4` has 32
members in **32** distinct gauge classes but only **5** distinct `coefclass`
values; `nl4` has 16 members in 16 gauge classes and the same 5 `coefclass`
values. Taking `partner[0]` therefore maps all 32 local generators onto at
most 5 non-local partners, and the 1024 "matched pairs" resolve to **25
distinct non-local comparisons**, with multiplicities 64/32/16 (measured
distribution: nine at ×64, twelve at ×32, four at ×16).

So the paper's "Of 1024 matched pairs, **616 have identical defect value
multisets**", and the same numbers inside the verdict, read as 1024 independent
matched comparisons and are 1024 weighted repetitions of 25. The paper's
supporting sentence — "the order-four local and non-local axes carry the same
nine gauge classes with the same coefficient values, so the contrast can be
read with the coefficient class, the axis order and **the gauge fixing** all
held equal" — is not what the code does: the gauge fixing is precisely the
coordinate that is *not* held equal.

**Repair.** Match on the full gauge class (offset → value), not the value
multiset; report the number of *distinct* matched comparisons alongside the
weighted count; and gate the agreement count against an independent
recomputation. Replace the paper sentence with, verbatim: *"Matching each
order-four local generator to a non-local generator of the same coefficient
value multiset yields 1024 ordered comparisons drawn from 25 distinct
non-local pairs; 616 of the 1024 agree on the defect value multiset. The
matching is by value multiset, not by gauge class, and the count is weighted
accordingly."*

### F9 — MINOR. `G-COUNTS-DERIVED`'s claim exceeds its content, and its "second enumeration" is the same filter over the same field.

Claim: "every headline count is recomputed by a second enumeration over the
census rows." Content:

```python
    recount = sum(1 for r in rows if r["level"] == maximal and r["nonzero_cells"] > 0)
    … counts["nonzero_at_maximal"] == recount and counts["pairs_total"] == len(pool) ** 2
```

Two of the twenty-three counts, and the "second enumeration" re-filters the
same `rows` on the same `nonzero_cells` field that produced the first — the
#219 shape. It can only catch a typed value (`MUT-COUNT-TYPED`, 999), which is
what it does. `pairs_at_maximal = 3364`, `distinct_values = 8`,
`all_rational_rows = 588`, `separations = 16`, `markov_pairs = 1792`,
`class_sizes`, `orders` and the locality quadruple are recomputed by nothing.

**Repair.** Recompute the headline counts from the receipt's serialized
`census_rows` in a function that shares no helper with the census builder, and
gate all of them.

### F10 — MINOR. `G-VERDICT-NO-PAPER-INPUT` claims more than it tests, and the comparator does read receipt strings.

Claim: "no external prose can reach the verdict: the string is invariant when
**every** non-numeric receipt field is replaced." Two fields are replaced
(`arena_declaration`, `census_rows`). The comparator does read non-numeric
receipt fields that are *not* replaced —
`R["realization_census"]["maximal"]` and `R["equal_time"]["rational_zero"]` —
and F4 shows the second is freely corruptible.

**Repair.** Replace *every* field the comparator does not need, enumerated
from the receipt's key set, or restate the claim as "invariant under
replacement of the declared prose fields", naming them.

### F11 — MINOR. Two of the nine verbatim consumers cannot meet the consumer standard.

Under the #62 spec (advisory here — it postdates delivery) every verbatim
row's consumer gate "must exist, be non-literal, and be falsified by a
declared mutant". Measured:

- `VB-DEFECT-DEF → G-DEFECT-DEFINITION-SHAPE`: the gate's predicate is the
  literal `True`, it has no declared falsifier, and it is one of the two
  waived gates. It binds existence, not meaning.
- `VB-DIVISION-EVENT → G-DIVISION-EVENTS-DECLARED`: the predicate is
  `ARENA["division_events"].startswith("t = 0 and t = 2")` conjoined with a
  flag parsed out of the same prose — the unit's own declaration compared
  against a typed prefix of itself.

The other seven consumers are genuine computations with genuine falsifiers.
`G-VERBATIM-ANCHORS` itself checks only `r["consumer_gate"] in GATE_REGISTRY`
— membership of a label in a list, the "unread label" shape the #62 amendment
names.

**Repair.** Bind each verbatim row to a consumer that is a measurement, and
gate that the named consumer appears in the falsifier map.

### F12 — MINOR. `G-WAIVERS-VERIFIED` fails through an uncaught exception rather than the unit's own failure protocol.

`G-WAIVERS-VERIFIED` is evaluated in `main()` outside both `try/except
GateFail` blocks. I broke its detector predicate (`PROBE-WAIVER-PREDICATE-
BROKEN`) and the gate did fire — correctly, with
`injected false waiver detected=False` — but as an uncaught `GateFail`
traceback, not as the unit's `GATE FAILED: … EXIT 1` line. Exit code is still
1, so no false pass; the failure is in the reporting contract.

**Repair.** Wrap the post-harness gates in the same handler.

### F13 — NOTE (with measured mitigation). Roughly 45 of the 82 mutants fabricate the gate's statistic instead of breaking the mechanism — but the mechanisms mostly bite anyway.

Forty-five injections are of the form `colsum_bad = 1`, `eq_bad = 1`,
`comp_bad = 1`, `handle_moves = 0`, `matched = 0`, `distinct = 1`,
`recon = {}`, `below = []`, `free_nz = []`, `orb_anchored = []`,
`cache_hits = 0`, `floats = [None]`, and so on: they assign the very variable
the gate predicate tests. Such a mutant proves the predicate *can* fail; it
does not prove the gate would catch a real corruption. I therefore built five
real mechanism breaks:

| real break | outcome |
|---|---|
| perturb one defect cell before the column-sum loop | **exit 1, `G-DEFECT-COLUMN-SUMS`** |
| perturb the composed-time difference | **exit 1, `G-TWOPOINT-COMPOSED`** |
| perturb one equivariance right-hand side | **exit 1, `G-DEFECT-EQUIVARIANCE`** |
| perturb one Born column | **exit 1, `G-TWOPOINT-STOCHASTIC`** |
| write a nonzero `defect` dict into a Markovian row | **exit 0 — survives** |

Four of five bite, which is the honest mitigation and worth saying plainly.
The fifth exposes that `G-MARKOV-ZERO` keys on `nonzero_cells`, a count, and
never inspects the defect object whose emptiness the paper asserts ("the
pairwise sum through the cut is literally empty"). Harmless in the delivered
run — the `defect` key is stripped from `census_rows` before the receipt — but
the claim is stronger than the gate.

### F14 — NOTE. `G-UNIQUE-SCALE`'s predicate is a typed anchor, not a measurement of uniqueness.

`admissible == [4]` rather than `len(admissible) == 1`. As an exit-1 anchor on
a committed number this is within §4; but the gate's claim ("exactly one swept
lattice size carries both") is a uniqueness statement and the predicate is an
identity statement. Restate the claim, or gate `len(admissible) == 1` *and*
anchor the value separately.

### F15 — NOTE. `proj_inv == 6 * 7` hard-codes the self-test's size from its loop literals.

`G-TWOPOINT-PERIODICITY` requires the gauge self-test to succeed at exactly
`6 * 7 = 42` of 42 combinations, with 6 and 7 written to match
`circ_pool[:6]` and `range(1, 8)`. Correct today; a silent no-op if the pool
ever shrinks below 6. Derive the denominator from the loop.

---

## EXECUTION AND RECOMPUTATION COUNTS

| activity | count |
|---|---|
| full plain delivery runs of the delivered code (scratch mirror) | 2 |
| external `--mutant NAME` runs, all 82 declared mutants | 82 |
| CLI-contract probes (unknown flag, unknown mutant, unknown anchor, 3 missing-arg, 5 real `--break-anchor`, `--verify-paper` baseline) | 12 |
| code injections of my own design (fast path) | 19 + 6 + 5 + 2 = 32 |
| full delivery runs of injected copies (end-to-end, incl. mutant harness) | 5 |
| per-row anchor drifts (10 path-value × value + 10 path-value × path + 9 verbatim) | 29 |
| paper corruptions driven through `--verify-paper` | 16 |
| **total instrument executions** | **178** |
| **injections of my own design, executed** | **77** |
| — survived undetected at exit 0 | **34** |
| — killed by a named gate | 41 |
| — killed by traceback (exit 1, no gate name) | 2 |
| **independent numeric recomputations** | **329** |
| — disagreements with the delivered artifacts | **0** |

The 329 recomputations: the 22-row class table cell by cell (154), the full
locality sweep at d=2 (32), the order-collapse census (27), the light-cone
radius-profile census and its multiplicities (10), the eight-value defect
table (16), the choice inventory (15), the realization census (4), the 27
measured values the verdict carries (27), the anchor and gate totals (13), the
combinatorial identities 3364 = 58², 2304 = 48², 1792 = 4096 − 2304,
576 = 24², 738 = 588 + 150, 1024 = 32², 15625 = 25³, 24 = 5 + 10 + 9 (12), and
the remaining scalar facts — equal-time values, projective and raw order sets,
group orders 32/128, five-point sweep sizes, parity delta, monomial count,
free-pair split, scramble control quadruple (20). Independent re-derivations of
the gauge-class count (72/8 = 9, cross-checked against 9 pool representatives
on axis (0,1)) and of the like-for-like degeneracy (25 distinct non-local
pairs) are included.

---

## THE COVERAGE AND WAIVER AUDIT (#34 / #62 standards)

**Headline, independently reproduced:** 77 registered gates, 77 evaluated, 77
passed; 82 declared mutants; **82/82 killed externally, 82/82 by their declared
target gate, 82/82 exit 1, zero tracebacks**; 75 gates carry ≥1 falsifier; **2
never falsified** — exactly the delivered claim. No gate outside the registry
was killed; no registered gate went unevaluated.

**Multi-falsifier gates:** `G-VERDICT-STRING-EQUALITY` (5),
`G-PATH-VALUE-ANCHORS` (2), `G-DEFECT-VALUE-CENSUS` (2),
`G-TWOPOINT-TRANSLATION-COVARIANT` (2).

**Shadowed gates: none in the "dies earlier" sense.** Every declared mutant
reaches its target, which is a genuinely good result and better than the R6a
baseline (12 false waivers, 10 shadowed gates at #34). The shadowing here is of
a different kind and I found exactly one instance: **F5**, where the mutant
reaches the gate but is killed by a laundered identity clause rather than by a
blind predicate. Measured, not asserted: removing the clause lets the mutant
live.

**The never-falsified two, verified individually.**

*`G-DEFECT-DEFINITION-SHAPE`* — registered forcing: "analytically true by
construction … a DISCLOSURE, not a measurement; the definition's CONTENT is
measured at `G-DEFECT-DEFINITION`, which reproduces the anchored source's own
two-by-two witness and dies under `MUT-DEFECT-WITNESS`." **Verified true by
execution.** The gate is evaluated (kind `DISCLOSURE`, predicate the literal
`True`). `G-DEFECT-DEFINITION` does reproduce the Hadamard witness: it builds
H and the unbiased V over ℚ(ζ₈), checks both unitary, and requires
Δ(H,V) = 0 and Δ(H,H) = ½·[[1,−1],[−1,1]] exactly, against the values quoted
in `VB-WITNESS-2X2`. `--mutant MUT-DEFECT-WITNESS` dies there in 1.9 s with the
sign-flipped witness printed:
`Delta(H,H)=(-1)/2+(+1)/2+(+1)/2+(-1)/2`. The mechanism is real. Two
qualifications: the expected values are *typed* in Python rather than parsed
from the anchored window, so the text→test binding is by declaration; and the
"forcing is machine-checked" requirement of #34 is implemented as "a forcing
*string* is registered and the gate was evaluated" — the forcing's content is
verified by me, not by the instrument.

*`G-WAIVERS-VERIFIED`* — registered forcing: it runs after the mutant harness,
so it carries its own in-gate injection falsifier (a synthetic waiver with no
registered forcing that the same predicate must detect). **Verified genuinely
firing by execution.** I replaced the detector predicate with a constant and
the gate failed with
`falsifiable=75 waived=1 unverified=none; injected false waiver detected=False`
— the injection is a live positive control, not decoration. I additionally
injected a *real* unregistered waiver (an extra `DISCLOSURE` gate with no
falsifier and no forcing): killed, by `G-EVERY-GATE-EVALUATED`, so the registry
closes the loop even though `G-WAIVERS-VERIFIED` itself is not the one that
bites. See F12 for its reporting defect.

**Waived gates I tried to kill.** I could not kill either. Both waivers are
substantively honest. That is a positive result for the unit and I record it
as such.

**Anchor coverage (34 perturbations, all fatal by name).** 5 byte anchors via
`--break-anchor` (all die at `G-BYTE-ANCHORS`); 10 path-value rows × 2 forms
(value drift and path drift) — 20 injections, all die at
`G-PATH-VALUE-ANCHORS`; 9 verbatim windows drifted individually — all die at
`G-VERBATIM-ANCHORS`. Only 2 of the 10 path-value rows and 1 of the 9 verbatim
rows carry a *declared* falsifier, so 31 of these 34 rows were previously
untested; all 31 hold. Anchor evaluation order is as claimed: verbatim first,
then bytes, then path-values.

**Determinism.** Two plain runs on the scratch mirror produced
`58ec08893526` / `3214f4da3af2` — byte-identical to each other and to the
committed artifacts, from a different absolute repository root. Byte-identity
now confirmed three times.

**Exact arithmetic.** My own AST scan of the delivered source: 0 float
literals, 0 `float()` calls, 0 true divisions. My own recursive scan of the
delivered receipt: no float at any depth. Both independent of the unit's gates.

---

## K1–K5 AT INSTRUMENT DEPTH

**K1 (the defect census) — instrument view: the census is honest but bound at
2 %.** 4096 rows = 64², one per ordered pair, count derived; 3364 = 58² at
FULL; 588 nonzero; eight exact values whose signed cell counts sum to zero
(24·⅝ − 24·⅜ + 108·½ − 108·½ + 336·¼ − 336·¼ + 144·⅛ − 192·⅛ = 0, recomputed);
`0 of 1792` Markovian; `738 of 2304` free. Three genuinely different routes
(sparse definition, separation convolution, character basis) agree on their
declared strides, and I confirmed the routes are not algebraic restatements of
one another. But the value binding covers 12 rows / 28 cells (F3), the
Markovian zero keys on a count rather than the object (F13), and the census
numbers reach the verdict through no independent recomputation (F9).

**K2 (the L = 4 uniqueness theorem) — instrument view: the theorem is
machine-confirmed, the scale is typed.** The order-collapse census is
exhaustive over 25³ = 15,625 alphabet triples at each of nine orders (140,625
evaluations), and the delivered table is exactly reproducible. The five-point
extension (34,925 nodes, 121 leaves, 0 non-monomial) reproduces. What the
instrument does *not* do is bind the census lattice to the gate's answer: `L`
is the literal 4 and `G-UNIQUE-SCALE` is the typed anchor `admissible == [4]`
(F4, F14). The theorem's scope disclosures — alphabet-relative order-3
emptiness, unswept 9-point stencil — are printed in `not_executed` and match
the paper.

**K3 (transformation-type census) — instrument view: the strongest section.**
22 extended / 38 anchored classes; the orbits partition the pool (sizes sum to
64, verified); orbit–stabiliser holds on every class from the *measured*
action; invariants constant on every orbit; and the 22-row paper table matches
the receipt in all 154 cells. The translation-triviality reading is genuinely
gated in both directions (circulant orbits all singletons; control orbits not).
The one instrument defect here is that the class *count* in the verdict is
freely corruptible (F4).

**K4 (the gates) — instrument view: the mandatory gate is the weakest one.**
The realization census is the pin's mandatory gate and it verifies only that
the level names are legal and at least three occur (F2). The gate's *bite* is
real and well gated (`150` excluded, and `G-REALIZATION-VERDICT-ONLY-MAXIMAL`
compares the two segment renderings) — but the classification the bite depends
on is unchecked. The state-motion verdict is properly two-sided: I confirmed
`recon == Dm` reconstructs the 16-cell coefficient matrix from the 16
point-mass responses exactly, and that `distinct = 18` over 18 states is a real
measurement; the gate on the second is only `distinct > 1`, so the 18 in the
verdict is unbound (F4). The projective-period self-test is a genuine
two-sided symmetry test (invariant 42/42, raw order moves) and satisfies §14's
"evaluate fresh" addendum — the cache is cleared, a cache-free recomputation
runs alongside, and `G-CACHE-EXERCISED` gates that the cache path is actually
exercised (hits > 0 and misses > 0), which is the #219 addendum honoured
correctly.

**K5 (the instrument) — the summary judgement.** The mutant table is
disciplined and complete on its own terms: 82/82 on target, zero shadowing in
the classical sense, two honest waivers, 34 anchor rows all fatal, byte
identity three times, exact arithmetic clean, and four of five real mechanism
breaks caught. The failure is that the gates guard the *pipeline* and not the
*object*: everything computed before the verdict object exists is well
defended, and the verdict object itself — head and eighteen of its
twenty-seven measured values — is defended only by consistency between two
paths that read the same fields. Thirty-four injections walked through that
gap at exit 0.

---

## FALSE-NUMBER REPORT

**Zero false numbers.** Every hand-written numeral in the paper that I could
trace to a measurement traces correctly. Specifically checked by value against
the receipt, not by eye:

- the locality table (5 printed rows against the 8-row d = 2 Moore sweep);
  parity witness 4 vs 2, delta −2;
- the order-collapse table, all 27 cells; the ≥ 5 rows; 15,625 triples per
  order;
- five-point 34,925 / 121 / 0; nine axes 4 local + 5 non-local; alphabet 25;
- pool 64 = 58 + 4 + 2; census 4096; 3364 at FULL; 588 nonzero; 588 rational;
- the eight-value table, all 16 cells, plus the zero-sum identity;
- 16 monomial generators; 0 of 1792; 738 of 2304;
- 1024 matched, 616 agreements; 216/576; 372/1188; radius 2 both sides;
- 15/256 and −1/256; 16 separations; six radius profiles with multiplicities
  16 / 8 / 18 and 33 of 58 at the half-width; projective {1,2,4}, raw {2,4};
  42 gauge combinations; 48 coherence triples;
- 22 / 38 classes, sizes {1,2,4}, group orders 32 / 128, and the full 22-row
  class table (154 cells);
- realization 1 / 5 / 0 / 58, maximal FULL, 150 excluded; 32 scrambled defect
  tables failing with 16 identically zero; 58 circulant transition tables
  passing;
- 18 prepared states, 18 distinct responses;
- 77 gates, 24 anchors = 5 + 10 + 9, 82 mutants, 75 falsifiable, 2 waived;
- 15 choice-inventory rows.

Two prose imprecisions, neither a false number: the choice-inventory row "the
division-event times | GENUINELY-FREE | declared" renders a fibre of 1 as the
word "declared"; and "the same nine gauge classes with the same coefficient
values" in §4.4 describes a matching that is by value multiset, not by gauge
class (F8 — that one *does* need a replacement sentence, supplied above).

The delivered verdict string occurs verbatim in the paper, and is
reconstructible from the wrapped copy in `r4_defect_stage_output.txt`.

---

## WHAT I COULD NOT BREAK

Recorded so the repair pass does not "fix" what is already sound: the anchor
layer (34/34 fatal, correct evaluation order, path *and* value bound); the
byte-identity and path-independence of the artifacts; the exact-arithmetic
discipline (independently scanned); the three-route defect agreement; the
Hadamard-witness reproduction; the gauge self-test in both directions with the
cache honestly handled; the orbit/stabiliser census; the two-sided
state-motion reading; the waiver ledger's two entries, both of which I attacked
and neither of which I could falsify; and the mutant table's on-target
discipline, which is the best I have measured in this campaign.

---

## REPAIR ORDERS, IN PRIORITY ORDER

1. **F1** — derive the head inside the comparator; re-assert pre-registration
   there; three new mutants (post-build retype, ABSENT-variant, off-pin).
2. **F2** — independent recomputation of the transport level vector; single
   generator promotion and demotion mutants.
3. **F3** — gate the full value→cell-count multiset and its zero-sum identity;
   an uncensused-stratum zeroing mutant.
4. **F4** — a flip probe per measured verdict value; drive `L`/`d` into SCOPE
   from measurement; gate `L == admissible_scales[0]`.
5. **F5** — make `MUT-PRECHECK-NAMES` die by output, not by flag; extend the
   AST scan to one-hop laundering.
6. **F6** — render every paper numeral from `R`; make `--verify-paper` a
   must-pass phase of the delivery run; bind the paper's quotations.
7. **F7** — the #82 CLI-contract minimum, including validation of `--mutant`
   and `--break-anchor` arguments.
8. **F8** — match on gauge class; report distinct vs weighted counts; adopt
   the replacement sentence.
9. **F9–F12** — recompute all headline counts from the serialized receipt;
   widen the prose-invariance probe; give every verbatim row a measuring
   consumer; wrap the post-harness gates.
10. **F13–F15** — convert the highest-value fabricated mutants to mechanism
    breaks; restate `G-UNIQUE-SCALE`'s claim; derive the self-test denominator.

Numbers must not move under this repair: none of the findings above proves any
delivered number wrong. If a repair moves a number, that is a new result and
must be reported as one.
