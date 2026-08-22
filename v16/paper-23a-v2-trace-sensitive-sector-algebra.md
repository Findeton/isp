# Paper 23a v2 — trace-sensitive sector classes and the honest fusion classification

Date: 2026-08-22

Status: **CONSTRUCTED CANDIDATE — SUBMITTED FOR THREE-SEAT BLIND REVIEW**

Bound to the frozen v2 pin `v16/note-paper23a-v2-pin.md` (ordinary
SHA-256 `26587fb58f4f30eb52f9daff725d547ba1d7547ead6f1255ce2ae2a83d0b5dd7`,
ledger #315). This paper executes the user's authorization: stages 1–2
repaired exactly as adjudicated at #314; stage 3 rebuilt on the honest
trace-sensitive class family with every algebraic clause proved,
refuted, or blocked on its own; finite-closure failure proved by
carrier monotonicity; the FP fusion-bootstrap route closed for the
present $\Gamma_D$ fixtures. No rescue quotient is introduced anywhere;
no associativity, dual, semiring, fusion ring, or FP character is
assumed; Paper 22 v3 is consumed nowhere. Every number was re-verified
in exact rational arithmetic before this document froze; the harness
is scaffolding and enters no proof.

Scope walls unchanged from v1: no channel odds, opportunity/activity/
root law, `Pi_phys`, `Gamma_struct`, chronology, dimension, metric,
gravity, actuality. Paper 17 gate CLOSED.

## 1. Referent census

Identical to v1 §1 (twelve referent classes of terminal Paper 13D at
bytes `3b91766f…`), with one clarification forced by the v1 rejection:
**process complex** now explicitly includes composites built from the
certified generators by categorical composition — in particular tensor
composites, single simultaneous fusions, and staged words of fusions —
each counted as a fixture whenever its generators are certified. The
census invents no new generator; it only refuses to discard composites
that v1 silently identified.

## 2. Stage 1 — trace-sensitive congruence (with the #314 replacement)

> **Definition 2.1 (predictive-sector congruence; #314-adopted form).**
> Complexes $\chi,\chi'$ are predictively equivalent, written
> $\chi\sim\chi'$, when they are alignable by some $g$ and the
> following comparison is exact: form the ordered aligned pair
> $(\chi,\chi')$, push both presented laws onto the common stabilizer
> orbits of the shared typed comparison space exactly as in Paper 13D
> Section 15, and require equality of the two pushed laws on every
> comparison cell. Equivalently: for every legal future $f$ of $\chi$
> with transported counterpart $f^{g}$ of $\chi'$, and every
> equivariant reader $R$ of $\chi$ with transported counterpart
> $R^{g}$ of $\chi'$ — counterparts declared by the groupoid action on
> the comparison object, not by map identity — the transported laws
> agree.

> **Lemma 2.2.** $\sim$ is an equivalence relation.
>
> **Proof.** As v1 Lemma 2.2: reflexivity by the identity alignment;
> symmetry by $g^{-1}$ with functorial pushforward; transitivity by
> composing alignments through the intermediate comparison object —
> legitimate because the diagonal comparison construction is itself
> functorial in the aligning morphism. ∎

> **Theorem A (congruence).** With Definition 2.1, $\sim$ is
> compatible with: (1) tensor; (2) single simultaneous fusion;
> (3) futures and composition; (4) paired restriction/deletion — if
> $\chi\sim\chi'$ are aligned by $g$, then for each occurrence $i$ of
> $\chi$, the deletions at $i$ and at $g(i)$ give congruent
> complexes, and consequently the uniformly selected unmarked deletion
> laws correspond as well; (5) stable words and erasure.
>
> **Proof.** As v1 Theorem A for clauses (1),(2),(3),(5) — each cited
> transport is functorial and bijective on diagnostic catalogues, so
> the diagonal comparisons agree termwise. Clause (4): deletion
> removes exactly the factors, bonds, seeds, and addresses incident to
> the deleted occurrence (Paper 13D §14, Thm 7), so the restricted
> pair remains aligned by the restricted $g$ and the comparison cells
> restrict bijectively. ∎

### 2.1 Trace shape as a class coordinate

> **Definition 2.3.** The **trace shape** of a complex $\chi$ is the
> isomorphism type of its typed string diagram — the ordered list of
> generator vertices with their boundary sorts and occurrence-carrier
> supports — as retained in every complete history of $\chi$
> (Paper 13D §7.1 retains all traversed boundaries).

> **Proposition B (trace-shape separation).** If two complexes have
> non-isomorphic trace shapes, then $\chi\not\sim\chi'$.
>
> **Proof.** The complete reader of $\chi$ is the identity on its
> outcome fiber, whose cells retain the complete trace (§7.1). Under
> the diagonal comparison, the pushed laws sit on disjoint orbit
> families whenever the retained boundary sequences differ: no
> stabilizer translate maps a history of one trace shape onto a
> history of the other, because transport acts diagonally and
> preserves the syntax-tree type of the experiment that produced the
> history. Hence some comparison cell has mass on one side only. ∎

### 2.2 Fixture computation

With trace shape now explicit, the certified classes at each size $n$
include at least:

$$
[\mathrm{U}(n)],\ [\mathrm{DQ}(n)],\ [\mathrm{RQ}(n)],\
[\mathrm{SRQ}(n)],\ [\mathrm{EQ}(n)]
$$

(v1's five families — Propositions A.1–A.2 of v1 hold verbatim under
Definition 2.1, being trace-shape separations), **plus** for each
factorization the composite classes:

$$
[\mathrm{T}_2(n)]\ (\text{tensor of two primitives}),\quad
[\Phi_2(n)]\ (\text{one simultaneous binary fusion}),\quad
[\Phi(\mathrm{T})](n)\ \text{etc.}
$$

> **Proposition C (bracketing separation).** For three one-occurrence
> sources, the left-bracketed staged word
> $\bigl(\Phi(U_1\boxtimes U_1)\bigr)\boxtimes U_1$ followed by
> $\Phi$, and the right-bracketed word
> $U_1\boxtimes\bigl(\Phi(U_1\boxtimes U_1)\bigr)$ followed by
> $\Phi$, are incongruent: their intermediate fused frontiers have
> occurrence-carrier supports $\{1,2\}$ versus $\{2,3\}$, retained in
> the respective histories; by Proposition B they are distinct
> classes. Both are distinct from the simultaneous triple fusion
> $\Phi_3(U_1\boxtimes U_1\boxtimes U_1)$ (one fewer traversed
> boundary) and from the primitive $U(3)$ (no fused boundary).
>
> **Proof.** Direct application of Proposition B to the four trace
> shapes; the frontier-support lists are read off §7.1/§10.2 verbatim:
> left bracket retains frontiers over $(\{1\},\{2\})$ then
> $(\{1,2\},\{3\})$; right bracket over $(\{2\},\{3\})$ then
> $(\{1\},\{2,3\})$. These lists are not isomorphic as ordered
> supported diagrams. ∎

Outcome: **`P23AV2-SECTOR-CONGRUENCE-TRACE-SENSITIVE-CONSTRUCTED`**
on the certified fixtures.

## 3. Stage 2 — multiplicity descent, repaired

Definitions 3.1 and Theorem B carry from v1 with the four #314
replacement sentences applied verbatim:

- chain proof (F-P1): constancy on classes follows by composing the
  per-pair transport argument along any congruence chain; on the
  certified fixtures each class is a single family-size-sort-trace
  cell, so chains collapse, but the proof covers them anyway;
- arithmetic sentence (F-C6/F-P2): the labeled support of
  $U_{\varnothing}(1)$ has $16\times4\times2=128$ positive traces
  (sixteen source tuples, four packets compatible with each
  $(c,e^0)$, two endpoints), drawn from $16\times625$ seed
  combinations, and normalization is exact;
- endpoint mass hypotheses (F-P3): the fair source marginal of $q_0$
  and the column symmetry $B^2_{j0}=B^2_{j1}$ give
  $M([\mathrm{DQ}(n)])(q_2{=}j)=\sum_a \tfrac12B^2_{ja}=\tfrac12$ —
  these are complete-reader $q_2$-pushforwards of descended cell
  masses;
- alignment-independence clause (F-P4): two alignings of the same
  pair differ by a stabilizer translate, under which every orbit sum
  is fixed pointwise.

Fixture tables: identical to v1 §3.2 and independently reproduced by
all three v1 seats and re-reproduced here — $U_{\varnothing}(1)$:
96 cells / 64 swap-fixed / six distinct masses
($3969/6250000^{\times16}$, $784/390625^{\times16}$,
$882/390625^{\times16}$, $2916/390625^{\times16}$,
$9216/390625^{\times16}$, $10368/390625^{\times16}$);
$D\circ Q^0_{\varnothing}(1)$: 192 / 128 / eight masses; endpoint
conditional $=B^2$ entrywise; bond marginals
$P(\ell_{ij}{=}1)=\tfrac12$ and the uniform three-pair pattern. New
under trace sensitivity: the composite classes above inherit masses
by the same descent — e.g. $[\Phi_2(1)]$ carries the joint law of
(tensor source, fused target) pairs, which is the product structure
of §10.2 with fresh cross-bond seeds; its total mass is $1$ by
normalization of the fusion kernel.

Outcome: **`P23AV2-MULTIPLICITY-DESCENT-REPAIRED-CONSTRUCTED`**.

## 4. Stage 3 — the honest classification

Throughout, fix the trace-sensitive family
$\mathsf{Sect}^{ts}_{13D}$ of certified complexes modulo $\sim$.
Define, wherever both arguments admit fusion into the same sort:

$$
[\chi]\otimes[\chi']=[\Phi_s(\chi\boxtimes\chi')].
$$

Each clause below is proved, refuted, or blocked on its own. Nothing
is assumed.

> **Proposition D (well-definedness).** $\otimes$ is well defined on
> $\mathsf{Sect}^{ts}_{13D}$: if $\chi\sim\bar\chi$ and
> $\chi'\sim\bar\chi'$, then
> $[\Phi_s(\chi\boxtimes\chi')]=[\Phi_s(\bar\chi\boxtimes\bar\chi')]$.
>
> **Proof.** Theorem A(1)+(2) compose the two alignments through the
> tensor and the fusion generator; the diagonal comparisons agree
> because each generator's kernel is equivariant and the fresh
> cross-pair seed sets are carried bijectively. ∎

> **Lemma E (carrier monotonicity).** Let $\mathrm{carr}(\chi)$ be
> the occurrence carrier of $\chi$. Then
> $\mathrm{carr}([\chi]\otimes[\chi'])=
> \mathrm{carr}(\chi)\sqcup\mathrm{carr}(\chi')$ as a label set up to
> transport, so
> $|\mathrm{carr}(\chi\otimes\chi')|=|\mathrm{carr}(\chi)|+
> |\mathrm{carr}(\chi')|$, strictly greater than either factor's size
> when the other factor is nonempty.
>
> **Proof.** Fusion unions occurrence fields (Paper 13D §10.2); no
> generator deletes occurrences. Transport relabels but never changes
> cardinality. ∎

> **Theorem F (finite closure fails).** No finite nontrivial
> subfamily of $\mathsf{Sect}^{ts}_{13D}$ is closed under $\otimes$.
>
> **Proof.** Take any nonempty finite subfamily containing a class
> with carrier size $\ge1$. Repeated products with any nonempty-
> carrier class strictly increase carrier size without bound
> (Lemma E), leaving the subfamily after finitely many steps. Only
> subfamilies of empty-carrier classes close trivially. ∎

Outcome: **`P23AV2-FINITE-CLOSURE-FAILS-BY-CARRIER-MONOTONICITY`.**
This replaces the v1 claim with a proof that identifies no classes
across trace shapes.

> **Proposition G (commutativity).** $[\chi]\otimes[\chi'] =
> [\chi']\otimes[\chi]$.
>
> **Proof.** The fusion generator is indexed by the finite *family*,
> not an ordered list, and gives the same kernel after the symmetric
> braiding (Paper 13D §10.2); braiding is an isomorphism in
> $\mathsf{Exec}_D$ (§5.2). The braiding map transports the diagonal
> comparison object of $(\Phi(\chi\boxtimes\chi'),\,
> \Phi(\chi'\boxtimes\chi))$ identically componentwise, so both sides
> satisfy the same comparisons against every third complex; being
> congruent to each other, they are equal classes. ∎

Outcome: **`P23AV2-CLASS-PRODUCT-COMMUTATIVE`**.

> **Proposition H (associativity fails at class level).** There exist
> certified complexes $\chi_1,\chi_2,\chi_3$ (one occurrence each)
> with
> $[L]=[(\Phi(\Phi(\chi_1\boxtimes\chi_2))\boxtimes\chi_3)\text{
> fused}] \neq [R]$, the right-bracketed analogue.
>
> **Proof.** By Proposition C, the left- and right-bracketed staged
> words are incongruent — their retained intermediate frontier
> supports differ ($\{1,2\}$ then union-with-$\{3\}$, versus
> $\{2,3\}$ then union-with-$\{1\}$) and Proposition B separates
> them. But $[L]$ and $[R]$ are precisely the two bracketings of
> $\chi_1\otimes\chi_2\otimes\chi_3$ under $\otimes$. ∎

Outcome: **`P23AV2-CLASS-PRODUCT-NONASSOCIATIVE`**.

> **Proposition I (unit).** The empty-complex class $\mathbf 1 =
> [U_{\varnothing}(\emptyset)]$ satisfies
> $\mathbf 1\otimes[\chi]=[\chi]=[\chi]\otimes\mathbf 1$ for every
> certified $[\chi]$: fusing with the empty family adds no cross
> pairs and unions no occurrences, and the trace shape gains only a
> degenerate fusion vertex over an empty component, which the
> diagonal comparison cannot distinguish from the unfused complex —
> both retain identical field content, and the added vertex carries
> no address, no seed, and no bond.
>
> **Proof sketch made exact:** the fusion kernel over an empty second
> component draws zero seeds and applies the identity on fields; the
> resulting history equals the original history pointwise; hence the
> presented laws coincide before quotienting, a fortiori after. ∎

> **Proposition J (duals absent).** No class $x$ with nonempty
> carrier admits $y$ with $\mathbf 1$ inside $x\otimes y$ in the
> strong sense required for a based-ring involution: since
> $\mathrm{carr}(x\otimes y)=\mathrm{carr}(x)\sqcup
> \mathrm{carr}(y)$ (Lemma E) while
> $\mathrm{carr}(\mathbf 1)=\emptyset$, we would need
> $|\mathrm{carr}(x)|+|\mathrm{carr}(y)|=0$, impossible for nonempty
> carriers. Hence `P23AV2-DUALS-ABSENT`.

### 4.1 Classification of what actually exists

Assembling the proved clauses: $(\mathsf{Sect}^{ts}_{13D},
\otimes,\mathbf 1)$ is a **commutative unital nonassociative magma
with cancellation-free monotone grading** by carrier size — more
plainly: a commutative unital groupoid-under-$\otimes$ (total,
well-defined operation) that is graded by $\mathbb N$ with
$|x\otimes y|=|x|+|y|$, has no duals, and is not associative. It is
not a semiring (associativity fails; there is not even an addition),
not a fusion ring (no involution possible), and supports no character
equation. The free such structures exist abstractly, but nothing
here needs or uses freeness: every clause above was checked on the
certified fixtures.

Tag: **`P23AV2-ALGEBRA-COMMUTATIVE-UNITAL-GRADED-NONASSOCIATIVE-MAGMA`**.

### 4.2 FP-route disposition

Since associativity fails at class level (Proposition H), the
Frobenius–Perron bootstrap route — finite based ring, positive
character $d_xd_y=\sum_zN_{xy}^zd_z$, conditional channel odds —
has **no subject matter** on the present $\Gamma_D$ fixtures:

> **`P23AV2-FP-BOOTSTRAP-ROUTE-CLOSED-FOR-PRESENT-GAMMA`**, with
> scope exactly: the certified fixtures of terminal Paper 13D under
> the trace-sensitive congruence. This is not a global no-go: it does
> not exclude that some future enlarged law (e.g. a successfully
> constructed `Gamma_struct`) carries an associative sector product,
> nor that a different congruence justified by new physics could
> change the verdict — only that no accepted object today supplies
> one, and none may be introduced to rescue fusion (control 19).
> Parent control 40 respected verbatim.

### 4.3 Classification table

| stage | object | outcome | exact scope |
|---|---|---|---|
| 1 | congruence | TRACE-SENSITIVE CONGRUENCE CONSTRUCTED | Def 2.1 (#314 form); Thm A; Props B–C |
| 2 | multiplicity descent | REPAIRED DESCENT CONSTRUCTED | Def 3.1 + six replacements; §3 tables |
| 3a | well-definedness | PROVED | Prop D |
| 3b | finite closure | FAILS BY CARRIER MONOTONICITY | Lemma E; Thm F |
| 3c | commutativity | HOLDS (proved) | Prop G |
| 3d | associativity | FAILS at class level | Prop H via Prop C/B |
| 3e | unit | EXISTS | Prop I |
| 3f | duals | ABSENT | Prop J via Lemma E |
| 3g | algebra tag | COMMUTATIVE UNITAL GRADED NONASSOCIATIVE MAGMA | §4.1 |
| 3h | FP bootstrap | CLOSED FOR PRESENT GAMMA | §4.2 |

Pre-registered outcomes earned, exactly:

```text
P23AV2-SECTOR-CONGRUENCE-TRACE-SENSITIVE-CONSTRUCTED
P23AV2-MULTIPLICITY-DESCENT-REPAIRED-CONSTRUCTED
P23AV2-FINITE-CLOSURE-FAILS-BY-CARRIER-MONOTONICITY
P23AV2-CLASS-PRODUCT-NONASSOCIATIVE
P23AV2-CLASS-PRODUCT-COMMUTATIVE
P23AV2-DUALS-ABSENT
P23AV2-ALGEBRA-COMMUTATIVE-UNITAL-GRADED-NONASSOCIATIVE-MAGMA
P23AV2-FP-BOOTSTRAP-ROUTE-CLOSED-FOR-PRESENT-GAMMA
```

Not earned (correctly, per pin): `P23AV2-CLASS-PRODUCT-ASSOCIATIVE`,
`…-NOT-WELL-DEFINED`, `-NONCOMMUTATIVE`, `…DUALS-PRESENT`,
`…FP-BOOTSTRAP-ROUTE-OPEN`.

## 5. Hostile-control matrix (v1 eighteen + new four)

| # | control | disposition |
|---|---|---|
| 1 | staged vs simultaneous trace | Props C/H: separated at class level, never equated |
| 2 | seed multiplicity as channels | $N$-talk eliminated entirely; no multiplicity numbers printed in stage 3 |
| 3 | automorphism orbit size as channel | masses remain full-orbit sums (Def 3.1); PASS |
| 4 | finite cutoff manufactures closure | no cutoff taken; failure proved by unbounded escape |
| 5 | mark called endogenous | no opportunity law exists |
| 6 | phi=0 cosmological constant | no phase exists |
| 7 | FP odds as opportunity rate | no odds exist; §4.2 closes route |
| 8 | source family as one operator | none constructed |
| 9 | apparatus hides root | no apparatus beyond census |
| 10 | complement exposure changes recovery | no commit used |
| 11 | spectator changes orbit multiplicity | orbit sums stable (Thm B repaired) |
| 12 | desired dimension selects | no dimension anywhere; ladder untruncated |
| 13 | reader family chosen | Def 2.1 quantifies over all admitted readers |
| 14 | representative mass | forbidden; all sums full-orbit |
| 15 | semiring from nonnegativity | no semiring claimed; associativity refuted first |
| 16 | character uniqueness assumed | no character equation exists (§4.2) |
| 17 | FP dimensions as states/odds | blocked by §4.2 closure |
| 18 | Paper 22 v3 as source | consumed nowhere |
| 19 | rescue quotient | refused: trace shapes kept distinct even where doing so destroys niceness |
| 20 | target-level associativity asserted | Prop H proves the opposite; final-target equality never promoted |
| 21 | commutativity unproved | Prop G proves it from the family-indexed generator + braiding transport |
| 22 | FP closure overstated | §4.2 scope engraved: present-$\Gamma_D$ fixtures only |

## 6. What is and is not constructed

Constructed at fixture scope: the trace-sensitive congruence; the
repaired descent; well-definedness, commutativity, unit,
nonassociativity, absence of duals, carrier-monotone infinite escape;
the algebra tag; the scoped FP-route closure. Not constructed, and
not inferable: everything on the v1 wall list, plus any associative
refinement, any quotient coarser than $\sim$, any statement about
laws other than the present $\Gamma_D$'s certified fixtures. Paper
17 gate CLOSED. No code; no new physical postulate; no automatic v3.

## 7. Comparators

As v1 §7: Etingof–Nikshych–Ostrik (fusion-ring axioms deliberately
failed here by Propositions H/J), Mac Lane (symmetric monoidal
syntax), terminal Paper 13D bytes. No comparator supplies any
probability, sector, or closure datum.
