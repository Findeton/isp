# CYCLE B″ HOSTILE REVIEW — R3, THE INSTRUMENT LENS

**Reviewer:** R3 (sufficiency / instrument), primary K4 — the measured
verdicts and the Feynman gate.  **Protocol:** `v13/note-rq0-admissibility-hostile-protocol.md`
(commit `e5144d4`), judged against that document only.  **Object verified
at the pinned SHA-256 prefixes:** paper `d08a761081a7`; code `c81f7f5530d1`;
output `4e2c7bf5e5fe`; receipt `dfd4f9435fd9` — all four match the freeze.
**Method:** every number below was recomputed in an independent
implementation transcribed from the paper's Definitions 2.1/2.2/4.1/4.2/7.1/8.1,
importing nothing from the unit and from neither terminal module; exact
arithmetic (`int`, `fractions.Fraction`) throughout; 25 independent
recomputations, 0 disagreements with the delivered numbers.

## VERDICT

$$\textbf{ACCEPT-WITH-FIXES}$$

Both registered rungs stand.  No computed number in the paper or the
receipt is wrong: all 25 native recomputations agree exactly, including
every anchor I could reach without the operator machinery, the sixteen
rigidity sweeps, the four discriminator verdicts, both Feynman statistics
and all four cost-tower levels.  Three defects are genuine and must be
repaired before the rung is called terminal; none of them moves a number,
and none of them touches the two registered outcomes.  The remainder are
scope qualifiers on sentences that currently read stronger than what was
measured.

---

## 1. FINDINGS, RANKED

### F1 — FIX-REAL. The measured kill-list is a property of the declaration the unit supplies, not of the forged context

This is the cycle's headline measurement ("the killing conditions are
measured rather than assumed: (i-a) and (ii-a) fail together"), and it is
declaration-relative.  Section 6 does not read the adversary's declared
family from the arena; for every context it *sets* `fam := Pres_L(A(B))`
and adjudicates the patch it has just constructed.  Re-run natively at the
forged boundary $\pi_1=\{01\mid2\mid3\mid4\}$ under DET:

| declared family at $\pi_1$ | $\lvert\mathfrak F\rvert$ | admissible | killed by |
|---|---|---|---|
| the closure $\operatorname{Pres}(\pi_1)$ — **the unit's choice** | 240 | no | (i-a), (ii-a) |
| the written-exact subfamily $\{F:\operatorname{comp}F=\pi_1\}$ | 120 | no | **(i-b) alone** |
| the merging subfamily $\{F:F(0)=F(1)\}$ | 120 | no | **(i-b) alone** |
| the repreparation task $(0,0,2,3,4)$ alone | 1 | no | **(i-b) alone** |
| the identity alone | 1 | no | (i-a), (i-b), (ii-a), (ii-b) |

The *verdict* (inadmissible) is declaration-independent, as it must be —
that part of the discriminator is sound and I confirm it.  The *identity of
the killing condition* is not.  Deviation (2) records the pin's expectation
as refuted by measurement; the refutation holds for exactly one of the five
declarations above.  The honest form is available and costs one clause:
condition (i-b) admits only one declaration at any boundary, so for the
unique family that could ever pass, the kill is (i-a)+(ii-a), and for every
other declaration the kill is (i-b).

Two consequences follow in the same breath, and neither is currently
disclosed:

- In §6, **(i-b) and (ii-b) are true by construction for every row** —
  (i-b) because the family is set to the closure, (ii-b) because the
  preparation is set to the whole carrier.  Measured: over all 52 records
  at five configurations under DET, the §6 protocol returns (i-b) true 52
  of 52 and (ii-b) true 52 of 52.  Those two columns of the nine-row table
  carry no information.
- With (i-b) imposed and the identity present, (ii-a) is forced by
  Theorem 3.2 and (i-a) reduces to a single bit.  Measured: over all 52
  records under DET, `(i-a) ⟺ A(B) is discrete` and
  `(ii-a) ⟺ A(B) is discrete`, both 52 of 52.  **The nine-row table has one
  measured degree of freedom per row: is the presented boundary the
  carrier's discrete algebra (and is it carrier-typed)?**  Everything else
  is Theorem 3.1 read out.

### F2 — FIX-REAL. Definition 2.1's patch is a triple; the axiom needs a quadruple, and the paper's own minimal witness proves it

Definition 2.1: "A patch is a triple $P=(B,\mathfrak F,L)$."  Definition
4.2: "The patch declares a preparation $X_0\subseteq X$."  Clause (ii-b) is
a function of $X_0$.  W1 and W3 of §5 have **the same boundary, the same
declared family and the same law** — $(\{0\mid1\mid2\},\{\mathrm{id}\},
L_{4.2})$ — and opposite verdicts, differing only in $X_0$; §5 says so
explicitly ("it differs from W1 in its declared preparation alone").  Two
patches equal as triples therefore receive different admissibility
verdicts, so admissibility is not a function of the triple.  Re-run
natively: W1 admissible with reach $\{0,1,2\}$; W3 inadmissible with reach
$\{0\}$ and never-occupied atoms $\{1\},\{2\}$.  Definition 8.1 inherits
the same gap — it writes the cost's patch as
$(B,\operatorname{Pres}_{\tilde L}(A(B)),\tilde L)$ while the computation
supplies the full preparation.  Fix: make the patch a quadruple in
Definitions 2.1 and 8.1, or make $X_0$ part of the boundary's declaration.

