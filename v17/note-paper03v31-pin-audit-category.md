# Paper 03 v3.1 independent pin audit — category and mathematics

## Atomic restart, integrated records, and exact semantic composition

Date: 2026-08-22

Status: **RESULT-NEUTRAL INDEPENDENT PIN AUDIT**

Verdict: **ACCEPT-FOR-CONSTRUCTION-WITH-BINDING-SCOPE**

First exact semantic or implementability blocker: **none**.

The v3.1 pin repairs the v3 point-state contradiction without changing the
v2 stochastic kernels or quantum probabilities. Its central mathematical
move is sound: point samples remain in `Ev`, while only dominated ensemble
laws are paired with the $L^\infty$ hybrid algebra through `Ens`. Finite and
atomic records retain exact normal point states. Generic nonatomic point
restart is explicitly refused.

This verdict authorizes an attempt at one mathematics-only construction. It
does not award a Paper 03 coordinate, certify an instrument not yet built, or
open Paper 04. Every conditional admission and refusal below is binding.

## 0. Authentication, chronology, and blindness

The audit began and ended at exact committed HEAD
`a4c4d4eb9aad2fa3e4ad1f06050b71fb4b6afb58`, whose sole parent is
`91c99fef73867ccbae7b2e3f037ee490182fc259`. HEAD is the immutable pin commit
`v17 #50: freeze Paper 03 v3.1 integrated semantics pin`.

| Bound artifact | Recomputed SHA-256 | Exact size |
|---|---|---:|
| `v17/note-paper03v31-integrated-hybrid-semantics-pin.md` | `b7ec12ad25c3ac6327cb242ad39ba03e1af541e544f11d32cb86dbce908b5fca` | 760 LF / 30,236 bytes |
| `v17/note-paper03v3-pin-audit-adjudication.md` | `a4cba0b98ceafa65888bca1a57b8b8205b26c186f264a807a37daf4c5eecb087` | 422 LF / 16,061 bytes |
| `v17/note-paper03v3-hybrid-instrument-semantics-pin.md` | `ada49694c66911455c2980c896ea10f8741d668ebb8af909e2f061c9d6e6d9af` | 597 LF / 25,686 bytes |
| `v17/note-paper03v3-pin-audit-category.md` | `5430ece42ca9e09c82442a9ea2abfa77127b579e06cc9be6b023cc7de780f3fc` | 422 LF / 19,117 bytes |
| `v17/note-paper03v3-pin-audit-quantum.md` | `ca5d9d8e2e1c97c86862f813709cd1c42b3e0b4e74a67a4c8f764f6285190f28` | 597 LF / 28,350 bytes |
| `v17/note-paper03v2-hostile-review-adjudication.md` | `74303ddd93b4aac35d3368760da4a0ad3d442570cb16320467076aa5f93ea358` | 476 LF / 22,617 bytes |
| `v17/paper-03v2-causal-frontier-relativistic-adequacy.md` | `93eaa95fba10831618512ab95447d3527ff5d8877ab5119237f73bb8c30e0181` | 958 LF / 36,711 bytes |
| `v17/paper-00-reality-first-programme.md` | `a9f8456763447eaa25a6a840e8f221f51d961ecd9c3ced649ae35a8616457cbe` | 476 LF / 21,268 bytes |

The pin and every bound authority were read completely before judgment. The
prior v3 quantum audit was read only because v3.1 explicitly binds it as
historical authority. No concurrent v3.1 quantum audit, future sibling report,
candidate, implementation, or ledger result was inspected. This report is the
sole path written by this audit.

## 1. Exact audit question

The pin is feasible only if it can preserve all of the following at once:

1. v2's point-valued Markov-kernel sample semantics;
2. a genuine category of boundary-tagged hybrid observable objects;
3. normal $W^*$ semantics for continuous record **ensembles**;
4. exact finite/atomic restart states;
5. refusal of generic nonatomic point restart;
6. representative-independent deterministic record maps;
7. full finite-path `Ev`/`Ens`/`Heis` compatibility;
8. exposure of all future-relevant memory; and
9. schedule equality only in the reachable certified-exchange domain.

The v3.1 pin does not obtain coherence by weakening a quantum probability. It
changes the false semantic identification that v3 made between an individual
nonatomic sample and a normal state on an equivalence-class algebra.

## 2. The `Ens` theorem is mathematically implementable

### 2.1 Canonical predual construction

Fix an integrated boundary and write

$$
\mathcal O_D
=\mathcal A_D\,\overline\otimes
L^\infty(R_D,\nu_D).
$$

Let $\Lambda\in\mathfrak E_D$, let
$\eta=(\pi_R)_*\Lambda$ be its record marginal, and use the pinned domination
$\eta\ll\nu_D$. Write

$$
h=\frac{d\eta}{d\nu_D}.
$$

