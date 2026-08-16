# REC (paper-41) — K1 OPERATOR REVIEW

*Three-seat hostile panel, OPERATOR seat. Object read and re-read at pinned
digests: `v14/paper-41-rec.md` 58b08940d04c (360 lines), `v14/code/rec_exact.py`
ba77c08c81a2 (2,703), `v14/code/rec_output.txt` 16b7a64c6156 (39),
`v14/code/rec_receipt.json` 2428d901e5c5 (1,162), pin `v14/note-rec-pin.md`
0b51e47b7b4b (5). All five verified at open AND at close, unchanged. Authority:
HANDOFF-PROMPT.md §4/§9, RUNBOOK through E-33, the pin, ledger #376; parents
FAC/EPR/AID read at HEAD. Sole repo write: this file. Git read-only. Scratch:
`.../scratchpad/rec_k1/`, 3.2M. In-flight HOR reviews not read.*

**Between delivery and adjudication every headline below — the unit's and mine —
is a candidate reading.**

---

## GRADE: ACCEPT-WITH-FIXES

The measured content stands. I rebuilt the unit from the declared spec in the
parents (AID §2, FAC §1, EPR §1) with no code shared with `rec_exact.py` — my
own site indexing, my own cell ordering, my own token scramble, my own
Bron–Kerbosch, my own transfer count — and reconciled **162 delivered leaves**.
**161 match. One does not.** The three verdict blocks are confirmed:
`CAST-DERIVED-UP-TO-THE-DIRECTION-DECLARATION` is what these bytes say.

What fails is not the arithmetic. It is (a) two general claims in the prose that
the unit's own corpus falsifies, (b) one published number that does not measure
what its name says, (c) an undisclosed cap in a control arm, and (d) four gate
mechanisms that do not bite as §8 describes them. All are liftable without
re-running the physics.

---

## 1. WHAT I REPRODUCED, FROM SCRATCH

| leg | my route | delivered | verdict |
|---|---|---|---|
| arena | AG(2,3), 4 classes, 3 declared, 27 cells, 6/actor | 9/4/3/27/27/[6] | MATCH |
| combinatorics | 280 groupings, 36 saturating, 72 I7-STRICT, 276 G-FLAT, 600 W4 | same | MATCH |
| corpus | 72 + 5,184 + 600 = 5,856 slots, 5,784 distinct (C3: 528), 101,160 events | same | MATCH |
| stripping | 100,392 written, 768 unwritten, 27 blocks all of size 3 | same | MATCH |
| **the rule** | meets {0,1,3} → τ=3; maximal cliques 27×3 and 9×6 | same | MATCH |
| **set equality** | derived cast = declared stars, **as sets**, in token coords | True | MATCH |
| links | 27 tokens each in exactly 2 actors; 27 pairs; degrees [6]; 3 parts of 3 | same | MATCH |
| menu | 3 of 6 (ANT/DISCRETE/TRIVIAL in; ROW/COL/DIA out), 0 stray | same | MATCH |
| naming | 1,296 / 108 / index 12; Aut = 108; 36 candidates; 12 resolutions | same | MATCH |
| level 0 | 36 distinct fields, 36 site rows, site-constant 5,856/5,856, max 4 | same | MATCH |
| obstruction | 768 / 175 / 1, silent history 12 events, 1 undeclared class | same | MATCH |
| minimality | 0 of 5,856 at every prefix; 17 histories/145 events/27 blocks; one-earlier False; drop-one 0 of 27 | same | MATCH |
| surplus | 5,784 → 5,643, lost 141, 39 classes / 180 histories, largest fiber 6; 1/4/4 | same | MATCH |
| **AID's time** | C1:5→72, C2:5→5,184, C3: 5→404, 7→36, 8→144, 11→12, never→4 | same | MATCH |
| **FAC's w\*** | C1:4→72, C2:4→5,184, C3: 3→4, 4→521, 5→75 | same | MATCH |
| connection | 8 joint rows, 5,856 total, record side 0 | same | MATCH |
| synthetic | all 7 arms: parts/tokens/blocks/**certificate string**/cast_size/recovered | same | MATCH |
| equivariance | 12 declared relabellings, 0 failures | same | MATCH |