### F3 — FIX-REAL. Theorem 7.2's inadmissible comparator fails two clauses, not the one reported

The paper's §7.2 table and the receipt both state that the 121-task
comparator fails "(i-b): the declared family is not the boundary's closure".
Measured natively: that patch fails **(i-b) and (ii-a)**.  The added task is
the total erasure $(0,0,0,0,0)$, whose written record is
$\operatorname{comp}=\{01234\}$, not the declared discrete boundary, so the
WRITTEN clause fires as well — one task fails it.  The receipt's `fails`
field is a hard-coded string, not a computed kill-list, which is why the
error survived: it is the one place in the unit where a clause verdict is
asserted rather than adjudicated.  Fix: compute the kill-list, print
"(i-b) and (ii-a)", and note that the comparator is separated from the
admissible patch by two clauses.

### F4 — SCOPE. Member 1's inadmissibility is not law-universal; only the pair's is

The abstract says "The forged member of the colluding pair is
**inadmissible**" without a law qualifier.  Measured counter-instance: take
the composition-closed, identity-free, left-total law $L=\{\sigma\}$ with
$\sigma=(0,0,2,3,4)$ — legitimate under Definition 2.1 and of exactly the
kind Proposition 3.4 puts in play.  Under it the **forged boundary
$\pi_1$ is ADMISSIBLE on all four clauses** (i-a ✓, i-b ✓, ii-a ✓, ii-b ✓,
$\lvert\mathfrak F\rvert=1$).  Member 2 is simultaneously inadmissible there,
$\operatorname{Pres}_L(\delta)=\varnothing$ — consistent with Theorem 6.1,
which is what actually protects the result.  So the cycle's law-universal
claim is the joint one, and the single-member claim is scoped to the
committed identity-containing laws.  §6's table header and §9's scope line
carry the qualifier; the abstract does not.

### F5 — DISCLOSURE. The Feynman statistic is not a function of admissibility at the fixed boundary

The pin asks for "an admitted tester statistic that differs between an
admissible patch and an inadmissible patch at the same boundary", and the
unit delivers exactly that: $\sigma=1$ against $\sigma=3/4$, both exact.
The existential form of the gate is passed and `EMPIRICALLY-IDLE` correctly
does not occur.  But the abstract's slogan — "admissibility changes a
number" — over-reads it.  At the *same* boundary, *same* law, *same* state,
the inadmissible patch $(\delta,\{\mathrm{id}\},\text{DET})$ has
$\sigma=1$, exactly the admissible patch's value; it fails (i-b) alone.
Measured distribution: over all 3005 one-task extensions of the closure,
$\sigma$ takes four distinct values, minimum exactly $3/4$, attained by
exactly the 5 constant maps.  So $3/4$ is the extreme of the comparator
family, not a generic inadmissible value, and $\sigma$ separates *some*
inadmissible patches, not the inadmissible ones.  §7.1 states two honest
halves; this is the third and it belongs with them.

### F6 — DISCLOSURE. Nine contexts, four distinct patches; three rows are literally the same patch

`ALIGNED1111`, `ERASER` and `ADDRESS` all present the atom list
$[[0],[1],[2],[3],[4]]$ — verified in the receipt's own `patch_verdicts`
and re-derived natively from the committed constructions (block-diagonal
projections with the retained sink; incidence by nonzero trace against the
diagonal address atoms).  The six carrier-typed rows contain **four**
distinct partitions.  §6.5 derives exactly this for the arena's two
contexts and §6.1 states it for member 2, so the fact is disclosed in
prose — but the table presents six independent measurements, and the
discriminators D1(member 2), D2 (the eraser) and D4 (the arena pair) are
one computation reported three times.

### F7 — DISCLOSURE. Proposition 3.3's covariance sweep is 30 non-vacuous checks on one boundary

"Over every one of the 6 and 24 relabellings and every one of the 5 and 15
records … zero violations."  Measured: of the $6\times5+24\times15=390$
instances, the antecedent ("$B$ is admissible") is true in exactly
$6+24=30$, and every one of those 30 is the discrete boundary carried to
itself.  Zero violations is correct and the statement is true for
structural reasons — every clause is defined equivariantly — but the
measurement tests one boundary.  §3.3 already discloses the counter-law's
$1$-of-$120$ vacuity; the DET vacuity is the same disclosure one step
earlier.

### F8 — STRENGTHENING (not a defect). Rigidity has an exact converse, and the axiom is a dichotomy

