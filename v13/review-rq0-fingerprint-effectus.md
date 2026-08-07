# R2 — EFFECTUS / ORDER-LENS HOSTILE REVIEW

## Branch C, the Nomological Fingerprint Hunt — K2 (the corridor hole) and K3 (the dichotomy)

**Reviewer:** R2, effectus/order lens. **Protocol:** `v13/note-rq0-fingerprint-hostile-protocol.md` (c120ea3).
**Object:** `v13/paper-rq0-nomological-fingerprint.md` + `v13/code/rq0_l4_fingerprint_*` at 75e0977. **Pin:** b4fc87c. **Base:** a5cb096.
**Discipline:** own exact code, `/opt/homebrew/bin/python3.13`, exact rationals only, nothing imported from the unit, repo read-only, no git.
**Independent recomputations:** 24 (table §6). **Numbers that failed to reproduce: 0.**

---

## 1. Verdict

# ACCEPT-WITH-FIXES

Every number in the paper reproduces exactly on independent routes — the 12-orbit
census with its 52×52 iff, the group sizes 24/24/24/24/1, the whole fixture
table, the amnesty sweep 1276/2017/1552, the two survivor sets. No false
numerical result was found anywhere in this lens's remit. Theorems 7.1, 7.2 and
6.1 are sound as stated and correctly scoped.

The fixes are not arithmetic; they are three load-bearing sentences that
generalize measured tallies into laws, and one misattributed citation:

1. **The fingerprint dichotomy is a tally over twelve rows, not a theorem.** It
   is refuted as a general claim by five statistics I construct inside the
   declared data — one of which passes the *entire* corridor at the counter-law
   under **both** readings of gate 1, separates, and survives the amnesty sweep
   with zero inversions while being neither order-entailed nor state-reading.
2. **The inherited reading of G1 is not the reading its own anchor supports** —
   but the strict *exclusion* is nonetheless right, on a different and better
   warrant that is also inherited, and that the paper does not cite.
3. **The strict reading does not empty the class a fortiori.** It empties the
   declared six and nothing more.

None of this overturns a registered tag. `RQ0-L4-CLASS-IMPOSSIBILITY` is
reading-independent and survives intact; `RQ0-L4-FINGERPRINT-AMNESTY` is a
correct kill; the qualified `RQ0-L4-NOMOLOGICAL-FINGERPRINT` and its four
qualifications stand, and after fix 2 the disqualification of C1 is *stronger*
than the paper claims. `RQ0-L4-BLOCKED-AT-THE-REFINEMENT-ORDER` needs its
universal narrowed from "the corridor" to "the declared family".

---

## 2. Findings, ranked

### F1 — MAJOR (K3). The dichotomy is a pattern. Five counterexamples, all inside the declared data.

`L4-DICH` computes, in the unit's own source,

```
dich = all(order_entailed != swept_killed for e in the 12 separating rows)
```

— an XOR tally over the twelve (candidate, law) rows the unit happened to find.
It is not a proof that the two arms are exhaustive or exclusive, and they are
neither. Every construction below is a statistic of declared data only (the
declared boundary, and where stated the declared state) at the committed
carrier, at the committed state, at the committed preparation.

| | definition | separates? (2+1+1, 2+2 \| LEGIT) | monotonicity type off-fixture | amnesty sweep (sep, tie, **INV**) | order-entailed | state-reading | arm |
|---|---|---|---|---|---|---|---|
| **D1** | $\#\{r\in\pi:\lvert r\rvert=2\}$ | YES 1, 2 \| **0** | neither | 4845, 0, **0** | no | no | **NEITHER** |
| **D2** | $\sum_{\lvert r\rvert=2}\Pr(r)$ | YES 1/8, 1/4 \| **0** | neither | 4692, 153, **0** | no | **yes** | **NEITHER** |
| **D3** | $2\#\{\lvert r\rvert=2\}+\mathbb 1[\{0,1\}\in\pi]$ | YES 3, 5 \| **0** | neither | 4845, 0, **0** | no | no | **NEITHER** |
| **D4** | $\#\{r:\lvert r\rvert\notin\{1,4\}\}$ | YES 1, 2 \| **0** | neither | 4845, 0, **0** | no | no | **NEITHER** |
| **D5** | $(\tfrac12-\rho_4)\sum_r\lvert r\rvert(\lvert r\rvert-1)$ | YES −1/2, −1 \| **−3** | **anti-monotone** | 330, 165, **4350** | **yes** | **yes** | **BOTH** |

