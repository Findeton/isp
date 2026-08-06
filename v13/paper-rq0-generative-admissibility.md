# Generative Patch Admissibility

## The Atlas Axiom, Its Rigidity Dichotomy, and the Price of Forging a Boundary

**Status:** `TERMINAL (delivered v13 #137; panel #140-#142; adjudicated #143; repair verified terminal #145)`

**Date:** 2026-08-06

**Frozen analytical pin:** `9576aee`

**Immutable base:** `efa7224` (Cycles B and B′ terminal; #103/#111 artifacts)

---

## Abstract

The predecessor cycle ended at a named obstruction. Nothing in it tied a
declared task family to the boundary that family presents, so an adversary who
declares both contexts of an arena controls both: two aligned manufactured
contexts pass the rebuilt independence gate while the forged greatest record of
one is certified fourteen times out of fifteen against the other. This paper
tests one candidate answer — that a patch is bound by its own generating
dynamics — and reports what the candidate earns and what it costs.

A **patch** is a quadruple: a boundary presented at a committed carrier, a
declared task family, a declared preparation, and an admitted law. The
preparation is a component because the axiom reads it, and two patches agreeing
on the other three receive opposite verdicts (Section 5). The candidate **Atlas
Axiom** calls a patch admissible when two conditions hold. Condition (i) is
two-sided minimality: the boundary is the minimal sufficient boundary of its own
declared family, and the family is that boundary's closure under the terminal
availability machinery. The two sides are adjoints of *different* connections —
the boundary side is the `ker` pairing and not the Cycle B core, which is the
conflation Cycle B's own Theorem 3.8 records as the one to avoid — and Section 3
measures what the substitution buys. Condition (ii) is generativity: the
declared family is non-empty and every declared task writes exactly what the
boundary asserts, and the reachable subprocess occupies every atom the boundary
declares. The first clause of condition (ii) is proved entailed by condition (i)
(Theorem 3.2), so condition (ii)'s independent content is occupancy.

The axiom is decidable, it is covariant, and it does what it was built to do.
The forged member of the colluding pair is **inadmissible at every admitted law
containing the identity**, and the killing condition is measured rather than
assumed: for the only declaration that could ever satisfy (i-b) — the boundary's
own closure — (i-a) fails and (ii-a) fails with it, on one exhibited witness, a
declared task that separates the two configurations the boundary asserts are a
single atom. Under any other declared family the patch fails (i-b) instead; the
verdict is declaration-independent, the identity of the killing condition is
not, and Section 6.1.1 reads the table against the adversary's actual
declarations. The boundary claims an identification its own realized legs never
write. The second member is admissible, and correctly so: as a boundary it *is*
the legitimate address algebra, and the collusion lives entirely in the first
member's patch. More than that, the pair is **jointly unforgeable at a shared
law**: no single admitted law makes both members admissible, because the
preserving family of the finer boundary is contained in the preserving family of
the coarser one, so the alterations that blind one blind the other — and the
general form of that argument says no law admits two strictly *comparable*
boundaries at all. The hypothesis is load-bearing and is stated with the result:
if each context may declare its own law, member one is admissible under the
identity-free law $\{(0,0,2,3,4)\}$ while member two is admissible under the
committed deterministic law, and the axiom rejects neither. Joint
unforgeability is a statement about one law, not about one adversary, and the
mixed-law arena is this paper's named open question. The legitimate eraser
context passes both conditions; the relabelled context passes, as covariance
requires; the counter-law leaves both verdicts stable while collapsing the
certificate to a single task; and the arena's two contexts, disclosed as
dependent in the predecessor, are returned here as literally one patch, because
the axiom makes the declared family a function of the boundary.

The price is a dichotomy. The carrier's own configuration algebra is admissible
**if and only if** the law contains the identity — equivalently, if and only if
it contains any reversible operation, since a composition-closed law on a finite
carrier contains a permutation only if it contains that permutation's identity
power. So every law has either exactly one chart, the carrier's, or no carrier
chart at all and possibly several proper ones. There is nothing in between: over
the $687$ composition-closed laws on three configurations the biconditional
holds $687$ times, $428$ laws admit a proper chart, and not one law admits both
kinds. This is not a tautology about coarse-graining and the trigger is not
idling: it is reversibility. The axiom certifies a boundary relative to a
declared carrier and does not derive one, and the de-smuggling question moves up
exactly one level, from the boundary to the carrier.

Two further results are first-class. The **Feynman gate is positive via
condition (i)**: admissibility changes a number. At one fixed boundary, with one
law, one state and one preparation, an admissible patch and an inadmissible
patch differ in an admitted two-time tester statistic, exactly $1$ against
exactly $3/4$. Its honest halves are reported with it: that statistic does not
separate the forged patch, which is separated instead by a refinement statistic,
exactly $0$ against exactly $1/16$; the same-boundary comparison cannot be run
at the forged boundary at all, because rigidity leaves no admissible comparator
there; and **neither statistic reads the declared preparation**, so neither can
ever see a failure of the occupancy clause — the axiom's only independent
content. An occupancy-sensitive statistic is left open.

And the **forging cost** is defined exactly and computed. Every member of an
obstruction set must be deleted and no addition removes one, so the cost is at
least the obstruction's cardinality, additions included; and it equals that
cardinality **exactly when** the boundary is still admissible in what remains,
which is a separate condition and is measured, not inherited. Under the
committed deterministic law of $3125$ operations at five configurations the
condition holds and the tower is exact: forging one identification costs $120$;
the aligned $2{+}2$ boundary costs $360$; the tomographic boundary costs $1260$;
and the limiting forgery costs $3120$, leaving five operations — not an altered
law but a complete alternative one. Where the condition fails the equality is
false, and it fails often: in $1008$ of $2748$ law-boundary pairs at three
configurations, and at the committed reversible law, where the complement is
empty and the cheapest forgery costs $n!+1$ and *requires* an addition. The
identity lies in the obstruction of every non-discrete boundary at every
identity-containing law, so inside that class there is no forgery at any price.
At the context-pair level the tower does not merely grow; at a shared law it
terminates.

The registered outcome is

$$
\boxed{
\begin{array}{l}
\texttt{RQ0-L2-GENERATIVE-ATLAS-AXIOM}\\
\texttt{RQ0-L2-BLOCKED-AT-CARRIER}
\end{array}}
$$

with `RQ0-L2-EMPIRICALLY-IDLE` and `RQ0-L2-CHEAP-LAW-FORGERY` both **not**
occurring at the declared scope.

---

## Scope box

| Item | Value |
|---|---|
| Dimension | finite throughout |
| Carrier | ONE committed carrier of five configurations — four success addresses and the retained sink — declared before every context |
| Boundaries | presented at that carrier by the predecessor's committed incidence; carrier typing is measured, never assumed |
| Laws | one law family per context, declared: the committed DET, REV and ALL families, the committed counter-law, and FUNNEL's composition closure; each contains the identity, and identity-free laws are run as positive controls and as counterexamples. FUNNEL itself is a declared **task family**, not a law in the sense of Definition 2.1: it is composition-closed at two configurations only (measured, Proposition 3.7), and the law it generates is swept in its place |
| Records | complete admitted nondisturbing repeatable classical instruments only; a record is a partition of the carrier's configurations |
| "Reachability" | an ORDER ON CONFIGURATIONS: the declared preparation closed under the realized legs of the declared family. It has **no** spatial, causal, temporal or spacetime reading of any kind; it is not a region, a cone, a neighbourhood or a history |
| Inherited scope | the declared #103 compact-convex Karoubi scope and the declared #111 ancilla-saturated, instrument-complete scope, unchanged |
| Arithmetic | exact throughout; no float in any substantive path, verified by an abstract-syntax-tree sweep of this unit and of both terminal modules it imports |
| Verification | exhaustive over all records at two, three, four and five configurations against every declared law; the cost measured exhaustively over every non-discrete boundary at three and four configurations under DET and at three under the full left-total family ALL, and over four declared levels at five under DET |
| Census | a second population, used wherever the committed sweep is too thin to test a claim: every composition-closed law on three configurations generated by at most three admitted maps — $687$ laws — and a declared sample of $865$ laws at four configurations |
| Lean | none |
| Not decided here | where the carrier comes from, autonomous charts, internal laws, patches declaring different laws, and every later object |

Every numbered result carries a scope tag. `[FIN]` means the finite declared
scope above. `[EXH-5]` means additionally verified exhaustively over all
records at two to five configurations against every declared law. `[EXH-4]`
means additionally verified exhaustively at three and four configurations.
`[CEN]` means additionally verified over the census population. `[ARENA]`
means verified on the predecessor's committed nine-context arena. `[FIX]`
means verified on the committed fixture set only.

The words *patch*, *carrier*, *atlas*, *reachable* and *occupied* in this paper
are operational vocabulary about admitted operations and declared
configurations. No region, locality, topology, manifold, causal order,
influence, spacetime, field, QCD or gravity object is constructed, used or
claimed. "Atlas" names the programme's target, not an object built here.

---

## 1. The question and the result

### 1.1 What is inherited

Four objects are inherited and are not re-derived.

First, the **minimal sufficient process boundary** of a declared task family:
the minimum-rank retract through which every declared task factors, unique up
to reversible operational equivalence.

Second, at ancilla-saturated instrument-complete scope, the **operational
classical core**, whose branches are the atoms of the Boolean algebra of
admitted split projections; admission is measured per law and never inferred
from algebraic existence.

Third, the predecessor cycle's **availability machinery**. For an admitted
future $F$ with sector support $\operatorname{sup}(k)$, write
$\operatorname{comp}(F)$ for the partition of the configurations into connected
components of the collision graph $k\sim l$ iff
$\operatorname{sup}(k)\cap\operatorname{sup}(l)\neq\emptyset$. Then
$\operatorname{comp}(F)$ is the finest record $F$ preserves,
$F\in\operatorname{Pres}(\pi)$ iff $\operatorname{comp}(F)$ refines $\pi$, and
$\operatorname{Core}(\mathcal G)$ is the partition generated by the union of
the $\operatorname{comp}(F)$, $F\in\mathcal G$. $\operatorname{Pres}$ and
$\operatorname{Core}$ form an antitone Galois connection; every closure fixes
the top of its own record lattice; and under any law admitting an irreversible
merge the closure is the identity, so the fixed-point condition selects
nothing. Cycle B's Theorem 3.8 is inherited with them, and it is a warning:
*the minimal-boundary core is not antitone… the Galois machinery belongs to the
availability relation, not to the minimal-boundary construction… the two are
easily conflated.* Section 3.5 is where that warning is collected.

Fourth, the predecessor cycle's **standing obstruction**. Two aligned
manufactured contexts — each a measure chosen to match a preselected one, with
the rotation deleted so that both are address-aligned — pass the rebuilt
binding independence gate as *independent*, and the forged greatest record of
the first descends against the second, fourteen of its fifteen records
certified. Nothing there ties a declared family to the boundary it presents.

### 1.2 The question

Can a patch be bound by its own generating dynamics? Concretely: is there a
condition on the quadruple (boundary, declared family, declared preparation,
admitted law), built only from committed structure, that rejects the colluding
pair while certifying the legitimate context?

### 1.3 The result, in one paragraph

The candidate axiom is stated with both conditions decidable (Section 2), and
condition (i) is then shown to be **rigid**: at any law containing the identity
it admits exactly the carrier's own configuration algebra, because the Cycle B
closure of a boundary always contains the identity while #103-minimality
excludes it from every proper coarse-graining (Theorem 3.1). The converse holds
too, so rigidity is a dichotomy whose trigger is reversibility (Theorem 3.5),
and the selectivity is produced by pairing `ker` with $\operatorname{Pres}$
rather than by any competition between two Cycle B minimalities
(Proposition 3.6). Condition (ii)'s first clause is proved *entailed* by
condition (i), so generativity's independent content is its occupancy clause
alone (Theorem 3.2); the identity-free positive control shows the dichotomy's
other side is populated (Proposition 3.4). The four mandatory discriminators
are then run (Section 6): the colluding pair's forged member fails, on an
exhibited witness, with the kill-list's dependence on the declared family
measured (§6.1.1); the pair is jointly unforgeable at any shared law, and the
mixed-law escape is exhibited (Proposition 6.2); the legitimate eraser context
passes; the relabelled and counter-law contexts get their honest verdicts with
the law-relativity disclosed; and the arena's dependent pair is returned as one
patch. The Feynman gate is positive with its three honest halves stated
(Section 7). The forging cost is bounded below everywhere, computed exactly
along a tower where the attainment condition is measured to hold, refuted as a
general equality where it does not, and shown to terminate at the pair level
(Section 8).

### 1.4 Four-gate audit of the two new objects

**Object 1 — the patch, and its admissibility predicate.**

| Gate | Disposition |
|---|---|
| Referent | a declared boundary presented at the committed carrier by the predecessor's incidence, a declared set of admitted futures, a declared preparation, and a declared composition-closed law. All four are laboratory data of exactly the kind the two predecessor cycles already use; nothing is added |
| Necessity | the predecessor's standing obstruction is precisely that no condition ties a declared family to the boundary it presents, and both halves of the fork the adjudication left open require such a condition |
| No-smuggling | the predicate mentions no candidate record, no measure, no provenance and no arena. It quantifies over structure fixed before any context is declared: the carrier, the law, and the two committed minimality notions. Provenance is *not* used, and could not be — it is not laboratory data |
| Discriminator | Section 6 exhibits contexts the predicate rejects and contexts it certifies, over the same construction; Section 3 exhibits laws under which a proper coarse-graining is admissible and laws under which none is; Section 5 exhibits patches failing each condition alone |

**Object 2 — the forging cost.**

| Gate | Disposition |
|---|---|
| Referent | a count of single-operation alterations of a declared law: admitted operations added or deleted. The unit of cost is an admitted operation, which is committed laboratory data |
| Necessity | "the adversary can forge this" is empty until the forgery has a price; the pre-registered conjecture cannot be tested otherwise |
| No-smuggling | the definition mentions no boundary's provenance and no notion of legitimacy; it is a minimum over all alterations, and it is computed by exhibiting the altered law and re-running the same predicate on it |
| Discriminator | the cost is finite and different at each level of the tower, it is zero for admissible patches by construction, it is strictly larger than its own lower bound at exhibited laws, and at the pair level it is proved unpayable — so it is not a constant dressed as a measurement |

---

## 2. The patch, and the axiom

### Definition 2.1 — the carrier, the law, the patch `[FIN]`

The **carrier** $X$ is the committed finite set of laboratory configurations —
here the five of the predecessor's arena: four success addresses and the
retained sink. An **admitted law** $L$ is a composition-closed set of admitted
futures on $X$, each presented by its sector support
$\operatorname{sup}_F:X\to 2^X$, left-total. A **patch** is a quadruple

$$
P=(B,\ \mathfrak F,\ X_0,\ L)
$$

with $B$ a declared boundary presented at the carrier by its committed
incidence $\iota_B$, $\mathfrak F\subseteq L$ a declared task family, and
$X_0\subseteq X$ a declared preparation. The preparation is a component of the
patch and not a parameter of the ambient setting: clause (ii-b) is a function of
it, and W1 and W3 of Section 5 agree on the other three components, differ in
$X_0$ alone, and receive opposite verdicts. Admissibility is therefore not a
function of the triple.

$B$ is **carrier-typed** when the images $\{\iota_B(k)\}$ form a partition
$A(B)$ of $X$. This is measured, never assumed: a boundary built by rotating
the coordinate basis has overlapping images and is not carrier-typed
(Section 6.6).

### Definition 2.2 — the axiom `[FIN]`

$P$ is **admissible** iff all four clauses hold.

- **(i-a) #103-minimality.** $A(B)=\ker(\mathfrak F)$, where
  $\ker(\mathfrak F)$ merges two configurations exactly when **no** declared
  task separates them:
  $j\approx j'$ iff $\operatorname{sup}_F(j)=\operatorname{sup}_F(j')$ for every
  $F\in\mathfrak F$. The quotient by $\approx$ is the coarsest retract through
  which every declared task factors — a partition $\rho$ is such a retract
  exactly when every declared task is constant on its blocks, i.e. exactly when
  $\rho$ refines $\ker(\mathfrak F)$, and the coarsest such $\rho$ is
  $\ker(\mathfrak F)$ itself — so it is the minimal sufficient boundary of
  $\mathfrak F$ *at sector-support granularity* (Appendix A.4). The empty family
  separates nothing, and its minimal boundary is the one-atom boundary; that
  convention is load-bearing several times below — in Theorem 3.5, in
  Theorem 6.1's degenerate branch and in both counterexamples of
  Proposition 8.6 — and it is cited where it bites.