Because the normal-state space and record space are standard Borel, a regular
conditional law $\kappa_r(d\rho)$ exists. Its conditional barycenter is

$$
\bar\rho_r
=\int \rho\,\kappa_r(d\rho)
\in(\mathcal A_D)_*.
$$

The pin requires a strongly measurable predual-valued posterior field. Under
that admission hypothesis,

$$
g(r)=h(r)\bar\rho_r
$$

is Bochner integrable and

$$
\int\lVert g(r)\rVert\,\nu_D(dr)
=\int h(r)\,\nu_D(dr)=1.
$$

For a represented von Neumann algebra with separable predual, this $L^1$
predual field defines the normal functional

$$
\Omega_\Lambda(F)
=\int\langle g(r),F(r)\rangle\,\nu_D(dr).
$$

Disintegrating $\Lambda$ shows that this is exactly the pinned formula

$$
\Omega_\Lambda(F)
=\int\rho(F(r))\,\Lambda(d\rho,dr)
=\operatorname{Ens}_D(\Lambda)(F).
$$

It is positive because each $\bar\rho_r$ is positive, normalized because
$F=1$ gives one, and normal because $g$ lies in the predual. The separable
predual hypothesis also supplies the countable approximation needed for joint
measurability of $(\rho,r)\mapsto\rho(F(r))$.

This proves feasibility. The construction must print this argument or an
equivalent predual theorem; the symbolic integral alone is not proof.

### 2.2 Representative independence

If $F_1=F_2$ in $\mathcal O_D$, then their decomposable representatives agree
$\nu_D$-almost everywhere. Since $\eta\ll\nu_D$, they also agree
$\eta$-almost everywhere. Hence

$$
\int\rho(F_1(r))\,d\Lambda
=\int\rho(F_2(r))\,d\Lambda.
$$

Thus the v3 constant-map/point-evaluation defect does not reappear inside
`Ens`. Marginal domination is used exactly where it is needed; it is not a
physical prior.

### 2.3 Point samples remain separate

For $\nu_D(\{r\})=0$, the Dirac law at $(\rho,r)$ is not in the dominated
ensemble class and point evaluation is not defined on $L^\infty(R_D,\nu_D)$.
The pin now refuses that restart. It does not deny that the `Ev` sample space
contains $r$, and it does not discretize the outcome.

For a finite or declared atomic $r$, the central singleton projection exists
and $\delta_{(\rho,r)}$ produces the exact normal state. The product can
therefore honestly carry both statuses:

```text
FINITE/ATOMIC-CONSTRUCTED
NONATOMIC-GENERIC-UNCONSTRUCTED
```

There is no contradiction between those coordinates.

### 2.4 Binding interpretation of a predictive value

The notation $(\rho,r)$ requires $\rho$ to determine a normal state on
$\mathcal A_D$. If a frozen v2 predictive object contains more information,
the construction must expose that information in the quantum algebra, a
record coordinate, or a typed predictive extension with a normal evaluation
map. An opaque process object cannot be inserted into the `Ens` integral by
renaming it $\rho$.

In a pure $C^*$ finite packet, “normal state” must be read as “admitted state,”
with normality required only in a represented $W^*$ packet. This is a typing
clarification, not a physical change.

## 3. One boundary, one domination class

The common-class rule is both necessary and feasible.

For finitely or countably many route probability measures $\eta_n$ reaching
one boundary, a strictly positive weighted sum

$$
\nu=\sum_{n\ge1}2^{-n}\eta_n
$$

dominates every route. For a fixed normal instrument, a faithful normal source
state can similarly generate a dominating outcome class. Neither construction
turns $\nu$ into the actual ensemble.

No common class is inferred for an arbitrary uncountable family. In
particular, a sigma-finite measure cannot dominate all
$\{\delta_x:x\in[0,1]\}$ because it would need uncountably many positive
atoms. Restriction, schema refinement, or an atomic/coarse interface is the
correct response.

The construction must additionally prove dynamic closure:

$$
\Lambda_D\in\mathfrak E_D
\Longrightarrow
\Lambda_D\operatorname{Ev}(p)\in\mathfrak E_E
$$

for every admitted path $p:D\to E$. Without this, the left side of the
integrated duality theorem may not lie in the domain of $\operatorname{Ens}_E$.
The pin requires primitive state-class closure; finite-path closure then
follows by induction.

A nonminimal dominating class may contain technically unused sectors. That
does not alter registered probabilities, but it is not equivalent to a
singularly smaller class. The chosen class must be frozen in the tagged
packet, and a later singular enlargement or reduction is a different object,
not gauge.

## 4. Deterministic record maps

For a deterministic map

$$
f:(R_D,[\nu_D])\longrightarrow(R_E,[\nu_E]),
$$

