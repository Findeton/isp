# Γ-MAIN (paper-12) — HOSTILE REVIEW, R1 OPERATOR LENS

**Reviewer:** R1, operator lens (from-scratch reconstruction with
different primitives).  **Protocol:** PANEL A of
`v14/note-gmain-r4-protocols.md` (frozen, `a3a39813e5b5`), K1–K5
binding.  **Pin:** `v14/note-gmain-pin.md` `8529ddc4a319`.

**Object, hashes verified at the start of the round and again after
every hostile run:** paper `d85a629a9378`, code `51c3b4cf3f3c`, output
`b2b45be500b7`, receipt `974f36b1251a`.  All four unchanged.

**GRADE: ACCEPT-WITH-FIXES.**  Not one delivered number is false.  I
rebuilt the unit from the committed layer with different primitives —
different family enumeration, different canonical-key encoder,
different potential recursion, and a **second, independent
construction of Γ from path-products of the kernels** — and every
construction fact, every census, every spectrum, every deficit and
every negative-entry count reproduced exactly.  The fixes are about
what the head is entitled to say, not about arithmetic: the
settlement's TARGETS link is carried by a measurement that never
touches Γ, at the readout the unit itself declares non-primary,
against targets that are count-defined in their own frozen source; and
the readout fiber is larger than the inventory says.  The K3 successor
question has a measured answer, and it is already pinned.

**Recomputations: 405.**  Everything on scratch copies; nothing
imported from the unit; every cross-unit read by `git show <sha>:`.

---

## 1. The reproduction ledger — what I rebuilt and what it returned

Independent code path throughout (`op1`–`op9` in scratch).  Only the
LAW is shared: the d42b1 admission-and-pricing prefix, exec'd from its
committed bytes at `f40f5e1` (`576275d55ecf`), as any reconstruction
must.

| what | delivered | my rebuild |
|---|---|---|
| per-level transport census | [1, 8, 60, 452, 3448, 26760] | identical |
| cumulative | [1, 9, 69, 521, 3969, 30729] | identical |
| carrier | 3969 | identical |
| MENU / REC classes | 113 / 2477 | identical |
| MENU dims per cut | [1, 5, 13, 45, 113] | identical |
| REC dims per cut | [1, 8, 51, 324, 2093] | identical |
| root potentials $G_1..G_5$ | 2, 4, 257/32, 1035/64, 4173/128 | identical |
| cut masses | 1 at all five cuts | identical |
| kernel properness / positivity | 0 / 0 violations | 0 of 4564 entries |
| column-stochastic, 20 transfers | 0 bad, 0 negative | identical |
| $G(\cdot,r)$ multi-valued, MENU | r=2: 4/13, else 0 | identical |
| $G(\cdot,r)$ multi-valued, REC | 0 at every r | identical |
| labelled edges MENU / REC | 368 / 2900, multi-weight 0 | identical |
| exchange-square census | closed 1546, AB-only 28, BA-only 12, both-blocked 142 | identical |
| $r_q$ spectrum | {1/2: 70, 2/3: 2, 3/2: 6, 2: 10}, 88 defective | identical |
| $r_k$ spectrum | adds {64/65: 6, 65/64: 2} | identical |
| MENU/q rung | closes 1402, self-loops 44, cycle rank 134, obstruction 44, ⟨2,3⟩ rank 2 | identical |
| MENU/k | self-loops 52, primes [2,3,5,13] rank 3 | identical |
| MENU/Γ | 144 not closing, 416 non-unit of 1402, primes [2,3,5,13,19,97,389] rank 7 | identical |
| REC at all three readings | flat: 0 / 0 / 1 on 473 | identical |
| 44 + 44 dichotomy | 44 curvature, 44 descent-obstruction, base depths {1: 4, 2: 40} | identical |
| Γ on the 44 curvature | {1/4: 2, 1/3: 8, 8/13: 2, 13/8: 6, 3: 24, 4: 2} | identical |
| CK census | MENU 6/10, failures [34, 112, 12, 12]; REC 10/10 | identical |
| eq. 22 negatives | 36 / 104 / 108 / 164; minima −1/97, −5/97, −1/18, −1/128 | identical |
| leg 1 | 152672 raw continuations, 3584 legs, five patterns | identical |
| leg 2 | 256 bases, 796672 expansions, 73728 legs | identical |
| COUNT readout | (3/7,1/7,3/7) and (4/9,1/9,4/9) | identical |
| OCCUPANCY readout | (3/8,1/4,3/8) at both legs | identical |
| F8 slot × kind | d: [1024, 0, 1024]; n: [512, 512, 512] | identical |
| prune gate | 3 bases, 60492 unpruned nodes, 864 legs, identical | identical |
| sector masses | delivery 1/2, idle 1, both legs; count 4 → 6 | identical |
| renewal transfer | 8 × 8, one column, every entry 1/8, count = occupancy | identical |
| Sylvester certificate | $HH^{T}-8I$ 0 nonzero, 0 mismatches | identical |
| screen DS deficits | 70/33, 31083/4279, 209/10; mis-normalized 5/2 and 5/2 | identical |
| B2 atoms | R-SIG 5161, R-MENU 1365, blocks {(1,1):1365,(2,2):3788,(2,3):4,(3,2):4} | identical |
| carrier blocks | 689 points, 9 classes, all pure | identical |
| mover census | 64 columns, 64 moving, 0 stationary | identical |
| 23 byte anchors | 23 expected digests | 23 of 23 verified independently |
| 9 path-value anchors | CR-A / CR-B / R4 / Γ-prep | 9 of 9 verified independently |