Four separations in neither arm; one in both. The dichotomy fails in both
directions, and it fails on statistics of exactly the kind the corridor was
built to adjudicate.

**D3 is the sharp one.** Run through the corridor on the 48 off-fixture records
by my own routes, at every committed law:

| gate | D3 @ DET/FUNNEL/REV/FC | D3 @ COUNTER-LAW |
|---|---|---|
| G3 nondegeneracy | pass | **pass** |
| G1 *pinned* (not refinement-monotone) | pass | **pass** |
| G1 *inherited* (non-monotone, either direction) | pass | **pass** |
| G2a not a function of ε | pass | **pass** |
| G2b not a function of the shape invariant | pass | **pass** |
| G5 covariance | **FAIL** (group 24) | **pass** (group 1, vacuous) |

D3 passes the **entire corridor at the counter-law under both readings of gate
1**, separates the committed pairs, and survives the amnesty sweep 4845/0/0. So:

- the corridor at the asymmetric law is **not empty under the strict reading
  either** — the strict reading kills C1 and C4c, and D3 walks in behind them;
- D3's separation is **not** order-entailed (it is not monotone in either
  direction) and **not** state-reading (it is state-blind), so Theorem 6.1 and
  the amnesty sweep both have no grip on it;
- D3 separates two boundaries of the *same shape* — $\{01\mid2\mid3\mid4\}\mapsto3$
  against $\{02\mid1\mid3\mid4\}\mapsto2$ — so it is **not** a function of the
  boundary's position in the refinement order.

That last point falsifies, as written, the sentence that carries
`RQ0-L4-BLOCKED-AT-THE-REFINEMENT-ORDER`: *"every separator the corridor admits
is a function of the boundary's position in the refinement order"*, and the
closing *"the only structure the committed pairs differ by that any admitted
statistic can see is how much they resolve."* D3 is admitted by the corridor and
sees the carrier's labels.

**D3 is not a cheat, and the paper half-knows it.** It exploits precisely the
vacuity the unit itself discloses at Deviation 8 — at the counter-law gate 5 has
no content. The paper treats that vacuity as a qualification attaching to *C1*.
It is not: it is a hole that admits an entire class of label-reading separators,
including ones that dodge Theorem 6.1 as well. The two theorems together do
**not** cover the class at the asymmetric law; they cover the declared family
there.

**D5 is the "both" case**, and it indicts the stated mechanism rather than a
number. It is covariant under the full 24 group, it is a statistic of the
declared boundary and the declared sink mass, and the unit's own G1 procedure —
which measures the monotonicity type **only at the committed state**
(`vals = {p: fn(p, law, PREP_FULL, RHO, 5) for p in OFF}`) — labels it
*anti-monotone*, hence "order-entailed", hence, per §5, a separator that "passes
the amnesty gate by construction". It does not: the sweep inverts it at **4350
of 4845** declared states.

### F2 — MAJOR (K2). A16's reading is not supported by A16's source.

The unit's §4.5 turns on one sentence: *"anti-monotone is monotone in the
refinement order."* The immutable base does not use the word that way. Stage-5
§1 and §9.1 both set the two terms in **contrast**:

> "Its one structural difference from ε is that it is *anti*-monotone under refinement, 0 violations over 4590 instances" (stage-5 §1, verbatim)

> "One honest consolation, and it is a genuine structural difference from ε: **ω is anti-monotone under refinement** — coarsening never raises it" (stage-5 §9.1)

If "anti-monotone" were a species of "monotone", both sentences would be
self-undermining: they exist to say ω is *not* what ε is. In this corpus's own
vocabulary "monotone" means order-preserving, so **"non-monotone in the
refinement order" does not exclude anti-monotone**, and the pin's literal gate 1
is not a narrowing of §10 — it is §10.

Two supporting points:

- §10's *argument* only reaches the order-preserving class. "The committed
  forgeries sit **below** the legitimate chart in the refinement order, so **no
  refinement-monotone statistic whatever** … can separate them by a threshold" is
  true of isotone statistics and **false** of antitone ones — an antitone
  statistic separates them by a threshold, which is exactly what C1 and C4c do.
  The constraint entailed by that argument is "not isotone", i.e. the pin's.
