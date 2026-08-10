# Γ-ITERATION (paper-16) — HOSTILE REVIEW, EFFECTUS (the meaning audit)

**Object (verified at my own hands):** paper `fd2f25d40002`, code
`fab2cdc1893e`, output `58ddd86a52f2`, receipt `8d28b5f2f807`; pin
`aa161f8f8e9d`; protocol `9f54f1083f21`. All six reproduce **as
sha256-12**, and working tree ≡ HEAD ≡ 9e481db for all four artifacts.
*(Protocol note: these are sha256-12, not git blob hashes; a reviewer
who verifies with `git hash-object` gets six mismatches. Worth one
clause in the protocol form.)*
**Assigned depth:** K4 (decisive: the three answers), the choice
inventory, the deviations register, the prose↔receipt sweep, the
successor register.
**Method:** full independent rebuild in scratch — the d42b1 layer
exec'd from its own pinned bytes (`576275d55ecf` verified), my own
canonical serialiser, my own partition refinement, my own potentials,
kernels, weights, Γ family, CK census, edge census, depth census,
R-SIG census. No import of the unit's code, no run of its delivery
script, one repo write.

**Standing: 113 independent recomputations, ZERO numerical
divergences.** Every delivered number within my reach reproduced
exactly, to the last rational. One apparent divergence (the descent
census) traced to *my* horizon convention and resolved in the unit's
favour. Not independently rebuilt, cross-checked against the receipt
only: the eq-22 matrix inversions, the eight LP verdicts, the square /
holonomy census (K1/K3/K5 — the operator's and instrument's turf).

**The defects are entirely in what the verdict CONCLUDES.** One
mechanism claim inside the verdict string is refuted on the unit's own
arena; one cap-scoping is backwards and its refuting datum was computed
in-run and discarded; one co-occurrence is promoted to a connection;
one "correction" compares two different objects.

**Grade: ACCEPT-WITH-FIXES (fixes BLOCKING — the head string must
change).**

---

## 1. Findings, ranked

### F-1 (MAJOR, decisive for K4(a)) — "the whole signature is carried by the multi-target edges" is refuted on this unit's own arena

The gate is `G-CARRIER-RELATIVE`. Its **statement** claims the
relativity is "not merely exhibited but MECHANISED — the whole
non-Markov signature at MENU-113 is carried by that quotient's
multi-TARGET labelled edges, and refining to the coarsest congruence
removes them and the signature together." Its **predicate** is

```python
_carrier_rel = (len(CKFAIL['MENU-113']) > 0
                and len(CKFAIL['CONG-185']) == 0
                and EDGES['MENU-113'][2] > 0
                and EDGES['CONG-185'][2] == 0)
```

— a four-way conjunction of existence and absence counts at two sampled
points. "Whole", "carried by" and "together" appear in no conjunct.
There is no ablation, no attribution of failing cells, no third point.

**The counterexample is inside the unit's own refinement trace.** The
refinement passes through four intermediate quotients before reaching
CONG-185. I measured each (own code, exact arithmetic):

| quotient | classes | multi-TARGET edges | depth-spanning classes | CK fails |
|---|---|---|---|---|
| MENU-113 (round 0) | 113 | **4** | 45 | **4 of 10** |
| refinement round 1 | 162 | **132** | 17 | **0 of 10** |
| refinement round 2 | 179 | 36 | 5 | 0 of 10 |
| refinement round 3 | 184 | 8 | 1 | 0 of 10 |
| refinement round 4 = CONG-185 | 185 | 0 | 0 | 0 of 10 |

**Round 1 carries thirty-three times MENU's multi-target edges and is
exactly CK-consistent at all ten triples.** The signature dies at the
first refinement step, while both of its alleged carriers — the edges
and the depth-recurrence — are still abundantly present. Removing the
edges is therefore *not* what removes the signature: the statistic is
not even monotone in the refinement order (4 → 132 → 36 → 8 → 0), it
rises 33-fold at exactly the step where the signature it allegedly
carries goes to zero.

I also ran the attribution the unit does not: at each of MENU's four
failing triples the differing cells touch **5** source classes, of which
4 are multi-target sources; at triples (1,3,4) and (2,3,4) **zero** of
the differing *target* classes are multi-target sources. Even the
localisation is not exact.

