# D43d (N4) — round 1 hostile review: the canonical-D* instrument on the generated families

**Object:** `v10/code/d43d_dstar_generated_exact.py` + `v10/data/d43d_dstar_generated_exact.out`
(4/4 PASS), pin `v10/note-d43d-dstar-on-generated-families.md` (#329), LOG #333. HEAD 96ca550.
**Standard:** receipt review — port fidelity checked against the COMMITTED v8 code
(`v8/code/{g2_dimension2_gate,i1_canonical_realizer,i2_characterization,j1_two_clock_sweep}.py`),
not against the extraction record's pseudocode; the six chain posets recomputed from the
committed d42b1 layer and re-scored with the v8 originals digit-for-digit; the NG3 dimension
verdict stress-tested against the full enumerated families AND against new constructed
histories admissibility-checked by the committed `admissible()`/`candidates_for()`; NG2's
descriptor lines parsed against their own labels; plumbing (determinism, exit-1 mutation,
caps, dead code).
**Review instruments** (session scratchpad, reproducible): `scriptA_fidelity.py` (v8-vs-port
diff harness), `scriptB_ng2.py` (NG2 forensics), `scriptC_witness.py` (the witness + width
audit), `scriptD_sweeps.py` (enumerated-family sweep + the skipped n=5 anchor),
`scriptE2_wiresearch.py` (wire-count thresholds), three mutation copies (`mut1..3.py`).

**Verdict: 0 BLOCKER / 4 MAJOR / 3 minor / 2 nit. The PORT is clean — every ported
function agrees with the committed v8 code on every tested object, digit-for-digit, and
every number in the `.out` is verified true. The MAJORs are one level up: the round's
pre-registered question ("does transport generate dimension?") is answered WRONGLY at
grammar scope — this review constructs 6-event admissible transport histories whose
event posets FAIL dim ≤ 2 under the committed oracle: W6 (6 actors, poset exactly S3)
and W4 (4 actors — CH's own actor count — a non-S3 3-irreducible); 6 events is the
theoretical minimum. Five of the six chains were structurally incapable of failing
(width ≤ 2), so 0/6 was five-sixths pre-decided. Plus one wrong-under-its-own-label NG2
descriptor and one LOG row recording an anchor the receipt never ran.**

---

## 1. MAJOR findings

### F1 — MAJOR (CONFIRMED, constructive): transport DOES generate dimension — a 6-event
### admissible witness with event poset exactly S3; the round's headline inverts at
### grammar scope

LOG #333's header: "TRANSPORT DOES NOT GENERATE DIMENSION at chain scale"; the receipt's
NG3 outcome line offers the dichotomy "TRANSPORT GENERATES DIMENSION at chain scale" vs
"every constructed chain is a TWO-CLOCK configuration (paper 13 universality holds at
chain scale)" and prints the second. The pin (§1) poses the question at grammar scope:
"are the generated record orders two-dimensional (= two-clock configurations, paper 13)
or does transport generate dimension? Either answer is a result."

The general answer is the FIRST disjunct, and it is available at the smallest possible
size. Take actors `('A','B','C','D','E','F')` and the pure-transport history of six
deliveries of the genesis version:

```python
W6 = [('d','C','E',V0),   # a0
      ('d','A','F',V0),   # a1
      ('d','B','D',V0),   # a2
      ('d','A','B',V0),   # b0: joins A(last=a1) + B(last=a2)
      ('d','C','D',V0),   # b1: joins C(last=a0) + D(last=a2)
      ('d','E','F',V0)]   # b2: joins E(last=a0) + F(last=a1)
```

Verified with the COMMITTED d42b1 machinery (scriptC):

- every event is admissible at its prefix per the committed `admissible()` AND present in
  the committed `candidates_for()` superset, each with weight exactly 1/20 (6 actors:
  deliver sector 1/4 over 5 receivers × 1 holding);
- `event_poset(W6)` pred sets: `[[],[],[],[1,2],[0,2],[0,1]]` — the event poset is
  EXACTLY S3 (the standard 3-dimensional example; induced-pattern check passes);
- the committed v8 `g2.order_dim_le_2` REJECTS it; the receipt's ported `dim_le_2`
  REJECTS it. The receipt's own NG3 row machinery would print
  `W6(n=6): DIM>2 — REJECTED`.

Since no 3-dimensional poset exists on ≤ 5 elements (the receipt's own NG1 anchors,
plus this review's exhaustive n=5 sweep, §4), **six events is the minimum possible
witness size — transport generates dimension at the first size at which dimension can
exist at all.** A 9-event physical variant with three genesis proposals as the
incomparable creations (`W9` in scriptC: 3 × `('p',X,V0,0)` + 6 deliveries) is likewise
admissible, contains S3 induced, and is rejected. And the actor count is not the escape:
`W4` (§3.6) does it with FOUR actors — the same set CH uses — at the same minimal
n = 6, via a non-S3 3-irreducible order.

The mechanism is the delivery JOIN itself: a delivery is a 2-wire event; three
2-wire events with pairwise-disjoint fresh wire-pairs make the 3-antichain, and three
more 2-wire events joining the right wire pairs make the crown tops. Nothing outside the
committed grammar is used; W6 is the same epistemic class as the committed chains
(constructed, admission-checked at every prefix — CH itself uses 4 actors, outside the
enumerated arms).

Consequences:
- The receipt's printed NG3 facts (0/6, per-chain values) are all TRUE and survive.
  What dies is the universality reading: "paper 13 universality holds at chain scale"
  is true only of the six sampled chains, and LOG #333's header sentence, read as the
  answer to the pin's question, is FALSE. No downstream paper cites it yet (grep clean)
  — the repair is cheap now and should happen before one does.
- Paper 13's Thm 2.1 (every 2D order is two-clock) is untouched; what fails is the
  converse reading at generated-grammar scope: generated record orders are NOT all 2D.

### F2 — MAJOR (CONFIRMED): the chain suite was structurally incapable of testing the
### question — five of six chains have width ≤ 2, so their verdicts were theorems
### before the run

Measured widths of the six committed chain posets (scriptC, brute-force max antichain),
with the Dilworth bound dim(P) ≤ width(P):

| chain  | n  | actors | width | dim ≤ 2 outcome    |
|--------|----|--------|-------|---------------------|
| SIG_KR | 4  | A,B    | 2     | GUARANTEED a priori |
| h5     | 5  | A,B,C  | 2     | GUARANTEED a priori |
| SIG_FM | 8  | A,B,C  | 2     | GUARANTEED a priori |
| CH     | 10 | A,B,C,D| 3     | live test (the only one) |
| h11    | 11 | A,B,C  | 2     | GUARANTEED a priori |
| h12    | 12 | A,B,C  | 2     | GUARANTEED a priori |

A width-2 order has dimension ≤ 2 (classical; dim ≤ width). So SIG_KR, h5, SIG_FM,
h11, h12 could not have failed the gate under ANY oracle — the pin's premise
("the CONSTRUCTED transport chains ... are large enough to FAIL dim<=2") is false in
the operative sense: capability is WIDTH (≥ 3, i.e. ≥ 3 wires carrying a 3-antichain
plus the right join pattern), not event count. n=12 with width 2 is exactly as unable
to fail as n=4. The suite's "pre-registered open" question was 5/6 pre-decided; the
one live sample (CH, width 3) passed — a sample of one, against which W6 (also width
3) fails. The 0/6 headline is therefore not evidence about the grammar; it is mostly
a measurement of the chains' sequential construction style.

Structural background (both directions, proved/searched in §3): width ≤ #actor-wires
always (every event carries ≥ 1 actor register; same-register events are chained;
version/mw registers are one-shot), so the 2-actor sector is 2D at ALL depths — a
theorem that makes ARM-1T dimension sweeps permanently vacuous; the 3-actor
pure-transport sector is exhaustively 2D through 10 events; and FOUR actors — CH's
own actor count — already generate a rejected order at six events (witness W4, §3.6,
verified admissible with the committed machinery). The suite's one live chain sat in
a sector that fails at n=6 and sampled a single 10-event point of it.

### F3 — MAJOR (CONFIRMED): NG2's percentile line is wrong under its own label —
### "mu-mass at-or-below landscape median = 0/1037/64" — the true at-or-below mass
### is 8 (~49.4% of the family)

The pin's NG2 promises "the d42a depth-4 family's mu-weighted D* distribution located
in it (percentiles MEASURED)". The single percentile line delivered is:

> `mu-mass at-or-below landscape median = 0/1037/64 [MEASURED, descriptor]`

Three defects (scriptB, all recomputed exactly):

1. **The number contradicts the label.** The landscape median value is
   `land4[109] = 21/64`. The family's dmin distribution over its 976 depth-4 records
   is exactly `{21/64: mu-mass 8 (408 records), 23/64: 141/64 (274), 25/64: 6 (294)}`
   with wsum = 1037/64. The mass at-or-below the median value is therefore
   **8, i.e. 8/(1037/64) ≈ 49.4%** — the family's MODAL value ties the landscape
   median exactly. The printed 0 is correct only for "strictly below the median
   value" (nothing is below; family min = 21/64 = the median).
2. **Why the code got 0:** the condition `sum(1 for x in land4 if x <= d) <= 109`
   is a rank test that excludes ties — 112 of the 219 landscape values are ≤ 21/64,
   so the tied value fails the test. The code measures "d's ≤-rank lies in the bottom
   half", which for a value sitting ON the median with multiplicity (60 landscape
   posets share 21/64) is a strictly-below test.
3. **The print is malformed:** `below` is the int 0 and `wsum` the Fraction 1037/64,
   so the f-string emits the unparseable triple `0/1037/64`.

The takeaway a reader gets ("zero family mass at or below the landscape median" —
the family lives wholly in the worse half) is qualitatively wrong: half the mu mass
sits exactly AT the median. The gate itself (`len(land4)==219 and len(recs)>0 and
wsum>0`) never touches this number, so the defect is descriptor-honesty, not a false
PASS. Everything else in NG2 verified exact: landscape [19/64, 25/64], mean
4735/14016; w_mean 23595/66368; wsum 1037/64; 976 depth-4 records; the family
realizes only {21,23,25}/64 (never the landscape's best 19/64) — a better one-line
descriptor than the one printed. No verdict wording appears — the pin's no-verdict
scope is respected.

### F4 — MAJOR (CONFIRMED): the receipt under-implements the pinned NG1 (the n=5
### 4,231 all-pass anchor is never run) and LOG #333 records it as run

Pin NG1: "the ported oracle + exact-D* reproduce the committed facts: S3 (6 elements)
REJECTED by dim<=2; all labeled posets pass at n = 4 (219) **and n = 5 (4,231)**; the
full 120-permutation n=5 D* range = [1/4, 7/20] exactly." LOG #329 pins the same
three anchors. The receipt enumerates only n=4 (219); no 4,231 enumeration exists in
the code, and the NG1 check label silently drops it. LOG #333 then records:

> "Port fidelity exact (S3 rejected; **219/4231 all-pass**; the n=5 D* range [1/4,
> 7/20] exact)."

