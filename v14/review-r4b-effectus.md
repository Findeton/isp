# R4b (paper-15, momentum) — EFFECTUS-LENS HOSTILE REVIEW

**Lens:** meaning, scope, motivation.  **Grade: AWF**
(accept-with-fixes).  **Recomputations: 234**, independent and
exact, rebuilt from the *parent's* definitions (R4 paper §3) in a
separate representation of Q(ζ₈); the delivered instrument was
never imported and never executed.  **False computed numbers
found: 0.**  Every delivered number reproduced, including all 58
census rows field-for-field, all 9 fiber rows, all 9 agreement
entries and all 19 circulant class rows.  The findings are all
about what the delivered sentences *claim* versus what the arena
*measures* — which is this lens's whole business.

**Object verified.**  All six pinned digests match under the
programme's sha256-12 convention: paper `5f8ec142319c`, code
`53a10e87ec19`, output `d33412225949`, receipt `00e7f6ea0f90`,
pin `bcd12bbe6fd8`, protocol `b9cd2133d961`.  Nothing drifted.

**Concurrent workers disclaimed.**  At review time the working
tree also carried, from other units, modifications to
`v14/code/w2_census_exact.py`, `w2_census_output.txt`,
`w2_census_receipt.json`, `v14/paper-13-weld2-carrier-census.md`,
and untracked `v14/code/u4_crystals_*` and
`v14/paper-14-u4-renewal-crystals.md`.  I touched none of them.
No git operation was performed; all execution was scratch-only
under `scratchpad/r4b-ef/`.  This file is my single repository
write.

---

## 0. What I rebuilt, and what it confirms

I re-derived the arena from the R4 paper's construction — the
25-element alphabet (0 together with ζ₈ᵗ times a modulus in
{1, ½, 1/√2}), the 9 axes as nonzero offsets modulo sign, the
stencil {0, a, −a}, unitarity as delta autocorrelation
A(m) = δ_{m,0}, and the global-phase quotient — swept every axis
exhaustively, and computed the symbol, the eigenphase, the
velocities, the drift, the winding and the point-group classes
from scratch.

Reproduced exactly, with no input from the delivered instrument:

| object | delivered | mine |
|---|---|---|
| circulant families | 58 | 58 |
| support histogram | 16 / 18 / 24 | 16 / 18 / 24 |
| monomial / non-monomial | 16 / 42 | 16 / 42 |
| eigen-equation, μ₈, unit modulus | 928 / 928 / 928 | 928 / 928 / 928 |
| non-constant dispersions | 57 of 58 | 57 of 58 |
| the constant family | C004, identity up to global phase | identity, coefficient −1 at (0,0) |
| parity a family invariant | 58 of 58 | 58 of 58 |
| distinct reduced dispersions | 58 | 58 |
| velocity cells, all even | 1856 | 1856 |
| speed spectrum, VMAX | {0,1,2}, 2 | {0,1,2}, 2 |
| aliased cells | 320 of 1856, 19 families | 320 of 1856, 19 families |
| the fiber, all 9 rows | 1856/1088/832/1536/768/704/1536/768/704 | identical |
| reach partition | 8 over / 14 under / 36 equal | 8 / 14 / 36 |
| agreement matrix, all 9 entries | 58,39,39 / 33,25,32 / 33,32,25 | identical |
| support drift table (tie-avg) | 16\|12, 18\|0, 24\|0 | identical |
| support drift table (positive) | 16\|15, 18\|10, 24\|8 | identical |
| interfering: moving / zero net | 42 / 42 | 42 / 42 |
| nonzero winding, all monomial | 12 of 16 | 12 of 16 |
| circulant extended classes | 19, sizes {1,2,4} | 19, sizes 4×[1], 3×[2], 12×[4] |
| the 19 class rows (size, supp, radius, v_max, aliased) | §5 table | identical, row for row |
| 64² − 48² | 1792 | 1792, and R4's Markov stratum is the 16 named monomials |

I also matched all **58 receipt census rows** to my rebuild by
coefficient map modulo global phase and compared *every* field
— support, radius, monomiality, the 16 eigenphases, the 16
reduced dispersions: **58 of 58 exact, zero mismatches**,
including the six σ-strings printed in §3.

Two structural facts the unit reports as measurements are in
fact **forced**, and saying so would strengthen it:

- The 4 zero-winding monomials are exactly the identity and the
  three self-antipodal shifts (0,2), (2,0), (2,2) — the unit says
  this in §8 and it is right.
- The 3 NOT-BLOCH-DIAGONAL classes are forced, not merely
  measured: Bloch-diagonal ⟺ circulant ⟺ translation stabiliser
  16, and the unit itself measures the brickwork stabiliser at 8.
  The unit reports the non-diagonality as a measurement (§2) and
  leaves the forcing on the table.

---

## 1. THE HEAD — honest, and its segments are not uniformly so

`R4B-DISPERSION-READ` is the honest head.  The three
pre-registered readings are genuinely reachable: the head law is
exercised in both directions (zeroed census → `R4B-NO-MOTION`,
gated), and `R4B-BLOCKED-AT-EIGENPHASE-OUTSIDE-MU-8` is a live
branch that the μ₈ measurement closes.  The head itself claims
only that the dispersions exist and were read, and §1's
disclaimer ("Reading a dispersion is not building a particle")
is the right one and is honoured throughout — no state is
propagated anywhere in the unit.