**What survives, and it is worth keeping:** a quotient with
single-valued labelled weight *and* target is a probabilistic
bisimulation, so its class process satisfies CK **by theorem**. That is
the sufficient direction, and it is genuinely established. The converse
— that multi-target edges *produce* non-Markovianity — is false here.

**Repair (BLOCKING).** In the verdict string replace

`MECHANISM=THE-SIGNATURE-IS-CARRIED-BY-THE-MULTI-TARGET-EDGES-AND-THE-45-OF-113-MENU-CLASSES-THAT-RECUR-ACROSS-CUTS`

with

`SUFFICIENT-CONDITION=SINGLE-VALUED-LABELLED-TARGET+WEIGHT=>PROBABILISTIC-BISIMULATION=>CK-EXACT-(THEOREM);NOT-NECESSARY-REFINEMENT-ROUND-1-CARRIES-132-MULTI-TARGET-EDGES-AT-CK-0-OF-10`

and in §7 delete "The whole signature is carried by the 4 multi-target
labelled edges" and "One structural fact accounts for both halves of
the carrier-relativity." Change the gate statement to match its own
predicate.

### F-2 (MAJOR, decisive for K4(b)) — the cap-scoping is backwards, and the unit computed the refuting datum and dropped it

§8.3 and §14 rest on: "A carrier built at a different cap, or at a fixed
point taken without one, need not be graded — **and this unit does not
build one**."

**It does build one.** `G-SUPPLY-D5` re-derives the coarsest weighted
congruence at d ≤ 5 (265 menu, 462 congruence, 6 rounds). The unit's
`refine()` returns the spanning-class count in its trace — that is how
the d ≤ 4 row `[17, 5, 1, 0, 0]` reaches both output and receipt. The
d ≤ 5 call keeps its trace in `_t5` and prints only `[t[1] for t in _t5]`.
The receipt's `supply_d5` block carries `{menu, congruence, rounds}` and
nothing else. **The decisive cap datum was computed in-run and
discarded.**

Recomputed here:

| | d ≤ 4 | d ≤ 5 |
|---|---|---|
| trace (round, classes, spanning) | (1,162,17)(2,179,5)(3,184,1)(4,185,**0**)(5,185,0) | (1,390,49)(2,439,17)(3,456,5)(4,461,1)(5,462,**0**)(6,462,0) |
| final classes spanning > 1 depth | 0 of 185 | **0 of 462** |
| root class depth profile | [0] | **[0]** |
| prefix-class returns | 0 | **0** |
| per-cut dims | [1,5,17,49,113] | [1,5,17,49,125,265] |
| purity reached at round | 4 of 5 | **5 of 6** |

Depth purity **reproduces at the next cap**, at the same "round N of
N+1" position. And it is not an empirical coincidence — it is forced:

> **Theorem (depth-grading is cap-universal).** Let the window be
> {h : |h| ≤ N} and suppose every history of depth < N has at least one
> successor (true here: 30728 transitions out of 3969 histories). After
> refinement round *k*, a history's class determines min(N − |h|, k).
> *Proof.* Round 1: the in-window successor multiset is empty iff
> |h| = N, so the class determines min(N−|h|, 1). Round k+1: the
> signature contains the round-*k* classes of the successors, each of
> which determines min(N−|h|−1, k); non-emptiness distinguishes |h| < N.
> So the class determines min(N−|h|, k+1). ∎ Hence at round N the class
> determines |h| exactly: **the fixed point is depth-pure at every
> finite cap**, and the fixed point is reached at round N+1.

Observed exactly: purity at round 4 for N = 4, at round 5 for N = 5,
fixed points at 5 and 6.

So "cap-driven" *understates the negative in a way that misdirects the
successor*. The grading is not contingent on this cap; **no finite cap
escapes it.** §14's first paragraph — "The successor's first question is
what the coarsest weighted congruence looks like … at d ≤ 5, where this
unit has already re-derived the 265/462 row" — points the successor at a
carrier this unit has already measured and which is graded.