Two independent constructions of Γ agree exactly: the unit's
joint-over-marginal formula and my path-product construction (push the
within-class occupancy forward under chained $k_r$) agree at **11,989
of 11,989** non-zero cells on both quotients.  That is an independent
proof of the exact-conditional identity the paper's §4 asserts.

---

## 2. Findings, ranked

### MAJOR

**M1 — THE TARGET TEST NEVER TOUCHES Γ, AND THE SETTLEMENT LINK IS
EVALUATED AT THE NON-PRIMARY READOUT AGAINST COUNT-DEFINED TARGETS.**
Three measurements, each independently checkable:

1. *TEST 1 is Γ-free and off-carrier.*  An exhaustive token scan of
   the whole TEST 1 region (`gmain_exact.py` lines 1125–1430) returns
   **zero** occurrences of `A_MENU`, `A_REC`, `GAM_M`, `GAM_R`,
   `IDX_M`, `MASS_M`, `W[`, `k_of(` or `CARRIER`.  The leg ensembles
   run from depth 3 to depth 7 and from depth 6 to depth 10 — the
   declared carrier is $d \le 4$.  So the pin's test 1 ("the
   constructed Γ must reproduce the transport positional laws … and
   exhibit the F8 mechanism as a property of Γ, not an import") is
   answered by a measurement of the transport grammar, with Γ, the
   quotient and the kernels absent.  The scope segment does disclose
   the depths (`LEGS=RENEWAL-CUT-ENSEMBLES-AT-DEPTHS-3..10`); §5.1
   does not, and the reader of §5.1 will take the table to be a
   property of Γ.
2. *The hit is at the readout the unit declares non-primary.*  The
   arena declares `readout: OCCUPANCY primary, COUNT alternative`.  At
   OCCUPANCY both targets miss, at both legs — I measure
   (3/8, 1/4, 3/8) exactly as delivered.  The settlement link is
   computed as `targets_hit = (T1_VERDICT != 'TARGETS-MISSED')`, an
   existential over the readout fiber: it is True whenever *some*
   readout hits.
3. *The targets are count-defined in their own frozen carrier.*  The
   R6b′ adjudication register (`f6c11163c77d`, the pin's declared
   carrier of the targets) derives the positional law from
   "C(n−1,2) **equiprobable** configurations" and drives 3/7 → 4/9 by
   "delivery **multiplicity** 2→3".  The unit's own T1-MULTIPLICITY
   gate re-derives $(m+1)/(2m+3)$ from **leg counts** (I reproduce
   slot 1 = 512·(m+1), total = 512·(2m+3)).  Reproducing them at the
   count readout is therefore inheritance of a convention, not
   confirmation of a law.

   **This is the RSQ shape at the summit and it must be in the head.**
   *Repair (three edits, no recomputation needed):* (a) §5.1 gains one
   sentence naming the depths and the absence of Γ from the test;
   (b) the settlement table's `targets hit` row reads
   `True at the COUNT readout / False at the declared PRIMARY readout`,
   and `SEG_SETTLE` either names both failed links or re-labels the
   link `TARGETS-HIT-AT-A-NON-PRIMARY-READOUT`; (c) §5.1 states that
   the targets are count-defined at their source, with the register's
   own words.  The paper is already most of the way there — the T1
   verdict string says which readout hits — but the settlement table
   says `True` unqualified, and that is the sentence the corpus will
   quote.