— a green ledger row asserting a check the receipt never ran. The FACT is true: this
review enumerated all 1,048,576 relation masks, found exactly 4,231 labeled 5-posets,
and all pass the receipt's `dim_le_2` (scriptD; ~7 s). So the defect is
gate-coverage + record integrity, zero false physics — but by this program's own
receipt-anchor standards a LOG row must not claim unrun checks. Repair pre-verified
(§6 R3).

---

## 2. minor findings

### F5 — minor (CONFIRMED): NG3 has zero mutation coverage of its own data; the
### parity check is mathematically vacuous and mislabeled; the two-clock certificate
### is claimed "delivered" but never printed

Mutation test (mut3): deleting SIG_FM's merge event `mB` — a transcription error in
the round's central objects — leaves the receipt **4/4 PASS, exit 0**. NG3's PASS
condition is only `len(rows) == 6 and ok3`; no anchor pins any chain's content,
poset, orientation count, or D* value. (Contrast NG1, which does its job: mut1,
lobotomizing the oracle to always-True, exits 1 on the S3 anchor; mut2, dropping the
star's closed side, exits 1 on the range anchor.)

The `ok3` parity check (`D*(emb(r2,r1)) == D*(emb(r1,r2))`) cannot fail for ANY point
set — swapping coordinates maps anchored boxes to anchored boxes, so exact star
discrepancy is symmetric identically. It tests the star function's symmetry, not "the
relabeling lemma" (module-reorientation invariance) as the comment claims. The REAL
invariance evidence — min == max over ALL transitive orientations, per chain — is
printed but ungated. And the row text "two-clock (b, chi) = ranks delivered" is not
accompanied by the ranks anywhere in the `.out`: the certificate exists in memory
only. Repairs in §6 R4 (anchors now referee-verified, so the fix is copy-in).

### F6 — minor (CONFIRMED): LOG #333's "CH is the most volume-faithful record
### measured (83/400)" is a cross-n D* ranking that the ported discipline forbids;
### "Seed-independent (0/7)" for an RNG-free receipt

The six chains have six different n (4,5,8,10,11,12). The extraction record the pin
itself cites is explicit that D* at these n is floor-dominated and "only same-n
RELATIVE comparisons across v10 families carry any content", and that cross-N band
comparison was a review-flagged v8 defect class (i2 CHECK 4, repaired to same-N).
Ranking CH's 83/400 (n=10) against h11's 1/4 (n=11) conflates the n-dependent floor
with faithfulness. The receipt correctly abstains from the comparison; the LOG row
adds it. Also: the receipt contains no RNG whatsoever, so "Seed-independent (0/7)" can
only mean interpreter-hash-seed variation; the honest phrasing is deterministic /
hash-seed-independent (verified here: PYTHONHASHSEED ∈ {0,1,424242} → byte-identical
output, and byte-identical to the committed `.out`).

### F7 — minor (CONFIRMED): pin-internal inconsistencies in the suite description;
### NG4's "unverified here" is a one-line theorem

Pin §1 says "the CONSTRUCTED transport chains (n = 8..11)"; pin §2 NG3 lists the six
chains with n ∈ {8,4,5,11,12,10}; LOG #329 says "n = 8..12". One sentence, three
scopes. And NG4's disclosure "zero qualifying pairs at n <= 12 with exp_k >= 10
unverified here" undersells a provable fact: max exp_k = (Δr1−1)(Δr2−1)/n ≤ (n−2)²/n,
which is < 10 for all n ≤ 13 (at n=12: 100/12 ≈ 8.33), so the statistical layer has
zero qualifying pairs on every possible chain at these sizes — a theorem, not an
unverified claim. The pin's NG4 wording ("the statistical layer's nan printed") is
also technically under-delivered — a disclosure sentence is printed instead of a
computed nan; substance identical.

---

## 3. The structural answer the round needed (delivered here)

**Is there a grammar-level argument that generated orders are ALWAYS 2D?** No —
the opposite is now a theorem-with-witness. The exact structural picture for the
committed d42b1 grammar:

1. **Wire structure.** Every event carries ≥ 1 actor register (`regs_of`: p/n → 1
   actor; d → 2 actors; r → all ckey authors + a version register; m → 1 actor + an
   `mw` register). Version/`mw` registers are one-shot (no later event type touches
   them), so the persistent wires are the ACTORS. Events sharing a wire are chained by
   `event_poset`'s `last[]` mechanism. Hence **width(P) ≤ #actors** for every
   generated poset — measured widths in F2 confirm.
2. **2-actor sector: 2D at all depths** (dim ≤ width ≤ 2). The ARM-1T family can
   never fail the gate at ANY cap — this review's sweep of all 3,969 ARM-1T histories
   (0 failures, scriptD) is a consistency check of a theorem, not evidence.
3. **Pure-transport realizability.** For the p/d/n sector: a wire's events form one
   ascending chain whose consecutive pairs are exactly the `last[]` links, so a poset
   is generable iff its elements can be covered by ≤ #actors chains, each element on
   ≤ 2 chains (1 for p/n, 2 for d), with every Hasse edge consecutive on some chain.
   Every such abstract sequence IS admissible: singletons realize as idles (always
   admissible), pairs as deliveries of v0 (always admissible; re-delivery is
   grammatical per the committed docstring).
4. **S3 threshold: exactly 6 actors** (p/d/n sector). Lower bound: if a generated
   order contains S3 induced, descend each crown top to its minimal join layer (if a
   top has a single lower cover m, then m dominates both required a's and not the
   third, so {a's, m's} is again induced S3 with smaller height; iterate). At the
   terminal layer each of the 3 pairwise-incomparable tops has ≥ 2 lower covers, each
   cover-edge needs its own wire through the top, and no wire can contain two
   incomparable tops — so ≥ 6 distinct wires. Upper bound: W6 (F1) does it with 6.
   Corollary: the committed chains (≤ 4 actors; every event ≤ 2 registers — their
   arbs are singleton-ckey, their merges 2-register, so the bound applies) could
   never have exhibited an S3-containing order; a dim-3 order without S3 would need
   a different 3-irreducible pattern, bounded-depth-searched below.
5. **Enumerated families, swept in full** (scriptD): ARM-1T (A,B; depth ≤ 4; 3,969
   histories): 0 dim failures (structural, see 2). ARM-2T (A,B,C; depth ≤ 3; 3,424):
   0 failures (n ≤ 3 — vacuous below n=6). d42a/d42b3 placement family (1,191): 0
   failures (n ≤ 4 — vacuous). No enumerated record can flip the headline at the
   committed caps; the flip lives in the constructed sector (W6), exactly where the
   round chose to place its own chains.
6. **Wire-count thresholds** (scriptE2, exhaustive BFS over abstract wire histories
   up to wire relabeling, dim tested once per distinct poset; level sizes printed):
   - **w=3: NO dim>2 poset exists up to depth 10** (exhaustive; 148,707 states at
     depth 9) — the 3-actor pure-transport sector is two-dimensional at least
     through 10 events;
   - **w=4: dim>2 FOUND at depth 6** — and it is realizable at CH's own actor
     count. Concrete verified witness (scratchpad, committed machinery):

     ```python
     W4 = [('d','A','C',V0), ('d','B','D',V0), ('p','A',V0,0),
           ('p','C',V0,1), ('d','A','B',V0), ('d','C','D',V0)]
     ```

     every event admissible per the committed `admissible()` and present in the
     committed `candidates_for()` (weights 1/12, 1/12, 1/8, 1/8, 1/12, 1/12);
     preds `[[],[],[0],[0],[0,1,2],[0,1,3]]` (a non-S3 6-element 3-irreducible);
     REJECTED by both the committed g2 oracle and the receipt's port. **Four
     actors — CH's actor set — generate dimension at six events.** CH's pass was
     not actor-count safety; it was the chain's sequential construction;
   - w=5: dim>2 found at depth 6; w=6: dim>2 found at depth 6 (search sanity —
     reproduces the S3/W6 class).
   (Scope note: the searches cover the p/d/n sector — events on ≤ 2 actor wires.
   k-author arb events are (k+1)-register joins, and an exact-repeat arb can ride
   its predecessor's vname register as an extra wire; either could in principle
   break the w=3 barrier. Untested corner, declared. Merges are effectively
   1-actor-wire events — the `mw` register is genuinely one-shot — so they are
   covered by the singleton moves.)

**Net:** the honest NG3 statement is: "0/6 sampled chains reject; five were width-≤2
and could not reject; the grammar itself generates 3-dimensional record orders at
n = 6 — with 6 actors (W6 = exactly S3, minimal) and already with 4 actors (W4, CH's
own actor set) — so two-clock universality FAILS at generated-grammar scope. The
frame remains exhaustive for the 2-actor sector (theorem), for the 3-actor
pure-transport sector through ≥ 10 events (exhaustive search; multi-author arbs
untested), and for whatever natural-family analysis constrains width to 2."

## 4. What survives (all verified, digit-for-digit)

- **Port fidelity is genuinely exact** (scriptA, all against COMMITTED v8 code, not
  the extraction): the six chain posets rebuilt from the committed d42b1 head are
  tuple-identical to the receipt's; `event_poset` preds audited transitively closed,
  strict, irreflexive; g2's `order_dim_le_2` reproduces every chain verdict and
  g2's `star_discrepancy_exact` every chain D* to < 1e-12 of the receipt's exact
  Fractions: 23/64, 1/4, 79/256, 83/400, 1/4, 145/576; i1's `count_orientations`
  (uncapped) matches the receipt's enumerator on all six chains (2,2,2,4,2,2 — the
  cap=64 was never approached) and on all 219 4-posets.