**Repair (BLOCKING).**
- SEDIMENTARY **is** the licensed head, and `AT-THIS-CAP` is the **wrong**
  qualification. Replace, inside the anchor body,
  `THE-GRADING-IS-CAP-DRIVEN-PURITY-AT-REFINEMENT-ROUND-4-OF-5`
  with
  `THE-GRADING-IS-CAP-FORCED-AT-EVERY-FINITE-CAP-MEASURED-AT-d<=4-AND-d<=5-PURITY-AT-ROUND-N-OF-N+1`.
- §8.3: replace "A carrier built at a different cap … need not be
  graded — and this unit does not build one" with the theorem and the
  d ≤ 5 row.
- §14: the successor's first question is **the boundary convention**,
  not the cap — a fixed point whose terminal stratum does not have an
  empty successor signature. Nothing else in this construction can
  escape the grading.
- Emit `_t5`'s spanning column to output and receipt (`supply_d5.trace`).

### F-3 (MAJOR, K4(b)) — recurrence ⟷ non-Markovianity is a two-point coincidence, refuted by the unit's own trace

§8.3: "recurrence of the renewal root is a property of the *coarser*
carrier, **and exactly there** the chain is not Markov." The brief asks
whether this connection is measured or coincidental. **Coincidental, and
refuted.** Per-round, recomputed:

| quotient | root class occurs at depths | prefix-class returns | CK fails |
|---|---|---|---|
| MENU-113 | [0,1,2,3,4] | 1900 | 4 |
| round 1 (162) | **[0,1,2,3]** | **204** | **0** |
| round 2 (179) | [0,1,2] | 28 | 0 |
| round 3 (184) | [0,1] | 4 | 0 |
| CONG-185 | [0] | 0 | 0 |

At round 1 the renewal root's own class recurs at four depths, 204
histories return to a prefix class, and the chain is exactly
CK-consistent. Recurrence and non-Markovianity co-occur at exactly one
of five sampled carriers and are separated at three.

**It is therefore not a new ontological item**, and must not be named as
one. **Repair:** delete "and exactly there the chain is not Markov", or
restate as: "the two carriers the pin names happen to differ in both
respects; the unit's own refinement trace separates them at rounds 1–3,
so no link is claimed."

*Consequence the successor must carry:* path (a) was decided on two
sampled carriers, and the unit's own lattice contains three quotients
where the renewal root **does** return and the chain is still CK-exact
by the unit's own property-6 criterion. Path (a)'s failure is licensed
**at CONG-185, as the pin scoped it** — and nowhere wider.

### F-4 (MAJOR, K4(c)) — the "correction" to Γ-main compares two different objects, and the verdict string carries the resulting tension unresolved

Γ-main §5.4 concludes: "at every depth-cut triple with a non-degenerate
first cut, **no interpolant of eq. 22's form** exists" — eq. 22's form
being the *square, padded* object on one fixed configuration space.
Paper-16's `b3_problem` asks a different question, in its own docstring:
"does a COLUMN-STOCHASTIC non-negative Gbar exist with
Gamma(dd←d) = Gbar · Gamma(md←d)?" — **rectangular, unpadded, no
enlarged configuration space.**

At MENU-113 triple **(1,2,4)** both are simultaneously true (triple order
verified: `TRIPLES = [(1,2,3),(1,2,4),(1,3,4),(2,3,4)]`; eq-22 negatives
`[36,104,108,164]`; coupled feasibility `[False,True,False,False]`):

- the padded candidate is unique and carries **104 negative entries**, so
  no interpolant of eq. 22's form exists there; **and**
- the rectangular column-stochastic problem is **FEASIBLE** (413
  variables, 258 equations, certified).

**Γ-main is therefore not wrong.** Its statement is true of its own
object and simply does not transfer. Paper-16's "This is a correction to
the predecessor's reading" and "The refutation survives, with its scope
narrowed by one cell" conflate the two. The refutation survives
*entirely*; what is narrowed is a different claim that Γ-main never made.

**Worse, the verdict string contradicts itself across segments.** The
QUANTUM segment enters
`EQ22-NEGATIVES-36/104/108/164-AT-2-OF-4-COMPLETIONS-THAT-SPEAK`
as MENU's quantum signature, while the B3 segment of the same string
reports `@MENU-113-INFEASIBLE-3-OF-4` — i.e. that at the triple
contributing the 104, a stochastic interpolant **exists**. Neither
segment references the other; the paper never sets them side by side.