Both parent thresholds independently reproduce, and they reproduce against the
**parents' own published values**, not only against REC's receipt: FAC §5 states
"3 at 4 of the 600 schedules, 4 at 521 of them and 5 at 75" — my transfer count
returns exactly that; AID §5 states crystallization 5 on C1 and C2 — my
signature scan returns exactly that. The 24-quantity `G-PARENTS-AGREE` leg is
sound at the two quantities that matter most.

The **hardest** claim in the paper — that the first three rows of §2 are *set
equality, not isomorphism* — is true, and it is not circular. The eraser's
bijection is a fixed declared affine map on token indices, chosen before any
reconstruction; the comparator only transports the declared cast through it. I
re-ran the reconstructor under my own unrelated scramble and got the same
answer, then under **200 further random relabellings** beyond the declared 12,
with 0 failures. The token-coordinate disclosure is priced.

I also **strengthened two control legs**, both confirming the delivered result:

- **Scrambles.** Against the delivered 261 I ran my own exhaustive family:
  27 drops + **78,246** alien-block replacements (every block against every one
  of the 2,898 alien 3-subsets) + **2,754** moving cross-block token swaps
  (all 351 block pairs) = **81,027 corruptions, 0 survivors**, 405 rejected as
  non-moving and reported as such. Further: **every one of the 78,246 replacements
  returns `TOKEN-IN-NO-ACTOR`** — the reconstructor never issued a certificate on
  a corrupted record at all, which is stronger than "none reached the declared cast."
- **Synthetic domain.** Against the delivered 7 arms I swept **113** balanced and
  unbalanced complete-multipartite shapes (2–5 parts, part sizes 2–6, ≤16
  actors). **Zero certified a wrong cast.** §6's line 290–291 —
  "no certificate was ever issued for a cast that was not that record's own" —
  survives a domain 16× wider than the one it was measured on.

**Recomputations: 162 delivered leaves re-derived leaf-by-leaf (161 match, 1
mismatch), plus 81,027 scramble runs, 212 equivariance trials, 113 synthetic
arenas, 351 25-block subsets and 27 26-block subsets, and a 5,856-history
overlap census.**

---

## 2. MAJORS

### MAJ-1 — §7's mechanism claim is falsified by this unit's own corpus, at 5,016 of 5,856 histories

Line 325–326: *"so shortness alone is not the obstruction — disjointness is."*
Line 219–224 supplies the same story as *"the reason"* the reconstruction depth
is unreached.

Measured, per history, the number of pairs of its distinct record blocks that
intersect:

| corpus | 0 overlapping pairs | >0 overlapping pairs |
|---|---|---|
| C1 | 72 | 0 |
| C2 | 432 | 4,752 (18 pairs ×3,888; 27 pairs ×864) |
| C3 | 336 | 264 (6 pairs ×216; 9 pairs ×48) |
| **total** | **840** | **5,016** |

**5,016 of 5,856 histories have overlapping record blocks and still refuse.**
For them the rule is not starved of a meet — it gets one, and the meet is
*wrong*:

```
C2, 18 overlapping pairs, 15 blocks : meets [0,1,2] tau=2 cliques 15x3+6x4 cast 6  -> TOKEN-IN-NO-ACTOR
C2, 27 overlapping pairs, 18 blocks : meets [0,1]   tau=1 cliques 36x3+27x5 cast 27 -> TOKEN-NOT-IN-EXACTLY-TWO
C3,  9 overlapping pairs, 12 blocks : meets [0,1]   tau=1                   cast 9  -> TOKEN-NOT-IN-EXACTLY-TWO
```

The disjointness story is correct **for C1 and nowhere else** — 72 of 5,856,
1.2% of the census the sentence generalises over. §4's paragraph is scoped
("A history in the first corpus…") and is true as written; §7's sentence drops
the scope and is false.