The segments are not uniformly honest.  Verdict segment by
segment:

| segment | verdict |
|---|---|
| `MOTION` | **clean.**  Every value is a property of the reduced dispersion and is invariant under every member of the declared fiber. |
| `DISPERSION` | **clean but one compressed comparison** (MINOR-4). |
| `VELOCITY` | **over-scoped.**  SPECTRUM, VMAX, INTEGER-VALUED and ALIASED are all functions of an ungated coordinate of the declared fiber (MAJOR-2). |
| `BOUND` | **over-scoped, and one key is mislabelled** (MAJOR-2, MAJOR-3). |
| `TRANSPORT` | **numbers clean; one word unearned** ("INTERFERING", MINOR-1). |
| `SCOPE` | **incomplete** — it does not carry the coordinate the BOUND and TRANSPORT segments depend on (MAJOR-1c). |

---

## 2. K2 — THE CONVENTION-SELECTION CLAIM (decisive)

### The claim as delivered

§1: "**the velocity convention is not free** … A convention that
was expected to be declared turns out to be selected by an
identity."  §7: "Exactly 1 of the 9 reading pairs makes the two
agree for every family."  §12: "the velocity definition (fiber 9,
printed in full in section 4, **with the declared member selected
by the identity of section 7**)."

### What I measured

§7's sentence is **true exactly as written** — I reproduced the
full 3×3 agreement matrix and exactly one of the nine
drift-reading × winding-reading pairs reaches 58 of 58, best
other 39.  §12's sentence is **not**.

The §4 fiber-9 is *lift × stencil*.  The §7 nine is *drift-tie ×
winding-tie*.  **These are different nines**, and the paper
silently identifies them.  I crossed the drift tie (3) against
the *full* fiber (3 lifts × 3 stencils = 9) — 27 combinations:

```
drift TIE-AVERAGED | winding TIE-AVERAGED  FORWARD  : 58  <== 58/58
drift TIE-AVERAGED | winding TIE-AVERAGED  BACKWARD : 58  <== 58/58
drift TIE-AVERAGED | winding TIE-AVERAGED  CENTRAL  : 46
      (all 24 others: 39 or below)
```

**Two of the 27 reach 58 of 58, not one.**  The identity of §7
does *not* select the declared member of the fiber-9.  It selects
the lift coordinate uniquely and narrows the stencil coordinate
from 3 to 2.  The residual fiber is **2**, and it is not
invisible: TIE-AVERAGED/BACKWARD differs from the declared
reading at **768 of 1856 cells** (the unit prints this itself, as
the 1088 row of its own fiber table, without drawing the
consequence).

### What actually forces the stencil — and it is already in the paper

§4 states a normalisation: "The sign is fixed by the requirement
that a monomial shift by an offset o have velocity o, and that is
what it does."  Elevate that from a sign-fixer to a criterion and
it does real work.  Measured over the 16 monomial families at
every momentum and both directions, counting only the
non-antipodal coordinates where the requirement is non-degenerate
(384 such coordinates):

| stencil | tie-averaged | positive | negative |
|---|---|---|---|
| FORWARD | **384/384** | **384/384** | **384/384** |
| BACKWARD | **384/384** | **384/384** | **384/384** |
| CENTRAL | 128/384 | 256/384 | 256/384 |

The central stencil **fails the unit's own declared
normalisation**, for every lift.  So the honest stratification of
the fiber-9 is:

| coordinate | fiber | status | mechanism |
|---|---|---|---|
| stencil | 3 → 2 | **FORCED** | the declared monomial normalisation, 384/384 vs 128 or 256/384 |
| lift | 3 → 1 | **SELECTED** | drift = winding at 58/58, best other 39/58 |
| residual | **2** | **DECLARED, measured inert** | every reported quantity identical under FORWARD ↔ BACKWARD; 768 of 1856 cell labels differ |

This is *stronger* than what the paper claims, and it is honest.
The instrument gates neither leg: the normalisation is stated in
prose and never tested, and the residual invariance is never
measured.

### Is "SELECTED, NOT DECLARED" an honest new category?

**Half-earned, and it must not be entered as a conclusion.**  Two
reasons, one fatal on its own.

**(i) The selecting identity is an arena artifact.**  §11's own
successor register proposes widening the modulus set, and points
at the R4-effectus review's constructive generator at the *same*
lattice size: c_a = ½ at a = (1,0), c_{−a} = i√3/2, over
Q(i,√3).  I computed it exactly (in Q(i,√3), no floats):

- unitary — exact delta autocorrelation, all 16 lags;
- eigenphases exact in μ₁₂: s(k_x) = [2, 7, 8, 1] ∈ Z/12;
- forward differences lifted: [5, 1, 5, 1], sum 12 ⇒ winding number 1;
- mean group velocity **v_x = −1**;
- Born drift **⟨Δx⟩_x = −1/2**.

**The drift = winding identity fails on the very generator the
unit's successor register is built around.**  The identity is not
a property of the velocity definition; it is a property of *this
alphabet*, which forces all 42 non-monomials drift-free — and the
R4-effectus review already proved that drift-freeness is
alphabet-relative and not theorem-forced.