**Does terminal Γ-main need an erratum row? No.** It needs a
**scope-annotation row**: "the 4-of-4 is a statement about eq. 22's
padded form; the rectangular column-stochastic question is answered in
paper-16 and separates 3-of-4, diverging at (1,2,4)."

**What the one interpolant cell MEANS for the padding convention — and
this is the largest methodological item in the unit, currently
under-billed.** The padding does not merely "answer a question about an
enlarged configuration space". It converts an **underdetermined
feasibility** question (413 variables, 258 equations — a non-empty
polytope) into a **determined algebraic** one (the padded first transfer
is invertible, so the candidate is unique), and the unique determined
answer can be negative while the feasible set is non-empty.
**Therefore eq-22 negativity is not equivalent to non-existence of a
stochastic interpolant** — demonstrated here at 1 of 4 cells. Every
eq-22-based refutation in the corpus is weakened by exactly this
amount, and that belongs in §14 as a named successor, not in a
subordinate clause of §8.1.

### F-5 (MINOR, K4(a)) — a verdict conjunct that is TRUE but ungated

"the 4 bad edges sit on … the 45 of 113 menu classes that recur across
cuts". I verified the containment: **true, 4 of 4**, each with depth
profile [1,2,3,4]. But the code never computes it — the gate detail
concatenates `len(_mt_src)` with the words "that recur across depth
cuts" and, separately, `DEPTHPURE['MENU-113'][0]`. The containment
predicate exists nowhere; `_mt_depths` (line 1985) is computed and never
used — an abandoned check. The receipt has no field for it.
**Repair:** add `_mt_src <= rec_menu` as a gated conjunct with its own
falsifier, and a `quantum.multitarget_sources_recurring` receipt field.
No number moves.

### F-6 (MINOR, K4(a)) — the negative control sits on the ruled carrier's side of every quantum row

Recomputed: REC (2477 classes, declared FLAT) has **0** multi-target
edges, **0** classes recurring across cuts, root class at depth [0], and
CK failing at **0 of 10** — identical to CONG-185 on every quantum-shape
statistic. eq-22 is not run at REC at all. So §7's table is two-column
where §4's and §6's are three, and the carrier the unit declares
degenerate scores exactly as the ruled one does.

This matters for the head: the quantum statistics **do not separate the
ruled carrier from the negative control**, so they cannot on their own
support a claim about Γ's character *at* CONG-185. **Repair:** add the
REC column to §7, run eq-22 there, and state the non-separation.

### F-7 (MINOR — new structure, unreported) — MENU's property-1 and property-2 failures are the SAME four classes

The four MENU classes on which the horizon potential is multi-valued at
r = 2 are **set-identical** to the four classes carrying a multi-target
labelled edge (verified: `bad == mt_src`, overlap 4 of 4). The unit
prints "4 of 13" in property 1 and "4" in property 2 and never observes
that they are the same 4. This is a real structural fact and the closest
thing in the unit to an actual mechanism — it belongs in §4. It does not
rescue F-1, because round 1 still has CK 0 at 132 multi-target edges.

### F-8 (MINOR) — no choice inventory, at the RSQ standard

Γ-main carried one in its head
(`MOTIVATION-FORCED-4|STABILIZER-FIXED-1|GENUINELY-FREE-5|I-READOUT…|I-CARRIER…|I-PADDING…|PER-SEGMENT-MOTIVATED-1-OF-7`).
Paper-16 has **none** — not in the paper, not in the head, not in the
receipt. Yet it makes more consequential choices, not fewer. The two
un-inventoried choices that drive the two headlines are:

| choice | fiber | what it decides |
|---|---|---|
| **THE CAP** (d ≤ 4 carrier, d ≤ 5 anchor) | ≥ 2 measured in unit | every §8.3 negative; the eq-22 silence; ANCHOR=SEDIMENTARY |
| **THE [B3] PROBLEM FORM** (rectangular vs eq-22-padded) | 2 | the entire "correction to Γ-main" (F-4) |