- **Anchor A16 is a substring-presence test.** The code checks that two literal
  strings occur in the immutable paper. That certifies the *words*; the semantic
  step from "non-monotone" to "excludes anti-monotone" is the unit's own
  inference and is not anchored by anything.

### F3 — MAJOR (K2/K4, provenance). The strict exclusion is right — on a warrant the paper does not cite, and that warrant is *about C1's own rows*.

The base already adjudicated the anti-monotone case, substantively, in the same
paragraph where it measures it:

> "where it is non-zero it therefore ranks the coarsest patch best, which is a grading of coarseness with the sign flipped rather than a reading of provenance" (stage-5 §1, verbatim)

and it did so on an explicitly counted set of rows:

> "That grading exists at **15 of the 155** (law, preparation) rows — **12 at FUNNEL, 3 at the counter-law**, and none at all under DET, REV or the funnel closure — and admits the legitimate patch at tolerance zero at **6** of them — all six at FUNNEL" (stage-5 §9.1)

I recomputed those rows from scratch: over 5 laws × 31 preparations = 155 rows,
ω ranks the legitimate patch strictly best at **15** rows — **12 FUNNEL, 3
counter-law, 0 at DET/REV/FUNNEL-CLOSURE** — and admits it at tolerance zero at
**6**, all at FUNNEL. These are, row for row, C1's separating rows: C1 is by
definition $\sum_{\text{31 preps}}\omega$, and the unit's own §4.4 reports C1
separating pointwise "at 12 of the 31 … at FUNNEL and at 3 of 31 at the
counter-law".

**So the corridor survivor's entire positive content is the immutable base's
already-published, already-dismissed ω grading, aggregated over preparations.**
The pin's C1 ("compare profiles, not points") returns separation exactly where
stage 5 already found it pointwise, and nowhere else.

This is the finding that repairs F2. The right citation for killing C1 is not
§10's word "non-monotone"; it is §9.1's verdict on these fifteen rows plus this
unit's own Theorem 6.1. That keeps the kill **inherited and substantive**,
removes the vocabulary claim the base contradicts, and closes a freeze question
the paper leaves half-open: Deviation 5 insists the order-entailment diagnostic
`L4-ENT` "neither gates a kill" and that "every kill in §4.5 is by a pinned
gate", yet under my adjudication of F2 the inherited column's kill of C1 is
carried by order-entailment. Citing §9.1 resolves that: the criterion pre-exists
the pin, in the immutable base, applied to these very rows.

### F4 — MAJOR (K2). The strict reading does not empty the class a fortiori.

Directly answering the protocol's question. The strict reading excludes *more
candidates*, so it empties the declared six. It does **not** make the remaining
class empty, and the gap is not hypothetical:

- **D1, D3, D4 are all measured type "neither"** — genuinely non-monotone — so
  they pass G1 under *both* readings. D3 additionally passes every other
  corridor gate at the counter-law and survives the sweep.
- Within the declared family, **C4a is already type "neither"** and passes both
  readings of G1; it dies at G2b. So the reading of G1 is not what empties the
  family — G2b, G2a and G3 do the work, and the strict G1 only adds the two
  anti-monotone candidates C1 and C4c to a list the other gates had already
  nearly filled.

The clean statement of what survives each reading:

| | pinned G1 | inherited/strict G1 |
|---|---|---|
| Theorem 7.2, covariant class at a symmetric law | **empty** | **empty** (identical — 7.2 never uses G1) |
| the declared six, all five laws | 1 survivor (C1 @ counter-law) | **0 survivors** |
| the class at the asymmetric law | **not empty** (D3) | **not empty** (D3) |

**The class impossibility is reading-independent; only the family-level
emptiness is reading-dependent.** That is the correct form of the answer, and it
is weaker than §9's "the impossibility extends to the whole declared family at
every committed law" invites a reader to hear.

### F5 — SIGNIFICANT. §5's mechanism is invalid as stated; the measurement that would license it is missing (and I supply it).

§5 claims the sweep's failure to kill C1 and C4c is "structural, not empirical",
because "monotonicity is a property of the order and the family, not of the
state". That is true of **state-blind** statistics (C4c, by construction) and
false in general — D5 is the counterexample, and D5 is covariant and lives on
declared data. C1 *is* state-dependent: ω reads ρ. The unit measures C1's
monotonicity type at the committed state only, then argues from a state-free
principle it has not established.