the formula

$$
f^*([g])=[g\circ f]
$$

is well defined exactly when

$$
f_*\nu_D\ll\nu_E.
$$

This condition is invariant under equivalent representatives and composes:
if $f_*\nu_D\ll\nu_E$ and $k_*\nu_E\ll\nu_F$, then
$(k\circ f)_*\nu_D\ll\nu_F$.

The pinned refusal of a constant map between Lebesgue classes is therefore
correct. A deterministic append $r\mapsto(r,a(r))$ can be admitted with a
target class containing the pushforward graph measure. If several routes
share that target schema, the one target class must dominate every route,
for example through a countable positive mixture when available. Blind use of
a nonatomic product class fails.

Discard is the inclusion of record-independent observables. Coarse-graining
is the nonsingular pullback from coarse to fine observables. Presentation and
packet isomorphisms require equivalence of transported classes, not only
one-way absolute continuity.

## 5. Finite and atomic complete instruments

For a finite outcome instrument,

$$
\widehat{\mathcal J}((A_s)_s)
=\sum_s\mathcal J_s(A_s)
$$

is CP because its matrix amplification is a sum of positive matrix maps. It
is unital exactly when $\sum_s\mathcal J_s(1)=1$. Branch insertion is generally
nonunital and is not a normalized hybrid arrow. Diagonal restriction gives
the nonselective operation and erases the result.

With an old retained record $r$, the exact map is fiberwise:

$$
(A_{r,s})_{r,s}
\longmapsto
\left(\sum_s\mathcal J_{r,s}(A_{r,s})\right)_r.
$$

It retains the old coordinate and appends the new result. Consequently the
binary result followed by the $I/X$ guard yields

$$
\mathcal J_0(A)+\mathcal J_1(XAX),
$$

the unchanged v2 branchwise law. Finite and countable atomic point states,
positive-support conditioning, guard composition, discard, and restart are
all implementable.

## 6. Tagged hybrid category and contravariant functor

### 6.1 Object and arrow typing

The tag

$$
\mathbf O_D=(B_{\Xi,D},\mathcal O_D,\mathsf{Reg}_D,[\nu_D])
$$

prevents equal underlying algebras from erasing different boundary schemas.
For clarity, the construction should print the hom convention

$$
(D,E,\Phi)\in
\operatorname{Hom}_{\mathbf{Hyb}_\Xi}(\mathbf O_E,\mathbf O_D),
\qquad
\Phi:\mathcal O_E\to\mathcal O_D.
$$

Then

$$
(D,E,\Phi)\circ(E,F,\Psi)
=(D,F,\Phi\circ\Psi)
$$

is ordinary typed composition from $\mathbf O_F$ to $\mathbf O_D$.
Identity, CP, unitality, normality in the $W^*$ regime, state-class
preservation, and nonsingularity are all stable under composition. A tag
mismatch is not composable.

This also handles explicit skip. Its underlying algebra map may be an
identity, but the triple has different tagged endpoints and is not a category
identity.

### 6.2 Heisenberg functor

For physical $p:D\to E$, the opposite-category arrow is represented by

$$
\operatorname{Heis}_\Xi(p):\mathbf O_E\to\mathbf O_D.
$$

Primitive reverse composition gives

$$
\operatorname{Heis}_\Xi(q\circ p)
=\operatorname{Heis}_\Xi(p)
\circ\operatorname{Heis}_\Xi(q),
$$

and the empty path gives the tagged identity. The pin has corrected the
missing identity display from v3. No partial composition predicate or later
physical admissibility test is needed after the tagged graph and arrow class
are fixed.

The category may contain finite $C^*$ packets and represented $W^*$ packets
as separately typed components. A cross-regime arrow is admitted only when
its exact algebraic source, target, and normality convention are declared.

## 7. Continuous instruments, guards, and complete memory

### 7.1 Complete continuous arrow

NEP is not treated as automatic. Each admitted continuous instrument owes one
normal UCP map on the exact hybrid algebras, a measurable `Ev` posterior
kernel, landing in the declared target algebra, common-class compatibility,
and closure of the ensemble/state class. An extension only into an ambient
$\mathcal B(\mathcal H)$ does not type the requested arrow. Approximate NEP
earns only an approximate result.

### 7.2 Decomposable guard

For a retained continuous record, a field
$r\mapsto\Phi_r$ defines the pointwise/decomposable action only after the
construction proves the appropriate weak or predual measurability, exact
common fibers/endpoints, essential boundedness, normal UCP behavior, and
ensemble closure. UCP fields have norm one, but measurability and target
closure are independent duties.

Two versions equal $\nu_D$-almost everywhere give the same integrated arrow.
They need not give the same response to an inadmissible Dirac restart. The pin
correctly refuses promotion of that null-set difference.