Also un-inventoried: operationalising "exact lumpability" as CK-at-10-triples
(F-10); the four padding completions (Γ-main inventoried this as I-PADDING);
the H4 horizon; the leg prune. **Repair:** restore the inventory segment,
with THE CAP declared FORCED-BY-COST and its consequence-set named, and
THE [B3] FORM declared GENUINELY-FREE with fiber 2 and both members
measured — which the unit has already done and merely failed to price.

### F-9 (MINOR — the deviations register) — the flow identity's 352/596 is honestly priced in prose and mis-priced in the head

§5 says "at every other admissible horizon the identity fails at 352 of
596 tests, so written with r free it is false" — accurate, and the ratio
is given. But the per-horizon structure is withheld and is strictly more
discriminating (recomputed):

| r | off-horizon tests | pass | fail |
|---|---|---|---|
| 1 | 520 | **244** | 276 |
| 2 | 68 | 0 | **68 (100%)** |
| 3 | 8 | 0 | **8 (100%)** |
| 4 | 0 | — | — |
| total | 596 | 244 | 352 |

**244 off-horizon tests pass**, all at r = 1. The head's
`352-OF-596-FAIL-AT-EVERY-OTHER-ADMISSIBLE-HORIZON` reads naturally as
"fails at every other admissible horizon", which is false at 244 tests.
**Repair:** `352-OF-596-OFF-HORIZON-TESTS-FAIL-(r=2-AND-r=3-AT-100%,r=1-AT-276-OF-520)`.
Honestly priced, the gate gets *stronger*, not weaker.

### F-10 (MINOR) — "exact lumpability" is CK-at-10-triples, and it does not select the carrier

`G-CONG-LUMPABLE` and `SIX[5]` both evaluate `len(CKFAIL['CONG-185']) == 0`.
Classical strong lumpability is a stronger condition, and on a
depth-graded carrier CK is structurally cheap (the cuts share no labels).
Recomputed: **rounds 1, 2, 3 and REC all pass property 6.** So the sixth
ruling property, alone, does not distinguish CONG-185 from four other
objects in the same lattice. **Repair:** rename the row "CK-exact at the
10 depth-cut triples", or measure the classical criterion and report both.

---

## 2. The licensed claim — (a) QUANTUM

**What the measurements license, exactly:**

> The four measured quantum-shape statistics — Chapman–Kolmogorov, the
> CK-exactness of the class chain, whether eq. 22's algebraic reading
> speaks, and its negativity when it does — take different values at
> MENU-113 and at CONG-185, each measured at both and stamped. Being a
> weighted congruence (single-valued labelled weight **and** target) is
> **sufficient**, by the probabilistic-bisimulation theorem, for the
> class process to satisfy CK at every triple. MENU-113 is not one and
> fails at 4 of 10. Depth-recurrence at MENU-113 makes the cuts of a
> triple share 13, 13, 45 and 45 labels, which is what leaves the padded
> first transfer non-singular and lets the algebraic reading speak;
> at CONG-185 the cuts share 0, 0, 0 and 0, the transfer is singular
> under all four completions, and the route is silent.

That second sentence — the eq-22 half of the mechanism — **is measured
and is sound**. The non-Markov half is not (F-1). *The mechanism has two
halves of different standing and the unit welds them into one sentence;
split them.*

**Not licensed:** "the whole signature is carried by the multi-target
edges"; "the 45 recurring classes carry it"; "one structural fact
accounts for both halves"; and any ontological reading of
"carrier-relative".

**Which candidate reading does the evidence support?** The brief offers
three. Two are refuted by the unit's own data *because their polarity is
inverted* — the refinement order here is REC ⊑ CONG-185 ⊑ MENU-113, so:

- "*the coarser carrier is Markov*" — **FALSE.** MENU-113 is the
  **coarsest** of the three and the **only** non-Markov one; REC is the
  **finest** and is Markov.
- "*the fine carrier's non-Markovianity is a quotient artifact*" —
  **vacuous.** The fine carriers (CONG-185, REC) have no
  non-Markovianity.
- "*quantumness is carrier-relative*" — true only as bookkeeping: four
  statistics differ across two named quotients.