C1 survives anyway, and I can say so exhaustively rather than by sample. C1 is
**linear in the declared state** — $C1(L,\pi,\rho)=\sum_j\rho_j\cdot
\#\{\text{preps where }j\text{'s atom misses Reach}\}$ — which makes the type
computable at every declared state. Over all 224 comparable off-fixture ordered
pairs and all **4845** declared states: C1 is anti-monotone at **4845/4845** at
FUNNEL and at **4845/4845** at the counter-law (constant at DET). That is the
measurement §5 needs; it is not in the receipt.

### F6 — SIGNIFICANT. "The sweep's power is exactly co-extensive with state-reading" is false.

Non-claim 4 of §10. **D2** reads the declared state — its value is a declared
mass — and the sweep never inverts it (4692, 153, **0**). The sweep's power is
co-extensive with *state-reading that inverts on the chain*, which is strictly
narrower. (Note also that D2's sweep profile is numerically identical to C1's at
the counter-law, 4692/153/0, from an unrelated construction.)

### F7 — MODERATE. Total erasure is a property of the three separators found, not of separators.

§4.4's bolded "**Every separator certifies total erasure at its own separating
tolerance**" reads as a law. **D4** separates (0 against 1 and 2) and gives the
one-atom boundary **1 > 0**: the tolerance admitting the legitimate chart and
rejecting both forgeries rejects total erasure. True of C1, C4a, C4c; not true
of separators.

### F8 — MODERATE (scope, K1-adjacent but bearing on K2/K3). Theorem 7.2 is a theorem about the committed state's degeneracy.

The theorem needs the full 24-element group, which is the stabilizer of the
committed state's level partition. Over the declared simplex the group-size
histogram at DET is

| group size | 1 | 2 | 4 | 6 | 12 | 24 |
|---|---|---|---|---|---|---|
| declared states | **1200** | 2640 | 510 | 440 | 30 | **25** |

**25 of 4845** declared states carry the hypothesis; **1200** have a trivial
group, where the theorem has no content whatever (there the shape invariant is
the complete invariant and clause (ii) is unsatisfiable for trivial reasons).
The paper scopes the theorem correctly, but the abstract's "at the committed
configuration the corridor is provably empty" should carry this number: the
emptiness is purchased by the state's symmetry, not by the carrier or the law.

### F9 — MODERATE. The counter-law's trivial symmetry is an artifact of a label-reading construction.

The counter-law is the composition closure of the block-minimum idempotents of
all 52 partitions — maps defined by "send every configuration to the **least**
member of its block". "Least" reads the carrier's label order, so the family is
not stable under relabelling and its stabilizer is trivial. This is worth one
sentence in §7.5, because it explains the whole asymmetric case: the one law
whose gate 5 is vacuous is the one law *defined* by a label-reading rule — which
is exactly why label-reading statistics like D3 walk through gate 5 there.

### F10 — MINOR. "Survives the sweep" is not "separates at every state".

C1 at the counter-law ties at **153** of 4845 states; C4a ties at 2017. §5's
"their ordering on the triple is fixed at every state" is true only non-strictly.
One clause.

### F11 — MINOR, cosmetic. The receipt's anchors run A01…A14, **A16, A15**.

A16 fires before A15. No consequence; noted for tidiness.

---

## 3. The K2 adjudication, in full

**Which reading binds?** On the letter, **the pin's** (narrow: exclude
order-preserving only). Grounds: (i) the pin is the frozen authorization and
says "NOT refinement-monotone"; (ii) §10's supporting argument reaches only the
order-preserving class, since antitone statistics *do* separate by a threshold;
(iii) the base's own vocabulary contrasts "anti-monotone" with "monotone" in two
places, so "non-monotone" does not cover antitone (F2).

**Is the strict exclusion nevertheless correct?** **Yes** — but not as a reading
of §10's wording. Its warrant is (a) stage-5 §9.1's explicit verdict that an
anti-monotone grading "ranks the coarsest patch best, which is a grading of
coarseness with the sign flipped rather than a reading of provenance", delivered
on exactly the 15 rows C1 reuses (F3), and (b) this unit's own Theorem 6.1,
which proves the same thing structurally. So the substance of the unit's most
consequential deviation is right and its citation is wrong.