- **(i-b) The Cycle B closure.** $\mathfrak F=\operatorname{Pres}_L(A(B))$,
  membership decided by the terminal availability criterion — the images of
  distinct blocks are pairwise disjoint — over the whole admitted law.
- **(ii-a) Written.** $\mathfrak F$ is non-empty and
  $\operatorname{comp}(F)=A(B)$ for every $F\in\mathfrak F$: the realized legs of
  every declared task identify exactly the configurations the boundary asserts
  are one atom, and no others. A boundary whose declared family is empty asserts
  identifications the realized process never writes because it writes nothing at
  all.
- **(ii-b) Occupied.** Let $\operatorname{Reach}(P)$ be the declared
  preparation closed under the realized legs of $\mathfrak F$. Every atom meets
  $\operatorname{Reach}(P)$, and every asserted identification is realized
  between reachable configurations.

Condition (i) is clauses (i-a) and (i-b); condition (ii) is clauses (ii-a) and
(ii-b). When a clause fails the decision procedure returns the offending
object: for (i-a) and (ii-a) a declared task together with the configuration
pair it separates inside a block; for (i-b) the tasks the closure contains and
the declaration omits; for (ii-b) the never-occupied atoms.

**What each clause is made of.** (i-a) is #103's minimality, at the
sector-support granularity the predecessor's availability criterion already
uses. (i-b) is the terminal Galois machinery. (ii-a) is the terminal co-merge
decision procedure — the realized legs. (ii-b) is the reachable-subprocess
restriction. No primitive is introduced.

---

## 3. Condition (i), and what it forces

### Theorem 3.1 — the rigidity theorem `[FIN]`, `[EXH-5]`

Let $L$ be an admitted law on a finite carrier $X$ containing the identity. A
patch $P=(B,\mathfrak F,X_0,L)$ with $B$ carrier-typed satisfies condition (i)
**if and only if** $A(B)$ is the discrete partition of $X$ and
$\mathfrak F=\{F\in L:\operatorname{comp}(F)=\text{discrete}\}$.

**Proof.** ($\Leftarrow$) $\operatorname{Pres}_L(\text{discrete})$ is exactly
the set of admitted futures whose collision partition is discrete, so (i-b)
holds; the identity lies in it and separates every pair of configurations, so
$\ker(\mathfrak F)$ is discrete and (i-a) holds.