If branch-dependent controls change the output schema, a typed direct
sum/measurable field of schemas is required. One cannot call maps with
different endpoints a single decomposable arrow.

### 7.3 Complete-memory test

Suppose two laws induce the same normal `Ens` state but a licensed future
distinguishes them using a hidden bit. Then no UCP arrow out of
$\mathcal O_D$ can represent that future, and integrated duality fails. The
pin's response is exact: expose the bit as a quantum memory port or retained
classical coordinate, refine the boundary, or refuse the future.

For ordinary quantum instruments, different convex decompositions with the
same conditional barycenter are not future distinguishable by complete
linear quantum operations. The conditional barycenter plus retained record is
therefore sufficient once every additional process memory is exposed.

## 8. Full `Ev`/`Ens`/`Heis` composition

For a primitive $p:D\to E$, construction must establish the state equality

$$
\operatorname{Ens}_E(\Lambda_D\operatorname{Ev}(p))
=\operatorname{Ens}_D(\Lambda_D)
\circ\operatorname{Heis}(p)
$$

for every admitted $\Lambda_D$. Equality on one scalar outcome or a
tomography-incomplete reader family is insufficient.

Assume the identity for $p$ and $q$, and use ensemble closure. Then

$$
\begin{aligned}
\operatorname{Ens}_F(\Lambda_D\operatorname{Ev}(p)
                         \operatorname{Ev}(q))
&=\operatorname{Ens}_E(\Lambda_D\operatorname{Ev}(p))
  \circ\operatorname{Heis}(q)\\
&=\operatorname{Ens}_D(\Lambda_D)
  \circ\operatorname{Heis}(p)
  \circ\operatorname{Heis}(q).
\end{aligned}
$$

The Markov tower property and Heisenberg functor law give the theorem for
every finite path. This is an actual induction, not a test at several depths.

The construction must preserve two equality levels:

1. `Ev` uses the exact frozen kernel representatives inherited from v2; and
2. integrated predictions are invariant under allowed almost-everywhere
   changes of posterior/control versions.

An exchange certificate may compare the frozen `Ev` representatives exactly,
as the pin requires. If a candidate instead quotients kernels modulo a.e.
equality, it must define that quotient and prove composition congruence before
using it. No such quotient may be assumed silently.

## 9. Conditioning, coarse boundaries, and restart

A positive-measure central event $\Delta$ gives a normalized conditional
ensemble and normal hybrid state. A finite or atomic positive point gives an
exact branch state. A nonatomic singleton remains the zero projection in the
hybrid algebra and receives no normal restart state.

This does not say continuous feedback is impossible. It says feedback is one
integrated whole-program operation, while generic conditioning at an exact
zero-mass point is not a complete restart boundary. Record, conditioning,
division, and actuality remain four different predicates.

After discard, the source schema of a later guard lacks the record. After
coarse-graining, it lacks the fine coordinate. A hidden cache that restores
either value violates complete-memory exposure.

## 10. Presentation, quotient, covariance, and concurrency

### 10.1 Transport

A full presentation or packet isomorphism must transport the tagged boundary,
quantum algebra, central classical algebra, sample and ensemble classes,
measure-class null ideal, posterior/control fields, kernels, maps, source
lineage, and exact occurrence multiplicity. A continuous record bijection must
send one measure class equivalently to the other. Coordinate bijection alone
does not suffice.

Proper `Loc` embeddings still give observable transport and state pullback,
not canonical forward state extension or full experiment transport.

### 10.2 Operational congruence

Complete contexts include prefixes, ancillary probes, adaptive controls,
discard, coarse-graining, records, randomization, and readers. Equality in all
such contexts is stable under precomposition, postcomposition, and every
registered constructor. With both semantic layers and the exact admission
scope printed, the operational relation is a category congruence on the
reachable packet interface.

### 10.3 Certified schedules

An exchange square must compare complete `Heis` maps and complete `Ev`
kernels, with identical tagged endpoints, output permutation, source,
apparatus, memory lineage, and measure-class data. Equality on one state,
reader, or marginal is not a certificate.

Any two linear extensions of a finite poset are connected by adjacent swaps
of incomparable elements. All-linearization equality therefore follows only
when every co-enabled pair in every reachable record context is certified.
The pin states exactly this condition. An uncertified serialization remains an
exposed procedure distinction, not a hidden universal clock.

## 11. Physics and source boundary

The repair is representational. It leaves all v2 branch maps, POVMs,
scattering maps, kernels, state updates, source assumptions, and probabilities
unchanged. It narrows only what the continuous Heisenberg representation may
claim at a null point.

The source anchors support this scope: NEP is a substantive condition tied to
normal complete extensions and measurable posterior families; localized
system--probe maps compose under named causal-factorization hypotheses; and
finite direct-sum classical--quantum channels are standard. None of those
results supplies a point posterior on every null singleton, a physical
reference prior, a selected outcome, or an ontology.