**Is the hole in the pinned corridor real?** **Yes.** The pin's gate 1 does not
exclude anti-monotone candidates; anti-monotone candidates separate the chain by
the order alone; C1 and C4c walk through. Reporting it rather than patching it
is correct, and §8.2's framing is right. The correction is to the *diagnosis* of
what closes the hole, not to the disclosure of it.

**Does the impossibility survive under both readings?** Split answer, per F4:
Theorem 7.2's class impossibility at a symmetric law — **yes, identically**,
because 7.2 never invokes G1. The declared-family emptiness — **only under the
strict reading** (1 survivor vs 0). The class at the asymmetric law — **no,
under either reading**: D3 is a corridor-admitted, non-monotone, sweep-surviving
separator there. The remaining class is not empty a fortiori; excluding
anti-monotone candidates removes exactly the two anti-monotone candidates.

**C1/C4c's anti-monotone walk, per reading.** Pinned: C4c is stopped at G2b
anyway (it is a function of the block-size profile hence of the shape), so only
**C1** walks, and only at the counter-law, where G5 is vacuous — one survivor,
as the paper reports and as I reproduce. Strict: both stopped at G1. Under my
adjudication both are stopped, C1 doubly — by Theorem 6.1 and by the base's own
prior verdict on its fifteen rows.

---

## 4. Sentences to rewrite

Ranked by how much they over-reach. Replacement text offered; the unit may
prefer its own words.

1. **§4.5**, *"and anti-monotone is monotone in the refinement order."*
   → *"and an anti-monotone separator's verdict on the chain is entailed by the
   order alone (Theorem 6.1), which is what the terminal cycle already ruled out
   on the anti-monotone case it measured: a grading that 'ranks the coarsest
   patch best … is a grading of coarseness with the sign flipped rather than a
   reading of provenance' (stage-5 §9.1)."*
   Same for **§2.1** ("the inherited G1 excludes **either** direction") and
   **Deviation 2**: attribute the strict exclusion to §9.1 + Theorem 6.1, and
   state plainly that A16 is a string anchor certifying the quotation, not the
   reading.

2. **§8.1 Theorem 8.1** — demote or qualify. It is an XOR tally over the twelve
   separating rows found. Suggested: *"**Observation 8.1** — over the six
   declared candidates and the five committed laws, every separation measured
   here is order-entailed or state-reading, and none is both (`L4-DICH`, a
   tally over the twelve separating rows). This is a property of the declared
   family, not of statistics on declared data: a state-blind non-monotone
   separator is in neither arm, and a state-dependent statistic measured
   anti-monotone at the committed state can be inverted elsewhere in the
   simplex, hence in both."*
   The same for the abstract's *"Over the declared family, every separation is
   either … No separation is both"* — keep the scope words, drop the tone of law.

3. **§9, `RQ0-L4-BLOCKED-AT-THE-REFINEMENT-ORDER`**, *"every separator the
   corridor admits is a function of the boundary's position in the refinement
   order"* and *"the only structure the committed pairs differ by that any
   admitted statistic can see is how much they resolve."*
   → restrict "the corridor admits" to "the declared family offers", and add:
   *"At the asymmetric law this is a statement about the declared family and not
   about the corridor: with gate 5 vacuous there, the corridor also admits
   label-reading statistics, which are neither covariant nor monotone and which
   neither theorem excludes."*

4. **§5**, *"the reason is structural, not empirical … monotonicity is a
   property of the order and the family, not of the state … **A monotone
   separator passes the amnesty gate by construction.**"* and the abstract's
   *"monotonicity is a state-free property."*
   → *"C4c is state-blind, so its type is state-free by construction. C1 is
   state-dependent (ω reads ρ), so its type is a measurement: C1 is
   anti-monotone at all 4845 declared states, which is why no state inverts it.
   A **state-blind** monotone separator passes the amnesty gate by construction;
   a state-dependent one passes it only as measured."*

5. **§10 non-claim 4**, *"the sweep's power is exactly co-extensive with
   state-reading"* → *"co-extensive with state-reading that inverts the chain;
   a statistic can read the declared state and never invert."*