**The reading the evidence actually licenses is the third one with its
polarity corrected: the COARSER carrier's non-Markovianity is a
quotient artifact.** The transport chain on histories is Markov **by
construction** — k_r(e|h) is a function of h alone, and the flow
identity holds at 3968 of 3968 transitions. So every non-Markov statistic
in this unit is manufactured by a lumping, and it is destroyed by *one*
round of successor-closure refinement.

**The ontological sentence the paper must say:**

> Non-Markovianity here is a property of the **description**, not of the
> process. The transport chain on histories is Markov by construction;
> MENU-113's indivisibility signature is an artifact of a quotient that
> is not a congruence, and one refinement round destroys it while
> leaving 132 multi-target edges and 17 depth-spanning classes standing.
> This unit does not measure a quantum character of Γ. It measures which
> quotients preserve the process's own conditional and which do not —
> and on every such statistic the ruled carrier is indistinguishable
> from the record quotient it declares flat.

**Head repair:** `QUANTUM=CARRIER-RELATIVE-CONFIRMED-BY-MEASUREMENT`
overstates on two counts — "CONFIRMED-BY-MEASUREMENT" is attached to a
mechanism that is not measured, and "CARRIER-RELATIVE" invites the
ontological reading §12 disclaims. Use
`QUANTUM=SIGNATURE-IS-QUOTIENT-RELATIVE-4-STATISTICS-STAMPED-AT-BOTH-CARRIERS`
plus the F-1 sufficient-condition segment, and add
`@REC:MARKOV-CK-0-OF-10;MULTI-TARGET-EDGES-0;RECURRING-CLASSES-0-THE-QUANTUM-STATISTICS-DO-NOT-SEPARATE-THE-RULED-CARRIER-FROM-THE-FLAT-CONTROL`.

## 3. The licensed claim — (b) ANCHOR

**SEDIMENTARY is licensed in the head** — and the cap audit the brief
ordered comes out the opposite way from the one the paper anticipates.
`AT-THIS-CAP` is **not** the repair; it would weaken a negative that is
in fact structural.

> **The licensed sentence.** At every finite cap, the successor-closure
> fixed point of the menu partition is depth-graded — measured at d ≤ 4
> (0 of 185 classes span a cut) and at d ≤ 5 (0 of 462), and forced by
> induction on height-to-cap, which places purity at round N and the
> fixed point at round N+1 (observed: 4-of-5 and 5-of-6). Consequently no
> class is ever revisited, prefix-class returns are 0 at both caps, the
> root's class occurs at depth 0 alone at both, and the renewal-root
> candidate **cannot be posed at the class grain of any capped carrier of
> this construction**. Path (a) fails at CONG-185, as the pin scoped it,
> for a reason that is structural rather than accidental; the long-run
> structure is therefore argued from accumulation, not from return, and
> no recurrence is assumed anywhere. What is open is **not a different
> cap** — the unit has already built and measured one — but a different
> **boundary convention**: a fixed point whose terminal stratum does not
> carry an empty successor signature.

**Is the "recurrence ⟷ non-Markovianity" connection a new ontological
item?** **No** (F-3). It is a coincidence at one of five carriers,
separated at three others inside this unit's own refinement trace. It
must not be named, and the words "and exactly there" must come out.

Every negative in §8.3 is honestly scoped **to this cap**; the defect is
that the scoping is *too weak* and misdirects §14. The four supporting
measurements all reproduce exactly at my hands: 0 of 185 recurring;
prefix-class returns 0 @CONG vs 1900 @MENU; root depth profile [0] vs
[0,1,2,3,4]; (1,1) block entered at 0 of 30728 transitions with (2,2),
(2,3), (3,2) at 1700, 4, 4. The delivery-free scoping of paper-09's
first-return law is carried verbatim and gated at `V-RENEWAL-SCOPE` with
a working drift falsifier — correct.

## 4. The licensed claim — (c) the corrections and the opens

**The [B3] isolation is LICENSED as stated, and this is where the unit's
"entirely" is earned.** 772 row problems over 8 (carrier, triple) cells,
0 infeasible, 772 of 772 certified, 0 orphan columns, 0 empty rows, both
verdict directions certificated. The obstruction really is the
column-sum coupling and nothing else. *Note the contrast the panel should
record: this unit makes two totality claims — "the coupling carries all
of it" and "the multi-target edges carry the whole signature" — and they
have opposite standing. The first is gated at 772 rows; the second has
no predicate at all.*

