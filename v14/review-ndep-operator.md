# NDEP (PAPER-39) — K1 OPERATOR REVIEW

**Seat:** K1 OPERATOR, three-seat hostile panel.  **Object:** `v14/paper-39-ndep.md`
(25bea1eddd3a), `v14/code/ndep_exact.py` (d83df6c1e07d), `ndep_output.txt`
(efa2987ef6a7), `ndep_receipt.json` (3f5639a9146d), pin `v14/note-ndep-pin.md`
(2ff14505f18f).  All five digests verified at open and at close.
**Method:** a from-scratch rebuild of the arena grammar and all five laws in
independent code (`k1_arena.py` + four drivers, scratch only), sharing no code,
no inputs and no typed literal with `ndep_exact.py`; plus provenance checks at
`git show f4172ea`, an independent execution of the unit's own `--selftest` and
of all 27 declared falsifiers, and a numeral sweep of the paper.
**Repo writes:** this file only.  Git read-only.

---

## GRADE: ACCEPT WITH FIXES (AWF)

**Zero false numbers.**  Every substantive numeral the paper publishes reproduced
in my independent rebuild — all five q = 3 fidelity counts, the whole n = 4
corpus and lattice, 45/48 and 3, the 53-prefix route census, 21,080/0/2,064 at
n = 16, 5 = 5 set equality, 8-of-16 at q = 4, {1..7}|{2,4,6}|{3,6} and {4,8},
539/144,991/11,928/133,063/2,731/142,260, 45/3 at m = 2,3,4,5, incidence 48
against budget 16, and the sharpened floor 2|4|6.  The numeral sweep of the
paper found nothing I could not reproduce.  Provenance is clean: the two FAC
digests and all six frozen FAC constants verify at commit `f4172ea`; both AID
digests verify; all six verbatim quotations are the parent's own bytes at the
lines I located.  All 27 falsifiers died at their declared gates with artifacts
unchanged when I ran them myself.

**The verdict words survive.**  I re-derived all seven transport tables from the
paper's own declared rule and reproduced every emitted word; PORTABLE-3-OF-5
stands on the procedure as run.

**Why not A.**  Nine majors, all instrument-level, none of which moves a
measured number and two of which move a headline.  Two gates cannot fail on any
faithful implementation (the naming routes and the coin residue channel), so one
of the three "portable" verdicts and the whole coin leg are carrying no
information.  Two legs of the four-leg division-forcing criterion never bind, so
"the census is blind to m" is forced rather than found.  The head's `6 OF 6`
denominator is a typed literal over a hand-listed set that omits the one numeral
the unit measured NOT to be q-carried.  A headline count (21,080) is a single
history behind a window declaration that does not say so.  And the n = 9
**attained** floor — the crux of the paper's sharpest table — is anchored at the
**counting bound's** JSON path, against a gate whose own text says "never minus
the bound", while the correct anchor sits unused in the parent's receipt.

---

## 1.  WHAT I REBUILT, AND WHAT AGREED

Independent constructor, independent GF(4), independent grouping enumeration,
independent Young/brute-force routes, independent legs, independent transport
procedure.  Agreement, object by object:

| leg | published | K1 rebuild |
|---|---|---|
| q = 3 fidelity (groupings/sat/strict/flat/window) | 280 / 36 / 72 / 276 / 600 | 280 / 36 / 72 / 276 / 600 |
| q = 3 C1FAN, C2 (parent's own) | 1,944 / 5,184 | 1,944 / 5,184 |
| n = 4 groupings / saturating / cells / max incidence | 3 / 2 / 8 / 4 | 3 / 2 / 8 / 4 |
| n = 4 corpora C1/C1FAN/C2/C3, total | 2 / 8 / 4 / 34 = 48 | 2 / 8 / 4 / 34 = 48 |
| n = 4 actor lattice | 15 | 15 |
| naming: prefixes, mismatches, forced, chart | 53 / 0 / 45 / 3 | 53 / 0 / 45 / 3 |
| chart = constant class (ROW³, COL³, DIA³) | set-equal | set-equal |
| stabilizer census | {1: 45, 4: 3} | {1: 45, 4: 3} |
| crystallization n = 4 (C1, C1FAN, C2) | 3 | 3 |
| attained floor n = 4 | 2 | 2 |
| redundant event; time when moved to the end | 2 of 2; 2 | 2 of 2; 2 |
| n = 16 class tuples / covering / time / floor | 256 / 24 / 7 / 6 | 256 / 24 / 7 / 6 |
| counting bound vs sharpened bound at q = 2,3,4 | 2,4,4 vs 2,4,6 | 2,4,4 vs 2,4,6 |
| n = 16 route window (1,240 perms) | 21,080 / 0 / 2,064 | 21,080 / 0 / 2,064 |
| coset menu: survivors, subgroups, cosets, set equality | 5 / 5 / 5 / True | 5 / 5 / 5 / True |
| subgroups of T and F_q-subspaces at q = 2,3,4 | 5,6,67 and 5,6,7 | 5,6,67 and 5,6,7 |
| declared links generate at q = 2,3,4 | 4/4, 9/9, 8/16 | 4/4, 9/9, 8/16 |
| ladder L = 1,2,3 at n = 4; L = 4 at n = 16 | {1..7},{2,4,6},{3,6}; {4,8} | identical |
| coin family, pairs, both m-splits | 539 / 144,991 / 11,928+133,063 / 2,731+142,260 | identical |
| census at m = 2,3,4,5 | 45 / 3 each | 45 / 3 each |
| leg pass counts | 240 / 57 / 720 | 240 / 57 / 720 |
| union of admissible | 4 | 4 |
| q = 4 saturation witness incidence | 48 vs budget 16 | 48 vs budget 16 |
| all seven transport words | as published | as published (one exception, M5) |
| five transport control arms | as published | as published |

I also independently closed two things the unit only cited or left open, and both
went the unit's way:

- **The parent arena's own ladder, measured.**  The unit carries the n = 9 first
  rung 3 as a frozen declared constant and cross-checks it only against
  `Arena(3).L`, i.e. against the declaration itself.  I ran the exhaustive
  homogeneous-ladder search at q = 3 over **all 36** saturating groupings:
  achievable budgets `{3, 6}`, first rung **3**.  Restricted to the
  parallel-class window: `{3, 6}` also.  So "the modulus is L" is true at the
  parent arena, and now measured rather than declared.
- **The 2,627,625 and 16! arithmetic** and the exhaustive maximality check at
  q ≤ 3 (max incidence 4 over all 3 groupings at q = 2; 9 over all 280 at q = 3)
  both hold.

**Recomputations: 124.**  (Counted honestly: 118 quantities recomputed from
scratch and compared object-for-object, plus the 5 object digests and the
`f4172ea` provenance set.)  **Discrepancies found: 0 numerical, 9 instrumental.**

---

## 2.  MAJORS

### M1 — G-LAW4-COIN cannot fail: "the record enters exactly mod m" is an identity of the operator's own definition, not a measurement

`coupled_columns` (ndep_exact.py:887–888) stores the phase as
`e = rec[...] % m`.  The column tuple therefore *is* a function of `rec mod m`
and of nothing else that varies with the record.  So `congruent mod m` ⟺
`identical one-step operator` holds for **any** integer vectors whatsoever; the
144,991-pair, 0-mismatch census is a tautology of the code.

**Establishing measurement (mine).**  I re-implemented the operator and re-ran the
exact pair classification on 120 **arbitrary random integer vectors** with no
relation to the arena, the corpus, or the record at all:
`m = 2 → 0 mismatches; m = 3 → 0 mismatches; m = 5 → 0 mismatches`.  A gate
that returns 0 on random noise is not reading the arena.  (I also reproduced the
published 539/144,991/11,928/133,063 and 2,731/142,260 exactly, so the numbers
are right; it is their content that is empty.)

MUT-COIN does die at the gate — but it dies by setting the operator's modulus to
1000 while the congruence test still uses m, i.e. it breaks the wiring, not the
claim.  A falsifier that can only fire on a mis-wired implementation does not
make the gate falsifiable.

**Exact repair (liftable).**  Either (a) carry the phase as an exact m-th
cyclotomic integer (`z^e` with `z` of order exactly m, e.g. an integer vector in
`Z[z]/(Φ_m)`), so that the ⟸ direction — *incongruent ⇒ different* — becomes a
real measurement of the root's primitivity and can fail when it is not primitive;
or (b) demote the leg: delete "Both halves of that sentence are measured" from
§6 and replace with "The first half is a DEFINITIONAL property of paper-20's
coin as this unit implements it — the operator reads the record only through its
residue — and is disclosed, not measured; the second half, the census's
blindness, is measured", and strike the 144,991 from the verdict fence.

### M2 — The four-leg criterion is a two-leg criterion on this corpus: legs 3 and 4 never bind, so the census could not have moved with m

**Establishing measurements (mine), over all 15 × 48 = 720 (partition, history)
pairs.**  Leg-3 passes **720 of 720 — zero failures**.  Leg-4 is reached at 51
pairs and passes **51 of 51 at both coin orders at m = 2, 3, 4 and 5 — zero
failures**.  Running the census with **legs 1 ∧ 2 only** returns exactly
**45 unique / 3 non-unique**, the published result.  The structural reason is
also measurable: every corpus record vector is constant in the site for each
link (verified on all 48 histories), because at n = 4 every grouping is a
parallel class, so leg-3 has nothing to cut.

The receipt publishes `leg_pass_counts` for legs 1–3 only — leg 4 has no row at
all — and nowhere states that leg 3's failure count is zero.  §7 presents the
criterion as "the geometry, the history, the record and the one-step dynamics,
each a per-object predicate".  Consequently CL-COIN ("the census is blind to the
coin's modulus") and the §6 sentence "the whole division-forcing census is
re-run at m = 2, 3, 4 and 5 and returns 45 unique and 3 non-unique every time"
are *forced by construction*: no leg that reads m ever binds.

**Exact repair.**  Add leg 4 to `legcount` (it is currently never counted) and
publish, in the receipt and in §7: `leg3 failures 0 of 720`, `leg4 evaluated at
51, failures 0 at m = 2,3,4,5, coin-order disagreements 0 of 51`.  Replace §6's
"And m is unconstrained: the whole division-forcing census is re-run …" with
"And the census cannot see m: the only leg that reads it, leg 4, is admissible
at every one of the 51 pairs that reach it, at every declared m, so the counts
could not have moved.  The freedom is therefore a statement about this census's
reach and not about the coin."

### M3 — LAW 1's transport re-measures a set-theoretic identity; G-LAW1-ROUTES cannot fail

σ fixes every event setwise ⟺ for every x and every F, `x ∈ F ⟺ σ(x) ∈ F` ⟺
σ preserves the participation signature ⟺ σ lies in the Young subgroup of the
signature partition.  This holds for **any** family of subsets of any finite
set; the arena plays no part.

**Establishing measurement (mine).**  Route A vs route B on **400 random
arbitrary event families** at n = 4 (random subsets, random sizes, random
lengths, not arena objects): **0 mismatches**.  And over all 87 distinct prefix
*sequences* of the real corpus (not just the 53 multisets): 0 mismatches.

The parent already knows this.  AID §(routes) states and *proves* it:
"Route B is a theorem … Fixing every event setwise is the same as fixing every
atom of the Boolean algebra the events generate … The atoms are exactly the
signature blocks."  So `NDEP-LAW-IN-N-NAMING` is not an arena measurement, and
one of the three legs of `PORTABLE-3-OF-5` is vacuous.  §3 hints at this ("The
statement contains no numeral at all, which is already a hint") but never says
the comparison cannot fail.

**Exact repair.**  Keep the leg as a regression check but say what it is.  In §3
after the first sentence: "The parent proved this by a Boolean-algebra argument
that mentions no arena at all — the atoms of the algebra the events generate are
exactly the signature blocks — so the routes agree for any family of subsets
whatever, and the measurement below is a fidelity check on this unit's
constructor rather than a test of transport.  What the n = 4 arena can and does
decide is the CHART SET and its count."  And add a receipt row
`law1_naming.routes_leg_is_arena_free: true` so the head's PORTABLE count can be
read with that stamp attached.

### M4 — The head's "6 OF 6" denominator is a typed literal over a hand-listed set that omits the one non-q-carried numeral

`ndep_exact.py:2536–2542`: `numerals_q_carried` is a `sum` over a literal tuple
of six words — `law1 chart`, `law2 time`, `law2 floor`, `law3 count`,
`law4 ladder`, `law5 count` — and `"numerals_tested": 6` is typed.  The unit
builds a **seventh** transport table, `law2["offset"]`, whose emitted word is
**LAW-IN-N**, and excludes it from both.  The same paper publishes that word in
its own crystallization fence — "OFFSET ONE AT ALL THREE (LAW-IN-N)" — and then
says in §9 "all 6 numerals tested … are carried by the square root or by the
declared link count", and closes with "what moves with the arena is every number
in it".  The unit's own offset row is a number in a law that does not move with
the arena.

**Establishing measurement (mine).**  I rebuilt all seven transport tables from
the declared rule and reproduced every published word; the offset table is the
only one excluded from the head's denominator, and it is the only one that is not
NEEDS-3 as published.

**Exact repair.**  Derive the denominator: `"numerals_tested": len(TABLES)` over
the list the run actually builds (7), and publish `6 of 7` with the exception
named.  Replace §9's last two sentences with: "Six of the seven numerals tested
are carried by the square root or by the declared link count.  The seventh — the
offset between the schedule time and the information floor — is one at all three
arena points and is stamped UNDISCRIMINATED, because a constant agrees with every
candidate reading at once; it is the one number in this corpus that does not move
with the arena, and it is published as such rather than dropped."

### M5 — The offset's transport table does not use the declared uniform rule, which §8 says is applied to every law

§8: "The n-only reading is fixed by rule and not fitted per law … the n-only
reading of every law's numeral is the corpus's own n-only quantity — the counting
bound — offset by whatever constant reproduces the parent's numeral at n = 9.
The same rule is applied to all five laws, so none of them gets a friendlier
reading than another."  `ndep_exact.py:1852–1859` builds the three offset rows
with `t_literal = t_n = t_q = 1` hard-coded; `t_n_reading` is never called for
them.

**Establishing measurement (mine).**  Applying the declared rule gives
`t_n = ⌈log₂n⌉ + (1 − 4)` = **1, −1, 1** at n = 9, 4, 16 against measured
1, 1, 1 — so the rule-applied offset emits **NEEDS-3 (DISCRIMINATED)**, not
LAW-IN-N (UNDISCRIMINATED).  I reproduced both outcomes from the same procedure.

Either branch is defensible; what is not defensible is asserting uniformity while
exempting one table.  Note the interaction with M4: under the rule the head would
honestly read **7 of 7**; under the exemption it must read **6 of 7**.

**Exact repair.**  Pick one and say so.  Preferred: keep the exemption (a
constant is genuinely blind to the rule) and amend §8 to "The same rule is
applied to every numeral whose parent value is a size.  The offset is not a size
but a difference of two, and the counting-bound rule returns a negative reading
for it at n = 4; its three candidate readings are therefore declared equal to the
parent's constant, which is why its row is stamped UNDISCRIMINATED and excluded
from the aggregate."  Add `law2.offset.rows[*].reading_rule: "DECLARED-CONSTANT,
NOT THE COUNTING-BOUND RULE"` to the receipt.

### M6 — The n = 16 naming window is ONE history; neither the paper nor the window declaration says so

`ndep_exact.py:1697`: `Href = cov16[0][1]`.  The 21,080 comparisons are
17 prefixes × 1,240 permutations of the **single** class tuple ROW|COL|DIA|ANT —
one of 24 covering tuples, of 256 class tuples.  W-N16-PERM declares only "all
transpositions and all 3-cycles of the sixteen actors, **at every prefix**";
§3 says "1,240 permutations at every prefix, 21,080 comparisons **in all**";
§9 says only that route A "runs on a permutation window because S_16 is not
filterable".  The referent binding NB-COMPARISON binds 21,080 to the bare noun
"comparisons".  G-WINDOWS-DISCLOSED passes because the *permutation* window is
declared; the *history* window is not declared anywhere.

**Establishing measurement (mine).**  On `cov[0]` I reproduce 21,080 / 0
mismatches / 2,064 positive exactly.  Over **all 24** covering class tuples:
**505,920 comparisons, 0 mismatches, 49,536 positive** — seconds of compute.

**Exact repair.**  Run the 24 and publish 505,920 / 0 / 49,536; §3 becomes
"1,240 permutations at each of the 17 prefixes of each of the 24 covering class
tuples — 505,920 comparisons, 0 mismatches, 49,536 of them landing inside the
stabilizer".  If the single history is kept for cost reasons, amend W-N16-PERM to
"… at every prefix of ONE declared covering class tuple, ROW|COL|DIA|ANT; the
other 23 are not taken", and bind NB-COMPARISON to "comparisons on that tuple".

### M7 — The n = 9 ATTAINED floor is anchored at the COUNTING BOUND's path, against a gate whose own text forbids exactly that

`PATH_ANCHORS` P-FLOOR (`ndep_exact.py:138–140`) reads
`crystallization/information_floor/counting_bound_ceil_log2_actors` = 4.  That
single read then supplies **both** the "attained floor" and the "counting bound"
cells of the n = 9 row of §4's table (`floor_rows[0]`: `measured = parent_floor`,
note "PARENT ANCHOR: the attained information floor at n = 9"), **and** the n = 9
offset (`offset.parent_n9 = parent_time − parent_floor`).  The gate text of
G-LAW2-OFFSET reads: "The offset is the schedule time minus the ATTAINED floor —
**never minus the bound**."  At n = 9 it is exactly time minus the bound.  The
whole thesis of §4 is that these are two different objects that diverge at
n = 16; the n = 9 row conflates them at the level of provenance.

The correct anchors exist in the parent's committed receipt and are unused:
`counts/information_floor` = 4;
`crystallization/information_floor/minimal_event_subset_C1` = {"4": 72};
`crystallization/information_floor/minimal_event_subset_forced_C3` = {"4": 596}.
(AID's prose likewise separates them: "That floor is a counting theorem, and it
is attained: the smallest event subset that forces identity has size 4 at all 72
R = 3 histories and at all 596 forced R = 4 histories.")

No number moves — both are 4 at n = 9.  The provenance is wrong, and MUT-OFFSET
does not catch it because it mutates only the n = 16 row (`off16`).

**Exact repair.**  Split P-FLOOR into two anchors:
`P-FLOOR-BOUND` at `crystallization/information_floor/counting_bound_ceil_log2_actors`
(consumer: the bound column) and `P-FLOOR-ATTAINED` at
`counts/information_floor` (consumer: G-LAW2-FLOOR's measured cell and
G-LAW2-OFFSET's n = 9 row).  Add a mutant `MUT-OFFSET-N9` that takes the n = 9
offset as time minus the bound and requires it to die at G-LAW2-OFFSET, so the
gate's own sentence acquires a falsifier.

### M8 — "12 distinct event sets" is a count of event MULTISETS; as sets the corpus carries 7

`ndep_exact.py:2496–2498` builds the key as `tuple(sorted(events of H))` — the
events of a history **with repetition** — so a ROW|ROW|ROW history contributes a
3-fold multiset, not a set.  The published field is named
`distinct_event_sets` and §2.1 and §7 read "48 driven histories, over 12 distinct
event sets" / "48 schedules over 12 distinct event sets".

**Establishing measurement (mine), over the 48 histories.**  Distinct event
**sets** = **7**.  Distinct event **multisets** = 12.  Distinct event
**sequences** = 33.  The parent's homonymous count is a genuine set count — AID
§2: the seed fan is "1,944 histories, 432 distinct sequences over 12 distinct
event sets", where the 12 are the unordered strict triples — so the analogue
being drawn is not the parent's quantity.

The same defect, smaller: **"53 distinct prefixes"** is a distinct-prefix-multiset
count (`ndep_exact.py:1551–1552`); distinct prefix *sequences* number 87.  The
dedup is sound for the test — the stabilizer reads only the event set — but the
noun published is "prefixes", and #87/§15 bind counts to referents.

**Exact repair.**  Rename the receipt key to `distinct_event_multisets` and
publish `distinct_event_sets: 7` beside it; §2.1 becomes "48 driven histories,
over 12 distinct event multisets and 7 distinct event sets".  In §3 and
NB-PREFIX, "53 distinct prefixes" becomes "53 distinct prefix event-multisets
(87 distinct prefix sequences; the stabilizer reads only the multiset, so the
comparison is taken once per multiset)".

### M9 — Two published counts are typed literals, not measurements

`"coin_order_disagreements": 0` (`ndep_exact.py:2306`) is typed: `admissible_actor`
computes `g` and `d` and returns `bool(g and d)`; the disagreement is never
counted anywhere.  `"numerals_tested": 6` (`:2542`) is typed (see M4).  The
standing discipline is explicit: "Counts computed, never typed."

**Establishing measurement (mine).**  The coin-order disagreement count really is
0 — I measured it at 0 of the 51 pairs that reach leg 4, at m = 2, 3, 4 and 5 —
so no number is wrong.  But the artifact vouches for a figure it did not measure,
and no falsifier can reach a literal.

**Exact repair.**  Return the two leg-4 booleans from `admissible_actor` into a
counter and publish the measured disagreement count with its denominator
(`0 of 51`); derive `numerals_tested` from the table list.  Add a mutant that
forces one coin order to differ and requires G-LAW5-CENSUS to die.

---

## 3.  MINORS

- **m1 — The L-sweep cannot separate L from the number of saturating groupings.**
  At n = 4 the two are numerically identical at every row of the sweep:
  `(L, #saturating) = (1,1), (2,2), (3,3)` (measured).  The paper asserts "The
  modulus is the declared link count L" on evidence in which a rival carrier is
  indistinguishable.  I closed it independently — at q = 3 with all 36 saturating
  groupings the achievable set is {3, 6} and the rung is 3 = L ≠ 36 — so the
  claim is **true**, but the unit's own instrument does not establish it.
  *Repair:* run `homogeneous_ladder` at q = 3 over the 36 (it costs seconds) and
  publish it as the row that kills the #saturating reading; add "#saturating
  groupings" as a fourth named rival in the carrier table.
- **m2 — The field characteristic is never computed.**  `carrier_rows`
  (`:2126–2127`) sets `equals_characteristic` to the *same expression* as
  `equals_q` (`first_rung == 2`), and `characteristic_is_fixed_at: A.q` (`:2188`)
  publishes q under the name "characteristic".  Correct at q = 2 only because
  char = q = 2 there; the same code at q = 4 would publish "characteristic 4".
  Since the headline claim is "the modulus is neither √n nor the characteristic",
  the characteristic should be an object, not an alias.  *Repair:* add
  `Plane.characteristic` (2 for q ∈ {2,4}, 3 for q = 3) and use it.
- **m3 — "reaches the budget" vs `== n`.**  §2.1 defines saturating as the weight
  "reaches the budget n"; the code uses equality.  I verified the two coincide at
  q ≤ 3 exhaustively (max incidence 4 over all 3 groupings at q = 2, 9 over all
  280 at q = 3) and diverge at q = 4, which §8 discloses.  *Repair:* write
  "equals the budget n" in §2.1 and add "at q ≤ 3 that is also the maximum, and
  §8 records that it is not at q = 4".
- **m4 — The two 45-of-48 fractions are one measurement.**  I verified the law-1
  CHART history set and the law-5 NON-UNIQUE history set are the **same three
  histories**; so §3's "45 of 48 force it" and §7's "45 histories admit the
  discrete partition alone" are one partition of the corpus with one cause (the
  history repeats a parallel class), published twice.  The parent ran an explicit
  control against exactly this reading ("this unit's own control against reading
  two equal counts as a mechanism").  *Repair:* one sentence in §7 — "the 45 here
  are the same 45 of §3: at n = 4 a history is chart, and non-unique, for the one
  reason, and the two fractions are not independent evidence."
- **m5 — The n = 4 C3 stratification is not published.**  Measured:
  crystallization on C3 is `{3: 25, 5: 6, never: 3}` and the attained floor is
  `{2: 31, never: 3}`.  §4 says only "constant across C1, C1FAN and C2".  The
  parent published its own C3 stratification in its head string
  (5:404|7:36|8:144|11:12|never:4).  Six n = 4 histories crystallize at **5** —
  the parent's own numeral — and the paper never says so.  It does not move the
  verdict (the n = 16 row is what discriminates), but the receipt has the datum
  and the paper suppresses it.  *Repair:* publish the C3 row in §4's table.
- **m6 — `--selftest` exercises one gate.**  I ran it: all three corrupted
  anchors die at **G-PROVENANCE**, the first gate, in 0.05 s; artifacts unchanged.
  The #82 contract is met literally.  *Repair:* add one selftest that corrupts a
  value *after* provenance (e.g. a path-anchor value) so a deeper gate is the one
  that fires.
- **m7 — The sealed artifact carries an empty sweep.**  `mutant_sweep: []`,
  `totals.sweep_rows: 0`; G-SWEEP-BOUND passes on zero rows in the committed run,
  and the ledger's "27 falsifiers 27/27" is not in the sealed object.  I ran all
  27 myself: **27/27 died at their declared gates, artifacts unchanged both
  digests** — so the claim is true and now independently confirmed.  *Repair:*
  either commit a `--sweep` run or publish
  `mutant_sweep: "NOT RUN IN THE COMMITTED RUN; taken separately"` so the gate is
  not a pass over nothing.
- **m8 — The n = 4 arena collapses a distinction the parent's grammar has.**  At
  q = 2 every grouping is a parallel class (3 of 3), so `saturating ⊂ parallel
  classes`; at q = 3, 36 saturate of which only 3 are declared classes.  Every
  n = 4 result about "saturating groupings" is therefore a result about parallel
  classes.  §2.1 notes the fact ("they are exactly the 3 parallel classes") but
  never draws the consequence.  It is what makes legs 3 and 4 inert (M2) and what
  makes m1's confound possible.  *Repair:* one sentence in §2.1 and a line in §9's
  scope paragraph.
- **m9 — The parent never published ⌈log₂n⌉ as an n-general formula.**  AID's
  V-FLOOR is explicitly about nine actors and four events, and AID says of the
  time that "The constant is a fact about the corpus's scheduling convention."
  §4's closing sentence handles this honestly ("The parent's statement was
  correct where it was made; its n-only generalisation is not"), so this is not a
  misquotation — but the reader of the fence "THE COUNTING BOUND ceil(log2 n)
  READS 4 AT n=16" should be told the formula is this unit's declared
  extrapolation, per §8's rule, and not a parent claim.  *Repair:* add
  "— this unit's declared n-only reading of the parent's nine-actor statement, by
  the rule of §8 —" after "the counting bound" at its first use in §4.

---

## 4.  WHAT THE HEADLINE LOOKS LIKE AFTER THE FIXES

Nothing in the measured record forces a different verdict, but three head
segments should change wording:

- `PORTABLE-3-OF-5` stands as a count of emitted words.  It should carry the M3
  stamp: one of the three portable laws (NAMING) is portable for a reason that is
  arena-free by proof, which the parent already gave.  The other two
  (COSET-MENU, DIVISION-FORCING) are real transport measurements.
- `EVERY ONE OF THE 6 TESTED NUMERALS IS q-CARRIED (6 OF 6)` must become
  **6 of 7** with the offset named, or **7 of 7** if the declared rule is applied
  uniformly (M4 + M5).  Under either branch the sentence "what moves with the
  arena is every number in it" is false as written and must be repaired.
- The mod-motif fence's coin half — "0 MISMATCHES OVER 144,991 PAIRS AT EACH OF
  m=2 AND m=3" — is a tautology of the operator's definition (M1) and should be
  removed from the fence or restated as a disclosure.  The ladder half is the
  unit's strongest result and survives intact; I strengthened it by measuring the
  parent arena's own rung (m1).

The sharpest genuinely-new object in the unit — **the sharpened floor
`min{k : 2^k ≥ n and kq ≥ Σ weights of the n lightest distinct k-vectors}`** —
is correct, is a valid lower bound for any event family of constant size q, and
I confirm it reads 2, 4, 6 at q = 2, 3, 4 and is attained at all three.  The
successor register's request that someone prove or break attainment at every q is
the right open.

---

## 5.  LICENSED REPLACEMENTS

Liftable verbatim; each is value-preserving except where noted.

1. **§6, coin half.**  Delete "Both halves of that sentence are measured." →
   "The first half is definitional and is disclosed as such: the coin this unit
   implements reads the record only through its residue mod m, so congruence and
   operator identity coincide by construction.  What is measured is the second
   half."  Strike "0 MISMATCHES OVER 144,991 PAIRS AT EACH OF m=2 AND m=3" from
   the `NDEP-NEEDS-3-MOD-MOTIF` fence.
2. **§6, census half.**  "And m is unconstrained: the whole division-forcing
   census is re-run at m = 2, 3, 4 and 5 and returns 45 unique and 3 non-unique
   every time." → "And the census cannot see m: leg 4, the only leg that reads
   it, is reached at 51 of the 720 partition-history pairs and is admissible at
   all 51, at every declared m and at both coin orders, so the counts could not
   have moved.  Re-run at m = 2, 3, 4 and 5 they do not."
3. **§3, first paragraph.**  Append: "The parent proved this by a
   Boolean-algebra argument that names no arena — the atoms of the algebra the
   events generate are exactly the signature blocks — so the two routes agree for
   any family of subsets whatever.  The comparison below is a fidelity check on
   this unit's constructor; what the n = 4 arena decides is the chart SET and its
   count."
4. **§3, n = 16 sentence.**  "21,080 comparisons in all" →
   "21,080 comparisons at the one declared covering class tuple ROW|COL|DIA|ANT"
   — or, preferred, run all 24 and write "505,920 comparisons in all, 0
   mismatches, 49,536 positive".  Amend W-N16-PERM to match.
5. **§9, last two sentences.**  As given in M4.
6. **§2.1.**  "That is 48 driven histories, over 12 distinct event sets." →
   "That is 48 driven histories, over 12 distinct event multisets and 7 distinct
   event sets."  Same in §7's E-24 paragraph.
7. **§4 table.**  Add the C3 row for n = 4 (`3: 25, 5: 6, never: 3`) or a
   sentence naming it.
8. **Code.**  `PATH_ANCHORS`: split P-FLOOR (M7).  `:2306` and `:2542`: derive
   the two typed counts (M9).  `:2262–2276`: count leg 4.  `:2126–2127, :2188`:
   compute the characteristic (m2).  `:1852–1859`: either call `t_n_reading` or
   stamp the exemption (M5).  Add `MUT-OFFSET-N9` and a coin-order mutant.

---

## 6.  CLOSING

**Grade: AWF.**  Nine majors and nine minors, all instrumental; no false number
found in 124 independent recomputations; all five object digests re-verified at
close; provenance verified at `git show f4172ea` and against AID's committed
receipt; all 27 declared falsifiers independently re-run and 27/27 on-target with
both artifacts unchanged.  The unit's central positive results — the constructor
fidelity, the coset-menu set equality, the division-forcing thesis, the
sharpened-floor formula, and the ladder's L-carrier — survive my rebuild, and two
of them (the parent-arena ladder rung; the full n = 16 route window) I closed
further in the unit's favour.  What does not survive unamended is the instrument's
account of what several of its gates are measuring.

Every finding above is a **candidate reading until adjudication**.

*K1 OPERATOR, 2026-08-15.  Scratch: `…/scratchpad/ndep_k1/` (< 5 GB).  Sole repo
write: this file.*