6. **§4.4**, *"**Every separator certifies total erasure at its own separating
   tolerance.**"* → *"Every separator **found here** certifies total erasure at
   its own separating tolerance (`L4-ERASE`)"* — it is a measured property of
   C1, C4a and C4c, not a property of separators.

7. **Abstract / §7**, "at the committed configuration the corridor is provably
   empty" → add the scope number: the 24-element group is carried by **25 of the
   4845** declared states (1200 carry none), so the emptiness is purchased by the
   committed state's degeneracy.

8. **§7.5**, add one sentence on F9: the counter-law is generated by
   block-minimum idempotents, a label-reading construction, which is *why* its
   admitted-isomorphism group is trivial.

9. **§9 CLASS-IMPOSSIBILITY bullet**, *"the impossibility extends to the whole
   declared family at every committed law"* → keep, but append: *"the declared
   family is the ceiling: at the asymmetric law neither theorem excludes a
   non-monotone, non-covariant statistic, and one exists."*

---

## 5. Per-rung confirmations

| rung | verdict |
|---|---|
| **(a) CLASS-IMPOSSIBILITY (12-orbit theorem)** | **CONFIRMED.** 52 records → 12 orbits at each of the four symmetric laws; orbit ⇔ shape profile verified over all 52×52 = 2704 pairs at every law; 52 orbits and the iff correctly **false** at the counter-law. Reading-independent (7.2 never uses G1). Scope sharpening F8. |
| **(b) freeze discipline** | **CONFIRMED as recorded.** 45 gates, 16 anchors, 15 must-pass, 0 failures. `L4-FREEZE` sits at gate index 15; all 15 gates before it (`L4-00`, the six corridor-membership gates, `L4-G6`, the seven cross-checks) carry `fixture_touched_when_fired: false`; fixture/amnesty/covariance gates all fire after. I audited the recorded flags, not a re-run — the repo is read-only for this lens, so the definition-hash side of the freeze is R3's rung. |
| **(c) per-candidate kills** | **CONFIRMED**, all six candidates × five laws on my own routes: C2 monotone at every law (dies G1, G2a behind it); C3 fan-in ≡ 1; C4b a function of ε at DET/REV/FC and constant at FUNNEL/counter-law; C4a dies at G2b; C4c dies at G2b; C1 degenerate at DET/REV/FC and shape-functional at FUNNEL. Exactly one pinned survivor (C1 @ counter-law), zero inherited survivors. |
| **(d) the amnesty sweep** | **CONFIRMED exactly.** C4a 1276 / 2017 / **1552**, summing to 4845 at each of the five laws; C1 4844/1/0 at FUNNEL and 4692/153/0 at the counter-law; C4c 4845/0/0. |
| **(e) the C1 disqualification** | **CONFIRMED and RE-WARRANTED.** Honest and correct — and stronger than claimed: C1's separating rows *are* stage-5 §9.1's fifteen already-dismissed ω rows (F3). The citation should move from §10 to §9.1. |
| **(f) the fingerprint dichotomy** | **REFUTED as a general claim; correct as a scoped tally.** Five constructions inside the declared data: four in neither arm, one in both (F1). |
| **(g) the corridor-hole adjudication** | **PARTLY CORRECTED.** The hole is real and correctly disclosed; the pinned (narrow) reading binds on the letter; the strict exclusion is right on the §9.1 + Theorem 6.1 warrant, not on §10's wording; and the claim that the strict reading leaves nothing standing holds only for the declared six (F4, D3). |