**The correction to Γ-main: no erratum row; a scope-annotation row**
(F-4). Γ-main's 4-of-4 is true of eq. 22's padded form. Paper-16 answers
the rectangular column-stochastic question, which separates 3-of-4. The
divergence cell is MENU (1,2,4), where the padded candidate carries 104
negatives and a rectangular column-stochastic interpolant exists.

> **The licensed sentence on the one interpolant cell.** The padding
> convention converts an underdetermined feasibility question into a
> determined algebraic one, and the determined answer can be negative
> while the feasible set is non-empty. At MENU-113 (1,2,4) it is:
> eq. 22's unique padded candidate carries 104 negative entries while
> the unpadded column-stochastic problem is feasible and certified.
> **eq-22 negativity is therefore not equivalent to the non-existence of
> a stochastic interpolant**, and any refutation resting on it is
> scoped to the padded object.

**The atom's death — LICENSED, and correctly self-deflating.**

> At a weighted congruence every class is trivially an exact atom — 72 of
> 72 testable classes have δ\* = 1 at N = 1, which the congruence forces —
> so δ\* has no discriminating power on this carrier; and the one
> non-trivial block's δ\* falls from 1 to 0 under the coarsening lemma.
> The atom language is **instrument-dead at this carrier**, not refuted:
> it is empty on the block and vacuous on the classes, and the successor
> should stop carrying it.

The scope word "at this carrier" is present in §8.2 and §14 and is
correct. The accompanying unreachability stamp is properly carried and
the pin's bar on recurrence readings is honoured — I found no recurrence
reading anywhere in the unit.