The laboratory slot poset remains declared protocol on a declared relativistic
comparator. No microscopic event web, time, spacetime, or gravity is inferred.

## 12. Target-theorem dispositions

These are pin-feasibility dispositions, not constructed results.

| Target | Audit disposition | Binding construction burden |
|---|---|---|
| V31-T1 | `FEASIBLE-INHERITED` | reproduce the exact v2 frontier/path category |
| V31-T2 | `FEASIBLE` | one fully tagged object per complete boundary schema |
| V31-T3 | `ALGEBRAICALLY-FEASIBLE` | prove CP/unitality of the direct-sum arrow |
| V31-T4 | `FEASIBLE-FINITE / CONDITIONAL-ATOMIC` | exact point state only at declared atoms |
| V31-T5 | `FEASIBLE-CONDITIONAL` | common class, predual field, representative-independent normal `Ens` |
| V31-T6 | `CORRECT-REFUSAL` | print generic nonatomic point restart unconstructed |
| V31-T7 | `FEASIBLE-CONDITIONAL` | prove every deterministic pullback nonsingular |
| V31-T8 | `FEASIBLE-CONDITIONAL` | exact NEP/equivalent landing map, posterior, and class closure |
| V31-T9 | `FEASIBLE` | define tagged hom-sets, identities, and total matched composition |
| V31-T10 | `FEASIBLE` | prove contravariant object/arrow assignment and both functor laws |
| V31-T11 | `FEASIBLE-CONDITIONAL` | one-step all-reader identity, ensemble closure, finite-path induction |
| V31-T12 | `FEASIBLE-CONDITIONAL` | measurable decomposable normal UCP guard field |
| V31-T13 | `FEASIBLE` | discard/coarse schemas make removed reads untyped |
| V31-T14 | `FEASIBLE` | positive event conditioning; null point refusal |
| V31-T15 | `FEASIBLE-CONDITIONAL` | move tags, classes, fields, maps, kernels, and multiplicity |
| V31-T16 | `FEASIBLE-SCOPED` | constructor-complete contexts and both semantic layers |
| V31-T17 | `FEASIBLE-CONDITIONAL` | full map/kernel certificate with all lineage |
| V31-T18 | `FEASIBLE-CONDITIONAL` | certify every reachable co-enabled context |
| V31-T19 | `FEASIBLE-INHERITED` | preserve exact v2 no-signalling/steering/Bell quantifiers |
| V31-T20 | `FEASIBLE-INHERITED` | preserve v2 normalized history kernels and prefixes |
| V31-T21 | `COHERENT-REFUSAL/CONDITIONAL` | retain frame and operator-algebra firewalls |
| V31-T22 | `COHERENT-REFUSAL` | keep record, conditioning, division, actuality distinct |
| V31-T23 | `COHERENT-INCOMPLETENESS` | no selected configuration/law/state/trajectory imported |
| V31-T24 | `CORRECTLY-UNCONSTRUCTED` | no ontology, internal time, spacetime, or gravity claim |

No target requires a new physical parameter. T5, T7, T8, T11, T12, T15,
T17, and T18 are conditional theorem obligations, not universal existence
claims.

## 13. Two-way control dispositions