The **true** mechanism is measurable and I measured it: no committed history
ever sees all 27 record blocks (the maximum over the corpus is **18**), and the
full block set is irredundant in a stronger sense than drop-one shows —
**0 of the 27 26-block subsets and 0 of the 351 25-block subsets reconstruct.**
Below the complete block set the derived threshold is wrong (τ ∈ {0,1,2}
instead of 3) and the certificate refuses.

**Repair (exact).** Replace line 325–326 with: *"so shortness alone is not the
obstruction: no committed history sees all 27 record blocks — the most any sees
is 18 — and the block set is irredundant at 26 and at 25, so below the whole
set the derived threshold is wrong and the certificate refuses. Disjointness is
the mechanism at C1 only, where it accounts for 72 of the 5,856 refusals."*
And in §4 line 219, scope "the reason" to the first corpus.

### MAJ-2 — §6's domain boundary is the wrong boundary

Line 287–289: *"outside the balanced three-part family the reconstructor
REFUSES rather than answering wrongly."*

Over my 113-shape sweep, four shapes **outside** the balanced three-part family
recover the cast exactly, with the reconstructor's own certificate:

| parts | recovered |
|---|---|
| 3+3+3+3 | yes |
| 4+4+4+4 | yes |
| 2+2+2+2+2 | yes |
| 3+3+3+3+3 | yes |

The delivered negative arm 2+2+2+2 is not evidence about part *count*: it is the
one balanced 4-part shape small enough to break, and its 5-part analogue
2+2+2+2+2 recovers. The measured boundary is **balance**, not three-ness, and it
is not monotone in the number of parts. §7's hedge ("a domain probe, not a
classification") mitigates but does not cover a sentence phrased as a
classification.

**Repair.** Line 287–289 → *"outside the balanced family the reconstructor
REFUSES rather than answering wrongly, and the certificate says which leg
failed; balance and not the number of parts is what the arms locate — the
2+2+2+2 arm breaks where its 5-part analogue does not."* If a stronger sentence
is wanted, the sweep is cheap: 113 shapes, zero certified-but-wrong.

### MAJ-3 — the published value for THE-EVENT-SET-ITSELF does not measure an event set

§3 table line 180 publishes `THE-EVENT-SET-ITSELF | NOT-CARRIED | 136`.
`rec_exact.py:1409-1411`:

```python
def prop_eventset(i):
    return tuple(sorted(tuple(sorted(SITE_INDEX[x] for x in F))
                        for F in corp[i][1]))
```

That is the sorted event **multiset** — duplicates retained. Events do repeat
(C2 diagonals repeat all nine; W4-CLASS quadruples repeat classes). Measured
both ways over the 5,784 distinct histories:

- sorted event **multiset**: **136** distinct values ← the delivered number
- the event **set** (`frozenset(H)`): **103** distinct values

The row's name is "THE-EVENT-SET-ITSELF" and the column header is "values". A
reader is told the event set takes 136 values; it takes 103. The **verdict is
unaffected** — NOT-CARRIED with 6 splitting fibers under either reading, which
I confirmed — so the 1/4/4 headline stands.

**Repair.** Either rename the row to `THE-EVENT-MULTISET` (receipt key and
paper together) and keep 136, or take the set and publish 103. The verdict word
and the split count do not move either way. This is the single mismatch in 162
leaves and it is a naming defect, not a computation defect — but it is a
published number that is wrong for its stated referent, and the campaign's
standing claim is zero false numbers.

### MAJ-4 — the SWAP control arm is silently capped

`rec_exact.py:1817-1819`:

```python
for u, v in combinations(range(len(base)), 2):
    if u > 8:
        break
```

`combinations` runs lexicographically in `u`, so the loop visits **198 of the
351** block pairs (56.4%) and stops. Candidate/counted arithmetic: 54 REPLACE +
27 DROP + 198 SWAP = **279 candidates → 261 counted**, so **18 are dropped by
the moving-filter and no receipt leaf records them**. The paper says "261
corruptions of these bytes were run" and "Each was required to move the object
before it counted" — the first reads as a census, the second names a filter
whose denominator is not published.

Two standing disciplines are hit: HANDOFF §4 "No silent caps", and #34 honest
denominators.