**The (1,1)-block split — verified exactly, and it answers Γ-prep's
open.** 341 points at depths 0–4; **1** MENU-113 class (block-pure);
**5** CONG-185 classes of sizes 256, 64, 16, 4, 1 (block-pure), one per
depth stratum; stratum sizes {0:1, 1:4, 2:16, 3:64, 4:256}. One
qualification the paper should add: the block splits **by depth because
every class does** (F-2's theorem). The "five classes, one per stratum"
answer is forced by depth purity and is not an independent fact about
the block.

## 5. Prose ↔ receipt sweep

Clean within my reach. Every headline numeral in §§4–9, §13 and the
verdict resolves to a receipt field, and each of the following
reproduced exactly at my own hands: the per-level and cumulative census;
3969 / 113 / 2477 / 185 / 5 rounds; the round trace with its spanning
column; dims [1,5,17,49,113], [1,5,13,45,113], [1,8,51,324,2093];
the descent census at all three carriers (after correcting my own
horizon convention); edges 572/0/0, 368/0/4, 2900/0/0; potentials
2, 4, 257/32, 1035/64, 4173/128; M census {2: 3757, 5/2: 212};
k₁ 0 of 30728 and k₂ 1340 of 3968; flow 3968/3968 and 352/596;
CK 4 of 10 at cells 34/112/12/12 and 0 at both other carriers;
shared labels [13,13,45,45] vs [0,0,0,0]; depth-recurrence 45/0/0;
prefix returns 1900/0; R-SIG 5161, R-MENU 1365, blocks
{(1,1):1365, (2,2):3788, (2,3):4, (3,2):4}; entries 0/1700/4/4 of 30728;
the block 341/1/5 with sizes [256,64,16,4,1]; column counts 102/90/454
(also checked against the cut-pair arithmetic 4+15+34+49). eq-22 minima
−1/97, −5/97, −1/18, −1/128 are present in the receipt.

Two prose items with **no receipt backing**: the containment of the 4
multi-target sources in the 45 recurring classes (F-5, true but ungated),
and the d ≤ 5 spanning trace (F-2, computed and dropped).

## 6. The successor register

**What the weld line inherits.** CONG-185 re-derived in unit and gated
6-of-6, with its provenance chain intact; the d ≤ 5 congruence at 462
with — once F-2 is applied — its spanning trace; and the warning that on
every quantum-shape statistic CONG-185 is indistinguishable from the
record quotient (F-6), so the weld cannot use those statistics to argue
that the ruled carrier is the physically distinguished one.

**What the v14 charter's R6 continuum inherits — and this is a wall.**
F-2's theorem says every capped successor-closure fixed point is
depth-graded. Any refinement family built from this construction —
R6a's derived family, R6b's scaling census — therefore consists entirely
of depth-graded carriers, in which no class is ever revisited and no
regeneration structure exists at any member. **A continuum programme
that needs a renewal or regeneration anchor cannot get one from this
family, at any cap, by theorem rather than by cost.** That belongs in
the charter, not only in paper-16's §14.

**What a Γ-successor inherits, named.**
1. **THE BOUNDARY CONVENTION** (replaces §14's "different cap", which
   F-2 refutes) — the only route by which path (a) becomes a question
   about the process rather than about the window.
2. **THE eq-22 / FEASIBILITY SEPARATION** (F-4) — re-run the corpus's
   eq-22-based refutations against the rectangular column-stochastic
   feasibility question. This unit has shown the two can diverge, and
   nothing tells us how often.
3. **THE [B3] CELL THAT SPEAKS** — kept from §14, now with its cause
   identified: (1,2,4) has 413 variables against 258 equations where
   (1,2,3) has 121 against 94. The distinguishing quantity is plausibly
   the slack of the column-sum coupling, and it is one measurement away.
4. **WHAT ACTUALLY CARRIES THE SIGNATURE** (new, from F-1) — the
   non-Markov signature dies at refinement round 1. What one round of
   successor-closure removes is unmeasured, and it is the real mechanism
   question.
5. Kept unchanged: the two rows to pin (the d ≤ 6 arena; the weld-2
   re-derivation once its bytes stop moving), and the atom language's
   retirement.

**Does GITER-LAW-CONFIRMED close the Γ campaign?** **No.** The law is
built and its targets are hit at the law's own values, at both legs, at
a readout re-proved on this carrier — that half is clean and is the
unit's real achievement. But the campaign's *interpretive* questions are
not closed: the quantum mechanism is refuted rather than established
(F-1), the anchor's negative is structural rather than cap-local and
therefore points at a different successor than the one named (F-2), and
the eq-22 instrument itself has been shown to be weaker than the corpus
has treated it (F-4). The Γ line closes on construction and **opens on
interpretation**, with items 1, 2 and 4 above as the named next unit.

---

## 7. Recomputation ledger

113 independent recomputations, 0 divergences. Scratch at
`.../scratchpad/git-ef/` (recomp1–recomp7). Repo writes: this file only.
Repo state unchanged; concurrent workers (`u4_*`, `u4b_*`, `r5_*`)
untouched and disclaimed.

| block | recomputations | result |
|---|---|---|
| sha256-12 of all six objects | 6 | all match |
| family census, carrier size, three quotients | 6 | match |
| refinement: rounds, class trace, spanning trace, dims ×3 | 12 | match |
| **d ≤ 5 cap audit (new)** | 7 | **grading reproduces; F-2** |
| descent census ×3 carriers ×5 horizons | 15 | match (after my own scoping fix) |
| edge census ×3 | 9 | match |
| depth-recurrence, root profiles, prefix returns ×3 | 9 | match |
| **intermediate quotients: edges/CK/spanning/root/returns (new)** | 20 | **F-1, F-3** |
| **CK failing-cell attribution (new)** | 8 | **F-1** |
| potentials, M census, k₁, k₂ | 8 | match |
| flow identity, matched + per-horizon (new breakdown) | 6 | match; F-9 |
| CK census ×3 carriers with cells | 7 | match |
| shared labels ×2 | 2 | match |
| R-SIG, R-MENU, blocks, entries, block split | 13 | match |
| column counts + cut-pair arithmetic | 4 | match |
| **descent-failures ≡ multi-target sources (new)** | 1 | **F-7** |

**Fixes required before terminal (BLOCKING):** F-1, F-2, F-4 — each
changes the verdict string. **Required, non-blocking:** F-3, F-5, F-6,
F-8, F-9, F-10, and the two receipt fields.
**No delivered number moves under any fix in this review.**
