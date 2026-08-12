# FAC (paper-35) — INSTRUMENT REVIEW (K3)

**Seat:** INSTRUMENT-LENS — gates, falsifiers, anchors, seals, transcript,
walls, windows, the CLI and #91 contract; the nine target probes with live
injections; E-22 / E-23 / E-24; the #267 checklist. **Authority:**
HANDOFF-PROMPT.md §4/§9; RUNBOOK.md E-22/E-23/E-24; the #267 checklist.

**GRADE: AWF** — accept with fixes.

**No delivered number of this unit is wrong.** Every count the paper and the
receipt publish was recomputed here from live registries or from independent
arithmetic, and none moved: Bell(9) = 21,147 and Bell(27) =
545,717,047,936,059,989,389 recomputed from scratch, 5,852 + 4 = 5,810 + 46 =
5,856, the rung decomposition 72 + 5,184 + 596 = 5,852 and 72 + 5,184 + 554 =
5,810, the threshold distribution 4 + 521 + 75 = 600, the free-groupoid counts
6⁹ = 10,077,696 / 6¹² = 2,176,782,336 / 6¹⁸ = 101,559,956,668,416, the
sub-window 72 + 600 = 672 with complement 5,184, 39 + 4 = 43 gates. The unit is
byte-reproducible off-tree, git-less, at two hash seeds, from a tree with the
artifacts deleted first. **All 36 falsifiers died at their declared gate, one
process each, out of harness, with artifacts byte-unchanged and rc = 0.** The
selftest writes nothing — proven here by a full-tree hash, not by the
instrument's own artifact check. The read-back-before-`os.replace` is real and
the staging files are removed on refusal.

**Every major below is a perimeter defect: something the instrument or the
paper SAYS it binds and does not.** Five of the nine target probes are PRESENT,
three are ABSENT, one is mixed. The two probes the unit self-repaired after
earlier rounds (the vacuous sentence-referent gate; the dead-exemption rule) are
split: the exemption repair is complete and provably inert, the referent repair
is not.

---

## 0. HASHES — VERIFIED AT OPEN AND AT CLOSE

| object | declared (sha256-12) | at open | at close |
|---|---|---|---|
| `v14/paper-35-fac.md` | `2e9cbae8a83e` | `2e9cbae8a83e` | `2e9cbae8a83e` |
| `v14/code/fac_exact.py` | `53e1e2683937` | `53e1e2683937` | `53e1e2683937` |
| `v14/code/fac_output.txt` | `43212e390250` | `43212e390250` | `43212e390250` |
| `v14/code/fac_receipt.json` | `240bad74217a` | `240bad74217a` | `240bad74217a` |
| `v14/note-fac-pin.md` (pin) | `11380265fcf3` | `11380265fcf3` | `11380265fcf3` |

All five match at open and at close. All execution was off-tree, in scratch
trees built by `rsync --exclude .git` and then by a 676 KB slim copy carrying
exactly the eleven files the instrument reads plus the two artifacts; every
destructive operation used absolute paths. Sibling working-tree drift (PERR,
POT, SPC) was neither read nor touched. **Repo writes by this seat: one — this
file.**

**Counts.** **101 instrument process launches**, of which **93 were full
43-gate evaluations**: 2 baseline delivery runs off-tree, 36 out-of-harness
`--mutant` runs one process each, **46 distinct hostile injections**, 2
byte-reproduction runs at two `PYTHONHASHSEED` values, 3 tree-preserving
confirmation runs, 1 `--selftest` (4 internal full runs), and 11 CLI-only
invocations (10 hostile argv + `--list-gates`). **≈175 discrete recomputations**
of delivered quantities; **zero disagreed**. Scratch peak for this seat: 558 MB,
released; steady state 1.2 MB; every per-run tree deleted immediately.

---

## 1. WHAT I VERIFIED FROM LIVE REGISTRIES (never from prose)

Every headline count of the claim list, read out of `fac_receipt.json` and
cross-checked against the code's registries, not against the paper:

| claim | source of truth | measured |
|---|---|---|
| 43 gates = 39 sealed + 4 closing | `len(R["gates"])`, `closing_gates.after_the_snapshot` | 39 + 4 = 43, all `passed: true` |
| 39 seals | `len(R["seal_manifest"])` = `len(SEALED_PATHS)` | 39 / 39, manifest total |
| 36 falsifiers | `len(MUTANTS)`, `coverage.rows` | 36, 36 hooked, 0 constant-boolean |
| 10 sha-pinned sources | `len(SOURCES)`, `provenance` | 10, all matched |
| 13 verbatim anchors w/ consumer gate | `verbatim_anchors` | 13 present, 13 consumer gates exist **and fire** |
| outcome vocabulary from the pin's bytes | `OUTCOME_PAT` over `note-fac-pin.md` | 5 raw → 5 families, no word typed in-code |
| 6 windows | `len(WINDOW_DECL)` | 6 (see m6) |
| 5 walls / 15 needles | `WALLS` | 5 / 15, all clean |
| 7 tables, 42 data + 7 header rows | `paper_tables` | 2+2+18+8+4+5+3 = 42, +7 headers |
| 38 class-binding rows | `class_binding.rows` | 38, 0 mismatches |
| 403 numerals + 97 spelled, 0 unbacked | `paper_coverage` | 403 scanned == 403 reference, 97 spelled, 0 unbacked |
| 190 numerals registered | `totals.numerals_registered` = `len(NUMREG)` | 190 |
| 18 referent universes | `len(REFERENT_UNIVERSES)` | 18, 3 aggregates excluded |
| 5 polarity axes both ways | `polarity.rows` | 5, all asserted present, 0 inverted |
| 9 gates without falsifiers named | `reachability.gates_without_a_falsifier` | 9, named |
| criterion digest `0019d84588bb`, leak-free | `criterion` | digest reproduces; `census_products_referenced: []` |

