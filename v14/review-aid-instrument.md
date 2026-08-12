# AID (paper-33) — K3 INSTRUMENT-LENS HOSTILE REVIEW

**Reviewer:** K3 (instrument lens), v14 panel.  **Object at 9f14488:**
`v14/paper-33-aid.md` 507da54ae871, `v14/code/aid_exact.py` edf3a540cd57,
`v14/code/aid_output.txt` 48fe931bfcdc, `v14/code/aid_receipt.json`
cd938d7ae9be; pin `v14/note-aid-pin.md` 294ffe6c9deb.  All five sha256-12
verified at open and at close; the repository objects are unchanged by this
review (siblings disclaimed).  Every execution ran off-tree in
`scratchpad/aid-in/`.

## GRADE: AWF (accept with fixes)

The census is right.  Sixty-eight published quantities were recomputed from
scratch by a route that shares no code with the unit — my own partition
enumeration, my own stabilizer by explicit filtering inside Stab(F₁), my own
orbit closure, my own Z[w] walk — and **68 of 68 agree, zero mismatches**.
The 47-falsifier sweep run OUTSIDE the unit's harness kills 47 of 47 with the
tree byte-unchanged under an independent hash.  Byte-reproduction holds twice
off-tree and git-less.

What fails is the binding between the measurements and the prose that reports
them.  **One sentence of the delivered paper is false** (M-1), and it is a
sentence the claim instrument RENDERED from the receipt — the two numerals it
joins are computed over different families.  The same family switch confounds
the unit's E-24 demonstration (M-2).  The paper-binding surface is one-way
(M-3), a consumer gate named twice in the receipt does not exist (M-4), and
the artifacts are promoted before they are verified while four of the
fifty-two gate verdicts reach neither artifact (M-5).

## COUNTS

| leg | count |
|---|---|
| executions of `aid_exact.py` | 94 |
| — plain runs off-tree (`PYTHONHASHSEED` 0 and 987654) | 2 |
| — paper injections (INJ01–INJ23, one re-run) | 24 |
| — declared mutants, outside the harness, one fresh tree each | 47 |
| — hostile argv vectors | 19 |
| — `--selftest`, bare-copy abort | 2 |
| independent recomputations of published values | 68 (68 agree) |
| independent instrument recomputations (numeral sweep, families, seals, phantoms, transcript, table totals) | 46 |
| **recomputations, total** | **114** |
| findings | 5 MAJOR, 5 MINOR |

## FINDINGS

### MAJOR-1 — a false sentence in the paper: the prefix census joins two families

`CLAIM-PREFIXES` renders, and §2 carries verbatim:

> the census runs over 101,160 prefix objects, 41,347 of them distinct.

`prefix_objects_total` = 101,160 is summed over the THREE primary corpora
(`CORPORA` = C1, C2, C3; `full_run` line 1348).  `distinct_prefixes` = 41,347
is the size of `ordered`, built over FOUR corpora — C1, C2, C3 **and the
1,944-history seed fan** (lines 1462–1469).  Measured by me:

| family | prefix objects | distinct |
|---|---|---|
| three primary corpora | 101,160 | **39,747** |
| four declared corpora | **118,656** | 41,347 |

Of the 101,160 objects the sentence quantifies over, 39,747 are distinct, not
41,347; the extra 1,600 distinct prefixes exist only in the seed fan, whose
17,496 prefix objects the sentence's first numeral excludes.  Each numeral is
individually receipt-backed, which is exactly why every gate passed: nothing
binds two numerals of one sentence to one referent.  §4 is written correctly
("all 41,347 distinct prefixes **of the four corpora**"); §2 is not.

**REPAIR (exact).** Publish the pair per family.  In `full_run`, replace the
single `prefix_objects_total` with

```
"prefix_objects_by_family": {
    "THREE-PRIMARY": sum(len(H) for _n, HS, _s in CORPORA for H in HS),
    "FOUR-DECLARED": sum(len(H) for _n, HS, _s in CORPORA for H in HS)
                     + sum(len(H) for H in C1FAN)},
```