Theorem 3.1 gives one direction.  The converse is two lines and I could
not break it: for any left-total law, $n$ pairwise-disjoint nonempty
supports inside an $n$-element carrier forces every support to be a
singleton, so $\operatorname{Pres}_L(\delta)$ **is** the set of permutations
in $L$ — measured exactly on the full left-total family ALL$(n)$ at
$n=2,3,4$ — and any $F\in\operatorname{Pres}_L(\delta)$ separates every
pair, so (i-a) at $\delta$ reduces to
$\operatorname{Pres}_L(\delta)\neq\varnothing$.  A composition-closed set
containing a permutation of a finite carrier contains the identity.  Hence

> **the carrier's own algebra is admissible if and only if the law contains
> the identity.**

Measured over all 687 composition-closed sub-laws of $T_3$ generated by at
most three elements: the biconditional holds 687 of 687; the number of laws
admitting *both* the carrier's algebra and some proper chart is **0**; the
number of identity-free laws admitting at least one proper chart is **428**
— exactly the identity-free complement of the 259 identity-containing laws.
So the axiom is a strict dichotomy: a law has either exactly one chart (the
carrier's) or no carrier chart at all and possibly several proper ones.
This upgrades Proposition 3.4 from an example to the only possibility and
sharpens `BLOCKED-AT-CARRIER`.

### F9 — STRENGTHENING. Theorem 6.1 is a partition-lattice fact about every comparable pair

The proof uses nothing about the arena, nothing about DET and nothing about
the five configurations.  If $\pi$ strictly refines $\pi'$ then
$\operatorname{Pres}_L(\pi)\subseteq\operatorname{Pres}_L(\pi')$ for every
$L$ (images of $\pi'$-blocks are unions of images of $\pi$-blocks), and the
paper's own argument then kills the finer member whenever the coarser one
is admissible.  Measured: 0 of 135 comparable pairs at four configurations
under DET/REV/FUNNEL are jointly admissible; 0 of 687 sub-laws of $T_3$
admit both $\{01\mid2\}$ and the discrete boundary (246 admit the coarse
one only, 259 the fine one only).  Incomparable pairs genuinely differ —
Proposition 3.4's two proper charts coexist — so the general statement is
"no law admits two **comparable** boundaries", and that is the sharp form.
§6.1's "this is the sharpest thing this cycle earns" is fair; the paper
should claim the general version, which is strictly stronger and costs
nothing.

### F10 — HYGIENE. One inert guard in the (ii-b) decision procedure

In `adjudicate`, the first of the two nested tests for unrealized
identifications iterates `for blk in [written_of(F)] if x in blk` — `blk`
is bound to the whole partition, not to a block, so `x in blk` is never
true, the generator is empty and the guard is constantly `True`.  The inner
test carries the semantics and is correct, so **no number moves**; I
verified this by re-deriving (ii-b) natively with the intended semantics
and reproducing W3, the never-occupied atoms $\{1\},\{2\}$, and every §6
row.  It should be deleted, not repaired, since if it ever became live it
would test the wrong thing.

---

## 2. THE FOUR DISCRIMINATORS, RE-RUN NATIVELY

Family := the boundary's closure and preparation := the full carrier, i.e.
the unit's own §6 protocol, so the comparison is like-for-like.  Under the
committed DET law at five configurations:

| context | partition | $\lvert\operatorname{Pres}\rvert$ | $\ker(\mathfrak F)$ | (i-a) | (i-b) | (ii-a) | (ii-b) | admissible | agrees with paper |
|---|---|---|---|---|---|---|---|---|---|
| ALIGNED211 — **member 1, forged** | $01\mid2\mid3\mid4$ | 240 | discrete | ✗ | ✓ | ✗ | ✓ | **no** | ✓ |
| ALIGNED1111 — **member 2** | discrete | 120 | discrete | ✓ | ✓ | ✓ | ✓ | **yes** | ✓ |
| ALIGNED22 | $01\mid23\mid4$ | 420 | discrete | ✗ | ✓ | ✗ | ✓ | no | ✓ |
| ERASER | discrete | 120 | discrete | ✓ | ✓ | ✓ | ✓ | yes | ✓ |
| ADDRESS | discrete | 120 | discrete | ✓ | ✓ | ✓ | ✓ | yes | ✓ |
| TOMO | $0123\mid4$ | 1280 | discrete | ✗ | ✓ | ✗ | ✓ | no | ✓ |
| MAN211/MAN22/MAN1111 | — | — | — | — | — | — | — | no, at typing | ✓ |

**D1, the colluding pair.**  Member 1's witness reproduces exactly: the
closure has 240 members, contains the identity, the identity's written
record is discrete, and it separates configurations 0 and 1, which the
boundary asserts are one atom; so $\ker=\delta\neq\pi_1$ and (i-a) fails
with (ii-a).  Confirmed.  Qualified by F1 (declaration-relativity) and F4
(law-relativity).

**D1′, the member-2 leak test** (protocol's explicit charge).  My finding:
**not a leak in the paper's sense, but the certificate is issued to a patch
the unit constructs rather than to the context the adversary declared.**
Three readings tested.
*Reading A — both members admissible at once:* False under DET, FUNNEL, REV
and the counter-law, and False after paying member 1's price of 120
(measured on the altered 3005-operation law: member 1 becomes admissible,
member 2 becomes inadmissible in the same breath, exactly as Theorem 8.5
says).
*Reading B — admissible under some common law:* False on all four committed
laws, False on all 687 sub-laws of $T_3$, and proved for every comparable
pair (F9).  $\operatorname{Pres}(\delta)\subseteq\operatorname{Pres}(\pi_1)$
confirmed natively.
*Reading C — the boundaries' compatibility:* member 2's boundary refines
member 1's, so the pair is comparable and reading B bites.
Under every joint reading the pair fails, and the forged record — the
collusion's object — lives at member 1's boundary, which is rejected at
every identity-containing law.  The residue is this: member 2 is admissible
**only** for the declaration $\mathfrak F=\operatorname{Pres}_L(\delta)$.
Declare the identity alone, or the 60 even permutations, and member 2 fails
(i-b) too.  The axiom never reads what family the arena's second context
actually declared, so "member two is admissible, and correctly so" is a
statement about the canonical patch at that boundary.  That is defensible —
(i-b) makes the canonical patch the only candidate — but it should be said.

**D2, the legitimate eraser context.**  Passes all four clauses; closure is
the 120-member reversible family; its minimal sufficient boundary is the
five-atom boundary itself; every member writes the discrete record; reach
is the whole carrier.  Confirmed — and identical, computation for
computation, to member 2 and to the address context (F6).

**D3, the relabelled context and the counter-law.**  The cyclic shift of
the discrete boundary is discrete and admissible: confirmed, and correctly
reported as covariance rather than as a discrimination.  Under the
counter-law (regenerated natively from the 52 repreparation maps: 120
members, exactly one reversible, all 52 records fixed, exactly 1 of 120
relabellings preserving it) the address context stays admissible with a
declared family of **one** task, the forged boundary stays inadmissible,
and the admissible set is again the singleton $\{\text{discrete}\}$.  The
certificate collapse 120 → 1 is real and is disclosed.  One number the
paper does not print and could: $\lvert\operatorname{Pres}_{L_R}(\pi_1)\rvert=9$.

**D4, the arena's own two contexts.**  Same partition, same family size,
both admissible: confirmed.  The derivation "same boundary ⟹ literally the
same patch" is right and is the cleanest thing (i-b) buys.

**D5, the three constructed contexts.**  Not carrier-typed — the $2{+}1{+}1$
images $\{0,1,2\},\{0,1,2,3\},\{0,1,2,3\},\{4\}$ overlap, so no partition,
so (i-a) cannot be posed.  Confirmed, and §6.6's limitation statement is
the right one.

---

## 3. THE FEYNMAN GATE, RECOMPUTED

State $\rho=(1/16,1/16,1/16,1/16,3/4)$, verified to sum to exactly 1 and to
match the committed eraser likelihoods $3/4$ and $1/4$ under a uniform
source.  Both statistics re-implemented from Definition 7.1's formulas.

| quantity | patch | paper | R3 native | verdict |
|---|---|---|---|---|
| $\sigma$ | discrete boundary, closure (120 tasks), admissible | $1$ | $1$ | ✓ exact |
| $\sigma$ | discrete boundary, closure + erasure (121 tasks), inadmissible | $3/4$ | $3/4$ | ✓ exact |
| $\sigma$ | forged boundary, closure (240 tasks) | $1$ | $1$ | ✓ exact |
| $\delta$ | discrete boundary, closure | $0$ | $0$ | ✓ exact |
| $\delta$ | forged boundary, closure | $1/16$ | $1/16$ | ✓ exact |

The positive is real: two patches sharing boundary, law and state and
differing only in declared family separate at $1$ vs $3/4$, both rational,
`EMPIRICALLY-IDLE` correctly does not occur.  I also confirm the mechanism
by hand: at the forged boundary $\Pr(\{0,1\})=1/8$ while the best
single-outcome mass inside that atom is $1/16$, so $\delta=1/8-1/16=1/16$ is
exactly the mass on which the later readout resolves the asserted atom's
split — the paper's reading of the number is correct.

**The honest half's no-admissible-comparator claim: CONFIRMED, and stronger
than stated.**  At $\pi_1$ under DET no declaration whatsoever yields an
admissible patch — I tested five declarations directly (closure,
written-exact, merging, single repreparation, identity alone: all
inadmissible) and the general reason is Theorem 3.1 applied to condition
(i), which is declaration-independent because (i-b) pins the family.  So
"rigidity leaves no admissible comparator there" holds for every patch at
that boundary, not merely for the canonical one.

**But see F3** (the comparator's kill-list is (i-b) *and* (ii-a), not
(i-b)) **and F5** ($\sigma$ is not a function of admissibility at the fixed
boundary: the inadmissible patch $(\delta,\{\mathrm{id}\},\mathrm{DET})$
also gives $\sigma=1$).

---

## 4. THE TEN DECLARED DEVIATIONS, ADJUDICATED

| # | deviation | adjudication |
|---|---|---|
| 1 | condition (ii) split into WRITTEN + OCCUPIED | **material, correctly handled.** The split is what makes Theorems 3.2 and 4.3 statable, and the entailment is reported as a limitation rather than smoothed. No fix. |
| 2 | the pin expected (ii) to be the killing condition; measured (i-a)+(ii-a) | **fix-real.** The measurement is declaration-relative (F1): under the written-exact or merging declarations the kill is (i-b) alone. The deviation is honestly declared; the sentence it declares needs the qualifier. |
| 3 | the (ii)-only cell runs through occupancy | **cosmetic as stated, but it exposes F2.** Forced by Theorem 3.2, correctly. W3 vs W1 differ only in a datum Definition 2.1 says a patch does not carry. |
| 4 | #103-minimality computed at sector-support granularity; the letter-side numbers 1 and 5 anchored separately as controls | **fix-real-lite, and the protocol was right to flag it.** The identification — "the quotient by $\approx$ is the minimum-rank retract through which every declared task factors" — is *true at this scope* (for a family of left-total sector maps the minimum-atom-count retract is exactly $X/\ker$, one line) but it is **asserted, never proved and never gated**. Anchors M11/M12 pin the #103 numbers 1 and 5, and neither constrains (i-a) in any way: deleting both would change no verdict in the paper. So (i-a) borrows the #103 name while the anchors carrying that name are inert with respect to it. Fix: one line of proof, or one gate that recomputes the minimum-rank retract at the fixture and compares. No number moves. |
| 5 | boundaries presented at the committed carrier; typing gate carrier-relative | **cosmetic.** Declared, and §6.6 states the limitation in the strongest available form ("reproduces rather than extends"). |
| 6 | two controls beyond the pin's four | **cosmetic, and both earn their place.** The identity-free control is load-bearing (without it Theorem 3.1 reads as a triviality); joint unforgeability is the cycle's strongest result. |
| 7 | the same-boundary form could not be run at the forged boundary | **declared and confirmed, but incomplete.** The third limitation (F5) is missing from the same list. |
| 8 | tower levels record → boundary → coarser → limit; pair level proved impossible | **cosmetic.** Matches what is proved; the pin's "law" level is honestly mapped to the limit row, where what remains genuinely is another law (5 constant maps, composition-closed, verified). |
| 9 | the cost admits alterations leaving the committed class; two readings reported | **fix-real-lite.** Both readings are stated and the numbers are right under reading (a) — pay 120/360/1260/3120 and leave the class — and unpayable under reading (b), inside it. What is not said is that reading (b) is **not an independent cost result**: $\mathrm{id}\in\operatorname{Pres}_L(\pi)$ for every $\pi$, and the identity separates inside every non-singleton block, so "every obstruction contains the identity" is Theorem 3.1's mechanism restated, true by one line for every identity-containing law and not only for the obstructions computed. The abstract also orders the two readings numbers-first while §8.4 orders them strength-first; Deviation 9 claims "the stronger one is stated first". Fix: one sentence, and align the abstract. |
| 10 | Lean none; no new primitive | **cosmetic, and verified.** Every object the axiom uses is $\ker$, $\operatorname{Pres}$, $\operatorname{comp}$, $\operatorname{Reach}$ — all committed. |

**Deviations appendix completeness: FAILS by three.**  Undeclared:
(U1) in §6 the declared family is supplied as the boundary's closure and
the preparation as the whole carrier, so (i-b) and (ii-b) are true by
construction for every context adjudicated (F1);
(U2) the patch is a quadruple, not the triple of Definition 2.1 (F2);
(U3) the Feynman comparator's printed kill-list is incomplete (F3).

---

## 5. NUMBERS TABLE (paper/receipt vs R3 native)

| # | quantity | paper/receipt | R3 native | route |
|---|---|---|---|---|
| 1 | record-lattice sizes, 1–5 configurations | 1, 2, 5, 15, 52 | 1, 2, 5, 15, 52 | own set-partition enumerator |
| 2 | FUNNEL family sizes, 2–5 | 3, 7, 13, 21 | 3, 7, 13, 21 | identity + elementary merges |
| 3 | DET / REV cardinalities at 5 | 3125 / 120 | 3125 / 120 | $5^5$ / $5!$ |
| 4 | counter-law: members / reversible / records fixed / preserving relabellings | 120 / 1 / 52 / 1 | 120 / 1 / 52 / 1 | regenerated from the 52 repreparations |
| 5 | DET and REV fixed-record counts | 1,2,5,15,52 and 1,1,1,1,1 | identical | $\operatorname{Core}(\operatorname{Pres}(\pi))$ |
| 6 | Example 4.2: closed / comps / records fixed | yes / 3 listed / 4 of 5 | yes / identical / 4 of 5 | own composition table |
| 7 | rigidity sweeps: admissible set | $\{\text{discrete}\}$ in 16 of 16 | 16 of 16 | exhaustive, 4 laws × 4 sizes |
| 8 | closure sizes at the four carrier-typed boundaries | 120, 240, 420, 1280 | 120, 240, 420, 1280 | availability criterion; 240 and 1260 also by hand |
| 9 | $\sigma$ admissible / inadmissible / forged | 1 / 3/4 / 1 | 1 / 3/4 / 1 | Definition 7.1, Fractions |
| 10 | $\delta$ admissible / forged | 0 / 1/16 | 0 / 1/16 | Definition 7.1, Fractions |
| 11 | cost tower | 120, 360, 1260, 3120 | 120, 360, 1260, 3120 | $\lvert\operatorname{Obs}\rvert$; all four also by hand |
| 12 | operations remaining | 3005, 2765, 1865, 5 | 3005, 2765, 1865, 5 | complement sizes |
| 13 | complements: composition-closed and admissible after | yes, all 4 levels + 18 exhaustive rows | yes; 4/4 at $n{=}3$, 14/14 at $n{=}4$, 4/4 at the tower | own closure test |
| 14 | cost-scaling spot values ($n{=}3,4$) | 6, 24, 24, 96, 72 | 6, 24, 24, 96, 72 | hand-recounted |
| 15 | counter-law address-context family size | 1 | 1 | $\operatorname{Pres}_{L_R}(\delta)=\{\mathrm{id}\}$ |
| 16 | covariance violations at $n{=}3,4$ | 0 | 0 (of 390 instances, 30 non-vacuous) | exhaustive |
| 17 | identity-free control: admissible proper charts | $\{01\mid2\},\{0\mid12\}$ | identical, and exactly these two | exhaustive over 5 records |
| 18 | minimal witness verdicts W1/W2/W3 | yes / (i-b) / (ii-b) | identical; $\operatorname{Pres}(\{01\mid2\})=\{\mathrm{id},a\}$ | own adjudicator |
| 19 | float literals in the delivered source | none (AST sweep claimed) | none; 4 `/` sites, all `pathlib` | own AST scanner |
| 20 | **new** — $\sigma$ minimum over all 3005 one-task extensions | not reported | $3/4$, attained by exactly the 5 constant maps; 4 distinct values | exhaustive |
| 21 | **new** — laws admitting both a comparable pair | not reported | 0 of 687 sub-laws of $T_3$; 0 of 135 comparable pairs at $n{=}4$ | exhaustive |
| 22 | **new** — "discrete admissible ⟺ identity in $L$" | not stated | 687 of 687 | exhaustive |
| 23 | **new** — identity-free laws with a proper chart | not reported | 428 of 687 | exhaustive |
| 24 | **new** — boundaries admissible under the relative form (i-b′) at DET(5) | not reported | 52 of 52, including the forgery | exhaustive |
| 25 | **new** — $\lvert\operatorname{Pres}_{L_R}(\pi_1)\rvert$ | not reported | 9 | own criterion |

Anchor fidelity to Cycle B / B′ / #103 / #111: all 45 anchor rows show
committed = computed.  I independently reproduced anchors M01–M10, M13,
M20–M24 and M32 by my own routes (rows 1–6 above and the incidence
partitions, re-derived from the committed constructions rather than the
matrix code), and cross-read M25 (14 of 15), M27 (the pair passes the gate
as independent), M28 (12 carrying relabellings), M29 (4 of 15), M30
(dependent, 120 witnesses) and M31 (51 of 52) directly against
`v13/paper-rq0-composite-boundaries.md` §7.7, §5.2, §5.5 and §6.4 — every
value matches the predecessor's committed text.  M11/M12/M14–M19 need the
operator machinery and are outside my lens; I note only that M11/M12 are
inert with respect to (i-a) (Deviation 4).

---

## 6. COMMON GATES

| gate | result |
|---|---|
| paper-vs-receipt sweep (≥10 each) | **PASS** — 25 quantities checked in both directions; every paper number appears in the receipt with the same value, and no receipt number contradicts the prose. One receipt field is asserted rather than computed (F3). |
| scope tags | **PASS with one gap** — `[FIN]`, `[EXH-5]`, `[EXH-4]`, `[ARENA]`, `[FIX]` are attached to every numbered result and each matches what was actually swept (I verified [EXH-5] on Theorems 3.1/3.2/6.1/8.5 and [EXH-4] on Prop 3.3 and Lemma 8.2/Theorem 8.3). Gap: the abstract carries no law scope on the member-1 sentence (F4). |
| forbidden vocabulary | **PASS** — 9 hits for locality/topology/causality/spacetime/QFT/gravity/manifold, all inside the scope box (l.109, 125–127), Definition 4.2's disclaimer (l.376–377) or the non-claims (l.790–796). The "reachability carries no spacetime reading" line holds everywhere; §4.2 and §10 restate it at the point of use. |
| prose vs gates | **PASS with F3** — each §-level claim maps to a gate row (L2-01…L2-20, 21 passed, 0 failed) and the gate texts do not overclaim relative to their `ok` conditions. The single exception is the Feynman comparator's `fails` string, which no gate condition tests. |
| deviations appendix complete | **FAIL** — three undeclared (U1–U3, §4 above). |
| mutants / determinism / floats | **PASS** — 8 anchor mutants and 6 derivation mutants declared with kill conditions that are the right ones (each perturbs a clause so that the corresponding discriminator cannot fire); determinism claim (no wall-clock in receipt or rendered output) is consistent with the source, where timing appears only on the progress stream; exactness independently confirmed by my own AST sweep (row 19). |
| single-threaded | **PASS** — no correction rounds, no review archaeology, no "we first thought" narration anywhere in the paper. |

---

## 7. STAGE 5, ANSWERED FROM THE INSTRUMENT SIDE

The protocol requires an answer to K1's consequence question — *are coarse
patches ever admissible in physical laws, or does the axiom need a
relative/approximate form?*  Measured answer, in four parts.

**(1) The blockade is exact, not incidental.**  By F8, admissibility of the
carrier's own algebra is *equivalent* to the law containing the identity.
So the axiom sorts every law into exactly one of two bins: laws that can
idle, whose unique chart is the carrier itself and which admit no proper
chart at all; and laws that cannot idle, which admit no carrier chart and
may admit several proper ones (428 of 687 at three configurations do; two
of them coexist in Proposition 3.4's control).  There is no law in between:
0 of 687.  An atlas that contains both a fine chart and a proper coarse one
of the same carrier is therefore impossible under a single law — not
difficult, impossible.

**(2) So coarse patches ARE admissible — but only where nothing may be left
alone.**  That is a real class of laws and the paper is right to run the
control.  Whether the programme's charts live there is the open question,
and it is stated as open in §9.

**(3) The obvious relative form repairs the blockade and destroys the
discriminator — measured.**  Weaken (i-b) to the closure intersected with
the WRITTEN clause, $\mathfrak F=\{F\in\operatorname{Pres}_L(A(B)):
\operatorname{comp}(F)=A(B)\}$ — the most natural "relative" reading, and
the one Theorem 3.2 makes available for free.  Under it, at DET with five
configurations, **all 52 boundaries become admissible, including the forged
$\pi_1$** (with $\lvert\mathfrak F\rvert=120$, all four clauses passing).
The same holds for the aligned $2{+}2$ boundary (60 tasks) and the
tomographic minimum (20 tasks).  The axiom's power against the colluding
pair and its blockade of coarse charts are **the same mechanism**: both are
carried by the identity's presence in the closure.  Confirmed from the
other side by F4: at an identity-free law the forged boundary passes all
four clauses.

**(4) What this leaves for stage 5.**  Any relative or approximate form
that admits a proper chart at an identity-containing law must, by the
dichotomy, also admit the forged boundary — unless it reads a datum the
axiom currently does not: the family the adversary *actually declared*
(which §6 discards, F1), or a cross-patch condition on the atlas rather
than a per-patch one.  The part of this cycle that transports is
therefore **the joint statement, not the single-patch one**: Theorem 6.1
generalized (F9) says no law admits two comparable boundaries, at every
law, with no arena input.  That is the shape an atlas condition would have
to take, and it is already proved here.  My recommendation to the
adjudication: register the dichotomy (F8) alongside `BLOCKED-AT-CARRIER`,
and treat the relative-form route as *measured closed* in its naive form
rather than open.

---

## 8. PER-RUNG CONFIRMATIONS

**(a) The four discriminator verdicts, including the measured (i-a)+(ii-a)
joint kill — CONFIRMED**, every verdict and every family size reproduced
natively (§2).  Qualified by F1 (the kill-list is declaration-relative) and
F4 (the single-member verdict is law-relative).

**(b) The rigidity theorem and its identity-free control — CONFIRMED.**
16 of 16 sweeps return the singleton $\{\text{discrete}\}$; the control law
$\{a,b\}$ is composition-closed, identity-free, and admits exactly the two
proper charts $\{01\mid2\}$ and $\{0\mid12\}$ — it is a genuine law of the
committed class, not a bespoke escape (closure verified by my own
composition table).  **Strengthened** by the exact converse (F8).

**(c) Joint unforgeability, Theorem 6.1 — CONFIRMED at the "for every
admitted law" quantifier**, and I could construct no escape: the inclusion
$\operatorname{Pres}_L(\delta)\subseteq\operatorname{Pres}_L(\pi_1)$ holds
for every left-total law by a lattice argument, and the edge case
$\operatorname{Pres}_L(\delta)=\varnothing$ still kills member 2 through
the empty-family convention.  Measured on 4 committed laws, 687 sub-laws of
$T_3$ and 135 comparable pairs at four configurations: zero joint
admissions.  **Generalizes** to every comparable pair (F9).

**(d) The Feynman gate's positive form and its honest half — CONFIRMED
numerically** ($1$ vs $3/4$; $0$ vs $1/16$; no admissible comparator at the
forged boundary, verified for five distinct declarations and proved for
all).  **Two fixes** required: F3 (the comparator fails two clauses) and F5
(the third honest half).

**(e) The cost tower, the exact-$\lvert\mathrm{Obs}\rvert$ proof and the
pair-level impossibility — CONFIRMED.**  All four levels reproduce; the
complement is composition-closed and the boundary admissible in it at every
level and at every non-discrete boundary at three and four configurations
(4/4 and 14/14, exhaustive, my own closure test); additions never help — at
five configurations DET is the full transformation monoid so no addition
exists at all, and at FUNNEL(4), where additions do exist, 0 of the closed
one-task extensions removed an obstruction member; the pair level is
impossible, verified on the altered 3005-operation law.  Qualified by
Deviation 9's adjudication (the "no forgery inside the class" reading is
Theorem 3.1 restated).

**(f) The rung pair `GENERATIVE-ATLAS-AXIOM` + `BLOCKED-AT-CARRIER` as the
correct pre-registered instantiation — CONFIRMED.**  Both earn at the
declared scope; `EMPIRICALLY-IDLE` correctly does not occur (the pin's
wording is existential and the exhibit meets it); `CHEAP-LAW-FORGERY`
correctly does not occur.  The paired registration — the axiom earned
*jointly with* its price — is the honest bookkeeping, and F8 makes the
price sharper rather than smaller.

---

## 9. SENTENCES TO REWRITE

1. **Abstract**, "the two killing conditions are measured rather than
   assumed: (i-a) and (ii-a) fail together, on one exhibited witness" → add
   the declaration scope: *for the only declaration that could satisfy
   (i-b) — the boundary's closure — (i-a) and (ii-a) fail together on one
   witness; under any other declared family the patch fails (i-b) instead.*
2. **Abstract**, "The forged member of the colluding pair is
   **inadmissible**" → *is inadmissible at every admitted law containing
   the identity* (and note that at an identity-free law it can be
   admissible, which is why the joint statement is the load-bearing one).
3. **Abstract / §7**, "admissibility changes a number" → *some inadmissible
   patches are separated from the admissible one by an admitted number*;
   $\sigma$ is not a function of admissibility at the fixed boundary.
4. **§7.2 table**, "no, fails (i-b)" → *no; fails (i-b) and (ii-a)* — and
   compute the field rather than asserting it.  Same in the receipt's
   `feynman_gate.same_boundary_comparison.inadmissible_patch.fails`.
5. **Definition 2.1**, "A patch is a triple $P=(B,\mathfrak F,L)$" → a
   quadruple $(B,\mathfrak F,L,X_0)$; propagate to Definition 8.1 and to
   the abstract's second paragraph.
6. **§6 preamble**, add one sentence: *throughout this section the declared
   family is set to the boundary's closure and the preparation to the whole
   carrier, so clauses (i-b) and (ii-b) hold by construction; the measured
   content of each row is clause (i-a).*
7. **§6 table caption**, add: *three of the six carrier-typed rows present
   the same partition and are therefore the same patch (§6.5).*
8. **Proposition 3.3**, add the vacuity disclosure the counter-law sentence
   already models: *under DET only one boundary is admissible at each size,
   so 30 of the 390 instances have a true antecedent and all 30 are that
   boundary carried to itself.*
9. **§8.4**, after "Every obstruction computed here contains the identity",
   add: *and must, since the identity preserves every boundary and
   separates inside every non-singleton block — this reading of the cost is
   Theorem 3.1 restated, not an independent measurement.*
10. **Theorem 6.1**, state the general form: *no admitted law makes two
    comparable boundaries both admissible*; the colluding pair is the
    instance, and the proof already given is the general proof.
11. **Appendix A**, add deviations (U1)–(U3).
12. **§9 / adjudication input**, add the dichotomy (F8) and the measured
    closure of the naive relative form (§7 above).

---

## 10. WHAT I TRIED AND COULD NOT BREAK

- Theorem 3.1 in both directions, at four laws and four carrier sizes, and
  the identity-free control's closure — no escape; the control is a law of
  the committed class.
- Theorem 3.2's entailment — no counterexample over the exhaustive sweeps,
  including the full left-total family at four configurations or fewer.
- Theorem 6.1 at the universal quantifier, including the empty-closure edge
  case and 687 independently generated laws.
- Theorem 8.3's lower bound against constructed additions (FUNNEL(4), every
  composition-closed one-task extension): 0 cases where an obstruction
  member disappeared.
- Lemma 8.2 and the achievement of the bound: exhaustive at three and four
  configurations, 18 of 18, plus all four tower levels.
- The Feynman numbers: every one reproduces exactly, and the mechanism
  behind $1/16$ is the one the paper names.
- Exactness: zero float literals, zero arithmetic divisions in the source.

**Freeze-on-delivery.**  This file is R3's single repo output and is final
as delivered.  Scratchpad: `.../scratchpad/r3ga/{core,m1_anchors,
m2_discriminators,m3_feynman_cost,m4_stage5,m5_declaration}.py`.