($\Rightarrow$) By (i-b), $\mathfrak F=\operatorname{Pres}_L(A(B))$. The
identity's collision partition is discrete, which refines every partition, so
$\mathrm{id}\in\mathfrak F$. By (i-a),
$A(B)=\ker(\mathfrak F)$, and $\ker$ merges $j$ and $j'$ only if **every**
member of $\mathfrak F$ has $\operatorname{sup}(j)=\operatorname{sup}(j')$; the
identity has $\operatorname{sup}(j)=\{j\}$, so it separates every distinct
pair. Hence $\ker(\mathfrak F)$ is discrete, and $A(B)$ with it. $\square$

The two minimality notions pull in opposite directions, and the identity is
where they meet: the Cycle B closure of a boundary always contains it, and
#103-sufficiency excludes it from every proper coarse-graining. The theorem was
measured before it was proved, exhaustively: over all $2,5,15,52$ records at
two to five configurations against DET, FUNNEL, REV, the full left-total family
ALL at four configurations or fewer, and the predecessor's counter-law, the
admissible set is the singleton $\{\text{discrete}\}$ in every one of the
sixteen sweeps, without exception — and in three further sweeps on FUNNEL's
composition closure (Proposition 3.7), nineteen in all.

An equivalent form is worth recording because it welds this section to
Section 8: for a non-empty declared family, condition (i) holds at $\pi$ exactly
when $\operatorname{Obs}(L,\pi)=\varnothing$, since under (i-b) every member's
collision partition already refines $\pi$ and (i-a) then says no member
separates a pair inside a block. Rigidity is the statement that the obstruction
of a proper boundary is never empty, and the forging cost is the distance to
condition (i).

### Theorem 3.2 — the entailment `[FIN]`, `[EXH-5]`, `[CEN]`

Let $L$ be a non-empty admitted law. Condition (i) implies clause (ii-a).

**Proof.** First the declared family is non-empty. By (i-b) it is
$\operatorname{Pres}_L(A(B))$; were that empty, (i-a) would make $A(B)$ the
one-atom boundary, whose preserving family is all of $L$ vacuously — there are
no two distinct blocks whose images could meet — so $L$ itself would be empty.
Now take $F\in\mathfrak F$. By (i-a), $A(B)=\ker(\mathfrak F)$, so $F$ has the
same sector support at any two configurations of one block; those supports are
non-empty by left-totality, so those configurations share a later configuration
and $\operatorname{comp}(F)$ is coarser than or equal to $A(B)$. By (i-b),
$F\in\operatorname{Pres}_L(A(B))$, so $\operatorname{comp}(F)$ refines $A(B)$.
Finer and coarser together give $\operatorname{comp}(F)=A(B)$. $\square$

The hypothesis is exactly the degenerate case the non-emptiness requirement in
(ii-a) excludes: at the empty law, condition (i) holds vacuously at the one-atom
boundary while nothing at all is written. The decision procedure and
Definition 2.2 agree on that case, and they agree because the clause says so.

Zero counterexamples — but the sweep that reports them is nearly vacuous as
evidence, and that is said rather than left to the reader: rigidity leaves the
committed sweep exactly nineteen instances in which the antecedent is true, one
per law, every one of them the discrete boundary. The theorem is therefore
corroborated on the census instead, where it can bite: over the $687$
composition-closed laws on three configurations there are $1004$ condition-(i)
instances, $745$ of them at **proper** boundaries, with **zero** (ii-a)
failures. The consequence is stated plainly rather than hidden: **generativity's
WRITTEN clause is not an independent constraint.** The axiom's content beyond
condition (i) is the OCCUPANCY clause alone, and Section 5 exhibits the patch
that separates them.

The converse fails and is not claimed. Given (i-b), a task whose collision
partition is strictly finer than $\pi$ has disjoint and hence distinct supports
inside a block, so $\neg$(ii-a) implies $\neg$(i-a); but a task may separate
supports that still overlap, so $\neg$(i-a) does not imply $\neg$(ii-a). Clause
(ii-a) is strictly weaker than (i-a) given (i-b): the "two killing conditions"
of Section 6.1 are one condition and its consequence.

### Proposition 3.3 — admissibility is covariant `[FIN]`, `[EXH-4]`, `[CEN]`

Admissibility takes equal values on any two patches carried onto each other by
an admitted relabelling of the carrier. Measured, not assumed: over every one
of the $6$ and $24$ relabellings and every one of the $5$ and $15$ records at
three and four configurations under DET, there is no case in which a boundary
is admissible and its relabelled copy is not — zero violations of $390$
instances.

The vacuity of that sweep is disclosed with it. Of those $390$ instances the
antecedent is true in exactly $30$: rigidity leaves one admissible boundary per
relabelling, and it is the discrete one carried to itself. Covariance is
therefore re-run where it can bite — over the census, against each law's own
symmetry group, so that the identity-free laws whose admissible boundaries are
*proper* are included. $4620$ tests, zero violations.

The law-relativity is disclosed too. The predecessor's counter-law is
preserved by exactly **one** of the $120$ relabellings of the five
configurations, so under that law the covariance statement has no content.
Admission, as the predecessor cycle already found, must be certified per law.

### Proposition 3.4 — the identity-free positive control `[FIN]`, `[FIX]`

Rigidity is a statement about laws that cannot idle, not a tautology about
coarse-graining. Delete the identity from the predecessor's committed
three-configuration law of Example 4.2, leaving the two sector maps
$a=(0,0,2)$ and $b=(0,2,2)$. The pair is composition-closed — computed, since
$a\circ a=a$, $b\circ b=b$, $a\circ b=b$ and $b\circ a=a$ — and contains no
identity. Under it, the **proper** two-atom boundary $\{01\mid2\}$ is
admissible, with declared family $\{a\}$: $\operatorname{Pres}(\{01\mid2\})$ is
$\{a\}$ because $\operatorname{comp}(b)=\{0\mid12\}$ does not refine
$\{01\mid2\}$; $\ker(\{a\})$ is $\{01\mid2\}$; and
$\operatorname{comp}(a)=\{01\mid2\}$. So is $\{0\mid12\}$, symmetrically.

The control is stronger than the positive half alone. Under it the carrier's own
algebra is **inadmissible**: $\operatorname{Pres}_{\{a,b\}}(\text{discrete})$ is
empty, so its kernel is the one-atom boundary and (i-a) fails at the discrete
boundary. The axiom's admissible set there is exactly the two proper charts and
*not* the carrier's — which is the other side of the dichotomy, and the next
theorem says there is no third side.

### Theorem 3.5 — the dichotomy `[FIN]`, `[CEN]`

Let $L$ be an admitted law on a finite carrier of $n$ configurations. Then

1. $\operatorname{Pres}_L(\text{discrete})$ is exactly the set of reversible
   members of $L$;
2. the carrier's own configuration algebra is admissible **iff** $L$ contains a
   reversible operation **iff** $L$ contains the identity;
3. consequently $L$ admits either exactly one boundary — the carrier's, when it
   contains the identity, by Theorem 3.1 — or no carrier boundary at all, and
   then possibly several proper ones. There is no law of both kinds.

**Proof.** (1) $F$ preserves the discrete boundary iff the images of the $n$
singleton blocks are pairwise disjoint; $n$ pairwise disjoint non-empty subsets
of an $n$-element carrier are forced to be singletons and to exhaust it, so $F$
is a permutation, and conversely every permutation preserves it. (2) If the
discrete boundary is admissible then (i-b) makes the declared family
$\operatorname{Pres}_L(\text{discrete})$, which cannot be empty — the empty
family's kernel is the one-atom boundary, and (i-a) would fail — so by (1) $L$
contains a permutation $\sigma$; $\sigma$ has finite order, so
$\sigma^k=\mathrm{id}\in L$ by composition-closure. The converse is
Theorem 3.1's ($\Leftarrow$). (3) is Theorem 3.1 together with (2). $\square$

**The trigger is reversibility, not idling.** "Laws that can idle" and "laws
with any reversible operation at all" are the same class at a finite carrier,
and that is a much larger claim than the idling reading suggests: it covers
unitary dynamics, every law closed under a symmetry group, and every law
containing a zero-time channel.

Measured over the census, both directions: the biconditional of (2) holds
$687$ of $687$; laws containing the identity $259$, laws containing a reversible
operation $259$, laws containing a reversible operation but not the identity
$0$; laws admitting at least one proper boundary $428$; identity-containing laws
admitting a proper boundary $0$; identity-free laws admitting no proper
boundary $0$. Over a declared sample of $865$ laws at four configurations, zero
failures in both directions. The class where proper charts survive is exactly
the strictly non-idling class, it is not small — $428$ of $687$ — and it
excludes reversibility altogether.

### Proposition 3.6 — what condition (i) actually is `[FIN]`, `[EXH-5]`

Condition (i) is not Cycle B's two-sided Galois fixed point, and the difference
is where the axiom's selectivity comes from.

$\operatorname{Pres}$ is Cycle B's right adjoint and (i-b) uses it correctly.
But (i-a) uses $\ker$, which is **not** $\operatorname{Core}$. The two move in
opposite directions with the family: enlarging $\mathfrak F$ coarsens
$\operatorname{Core}(\mathfrak F)$ — more collision partitions to generate from
— and refines $\ker(\mathfrak F)$ — more tasks available to separate a pair.
Exhibited at Example 4.2's law: enlarging $\{a\}$ to $\{a,b\}$ carries
$\operatorname{Core}$ from $\{01\mid2\}$ to the one-atom boundary and $\ker$
from $\{01\mid2\}$ to the discrete boundary. $\operatorname{Core}$ is the
adjoint of $\operatorname{Pres}$; $\ker$ is the adjoint of a different pairing,
the one sending a family to the tasks constant on a boundary's blocks. Condition
(i) welds the left adjoint of one connection to the right adjoint of the other,
which is exactly the conflation Cycle B's Theorem 3.8 records.

The measured consequence is the sharpest available statement of what the
substitution buys. The genuine two-sided Cycle B condition
$\pi=\operatorname{Core}(\operatorname{Pres}_L(\pi))$ fixes **every** record —
$2$ of $2$, $5$ of $5$, $15$ of $15$, $52$ of $52$ under DET, and $52$ of $52$
under the counter-law — while the mixed condition
$\pi=\ker(\operatorname{Pres}_L(\pi))$ fixes **exactly one** at every count. The
axiom's selectivity is therefore neither inherited from Cycle B nor a discovery
about competing minimalities: it is produced entirely by the substitution, which
overshoots from *everything is a fixed point* to *exactly one is*. **Rigidity is
the signature of the mismatched pairing**, and `BLOCKED-AT-CARRIER` names one of
two available diagnoses — the other being *blocked at the choice of pairing*.

### Proposition 3.7 — FUNNEL is a declared task family, not a law `[FIN]`, `[EXH-5]`

Definition 2.1 requires an admitted law to be composition-closed. The
predecessor's committed FUNNEL family — the identity together with the
elementary sector merges — is composition-closed at two configurations **only**.
At three, $f_{0\to1}\circ f_{1\to2}=(1,2,2)$ moves two configurations and is
neither the identity nor an elementary merge, so it lies outside FUNNEL; the
same failure occurs at four and five. Measured.

FUNNEL is therefore carried here as what it is, a declared task family, and the
law it generates is swept in its place: its composition closure, which is the
identity together with every non-injective map, of sizes $22$, $233$ and $3006$
at three, four and five configurations. The three affected rigidity sweeps are
re-run on that closure and **nothing moves** — the admissible set is the
singleton $\{\text{discrete}\}$ in each, as Theorem 3.1 requires of any law
containing the identity. The FUNNEL rows are retained beside them, labelled with
their measured closure status.

---

## 4. Condition (ii), and what it adds

### Definition 4.1 — realized legs and the written record `[FIN]`

The **realized legs** of an admitted future $F$ are the transitions
$(j,j')$ with $j'\in\operatorname{sup}_F(j)$. The predecessor's non-negativity
argument applies unchanged: no entry is lost to cancellation, so a leg is
present exactly when the process can take it. The record $F$ **writes** is
$\operatorname{comp}(F)$, the co-merge partition of its realized legs — the
predecessor's own decision procedure, not a new one.

Clause (ii-a) demands that every declared task write exactly the boundary's
record. A boundary asserting an identification that no declared task's realized
legs perform is asserting something the process never writes; a boundary
merging configurations that a declared task keeps apart is asserting a block
that is a fiction. Both are the same failure seen from two sides, and both
return the same witness: the task, and the pair.

### Definition 4.2 — the reachable subprocess `[FIN]`

The patch's third component is a declared preparation $X_0\subseteq X$. The
**reachable subprocess** $\operatorname{Reach}(P)$ is the least superset of
$X_0$ closed under the realized legs of the declared family.

This is an order on configurations. It has no spatial, causal or temporal
reading; it is not a region and not a history. Clause (ii-b) demands that every
atom the boundary declares be occupied by it, and that every asserted
identification be realized between configurations the process actually
occupies.

### Theorem 4.3 — occupancy is independent `[FIN]`, `[FIX]`

Clause (ii-b) is not entailed by condition (i). The separating patch is W3 of
Section 5: both halves of condition (i) hold, clause (ii-a) holds, and the
patch is inadmissible because the declared preparation leaves two of its three
atoms never occupied.

This is the transported form of a finding the wider corpus already carries: an
identification — here, a distinction — carried by transitions the process never
takes. What condition (i) cannot see is which of the law's operations the
process actually runs. Section 7 adds the sharper form of the same limitation:
neither admitted tester statistic can see it either.

---

## 5. The minimal witness

Three configurations, one committed law, every entry an integer or a singleton
set. The law is the predecessor's Example 4.2 law $\{\mathrm{id},a,b\}$ on
$\{0,1,2\}$, composition-closed as computed, with sector supports and the
records they write:

| task | sector support | writes $\operatorname{comp}$ |
|---|---|---|
| $\mathrm{id}$ | $\{0\},\{1\},\{2\}$ | $\{0\mid1\mid2\}$ |
| $a$ | $\{0\},\{0\},\{2\}$ | $\{01\mid2\}$ |
| $b$ | $\{0\},\{2\},\{2\}$ | $\{0\mid12\}$ |

Three patches over that law:

| patch | boundary | declared family | preparation | reach | (i-a) | (i-b) | (ii-a) | (ii-b) | admissible |
|---|---|---|---|---|---|---|---|---|---|
| **W1** | $\{0\mid1\mid2\}$ | $\{\mathrm{id}\}$ | $\{0,1,2\}$ | $\{0,1,2\}$ | ✓ | ✓ | ✓ | ✓ | **yes** |
| **W2** | $\{01\mid2\}$ | $\{a\}$ | $\{0,1,2\}$ | $\{0,1,2\}$ | ✓ | **✗** | ✓ | ✓ | no |
| **W3** | $\{0\mid1\mid2\}$ | $\{\mathrm{id}\}$ | $\{0\}$ | $\{0\}$ | ✓ | ✓ | ✓ | **✗** | no |

**W1** is admissible. $\operatorname{Pres}(\{0\mid1\mid2\})=\{\mathrm{id}\}$,
whose kernel is discrete and whose written record is discrete; the preparation
occupies all three configurations.

**W2 fails condition (i) only.** Its declared family writes exactly its
boundary's record, and that boundary is the minimal sufficient boundary of the
family — but the family is not the boundary's closure:
$\operatorname{Pres}(\{01\mid2\})=\{\mathrm{id},a\}$ and the declaration omits
$\mathrm{id}$. The witness printed is that omission. (By Theorem 3.1 no
declaration repairs it: adding $\mathrm{id}$ restores (i-b) and destroys (i-a).)

**W3 fails condition (ii) only.** Both halves of condition (i) hold and the
declared task writes what the boundary asserts; the patch is inadmissible
because the declared preparation $\{0\}$ is closed under the identity's legs,
so atoms $\{1\}$ and $\{2\}$ are never occupied. The witness printed is those
two atoms.

The two conditions are therefore independently violable, and the axiom is not
one condition wearing two names. By Theorem 3.2 a (ii)-only failure must run
through the occupancy clause; W3 is that patch, and it differs from W1 in its
declared preparation alone — which is why Definition 2.1 carries the
preparation as a component of the patch, and why Section 7's statistics, which
do not read it, cannot see this failure.

---

## 6. The four discriminators

All four are run, each with the honest verdict, and two further controls are
added and reported. The full verdict table over the predecessor's committed
nine-context arena, under the committed deterministic law at five
configurations:

| context | carrier-typed | (i-a) | (i-b) | (ii-a) | (ii-b) | admissible | killed by |
|---|---|---|---|---|---|---|---|
| aligned manufactured $2{+}1{+}1$ | yes | ✗ | ✓ | ✗ | ✓ | **no** | (i-a), (ii-a) |
| aligned manufactured $1{+}1{+}1{+}1$ | yes | ✓ | ✓ | ✓ | ✓ | **yes** | — |
| aligned manufactured $2{+}2$ | yes | ✗ | ✓ | ✗ | ✓ | no | (i-a), (ii-a) |
| corrected eraser minimum | yes | ✓ | ✓ | ✓ | ✓ | **yes** | — |
| declared address family | yes | ✓ | ✓ | ✓ | ✓ | yes | — |
| corrected tomographic minimum | yes | ✗ | ✓ | ✗ | ✓ | no | (i-a), (ii-a) |
| constructed manufactured $2{+}1{+}1$ | **no** | — | — | — | — | no | (i-a), at typing |
| constructed manufactured $2{+}2$ | **no** | — | — | — | — | no | (i-a), at typing |
| constructed manufactured $1{+}1{+}1{+}1$ | **no** | — | — | — | — | no | (i-a), at typing |

Two things about this table are said here rather than left to the reader.
First, **throughout this section the declared family is set to the boundary's
closure and the declared preparation to the whole carrier**, so clauses (i-b)
and (ii-b) hold by construction in every row — measured: $52$ of $52$ records
each under DET — and the measured content of a row is clause (i-a), which under
those substitutions is the single bit *is the presented boundary the carrier's
own algebra*, again $52$ of $52$. Section 6.1.1 reads the same contexts against
other declarations. Second, the six carrier-typed rows present only **four**
distinct patches: the aligned $1{+}1{+}1{+}1$, eraser and address contexts are
the same partition under the same law, and so, by §6.5, literally the same
patch.

### 6.1 The colluding pair `[ARENA]`, `[FIN]`

This is the discriminator the cycle exists for, and it is reported first.

The predecessor's adversary declares both contexts of the arena: context one
the aligned manufactured $2{+}1{+}1$ boundary, whose atoms at the carrier are
$\{0,1\},\{2\},\{3\},\{4\}$; context two the aligned manufactured
$1{+}1{+}1{+}1$ boundary, whose atoms are the five singletons. The forged
record is the greatest record of the first — the object the predecessor proved
no one-boundary closure can reject — and it descends, with fourteen of the
first context's fifteen records certified, while the rebuilt binding
independence gate returns the pair *independent*.

**Member one is inadmissible, and the killing conditions were measured, not
assumed.** Both (i-a) and (ii-a) fail, on the **same** witness:

- the declared family is the boundary's closure, $240$ admitted operations, and
  it contains the identity;
- the identity separates configurations $0$ and $1$, which the boundary asserts
  are one atom;
- so the minimal sufficient boundary of the declared family is the five-atom
  discrete boundary, strictly finer than the declared four-atom one, and (i-a)
  fails;
- and the identity's written record is discrete, not the declared
  $\{01\mid2\mid3\mid4\}$, so the identification $\{0,1\}$ is one the realized
  legs never write, and (ii-a) fails.

The pin's expectation was that (ii) would be the killing condition. The
measurement is that (i-a) and (ii-a) fail together — which Theorem 3.2 explains:
they are not independent, so where one fails for this reason the other fails
with it. The witness printed by the decision procedure is the pair
$(\mathrm{id},\{0,1\})$: *the boundary claims an identification its own
realized legs never write.* The scope of that measurement is §6.1.1's business.

The verdict is not law-universal, and the qualifier belongs with it: member
one is inadmissible at every admitted law **containing the identity**, by
Theorem 3.1. At an identity-free law it can be admissible, and
Proposition 6.2 exhibits one. What is law-universal is the joint statement.

**Member two is admissible, and correctly so.** Its boundary is the five
singletons — which *is* the legitimate address algebra of the arena, atom for
atom. The collusion lives entirely in member one's patch, and the axiom locates
it there. The certificate is issued to the canonical patch at that boundary:
member two is admissible *for the declaration* $\mathfrak F=
\operatorname{Pres}_L(\delta)$, and clause (i-b) is what makes that the only
candidate declaration.

### Theorem 6.1 — comparable boundaries are jointly unforgeable `[FIN]`, `[EXH-5]`, `[CEN]`

Let both contexts declare the **same** admitted law $L$. Then no admitted law
makes two strictly comparable boundaries both admissible; in particular there
is no admitted law under which both members of the colluding pair are
admissible.

**Proof.** Let $\pi$ strictly refine $\pi'$. Every $F$ with
$\operatorname{comp}(F)$ refining $\pi$ has $\operatorname{comp}(F)$ refining
$\pi'$, so $\operatorname{Pres}_L(\pi)\subseteq\operatorname{Pres}_L(\pi')$ for
every $L$ — computed, and immediate. Suppose the coarser boundary $\pi'$ is
admissible under $L$. Since $\pi$ strictly refines $\pi'$, some $x,y$ lie in one
$\pi'$-block and in different $\pi$-blocks. By (i-b) and (i-a),
$\ker(\operatorname{Pres}_L(\pi'))=\pi'$, so **no** member of
$\operatorname{Pres}_L(\pi')$ separates $x$ from $y$; a fortiori no member of
the subset $\operatorname{Pres}_L(\pi)$ does either, so
$\ker(\operatorname{Pres}_L(\pi))$ merges $x$ and $y$ and is not $\pi$. The
finer boundary then fails (i-a) — and if its declared family is anything other
than $\operatorname{Pres}_L(\pi)$ it fails (i-b) instead. $\square$

The colluding pair is the instance $\pi=\delta$, $\pi'=\{01\mid2\mid3\mid4\}$.
Measured on every declared law, and on the altered law of Section 8 that
actually pays member one's price: after paying it, member two is inadmissible.
Measured in general form over the census: $277$ of $687$ laws have more than one
admissible boundary, $357$ unordered admissible pairs occur, and **zero** of
them are comparable; no law of the $687$ admits both $\{01\mid2\}$ and the
discrete boundary ($246$ admit the coarse one only, $259$ the fine one only). At
four configurations, over DET, REV and the funnel closure: $135$ comparable
pairs, zero jointly admissible. Incomparable boundaries genuinely differ —
Proposition 3.4's two proper charts coexist — so comparability is the sharp
hypothesis and not a convenience.

One degenerate branch of the proof runs through the empty-family convention: on
the paid law $\operatorname{Pres}_{\tilde L}(\delta)$ is empty, and member two
fails (i-a) because the empty family's kernel is the one-atom boundary, not
because some member fails to separate. The convention is load-bearing there and
is stated in Definition 2.2 for that reason.

### Proposition 6.2 — the mixed-law escape `[FIN]`, `[ARENA]`

The shared-law hypothesis of Theorem 6.1 is not decorative. The declared scope
of this cycle is *one law family per context*, and an adversary who uses that
freedom holds both members.

Take $L_1=\{a\}$ with $a=(0,0,2,3,4)$ on the committed carrier: composition-
closed, since $a\circ a=a$ (computed), and identity-free. Under it, member one's
forged boundary $\pi_1=\{01\mid2\mid3\mid4\}$ passes **all four clauses** —
$\operatorname{Pres}_{L_1}(\pi_1)=\{a\}$, $\ker(\{a\})=\pi_1$,
$\operatorname{comp}(a)=\pi_1$, reach is the whole carrier — with a declared
family of one task. Member two remains admissible under DET, exactly as §6.1
reports. The axiom rejects neither.

So "no admitted law whatsoever makes both members admissible" is false, and "no
single admitted law" is what is proved. Joint unforgeability is a statement
about one law, not about one adversary. Whether the predecessor's record-descent
attack still runs at $L_1$ is a separate question this cycle has **not**
measured, and the disclosure says so rather than guessing. **The mixed-law arena
— what binds two patches that declare different admitted laws — is this paper's
named open question**, and it is the physically realistic case: patches with
different effective laws.

#### 6.1.1 The kill-list is declaration-relative `[ARENA]`, `[FIN]`

Section 6's protocol *sets* the declared family to the boundary's closure. That
substitution is what makes the table's rows comparable, and it is also what
makes the reported kill-list a property of the declaration the unit supplies.
The verdict is not: it is declaration-independent, as it must be. Measured at
$\pi_1$ under DET:

| declared family at $\pi_1$ | $\lvert\mathfrak F\rvert$ | admissible | killed by |
|---|---|---|---|
| the boundary's closure — the canonical substitution | $240$ | no | (i-a), (ii-a) |
| the written-exact subfamily $\{F:\operatorname{comp}(F)=\pi_1\}$ | $120$ | no | **(i-b) alone** |
| the merging subfamily inside the closure $\{F\in\operatorname{Pres}:F(0)=F(1)\}$ | $120$ | no | **(i-b) alone** |
| the merging subfamily of the whole law $\{F\in L:F(0)=F(1)\}$ | $625$ | no | (i-b), (ii-a) |
| the single repreparation task $(0,0,2,3,4)$ | $1$ | no | **(i-b) alone** |
| the identity alone | $1$ | no | (i-a), (i-b), (ii-a), (ii-b) |

The second and third rows are the same $120$ tasks — measured, and worth
recording: inside the closure, merging $0$ with $1$ and writing exactly $\pi_1$
are the same condition. The honest form of §6.1's headline costs one clause:
**(i-b) admits exactly one declaration at any boundary, so for the unique family
that could ever pass, the kill is (i-a) together with (ii-a); under every other
declaration the kill is (i-b).** Rigidity is what makes the verdict
declaration-independent, since (i-b) pins the family before the other clauses
are asked.

### 6.3 The legitimate eraser context `[ARENA]`

The corrected eraser minimum passes **both** conditions. It is carrier-typed
with five atoms; its Cycle B closure is the $120$-member reversible family;
that family's minimal sufficient boundary is the five-atom boundary itself;
every member writes exactly that record; and the reachable subprocess occupies
every atom. All four clauses return true. It is, computation for computation,
the same patch as member two and as the address context.

### 6.4 The relabelled context, and the counter-law `[ARENA]`, `[FIN]`

**The relabelled context.** Applying the committed cyclic address shift to the
address context returns a context that is still carrier-typed and still
discrete, and the axiom returns **admissible** — as Proposition 3.3 requires it
must. This is reported as what it is: the axiom does not discriminate
relabelled copies and was never asked to. The predecessor's binding gate is the
instrument for that, and it fails the relabelled control by design; the two
instruments answer different questions and neither replaces the other.

**The counter-law.** Under the predecessor's counter-law — $120$ admitted
sector maps of which exactly one, the identity, is reversible — the address
context remains admissible and the forged boundary remains inadmissible, and
the admissible set is again the singleton $\{\text{discrete}\}$. So the
discriminator's verdicts are stable across both committed laws. What is *not*
stable is the content of the certificate: the declared family collapses from
$120$ tasks to **one**, the identity alone, because the closure of the discrete
boundary is the set of collision-free admitted futures and the counter-law has
only one. Admissibility survives while saying strictly less, and that is
disclosed rather than absorbed.

### 6.5 The arena's own two contexts `[ARENA]`

The predecessor disclosed that its declared second context coincides with the
declared overlap atom for atom, and that the rebuilt gate returns the pair
**dependent** with all $120$ relabellings as witnesses. The axiom returns both
contexts admissible, and returns more: under clause (i-b) the declared family
is a *function* of the boundary, so two contexts presenting the same boundary
under the same law are literally the same patch. What had to be disclosed in
the predecessor is derived here.

### 6.6 The three constructed manufactured contexts `[ARENA]`

All three are inadmissible, and the axiom names where: they fail the
carrier-typing gate. Their atoms' images at the committed carrier overlap —
$\{0,1,2\},\{0,1,2,3\},\{0,1,2,3\},\{4\}$ for the $2{+}1{+}1$ type — so they
are not a coarse-graining of the carrier's configurations, no family of
carrier-level tasks has any of them as its minimal sufficient retract, and
clause (i-a) cannot be satisfied at all.

The limitation is stated with the result. **The bite here is carrier-relative,
and against these three contexts it reproduces the predecessor's
rotated-versus-address-aligned biconditional rather than extending it.** What
is new in this cycle is Section 6.1, which rejects a boundary that *is*
address-aligned — exactly the case the predecessor's discriminator could not
reach.

---

## 7. The Feynman gate

The pre-registered question: does admissibility ever change a number?

### Definition 7.1 — the two admitted statistics `[FIN]`

Both are functions of the predecessor's own two-time experiment: prepare an
admitted state $\rho$, read the boundary's record (outcome $r$, a block), run a
declared task $F$, read the finest admitted later instrument (outcome $s$, a
configuration). The state is committed — the branch-memory eraser likelihoods
with a uniform source give
$\rho=(1/16,1/16,1/16,1/16,3/4)$ on the carrier.

- **Record recovery.**
  $\sigma(P)=\min_{F\in\mathfrak F}\ \sum_s\ \max_r\ \Pr(r,s)$ — the best
  achievable probability that the record is reproduced token by token, at the
  patch's worst declared task.
- **Refinement.**
  $\delta(P)=\max_{F\in\mathfrak F}\ \sum_r\bigl[\Pr(r)-\max_s\Pr(r,s)\bigr]$ —
  the probability mass on which the admitted later readout resolves a
  distinction the declared record does not.

Both are functions of the boundary, the declared family and the state. Neither
takes the declared preparation as an argument. That is recorded here because it
is a limitation, and §7.1 states what it costs.

### Theorem 7.2 — the gate is positive, via condition (i) `[FIN]`, `[FIX]`

At **one** boundary — the carrier's configuration algebra — with one law, one
state and one preparation, an admissible patch and an inadmissible patch differ
in an admitted tester statistic:

| patch at that boundary | declared family | admissible | $\sigma$ |
|---|---|---|---|
| the closure, $\operatorname{Pres}_L(\delta)$ | $120$ tasks | **yes** | $1$ |
| the closure plus the total eraser to one configuration | $121$ tasks | no; fails **(i-b) and (ii-a)** | $3/4$ |

Exactly $1$ against exactly $3/4$, both rational and both computed. The two
patches share their boundary, their law, their state and their preparation;
only the declared family differs. The comparator's kill-list is computed rather
than asserted, and it is two clauses, not one: (i-b), because the declared
family is not the boundary's closure, and (ii-a), because the added task —
the total erasure $(0,0,0,0,0)$ — writes the one-atom record rather than the
declared discrete one. Exactly one task in the family fails the written clause.
The condition whose failure changes the number is therefore condition (i);
`RQ0-L2-EMPIRICALLY-IDLE` does **not** occur.

### 7.1 The gate's honest halves

Reported with the positive, not after it. There are three.

**$\sigma$ does not separate the forgery, and it is not a function of
admissibility at a fixed boundary.** Every task in the forged boundary's
closure preserves that boundary's record, so $\sigma$ is exactly $1$ for the
forged patch too. What separates it is the refinement statistic: $\delta$ is
exactly $0$ for the admissible patch and exactly $1/16$ for the forged one —
the mass on which the admitted later readout resolves the split inside the
asserted atom $\{0,1\}$. At the carrier's own boundary the *inadmissible* patch
that declares the identity alone also has $\sigma=1$: the statistic fires in the
addition direction of (i-b) and is blind to omission. And over all $3005$
one-task extensions of the closure $\sigma$ takes four values with minimum
exactly $3/4$, attained by exactly the five constant maps — so $3/4$ is the
extreme of the comparator family, not a generic inadmissible value.

**The same-boundary form cannot be run at the forged boundary at all.** By
Theorem 3.1 there is no admissible patch there to compare against — and by §6.1.1
that holds for *every* declaration at that boundary, not merely the canonical
one. The forgery is separated across boundaries, by $\delta$, and that is a
weaker form of the gate than the one Theorem 7.2 passes.

**Neither statistic can ever see the axiom's independent clause.** By
Theorem 3.2 occupancy is the only content the axiom has beyond condition (i),
and neither $\sigma$ nor $\delta$ reads the declared preparation. Exhibited at
the committed carrier under the counter-law, where the closure of the discrete
boundary is the identity alone: two patches differing in the preparation alone —
the whole carrier against $\{0\}$ — have opposite verdicts, the second leaving
four atoms never occupied, and identical statistics, $\sigma=1$ and $\delta=0$
for both. W1 and W3 of Section 5 are the same phenomenon at three
configurations. The gate is positive for condition (i); at the axiom's
independent clause it is idle, and **an occupancy-sensitive statistic is left
open**.

---

## 8. The collusion-cost tower

### Definition 8.1 — forging cost `[FIN]`

An **alteration** of an admitted law is the addition or deletion of one
admitted operation. The **forging cost** of a declared boundary $B$ under a law
$L$ is

$$
c(B,L)=\min\bigl\{\,\lvert L\,\triangle\,\tilde L\rvert\ :\ \tilde L
\text{ composition-closed},\ (B,\operatorname{Pres}_{\tilde L}(A(B)),X,\tilde L)
\text{ admissible}\,\bigr\},
$$

the patch being the quadruple of Definition 2.1 with the whole carrier declared
as its preparation. Define the **obstruction**

$$
\operatorname{Obs}(L,\pi)=\{\,F\in\operatorname{Pres}_L(\pi)\ :\ F\text{
separates two configurations inside a block of }\pi\,\}.
$$

### Lemma 8.2 — the complement of the obstruction is a law `[FIN]`, `[EXH-4]`

$L\setminus\operatorname{Obs}(L,\pi)$ is composition-closed.

**Proof.** Suppose $h=f\circ g$ lies in $\operatorname{Obs}(L,\pi)$. If
$\operatorname{sup}_g(x)=\operatorname{sup}_g(y)$ then
$\operatorname{sup}_h(x)=\operatorname{sup}_h(y)$, so $h$ separating some $x,y$
inside a block forces $g$ to separate them too. And if $x,y$ collide under $g$,
any $l\in\operatorname{sup}_g(x)\cap\operatorname{sup}_g(y)$ contributes the
non-empty $\operatorname{sup}_f(l)$ to both $\operatorname{sup}_h(x)$ and
$\operatorname{sup}_h(y)$, so they collide under $h$; hence
$\operatorname{comp}(g)$ refines $\operatorname{comp}(h)$, which refines $\pi$,
so $g\in\operatorname{Pres}_L(\pi)$. Therefore
$g\in\operatorname{Obs}(L,\pi)$: a composite lies in the obstruction only if
its right factor does. (The argument is written for left-total relations, which
is what Definition 2.1 admits; for deterministic maps it is the familiar
statement that the fibres of $g$ refine the fibres of $h$.) $\square$

Measured exhaustively over every non-discrete boundary at three and four
configurations and over the four declared levels at five. **This lemma says
nothing about admissibility.** That the boundary is admissible in the complement
is a separate four-clause condition; it is the hypothesis of Theorem 8.3, it is
measured and not inherited, and Proposition 8.6 exhibits laws where it fails.

### Theorem 8.3 — the cost, bounded and its equality decided `[FIN]`, `[EXH-4]`, `[CEN]`

For every admitted law $L$ and every carrier-typed boundary $B$,

$$
c(B,L)\ \geq\ \lvert\operatorname{Obs}(L,A(B))\rvert ,
$$

and equality holds **if and only if** the patch
$\bigl(B,\operatorname{Pres}_{L\setminus\operatorname{Obs}}(A(B)),X,
L\setminus\operatorname{Obs}\bigr)$ is admissible.

**Proof.** *Lower bound.* Let $\tilde L$ be any composition-closed law in which
the boundary is admissible, and let $F\in\operatorname{Obs}(L,A(B))$. Suppose
$F\in\tilde L$. Membership in $\operatorname{Pres}$ depends only on
$\operatorname{comp}(F)$, which is intrinsic to $F$ and cannot be changed by
anything else in $\tilde L$; since $\operatorname{comp}(F)$ refines $A(B)$ we get
$F\in\operatorname{Pres}_{\tilde L}(A(B))$, which by (i-b) is the declared
family. But $F$ separates two configurations inside a block, so
$\ker$ of that family separates them and (i-a) fails — contradiction. Hence
$\operatorname{Obs}\subseteq L\setminus\tilde L$ and
$\lvert L\triangle\tilde L\rvert\geq\lvert\operatorname{Obs}\rvert$, additions
included. *Equality.* If $\lvert L\triangle\tilde L\rvert=
\lvert\operatorname{Obs}\rvert$ then, since $\operatorname{Obs}\subseteq
L\setminus\tilde L\subseteq L\triangle\tilde L$, the symmetric difference **is**
$\operatorname{Obs}$ and $\tilde L\setminus L$ is empty: $\tilde L$ is the
complement. So the bound is attained exactly when the complement — a law, by
Lemma 8.2 — admits the boundary. $\square$

Two consequences are recorded because they are where the general statement
stops. First, no addition can ever *remove* an obstruction member, which is why
the lower bound holds over additions too; but an addition can be **necessary**,
and Proposition 8.6 exhibits a law where the cheapest forgery uses one. Second,
the hypothesis is not a convenience: it is the exact criterion, and it fails
often. Censused over the $687$ composition-closed laws at three configurations
against every non-discrete boundary, the complement fails to admit the boundary
in $1008$ of $2748$ pairs — so in each of those the true cost is *strictly*
greater than the obstruction's size — and $927$ of them have a non-empty
complement, so this is not an artefact of emptiness.

The committed law of the tower is clean, and that is measured, not assumed:
under DET the hypothesis holds at every non-discrete boundary at three and four
configurations and at all four levels at five, and it holds under the full
left-total family ALL at three. Each measured row carries the law it was
measured under.

**Every member of the obstruction must go.** Retaining a single member $F$
leaves the declared boundary strictly coarser than the minimal sufficient
boundary of the family it belongs to, so (i-a) fails; the family tested is the
complement together with $F$, and the test is run on all $4860$ members across
the four levels of the tower — $120+360+1260+3120$ — with no exception.

### Theorem 8.4 — the tower, and the Borges reading `[FIN]`, `[FIX]`

At five configurations under the committed deterministic law of $3125$ admitted
operations, where Theorem 8.3's hypothesis is measured to hold at every level:

| level | boundary forged | cost | operations remaining | remaining is a law | admissible after |
|---|---|---|---|---|---|
| record | $\{01\mid2\mid3\mid4\}$ — one asserted identification | $120$ | $3005$ | yes | yes |
| boundary | $\{01\mid23\mid4\}$ — the aligned $2{+}2$ context | $360$ | $2765$ | yes | yes |
| coarser boundary | $\{0123\mid4\}$ — the tomographic minimum | $1260$ | $1865$ | yes | yes |
| the limit | $\{01234\}$ — everything identified | $3120$ | $5$ | yes | yes |

The cost grows strictly along the tower. At the limit, forging leaves **five**
of $3125$ admitted operations: what remains is not an altered version of the
original law but a complete alternative one — no longer a forgery within a
world but the specification of another. That is the Borges reading, and it is
stated only as far as these finite numbers carry it: four levels, one carrier,
one law family, and one measured hypothesis. Under the committed reversible law
the same arithmetic would be wrong (Proposition 8.6).

**And inside the identity-containing class there is no forgery at all.** This is
a one-line corollary of Theorem 3.1 rather than a fact about the levels swept:
$\operatorname{comp}(\mathrm{id})$ is discrete, which refines every boundary, so
the identity lies in $\operatorname{Pres}_L(\pi)$ for every law and every
boundary, and the identity separates every pair, so it lies in the obstruction
of every non-discrete boundary. Any admissible altered law must therefore delete
the identity. The class provably closed to forgery is the class of
identity-containing laws, which is larger than the five committed families; a
laboratory law under which nothing may be left alone is not one of them. So
forging any proper coarse-graining requires leaving that class, not paying a
price inside it.

`RQ0-L2-CHEAP-LAW-FORGERY` does **not** occur at the declared scope: under the
committed deterministic law the cheapest forgery deletes $120$ of $3125$
operations, under the committed reversible law it costs more than the whole law,
and inside the identity-containing class it is unavailable at any price. The
one-operation forgery of Proposition 8.6 lives at a degenerate identity-free law
of a single constant operation, outside the committed class; it is disclosed
rather than absorbed.

### Theorem 8.5 — the pair level does not grow, it terminates `[FIN]`, `[EXH-5]`

At a shared declared law, the context-pair level of the tower has no finite cost,
and no infinite one either: it is impossible. This is Theorem 6.1, restated as a
cost. Paying the record-level price of $120$ makes member one admissible and
member two inadmissible in the same breath, because
$\operatorname{Pres}(\delta)\subseteq\operatorname{Pres}(\pi_1)$, so the
deletions that blind the coarser boundary's family blind the finer boundary's
family too. Measured on the altered law itself. The hypothesis is Theorem 6.1's
and is inherited with it: if the two contexts may declare different laws,
Proposition 6.2 is the escape and no cost is paid at all.

### Proposition 8.6 — where the equality fails `[FIN]`, `[EXH-4]`

Two counterexamples to the equality $c=\lvert\operatorname{Obs}\rvert$, both
inside the objects this paper already declares.

**REV, where the complement is empty and an addition is necessary.** Every
permutation is collision-free, so its collision partition is discrete, so
$\operatorname{Pres}_{\mathrm{REV}}(\pi)$ is *all* of REV at every boundary; and
every permutation separates every pair, so the obstruction is the whole law and
the complement is **empty**. The empty declared family fails (i-a) — its
kernel is the one-atom boundary — so the boundary is not admissible in the
complement, and by Theorem 8.3 the cost is strictly greater than $n!$. It is
exactly $n!+1$: delete every permutation and **add** the block-minimum
idempotent $x\mapsto\min(\text{block of }x)$, which is idempotent, hence a law
on its own, and under which the boundary passes all four clauses — its kernel
and its written record are both $\pi$, and its preserving family is itself. So
$6\to7$ at three configurations, at each of the $4$ non-discrete boundaries, and
$24\to25$ at four, at each of the $14$: **eighteen counterexamples inside the
range the exhaustive tag advertises**. Confirmed at three configurations by
brute force over every composition-closed law at distance at most $7$, drawn
from the full left-total family.

**An empty obstruction at a boundary that is inadmissible at any price.** Take
the composition-closed identity-free law $\{\mathrm{const}_0\}$ at three
configurations and the boundary $\{0\mid12\}$. The images of the two blocks are
$\{0\}$ and $\{0\}$ — not disjoint — so the preserving family is empty, so the
obstruction is empty and $\lvert\operatorname{Obs}\rvert=0$ would report the
boundary as already admissible. It is not: with an empty declared family (i-a)
fails. The obstruction sees only over-separation *inside* a block, and is blind
to under-separation *between* blocks — the decision procedure's own second
witness branch — and to (ii-a) and (ii-b) entirely. The true cost is **one**:
deleting $\mathrm{const}_0$ leaves the empty law, still inadmissible, but a
single addition suffices, and three distinct additions achieve it, because
$\mathrm{const}_0$ never enters the declared family and so never needs removing.

---

## 9. Verdict

$$
\boxed{
\begin{array}{l}
\texttt{RQ0-L2-GENERATIVE-ATLAS-AXIOM}\\
\texttt{RQ0-L2-BLOCKED-AT-CARRIER}
\end{array}}
$$

- `RQ0-L2-GENERATIVE-ATLAS-AXIOM` — **earned at the declared scope.** The
  two-condition axiom is well posed, decidable, covariant, and discriminating
  in both directions. The colluding pair's forged member is rejected with the
  killing condition named and one witness exhibited, and with the kill-list's
  dependence on the declared family measured; the pair is jointly unforgeable at
  any shared law, in the general form that no law admits two comparable
  boundaries, with the mixed-law escape exhibited and the mixed-law arena named
  open; the legitimate eraser context passes both conditions; the relabelled and
  counter-law contexts get honest verdicts with the law-relativity disclosed;
  the arena's dependent pair is returned as one patch; and the three constructed
  manufactured contexts fail at typing.
  *Scope:* finite; one committed carrier of five configurations; the committed
  law families DET, REV, ALL (at four configurations or fewer), the counter-law
  and the funnel closure; exhaustive over all records at two to five
  configurations, with a census of $687$ laws at three where the committed sweep
  is too thin to test a claim; boundaries presented at the carrier by their
  committed incidence.

- `RQ0-L2-BLOCKED-AT-CARRIER` — **earned, and it is the price of the first
  rung.** The carrier's own configuration algebra is admissible if and only if
  the law contains the identity, equivalently if and only if it contains any
  reversible operation, so a law admits either exactly one boundary — the
  carrier's — or none of the carrier's kind and possibly several proper ones
  (Theorems 3.1 and 3.5). The trigger is reversibility, which covers unitary
  dynamics and every law closed under a symmetry group. The axiom therefore
  certifies relative to a declared carrier rather than deriving one, and the
  de-smuggling question moves up exactly one level, from the boundary to the
  carrier. The identity-free positive control (Proposition 3.4) shows the other
  side of the dichotomy is populated — $428$ of the $687$ censused laws admit a
  proper chart — and Proposition 3.6 shows the block admits a second diagnosis:
  it sits at least as much at the choice of pairing, since condition (i) welds
  $\ker$ to $\operatorname{Pres}$, which are adjoints of different connections.
  *Scope:* the same; proved and measured exhaustively, not sampled.

- `RQ0-L2-EMPIRICALLY-IDLE` — **does not occur** (Theorem 7.2), with the gate's
  three honest halves stated (§7.1), of which the third is that no statistic
  here can see the axiom's independent clause.

- `RQ0-L2-CHEAP-LAW-FORGERY` — **does not occur at the declared scope**
  (Theorems 8.3–8.5), with Proposition 8.6's degenerate one-operation forgery
  disclosed.

**What is nevertheless not earned.** No carrier. The axiom binds a declared
family to the boundary it presents — which is exactly what the predecessor's
standing obstruction asked for — but it does so by making the family a function
of the boundary and the boundary a function of the carrier. An adversary who
declares the carrier is untouched by anything here. Nor is the axiom's positive
content large where the law is rich: at every committed identity-containing law
it certifies one boundary, and the interesting charts — the proper
coarse-grainings a later atlas would need — are admissible only under laws with
no reversible operation whatsoever. And nothing here binds two patches that
declare *different* laws. Whether the programme's charts live at such laws, or
whether the carrier can itself be derived, is not decided here and is not
touched.

**The next obstruction, named.** The carrier, and beside it the mixed-law
arena. A patch certified against a carrier the adversary also supplies has not
yet measured anything the adversary did not choose — the predecessor's sentence
about the arena, one level up. Two routes are visible and neither is opened
here: derive the carrier, or show that admissibility is invariant across
carriers whose patches agree. Until one of them is taken, certification remains
relative to a declared configuration set — and, by Proposition 6.2, to a
declared law per context.

---

## 10. Non-claims

This paper claims none of the following.

- **No spatial reading of "reachability".** Reachability is an order on
  configurations: a declared preparation closed under realized legs. It is not
  separation, not distance, not a region, not a cone, not a history, and not
  any spatial or spatiotemporal notion whatsoever.
- No locality, topology, atlas-as-place, manifold or geometric object. The word
  *patch* names a quadruple of committed operational data; the word *atlas*
  names the programme's target, not an object built here.
- No influence, causal order, spacetime or Lorentzian object.
- No field, QFT, QCD or gravity object.
- **No claim that the axiom derives a carrier.** Theorems 3.1 and 3.5 say the
  opposite, and the second rung is registered with that price attached.
- **No claim that condition (i) is Cycle B's two-sided Galois fixed point.** It
  pairs $\ker$ with $\operatorname{Pres}$, which are adjoints of different
  connections, and Cycle B's Theorem 3.8 records that conflation as the one to
  avoid (Proposition 3.6).
- **No claim that condition (ii)'s WRITTEN clause is independent of condition
  (i).** It is proved entailed (Theorem 3.2); only the occupancy clause is
  independent.
- **No claim that the forging cost equals the obstruction's size in general.**
  That is false, and Proposition 8.6 refutes it inside the declared objects.
  What is claimed is the lower bound, sound everywhere, and the equality exactly
  where the complement admits the boundary — measured under the law the tower
  runs at.
- **No claim that joint unforgeability holds across different declared laws.**
  It is a statement about one law shared by both contexts, and the mixed-law
  escape is exhibited (Proposition 6.2).
- **No claim that an admitted statistic here can see the occupancy clause.**
  Neither tester statistic reads the declared preparation, and an
  occupancy-sensitive statistic is left open.
- No claim that provenance is measurable. Every verdict here is computed from
  declared boundaries, declared families, declared preparations and admitted
  laws; how a boundary came to be declared is not laboratory data and is not
  used.
- No claim beyond the committed law families, the census population and the one
  committed carrier. Nothing is claimed for infinite dimension, for other
  carriers, or for laws not run.
- No claim that the axiom subsumes the predecessor's binding independence gate.
  The two answer different questions; the axiom passes the relabelled context
  that the gate fails.

---

## 11. Reproduction

`v13/code/rq0_l2_admissibility_exact.py` regenerates every number in this
paper. Exact arithmetic throughout; substantive negatives exit $0$; anchor
mismatches exit $1$. $32$ gates and $45$ anchors. `--falsification-selftest`
runs every mutant — $8$ anchor mutants and $10$ derivation mutants — each of
which must exit $1$. No wall-clock value enters the receipt or the rendered
output, so two runs of the same source produce byte-identical artifacts.

Outputs: `rq0_l2_admissibility_output.txt`, `rq0_l2_admissibility_receipt.json`.

Anchors reproduce, by this unit's own routes, every committed value it reuses:
the Bell record-lattice sizes $1,2,5,15,52$; the FUNNEL family sizes
$3,7,13,21$; the reversible law's single fixed record at every atom count; the
DET fixed-record counts $1,2,5,15,52$; the counter-law's $120$ maps with
exactly one reversible and all $52$ records fixed; Example 4.2's closed law,
its three realized collision partitions and its $4$-of-$5$ fixed records; the
minimal classical experiments $1$ and $5$ of the preserving and eraser tasks;
the eraser likelihood weights $3/4$ and $1/4$; the core atom counts $5$ and
$2$; the constructed manufactured centre dimensions $4,3,5$ and the $2{+}1{+}1$
incidence; the aligned manufactured incidences; the colluding pair's $14$
certified records, its descending forged record and its passing gate verdict;
the duplicate-boundary form's $12$ carrying relabellings; the third form's $4$;
the arena pair's dependence with $120$ witnesses; the eraser context's $51$ of
$52$; and the DET and REV cardinalities $3125$ and $120$.

The three-lens hostile panel of this cycle — operator, effectus/order and
instrument — supplied constructions this paper carries natively: the REV and
$\mathrm{const}_0$ counterexamples of Proposition 8.6 and the equality
criterion's census (operator); the $\ker$/$\operatorname{Core}$ contrast of
Proposition 3.6, the reversibility trigger of Theorem 3.5, the entailment
population of Theorem 3.2 and the occupancy blindness of §7.1 (effectus); the
declaration-relative table of §6.1.1, the patch's fourth component, the
comparator's second failing clause and the dichotomy's converse (instrument).
The mixed-law escape of Proposition 6.2 was constructed independently by two of
the three.

---

## Appendix A. Declared deviations from the frozen pin

Per the #121 rule, every deviation ships with the delivery.

1. **Condition (ii) is operationalized as two clauses**, WRITTEN and OCCUPIED,
   rather than one. The pin's phrase — "each task is one the boundary's
   realized process actually writes" — separates cleanly into a statement about
   what the realized legs identify and a statement about which configurations
   the process occupies, and the two behave differently: the first is proved
   entailed by condition (i) (Theorem 3.2), the second is independent
   (Theorem 4.3). Both are reported; the entailment is stated as a limitation
   of the axiom, not smoothed over.

2. **The pin expected condition (ii) to be the killing condition for the
   colluding pair.** The measurement is that (i-a) and (ii-a) fail together, on
   one witness, and Theorem 3.2 says why they must. The pin's instruction to
   measure rather than assume is what produced this; the expectation is
   recorded as refuted. The measurement is relative to the declaration the unit
   supplies, and §6.1.1 gives the kill-list under five further declarations: for
   the only family that could satisfy (i-b) the refutation stands, and under
   every other declaration the kill is (i-b).

3. **The minimal witness's (ii)-only cell runs through the occupancy clause**,
   because Theorem 3.2 forbids a WRITTEN-only failure with condition (i)
   intact. W3 therefore differs from W1 in its declared preparation, not in its
   law. Three configurations, under the pin's cap of five.

4. **#103-minimality is computed at sector-support granularity**, the same
   granularity the predecessor's availability criterion uses, and on the
   process-boundary reading of #103 — the coarsest retract through which the
   declared tasks factor. That identification is now proved in Definition 2.2
   and gated: the minimum-atom retract is recomputed independently of $\ker$ at
   every boundary of every censused law and compared, $3435$ families, zero
   mismatches. The granularity is strictly coarser than the letter-side kernel,
   since equal supports do not imply equal likelihood columns; the letter-side
   minimal classical experiments of the branch-memory tasks are anchored
   separately as controls ($1$ and $5$) and are not the object condition (i-a)
   tests.

5. **Boundaries are presented at the committed carrier by the predecessor's
   incidence**, so the carrier-typing gate is carrier-relative. Against the
   three constructed rotated contexts this reproduces the predecessor's
   rotated-versus-address-aligned biconditional rather than extending it, and
   §6.6 says so.

6. **Two controls beyond the pin's four discriminators are added and
   reported**: the identity-free positive control (Proposition 3.4), without
   which the rigidity theorem would read as a triviality; and the joint
   unforgeability of the colluding pair (Theorem 6.1), which the pin did not
   ask for and which is the cycle's strongest result.

7. **The Feynman gate's same-boundary form could not be run at the forged
   boundary**, because rigidity leaves no admissible comparator there. The
   gate's positive is established at the carrier's own boundary as the pin
   requires; the forgery is separated by a second statistic across boundaries;
   and a third limitation is stated with them in §7.1 — neither statistic reads
   the declared preparation, so neither can see the occupancy clause.

8. **The cost tower's levels** are instantiated as record → boundary → coarser
   boundary → limit, with the pin's context-pair level proved *impossible*
   rather than costed (Theorem 8.5). The pin's "law" level is the limit row,
   where the remaining law has five operations.

9. **The forging cost admits alterations that leave the committed class of
   laws.** The identity lies in the obstruction of every non-discrete boundary
   at every identity-containing law, so within that class the cost is unpayable;
   the finite numbers of Theorem 8.4 are the costs when the identity may be
   deleted. Both readings are reported, the stronger one — the unpayability —
   first in §8.4 and in the abstract alike. The unpayability reading is not an
   independent measurement: it is Theorem 3.1's mechanism restated, true by one
   line for every identity-containing law and not only for the obstructions
   computed here.

10. **Lean: none**, as pinned. **No new primitive**, as pinned: every object
    used is committed structure from Cycles B and B′ and from #103/#111.

11. **The pin's condition (ii) reads "the declared task family is GENERATED BY
    THE PATCH'S OWN ADMITTED DYNAMICS".** In the delivered axiom the family is
    generated by the *law*, through (i-b), which makes it
    $\operatorname{Pres}_L(A(B))$; what survives of generativity is a *test on*
    the realized legs together with occupancy, not a generation condition. The
    pin's operational demand — exhibit the offending task — is met; the
    generation reading is dropped, and that is declared here rather than left
    implicit in Deviation 1.

12. **The patch is a quadruple, not the triple the pin's parenthesis names**
    ("context: boundary + declared task family + admitted law"). Clause (ii-b)
    is a function of the declared preparation, and W1 and W3 differ in it alone
    while receiving opposite verdicts, so admissibility is not a function of the
    triple. Definitions 2.1 and 8.1 carry the fourth component, and Definition
    8.1 fixes it at the whole carrier.

13. **Section 6 supplies the declaration it then adjudicates.** For every
    context the declared family is set to the boundary's closure and the
    preparation to the whole carrier, so (i-b) and (ii-b) are true by
    construction in every row of the verdict table — $52$ of $52$ records each,
    measured — and one bit per row is genuinely measured. The substitution is
    what makes the rows comparable; §6.1.1 is the disclosure and the alternative
    declarations.

14. **FUNNEL is not composition-closed at three configurations or more**, so it
    is not a law in the sense of Definition 2.1. It is carried as a declared
    task family, its committed sizes $3,7,13,21$ are anchored as the
    predecessor's values, and the three rigidity sweeps that used it are re-run
    on the law it generates, where nothing moves (Proposition 3.7).

15. **The exact-cost claim is false in general, and the paper states the bound
    and the criterion instead.** Theorem 8.3 as delivered is a lower bound
    valid at every admitted law together with an exact criterion for equality;
    the tower's numbers are unchanged because the criterion is measured to hold
    under the law they were computed at. Proposition 8.6 is the refutation, and
    the general claim that additions never help is withdrawn: at the committed
    reversible law an addition is necessary.