render `CLAIM-PREFIXES` from ONE family ("118,656 prefix objects over the four
declared corpora, 41,347 of them distinct"), and add to `G-CORPORA-SHAPE` the
per-object gate `distinct_prefixes <= prefix_objects_of_the_same_family`,
which is the arithmetic the false sentence violates.

### MAJOR-2 — the E-24 pair is confounded by the same family switch

§7, T10 and verdict segment 5 publish "3/19 by distinct prefix and 1235/6008
by corpus multiplicity" as a measure contrast.  The distinct measure is taken
over the four declared corpora (703 nontrivial objects); the multiplicity
measure over the three primary ones (24,032).  Held at ONE family, I measure:

| universe | distinct-prefix | multiplicity |
|---|---|---|
| three primary corpora | **96/483 = 32/161 ≈ 0.1988** | 1235/6008 ≈ 0.2056 |
| four declared corpora | 111/703 = 3/19 ≈ 0.1579 | — |

The measure effect at fixed family is +3.4%; the family effect at fixed
measure is −20.6%.  The larger half of the published contrast is a change of
the counted family, not of the measure.  `G-E24-MEASURE` certifies only
`f_dist != f_mult`, so it passes on a difference it does not attribute.  The
receipt names the two universes
(`DISTINCT-PREFIX-OVER-THE-FOUR-DECLARED-CORPORA` /
`MULTIPLICITY-OVER-THE-THREE-PRIMARY-CORPORA`) — the paper never does.

**REPAIR (exact).** (a) Compute and publish `record_fraction_distinct_primary`
= Fraction(96, 483) and strengthen `G-E24-MEASURE` to require BOTH
`f_dist_primary != f_mult` (the like-for-like measure effect) and
`f_dist != f_dist_primary` (the family effect), so the two are separated
rather than summed.  (b) Carry the universe into the paper: T10's column
headers become "distinct prefix, four declared corpora" and "multiplicity,
three primary corpora", and segment 5 names them as the receipt does.

### MAJOR-3 — the paper-binding surface is ONE-WAY (four demonstrations)

Every paper gate asks "does the paper carry what the run computed?"; none asks
"did the run compute what the paper carries?"  `G-PAPER-TABLES` passes on
`not unrendered` alone and never compares `got_rows` with `want_rows` —
although it MEASURES both and prints the discrepancy.  Demonstrated:

1. **INJ19 — a forged table row.** A row `| 4 | 24 | 6 | 60 |` appended to T7
   (numerals chosen from the registry) passes at exit 0 while the gate's own
   evidence reads `required rows 69, paper rows 80, unrendered 0`.
2. **INJ23 — a forged contradicting sentence.** "the record's attribution is
   orbit-constant at 703 of 703 objects" — the direct negation of the measured
   111 of 703 — inserted beside the true claim, exit 0.  The five polarity
   probes are hand-written and do not cover it.
3. **INJ20/INJ14 — the instrument counts are unbound.** Swapping §9's numerals
   ("13 pinned sources, each naming the object it corrupts; 47 falsifiers
   whose bytes are digest-checked; 7 declared windows bound to consumer
   gates") — every predicate attached to the wrong noun — runs at exit 0 and
   emits a receipt **byte-identical to the committed one** (cd938d7ae9be).
   "Four reading walls" → "Eleven reading walls" likewise passes, because 11
   is in the registry as a crystallization time.  Measured exposure: of the
   544 scanned numerals, 106 occurrences sit outside every gated table row and
   verdict fence, and 68 of those use tokens no rendered claim carries.
4. **INJ06/INJ21 — the reading walls fall to paraphrase.** WALL-REALITY bans
   five literal forms; "The census therefore shows the actors are truly real
   threads, and that the nine are genuine individuals rather than a chart."
   contains none of them and passes at exit 0 with all four walls green over
   24,508 scanned characters.  WALL-SCOPE falls the same way ("true of every
   conceivable history … generalises to arbitrary corpora").

**REPAIR (exact).** (a) `G-PAPER-TABLES`: add
`len(got_rows) == len(want_rows) + len(R["paper_tables"])` (rows plus one
header per table) to the passing condition, and better, compare the MULTISET
of paper rows against the required multiset exactly as E-22 already does for
fences — the discrepancy is already computed, it is only unused.  (b) Render
§9's instrument sentence as `CLAIM-INSTRUMENT` from `R["totals"]`, so 13/47/
10/10/7 are bound to their nouns; bind spelled numerals the same way.
(c) The walls: their statements ("it does not assert that actors are real")
are stronger than a five-literal blacklist can enforce.  Either narrow the
statement to "no sentence carries one of the N banned forms", or make the wall
positive — every sentence containing "actor"/"actors" within k words of a
reality predicate (`real|exist|genuine|truly|individual`) must also carry the
description stamp — and add a NEAR-MISS mutant proving the wall fires on
paraphrase, not only on the exact banned string.

### MAJOR-4 — a phantom consumer gate, named twice in the receipt

`G-INVARIANCE-SPLIT` is not among the 52 gates and never runs.  It is named
as V03's `consumer_gate` (the pin quote "any non-invariance ⟹ the observable
NAMES threads the structure does not force") and as SEAL-INVARIANCE's
`sealed_at_gate` — the seal over the unit's entire deep half.  The seal IS
taken at value-close (line 1901, after G-CODIVISION-FORGETS) and
`Seal.close` re-verifies it, so the object is genuinely sealed; the published
provenance of that seal is false.  `G-COVERAGE` checks mutants for dead gate
names but nothing checks the anchors' or the seals'.  A second leg is missing
from E-23: `run_mutant` records `died_at` but never compares it with the
declared gate, and `G-SWEEP-BOUND`/`main` accept death anywhere — while
`G-REACHABILITY`'s published statement says the sweep "requires it to die at
the gate it names".  My outside-the-harness sweep found the exception:
**MUT-PAPER-FENCE-MULTISET is declared at G-PAPER-COVERAGE and dies at
G-PAPER-HEAD-VERBATIM** (the multiset flag is consumed by the earlier gate),
so G-PAPER-COVERAGE's mutant coverage is overstated by one.

**REPAIR (exact).** (a) Point V03 and SEAL-INVARIANCE at
`G-RECORD-ATTRIBUTION`, the gate that actually decides the split, or add the
missing gate.  (b) In the closing battery add to `G-COVERAGE`:
`phantom = sorted({v[3] for v in VERBATIM} | {s[2] for s in SEALED_PATHS}
- set(gate_names))` and require it empty.  (c) Carry the declared gate into
the sweep: `run_mutant` takes the declared gate, returns
`at_named_gate = (died == declared)`, and `G-SWEEP-BOUND` requires
`not [r for r in SWEEP_ROWS if not r["at_named_gate"]]`; then either re-declare
MUT-PAPER-FENCE-MULTISET at G-PAPER-HEAD-VERBATIM or move the multiset flag's
consumption to G-PAPER-COVERAGE.

### MAJOR-5 — the artifacts are promoted before they are verified, and four gate verdicts reach neither artifact

`finish` writes `tmp`, calls `os.replace` for BOTH artifacts, and only then
reads back and compares against the gate-time seal (lines 3313–3342).  A
failing `G-ARTIFACT-INTEGRITY` therefore leaves the corrupt bytes promoted —
the era's rule is that a failing run promotes nothing.  Separately, the
transcript is staged at line 3237, before the last four gates run: the file on
disk carries 175 lines and **G-TRANSCRIPT-INTEGRITY, G-GATE-ACCOUNTING,
G-SEAL-TOTALITY and G-ARTIFACT-INTEGRITY appear in neither artifact** — not in
the transcript (staged too early) and not in `R["gates"]` (snapshotted at line
3224, 48 rows).  Four of the fifty-two gate verdicts, including the two that
certify the artifacts, are published nowhere; the gate's own statement, "the
digest published is taken over ALL 175 transcript lines this run emitted", is
false — the run emits 191.

**REPAIR (exact).** (a) Hash the temp files and compare against `seal_j`/
`seal_t` BEFORE `os.replace`; keep the post-replace read-back as the second
leg.  (b) Move the staging past G-TRANSCRIPT-INTEGRITY, G-GATE-ACCOUNTING and
G-SEAL-TOTALITY (append their rows to `R["gates"]` and to `staged`), leaving
only G-ARTIFACT-INTEGRITY outside — it cannot be inside the file it certifies
— and say exactly that in the statement instead of "ALL … lines this run
emitted".

### MINOR

- **m-1 comparator independence overstated.** `independent_head` calls the
  builder's `stab_elements`, `born_rows`, `codivision` and `TRANSL`, and
  consumes the builder's `ordered`, `NTP` and `never` objects; 5 of its 13
  quantities (`distinct_prefixes`, `stabilizer_elements`,
  `walk_blind_depth1/2`, `walk_symmetries`, `complete_relation_histories`) are
  therefore not derived by a second route, against #82's "no shared code …
  comparators DERIVE".  All five reproduce under MY independent route, so no
  number moves.  *Repair:* re-derive the prefix set and a second stabilizer
  inside the comparator (the Young route is four lines), or narrow the gate
  statement to name which quantities are twice-derived.
- **m-2 a computed flag nobody consumes.** `constant_boolean_falsifier` is
  computed per mutant and published, but `G-FALSIFIER-HONEST` gates only
  `description_matches_code`.  (Measured: 0 of 47 are constant-boolean, so the
  hole is currently empty.)  *Repair:* add `and not r["constant_boolean_falsifier"]`
  to the `ebad` predicate.
- **m-3 a repeated flag is silently dropped.** `aid_exact.py --mutant A
  --mutant B` runs B and discards A at exit 0, though the parser's docstring
  says "there is no silent flag-ignoring anywhere in this file".  *Repair:*
  raise `CliError` when `opts["mutant"] is not None` on a second `--mutant`.
- **m-4 the bare copy aborts, but not through a gate.** With the pinned
  sources absent the run dies with an uncaught `FileNotFoundError` at
  `read_bytes`, exit 1, writing nothing — loud and compliant, but not a
  `[FAIL] G-PROVENANCE` line.  *Repair:* wrap the source read and re-raise as
  `GateFail("G-PROVENANCE :: pinned source absent: %s" % rel)`.
- **m-5 five seals name a gate that does not establish them.**
  SEAL-TRANSCRIPT, SEAL-GATES, SEAL-CLOSING and SEAL-TOTALS all declare
  `G-PAPER-COVERAGE-FINAL` while their values are established by
  G-TRANSCRIPT-INTEGRITY and G-GATE-ACCOUNTING respectively; SEAL-INVARIANCE
  names the phantom (M-4).  The other 24 of 29 are exact, and no seal is taken
  before its declared gate has run except the phantom.  *Repair:* re-point the
  four attributions.

## THE INJECTIONS (23 paper injections, off-tree, artifacts hashed each time)

| # | injection | expected | outcome |
|---|---|---|---|
| INJ01 | census table: two whole rows exchanged (row ORDER only) | pass | exit 0 — gate is row-order-blind, contents intact |
| INJ02 | census table: two corpus NAMES swapped, data held | die | **G-PAPER-TABLES** |
| INJ03 | crystallization table: C2/C3 labels swapped | die | **G-PAPER-TABLES** |
| INJ04 | invariance table: Born depth-1/depth-2 labels swapped | die | **G-PAPER-TABLES** |
| INJ05 | window table: W-C1 and W-C2 declarations swapped | die | **G-PAPER-TABLES** |
| INJ06 | reality overclaim, paraphrased past the banned forms | die | **exit 0 — M-3(4)** |
| INJ07 | §9 numerals cross-substituted (47→29 …) | die | G-PAPER-COVERAGE (unbacked "29" only) |
| INJ08 | never-crystallizing class labels ANT↔ROW | die | **G-PAPER-CLAIMS** |
| INJ09 | FORCED/CHART exchanged in prose | die | **G-PAPER-CLAIMS** |
| INJ10 | inline code span numeral corrupted (E-22) | die | **G-PAPER-COVERAGE** |
| INJ11 | one of the two verdict-fence copies forged (5,852→5,853) | die | **G-PAPER-HEAD-VERBATIM** |
| INJ12 | polarity: the opposite of a measured fate asserted | die | **G-PAPER-CLAIM-POLARITY** |
| INJ13 | one gated table row deleted | die | **G-PAPER-TABLES** |
| INJ14 | "Four reading walls" → "Eleven reading walls" | die | **exit 0 — M-3(3)** |
| INJ15 | a claim's number moved (111→112) | die | **G-PAPER-CLAIMS** |
| INJ16 | driven table: window labels swapped between rows | die | **G-PAPER-TABLES** |
| INJ17 | orbit-shape table: two shape labels swapped | die | **G-PAPER-TABLES** |
| INJ18 | E-24 stamp replaced by "with probability 3/19" | die | **G-WALLS-SCAN-THE-PAPER** |
| INJ19 | a forged EXTRA table row, registry-safe numerals | die | **exit 0 — M-3(1)** |
| INJ20 | §9 instrument numerals swapped (multiset invariant) | die | **exit 0, receipt byte-identical — M-3(3)** |
| INJ21 | scope overclaim, paraphrased | die | **exit 0 — M-3(4)** |
| INJ22 | a forged EXTRA fenced block | die | **G-PAPER-HEAD-VERBATIM** |
| INJ23 | a forged claim-shaped sentence contradicting a measured one | die | **exit 0 — M-3(2)** |

Sixteen of nineteen kill-injections died at a named gate with the artifacts
byte-unchanged; the five survivors are the demonstrations of M-3.

## THE DISEASE SWEEP

| # | disease | verdict | demonstration |
|---|---|---|---|
| 1 | referent-binding of the census names | **PARTIAL** | C1/C2/C3, class labels, window names and FORCED/CHART are bound wherever a claim or a gated table row carries them (INJ02–05, 08, 09, 16, 17 all die); they are NOT bound in §9's instrument sentence (INJ20) nor across the two numerals of CLAIM-PREFIXES (M-1) |
| 2 | phantom consumers | **PRESENT** | G-INVARIANCE-SPLIT named by V03 and SEAL-INVARIANCE, absent from all 52 gates (M-4); the other 9 anchors and 28 seals resolve |
| 3 | constant-boolean / E-23 three-legged falsifiers | **PARTIAL** | 0 of 47 constant-boolean; 47/47 descriptions match their AST-located hook; the third leg (dies at the DECLARED gate) is ungated and 1 of 47 fails it (M-4) |
| 4 | seal windows at value-close; read-back before replace | **PARTIAL** | 28 of 29 seals taken after their declared gate; `Seal.close` re-verifies all; read-back happens AFTER `os.replace` (M-5) |
| 5 | E-22 (fences by multiset, all tables, inline spans, digest-free whitelist, spelled numerals) | **MOSTLY ABSENT** | 10 fences = 5 segments × 2, multiset gated (INJ11, INJ22 die); 10 tables / 69 rows all render, but one-way (M-3); 4 inline-span numerals scanned and gated (INJ10 dies); registry 167 tokens, digest-free; 61 spelled numerals scanned but unbound (INJ14) |
| 6 | #267 checklist | **PARTIAL** | walls scan the paper's 24,508 characters but fall to paraphrase (M-3(4)); no typed counts (probes 52/47/29/69 all absent as literals — the AST scan is clean and "29"/"52" are not even in the registry); full-transcript integrity incomplete (M-5) |
| 7 | two-route agreement's independence | **ABSENT** | Route A filters S₉ by mask recursion, Route B builds the Young subgroup from participation signatures; no shared intermediate, no shared literal; agreement at order on all 41,347 and at element set on all 703 reproduced independently by me (my own third route, inside Stab(F₁)) |
| 8 | window declarations | **ABSENT** | 7 windows declared in-string; W-C1/C1FAN/C2/C3 are entire classes; W-DRIVE's 9+6+2 = 17 rows match T9 exactly; W-AUTC2's 72 diagonal concatenations match the code; W-WALK publishes all 5 depths |
| 9 | E-24 | **PRESENT** | COUNTING-ONLY stamped and both fractions published, but the pair is confounded with a family switch and the paper never names the universes (M-2) |
| 10 | the 47-falsifier sweep outside the harness | **ABSENT** | 47/47 died, exit 0, each in its own fresh tree, tree hash byte-identical before and after under my hasher; 46/47 at the declared gate (M-4) |
| 11 | CLI + selftest | **ABSENT** | 19 hostile argv vectors: unknown flags, `-h`, `--help`, missing `--mutant` arity, `--mutant=NOPE`, trailing junk, `--` → all exit 2 with the tree unchanged; `--selftest` dies at G-PROVENANCE, tree byte-identical under my own hash (m-3 is the only nit) |
| 12 | byte ×2 off-tree | **ABSENT** | `PYTHONHASHSEED` 0 and 987654, two provisioned trees holding only the 13 pinned sources and the paper, no `.git` anywhere: receipt cd938d7ae9be, transcript 48fe931bfcdc, identical to the committed artifacts both times.  Bare copy aborts loudly and writes nothing (m-4) |
| 13 | the 544-numeral sweep | **ABSENT** | independently retokenised: 544 numerals (89 distinct) and 61 spelled numerals, matching the receipt exactly; `scan_is_total` binds 544 == 544 against a reference taken over the untouched text, and MUT-COVERAGE-SCAN dies on it — the worker's self-caught fix is real |

## THE #267 CHECKLIST, COMPLIANCE

| item | required | delivered |
|---|---|---|
| the walls scan the paper's characters | yes | yes — 4 walls × 24,508 characters, gated; but literal-form only (M-3(4)) |
| all tables rendered | yes | yes — 10 tables, 69 rows, cell by cell; one-way (M-3(1)) |
| no typed counts | yes | yes — AST scan of `verdict_segments`, `paper_claims`, `paper_tables`, 0 typed literals; probes 52/47/29/69 clean |
| full-transcript integrity | yes | partial — sealed whole as STAGED, but the staged object is a prefix of the run (M-5) |
| digest-free whitelists | yes | yes — 167 tokens, `registry_digest_free` true, MUT-DIGEST-WHITELIST dies |
| spelled numerals | yes | yes — 61 scanned, word list of 22 entries; scanned but not referent-bound (M-3(3)) |

## WHAT I COULD NOT BREAK

The physics.  Every headline of the head reproduces under an independent
route: 5,852/5,856 forced with the four chart histories at order 216 and orbit
shape 3+3+3; crystallization exactly 5 on C1, C2 and the 1,944-history fan;
the C3 strata 404/36/144/12/never-4 with the four constant-class quadruples
named correctly; the profile (4320, 216, 216, 8, 1, 1) at all 72 and all
5,184, with events four and five transversals of the first round; 0 prefix-law
disagreements and 0 growth events; 0 co-division violations over 121,152
elements at 703 objects; the record blind at 111 and naming-dependent at 592;
the Born menu at 134, 58, 58, 58, 58; the cross-tab 569/23/53/58; 813 walk
symmetries and 51,769 record-preserving elements; 24 complete-relation
histories all with trivial stabilizer, and |Aut| = 1,296 at every R = 3
history and every diagonal R = 6 concatenation; the full stabilizer/
automorphism pair table (12 rows summing to 703); all four E-24 fractions.
Sixty-eight for sixty-eight, no number moved.