| Control | Audit disposition | Exact reason |
|---|---|---|
| C1 | `COHERENT` | finite records are central direct-sum atoms; branch list is not an arrow |
| C2 | `COHERENT-POSITIVE` | complete binary arrow followed by block $I/X$ gives branchwise law |
| C3 | `COHERENT` | complete sum is unital; branch insertion generally is not |
| C4 | `COHERENT` | atomic point is normal; nonatomic evaluation is refused |
| C5 | `COHERENT` | dominated law yields `Ens`; nonatomic Dirac is outside the class |
| C6 | `COHERENT` | posterior/control versions are a.e.; null singleton is not canonical |
| C7 | `COHERENT-CONDITIONAL` | one boundary class must dominate all routes |
| C8 | `COHERENT` | nonsingularity is necessary and sufficient for the pullback |
| C9 | `COHERENT-CONDITIONAL` | graph-compatible append class required; blind product refused |
| C10 | `COHERENT` | equivalent classes give same null ideal; singular class changes object |
| C11 | `COHERENT` | faithful state is a domination tool only |
| C12 | `COHERENT` | boundary tag distinguishes skip from empty path |
| C13 | `COHERENT` | guard source contains past record; future record is absent |
| C14 | `COHERENT-CONDITIONAL` | decomposable guard owes measurability, normality, endpoints, closure |
| C15 | `COHERENT-OBLIGATION` | every future-readable memory must be exposed |
| C16 | `COHERENT` | discard target omits the coordinate, so later read is untyped |
| C17 | `COHERENT` | positive coarse event conditions; null point does not |
| C18 | `COHERENT-OBLIGATION` | equality is an evaluated quantum-state integral for every reader |
| C19 | `COHERENT` | full maps/kernels required; one scalar is insufficient |
| C20 | `COHERENT` | all reachable swaps, not one initial square, are required |
| C21 | `COHERENT` | exact record permutation is certificate data |
| C22 | `COHERENT` | product source exposed; correlation is a joint mechanism |
| C23 | `COHERENT` | presentation moves null ideal and retains occurrence multiplicity |
| C24 | `COHERENT` | full isomorphism moves both layers; proper state push is refused |
| C25 | `COHERENT-INHERITED` | complete nonselective map no-signals; selected branch may steer |
| C26 | `COHERENT-INHERITED` | KMS/material frame is physical state data, not covariance failure |
| C27 | `COHERENT-REFUSAL` | type-III scope uses normal functionals, not generic density matrices |
| C28 | `COHERENT-CONDITIONAL` | split factorization needs collar and named hypothesis |
| C29 | `COHERENT` | record exists only while typed interface carries it |
| C30 | `COHERENT-REFUSAL` | future sufficiency, not frontier/sample alone, earns division |
| C31 | `COHERENT-REFUSAL` | predictive law does not select an outcome |
| C32 | `COHERENT-REFUSAL` | finite slots are laboratory protocol, not microscopic time |
| C33 | `COHERENT-REFUSAL` | comparator spacetime is declared, not emergent |
| C34 | `COHERENT-FROZEN` | all v2 probabilities and physical inputs remain unchanged |

All 34 controls have a mathematically available positive construction or an
exact refusal. None is made true by a lookup table or implementation.

## 14. Fresh hostile countermodels

These attacks are additional to the pin's mandatory 52.

### A1 — Dominated marginal, altered observable representative

Choose $F=G$ $\nu$-a.e. but different on a null set carrying many point
samples. **Required result:** `Ens(F)=Ens(G)` because the record marginal is
absolutely continuous. Pointwise `Ev` may retain the chosen samples but gains
no normal restart state. **Disposition:** pass.

### A2 — Scalar posterior density without a predual barycenter

Supply $h=d\eta/d\nu$ but no strongly measurable normal-state field.
**Required result:** fail integrated packet admission; scalar domination alone
does not define a normal hybrid state. **Disposition:** pass by refusal.

### A3 — Weakly named “state” with future nonlinear cache

Let two predictive values induce the same normal quantum state and record but
let a later licensed primitive read a hidden cache. **Required result:** expose
the cache or refuse the future; `Ens` is otherwise not sufficient.
**Disposition:** pass by complete-memory gate.

### A4 — Output law leaves the next ensemble class

Make a one-step identity hold but choose $\Lambda_D\operatorname{Ev}(p)$
outside $\mathfrak E_E$. **Required result:** no path theorem; primitive and
path closure are mandatory. **Disposition:** pass by admission.

### A5 — Nonminimal technical class gains an unused atom

Replace $[\nu]$ by the singularly larger class of $\nu+\delta_{r_0}$ while
all registered laws ignore $r_0$. **Required result:** predictions may agree,
but the tagged object has changed; this is not equivalent-measure gauge.
**Disposition:** pass.

### A6 — Two nonsingular maps whose composite is claimed singular

Take $f_*\nu_D\ll\nu_E$ and $k_*\nu_E\ll\nu_F$. **Required result:** the
composite is automatically nonsingular by transitivity, so category closure
cannot be defeated this way. **Disposition:** pass positive control.

### A7 — Record append shares a schema with a disjoint graph

Two deterministic routes land on disjoint graphs in one target record space.
**Required result:** use one class dominating both graph pushforwards or split
the boundary schema; an instrument-specific class is insufficient.
**Disposition:** pass conditionally.

### A8 — Mixed atomic/nonatomic outcome

Use $\nu=a\delta_{r_0}+(1-a)\lambda$. **Required result:** exact point restart
is normal at $r_0$ and generically refused on the nonatomic component. One
record space may support both statuses only when the atom is declared.
**Disposition:** pass.

### A9 — UCP guard field with nonmeasurable matrix coefficient

Choose normal UCP maps $\Phi_r$ pointwise but make
$r\mapsto\omega(\Phi_r(A))$ nonmeasurable for some normal $\omega,A$.
**Required result:** no decomposable arrow; pointwise UCP is insufficient.
**Disposition:** pass by refusal.

### A10 — Same complete map, different tagged endpoint

Let explicit skip and identity have literally equal underlying CP maps.
**Required result:** their triples remain different because source/target tags
differ; skip consumes the slot. **Disposition:** pass.

### A11 — One-reader duality with a nonseparating reader