**M2 — THE READOUT FIBER IS AT LEAST THREE, AND THE THIRD READING IS
THE HONEST ONE.**  New measurement.  The local menu mass
$M(h) = \sum_e q(e\mid h)$ is **not constant** on the carrier: 2 at
3757 histories, 5/2 at 212.  So the product of raw weights along a leg
is not a probability, and the readout the paper calls "the process's
own law" is an *unnormalised* weight readout.  Normalising each step —
the same move the unit calls "the enabling step" at the carrier —
gives a third positional law:

| readout | leg 1 | leg 2 | hits targets |
|---|---|---|---|
| COUNT (uniform on legs) | (3/7, 1/7, 3/7) | (4/9, 1/9, 4/9) | yes |
| RAW-μ (the unit's "occupancy") | (3/8, 1/4, 3/8) | (3/8, 1/4, 3/8) | no |
| **LOCAL, step-normalised $q/M(h)$** | **(15/38, 5/19, 13/38)** | **(15/38, 5/19, 13/38)** | **no** |
| H4-chain (the law Γ is built from) | EXCLUDED-BY-CAP (needs depth 11) | — | — |

The third reading is leg-independent like the second and, unlike
either declared reading, **left–right asymmetric** (15/38 ≠ 13/38).
The fourth — the chain law Γ actually uses — cannot be evaluated on
the legs at the declared cap at all.  *Repair:* the I-READOUT row and
the `MOTIVATION` segment's `FIBER-2` must become `FIBER->=3 (three
measured; the H4 reading EXCLUDED-BY-CAP)`, and §4 must say that the
leg-level readout pair is **not** the carrier-level readout pair
(carrier: $w$ vs uniform-on-classes; legs: $\prod q$ vs
uniform-on-legs).  The inventory currently folds two different fibers
into one item.

**M3 — K3: THE BETWEEN-CARRIER QUESTION HAS A MEASURED ANSWER, AND
THE PROTOCOL'S PREMISE IS FALSE.**  See §4 below; this is the
successor's address.

**M4 — "THE BLOCK DECOMPOSITION" DECOMPOSES 9 OF 113 CLASSES.**  §4
prints the depth-≤5 anchor census (5161 R-SIG points, 1365 menu-exact,
blocks {(1,1): 1365, (2,2): 3788, (2,3): 4, (3,2): 4}) and calls it
"The block decomposition" of the carrier.  The carrier facts — which
the unit measures and prints in its own output, and which I reproduce
— are **689** R-SIG points in blocks {(1,1): 341, (2,2): 348}, meeting
**9 of 113** MENU classes.  The claim "every carrier class that meets
R-SIG meets exactly one block" is true and is a statement about nine
classes.  *Repair:* print 689 and 9/113 in §4 beside the anchor
census.

### MODERATE

**D1 — two of the 36 mutants are vacuous.**  I extracted every
`mutant()` kill predicate by AST (32 call sites, one in a 5-iteration
loop = 36 mutants).
* `MUT-WAIVER-FALSE → G-NEVER-FALSIFIED`, killed by
  `all(g['name'] in {x['name'] for x in GATES} for g in GATES)` — a
  **tautology**, true of any ledger.
* `MUT-PAPER-DRIFT → G-PAPER-CLAIMS`, killed by
  `'9999' not in PAPER_TEXT` — unrelated to the gate's predicate, and
  trivially true (I measure 0 occurrences of `9999` in the paper).

  Three more assert a property of the ledger instead of injecting a
  corruption: `MUT-FLOAT-LEAK` (proves that `ast` represents `0.5` as
  a float, not that the guard fires on mutated source),
  `MUT-CENSUS-LAX`, `MUT-COMPLIANCE-FALSE`.  The remaining ~20 are
  genuine injections that construct a mutated object and evaluate the
  gate's own predicate on it, and ~7 are "the inverse claim is
  measurably false" contrasts, which are acceptable at the #34
  standard.  *Repair:* `MUT-WAIVER-FALSE` → append a synthetic
  never-falsified gate with no waiver and show `G-NEVER-FALSIFIED`
  turns False; `MUT-PAPER-DRIFT` → perturb one `PAPER_CLAIMS` value
  and show the membership test fails; `MUT-FLOAT-LEAK` → run the AST
  guard over a copy of the source with one float inserted.  The
  never-falsified count does not move (both target gates carry other,
  genuine coverage), but the "36 declared, 36 killed" line is
  currently worth 34.

**D2 — the paper is read from the worktree and the compliance rows do
not say so.**  `v14/paper-12-gamma-main.md` does **not** exist at the
declared tree sha `f40f5e1` (verified: `git cat-file -e` fails), so
`PAPER_TEXT` falls back to `PAPER_ON_DISK`.  The 13 verbatim
quote-fidelity rows — evaluated first, with the genuine short-circuit
— and `G-PAPER-CLAIMS` are therefore evaluated against **mutable
worktree bytes**.  The code comment discloses it; the #46 and #62
compliance rows in the output do not, and #62's row says
"worktree bytes are never read for a source".  The risk is contained
(the paper is the object under review and its digest is frozen and
verified), but the disclosure belongs in the output.  *Repair:* the
#46 row gains "… and this unit's own paper, read from the worktree
because it is not committed at delivery time (sha256-12
d85a629a9378)".

**D3 — the verbatim anchors are spliced into prose and break the
sentences that host them.**  §4 ends mid-sentence ("…it is a monotone
non-decreasing"); §5.1 carries a stray `**` and an ungrammatical
splice ("The register records the mechanism as (p,d,p,r) does not
occur…"); §5.2, §5.3, §5.4 and §5.7 run quote into prose without
punctuation.  The paper reads as machine-assembled at exactly the
places the #62 spec touches.  *Repair:* set each anchor as a
blockquote and complete the host sentence.  The quoted **bytes** need
not change, so all 13 anchors keep binding.

**D4 — "the group DOES discriminate at the k and Γ readings" is
weaker than it reads.**  The unit is right to warn that the q-group
cannot discriminate; I verify the reason independently (the $r_q$
value set over all 1546 closed squares is {1, 1/2, 2/3, 3/2, 2}, so
every quotient's q-group is a subgroup of ⟨2,3⟩ — measured on ten
carriers, all give ⟨2,3⟩ or trivial).  But the same argument bounds
the k-reading: the $r_k$ value set is
{1, 1/2, 2/3, 3/2, 2, 64/65, 65/64}, so every quotient's k-group is a
subgroup of ⟨2,3,5,13⟩; and across the ten carriers I measure it takes
exactly **two** values — rank 2 on every carrier where the horizon
potential descends, rank 3 on every carrier where it does not.  The
k-group is a *descent detector*, not a carrier fingerprint.  *Repair:*
say so in §5.2's methodological note.  This strengthens the note.

**D5 — the screen's four `S-FAIL-DS` verdicts are structurally
forced.**  For a column-stochastic $M$, $\sum_i(\text{row}_i - 1) = 0$
exactly, so DS holds only if every row sum is exactly 1; under the
identity padding any class realised at the later cut but not the
earlier one has row sum > 1 the moment it receives mass.  The
informative content is the exact $L_1$ price (70/33, 31083/4279,
209/10), which is a measurement, and the pass/fail contrast with the
renewal transfer.  *Repair:* one clause in §5.3 saying the DS failure
is forced by the shape and the price is the datum.

### MINOR

**N1 — the exact-conditional identity needs its horizon named.**  §4
writes "the identity $w(h)\,k_r(e\mid h) = w(h+e)$" with $r$ free.
Measured: at $r = 4 - |h|$ there are **0** violations over the
carrier; at every other admissible $r$, **352 of 596** tests violate
it.  *Repair:* write $k_{4-|h|}$.

**N2 — deliverable names.**  The pin declares `gmain_exact.py` +
`_output.txt` + `_receipt.json`; the delivered files are
`gmain_output.txt` / `gmain_receipt.json`.  The paper's Artifacts line
is correct; the pin's line is not.  Cosmetic.

**N3 — interim gate counts drift in the output** (84 at the
never-falsified census, 87 at the closing census, 88 in TOTALS)
because gates are appended as the run proceeds.  Harmless; the receipt
totals are the authority and the paper quotes them.

**N4 — CR-B's receipt carries a second reading** (`flip_orbits` 2,
`flip_simplex_dim` 1, `flip_transitive` False) that §5.5 does not
mention.  Both readings give `transitive False`, so no verdict moves.

---

## 3. K1, K2, K4, K5 adjudications

**K1 — THE CONSTRUCTION'S FIDELITY: PASS.**  Rebuilt independently:
the family (BFS by level, candidates computed only where used), the
canonical keys (a recursive canonical-string encoder, not the unit's
tuple encoder), the two quotients from d74's own definitions, the
potentials by upward DP, the kernels, and **Γ twice** — once as the
unit builds it, once as a path-product of chained kernels averaged
over the within-class occupancy.  Column-stochastic exactness holds on
all 20 transfers with 0 negative entries; the cut dims are
[1, 5, 13, 45, 113]; the class law is the exact conditional (the two
constructions agree at 11,989/11,989 cells); the 23-sha provenance
verifies 23 of 23 independently; the non-descent measurement is 4 of
the 13 classes the depth-2 cut carries — I checked both readings of
that denominator (the 4 multi-valued classes are carried at depths 1
and 2, take values {4, 65/16}, and are multi-valued **within** the
depth-2 cut), so the paper's sentence is exactly right.  One
structural fact the paper does not state: **45 of the 113 MENU classes
occur at more than one cut** (distribution over cuts
{1: 68, 2: 32, 3: 8, 4: 4, 5: 1}), so the carrier is not depth-graded
and 90 of Γ's 1092 non-zero cells are label-diagonal.  Worth a line in
§2; nothing depends on it.

**K2 — THE TARGETS UNDER READOUT-RELATIVITY: the decisive ruling.**

> **Is there any pinned fact that forces either readout?  For Γ,
> yes — and it forces OCCUPANCY.  For the targets, no — and they were
> born at COUNT.**

* The pin's own construction clause defines Γ as "built from the
  pinned kernels $k_r$ (the horizon normalization is the enabling
  step)".  The COUNT readout uses **no kernel at all** — it replaces
  $w$ by the uniform measure on admissible objects.  So at the
  carrier, the pin points at OCCUPANCY, and the unit's own arena
  declares OCCUPANCY primary.  Nothing pinned forces COUNT.
* The targets, by contrast, are count-defined in the frozen register
  that carries them (M1.3), and the test that reproduces them never
  touches Γ (M1.1).
* Therefore **TARGETS-HIT is readout-selected**, and it is selected by
  the targets themselves.  At the unit's declared primary readout the
  link is False; at the third readout I measured it is False; at the
  fourth it is not evaluable at the cap.  One of at least three
  motivated readings hits, and it is the one that discards the weights.
* **Is TARGETS-HIT an honest head at any motivated reading?**  Yes —
  at the count/multiplicity reading, which is the reading in which the
  targets are *defined*.  That is a real and reportable result: Γ's
  underlying process reproduces the register's leg-count law exactly,
  including the F8 mechanism, which the unit derives rather than
  imports (the (p,d,p) comparability census, 512/512 vs 0/256, I
  reproduce).  What it is not is evidence that Γ reproduces a
  positional *law*: at every weighted reading measured the positional
  law is leg-independent and misses both targets.
* **Does the settlement survive?**  The construction survives; the
  head does not, unrepaired.  With M1's repair the settlement reads
  PARTIAL with the failed links named as `HOLONOMY-CONSISTENT` and
  (at the primary readout) `TARGETS-HIT`, or with the targets link
  explicitly re-labelled.  I do not ask for the verdict to be
  reversed — I ask for the qualifier that the unit's own arena
  already implies.

**K4 — THE QUANTUM-SHAPE CLAIMS: the eq. 22 refutation is ROBUST to
the padding.**  I re-ran the test under four conventions on the union
of the three cuts' supports:

| padding | (1,2,3) | (1,2,4) | (1,3,4) | (2,3,4) |
|---|---|---|---|---|
| identity (U1's, the unit's) | 36 neg, min −1/97 | 104 neg, min −5/97 | 108 neg, min −1/18 | 164 neg, min −1/128 |
| **cyclic** (unrealised labels permuted by a fixed cycle) | **36 neg, min −1/97** | **104 neg, min −5/97** | **108 neg, min −1/18** | **164 neg, min −1/128** |
| uniform (unrealised column → uniform) | first transfer SINGULAR | SINGULAR | SINGULAR | SINGULAR |
| marginal (unrealised column → the cut marginal) | SINGULAR | SINGULAR | SINGULAR | SINGULAR |

Column sums are exactly 1 in every non-singular case.  So: the
**conclusion** — no interpolant of eq. 22's form exists at any of the
four non-degenerate triples — survives all four conventions; the
negative-entry **counts** are invariant under a genuinely different
permutation padding (they are carried by the realised block); and
under the two mass-spreading paddings the candidate does not exist at
all, because the first transfer is singular.  The paper's caution (the
padding is a CONVENTION and the verdict is quoted with it) is
warranted and can now be strengthened: *recommended addition to §5.4* —
"the refutation is robust: a permutation padding returns the identical
negative-entry counts, and under mass-spreading paddings the first
transfer is singular, so eq. 22's candidate does not exist at all."
The rest of the quantum-shape battery is reproduced and honestly
scoped: the non-Markov census is 4 of 10 with failures at
[34, 112, 12, 12] cells and REC exactly lumpable at 10 of 10; the U3
census is 5 N/A-SHAPE / 4 S-FAIL-DS / 1 S-PASS with the one pass the
known degenerate $J/8$ (column-constant, unistochastic at every $n$,
certificate verified in exact integer arithmetic — I rebuilt the
Sylvester check: 0 nonzero in $HH^{T}-8I$, 0 mismatches); the 44
squares split 44 curvature (Γ-holonomy non-unit at 44 of 44, spectrum
reproduced) and 44 descent-obstruction (endpoints in different carrier
classes at 44 of 44, so Γ has no loop there).  **What the paper may
claim at citable scope:** that Γ is *not* of Barandes' form anywhere
its shape admits the question (never doubly stochastic away from
renewals, with the exact $L_1$ price), that it is non-Markov at 4 of
10 depth-cut triples where the record chain is exactly lumpable, and
that it admits no eq.-22 interpolant at those four triples under every
padding tested.  It may claim nothing about quantumness from the
curvature — and it claims nothing (W-CROSS count gated at 0,
reproduced).

**K5 — INSTRUMENT: PASS WITH THE FIXES IN D1/D2.**  88 gates, 33
must-pass, 0 failures, 36 mutants; the two never-falsified gates are
`G-KERNEL-PROPER` and `G-CUT-ADDITIVITY`, both THEOREM-PASS, and I
verified both waivers are correct: properness is an identity of the
definition $G(h,r) := \sum_e q\,G(h+e,r-1)$ (0 violations over 4564
kernel entries), and cut-mass-1 follows by induction (measured 1 at
all five cuts).  Both waivers are honest.  The verdict string rebuilds
byte-for-byte from my own censuses (§5).  All 23 byte anchors and all
9 path-value anchors verify independently.  Era injection classes are
all present (verdict ×5, table, render, path-drift, quotation-meaning)
and the verdict mutants are genuine.  The coverage defects are D1 (two
vacuous mutants, three weak) and D2 (an undisclosed worktree read).
Two plain runs on scratch copies were executed for byte-identity;
result recorded in §6.

---

## 4. K3 — THE BETWEEN-CARRIER RESULT (my decisive contribution)

I built the quotient lattice explicitly, from the pinned d74
abstractions plus three constructions from pinned parts, and measured
descent and holonomy on each.

**(a) The protocol's premise is refuted by measurement.**  PORT (65),
STATE (125) and MULT (578) do **not** sit between MENU and REC.  The
refinement relation, measured on all 100 ordered pairs:

* **MENU refines PORT** — PORT is strictly *coarser* than the carrier,
  not between it and REC;
* **MULT and STATE are incomparable with MENU** — neither refines the
  other (MULT refines STATE; neither refines MENU or PORT);
* REC refines every rung, and the meet MENU ∧ REC **is** REC (2477
  classes), so the interval $[\mathrm{MENU}, \mathrm{REC}]$ contains
  none of the three named rungs.

The "ladder" of d74 is a list of six abstractions, not a chain.

**(b) The interval is not empty, and it contains a carrier with BOTH
descent and holonomy — and that carrier is already pinned.**  d74's own
**coarsest weighted congruence**, which I rebuilt by partition
refinement from the menu partition (5 rounds) and which returns
**185 classes, reproducing d74's committed AB4 value exactly**.

| carrier | classes | in [MENU, REC]? | horizon potential descends | multi-valued labelled edges (weight / target) | q-reading | k-reading | Γ-reading | CK |
|---|---|---|---|---|---|---|---|---|
| REC | 2477 | endpoint | **yes** | 0 / 0 | flat (obstr 0, self-loops 0) | flat | flat | 10/10 |
| **CONG** | **185** | **yes** | **yes** | **0 / 0** | **⟨2,3⟩ rank 2; closes 1362; DEF-close 44; self-loops 44; obstr 44** | **⟨2,3⟩ rank 2** | {2,3,13} rank 3 | **10/10** |
| MENU+G | 181 | yes | yes | 0 / 4 | ⟨2,3⟩ rank 2; closes 1394; DEF-close 44; obstr 44 | ⟨2,3⟩ rank 2 | {2,3,13,19} rank 4 | 8/10 |
| MENU+G(·,2) | 162 | yes | yes | 0 / 132 | ⟨2,3⟩ rank 2; obstr 44 | {2,3,5,13} rank 3 | rank 3 | 10/10 |
| MENU | 113 | endpoint | **no (4 classes)** | 0 / 4 | ⟨2,3⟩ rank 2; closes 1402; obstr 44 | {2,3,5,13} rank 3 | rank 7 | 6/10 |
| PORT | 65 | **no — coarser than MENU** | no (2) | 0 / 4 | ⟨2,3⟩; closes 1458; obstr 44 | rank 3 | rank 9 | 6/10 |
| STATE | 125 | **no — incomparable** | no (6) | 4 / 0 | ⟨2,3⟩; closes 1546; obstr 0; self-loops 88 | rank 3 | rank 8 | 6/10 |
| MULT | 578 | **no — incomparable** | no (12) | 8 / 0 | ⟨2,3⟩; closes 1546; obstr 0; self-loops 88 | rank 3 | rank 7 | 6/10 |
| SEQ | 3969 | above REC | yes | 0 / 0 | trivial (no square closes) | trivial | trivial | 10/10 |

(The MULT / STATE / PORT / MENU / SEQ / REC rows reproduce d74's
committed ladder table column for column — μ-descent 514/578, 84/125,
24/65, 44/113; menu-descent 492/578, 103/125, 29/65, 113/113;
multi-valued edges 8, 4, 0, 0; sq-close 1546, 1546, 1458, 1402;
DEF-close 88, 88, 44, 44; cycle rank 0, 0, 80, 134.)

**On CONG-185:**
* the horizon potential descends at every horizon, so the horizon
  kernel descends — **the lift that forced the readout declaration on
  MENU is not needed**;
* the weighted menu descends 185/185 and there are **0 multi-valued
  labelled edges in both weights and targets** — CONG is a genuine
  congruence, which MENU is not (MENU carries **4 multi-valued
  labelled targets**, a fact the d74 ladder's "multi-valued edges 0"
  column does not report because that column counts weights);
* all **44 curvature-type defective squares still close**, with the
  same 44 non-unit self-loops and obstruction 44, and the q-group is
  exactly **⟨2,3⟩**;
* **the k-reading collapses onto the q-reading: ⟨2,3⟩, rank 2.  The
  enlargement that made this unit's settlement PARTIAL disappears.**
* the class chain is **exactly lumpable: CK divides at 10 of 10
  triples** — the carrier's non-Markov finding is a MENU artefact, not
  a transport fact;
* dims per cut are [1, 5, 17, 49, 113], so the successor is cheap.

**What does not go away on CONG:** the constructed family's own
aggregate holonomy is still an enlargement (primes {2, 3, 13}, rank
3), and the occupancy/count readouts still differ at **1188 of 1188**
cells — indeed they differ at 100% of cells on *every* carrier I
tested including REC (10897/10897).  So the readout fiber is a fiber
of the **construction scheme**, not of the carrier, and descent does
not collapse it.  §4's "the potential does descend on REC, which is
why the control behaves" is right about the potential and does not
remove the readout choice.

**(c) The mechanism, as a theorem.**

> **LEMMA.**  If $G(\cdot, r)$ is class-constant on a quotient $V$,
> then $r_k = r_q$ on every exchange square that closes in $V$.

*Proof.*  $r_k / r_q = G(h e_A e_B, r-2)/G(h e_B e_A, r-2)$ — I verify
this as an identity on **all 1546** closed squares, factor spectrum
{64/65: 6, 1: 1538, 65/64: 2}.  A square closes in $V$ exactly when
its two endpoints, which are at the same depth, lie in one class, on
which $G(\cdot, r-2)$ takes one value.  Hence the factor is 1. ∎

*Measured corroboration:* 2756 closing squares across the two
descending carriers, **0 exceptions**; the 8 squares carrying 64/65
and 65/64 are all at base depth 0, close in MENU (8/8) and PORT (8/8),
and close in **none** of CONG, MENU+G, REC; and the two values are
exactly the ratio of the two horizon potentials {4, 65/16} on the four
non-descending depth-2 classes, since $65/64 = (65/16)/4$.

*Consequence for the head:* the enlargement to {2, 3, 5, 13} is not a
property of "the horizon normalization" as such — it is caused by the
carrier's failure to descend, and it vanishes on every descending
refinement.  The paper's §5.2 prose identifies the cause correctly
("the potential is the quantity measured above *not* to descend"); the
**head segment** should carry the qualifier, e.g.
`K-PRIMES-{2,3,5,13}-RANK-3-ON-A-NON-DESCENDING-CARRIER`.

**(d) The successor's address.**  Re-run the nine-test battery on
**CONG-185** — a pinned object, cheap, in the interval, with the
potential descending, the same 44 defective self-loops, and a
holonomy that already agrees with ⟨2,3⟩ at two of the three readings.
The open question that survives is the right one and is sharper than
the one this unit leaves: *is the constructed family's own aggregate
holonomy (rank 3 on CONG) removable at all, or is coarse-graining
curvature a third phenomenon distinct from both q-curvature and
descent-obstruction?*

---

## 5. The verdict, rebuilt from my own censuses (K5)

Every segment of the emitted head reconstructs from my independent
measurements: carrier 113 classes at (A,B) d ≤ 4, 5 cuts, dims
1×5×13×45×113, 10 pairs, column-stochastic exact, 23 sha-pinned
sources (23/23 verified); TARGETS = hit at COUNT, missed at OCCUPANCY;
HOLONOMY = DEVIATE-AT-BOTH with D74 {2,3} rank 2 reproduced, k
{2,3,5,13} rank 3, Γ {2,3,5,13,19,97,389} rank 7, REC flat at all
three; SCREEN = N/A-SHAPE 5, S-FAIL-DS 4, S-PASS 1; KERNEL induced,
n-indexed at occupancy, leg-indexed at count; MOVER blocked at
referent; INTERPOLANT non-Markov at 4 of 10 with REC exactly lumpable;
44 close + 44 not-a-loop; MOTIVATION 4 forced / 1 stabilizer-fixed / 5
free; SETTLEMENT PARTIAL.  **The one segment my censuses do not
support as written is `MOTIVATION-…-FIBER-2` (M2) and the unqualified
`targets hit: True` in the settlement table (M1).**

---

## 6. Byte-identity, hashes, and discipline

**Two plain runs, executed on a scratch copy of the unit** (only the
two output paths redirected, so the repo was never written): the
outputs are **byte-identical to each other**, the receipts are
**byte-identical to each other**, and run 1's output file is
**byte-identical to the committed `gmain_output.txt`**
(`b2b45be500b7`).  The two receipts differ from the committed one only
in `source_sha256`, which records the running file's own digest and
therefore moves with the two redirected path strings; every other key
is identical.  Both runs exit 0.  Determinism and reproducibility are
confirmed at the strongest available standard: **an independent
machine reproduces the delivered artifact byte for byte.**


**Frozen hashes re-verified after all hostile work:** paper
`d85a629a9378`, code `51c3b4cf3f3c`, output `b2b45be500b7`, receipt
`974f36b1251a` — all four unchanged.  Pinned sources re-verified:
d42b1 `576275d55ecf`, d74 note `0180e21c7127`, d74 code
`bb852161aced`, d74 out `b5a9d50f9573`, R6b′ register `f6c11163c77d`.
No repo write but this file; no import from the unit; every
cross-unit read through `git show <sha>:`; all hostile runs on scratch
copies.

**Recomputation count: 405.**