- **NG1 anchors:** S3 rejected by committed g2; n=5 range [0.25, 0.35] reproduced by
  committed g2 star over all 120 permutations; 219 labeled 4-posets, all pass under
  committed g2. The skipped 4,231 anchor verified TRUE by this review.
- **The 219 landscape** independently reproduced with a brute-force orientation
  enumerator (all 2^k arc assignments, transitivity-checked) + an independent
  Fraction port of v8's two-combo star formula: per-poset min-D* and orientation
  counts agree 219/219; min/max/mean = 19/64, 25/64, 4735/14016 exact.
- **The receipt's 4-combination star equals v8's 2-combination star** — provably (the
  mixed open/closed corners are dominated by the diagonal ones) and empirically (400
  random rational point sets incl. ties, exact equality). A port deviation from both
  the v8 code and the extraction pseudocode, but a sound one (F9).
- **Oracle agreement on hostile populations:** 60 random transitive-closure posets
  (n = 6..12; 10 rejected by both) + 10 KR(24) orders (all rejected by both) — zero
  verdict divergence between committed g2 and the port.
- **NG2's other numbers:** wsum 1037/64, w_mean 23595/66368 (~0.3555), landscape mean
  4735/14016 (~0.3378), 976 depth-4 records, all exact; mu correctly weights only the
  family average (D* stays unit-weight canonical, per the committed convention).