**Common gates.** Paper-vs-receipt sweep: every table in §4–§7 matches the
receipt (fixture values, `admitted_isomorphism_action`, `amnesty_sweep`,
`identity_free_side` 3/1/12/2/2/2, `census_fan_in_resource` 874/175/699/428,
`c1_pointwise_profile` 0/12/0/0/3), and every one of those matches my
independent recomputation. Scope tags: present on every impossibility sentence
in §7 and §9 (`[FIN]`, `[OFF]`, `[FIX]`, `[SIMPLEX]`, `[CEN]`); the two
sentences that lack an adequate quantifier are items 3 and 4 above, and they are
quantifier problems ("every separator the corridor admits", "any admitted
statistic"), not missing tags. Forbidden vocabulary: clean — the only
occurrences of spacetime/locality/manifold/causal/gravity in the paper are the
explicit non-claims at the scope box and §10. Floats: none in any substantive
path. Deviations: eleven declared, all substantive, and the two that most needed
declaring (the two-reading G1 and the post-barrier diagnostics) are declared.
Single-threaded: the paper reads as one argument; no correction-round archaeology.

---

## 6. Numbers — independent recomputations

All computed in `/private/tmp/claude-501/-Users-felixrobles-workspace/82d34949-326c-4269-8dd0-587362126fa5/scratchpad/r2fp/`
(`core.py`, `a1_common.py`, `a2_sweep.py`, `a3_counter.py`, `a4_corridor.py`, `a5_c1state.py`),
exact rationals, no import from the unit.

| # | quantity | unit | R2 | ✓ |
|---|---|---|---|---|
| 1 | record lattice at five configurations | 52 | 52 | ✓ |
| 2 | law cardinalities DET/FUNNEL/REV/FC/COUNTER | 3125/21/120/3006/120 | same | ✓ |
| 3 | off-fixture population | 48 | 48 | ✓ |
| 4 | admitted isomorphisms per law | 24/24/24/24/**1** | same | ✓ |
| 5 | DET's group = Sym{0,1,2,3} | asserted | verified | ✓ |
| 6 | orbits of the 52 records | 12/12/12/12/52 | same | ✓ |
| 7 | orbit ⇔ shape profile, all 52×52 | true (symmetric laws) | true; false at counter-law | ✓ |
| 8 | orbit sizes of the committed triple | 6, 3, 1 | 6, 3, 1 | ✓ |
| 9 | ε at the fixture | 1/16, 1/8, 3/16 | same, all 5 laws (1-atom 1/4) | ✓ |
| 10 | C1 @ COUNTER-LAW | 95/8, 93/8, **45/4** | same | ✓ |
| 11 | C1 @ FUNNEL | 14, 13, **23/2** | same | ✓ |
| 12 | C4a fixture | 1/4, 1/4, **0** | same | ✓ |
| 13 | C4c fixture, and total erasure | −2, −4, **−12**; −20 | same | ✓ |
| 14 | C1 pointwise separating preparations of 31 | 0/12/0/0/3 | same | ✓ |
| 15 | amnesty C4a | 1276 / 2017 / **1552** | same (sum 4845) | ✓ |
| 16 | amnesty C1 FUNNEL / COUNTER-LAW | 4844,1,0 / 4692,153,0 | same | ✓ |
| 17 | amnesty C4c | 4845, 0, 0 | same | ✓ |
| 18 | monotonicity types, six candidates × five laws | per receipt | all 25 rows reproduce | ✓ |
| 19 | pinned corridor survivors | {C1 @ COUNTER-LAW} | same | ✓ |
| 20 | inherited corridor survivors | ∅ | ∅ | ✓ |
| 21 | ω rows ranking the legitimate patch best | (stage-5) 15 of 155; 12 F, 3 CL; 6 at tol. 0 | 15; 12 F, 3 CL; 6 | ✓ |
| 22 | states with the full 24 group, of 4845 | not reported | **25** (1200 trivial, 3645 nontrivial) | new |
| 23 | C1's monotonicity type over all 4845 states | measured at ρ only | anti-monotone **4845/4845** (F, CL) | new |
| 24 | D1–D5: gates, fixture values, sweeps | — | §2 table | new |

Comparable off-fixture ordered pairs used for every monotonicity measurement:
**224**. Declared simplex: **4845**, cross-checked by brute-force stabilizer on a
400-state prefix.

---

## 7. Limits of this lens

I did not re-run the unit's code (repo read-only), so byte-identical
reproduction and the 21 mutants are asserted from the receipt, not re-executed —
R3's rung. I did not rebuild the 745 identity-free census patches or the 2847-law
population; the `identity_free_side` and fan-in tables are checked
paper-vs-receipt only. Consequently my constructions D1–D5 are not gated against
G6 — I note that G6 kills nothing in the unit's own adjudication (C1 fails it
with 3 distinct values and is still the declared survivor), so D3's corridor
passage is established against exactly the standard C1 was held to. K1's edge
question (does some orbit pair share shape while differing in another covariant
datum) is R1's; my 52×52 iff check answers it in the negative at all four
symmetric laws.

---

*R2, effectus/order lens. Frozen on delivery.*