**Result unaffected**: my uncapped, exhaustive SWAP arm is 2,754 moving
corruptions over all 351 pairs, 0 survivors.

**Repair.** Delete the `if u > 8: break` (my full run costs seconds), and add
`"candidates"` and `"rejected_as_non_moving"` leaves to `control_scrambled`
beside `trials`. Also worth noting: the REPLACE arm's aliens are only the two
token-index translates `{(t+1)%27}` and `{(t+2)%27}` of each block — 2 of 2,898
possible aliens. My exhaustive 78,246 closes that arm; a one-line note in §6
that the alien family is a declared two-member family would be honest as
delivered.

### MAJ-5 — G-PAPER-COVERAGE is value-membership, not value-at-place

`harvest` (2183–2198) flattens the whole receipt into one integer set, including
digits scraped out of strings with `re.findall(r"\d+", o)` — so sha256-12 hex
digits pollute the backing set. The test (2206–2207) is
`int(n) not in backing`. Consequence, **demonstrated by direct experiment**: the
two numerals in §5 were swapped to read "There are **175** such events in the
corpus; **768** histories carry at least one" — flatly wrong, and contradicted
by the fence on line 25 of the same paper — and the full run returned
`[PASS] G-PAPER-COVERAGE :: numerals 144 unbacked none` with **37 gates green,
exit 0**. Both values sit in the same referent universe, so G-PAPER-REFERENTS
cannot separate them either.

The gate detects an *unfamiliar* number, never a *wrong* one. §8's sentence
"no typed numeral in anything the unit vouches for" is true; the coverage claim
that a reader will infer from it is not.

**Repair.** Bind numerals per-occurrence to the receipt path their sentence
names (the §3/§4/§6 tables already are, by `G-PAPER-CLAIMS` two-way keyed
equality — extend that discipline to prose), and drop string-scraped digits
from the backing set.

### MAJ-6 — the S-1 disjointness scan covers 43 of 78 functions and is one level deep

§8: *"an AST scan requires that no reconstructor function name an arena constant
or call a builder or comparator function… That is this corpus's registered S-1
family, answered here with a mechanism rather than a promise."*

`audit_regions` (886–912) assigns regions by **name prefix** and `else: continue`
(897–902); the arena ban list is a **hard-coded 15-name set** (892–894, one entry
`ACTORS` never defined). Census: builder 24, comparator 6, reconstructor 9,
stripper 4 = **43**; the file holds 57 top-level function definitions and 78
total, so **35 are in no region — including `full_run`**, the orchestrator that
holds the declared arena and the bare record at once. No transitive call
following. Escapes that return `violations=0` against the real predicate:
`globals()['CELLS']`; `getattr(sys.modules[__name__],'CELLS')`; an aliased
constant; a closure; a lambda bound to an `r_` name; and — most directly —
**passing the arena in as an argument**, `r_reconstruct(blocks, CELLS, CLASS_DIR)`,
clean because `CELLS` is named in unregioned `full_run`. Renaming
`r_derived_menu` → `derived_menu` moves the census 9 → 8 with no violation and
nothing pins 9. The direction-declaration globals `B_COMMITTED_R4`,
`B_COLLINEAR_FLAT`, `B_SEEDS_PER_ROUND` (217–219) — the paper's own named
obstruction — are not in the ban list.

I want to be fair about what this does and does not mean. The instrument's
blindness claim is **not actually carried by the AST scan**; it is carried by
`G-STRIPPING-TOTAL` (the depth-3 type walk, which the author's own falsifier
history shows was hardened for exactly the right reason),
`G-STRIPPING-EQUIVARIANT`, and the control arms — all of which I independently
confirmed. The finding is that §8 credits the wrong mechanism.

**Repair.** Either (i) make the region map total — every top-level def must be
declared into a region, unassigned is a violation — and follow calls
transitively, or (ii) rewrite §8 to say what is actually true: *"the reconstructor
is a prefix-declared region whose bodies are scanned for named arena constants
and cross-region calls; the blindness itself is carried by the type walk, the
equivariance leg and the control arms."* Option (ii) costs nothing and is
accurate.