- **NG3's printed facts:** 0/6 true of the six chains; min == max over ALL
  orientations for every chain (the genuine relabeling-lemma evidence); CH's 4
  orientations all at 83/400.
- **Plumbing:** byte-identical rerun; PYTHONHASHSEED-independent; exit-1 machinery
  fires on oracle/star mutations (mut1, mut2); the d42-layer exec heads are
  def-only (no family enumeration side effects); committed d42b3/d42b1 `.out`
  anchors (1191; 3969/3424) match this review's re-enumerations.
- **NG4's disclosure fact** upgraded to a theorem: zero qualifying statistical pairs
  is provable for all n ≤ 13.

## 5. nits

- **F8 (dead code):** `CACHE` in NG2 is write-only (vestige of d42b3's
  `enumerate_family`); `dim_le_2`'s `want_realizer` parameter is unused; NG2 unpacks
  `dmax, cnt` and uses neither; `sys.setrecursionlimit(300000)` is fine (bt recursion).
- **F9 (port notes, both sound):** the 4-combo star superset (see §4); `topo_rank`
  uses lexicographic-min tie-breaking vs v8's reversed-stack — immaterial because
  L1/L2 are total orders (unique topological order), verified by the digit-for-digit
  agreement.

## 6. Prescribed repairs (pre-verified where stated)