Match the two semantics on the identity and all classical effects but disagree
on one quantum observable. **Required result:** V31-T11 fails; equality is for
every complete hybrid reader. **Disposition:** pass by theorem burden.

### A12 — A.e.-equal controls used as exact exchange evidence

Make two guards differ on a $\nu$-null set and claim exact equality of frozen
`Ev` kernels. **Required result:** either compare the fixed representatives
exactly or construct an a.e. kernel quotient and prove congruence; integrated
equality alone is not the printed exact certificate. **Disposition:** pass by
certificate scope.

### A13 — Reachable adaptive context omitted from certification

Two operations commute initially but a prior record changes one guard so the
later pair does not. **Required result:** the protocol is not fully certified;
all-linearization equality is unavailable. **Disposition:** pass.

### A14 — Coarse result plus hidden fine-memory revival

Coarse-grain $r$ to $c(r)$, then make a later operation depend on the old
$r$. **Required result:** untyped unless the fine value remained in an exposed
memory port, in which case it was not discarded. **Disposition:** pass.

### A15 — Ambient NEP extension mistaken for target landing

Supply a normal extension into $\mathcal B(\mathcal H)$ that does not preserve
the declared local algebra. **Required result:** the instrument is outside the
hybrid theorem. **Disposition:** pass by exact landing condition.

### A16 — Conditioning on a null point after positive coarse conditioning

First condition on a positive interval, then select one singleton inside it.
**Required result:** the interval conditional is normal; the singleton remains
null unless it is an atom in the conditional class. **Disposition:** pass.

All sixteen fresh attacks have a pin-consistent theorem or refusal. None
uncovers a semantic blocker or licenses probability retuning.

## 15. Mandatory-attack package feasibility

The pin's 52 attacks are mutually compatible and finite. Their decisive
groups have the following audit disposition:

| Mandatory range | Subject | Feasibility disposition |
|---:|---|---|
| 1–5 | nonatomic failure, positive event, atomic restart | exact two-layer controls supplied |
| 6–10 | common class, pullback, append, measure equivalence, technical state | exact domination/nonsingularity refusals supplied |
| 11–16 | NEP, landing, posterior, memory, quantum field | conditional admissions are coherent |
| 17–21 | finite guard, branch/nonselection, old fiber, skip | direct-sum/tagged construction is exact |
| 22–27 | schemas, future guard, discard, coarse read, a.e. versions | source/target and integrated scope block each attack |
| 28–32 | evaluated integral, all-reader duality, presentation, transport | exact construction obligations are stated |
| 33–38 | certificates, permutations, sources, adaptive contexts | reachable full-certificate quantifier is sufficient |
| 39–44 | signalling, Bell, type III, split, frame | inherited scoped refusals remain consistent |
| 45–52 | record/division/actuality/ontology/downstream/retuning | all promotions remain expressly closed |

No attack requires code or an unbounded lookup. General claims are structural;
model-specific existence remains conditional.

## 16. Full product feasibility audit

This table records what the pin permits a future construction to attempt. It
does not record a scientific result.

| Coordinate | Pin-audit disposition | Exact scope |
|---|---|---|
| input | `BOUND/COHERENT` | exact authority corpus and v2 physics |
| slot-skeleton | `INHERITED` | finite laboratory protocol only |
| frontier | `INHERITED` | lower-set type, not division |
| boundary | `FEASIBLE-TAGGED-TYPE` | complete ports, records, memory, regime |
| sample-semantics | `INHERITED` | exact point-valued v2 `Ev` kernels |
| ensemble-semantics | `FEASIBLE-CONDITIONAL` | dominated laws and predual fields |
| hybrid-object | `FEASIBLE` | finite exact; integrated conditional |
| heisenberg-functor | `FEASIBLE` | tagged opposite-category functor |
| integrated-compatibility | `FEASIBLE-CONDITIONAL` | every admitted law/path/reader |
| point-restart | `FINITE/ATOMIC-FEASIBLE; NONATOMIC-REFUSED` | no generic Dirac restart |
| presentation | `FEASIBLE` | tags, null ideals, fields, multiplicity transported |
| quotient | `FEASIBLE-SCOPED` | constructor-complete reachable contexts |
| covariance | `FEASIBLE-CONDITIONAL` | full packet isomorphism only |
| state-class | `CONDITIONAL-ADMISSION` | normal/predual and dynamic closure |
| instrument | `FINITE-FEASIBLE; CONTINUOUS-CONDITIONAL` | complete arrow, NEP/landing/posterior |
| causal-factorization | `INHERITED-CONDITIONAL` | complete localized maps and sources |
| certified-schedule | `FEASIBLE-CONDITIONAL` | every reachable co-enabled context |
| no-signalling | `INHERITED-SCOPED` | complete nonselective operation |
| steering | `INHERITED-SCOPED` | selected conditional plus record cost |
| bell | `INHERITED-COMPATIBILITY` | no universal exact probe realization |
| positive-model | `INHERITED` | normalized predictive histories, unselected |
| context | `FEASIBLE-SCOPED` | all registered constructors included |
| fibers | `INHERITED-SCOPED` | no physical prior/selector added |
| type-III | `REFUSAL/MODEL-SPECIFIC` | normal functionals/maps only |
| split | `CONDITIONAL-CONTROL` | collar and named split hypothesis |
| gauge | `TYPED-UNSELECTED` | no factorization or sector derivation |
| particles | `TYPED-UNSELECTED` | no universal Fock ontology |
| continuum | `ABSTRACT-COMPARATOR-CONDITIONAL` | no interacting model derived |
| UV | `SCOPED-REFUSAL` | no cutoff removal theorem imported |
| preferred-frame | `SCOPED` | physical KMS/material frames allowed |
| record | `FEASIBLE-OPERATIONAL` | point sample separate from ensemble state |
| division | `UNCONSTRUCTED/TEST-REQUIRED` | future sufficiency independent |
| actuality | `UNCONSTRUCTED` | no selected branch or history |
| barandes | `COMPATIBLE-BUT-INCOMPLETE` | no universal configuration/law/trajectory |
| ontology | `UNCONSTRUCTED` | hybrid algebra is predictive representation |
| downstream | `CLOSED` | no Paper 04, time, spacetime, or gravity |