Every one holds. The paper's §4–§8 prose numbers also reconcile with the
receipt field by field (sub-window 76 with complement 5,780; LEG-2 = 1 and 125;
LEG-3 = 21,147; the synthetic cuts 1,015 / 125 / 104; the wedge 0 / 4;
11,799 LEG-4 passes under each coin order; 668 of 672 and 0 of 672; the
triangle's histories column summing to 672; the three alternative link-set rows
42 / 6 / 6).

**The head law is genuinely three-way.** `head_law` returns FORCED when both
grains are uniform, DECLARED when both are non-unique on the *same* set, and
STRATIFIED otherwise; the four control arenas realize the first three on real
evaluations. No pigeonhole decided the verdict.

**The out-of-harness sweep (E-23's hardest leg).** All 36 falsifiers, one
process each via `--mutant NAME`, in a tree with no `.git`:

```
36 runs, rc=0 on all 36, "on target True" on all 36, "artifacts unchanged" on all 36
```

I also read all 36 hooks located by AST against all 36 descriptions by hand.
Each description states what the code does; none is inverted; none is a
constant boolean; each is three-legged (declared gate + description + AST-located
fragment matched against the statement that carries it). **E-23 passes on the
substance, not only on the automated check.**

---

## MAJOR-1 — THE CRITERION-LEAK GATE IS A BLACKLIST, AND THE PUBLISHED DIGEST IS UNBOUND

The paper's §2 says the criterion's free names are "extracted and required to
contain no census product, so no leg can consult the answer it is deciding".
The gate's own statement repeats it. What the code does is

```python
leaks = sorted({n for names in creads.values() for n in names
                if n in CRITERION_FORBIDDEN_NAMES})
```

with `CRITERION_FORBIDDEN_NAMES = ("actor_census", "cell_census", "CENSUS",
"ADMISSIBLE_SET", "R", "VERDICT")`. That is a six-element **blacklist of
spellings**, not a property of the reference. Three independent leak channels
pass it and the whole 43-gate battery at exit 0:

| injection | channel | outcome |
|---|---|---|
| **I4a** | a module global `_ANS`, assigned after the actor census, read inside `leg1_actor` | **SURVIVES, rc = 0** |
| **I4b** | `globals().get("actor_census")` inside `leg1_actor` — the forbidden name never appears as an `ast.Name` | **SURVIVES, rc = 0** |
| **I4c** | a default-argument alias `_leak=_CACHE` on `leg3_actor` | **SURVIVES, rc = 0** |

The freezing leg of the gate is real — the digest is taken at a point where no
admissible set exists, and I confirmed the ordering in the source. The
**no-leak** leg is a spelling filter.

What makes this load-bearing rather than academic is the second half. In the
I4a run the criterion's combined digest silently moved:

```
criterion digest now: 75a05bf4bdbb
leaked names: []
paper still says: 0019d84588bb
counts: 5852 5810   (unchanged — a silent criterion swap need not move the answer)
```

Nothing catches the drift. The digest is a 12-hex token, and `HEXTOK` masks
12-hex tokens out of the numeral scan *and* out of the totality reference by
declaration (#267 M6). It is rendered in no `paper_claims` sentence and in no
table. So the paper's assertion "The combined digest is 0019d84588bb" is a
free-floating string: **I11c** rewrites it to `ffffffffffff` and the run exits 0
with the receipt and the transcript **byte-identical** to the delivered ones
(`240bad74217a` / `43212e390250`). **I11d** does the same to the paper's stated
pin digest `11380265fcf3` with the same byte-identical result.

The delivered artifact is clean — I read all ten criterion functions and none
references a census product, and `census_products_referenced: []` is true of the
delivered source. This is a gate-strength finding, not a false result.

**Fix.** Invert the test: require every free name of the ten criterion functions
to lie in a declared whitelist (the arena constants, the folding helpers, the
`ast`/builtin names actually used), and fail on anything else — including
`globals`. Then bind the digest: add `"the combined digest is %s"` to
`paper_claims` so a moved criterion breaks G-PAPER-CLAIMS, or exempt the
criterion digest from `HEXTOK` and register it.

---

## MAJOR-2 — THE SENTENCE-REFERENT GATE HAS NO TOTALITY CHECK, LOSES A REAL RATIO TO `mdstrip`, AND STILL PASSES A FALSE RELATION

Three separate defects, one gate.

**(a) No totality reference.** `paper_coverage` earns its "0 unbacked" by
arithmetic: `scanned == reference`, gated. `referent_binding` has no analogue.
It reports `relations_checked: 5` and nothing compares 5 to the number of
ratios the paper actually carries. A ratio that the scanner fails to see is
indistinguishable from a ratio that passed.

**(b) `canon()` deletes line-initial numerals — measured on the delivered
paper.** `mdstrip`'s `_MD_PREFIX = r"^(?:\s*(?:>+|[-*+]|\d+[.)])\s+)+"` treats a
line beginning `672. ` as a Markdown ordered-list marker and **removes it**.
The delivered paper wraps one of its own ratios across exactly that boundary
(lines 292–293: `...at 0 of` / `672. The carrier's excess...`). The body the
referent gate scans therefore reads:

```
...agree at the actor grain at 668 of 672 rows and at the carrier grain at 0 of The carrier's excess is freedom...
```

`RATIO_PAT` finds `668 of 672` and never sees `0 of 672`. One of the paper's
published ratios is silently unchecked in the delivered run. This is the first
measured instance; the mechanism generalizes.

**I3d** weaponizes it. Planting

```
The carrier-grain factorization is unique at 5,810 of
600. That is the window this unit declares.
```

puts a cell-census numerator over a corpus denominator — the LOR disease
exactly, and cross-universe — and the run **exits 0**. `600.` is eaten as a list
marker before `RATIO_PAT` runs. Every numeral is backed, so the coverage gate is
silent too.

**(c) The universes are still coarse.** The self-repair excluded `counts`,
`verdict` and `measure_relativity` because "a universe carrying every number
binds nothing". But the surviving universes are top-level receipt keys, each
carrying heterogeneous quantities: `actor_census` carries both the 5,856-history
axis *and* the 21,147-partition axis; `cell_census` carries 46 *and* 42,295;
`controls`, `grain_triangle` and `windows` are similarly mixed. **I3a** plants

> The actor-grain factorization is unique at 5,852 of 21,147 committed histories.

— a histories count over a partition-lattice size, a false relation with both
numerals true — and it **survives at exit 0**, bound through `actor_census`. The
disease the gate is named for is still expressible; the repair narrowed it, it
did not close it.

For the record, the gate does work where it reaches: **MUT-REFERENT** (5,852 of
42,295, cross-universe, mid-line) dies on target out of harness.

**Fix.** (i) Run the ratio scan over a body normalized by ASCII-fold and
whitespace only, never through `mdstrip`; or make `_MD_PREFIX` require the
marker to be followed by a non-digit context. (ii) Publish a totality
reference — count `N of M` occurrences in the raw paper and gate
`relations_checked == that`. (iii) Bind ratios to a *quantity axis*
(histories / partitions / cells / arrows), not to a receipt key.

---

## MAJOR-3 — PROSE POLARITY IS UNGUARDED, INCLUDING ON A DECLARED AXIS

The `atom-word` polarity axis keys on the fence form
`ATOM=FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN`. That choice is defended in the
code comment — the bare word appears as legitimate *data* in T6's control rows,
so a bare-word scan would false-positive. The cost is that the paper's own
assertion of its atom word, in §5, is outside the axis:

> and the word this unit emits, `FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN`, is
> computed from that count.

**I2a** flips that occurrence to `...HOLDS...`. The paper then asserts, in the
sentence that claims the word is *computed*, the opposite of its own head — and
the run **exits 0**. This is inside the surface the unit advertises: an axis
named `atom-word` that does not catch an atom-word inversion in the paper.

Three further inversions in unrendered prose survive at exit 0:

| injection | inversion | outcome |
|---|---|---|
| **I2b** | §8 "the law returns the forced word" → "the declared word" | SURVIVES |
| **I2f** | §3 "admissible precisely when the history **never** distinguishes the actors a coarsening would merge" → "**always** distinguishes" — the sentence the paper calls "a description of the mechanism rather than a summary of the count" | SURVIVES |
| **I9b** | "There are seventeen declared coherence relations" (true: 6) | SURVIVES — 17 is in the allow-set (it is `len(CLOSING_GATE_NAMES)`) |

The rendered surface, by contrast, is hard. Four inversions die at named gates,
artifacts unchanged:

| injection | inversion | died at |
|---|---|---|
| **I2c** | "disagree on 0 census rows" → "3 census rows" | `G-PAPER-CLAIMS` (missing C05) |
| **I2d** | "is unique at 5,852" → "is non-unique at 5,852" | `G-PAPER-CLAIMS` (missing C02) |
| **I2e** | the thesis `...ONLY-WHERE-THE-HISTORY-REPEATS...` → `...EVERYWHERE-EXCEPT-WHERE...`, in **both** fence copies | `G-PAPER-NUMERAL-COVERAGE` (`fences False`) |
| **I11g** | T1's `actor`/`carrier` grain labels exchanged | `G-PAPER-TABLES-WITH-HEADERS` |

**Fix.** Add a polarity axis on the bare atom word scoped to the paper *outside*
the T6 rows (e.g. scan the non-table lines), and add C11 rendering the atom word
and C12 rendering the mechanism sentence's direction word to `paper_claims`.

---

## MAJOR-4 — THE ACT DISEASE IS PRESENT: A KEY FORGED AFTER THE TOTALITY GATE IS PUBLISHED UNSEALED AT EXIT 0

`G-SEAL-TOTALITY` claims, universally: "Every published receipt key is either
sealed at the gate that established it or named in the declared-unsealed list."
It computes `published` from `R` *at gate time*. Four statements later, `R` is
serialized. Anything added in that window is published, sealed by nothing, and
named by nothing.

**I7a** inserts one statement between `R["seal_manifest"] = SEAL.rows` and
`payload = json.dumps(R, ...)`:

```python
R["reviewer_forged_headline"] = {"actor_unique": 1, "claim": "THE DIVISION IS FORCED"}
```

The run **exits 0** with that key in the promoted receipt. `SEAL.close` verifies
only the 39 declared paths and is blind to a new top-level key.

The control fixes the window precisely. **I12c** inserts the *same kind* of key
one statement **earlier**, before `SEAL.totality()`:

```
[FAIL] G-SEAL-TOTALITY :: seals 39, missing none, extra none,
       unsealed keys ['reviewer_unsealed_key'], closing gates that did not run none
```

So the gate is correct and the *ordering* is the defect.

A second face of the same issue: the four `DECLARED_UNSEALED` keys are published
claims that nothing checks. **I7c** rewrites `R["arithmetic"]` from "exact
integers and Z[w] pairs; no float anywhere" to "IEEE754 double precision
throughout; floats everywhere" — the run **exits 0**, and `G-NO-FLOATS` still
passes, because the string and the scan are never compared.

The seal machinery itself is sound where it applies. **I12b** mutates a *sealed*
subtree (`R["counts"]["actor_unique"] = 5856`) after its seal:

```
[FAIL] G-ARTIFACT-INTEGRITY :: the payload was sealed over a broken seal :: ['SEAL-COUNTS']
```

and **I7b** appends a forged row to the manifest itself:

```
[FAIL] G-ARTIFACT-INTEGRITY :: the payload was sealed over a broken seal :: ['SEAL-FORGED']
```

**Fix.** Move the `published`/`unsealed` computation and the totality gate to
immediately before `json.dumps`, or recompute `unsealed` inside `SEAL.close`
against the object actually being serialized. Bind `arithmetic` to `G-NO-FLOATS`
by rendering it from the scan's result rather than typing it.

---

## MAJOR-5 — THE TABLE AND FENCE CHECKS ARE ONE-DIRECTIONAL: FORGED ROWS AND FORGED FENCES RIDE IN AT EXIT 0

`G-PAPER-TABLES-WITH-HEADERS` requires *rendered ⊆ paper*, cell by cell. Nothing
requires *paper ⊆ rendered*. The fence check has the same shape: `want` is
required to be present with the right copy count, but extra fenced blocks are
not enumerated.

In-place corruption is caught — **I1a** (T3 `minimum`↔`maximum`), **I1b** (T4
`TEST-RAW at ACTOR-S9`↔`TEST-RAW at CARRIER-S27` and the two TEST-REALIZABLE
columns), **I1c** (T5 `actor non-unique`↔`carrier non-unique`), **I11g** (T1's
grain labels) all die at `G-PAPER-TABLES-WITH-HEADERS` with artifacts unchanged,
each naming the exact missing header or row. Additive corruption is not:

| injection | forgery | outcome |
|---|---|---|
| **I1d** | two extra T2 rows, grain labels swapped, every numeral backed: `\| actor \| 5,810 \| 46 \| 5,856 \|` and `\| carrier \| 5,852 \| 4 \| 5,856 \|` | **SURVIVES, rc = 0** |
| **I1e** | a "Restated:" duplicate of the census table with `unique`/`non-unique` headers exchanged, printed beside the true one | **SURVIVES, rc = 0** |
| **I11h** | an extra control-arm row `\| CTRL-THE-WHOLE-CORPUS \| 5,856 \| 0 \| 0 \| FAC-FACTORIZATION-FORCED \|` | **SURVIVES, rc = 0** |
| **I11b** | an **extra fenced verdict block** with the two grains' uniqueness counts exchanged (`ACTOR-GRAIN-UNIQUE-FACTORIZATION=5,810-OF-5,856; CARRIER-...=5,852-OF-5,856`) | **SURVIVES, rc = 0** |

I11h is the sharpest: a forged control row asserting the FORCED head word on the
whole corpus, in the paper, at exit 0 — precisely the reading the control arm
exists to exclude. I11b is next: a fourth verdict fence contradicting the three
real ones, at exit 0.

**Fix.** Make both checks bijections. Require the multiset of the paper's
markdown table rows *inside the sections that carry tables* to equal the
rendered multiset; require `Counter(canon(b) for b in FENCE.findall(text))` to
equal `want` exactly rather than dominating it.

---

## MINORS

**m1 — The transcript is sealed for integrity but never reconciled with the
sealed gate ledger.** The full-byte claim is honest: `whole` and `staged` are
digests of the complete `LINES` list, no whitelist, no indentation class, no
substring acceptance (I read `finish` line by line; `MUT-TRANSCRIPT` dies out of
harness). But nothing compares the transcript's `[PASS] G-…` lines to
`R["gates"]`. **I5a** appends `  [PASS] G-FORGED-BY-THE-REVIEWER` to a
transcript line *before* the digest is taken. Confirmed in a preserved tree: the
promoted `fac_output.txt` carries the forged line (1 occurrence), the receipt's
gate ledger contains no such gate (`[]`), `whole == staged` is `True`, and the
run exits 0. **Fix:** derive the gate lines of the transcript from `R["gates"]`
at seal time, or gate `set of G-names in LINES == set of gate names in R`.

**m2 — Anchor and seal "consumer gate" names are not existence-checked.**
`G-VERBATIM-ANCHORS-IN-SOURCE` checks `all(v["consumer_gate"])` — non-emptiness,
not existence. **I6a** renames V01's consumer to `G-NO-SUCH-GATE-EXISTS-ANYWHERE`
and **I6b** renames SEAL-ARENA's `sealed_at_gate` to `G-PHANTOM-SEAL-GATE`; both
**survive at exit 0**. In the delivered artifact the property holds — all 13
anchors are present in their sources, all 13 named gates exist and all 13 fire —
so this is enforcement, not fact. Note the falsifier table *does* carry
`gate_exists` and gates it; the anchor and seal tables should borrow it.

**m3 — E-24 is gated on the top-level stamp only.** The gate statement says
"each is stamped COUNTING-ONLY", but the condition reads
`R["measure_relativity"]["stamp"] == "COUNTING-ONLY"`. **I11a** sets
`rows[0]["stamp"] = "PROBABILITY"` and the run **exits 0**. Separately, the
statement's clause "or whose numerator and denominator come from different
windows, fails here" is unimplementable as written — each row carries a single
`window` field, so the condition cannot be expressed, let alone checked. The
substance is right: all six ratios (including the Bell(27) row, 42,295 against
545,717,047,936,059,989,389) carry a window and satisfy numerator ≤ denominator,
and `MUT-E24` dies on target.

**m4 — The corpus is a multiset and the paper does not say so.** The receipt
publishes `distinct_histories: 5,784` against `total_histories: 5,856`; the
paper writes "5,856 committed histories" throughout and never mentions 5,784. I
located the duplication: **C1 (72) and C2 (5,184) are duplicate-free; C3's 600
driven-window schedules yield only 528 distinct histories — 519 appear once and
9 appear nine times each** (519 + 81 = 600; 519 + 9 = 528; 72 + 5,184 + 528 =
5,784). No headline is corrupted — the four non-unique histories are C3
singletons at indices 5,256 / 5,341 / 5,426 / 5,511, one per parallel class,
each with inventory count 1 — but "5,852 of 5,856" and "596 of 600" are counts
over corpus *slots*, not over distinct histories, and a reader is not told.

**m5 — The grain-triangle / groupoid-arrow sub-window is not a declared
window.** §5 says "on the 672 histories of the declared sub-window" and §6's
entire table runs on the same 672 (= C1's 72 + C3's 600). The six entries of
`WINDOW_DECL` do not include it: `W-FULL-LATTICE-PER-LEG` is the 76-history
per-leg sweep, `W-COHERENCE-LADDER` is a set of relations. The receipt does
disclose `grain_triangle.sub_window: 672` with `complement: 5184` and
`groupoid.arrow_sub_window: 672`, but §6 never names its complement (5,184) the
way §4 names its own (5,780), and §10's "6 windows are declared with their
bounds" undercounts the windows in use.

**m6 — Two declared windows publish `members: 0` as a size.**
`W-FULL-LATTICE-PER-LEG` and `W-CONTROL-ARENAS` are hard-mapped to `size = 0` in
the windows table. The real per-leg sub-window is 76. A placeholder is published
in a numeric field indistinguishable from a measurement.

**m7 — `families_no_arena_reached: []` claims more than the computation
supports.** `words` is the union of the control arenas' head words, the
synthetic histories' atom words, **and three direct invocations**
`atom_law(0, True)`, `atom_law(1, True)`, `atom_law(1, False)`. Arenas reach
four of the five pin families; the fifth, `FAC-BLOCKED-AT`, is reached only by
the third direct call with hand-supplied arguments. The **gate statement is
honest** about this ("its blocked word is reachable only from an instrument
fault, which is what that word is for") — it is the receipt key's *name* that
overstates. Rename it, or split arena-reached from law-reached.

**m8 — The walls are 15 exact needles, not paraphrase-hardened.** The
normalization is genuinely strong: markdown prefixes, emphasis, ASCII fold, and
a whitespace-free second pass, so bullet-wrapped and list-marker-split plants
are still caught, and `MUT-WALL-PLANT` dies on target. But **I11e** plants "The
law forces the actor factorization, and actors are genuine persisting threads."
— a word-order paraphrase of two banned needles — and the run **exits 0**. The
warrant's phrase "paraphrase-hardened" describes three or four listed variants
per wall, not paraphrase invariance. The walls *do* scan the verdict fences and
the head (the scanned text is the whole paper, 22,846 characters), which I
verified in code.

**m9 — The spelled-numeral scan has no totality reference and never composes
compounds.** `paper_coverage` earns "403 of 403" by arithmetic for digits; the
97 spelled numerals have no analogous reference. The scan is per word:
`WORDTOK` splits, `WORDNUM` maps, each atom is checked alone. The planted
compound "five thousand eight hundred fifty-three" (**I9a**) *did* die —

```
[FAIL] G-PAPER-NUMERAL-COVERAGE :: scanned 403 of 403, unbacked none,
       spelled 103 unbacked ['fifty', 'hundred', 'thousand'], fences True
```

— but for the incidental reason that 1000, 100 and 50 are individually unbacked,
not because 5,853 was ever computed. A compound built from backed atoms would
pass, and the single-word case already does (**I9b**, "seventeen", true value
6).

**m10 — `G-PAPER-CLAIM-POLARITY` does not require the asserted form to be
present.** The condition is `inverted_forms_present == 0` alone. All five
asserted forms *are* present in the delivered paper (verified), but an axis
whose asserted form vanished would pass.

**m11 — The paper does not disclose that 9 of its 43 gates carry no
falsifier.** The receipt names them —
`G-ARTIFACT-INTEGRITY, G-CORPORA-SHAPE, G-FALSIFIER-COVERAGE,
G-FALSIFIER-REACHABILITY, G-NO-FLOATS, G-NO-TYPED-COUNTS,
G-PROVENANCE-SHA-PINNED, G-READS-DECLARED, G-VERBATIM-ANCHORS-IN-SOURCE` — and
the list is derived from live registries and sealed, not typed. But §10 says
only "36 falsifiers are declared, each naming the gate it must die at", which
invites the reading that the battery is total, and no per-gate justification is
given for the nine. I exercised six of them by hand and **all six have teeth**
(see §3 below), and `--selftest` exercises two more, so the surface is sound —
it is the disclosure that is missing.

---

## 2. THE NINE PROBES — PRESENT / ABSENT WITH EVIDENCE

**1. UNBOUND HEADERS — ABSENT in place, PRESENT additively.** Every rendered
header is required in the paper cell by cell, so semantically-opposed swaps die:
I1a (T3 `minimum`↔`maximum`) → `G-PAPER-TABLES-WITH-HEADERS ::
missing ['T3-THE-COHERENCE-LADDER/HEADER']`; I1b (T4 the two TEST-RAW columns
*and* the two TEST-REALIZABLE columns) → `missing ['T4-THE-GRAIN-TRIANGLE/HEADER']`;
I1c (T5 `actor non-unique`↔`carrier non-unique`) → `missing
['T5-THE-CONTROL-ARM/HEADER']`; I11g (T1's ACTOR/CARRIER row labels) → `missing
['T1-THE-GEOMETRY-LEG/actor', 'T1-THE-GEOMETRY-LEG/carrier']`. All four
artifacts-unchanged. **But** a swapped-header duplicate table (I1e) and forged
extra rows (I1d, I11h) survive — see MAJOR-5.

**2. DIRECTION FLIPS — PRESENT in prose, ABSENT in the rendered surface.**
Deaths at named gates: "0 disagreements"→"3" (I2c, `G-PAPER-CLAIMS`/C05);
"unique at 5,852"→"non-unique at 5,852" (I2d, `G-PAPER-CLAIMS`/C02); the thesis
ONLY-WHERE inverted in both fence copies (I2e, `G-PAPER-NUMERAL-COVERAGE`,
`fences False`). Survivals: "ATOM-BREAKS"→"ATOM-HOLDS" in §5 prose (I2a);
"forced word"→"declared word" in §8 (I2b); the §3 mechanism sentence's
"never"→"always" (I2f). See MAJOR-3.

**3. THE SELF-REPAIRED HOLES — (a) PRESENT, (b) ABSENT.**
(a) Residual aggregates are exploitable: I3a ("unique at 5,852 of 21,147
committed histories") binds through `actor_census` and survives; I3d
("5,810 of\n600.") is never even scanned because `mdstrip` eats the denominator,
and survives. See MAJOR-2.
(b) The exemption rule is **complete**. `NUMERAL_EXEMPTIONS = ()` in the
delivered source, and the gate refuses both directions: a **dead** exemption
fails (`I3b`, planted directly in the tuple → `G-PAPER-NUMERAL-COVERAGE`) and a
**fired** exemption fails too (`I3c`, exemption + matching numeral in the paper →
same gate, `scanned 404 of 404`). The mechanism is provably inert: no exemption
can ever be live. This is a real improvement and should be kept as precedent.

**4. THE CRITERION-LEAK GATE — PRESENT.** Defeated three ways (alias, `globals()`,
default argument), all at exit 0; the modified digest is caught by no seal and
no gate, and the paper's stated digest is unbound (I11c redeploys byte-identical
artifacts). See MAJOR-1.

**5. TRANSCRIPT INTEGRITY — forgeable clauses ABSENT; cross-ledger consistency
PRESENT.** Full-byte equality is genuinely claimed and genuinely implemented on
both legs (`digest("\n".join(LINES))` vs `digest("\n".join(staged))`, then the
staged bytes read back from disk against `seal_t`). There is no whitelist, no
indentation class and no `contains` clause anywhere in `finish` — I grepped and
read it. `MUT-TRANSCRIPT` dies out of harness. The gap is m1: the transcript is
never reconciled with the sealed gate ledger, and I5a rides a forged
`[PASS] G-FORGED-BY-THE-REVIEWER` line into the promoted transcript at exit 0.

**6. PHANTOM CONSUMERS — ABSENT as fact, PRESENT as enforcement.** All 13
anchors are present in their sources; all 13 named consumer gates exist in the
39-row ledger and all 39 gates passed, so every anchor is genuinely consumed. No
receipt field names a nonexistent gate: `coverage.gates_named_that_do_not_exist`
is `[]` and is *gated*. But the anchor table and the seal table do not
existence-check their gate names (I6a, I6b survive) — m2. The 9 falsifier-less
gates are named honestly, derived from live registries and sealed, and the
naming is not itself gated for completeness or justification; the paper does not
disclose them — m11.

**7. HONEST DENOMINATORS + WALL SURFACE — denominators honest; unsealed-key
forgery PRESENT; walls reach the head.** Coverage denominators are gated by
equality, not by construction: `scanned == reference` (403 == 403) and
`required == matched` with `absent_required == 0` for the 10 claims — I confirmed
both conditions in code and both fire (I2c/I2d/I3b/I3c/I9a). `G-SEAL-TOTALITY`
computes 39 seals over the published keys and fires correctly when a key is
added before it (I12c). The ACT disease is present in the post-gate window (I7a)
and the four `DECLARED_UNSEALED` keys are unchecked published claims (I7c) —
MAJOR-4. The wall sweep does reach the verdict and the head: the scanned text is
the whole paper including all six fenced blocks (22,846 characters). The wall
surface is 15 exact needles under strong normalization; a word-order paraphrase
evades (I11e) — m8.

**8. CLOSING GATES + READ-BACK — ABSENT (the strongest part of the unit).**
Post-`os.replace` corruption is impossible because the read-back happens first,
and I proved the comparator is live rather than decorative:
- **I8a** appends 21 bytes to the staged transcript between the write and the
  read-back → `G-ARTIFACT-INTEGRITY :: transcript staged fbbcd9c3fb8f seal
  43212e390250 ... promoted False`, rc = 1, **artifacts byte-unchanged**, and in
  a preserved tree **0 `.tmp` files remain**. Staging removal on refusal is real.
- **I8b** neutralizes the one-bit-flip control (`flipped = raw_t`) → the gate
  fails with `one-bit-flip control rejects False`. The control is a conjunct of
  the pass condition and can fail, so it is not decoration — though on unmodified
  code it is tautological (a flipped byte cannot collide under SHA-256), so it
  demonstrates the comparator runs rather than that it discriminates.
- **I8c** forces `ok = False` → fails, nothing promoted, artifacts unchanged.
- **I12b / I7b** show the seal machinery catches post-seal mutation of a sealed
  subtree and a forged manifest row, both at `G-ARTIFACT-INTEGRITY`.

**9. SPELLED NUMERALS — PARTIALLY PRESENT.** The *digit* scan has the claimed
arithmetic totality and it is gated (`scan_is_total`, 403 == 403), covering
prose, tables, inline code spans (only two spans carry digits — the two file
paths — and the raw-text scan reaches them) and the fenced verdict blocks; the
fence multiset with `FENCE_COPIES = 2` is gated and `MUT-COVERAGE-SCAN` and
`MUT-PAPER-FENCE-MULTISET` both die out of harness. The *spelled* scan has no
totality reference and never composes compounds: the planted "five thousand
eight hundred fifty-three" died only on its atoms (I9a), and a false single-word
claim survives (I9b). See m9.

---

## 3. E-22 / E-23 / E-24, THE CLI, AND THE REPRODUCTION LEDGER

**E-22 — PASSES.** Fence multiset including copy counts (`FENCE_COPIES = 2`,
`want`/`got` Counters, gated, and `MUT-PAPER-FENCE-MULTISET` dies); inline code
spans included (the scan runs on raw text, not on `canon`); **all** table rows
*and* headers rendered from the receipt and required present (42 + 7). The one
gap is directionality — MAJOR-5.

**E-23 — PASSES on the substance.** All 36 descriptions read against their
AST-located hooks by hand: none inverted, none a constant boolean, all
three-legged. All 36 executed out of harness, one process each, each dying at
its declared gate with artifacts byte-unchanged. The 9 falsifier-less gates are
named in the receipt; I exercised six of them by hand and all six have teeth:

| gate without a falsifier | my injection | died at |
|---|---|---|
| `G-NO-FLOATS` | a `0.5` constant added to the source (I13a) | `G-NO-FLOATS :: float sites [689]` |
| `G-CORPORA-SHAPE` | one extra C2 entry (I13d) | `G-CORPORA-SHAPE :: C1 72, C2 5185, C3 600, total 5857` |
| `G-READS-DECLARED` | an undeclared `read_bytes` (I13f) | `G-READS-DECLARED :: sources 11 declared 10, extra [...]` |
| `G-FALSIFIER-COVERAGE` | MUT-CLASSWORD's description and fragment retargeted (I13e) | `G-FALSIFIER-COVERAGE :: description mismatches ['MUT-CLASSWORD']` |
| `G-NO-TYPED-COUNTS` | a numeral typed into claim C08's template (I13b) | `G-PAPER-CLAIMS` (fires first, same run, rc = 1) |
| `G-PROVENANCE-SHA-PINNED`, `G-VERBATIM-ANCHORS-IN-SOURCE` | `--selftest` | both, on all four anchor classes |

Only `G-FALSIFIER-REACHABILITY` and `G-ARTIFACT-INTEGRITY` were left to
argument, and I exercised `G-ARTIFACT-INTEGRITY` five ways above.

**E-24 — PASSES with m3.** Six ratios, each carrying its declared window and its
COUNTING-ONLY stamp, each with numerator ≤ denominator; the Bell(27) ratio row
(42,295 against 545,717,047,936,059,989,389) is stamped and windowed like the
rest, which is exactly where a probability reading would have been most
tempting; `declared_measure: null`. The per-row stamp is not gated — m3.

**The pin-vocabulary parse — LIVE AND GATED.** I edited the pin in the mirror
(`FAC-STRATIFIED-<by-grain>` → `FAC-LAYERED-<by-grain>`) and re-pinned its
digest in `SOURCES` so the provenance gate would not mask the test (I10). The
run dies:

```
[FAIL] G-EVERY-OUTCOME-WORD-EMITTABLE :: head words ['FAC-FACTORIZATION-DECLARED',
'FAC-FACTORIZATION-FORCED', 'FAC-STRATIFIED'], atom words [...],
unreached families ['FAC-LAYERED']
```

The vocabulary really is the pin's bytes: a renamed family propagates and is
caught. (It dies one gate earlier than `G-HEAD-WORDS-COME-FROM-THE-PIN`, which
would also have caught it.) An unmodified pin corruption dies at
`G-PROVENANCE-SHA-PINNED`, as `--selftest` confirms.

**Hostile argv — CLEAN.** Ten forms, all `rc = 2`, all with a usage line, none
writing anything: `--bogus`, `-h`, `--mutant` (no name), `--mutant NOPE`,
`--mutant=NOPE`, `--quiet extra`, `--`, `--MUTANT=MUT-ATOM`,
`--list-gates --nope`, `--sweep=1`. Artifacts unchanged, no `.tmp` left. The
whitelist is total — nothing is silently ignored.

**Byte ×2, off-tree, git-less, two hash seeds.** In a slim tree with no `.git`
anywhere and with **the artifacts deleted first**, so nothing could be
carried over:

| run | `PYTHONHASHSEED` | receipt | transcript |
|---|---|---|---|
| A | 0 | `240bad74217a` | `43212e390250` |
| B | 987654321 | `240bad74217a` | `43212e390250` |
| committed | — | `240bad74217a` | `43212e390250` |

Both identical to the delivered artifacts, rc = 0.

**Selftest write-nothing — proven by tree hash.** The instrument reports
"artifacts unchanged"; I checked the stronger claim. Hash of the hashes of every
file in the tree, before and after `--selftest`:

```
before: 54f42079f62e3ff323417ff237d8d53632d3290a36e19eb7196f481b14b8ec0f
after:  54f42079f62e3ff323417ff237d8d53632d3290a36e19eb7196f481b14b8ec0f
```

Identical. All four anchor classes died (A-PIN and A-RUNBOOK at
`G-PROVENANCE-SHA-PINNED`, V01 and V11 at `G-VERBATIM-ANCHORS-IN-SOURCE`),
rc = 0.

---

## 4. INJECTION LEDGER — 46 INJECTIONS, EVERY GATE EVALUATION

Deaths (23): each rc = 1, artifacts byte-unchanged, nothing promoted.

| # | injection | died at |
|---|---|---|
| I1a | T3 `minimum`↔`maximum` header swap | `G-PAPER-TABLES-WITH-HEADERS` |
| I1b | T4 TEST-RAW / TEST-REALIZABLE header swaps | `G-PAPER-TABLES-WITH-HEADERS` |
| I1c | T5 actor/carrier non-unique header swap | `G-PAPER-TABLES-WITH-HEADERS` |
| I2c | coin disagreements 0 → 3 | `G-PAPER-CLAIMS` |
| I2d | "unique at 5,852" → "non-unique at 5,852" | `G-PAPER-CLAIMS` |
| I2e | thesis ONLY-WHERE inverted, both fences | `G-PAPER-NUMERAL-COVERAGE` |
| I3b | dead numeral exemption planted in the tuple | `G-PAPER-NUMERAL-COVERAGE` |
| I3c | live exemption + matching numeral in the paper | `G-PAPER-NUMERAL-COVERAGE` |
| I7b | forged seal-manifest row | `G-ARTIFACT-INTEGRITY` |
| I8a | staged transcript corrupted before read-back | `G-ARTIFACT-INTEGRITY` |
| I8b | one-bit-flip control neutralized | `G-ARTIFACT-INTEGRITY` |
| I8c | `ok = False` forced | `G-ARTIFACT-INTEGRITY` |
| I9a | "five thousand eight hundred fifty-three" | `G-PAPER-NUMERAL-COVERAGE` |
| I10 | pin outcome family renamed + re-pinned | `G-EVERY-OUTCOME-WORD-EMITTABLE` |
| I11g | T1 grain labels exchanged | `G-PAPER-TABLES-WITH-HEADERS` |
| I12b | sealed subtree mutated after its seal | `G-ARTIFACT-INTEGRITY` |
| I12c | unsealed key added before the totality gate | `G-SEAL-TOTALITY` |
| I13a | float constant in the source | `G-NO-FLOATS` |
| I13b | typed count in a claim template | `G-PAPER-CLAIMS` |
| I13d | corpus shape broken | `G-CORPORA-SHAPE` |
| I13e | falsifier description/fragment retargeted | `G-FALSIFIER-COVERAGE` |
| I13f | undeclared read | `G-READS-DECLARED` |
| I13c | (void — my slim tree lacked the target file; re-run as I13f) | — |

Survivals (22), each rc = 0, each a defect located above:

| # | injection | finding |
|---|---|---|
| I1d | forged T2 rows, labels swapped | MAJOR-5 |
| I1e | duplicate census table, headers swapped | MAJOR-5 |
| I11b | extra forged verdict fence, grains exchanged | MAJOR-5 |
| I11h | forged control row asserting FORCED on the whole corpus | MAJOR-5 |
| I2a | atom word inverted in §5 prose | MAJOR-3 |
| I2b | "forced word" → "declared word" | MAJOR-3 |
| I2f | mechanism sentence "never" → "always" | MAJOR-3 |
| I9b | "seventeen declared coherence relations" | MAJOR-3 / m9 |
| I3a | false intra-universe ratio 5,852 of 21,147 | MAJOR-2 |
| I3d | false ratio hidden by `mdstrip`'s list-marker swallow | MAJOR-2 |
| I4a | criterion leak via module-global alias | MAJOR-1 |
| I4b | criterion leak via `globals()` | MAJOR-1 |
| I4c | criterion leak via default argument | MAJOR-1 |
| I11c | paper's criterion digest forged (artifacts byte-identical) | MAJOR-1 |
| I11d | paper's pin digest forged (artifacts byte-identical) | MAJOR-1 / m9 |
| I5a | forged `[PASS]` line in the promoted transcript | m1 |
| I6a | phantom consumer gate on anchor V01 | m2 |
| I6b | phantom `sealed_at_gate` on SEAL-ARENA | m2 |
| I7a | unsealed key forged after the totality gate | MAJOR-4 |
| I7c | `arithmetic` rewritten to assert floats | MAJOR-4 |
| I11a | per-row E-24 stamp set to PROBABILITY | m3 |
| I11e | wall paraphrase (word order) | m8 |

---

## 5. WHAT THE PANEL SHOULD NOT LOSE

The census, the groupoid ladder, the grain triangle and the transport rows are
sound, exactly reproducible, and internally consistent to the last digit. The
control arm is real: three different head words on three declared arenas, both
atom words on declared synthetic histories, and the record leg — non-binding on
the committed corpus — exercised on the control with the modulo-three wedge
firing 4 times. `distinct_histories` is *published* even though the paper does
not use it, which is how I was able to find m4 at all; that is the receipt
behaving well. The exemption mechanism (probe 3b) is closed in both directions
and is the cleanest such repair I have seen in this programme.

The five majors are all of one shape: a check that is **one-directional, a
blacklist, or ordered one statement too early**. None of them touches a measured
quantity. All five are mechanically fixable without re-running the physics —
four of the five need no recomputation at all, and the fifth (binding the
criterion digest into `paper_claims`) needs one line in the paper.

**Verdict: AWF.** Candidate until adjudication.

---

*K3 INSTRUMENT-LENS. Object hashes re-verified at close (§0): all five
unchanged. Repo writes by this seat: one — this file.*