### MAJ-7 — the one waiver's "machine-checked forcing" is a literal `True`

`rec_exact.py:2401-2404` passes `{"T-FALSIFIER-COVERAGE": True}` as the forcings
map; `era_template.py:934` accepts any truthy value. HANDOFF §4 #34: "waivers
only as machine-checked forcings." Nothing computes this one.

**Repair.** Compute the forcing (the gate is self-referential, so the forcing is
a short argument that a coverage gate cannot be its own falsifier's target) or
drop the waiver and let the count read 36 of 37.

### MAJ-8 — three falsifiers are constant-append sentinels; the anti-sentinel leg exists and is never called

`era_template.py:901-921` defines `audit_descriptions` for exactly this class.
`rec_exact.py` never calls it — only `.coverage`. Run against the source it
returns three hits: line 1006, 2209, 2284 — `drifted.append("injected")`,
`cov.append("injected")` (**MUT-COVERAGE**), `bad_types.append("/injected")`
(**MUT-FLOAT**). These append to the offender list *after* the detector has run,
so the typewalk and the backing test are never exercised; the mutants die at
their named gate without moving the measurement the gate reads.
**MUT-TYPED** (2251–2252) is the same shape. That is E-32 — "a falsifier moves
the measurement or it is not a falsifier" — unmet at 3–4 of 38. Relatedly,
`falsified: 37` (era_template.py:939) is `len(targeted)`, a count of gate names
**declared** in MUTANTS, not of gates whose measurement was moved:
`T-SEAL-PROMOTION` is targeted but is never a ledger row, and
`T-FALSIFIER-COVERAGE` fires but is waived, so the two 37s conceal a swap.

**Repair.** Wire `audit_descriptions` into the run (it already refuses these
three), and rewrite the recipes to plant the real defect — an unbacked numeral
for MUT-COVERAGE, a float leaf for MUT-FLOAT — rather than to append to the
finding list.

### MAJ-9 — "both are finite and small" is contradicted by the unit's own NEVER-CRYSTALLIZING=4

Line 67–68: *"AID's naming time is a prefix fact about one history and FAC's
coherence width is a window fact about one; both are finite and small."* This is
the setup for the paper's self-declared sharpest contrast. Measured here
independently: **4 histories never crystallize** (the constant-class quadruples;
receipt `crystallization.never = 4`, `connection.rows[0].crystallization = -1`).
The §4 table renders the C3 crystallization column as `stratified` while
rendering the C3 collapse-threshold column explicitly as "3, 4, 5" — the one
column whose expansion contains a *never* is the one compressed. The datum **is**
disclosed, but only inside the verdict fence at line 21, never in prose or in a
table; the parent AID discloses it in its own headline.

**Repair.** Line 67–68 → *"…both are finite and small wherever they are defined,
and AID's time is undefined at four of the 5,856."* §4 table C3 cell for
crystallization → `5:404, 7:36, 8:144, 11:12, never:4`.

---

## 3. MINORS

- **MIN-1 — the rule as stated in §2 is not the rule as implemented.** §2's rule
  has no refusal clause. `r_sharing` (492–509) returns `None` → `NO-MEET-GAP`
  when `len(meets) < 2`. §4 describes the behaviour ("the rule has no meet to
  threshold and refuses") but §2's statement of the rule omits it. I checked
  that the omission is harmless here: implementing §2 literally (τ = max even
  with one meet value) still returns 0 of 5,856 at every prefix, because the
  degenerate case then fails `TOKEN-NOT-IN-EXACTLY-TWO` instead. No headline
  moves. Add the clause to §2.
- **MIN-2 — "in the order it wrote them" (line 83) is not what the
  reconstructor reads.** `r_reconstruct` (528) does
  `sorted({tuple(sorted(b)) ...})`: the reconstruction consumes the **set of
  distinct blocks**, discarding both order and multiplicity. Order matters for
  the fibers in §3 and nowhere else. The sentence over-credits the record.
- **MIN-3 — line 312, `record-completeness is analytic at EPR's own catalogue`,
  is typeset as a parent quotation and is REC's own sentence.** It is not in
  paper-38-epr.md and not in note-epr-adjudication.md (which says
  "RECORD-COMPLETE is true-by-construction at the record's own catalogue"). The
  other six anchored quotations in the paper are verbatim and I confirmed all
  six (FAC carrier row at fac:95-97; both EPR strings at epr:89-92; both AID
  strings; FAC's width string at fac:78-80 — none is a disguised paraphrase).
  This one sits among them, in the paragraph about parent scope, in identical
  typography. Unbackticked or attributed to this unit.
- **MIN-4 — "the seed fan" is quoted and not re-measured.** Line 211-213
  presents `the crystallization time is exactly 5 on C1, C2 and the seed fan` as
  what *"measured that way"* returns here. AID's seed fan is a separate
  1,944-history corpus; it is not in this unit's 5,856 and there is no seed leaf
  in the receipt. Trim the quotation to C1 and C2 or say the third conjunct is
  AID's.
- **MIN-5 — §8 says "three regions"; the census publishes four.** `disjoint_code.regions`
  = builder 24, comparator 6, reconstructor 9, **stripper 4**. The stripper is
  the erasure component and is unconstrained by S-1 by design (it names `DIM`,
  `SCRAMBLE_MULT`, `SCRAMBLE_ADD`) — which is right, and which the paper does
  not say.
- **MIN-6 — G-VERDICT-EQUALITY reparses 12 of the 38 numerals in the three
  fences.** `k_parse_head` takes only the **first** numeral of each named field.
  Reparsed: 5,856 / 5,784 / 27 / 9 / 1,296 / 12 / 0 / 17 / 4 / 768 / 175 / 1.
  Not reparsed: `SITE-SET` 9,9; `LINK-STRUCTURE` 27,27; `MENU` 3,6; `NAMING`'s
  **108**; `LEVEL-0` 36; `CORPUS-ORDER`'s 145; `BLOCK-MINIMAL` 27,27,0;
  `COLLAPSE-THRESHOLDS` 3,4,5; `CRYSTALLIZATION` 5; `RECORD-COLLISIONS` 39,180;
  `SURPLUS` 1,4,4; `CONTROLS` 261,0,4,7. They remain bound to the renderer by
  fence multiset equality; §8's "each declared head field" is literally true and
  does not disclose the scope.
- **MIN-7 — one datum, two names in one verdict block.** The outcome word is
  `...UP-TO-THE-DIRECTION-DECLARATION`; the field inside reads
  `OBSTRUCTION=THE-LINK-DECLARATION`; §5 says "the direction declaration". Pick one.
- **MIN-8 — line 280 omits the cast_size column.** For 2+2+2+2 the reconstructor
  derived a cast of **24**; for 2+3+4, **8**. The reader's only inference route
  (cast = sum of parts) is wrong on 2 of the 7 rows. Adding the column costs a
  column and kills the wrong inference.
- **MIN-9 — `rec_output.txt:38` prints `rows 35 chain b37ae3b6b2b7e940`** while
  the receipt carries `gate_rows 37`, `chain_head 5a331a7442cc550a`. The output
  line is a mid-run snapshot; the receipt is correct against the artifact. Cosmetic.
- **MIN-10 — §3 column header "values".** In §3 the numbers 5 and 3 are *counts
  of distinct values*, and 24 lines later 5 and 3 are the crystallization time and
  the collapse threshold themselves. Header → "distinct values".

---

## 4. WHAT BITES, AND SHOULD BE SAID SO

Against the majors above, these legs are real and I confirmed them independently:

- **The seal is total** — 37 sealed + 0 declared-unsealed + the manifest = 38 =
  every published key; integrity is disk-vs-gate-time-digest, never
  re-derivation; all 37 seal digests recompute against the on-disk receipt with
  0 mismatches; all 4 provenance digests and all 8 pinned sources match current
  repo bytes.
- **The artifacts are byte-reproducible.** Run off-tree in a scratch mirror,
  `--run` regenerates `rec_output.txt` (16b7a64c6156) and `rec_receipt.json`
  (2428d901e5c5) byte-identically. `--selftest` writes nothing. `--mutant NOPE`
  and a bad argument both exit 2. All 38 mutants die at their declared gate with
  artifacts unchanged. (Note for the orchestrator: `--run` writes into the repo
  by absolute path, so a reviewer must mirror before running.)
- **`ReadSet` is a genuine `sys.addaudithook` on `open`**, compared both
  directions with unused-exemption detection — E-33 met in substance.
- **The blindness itself is sound.** The depth-3 type walk, the equivariance leg
  and the control arms carry it, and my 212 relabellings and 81,027 corruptions
  agree with every one of them.

---

## 5. LICENSED REPLACEMENTS

Offered as measured, liftable text. All numbers below are mine, recomputed.

1. **§7 line 325–326** → *"so shortness alone is not the obstruction: no
   committed history sees all 27 record blocks — the most any sees is 18 — and
   the block set is irredundant at 26 and at 25 blocks alike, so below the whole
   set the derived threshold is wrong and the certificate refuses. Disjointness
   is the mechanism at the first corpus only: 5,016 of the 5,856 histories carry
   overlapping record blocks and refuse anyway."*
   (Establishing measurements: max distinct blocks per history 18; 26-of-27
   survivors 0 of 27; 25-of-27 survivors 0 of 351; overlap census 840 / 5,016.)
2. **§6 line 287–289** → *"outside the balanced family the reconstructor REFUSES
   rather than answering wrongly, and the certificate says which leg failed;
   what the arms locate is balance and not the number of parts."*
   (Establishing measurement: 3+3+3+3, 4+4+4+4, 2+2+2+2+2, 3+3+3+3+3 all recover;
   113 shapes swept, 0 certified-but-wrong.)
3. **§3 table row 5** → rename to `THE-EVENT-MULTISET` (paper and receipt key
   together), or recompute as a set and publish **103**. Verdict and split count
   are invariant under the choice.
4. **§0 line 67–68** → *"…both are finite and small wherever they are defined,
   and AID's is undefined at four of the 5,856."* §4 table C3 crystallization
   cell → `5:404, 7:36, 8:144, 11:12, never:4`.
5. **A finding this unit measured and did not state.** The four histories that
   never crystallize are **exactly** the four whose collapse threshold is 3 —
   a biconditional at 4 of 4 in both directions over 5,856 slots. It is visible
   in `connection.rows[0]` and is nowhere claimed. If §4's business is the
   relation between the two parent depths, this is the one exact relation
   between them that the corpus carries, and it is free.
6. **A second free strengthening.** The paper says of the residue index that
   "The quotient is an integer, and it counts something." The reason it counts
   that thing is that the 1,296 admissible namings act **transitively** on the
   12 resolutions — the orbit of the declared splitting has size 1,296/108 = 12,
   which is all of them. That is why index = count rather than a coincidence,
   and both numbers are already in the receipt.
7. **Control-arm repairs** (MAJ-4): delete `if u > 8: break`; publish
   `candidates` and `rejected_as_non_moving` beside `trials`.
8. **§8 rewrite** (MAJ-6): credit the type walk, the equivariance leg and the
   control arms with the blindness, and describe the AST scan as the
   prefix-declared region check that it is — or make the region map total.

---

## 6. SCOPE OF THIS SEAT

I verified the measured content, the paper's claims against the receipt, the
control arms, and the gate mechanisms named in §8. I did not adjudicate the
pin's outcome menu beyond confirming that
`REC-CAST-DERIVED-UP-TO-<the residue>` is a declared outcome and that
`THE-DIRECTION-DECLARATION` is a named residue. I did not read the in-flight HOR
reviews. I made no repo write but this file.

**Every headline in this review is a candidate reading until adjudication.**

*Object re-verified at close, unchanged: paper-41-rec.md 58b08940d04c,
rec_exact.py ba77c08c81a2, rec_output.txt 16b7a64c6156, rec_receipt.json
2428d901e5c5, note-rec-pin.md 0b51e47b7b4b.*