- **R1 (F1/F2, the round's substance):** add W6 and W4 to the chain suite and
  re-scope. The receipt's own machinery already handles rejection rows
  (`W6(n=6): DIM>2 — REJECTED`); admissibility, posets, and both-oracle rejection
  are pre-verified here (scriptC + the W4 verification). Rewrite the NG3 outcome
  line to the §3 "net" statement; amend LOG #333's header (a correction row, per
  program convention — the entry's per-chain facts stand). Record the structural
  results: dim ≤ width ≤ #actors; 2-actor sector permanently 2D; 3-actor
  pure-transport 2D through 10 events (exhaustive); 4 actors fail at n=6; S3
  threshold = 6 actors sharp; five chains width-≤2 (a priori passes). The width
  table (F2) is copy-ready.
- **R2 (F3):** replace the median line with the measured distribution
  (`21/64: 8 (~49.4%, AT the median value); 23/64: 141/64 (~13.6%); 25/64: 6
  (~37.0%)`) or fix the condition to `d <= land4[109]` and print
  `float(below/wsum)`; either way, print fractions of wsum, not the `0/1037/64`
  triple. Pre-verified numbers above (scriptB).
- **R3 (F4):** add the n=5 enumeration to NG1 (1,048,576 masks → 4,231 posets → all
  pass; ~7 s; scriptD's loop is copy-ready). Until then, LOG #333's "219/4231" claim
  needs a correction row.
- **R4 (F5):** anchor the six (n, verdict, D*, orientation-count) tuples in NG3 — the
  values are now referee-verified against committed v8 code, so hard-coding them as
  anchors is honest; gate `dmin == dmax` per chain (the real invariance content);
  relabel the parity check as a star-symmetry sanity check or drop it; print the
  (r1, r2) ranks if the row claims the certificate is delivered.
- **R5 (F6):** strike or re-scope the LOG's cross-n "most volume-faithful" line
  (same-n floors would be needed first — the extraction's own floor-calibration
  convention, §8); replace "Seed-independent (0/7)" with
  "deterministic (byte-identical; hash-seed-independent)".

---

*Review artifacts: scriptA output (all PASS), scriptB (NG2 forensics), scriptC
(W6/W9 witnesses; width table), the W4 verification, scriptD (0 failures across
3,969 + 3,424 + 1,191 histories; 4,231/4,231 n=5 pass), scriptE2 (wire thresholds:
w=3 clean to depth 10; w=4/5/6 fail at depth 6), mut1/mut2 exit 1, mut3 exit 0
(the F5 exhibit). Independent wsum cross-check via the committed `enumerate_family`
plus flow conservation (1037/64 twice). Nothing in the pinned object was modified.*

---

# Delta verification (round 2) — repairs at HEAD b4d164b (#341)

**Object:** the repaired `v10/code/d43d_dstar_generated_exact.py` + committed `.out`
(6/6 PASS), pin amendments C1–C2 (`note-d43d` §3), LOG #337 (round frozen,
forward-correction of #333) and #341. Round-1 body above untouched.
**Instrument:** `scriptF_delta.py` (scratchpad) — re-verification of every repaired
gate against this round's own machinery (committed d42b1 layer + committed v8 g2
oracle), the three round-1 mutants rebuilt against the repaired source, determinism.

**Verdict: DELTA-CLEAN on substance — 0 new defects; all four MAJORs and the
gate-coverage minor discharged. ONE residual minor (the F3 print format, below) +
two cosmetic nits; none gate-relevant, none blocking terminal.**

## D1. Item-by-item

1. **NG3b (F1 — the witnesses gated): VERIFIED.** The receipt's `W6` and `W4` are
   tuple-exact to the round's witnesses. Independent re-verification through the
   committed layer (stronger than the receipt's own gate — admissibility AND
   `candidates_for` membership): W6 admissible ×6 at exactly 1/20; W4 at
   1/12, 1/12, 1/8, 1/8, 1/12, 1/12. W6 preds `[[],[],[],[1,2],[0,2],[0,1]]` = S3;
   both posets REJECTED by the committed v8 g2 oracle; the receipt's gate values
   (`d2_w6 = d2_w4 = False`, `is_s3 = True`) agree. The check text carries the
   thresholds (2-actor never / 3-actor through 10 / 4-actor at 6) cited to the
   frozen round, with #333 marked forward-corrected at #337. Correct.
2. **NG3 width diagnostic (F2): VERIFIED.** Receipt `width_of` (exhaustive
   antichain) reproduces this round's measurements exactly —
   `{SIG_KR:2, h5:2, SIG_FM:2, CH:3, h11:2, h12:2}` — and the gate now REQUIRES
   5/6 ≤ 2 ∧ CH = 3; the label owns the width-blindness ("capability is width,
   not event count ... only CH was live").
3. **NG2 median line (F3): SEMANTICS REPAIRED, FORMAT NOT.** The condition is now
   `d <= med` with `med = land4[109] = 21/64` — at-or-below the true median VALUE,
   ties included — and the mass is 8, i.e. **512/1037 ≈ 0.4937 of wsum**, matching
   the round's ~49.4%. RESIDUAL (minor): the `.out` still prints the double-slash
   triple `= 8/1037/64` (`{below}/{wsum}` with Fraction wsum) — F3 defect (3)
   verbatim; no parseable fraction or percentage appears in the output, while LOG
   #341 quotes "~49.4%" as if printed. One-line fix, pre-verified:
   print `f"{Fr(below)/wsum} (~{float(Fr(below)/wsum):.4f}) of wsum"`
   → `512/1037 (~0.4937)`.
4. **NG1 n=5 anchor (F4): VERIFIED.** `all_posets(5)` runs in-receipt; `len == 4231`
   and all-pass are inside the NG1 PASS condition (`ok5`); the `.out` discloses
   "n=5 posets = 4231 all-pass (F4: now IN-RECEIPT)". LOG #341's record now
   matches an executed check.
5. **NG3c + mutation coverage (F5): DISCHARGED.** All three round-1 mutants rebuilt
   against the repaired source now exit 1: oracle lobotomy (4/6, NG1+NG3b bite —
   NG3b is itself new coverage), star-closure drop (3/6), and the round's exhibit,
   the SIG_FM merge-deletion mutant, now **fails NG3c (5/6, exit 1)** — the 79/256
   anchor does its job (and matches the committed-v8 value verified in round 1).
6. **Pin amendments C1–C2: VERIFIED PRESENT AND ACCURATE.** C1 owns the width axis,
   adopts the witnesses, states the thresholds with the 3-actor bound correctly
   scoped ("not through ten events"), answers §1's question POSITIVELY, records
   the #333→#337 forward-correction, and owns the n-range error ("n = 8..11"
   mis-stating the n = 4..12 suite). C2 covers the median repair, 4,231
   in-receipt, the SIG_FM anchor, the cross-n withdrawal from the verdict
   (same-n discipline), and re-reads "seed-independent" as deterministic. The
   repaired verdict line states the settled result correctly ("transport
   generates dimension at actor-width >= 4 (S3 at 6 actors)").
7. **Untested corner: PRESENT and — upgrade — now provably MINIMAL.** C1 declares
   multi-author arbitrations the untested corner. The round-1 scope note had
   flagged a second candidate corner (an exact-repeat arb riding its
   predecessor's vname register as an extra wire). Delta-verified: that corner is
   VACUOUS — the initiator's own chain always contains its earlier arb, the base
   is superseded in its view, and both the exact-repeat arb and the same-base
   re-proposal are inadmissible per the committed `admissible()` (checked
   mechanically). vname/mw registers are therefore provably one-shot, and
   "multi-author arbitrations" is exactly the residual corner — the pin's scope
   is not just present but sharp.

## D2. Plumbing

Repaired receipt rerun: byte-identical to the committed `.out`; PYTHONHASHSEED ∈
{0, 7, 424242} → byte-identical (consistent with #341's "Deterministic (0/19)").
Exit-1 machinery verified via the three mutants above.

## D3. Residuals (non-blocking)

- **minor (the only substantive one):** F3 defect (3) — the malformed
  `8/1037/64` print — survives the repair; fix pre-verified in D1.3. LOG #341's
  "~49.4%" is the LOG's gloss, not the receipt's output, until this line is
  patched.
- nit: the legacy print "NG3 outcome: 0/6 chains REJECTED ... (paper 13
  universality holds at chain scale)" survives verbatim below NG3c, including
  the now-dead dichotomy branch; true of the six chains and disambiguated by the
  repaired verdict line, but the phrase "universality holds" earns its keep only
  with the width-blindness clause one line above it.
- nit: NG2's PASS condition still gates none of its descriptor numbers (unchanged
  round-1 posture; consistent with "descriptors ONLY").

**DELTA-CLEAN on substance. With the D1.3 one-liner (or an explicit acceptance of
the print as a documented cosmetic residual), d43d is fit for terminal with the
settled statement: transport generates dimension at actor-width ≥ 4 (S3 sharply
at 6 actors for pure transport; 3-actor pure transport 2D through 10 events,
multi-author arbs the declared — and now provably minimal — untested corner);
the D* instrument is port-faithful digit-for-digit; the family sweep is
descriptors-only at its floor-dominated scale.**
