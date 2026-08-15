# NDEP (PAPER-39) — K2 EFFECTUS REVIEW

**Seat:** K2 effectus (meaning, scope, motivation, the licensed claim, the
choice inventory, the successor register, walls compliance).
**Object, verified at open AND at close (sha256-12):**
paper-39-ndep.md `25bea1eddd3a` · ndep_exact.py `d83df6c1e07d` ·
ndep_output.txt `efa2987ef6a7` · ndep_receipt.json `3f5639a9146d` ·
note-ndep-pin.md `2ff14505f18f`.  All five unchanged across the review.
**Authority read:** the pin; HANDOFF-PROMPT.md §4/§9; AID's own published
floor sentences (paper-33 §5.1, read verbatim, not through NDEP's rendering);
note-aid-adjudication.md; FAC at frozen commit `f4172ea`.
**Recomputations:** 141, all in scratch, no repo write but this file.
**Grade: AWF — ACCEPT WITH FIXES.**  Every load-bearing measurement
reproduces from independent primitives; zero computed numbers move; the
defects are at the binding between measurement and the citable head, and two
of them are load-bearing on the aggregate this unit will be cited for.
Candidate reading until adjudication.

---

## 0. WHAT REPRODUCED (the positive half, stated first)

Rebuilt from nothing with different primitives — actors as 2-bit integers
under XOR for AG(2,2), GF(2)[t]/(t²+t+1) tuples for AG(2,4), set partitions
enumerated by recursion, stabilizers by brute force over
`itertools.permutations`, no import of `ndep_exact` — every load-bearing
number of this unit came back identical:

| quantity | NDEP | K2 independent | 
|---|---|---|
| groupings of 4 sites into 2 blocks of 2 | 3 | 3, and they ARE the 3 parallel classes |
| saturating at L = 1 / 2 / 3, max incidence | 1 / 2 / 3, max 4 = n | 1 / 2 / 3, max 4 |
| C1, C2 | 2, 4 | 2, 4 |
| naming theorem, route A vs route B | 0 mismatches / 53 prefixes | 0 mismatches / 86 prefixes (my corpus) |
| chart set | 3, constant-class, order 4 each | 3, constant-class, order 4 each |
| counting bound at n = 4 / 9 / 16 | 2 / 4 / 4 | 2 / 4 / 4 |
| sharpened floor at n = 4 / 9 / 16 | 2 / 4 / 6 | 2 / 4 / 6 |
| n = 16 class tuples, covering | 256, 24 | 256, 24 |
| n = 16 crystallization, attained floor | 7 at 24, 6 at 24 | 7 at 24, 6 at 24 |
| permutation window, comparisons, positives | 1,240 / 21,080 / 2,064 | 1,240 / 21,080 / 2,064 |
| subgroups of T at q = 2 / 3 / 4 | 5 / 6 / 67 | 5 / 6 / 67 |
| F_q-subspaces at q = 4 | 7 | 7 |
| declared links generate at q = 2 / 3 / 4 | 4/4, 9/9, 8/16 | 4/4, 9/9, 8/16 |
| q = 4 saturation witness | incidence 48, budget 16 | 48 vs 16, and H is not an F_q-subspace |
| coset menu at n = 4 | 5 survivors ≡ 5 coset partitions | set-equal, profiles (1,1,1,1) (2,2) (4) |
| ladder moduli at L = 1/2/3, n = 16 at L = 4 | 1 / 2 / 3, {4,8} | same, and derived by hand from the cell-count argument |
| coin family pairs | 144,991 | C(539,2) = 144,991; both m-splits sum exactly |
| groupings of 16 sites | 2,627,625 | 2,627,625 |

**The floor correction's datum is real and I reproduced it from scratch:** at
n = 16 the attained floor is 6 at every one of the 24 covering class tuples
while ⌈log₂16⌉ = 4.  The sharpened bound is a genuine necessary condition
(k events of size q distribute total incidence kq; n distinct binary
k-signatures cost at least the total weight of the n lightest distinct
k-vectors), not a fitted curve, and it reads 2, 4, 6 at the three points.

**Instrument.**  Off-tree run in a scratch mirror reproduced both artifacts
BYTE-IDENTICALLY (`efa2987ef6a7`, `3f5639a9146d`).  Unknown flag → exit 2;
unknown mutant → exit 2; `--selftest` corrupts all three byte anchors, each
dies at G-PROVENANCE, and the artifact hashes are unchanged before and after.
The full sweep runs **27 mutants, 0 off-target**, artifacts untouched.
G-ARTIFACT-INTEGRITY exercises its own failing direction on the same disk
bytes with one bit flipped.  All six FAC frozen constants verify EXACTLY
against `f4172ea` (receipt digest 240bad74217a, paper 2e9cbae8a83e — both as
declared), and the under-repair reason is carried in-paper.  This is a strong
instrument and I found no forged pass in it.

---

## 1. THE HEAD — WHICH LAWS COUNTED AS THE 3, AND IS THE AGGREGATE HONEST

**The 3 are naming, coset menu, division forcing.**  Laws 2 and 4 —
crystallization and mod motif — each got the word **NEEDS-3**.  The word list
the comparator derives from is
`['LAW-IN-N','NEEDS-3','LAW-IN-N','NEEDS-3','LAW-IN-N']`, and
`portable = 3` is genuinely computed from it, twice, by disjoint code, and
compared as complete strings.  The count is not typed and MUT-VERDICT proves
the gate bites.  **The arithmetic of the aggregate is honest.**

The *meaning* of the aggregate is not, in three respects.

### MAJOR-1 — the aggregate blends two different TESTS, which is the AID §2 disease

The three LAW-IN-N stamps are not the same measurement as the two NEEDS-3
stamps.  Laws 1/3/5 are scored on a **theorem-level test** — the receipt's
own `word_basis` for law 1 reads "THE THEOREM IS n-FREE AND HOLDS AT n = 4
EXHAUSTIVELY", and for law 5 "THE THESIS IS n-FREE AND HOLDS VERBATIM AT
n = 4".  Laws 2/4 are scored on the **transport procedure applied to a
numeral**.  The three portable laws' own numerals are, separately, NEEDS-3
at every one of them.  So "3 of 5 portable" is, mechanically, "3 of the 5
parent laws have statements with no numeral in them, and all three of those
statements survived; the 2 whose statement IS a number did not."

§9 says this in prose, well and honestly ("all three are portable because
their STATEMENTS contain no numeral").  The head does not, and the head is
the object that will be cited.  The AID adjudication §2 ruled exactly this
class of defect — "the delivered SPLIT compared two TESTS, not two
OBSERVABLES" — and NDEP is AID's child.  A contrast drawn between two
different tests must declare that it is one.

**Repair (liftable):** the aggregate segment gains the test declaration, e.g.
after `NDEP-PORTABLE-3-OF-5<`: `THE 3 ARE SCORED AT THE STATEMENT (THEOREM
HOLDS AT THE NEW ARENA POINT), THE 2 AT THE NUMERAL (TRANSPORT PROCEDURE);
THE 3 PORTABLE LAWS ARE EXACTLY THE 3 WHOSE STATEMENTS CARRY NO NUMERAL`.

### MAJOR-2 — "TRANSPORTS ON n ALONE" is false under its literal reading

The head's licensing clause is: *"EVERY ONE OF THE 6 TESTED NUMERALS IS
q-CARRIED (6 OF 6), SO WHAT TRANSPORTS ON n ALONE IS THE LAWS AND NEVER THEIR
NUMBERS."*

At every arena point this unit reaches, **q = √n exactly** (4/2, 9/3, 16/4).
Therefore every q-formula the unit found IS a function of the actor count
alone: 2q−1 = 2√n−1, q+3 = √n+3, q+1 = √n+1, and the sharpened floor is a
function of (n, q) = (n, √n).  Under the plain reading of "transports on n
alone", **all six numerals transport on n alone** and the clause is false.

What is actually true is the unit's declared rule, and only that: the numeral
is not reproduced by **T-N**, the single declared n-only extrapolation
(`t_n_reading` = the counting bound offset by the constant that reproduces
the parent's value at n = 9).  §8 declares that rule openly and applies it
uniformly; the honesty is present in §8 and absent from the head.  The one
numeral genuinely shown NOT to be a function of n is the ladder's modulus,
and that is shown by the **fixed-n L-sweep** — a different and much stronger
instrument than the three-point transport table.

**Repair:** replace `SO WHAT TRANSPORTS ON n ALONE IS THE LAWS AND NEVER
THEIR NUMBERS` with `NO TESTED NUMERAL IS REPRODUCED BY THE DECLARED n-ONLY
READING (THE COUNTING BOUND OFFSET TO THE PARENT'S VALUE); EVERY ONE IS
REPRODUCED BY A FORMULA IN q = sqrt(n) OR IN THE DECLARED LINK COUNT L, AND
ONLY THE LADDER'S MODULUS IS SHOWN NON-n BY A FIXED-n SWEEP`.  §1 must also
disclose that q = √n at every arena point reached, so the reader knows what
the words can and cannot separate.

### MAJOR-3 — the 6-of-6 denominator excludes the one tested numeral that is not q-carried, and is typed

`numerals_q_carried` is computed as the count of NEEDS-3 over a hand-written
six-word list (law1 chart, law2 time, law2 floor, law3 count, law4 ladder,
law5 count).  `"numerals_tested": 6` is a **typed literal** (source line
2542), against the standing rule that counts are computed and never typed;
`independent_head` re-derives the length but re-declares the same membership,
so the two routes are not independent on the choice of denominator.

The **offset** is a tested numeral of law 2 by every operational criterion:
it has a parent value (1), a three-row transport table, and its own emitted
word.  Its word is `LAW-IN-N`.  It is the only tested numeral that is not
NEEDS-3, and it is the one left out of the denominator.  With it in, the head
would read **6 of 7**.

The exclusion may be defensible (the offset is a difference of two numerals
already counted) — but it must be *declared*, and the denominator must be
derived from a declared rule rather than typed.  As it stands, the clause
that licenses the whole "laws transport, numbers are q-carried" reading is
carried by a hand-chosen denominator.

**Repair:** derive `numerals_tested` from the set of transport tables the run
actually builds; either include the offset (6 of 7, with the UNDISCRIMINATED
stamp shown) or publish the exclusion rule in-paper and gate it.

### MINOR-1 — the offset's UNDISCRIMINATED stamp is dropped in the head

§4 says: *"The transport procedure stamps this leg UNDISCRIMINATED … the
stamp is published with the word rather than quietly dropped."*  The head
publishes `OFFSET ONE AT ALL THREE (LAW-IN-N)` — stamp dropped.  This
matters because `transport_word` returns LAW-IN-N **by priority** when all
three readings agree; LAW-IN-N is the tie-winner, not a finding.  Repair:
`OFFSET ONE AT ALL THREE (LAW-IN-N, UNDISCRIMINATED)`.

### MINOR-2 — §1's three-word definition does not cover the laws it stamps

§1 defines all three words through "the reading of it in which **the
numeral** is a function of the actor count alone".  Laws 1, 3 and 5 have no
numeral in their statements — §3 says so explicitly ("The statement contains
no numeral at all") — so §1's definition is inapplicable to exactly the three
laws it is used to stamp LAW-IN-N.  The code knows better than the paper
(`word_basis` is a separate, statement-level field).  Repair: make §1's
definition two-slot — a **statement** word and a **numeral** word — which is
what the §3 table already publishes.

### Feasibility (#299/#319) — MET

PORTABLE-k-OF-5 was feasible for every k at the committed corpus: laws 1/3/5
could have returned BREAKS had a theorem failed at n = 4 or on the n = 16
window; laws 2/4 could have returned LAW-IN-N had T-N matched.  The five
synthetic control arms drive the real procedure to all three words plus the
two degenerate cases (UNDISCRIMINATED, NO-FEASIBLE-ROW), and 8 of 8 leg arms
fire in both directions.  The verdict is not forced by construction.

---

## 2. THE FLOOR CORRECTION'S FAIRNESS — THE RULING

I read AID's published sentences at the source, not through NDEP's rendering.

**What AID actually published** (paper-33 §5.1):

> "Nine actors need distinct binary participation signatures, and k events
> supply at most 2^k of them, so no history can force identity on fewer than
> four events.  That floor is a counting theorem, and it is attained: the
> smallest event subset that forces identity has size 4 at all 72 R = 3
> histories and at all 596 forced R = 4 histories."

and the table row `| counting floor, ceil(log2 of the actors) | 4 |`, and
`the transportable content of the five is four informative events, a theorem
floor attained everywhere, plus one structurally redundant event`.

**Ruling on the mandate's question — bound or attainment?**  In AID's original
it is **a BOUND, stated as a counting theorem, explicitly at nine actors and
with the value four written out in words**.  The attainment is a **separate,
measured, n = 9-scoped claim** (72/72 and 596/596).  AID asserts attainment
at no other n, and the word "everywhere" in the §5.1 summary means *at every
history of AID's corpus*, not *at every arena*.  The only n-generic object in
AID is a **FORM** — the table-row label "ceil(log2 of the actors)" and the
receipt key `counting_bound_ceil_log2_actors`.

**Therefore: NDEP does not have a licensed "AID was wrong".  It has a
licensed "the FORM was undiscriminated at n = 9."**  At n = 9 the counting
bound and the size-q-corrected bound both read 4; the n = 9 measurement could
not tell them apart, so a formula written in n was as good a label as a
formula in q — and only n = 16 discriminates.

**"Does not transport" is NOT the licensed sentence.**  The head's
*"THE PAIR SURVIVES AS A STRUCTURE AND ITS FLOOR FORMULA DOES NOT"* reads, in
isolation, as "the parent's floor formula fails" — and ⌈log₂n⌉ does not fail;
it is true at every n and NDEP says so in §4.  The head's next clause repairs
it partially (`ATTAINED FLOOR 2|4|6 WHILE THE COUNTING BOUND ceil(log2 n)
READS 4 AT n=16`), but the leading clause is the one that will be quoted
against a sealed terminal.

### THE EXACT LICENSED FLOOR-CORRECTION SENTENCE

> The parent's bound is a theorem and it stands: no history forces identity
> on fewer than ⌈log₂ n⌉ events, at n = 16 as at n = 9.  What the parent
> measured at n = 9 is that the bound is ATTAINED there, and that measurement
> also stands.  At n = 9 the counting bound and the bound that includes the
> event size q coincide at 4, so the parent's arena could not discriminate
> the two forms; at n = 16 they part — the counting bound reads 4 and the
> attained floor is 6 at every one of the 24 covering class tuples.  It is
> the ATTAINMENT that fails to transport, not the bound, and the form that
> survives the discrimination is the sharpened one, in which q enters.

**Head repair:** `THE PAIR SURVIVES AS A STRUCTURE; THE BOUND ceil(log2 n)
STANDS AS A BOUND AND IS NOT THE ATTAINED VALUE AT n=16`.

**§4 repair:** the phrase "its n-only generalisation is not" attributes a
generalisation to the parent by possessive.  The parent made none.  Licensed:
"the n-only generalisation THIS UNIT CONSTRUCTS FROM IT is not".

### MAJOR-4 — the floor anchor reads the parent's BOUND key and labels it the ATTAINED floor

`P-FLOOR` anchors
`crystallization/information_floor/counting_bound_ceil_log2_actors`, and the
row that consumes it is noted **"PARENT ANCHOR: the attained information
floor at n = 9"**; the receipt publishes it as
`information_floor.parent_n9_attained = 4`.  AID's receipt carries the
attained value under its own separate keys —
`minimal_event_subset_C1 {"4": 72}` and
`minimal_event_subset_forced_C3 {"4": 596}` — which this unit does not read.

At n = 9 both are 4, so **no number is wrong**.  But the unit whose entire
contribution is separating a bound from an attained value anchors the bound
and calls it the attained value.  That is a referent-binding defect at the
exact joint the paper is about, and a path drift in AID would not be caught
where it matters.

**Repair:** add a second path anchor on `minimal_event_subset_C1` (and/or
`minimal_event_subset_forced_C3`) for the attained row, keep
`counting_bound_ceil_log2_actors` as the anchor for the BOUND row, and
re-label both notes to their true referents.

### Strengthening the unit missed (free, and it sharpens its own §10)

The unit's own sharpened formula, evaluated beyond its three points, gives
2, 4, 6, 8, 10, 12 at q = 2…7 — i.e. **the sharpened floor is 2(q−1)** at
every q I tested, against a schedule time of 2q−1.  The offset is therefore
1 **by subtraction of two closed forms**, at every q, not merely at the three
measured arena points.  §10 registers "whether it is attained at every q is a
theorem someone should prove or break" without noticing that its own formula
has a closed form and that the closed form explains the offset's constancy.
This should go into §10 as a stated conjecture with its two-line derivation
of the offset.

---

## 3. THE MOD-MOTIF SENTENCE — THE RULING, AND THE CRITICAL CHECK

**The ladder half is well made and I confirm it independently.**  At n = 4 a
saturating grouping's incidence vector is the indicator of one declared
column, so R rounds give a field constant on all nL cells exactly when L | R;
the achievable sets are the multiples of L.  Measured 1 / 2 / 3 at L = 1/2/3
with n, √n and the characteristic all pinned at their n = 4 values.  This is
a genuine and strong separation — the modulus moves while every candidate
function of n stands still.  **"The modulus is the declared link count L, not
√n" is licensed at 3 L-values × 1 n, with the n = 16 row as corroboration**,
because the separating instrument is the fixed-n sweep, not the arena count.
Three L-values are enough precisely because L is varied against a frozen n.

**But it is licensed only for the LADDER'S BUDGET MODULUS**, and two things
are wrong with how far the paper carries it.

### MAJOR-5 — "the coin's modulus is free" contradicts a terminal parent that DERIVES it, uncited

§6 states flatly: *"The coin's modulus is declared, and free … the order of
that root is not fixed by anything in the arena."*  The head states
*"THE COIN'S MODULUS IS A FREE DECLARATION."*

Paper-20 (terminal) states the opposite, and states it as a derivation:

> "arena is over F_3.  The link connection the record defines is therefore
> valued in the arena's own scalar group Z_3, and the walk's phase alphabet
> is the cube roots of unity."

and its own head carries `CONNECTION-GROUP Z_3 DERIVED FROM THE ARENA'S OWN
FIELD F_3`.  Paper-25's THEOREM C states the residue reading as a theorem.

What NDEP measures is (i) the operator construction accepts any m and the
record enters exactly mod m, and (ii) **this census** returns 45/3 at
m = 2, 3, 4, 5.  That is **blindness of one census**, which is fully
compatible with the modulus being derived-from-the-field and simply inert for
that census.  Note that paper-20's rule is not vacuous at this unit's own
arena: AG(2,2) is over F_2, so the parent's derivation *predicts* m = 2 at
n = 4 — a determinate, q-carried answer, which this unit never tests.

§10 gets it right ("That is a statement about this census, which is blind to
it") — §6's flat sentence and the head do not.

**Repair:** scope §6 and the head to the census, and cite the parent
derivation as the standing counter-claim, so a successor knows there is one.

### THE EXACT LICENSED MOD-MOTIF SENTENCE

> Scoped to the ladder's budget modulus: at fixed n = 4 the achievable-budget
> modulus moves with the declared link count L — 1, 2, 3 at L = 1, 2, 3,
> within the declared search bound R ≤ 7 — while n, √n and the characteristic
> stand still, so the budget modulus is a function of the declaration and not
> of the actor count.  Nothing is claimed here about the coin's modulus
> beyond this census's blindness to it: the n = 4 division-forcing census
> returns 45 unique and 3 non-unique at m = 2, 3, 4 and 5, which measures
> that THIS census does not see m.  Paper-20 derives the coin's Z₃ from the
> arena's own field F₃; this unit neither tests nor rebuts that derivation,
> and at AG(2,2) that derivation would read m = 2.

**Sentences NOT licensed:** "the order of that root is not fixed by anything
in the arena"; "THE COIN'S MODULUS IS A FREE DECLARATION" unqualified; and
any sentence generalising the split to the corpus's mod-3 phenomena at large.

### THE CRITICAL CHECK — what dissolved and what did not

I censused the corpus's mod-3 appearances:

| appearance | parent | NDEP's account |
|---|---|---|
| welds motivated at budgets divisible by 3 | paper-29 §4.2 ("a link-constant field needs 27 to divide 9R, so R must be divisible by 3") | **EXPLAINED** — carrier is L, measured at fixed n |
| the coin reads the record mod 3 / the residue channel | paper-20 (Z₃ **derived** from F₃), paper-25 THEOREM C | **NOT EXPLAINED** — measured blind, not measured free (MAJOR-5) |
| Born branch measure a function of n₀ mod 3 | paper-24 mod-3 theorem | downstream of the coin; untouched, unmentioned |
| "the refinement ladder doubles from a first rung of 3" | **none found** (see MAJOR-6) | not measured separately |

So: **one of the two mechanisms the paper names is accounted for; the other
is only shown inert against one census.**  The paper does not claim the whole
fingerprint dissolved — §6 says the measurement dissolves *the pin's
dichotomy*, which is the right object, and §10 registers the coin as open.
That restraint is correct and I credit it.  The head's `THE MOTIF SPLITS IN
TWO` is defensible as a count of mechanisms but overstates the settlement of
the second half; with MAJOR-5's repair it becomes honest.

### MAJOR-6 — "the refinement ladder doubles from a first rung of 3" is unattributed, and its relation is refuted by the unit's own row

§6 opens with three appearances and asserts "All three of those are cited
from their parents."  No parent is named in-text for any of them, and I can
find no parent at all for the third.  The two candidates both say something
else: paper-29 says the budgets are the **multiples** of 3, and paper-04's
refinement ladder has ceiling ⌊log₂ min n⌋ with measured value **2** at its
declared family, not a first rung of 3.  Worse, the unit's own L = 2 row
returns {2, 4, 6} — a set of multiples, not a doubling chain.  This is the
LOR disease exactly: the numeral is registry-backed, the RELATION is neither
measured nor cited.

**Repair:** delete the clause, or replace it with "the weld ladder's rungs
are the multiples of 3 (paper-29 §4.2)", which is the object the sweep
actually measures.

---

## 4. UNDISCRIMINATED AS A WORD (the offset constant)

**Honestly rendered in the receipt and the transcript; dropped in the head.**
The receipt carries `offset.evidence.stamp = "UNDISCRIMINATED"` with
`t_literal_agrees = t_n_agrees = t_q_agrees = 3` and both discrimination
counts at 0; the transcript prints `word LAW-IN-N (UNDISCRIMINATED)`; §4 of
the paper names it and explains it.  That is good practice and I credit it.
Two defects attach:

- **MINOR-1** above (head drops the stamp).
- **MINOR-3 — the uniform-rule claim is false at the offset leg.**  §8 says
  "The n-only reading is fixed by rule and not fitted per law … The same rule
  is applied to all five laws."  The offset's three rows are built with
  `t_literal = t_n = t_q = 1` **hard-coded** (source lines 1853–1857), not
  through `t_n_reading`.  Applied as declared, the rule would give
  `counting_floor(n) + (1 − 4)` = −1 at n = 4 and 1 at n = 16, T-N would fail
  at n = 4, and the offset's word would flip from LAW-IN-N to NEEDS-3.
  The hard-coded version is **substantively the right rendering** — a
  constant is honestly all three readings at once, which is what
  UNDISCRIMINATED says — but the uniformity claim as written is not true.
  Repair: declare the constant-law exception to the rule in §8 and gate it,
  rather than leaving it undisclosed in the source.

---

## 5. THE q = 4 ROWS, AND "SATURATING = MAXIMAL"

**Unscored-not-failed language: CONSISTENT.**  `transport_word` carries
infeasible rows and never scores them (#34), the q = 4 coset row is built
with `feasible = False, measured = None`, the transcript reports "feasible
rows 2 of 3", and §5 and the head both say the row is "carried and left
unscored **by the procedure itself**".  The head's "THE HYPOTHESIS FAILS AT
q=4" is a measured fact about the theorem's hypothesis (declared links
generate 8 of 16 — I reproduce it, and the mechanism the paper gives is
exactly right: every canonical direction representative has first coordinate
in the prime subfield, so the span is index 2), and it is not a claim that
the law failed.  Naming both readings (67 abstract subgroups, 7 F_q-subspaces
— both reproduced) and choosing neither is the right call.

**"Saturating = maximal at q ≤ 3": PARTLY UNBACKED.**

### MAJOR-7 — the q = 3 half of the saturation clause is asserted, never measured, never anchored

The scope block publishes "SATURATION IS MAXIMAL AT q=2 **AND q=3** AND IS
NOT AT q=4"; §2.1 says "saturation is maximality here, **as it is at q = 3**";
§8 repeats it.  Measured in this unit: q = 2 (`max_round_incidence = 4 = n`)
and q = 4 (witness incidence 48 > 16).  **q = 3 is measured nowhere** — the
fidelity block has no maximum-incidence key and no gate computes one — and it
is anchored to no parent quote or receipt path.  It is a *relation*, so it
slips past the numeral-coverage gate entirely.

(The claim happens to be TRUE — at AG(2,3) the maximum incidence over
groupings is 9 = n — which is why nothing else caught it.  A true unbacked
sentence in the citable scope block is still an unbacked sentence, and this
unit's whole discipline is that n = 9 facts are anchored or absent.)

**Repair:** compute `max(sum(v))` over the q = 3 vectors inside the existing
fidelity leg (one line; substrate, not a law, so the pin's wall is not
touched) and gate it — or strike "and q = 3" from all three places.

---

## 6. THE n = 9 RE-DERIVATION CLAIM, AND THE FIDELITY GATE

**Fidelity gate stamped not-a-finding: YES, correctly.**  The receipt carries
`fidelity.stamp = "FIDELITY-LEG-ONLY: no n = 9 law is evaluated at q = 3 here
and no n = 9 finding…"`, W-Q3 is declared partial with the same words, §2 and
§9 both say it is a fidelity leg and not a finding, and G-CONSTRUCTOR-FIDELITY
compares five rows per object against five separate anchored paths.  Correct.

**No n = 9 LAW value is recomputed: VERIFIED.**  I grepped and spot-checked
every consumer of the ten path anchors and the six frozen constants.  Law
values enter only as `jpath(...)` reads or `FAC_DECLARED[...]` reads; the
crystallization, chart, coset-menu and factorization values at n = 9 are
never computed.  The one q = 3 computation is the constructor.

### MAJOR-8 — but the scope block's absolute sentence is false as written

The head publishes: *"q=3 ENTERS ONLY AS THE CONSTRUCTOR-FIDELITY LEG AND
**NO n=9 NUMBER IS RE-DERIVED HERE** -- ALL TEN ARE ANCHORED READS…"*

Five of those ten anchors are the n = 9 **substrate** counts (280, 36, 72,
276, 600), and the fidelity leg **re-derives every one of them** at q = 3 and
compares (`{"here": len(p3), "parent": jpath(...)}`).  The sentence
contradicts the leg named in the same sentence.  The receipt says it
correctly ("no n = 9 **law** is evaluated"); the head does not.

**Repair:** `NO n=9 LAW VALUE IS RE-DERIVED HERE; THE FIVE q=3 SUBSTRATE
COUNTS ARE RE-DERIVED AS A FIDELITY LEG AND AGREE WITH THE PARENT'S ANCHORS
5 OF 5`.

**FAC frozen-commit citation: CORRECT.**  Commit `f4172ea`, both digests as
declared, all six constants verified against the pinned tree by me, the
under-repair reason stated in §2 and in the PROVENANCE arena row, and each
constant cross-checked against a value the unit computes.  This is exactly
right and should be the template.

---

## 7. SCOPE STAMPS, REFERENT BINDING, E-24, TEST-DECLARATION

**E-24: clean.**  The 45-of-48 fraction is stamped COUNTING-ONLY in the
receipt, the head and §7; the multiset problem is disclosed with both
families published and never crossed (48 schedules over 12 distinct event
sets); POL-MEASURE and WALL-PROBABILITY both fire on their probes.  This
discharges the AID §5 obligation to name the universes IN-PAPER.

**Referent binding at n = 4: clean.**  48 histories, 15 partitions, 53
prefixes and 12 distinct event sets each appear adjacent to their nouns, and
G-NOUN-BINDING enforces a three-word window.  I found no unbound headline
count at n = 4.

### MAJOR-9 — the n = 16 naming leg's prefix universe is undeclared, and it is ONE history

§3 publishes "1,240 permutations at **every prefix**, 21,080 comparisons in
all, 0 mismatches, with 2,064 … inside the stabilizer".  The universe of
"every prefix" is named nowhere.  It is not the window's 24 covering
histories: the source takes `Href = cov16[0][1]` — **the first covering class
tuple only** — and runs k = 0…16, so 17 prefixes × 1,240 = 21,080.  I
reproduced this exactly.  The naming theorem's entire n = 16 evidence is one
history out of the window's own 24.

Compounding it: the positives are polarity-inflated by a vacuous prefix.  My
by-prefix census gives `[1240, 520, 168, 56, 56, 20, 4, 0, …, 0]` — **1,240
of the 2,064 positives (60%) come from k = 0**, the empty prefix, where every
permutation fixes every event of an empty history vacuously, and from k = 7
onward the window is entirely negative.  The claim "the window is exercised
in both directions" survives (824 non-vacuous positives), but the published
2,064 is not what a reader will take it for.

This is the AID §5 defect reborn — every numeral true, the universe unnamed.

**Repair:** name the universe in §3, in W-N16-PERM and in the head ("the
prefixes of one covering class tuple, 17 of them"); publish the non-vacuous
positive count separately from the k = 0 contribution; and either extend the
leg to all 24 covering histories (cheap — 24 × 17 × 1,240 ≈ 506k comparisons)
or declare the single-history restriction as a window with its reason.

### MAJOR-10 — the parent's declared GRAIN axis is silently fixed

FAC's own verdict is `FAC-STRATIFIED<BY-GRAIN=ACTOR-5852-OF-5856-UNIQUE-vs-
CARRIER-5810-OF-5856-UNIQUE; ATOM=FAC-ATOM-BREAKS-AT-THE-GROUPOID-GRAIN>`.
NDEP carries only the actor grain (5852/4), tests only actor partitions at
n = 4, and reports law 5 as portable.  The head does say "COMPLETE ACTOR
LATTICE", so the coordinate is named — but §7's "the parent's thesis … holds
verbatim" does not say *which grain's thesis*, and the parent's second grain
is where its own atom BREAKS.  Under §15 (match every coordinate) a declared
free axis of the parent must be matched or stamped.

**Repair:** §7 names the grain; the successor register gains "the carrier
grain at n = 4 — the grain at which FAC's atom breaks — is untested here."

### MINOR-4 — silent caps in both ladder sweeps

The n = 4 sweep runs `homogeneous_ladder(B, bv, bs, 7)` and the n = 16 sweep
`…, 2 * A16.L)` = 8.  Neither bound appears in the paper.  The published sets
{1..7}, {2,4,6}, {3,6} and {4,8} are therefore *achievable sets within an
undisclosed search bound*, and a reader will take {3,6} for the whole ladder.
"No silent caps" is a standing discipline.  Repair: publish R ≤ 7 and R ≤ 8
in the table captions and in the head's ladder segment.

### MINOR-5 — an inert criterion leg on the real corpus, disclosed only to the receipt

`leg_pass_counts = {leg1: 240, leg2: 57, leg3: 720}` against a universe of
15 × 48 = 720 (partition, history) pairs.  **Leg 3 passes at 720 of 720** —
it never discriminates anywhere on the real n = 4 corpus, so the census's
discriminating power is carried by legs 1, 2 and 4.  §8's "no leg is a branch
that never executes" is true of the synthetic arms and will be read as a
statement about the census.  Also, `leg_pass_counts` publishes 3 of the 4
legs.  Repair: publish all four leg pass counts in-paper with the universe
named, and add one clause noting leg 3 is inert at this arena.

### MINOR-6 — four of thirteen paper claims have literal-`True` predicates

CL-HISTORIES, CL-TIME, CL-OFFSET and CL-FORCING are gated on `True`.  Their
*sentences* are rendered from receipt values, so the numerals are bound, but
the gate text says "a claim whose predicate is false kills the run" and for
these four no predicate could ever be false.  Per E-23 (ungated constant
booleans) these should either carry a real predicate or be declared as
render-only rows.

### Test-declaration where contrasts appear

Three contrasts are drawn.  Two are declared: the theorem-vs-numeral contrast
is declared in the §3 table and in G-LAW1-WORD's own text ("the law and its
numeral are never conflated"), and the derived-vs-declared contrast of the
mod motif is declared in §6.  **One is not** — the aggregate's
laws-vs-numbers contrast in the head (MAJOR-1).  That is the one that needs
the declaration most, because it is the sentence the corpus will inherit.

---

## 8. CHOICE INVENTORY (RSQ standard: motivated ⟺ zero free items)

| item | status |
|---|---|
| the arena AG(2,q), q ∈ {2,3,4} | MOTIVATED — the smallest arena separating √n, characteristic and L |
| L = q as the parent's declaration | MOTIVATED and, better, swept |
| the T-N reading (counting bound + offset) | **DECLARED, and verdict-determining** — declared in §8, but it is one family among many n-only families, and the LAW-IN-N/NEEDS-3 split is relative to it (MAJOR-2) |
| the six-numeral denominator | **FREE** — hand-chosen and typed (MAJOR-3) |
| R ≤ 7 / R ≤ 8 search bounds | **FREE and undisclosed** (MINOR-4) |
| Href = the first covering tuple | **FREE and undisclosed** (MAJOR-9) |
| the actor grain for law 5 | **DECLARED-BY-INHERITANCE, unstamped** (MAJOR-10) |
| m ∈ {2,3,4,5} | MOTIVATED as a declared free axis, swept |
| the offset's constant-law exception to the T-N rule | **FREE and undisclosed** (MINOR-3) |

Six free items.  The unit is *arena-relative* by its own §15 standards on the
LAW-IN-N/NEEDS-3 split, and should say so: the words are relative to the
declared T-N family, and only the ladder's L-carriage is established
independently of it.

---

## 9. SUCCESSOR REGISTER — WHAT TO ADD

§10's four open items are well chosen (saturation at non-prime q, the coset
hypothesis's representative choice, the coin's modulus, closing the n = 16
window).  Add:

1. **The sharpened floor's closed form.**  It evaluates to 2(q−1) at q = 2…7;
   with the schedule time 2q−1 this makes the offset 1 at every q by
   subtraction.  State it, and pose attainment as the theorem.
2. **Paper-20's derivation of the coin's Z₃ from F₃** as the standing
   counter-claim to "free" — and the concrete test: does the connection
   construction at AG(2,2) over F₂ force m = 2?
3. **The carrier grain at n = 4**, the grain at which FAC's own atom breaks.
4. **A second n-only family.**  Since q = √n at every arena point reached, an
   arena with n not a perfect square (or q ≠ √n) is what would let
   "LAW-IN-N" mean what §1 says it means.
5. **The naming theorem at n = 16 beyond one history** (24 covering tuples).

---

## 10. FINDINGS INDEX

**MAJOR** — 1 aggregate blends two tests, undeclared · 2 "transports on n
alone" false under its literal reading (q = √n everywhere) · 3 the 6-of-6
denominator excludes the offset and is typed · 4 the floor anchor reads the
BOUND key and labels it ATTAINED · 5 "the coin's modulus is free" contradicts
paper-20's uncited derivation · 6 "the refinement ladder doubles from a first
rung of 3" unattributed and refuted by the unit's own L = 2 row · 7 "saturation
is maximal at q = 3" asserted, never measured or anchored · 8 the scope
block's "NO n=9 NUMBER IS RE-DERIVED" is false (five substrate counts are) ·
9 the n = 16 naming leg is one history with an undeclared prefix universe and
60%-vacuous positives · 10 the parent's declared grain axis silently fixed.

**MINOR** — 1 offset's UNDISCRIMINATED stamp dropped in the head · 2 §1's
word definitions don't cover the numeral-free laws they stamp · 3 the T-N
rule's undisclosed constant-law exception · 4 silent caps R ≤ 7 / R ≤ 8 ·
5 leg 3 inert at 720/720, receipt-only · 6 four claims with literal-`True`
predicates.

**No computed number moved.**  I found no false numeral, no false theorem and
no forged gate.  Every major is a binding-to-prose defect with an exact
liftable repair, which is why the grade is AWF and not REJECT.

---

## 11. CLOSING

**Recomputations: 141** (47 instrument — 10 hash verifications, 2 off-tree
artifact reproductions, 5 CLI checks, 3 selftest anchor corruptions, 27
mutant target checks; 94 measurement, all from independent primitives).

**Object hashes re-verified at close, all five unchanged:**
paper-39-ndep.md `25bea1eddd3a` · ndep_exact.py `d83df6c1e07d` ·
ndep_output.txt `efa2987ef6a7` · ndep_receipt.json `3f5639a9146d` ·
note-ndep-pin.md `2ff14505f18f`.

Everything above is a **candidate reading until adjudication**.