RUNBOOK §15 is exactly on point: *"Claims of physical
significance are entered only for quantities GATED as invariant
across the unit's admissible arenas; arena-artifacts may serve as
instruments but never as conclusions."*  The identity is a
legitimate **instrument** — it does pick the lift here.  It is
not admissible as the **conclusion** "the velocity convention is
not free."

**(ii) It was not pre-registered.**  The pin's R2 says: declare
the definition as data, print the fiber if alternatives exist.
It registers no selection criterion.  The identity is a post-hoc
discovery — the paper says so honestly ("Two results were not
asked for") — and a criterion chosen after seeing which readings
agree is a coherence argument, not a forcing.

### Comparison with R4's connective: strictly weaker

R4's `CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1))` is a
derivation from an anchored datum to a **unique** answer: fiber 1,
reason printed, routing mutant dying at the named forcing gate.
Drift = winding universality is weaker on every axis: post-hoc
rather than pre-registered; leaves fiber 2 rather than 1;
arena-relative rather than theorem-grade; and gated only as a
count, never as a forcing.  The registry word must record the
difference.

### MAJOR-1 — the convention-selection claim over-reaches

**Repair (three parts, all exact).**

**(a)** Replace §12's clause.  From:

> the velocity definition (fiber 9, printed in full in section 4,
> with the declared member selected by the identity of section 7)

to:

> the velocity definition (fiber 9 = 3 lifts × 3 stencils,
> printed in full in section 4).  Its two coordinates resolve
> differently.  The **stencil** is forced to {forward, backward}
> by the declared normalisation — a monomial shift by an offset o
> has velocity o at 384 of 384 non-antipodal monomial
> coordinates under both, and at 128 or 256 of 384 under the
> central stencil, which therefore fails the definition's own
> sign-fixing requirement.  The **lift** is then selected among
> the surviving three by the identity of section 7, uniquely.
> The residual fiber is 2: every quantity this unit reports is
> measured identical under forward and backward, and the two
> differ only in the cell-level labelling of signed velocity, at
> 768 of 1856 cells.

**(b)** Rewrite §1's headline sentence.  From "**the velocity
convention is not free**" to:

> **the velocity convention is not free at this alphabet.**  Its
> stencil coordinate is forced by the definition's own
> normalisation; its lift coordinate is then selected, uniquely,
> by an identity between two independently computed transport
> functionals — an identity that holds at 58 of 58 families here
> and that fails at the first widening of the modulus set, so it
> is an instrument for fixing the convention in this arena and
> not a law about the definition.

Then add one sentence to §7, immediately after the matrix, giving
the counterexample: *the identity is alphabet-relative — on the
widened-alphabet generator the effectus review exhibits at this
same lattice size, the Born drift is −1/2 and the winding is −1.*

**(c)** Two new gates and two new verdict clauses.

- `G-STENCIL-FORCED-BY-NORMALISATION`: for every monomial family,
  every momentum, every direction, and every non-antipodal offset
  coordinate, v_j(k) = o_j — required to hold at 384/384 under
  forward and backward and to **fail** under central.  Falsifier:
  a mutant that admits the central stencil.
- `G-RESIDUAL-FIBER-INERT`: the speed spectrum, VMAX, the
  per-family v_max, the motion head and the aliasing census are
  bit-identical under forward and backward.  Falsifier: a mutant
  that perturbs one backward-stencil family.
- `VELOCITY` segment gains
  `DEFINITION=FORWARD-DIFFERENCE-WITH-TIE-AVERAGED(FIBER=9;STENCIL-FORCED-TO-2-BY-MONOMIAL-NORMALISATION;LIFT-SELECTED-1-OF-3-BY-DRIFT=WINDING;RESIDUAL-FIBER=2-MEASURED-INERT)`.
- `SCOPE` segment gains
  `VELOCITY-READING=FORWARD-DIFFERENCE-WITH-TIE-AVERAGED`, and
  `arena_declaration.law` names the two coordinates as data
  rather than saying "the declared discrete derivative".  This is
  what §15 requires: the BOUND and TRANSPORT segments are both
  functions of this coordinate, and a successor that inherits
  SCOPE verbatim currently does not inherit it.

### The second half — identifying the panel's unstated convention

This half **holds and is well built**.  The verbatim anchor
`VB-DRIFT-TABLE` carries the frozen R4-effectus table's three
rows including their numerals, bound to the byte-anchored review
`A-REV-EFFECTUS` (`f54fa11dfd07`), and `G-EFFECTUS-DRIFT-TABLE`
requires this unit's independent rebuild to produce 16|12, 18|0,
24|0.  The loop is closed: the review's bytes are frozen, so the
gate's literals cannot drift without the anchor failing.  I
reproduced both tables independently.  A genuine result: the
panel's convention was inferred, and is now measured.

**MINOR-2 — the "only under it" half is not gated, and one
reading is never printed.**  The gate's claim string says "Under
that reading, **and only under it**", but the predicate tests
only the tie-averaged table.  The positive reading is computed
and stored; the **negative reading is never computed at all**.  I
computed it: 16|15, 18|10, 24|8 — identical to positive, because
sign flips preserve nonzero-ness.  *Repair:* compute
`support_drift_table_negative_reading`, print it beside the
positive row in §7, and extend the predicate to require that
both alternative readings **fail** to reproduce the panel's rows.
Falsifier: a mutant that makes the positive table match.

---

## 3. K4 — THE CANCELLATION CLAIM (decisive)

### What is measured, and it is all correct

I reproduced every number: 42 non-monomial families, all with
non-constant reduced dispersion, all with nonzero cell speed at
individual momenta, all with **exactly** zero Born drift and
**exactly** zero mean group velocity in both spaces; 12 families
with nonzero winding, every one monomial, of 16 monomials; the
other 4 monomials are the identity and the three self-antipodal
shifts.  The Markov binding is real and not a numerical
coincidence: R4's receipt names its 16 monomial generators
explicitly and its `markov_pairs` = 1792 = 64² − 48² is exactly
the set of pairs with a monomial member (its complement,
`free_pairs` = 2304 = 48², checks out).

### The licensed sentence, at citable scope

> On R4's 58-family circulant stratum — d = 2, L = 4, the
> declared 25-element alphabet over Q(ζ₈), the single-occupation
> sector, and the declared forward/tie-averaged velocity reading
> — every one of the 42 non-monomial generators has a
> non-constant Bloch dispersion and a nonzero group speed at
> individual momenta, and every one has exactly zero Born drift
> and exactly zero mean group velocity; the 12 generators with
> nonzero mean group velocity are all monomial.  The parent
> panel's "charge without momentum" is therefore a true statement
> about **net one-step transport** and a false statement about
> **momentum-resolved velocity**, and the two halves of the
> panel's sentence are about different objects.

That is the whole of what the arena measures, and it is a real
result.

### Over-readings to kill

**MINOR-1 — "interfering" is a rename, not a measurement.**  In
the instrument, `interfering` is defined as `not monomial`.  Full
stop.  Nothing in this unit measures interference: §9 concedes
"No defect is recomputed — every defect number is inherited."
The link from non-monomiality to interference is real but it
lives in the *R4-effectus review's* support-overlap criterion
(support ≥ 2 ⇒ the diagonal defect is nonzero), not in this
unit's gates, and not in the R4 *paper*.  *Repair:* either (a)
say "non-monomial" in the verdict key and in §8's bullets and
carry "interfering" only where the inherited criterion is cited
by name, or (b) add one gate binding each of the 42 to the
parent receipt's own nonzero diagonal-defect row, which makes the
word earned.  (b) is cheap and I recommend it; the parent's
`defect_value_census` has the rows.

**Kill: "cancellation" as a mechanism.**  Nothing is propagated
in this unit; no state exists; no wavepacket is built; §9 says
so.  The measured object is a **sum over the dual torus that
equals zero**, and a Born expectation over offsets that equals
zero.  "Cancellation" is licensed as a *description of the
arithmetic* — the summands are individually nonzero and the sum
is zero — and it is not licensed as a claim that something
physically interferes destructively, nor that a particle would
fail to move.  The paper's §8 is careful; §1's headline
("**the tension … is a cancellation, not an absence**") is one
step past it.  *Repair:* §1 reads "is a cancellation in the
arithmetic of the net transport, not an absence of motion" — six
added words, and the claim becomes exactly what was measured.

**Kill: any forcing reading.**  The zero net transport of the 42
is **alphabet-relative**, proved by the parent's own panel and
confirmed by me above (drift −1/2 at the same lattice size over a
wider field).  No sentence may suggest the cancellation is
structural.  §9's "Not decided" paragraph covers this; §1 and §8
should carry a clause pointing at it.

**MINOR-4 — a compressed comparison in the verdict.**
`DISTINCT-REDUCED-PROFILES=58-VS-14-INVARIANT-LABELS` puts two
counts on different index sets side by side: 58 profiles on 58
*families*, 14 labels on 22 *classes*.  The paper says it
correctly; the verdict key invites the wrong reading.  *Repair:*
`DISTINCT-REDUCED-PROFILES=58-ON-58-FAMILIES-VS-14-LABELS-ON-22-CLASSES`.
(I verified R4's collision structure: 6 shared labels, the
largest shared by four classes — C000, C001, C020, C021 — exactly
as §3 says.)

---

## 4. K3 — "THE BOUND HAS NO CONTENT": a fact about what?

The protocol asks whether the emptiness is a fact about the
physics or about the arena's size.  **It is neither, as
delivered: it is a fact about the arena's size *and* an ungated
coordinate of the declared velocity reading.  And once that
coordinate is forced, the emptiness turns out to be structural at
every even L — not a resolution artifact of L = 4 at all.**  Two
findings.

### MAJOR-2 — the bound's numbers are stencil-dependent and ungated

Recomputing the whole census under each stencil:

| stencil | speed spectrum | VMAX | aliased | reach over/under/equal | one-step cone |
|---|---|---|---|---|---|
| FORWARD (declared) | {0,1,2} | **2** | 320 in 19 | 8 / 14 / 36 | **16 of 16** |
| BACKWARD | {0,1,2} | **2** | 320 in 19 | 8 / 14 / 36 | **16 of 16** |
| CENTRAL | {0, ½, 1} | **1** | 512 in 24 | 0 / 41 / 17 | **9 of 16** |

Under the central stencil — a printed member of the unit's own
fiber — VMAX is 1, strictly below the diameter, and the one-step
cone covers 9 of 16 sites, so **the cone leg of the "empty twice
over" argument would not hold**.  Every number in the BOUND
segment except the two inherited ceilings moves.  Nothing in the
unit gates this, and §9's "Decided … The propagation bound is
empty in both senses available at this scale" states it
unconditionally.

The unit is *defensible*: §7's identity excludes central
(46 of 58), and MAJOR-1's normalisation excludes it outright.
But the paper never connects K2 to K3, and the connection is the
whole justification.  As delivered, K3's emptiness rests on an
undisclosed dependence.

One further wrinkle: the code's predicate is
`bound_has_content = (not cone_covers) and not under`.  The
second clause makes a *nonempty undershoot set* sufficient to
void the bound.  That is the wrong test for an upper bound —
families whose reach falls below VMAX are perfectly consistent
with VMAX as an upper bound, merely not tight.  The clause is
why `NO-CONTENT=YES` happens to survive the stencil change, and
it survives for the wrong reason.

**MINOR-3.** `G-SPEED-CANONICAL`'s claim string asserts the speed
is "independent of **every reading in the fiber**".  It is not —
it is independent of the *lift*, which is what its stated reason
("the distance of an element of Z/8 to zero does not depend on
how the antipode is signed") actually covers, and the predicate
only ever evaluates the declared stencil.  The **paper's** §4
sentence is correct as written ("does not depend on how the
antipode is signed"); the gate's claim is the one that
over-reaches.  *Repair:* narrow the claim string to the lift, and
add the stencil invariance to `G-RESIDUAL-FIBER-INERT`.

### MAJOR-3 — VMAX = diameter is structural, not an L = 4 fact

This is the finding I most want the adjudicator to carry.

§6 presents "VMAX = 2 and the torus has max-norm diameter 2" as a
measured coincidence at the admitted scale, and §11 builds the
entire successor register on the premise that "**Every negative
result in section 6 is a resolution result, and resolution is set
by two numbers … Both are fixed by L = 4.**"  That premise is
false for the cone.

The group velocity is a phase difference per momentum step, so
|v| ≤ (L/2π)·π = L/2, and the max-norm diameter of (Z_L)^d is
exactly L/2 for even L.  **VMAX ≤ diameter by construction, at
every even L.**  Equality holds whenever some family attains the
antipodal phase difference — and the monomial shift by the
antipodal offset (L/2, 0) is a unitary member of the axis family
at *every* even L, with Δ_x s = L/2 at every momentum.  Measured:

| L | Δ_x s for the antipodal monomial | speed | diameter | VMAX = diameter |
|---|---|---|---|---|
| 4 | 2 | 2 | 2 | yes |
| 6 | 3 | 3 | 3 | yes |
| 8 | 4 | 4 | 4 | yes |
| 10 | 5 | 5 | 5 | yes |
| 12 | 6 | 6 | 6 | yes |

**So the one-step cone covers the whole torus at every even L, and
L = 8 will not change it.**  The cone's vacuity is a property of
defining group velocity as a discrete phase derivative on a
periodic lattice, not a resolution failure of the admitted size.

What L = 8 *does* change is the other number: the count of
max-norm radii strictly between 0 and the diameter goes 1 → 3
(and 1 → 2 at L = 6, 1 → 5 at L = 12).  That is the genuine
resolution parameter, and it governs whether a front can take
distinguishable intermediate values across **multiple** steps —
not whether a one-step cone binds.

**Repair.**  §6's "The cone" paragraph gains:

> This is not a fact about the admitted size.  The group speed is
> a phase advance per momentum step, so it is bounded by L/2,
> which is exactly the max-norm diameter; and the monomial shift
> by the antipodal offset is a family member at every even L and
> attains it.  The one-step cone therefore covers the whole torus
> at every even L, and no enlargement of the lattice makes this
> constraint bite.  What the admitted size does control is the
> number of interior max-norm radii — one here, three at L = 8 —
> and that is the number a multi-step front resolution would turn
> on.

§11's opening premise must be corrected in the same motion: only
the *interior-radius* and *dual-torus* halves of §6 are
resolution results; the cone is structural.  Gate it:
`G-CONE-VACUITY-STRUCTURAL`, computing VMAX and the diameter for
the antipodal monomial at L ∈ {4, 6, 8, 10, 12} and requiring
equality at each; falsifier, a mutant that perturbs one L.

### MAJOR-4 — `REACH-BOUND-FALSE-AT=14-OF-58` is mislabelled

An **upper** bound on reach is falsified by the families that
**overshoot** it — 8 of them.  The 14 that fall below are
consistent with an upper bound.  The verdict's single key ties
"bound false" to the undershoot count, which reads as "the bound
fails at 14 of 58" when the upper-bound failure is at 8 of 58.
The paper's §6 prose is correct and careful ("neither an upper
nor a lower bound"); the **verdict** — the citable object — is
not.  *Repair:* split the key into
`REACH-UPPER-BOUND-FALSE-AT=8-OF-58;REACH-LOWER-BOUND-FALSE-AT=14-OF-58;SATURATES-AT=36`,
and correct the `bound_has_content` predicate so the undershoot
set enters only the lower-bound clause.

### The propagator relation: measured, but half of it is renamed

The parent's remark — "the local family lives exactly where the
propagator cannot be resolved" — is carried at a verbatim anchor
and turned into two printed rows.  Assessment:

- **Momentum side: genuinely measured.**  4 points per axis, 8
  phase values, 320 of 1856 cells at the antipodal value in 19 of
  58 families.  I reproduced all of it.  This is a new
  measurement, not a rename.
- **Position side: a rename.**  "The lattice has three max-norm
  radius classes, 0, 1 and 2; its diameter is 2; the only radius
  strictly between zero and the diameter is 1" is a restatement
  of L = 4 with no dispersion input whatsoever.  The dispersion
  enters only via "the fastest family covers everything in a
  single step" — which MAJOR-3 shows is structural at every even
  L.  As printed, this side is a register row wearing the
  language of a relation.

*Repair:* §6 should say which side is which.  The momentum side
is the measured relation; the position side is a property of the
lattice, and its one interior radius is the successor's parameter,
not this unit's finding.

---

## 5. THE CHOICE INVENTORY, at the RSQ standard

The unit prints four declared items in §12.  Corrected and
completed:

| choice | fiber | status as delivered | status after repair | evidence |
|---|---|---|---|---|
| the momentum lattice (dual torus, 16) | 1 | DECLARED (pin) | DECLARED, fiber 1 at the admitted size — correct as delivered | the characters are the only simultaneous eigenbasis of the circulant family |
| the character convention | 2 | DECLARED jointly with the velocity sign | correct as delivered; the k ↦ −k recomputation is a real invariance measurement | speeds, heads, aliasing invariant; signed velocity and winding negate |
| the eigenphase branch | 1 | DECLARED | correct — the phase is the verified eigenvalue's exponent, and the reduction by s(0) is the gauge quotient | 928 verified eigenvalue identities |
| the velocity **stencil** | 3 | folded into "fiber 9, selected" | **FORCED to 2** by the declared monomial normalisation | 384/384 vs 128 or 256/384 |
| the velocity **lift** | 3 | folded into "fiber 9, selected" | **SELECTED to 1**, arena-relatively, by drift = winding | 58/58 vs best other 39/58 |
| the residual forward/backward | 2 | **not disclosed** | **DECLARED, measured inert** | every reported quantity identical; 768/1856 cell labels differ |
| the interference/non-monomial identification | — | **not registered** | either a rename, or bound to the parent's defect rows | 42 = non-monomial by definition in the instrument |
| the selection criterion itself (drift = winding) | — | **not registered** | **post-hoc, arena-relative** — an instrument, not a conclusion (§15) | fails at drift −1/2 vs winding −1 over Q(i,√3) |

The last two rows are missing from the delivered inventory
entirely, and the RSQ standard requires them.

**The deviations register.**  §12 leaves the programme's
false-claim count at 5, all prose, none in a computed artifact.
After this review the honest accounting is: MAJOR-1(a)'s §12
clause is a **sixth prose false claim** (it attributes to the §7
identity a selection the identity demonstrably does not perform —
two of 27, not one).  MAJOR-4 is the more serious entry: a
mislabelled key **inside the verdict string**, which would be the
programme's **first defect in a computed artifact**.  It is a
labelling defect, not a wrong number — every number in the
verdict is correct — but the register must say so rather than
carry "none in a computed artifact" unqualified.

**The prose ↔ receipt sweep.**  I extracted every integer token
from the paper and checked each against every scalar in the
receipt.  Under my tokenizer, 51 distinct numerals in 370
occurrences (the unit's own coverage gate counts 78 in 413,
including tokens my regex excludes — subscripted field elements,
"Z/8", "L/2", section numbers).  Residue with no literal receipt
match: the six σ-strings of §3 (present in the receipt as
`reduced_dispersion` arrays — I verified all six digit-for-digit
against my own rebuild) and three section numbers.  **No
unsupported numeral.**  Every headline number in every section
traces to a receipt path and to my independent recomputation.

---

## 6. THE SUCCESSOR REGISTER

### (a) R4c-multi (Fock / statistics)

| row | content |
|---|---|
| **R-R4B-1 — INHERIT** | the one-body momentum label: 58 distinct reduced dispersions on 58 families, exact in Z/8, gauge-reduced by s(0). The label separates the whole family, so a Fock grading on (k, s(k)) is well posed. This is the unit's cleanest hand-off. |
| **R-R4B-2 — DO NOT INHERIT** | *any* transport number. `INTERFERING=42-ZERO-NET-TRANSPORT` is a Born average over the dual torus **in the single-occupation sector**, which SCOPE declares. Multi-occupation changes the measure; the cancellation is a property of the uniform average, not of the generator. R4c must re-measure drift and winding in its own sector, and its pin must forbid quoting 42/12/16 as inherited. |
| **R-R4B-3 — THE FIRST QUESTION** | build a two-particle state supported on the **non-cancelling** momenta of one interfering family and measure its drift. The momentum-resolved velocity is nonzero at individual cells for all 42; if a legitimate multi-particle state selects those cells, "charge without momentum" dissolves in the multi sector and the cancellation is exhibited as a single-particle-uniform-measure artifact. Pre-register both outcomes. |
| **R-R4B-4 — CARRY THE WORD** | do not inherit "interfering". Either bind it to the parent's diagonal-defect rows (MINOR-1 repair (b)) or say "non-monomial". |
| **R-R4B-5 — CARRY THE READING** | the velocity reading is a declared arena coordinate: forward difference, tie-averaged, stencil forced to 2, lift selected, residual 2. Under §15 a multi-sector comparison must match it. |

### (b) R5-gauge

| row | content |
|---|---|
| **R-R4B-6 — THE PIN DATUM, FORCED** | the 4 brickwork generators are not Bloch-diagonal, and this is a **theorem**, not a measurement: Bloch-diagonal ⟺ circulant ⟺ translation stabiliser 16, and their stabiliser is measured at 8, index two. R5 opens with this as a forcing (the unit currently reports it as measured — a free strengthening). |
| **R-R4B-7 — THE BLOCK STRUCTURE** | the index-two stabiliser block-diagonalises them under the coarser character set, in 2×2 blocks. Their eigenphases will **not** lie in Q(ζ₈); R5's pin must declare the field it will construct and gate its exactness, and must carry `R5-BLOCKED-AT-EIGENPHASE-OUTSIDE-<field>` as a live outcome, exactly as R4b carried the μ₈ branch. |
| **R-R4B-8 — DO NOT INHERIT** | VMAX = 2, the aliasing census, the reach partition, `BOUND=NO-CONTENT`. All are circulant-stratum facts at a declared reading. What R5 *may* inherit is MAJOR-3's structural statement: on any even-L periodic lattice the one-step group-velocity cone is vacuous, so a gauge unit should not seek a light cone there. |
| **R-R4B-9 — INHERIT VERBATIM** | `CONNECTIVE=MAX-NORM(FORCED-BY-ANCHORED-LINK-(1,1))`, the SCOPE segment, and (after MAJOR-1(c)) the velocity-reading clause. |

### (c) R4b follow-ons

| row | content |
|---|---|
| **R-R4B-10 — THE ALIASING QUESTION, re-posed** | §11 asks whether direction-free cells survive an alphabet widening. Sharpen it: the widened generator's eigenphases leave μ₈ (I measured μ₁₂ for the effectus construction), so the successor must first determine the actual root order N and re-run the census in Z/N. The aliased value is then N/2, and the question is whether it is still attained. Pre-register both. |
| **R-R4B-11 — THE SELECTION'S DOMAIN** | the drift = winding identity is what selected the convention, so its domain of validity is the domain of the selection. Census its failure over a widened alphabet. One counterexample is already in hand at the admitted size: drift −1/2, winding −1. If the identity fails generically, the convention reverts to DECLARED and every transport number becomes reading-relative — which is the single most consequential open this unit leaves. |
| **R-R4B-12 — THE L = 8 QUESTION, corrected** | do **not** run L = 8 to test the cone; MAJOR-3 settles it in the negative for every even L. Run it to test the *interior-radius* count (1 → 3) and the multi-step front, which is where the resolution parameter actually lives. Note the constraint: R4's uniqueness theorem confines the local non-monomial family to L ≤ 4, so an L = 8 census is a census of monomials plus non-local families, and for monomials speed = reach identically — the reach partition will degenerate. Pre-register that degeneracy. |
| **R-R4B-13 — THE NON-CIRCULANT DISPERSION** | §9 leaves the index-two block decomposition unbuilt. It is the shortest path to a second dispersion stratum and it is a prerequisite for R5. |

---

## 7. Findings, ranked

**MAJOR-1** — the convention-selection claim over-reaches: the §7
identity leaves **2** of the 27 drift×fiber combinations at 58/58,
not 1; the stencil coordinate is forced by a different, stated,
ungated requirement; the residual fiber is 2 and undisclosed.
§12's clause is false as written.  Repairs in §2 above: three
parts, two new gates, two verdict clauses, one SCOPE addition.

**MAJOR-2** — §15 violation: SPECTRUM, VMAX, INTEGER-VALUED,
ALIASED and the whole BOUND segment are functions of an ungated
coordinate of the declared fiber (under CENTRAL: VMAX 1, cone
9/16, reach 0/41/17, aliased 512 in 24), and no invariance gate
exists.  Repair: `G-RESIDUAL-FIBER-INERT` plus the disclosure that
central is excluded by the normalisation, not by fiat.

**MAJOR-3** — "the bound has no content" is presented as a fact
about the admitted scale; VMAX = L/2 = diameter is **structural at
every even L** (the antipodal monomial always saturates it), so
the one-step cone is vacuous at every even L and L = 8 cannot fix
it.  §11's founding premise ("every negative result in section 6
is a resolution result … both fixed by L = 4") is wrong for the
cone.  Repair: §6 paragraph, §11 premise, one gate over
L ∈ {4,6,8,10,12}.

**MAJOR-4** — `REACH-BOUND-FALSE-AT=14-OF-58` labels the
undershoot count as the bound's falsification; an upper bound is
falsified by the 8 overshooters.  A mislabelled key inside the
verdict string, and the `bound_has_content` predicate's
`and not under` clause encodes the same error.  Repair: split the
key, fix the predicate.

**MINOR-1** — "interfering" is a definitional rename of
"non-monomial"; no interference is measured in this unit (§9
concedes it).  Repair: bind to the parent's defect rows, or say
"non-monomial".

**MINOR-2** — the drift table's "and only under it" is ungated,
and the negative reading is never computed.  I computed it:
16|15, 18|10, 24|8.  Repair: compute, print, and gate the
exclusion.

**MINOR-3** — `G-SPEED-CANONICAL` claims independence of "every
reading in the fiber"; true for the lift, false for the stencil,
and the predicate tests only the declared stencil.  The paper's
own sentence is correct.  Repair: narrow the claim string.

**MINOR-4** — `DISTINCT-REDUCED-PROFILES=58-VS-14-INVARIANT-LABELS`
compares counts on different index sets.  Repair: name both index
sets in the key.

**MINOR-5** — SCOPE and `arena_declaration.law` do not carry the
velocity reading's coordinates, though BOUND and TRANSPORT depend
on them; a successor inheriting SCOPE verbatim does not inherit
the coordinate.  (Folded into MAJOR-1(c).)

**MINOR-6** — the 3 NOT-BLOCH-DIAGONAL classes are reported as
measured when they are forced by the measured index-two
stabiliser.  Repair: state the forcing; it strengthens the unit
and it is what R5 will inherit.

---

## 8. THE LICENSED CLAIM

Everything below is measured, reproduced independently, and
survives at the arena's own declared scope.

> **On R4's terminal stratum — d = 2, L = 4, the 25-element
> alphabet over Q(ζ₈), the 3-term axis stencil, the
> single-occupation sector, the dual torus of 16 momenta declared
> as data, and the declared velocity reading (forward difference,
> antipodal tie averaged) — every one of the 58 circulant
> generators is diagonal in the lattice characters, every one of
> the 928 eigenvalues is an eighth root of unity, and the
> eigenphase is therefore an exact function into Z/8.  57 of the
> 58 families have non-constant reduced dispersion; the one
> exception is the identity.  18 of the 19 circulant classes
> move.  Every phase difference is even, so every group velocity
> is an integer; the speed spectrum is {0, 1, 2}; the antipodal,
> direction-free phase difference occurs at 320 of 1856 cells in
> 19 of 58 families.**
>
> **The maximal group speed equals the max-norm diameter — which
> is forced, on any even-L periodic lattice, by the antipodal
> monomial shift — so the one-step cone covers the whole torus
> and constrains nothing, here or at any larger even size.
> Family by family the group speed is neither an upper nor a
> lower bound on the one-step reach: 8 families overshoot it,
> 14 fall below, 36 saturate.**
>
> **The Born drift and the mean group velocity, computed by
> different code from different inputs, agree for all 58 families
> under exactly one of the 9 tie-reading pairs — the pair that
> averages the antipodal tie on both sides, against a best other
> of 39 of 58 — and that reading, and only that reading,
> reproduces the frozen R4 panel's one-step drift table
> (16 | 12, 18 | 0, 24 | 0) from an independent rebuild.  The
> panel's unstated convention is therefore measured rather than
> inferred.  The identity is an instrument for fixing the
> convention in this arena and not a property of the definition:
> it fails at the first widening of the modulus set, where the
> Born drift is −1/2 and the winding is −1 at this same lattice
> size.**
>
> **All 42 non-monomial generators have non-constant dispersion
> and nonzero group speed at individual momenta, and all 42 have
> exactly zero net transport in both spaces; the 12 generators
> with nonzero mean group velocity are all monomial, and the four
> monomials without are the identity and the three self-antipodal
> shifts.  "Charge without momentum" is therefore true of the net
> one-step transport and false of the momentum-resolved velocity
> — a cancellation in the arithmetic of the average, at this
> alphabet, which the parent's own panel proved is not
> theorem-forced.  The momentum label lives on the symbol and
> separates the whole family: 58 distinct reduced dispersions on
> 58 families, against 14 distinct invariant labels on 22
> classes.**

Nothing here is a claim about a state, a particle, a propagated
excitation, a continuum, an infinite volume, a long time, or an
interacting theory, and nothing here survives a change of
alphabet without being re-measured.

---

## 9. Grade

**AWF.**  The measurement is excellent and the arithmetic is
clean: I rebuilt the arena from the parent's definitions in a
different representation and reproduced every delivered number,
including all 58 census rows field-for-field.  The unit found two
real things it was not asked for, and the second (the panel's
unstated convention, measured) is a genuinely new kind of result.

What holds it back is scope discipline on exactly the two claims
the protocol made decisive.  The convention-selection claim
merges a forcing, a selection and an undisclosed residual, and
enters an arena-artifact as a conclusion in the teeth of §15.
The bound's emptiness is asserted at a scale when it is
structural at every scale, and its verdict key mislabels which
count falsifies it.  Every repair is small, every one is
supported by numbers the unit almost already has, and three of
the four MAJORs make the paper *stronger* rather than weaker —
MAJOR-1 upgrades a muddle into a clean forced/selected/inert
stratification, and MAJOR-3 upgrades a scale-relative negative
into a structural theorem.

**Repository writes: 1** (`v14/review-r4b-effectus.md`).  No git
operation performed.  All object digests re-verified unchanged
after all work.