## 17. Outcome ladder and binding construction scope

No rung is awarded by a pin audit. If construction meets every obligation,
the strongest pin-permitted outcome remains rung 8:

```text
P03V31-RELATIVISTIC-QUANTUM-OPERATIONAL-ADEQUACY-WITH-GLOBAL-ONTOLOGY-DEBT
```

The construction must fail at the earliest applicable lower rung if common
domination, hybrid category closure, functoriality, integrated compatibility,
or certified concurrency is not proved. Admission language cannot be used to
declare a missing proof true.

This acceptance is binding on the following points:

1. construct `Ens` through an explicit $L^1(R,\nu;(\mathcal A_D)_*)$
   predual field and prove representative independence and normality;
2. require each predictive quantum value to have the printed normal-state
   evaluation used in that field;
3. freeze one common class per integrated boundary and prove path closure of
   every $\mathfrak E_D$;
4. prove nonsingularity for every deterministic record pullback and class
   equivalence for isomorphisms;
5. keep finite/atomic point restart exact and print generic nonatomic restart
   unconstructed;
6. define tagged hom-sets and the contravariant composition convention
   explicitly;
7. construct every complete instrument on its exact source/target algebra,
   with old record fibers retained;
8. prove continuous guards as measurable decomposable normal UCP arrows;
9. expose every future-relevant quantum and classical memory coordinate;
10. prove one-step all-reader duality, ensemble closure, and the finite-path
    induction;
11. distinguish exact frozen `Ev` representatives from integrated a.e.
    equivalence;
12. transport sample, ensemble, null-ideal, map, kernel, field, and
    multiplicity data together;
13. certify exchanges in every reachable adaptive context with complete
    maps, kernels, outputs, sources, and memory; and
14. preserve every v2 probability and every actuality, ontology, spacetime,
    and gravity refusal.

## 18. Final verdict

**ACCEPT-FOR-CONSTRUCTION-WITH-BINDING-SCOPE.**

The corrected pin is internally coherent and implementable. Absolute
continuity makes `Ens` representative independent; the strongly measurable
predual barycenter makes it normal; tagged objects make skip and boundary
schemas exact; nonsingular pullbacks compose; finite/atomic restart remains
literal; continuous guards compose at a.e. ensemble scope; and one-step
duality plus the tower property extends to every finite path. Certified
concurrency has the correct reachable-context quantifier.

The first exact blocker is **none**. The highest-risk construction failures
are incomplete memory exposure, omission of ensemble-class closure, an
ill-defined continuous decomposable field, or accidental replacement of
exact `Ev` equality by unproved a.e. kernel equivalence. Each is already a
named gate, not a license to edit the pin.

One self-contained mathematics-only construction may begin on a new path.
There is no implementation stage and no automatic v3.2. Paper 04, internal
time, spacetime, and gravity remain closed until terminal v3.1 adjudication.

## 19. Report authentication

Report line count: `000827`

Report byte count: `037425`

Normalized self-SHA-256: `f11526ff46ec10ecfb588c00c1e97085580c45bdcc2da5140a09f9ca6e5a29ec`

Normalization rule: replace the 64 hexadecimal characters on the preceding
line by 64 ASCII zeroes, preserve every other byte, and compute SHA-256. The
report ends in one LF and contains no trailing horizontal whitespace.
