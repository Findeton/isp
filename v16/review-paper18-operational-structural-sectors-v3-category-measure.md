# Paper 18 version-3 composite hostile review — Seat M

Date: 2026-08-21

Seat: category and measure

Verdict: **REVISE**

## 1. Authentication, composite scope, and blindness

I authenticated and read every frozen composite component completely before
reviewing it.

| role | ordinary SHA-256 | size | result |
|---|---|---:|---|
| complete version-2 base | `b9dbcbd40e4f2e2eb1b18c4b5e98ba4d33eb491a5af791e9106369a53c51e614` | 1,165 LF / 41,256 bytes | exact match |
| binding version-3 amendment | `496942b2a742ee2fe81561790e185aba6a3fcc865630c23ca278c3067c80f6dd` | 318 LF / 10,598 bytes | exact match |
| version-3 construction note | `71d3bef893d772aff8c102915a570ffee76d4bbab15e48a47219bbef3de7876b` | 76 LF / 2,828 bytes | exact match |
| version-3 hostile-review protocol | `cece6b5e44c1d3f5bdebe650d1723a03f828e5a107610bbacf9a24416852f910` | 137 LF / 6,250 bytes | exact match |
| version-2 adjudication | `172f8fa73d3f3d06703c6128bb53ccf28f11936d8210a8e1a3603a9566f8468b` | 79 LF / 2,944 bytes | exact match |

I applied the amendment only to its expressly named replacement clauses; all
other version-2 text remained literal. For the accepted-law specialization I
also reauthenticated the Paper 13D law and terminal adjudication at
`3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9`
and
`ae2c4ef066335c39a0b8057c897c947b06e4270be67d1ed3ec59bf8d6d0a00c9`,
and consulted only their exact simultaneous-fusion result.

This review uses no implementation, code-based proof, parameter fit, Paper
17 output, chronology, dimension, geometry, gravity, or repair. I wrote only
this assigned report and left it unstaged and uncommitted.

I remained blind to all version-3 sibling reports and reviewers. I did not
inspect, list, contact, summarize, or infer any of them. The authorized
version-2 adjudication was used only as part of the frozen composite corpus.

## 2. First decisive issue

The amendment defines a finite measure \(\mu_{a,b}\) separately on each
resolved channel class space and requires each fiber target map
\(\tau_{a,b}\) to be measurable. It does **not** construct:

1. a measurable total resolved-channel space or measurable field of class
   spaces over \(\mathsf S\times\mathsf S\);
2. a joint measurable target map on that total space; or
3. an input-measurable resolved kernel
   \((a,b)\mapsto\mu_{a,b}\).

Fiberwise measurability does not imply any of these. Consequently equation
(V3.1) need not be a measurable target kernel, and—even if its pushforward is
separately assumed to satisfy inherited Definition 13—equation (V3.3) need
not be a measurable resolved Markov kernel. The proof of Replacement Theorem
3 invokes “the resolved kernel,” but no such kernel is among its hypotheses
or in Definition 10A.

This is a failed theorem-level typing claim, hence at least `REVISE` under the
frozen protocol. It is bounded rather than central rejection: normalization
and pushforward are correct for each fixed input, the target-level theorems
survive when \(\mathsf M\) is independently a measurable convolution, and no
current physical law coordinate was promoted.

## 3. First decisive semantic counterexample

Let the sector space be \(\mathsf S=\mathbb R_{\geq0}\) with its Borel sigma
algebra and additive unit 0. For every \(a,b>0\), let the resolved channel
groupoid be the discrete two-object groupoid

\[
 \mathsf{Ch}(a,b)=\{\kappa^0_{a,b},\kappa^1_{a,b}\},
\]

with both objects targeting \(a+b\). Unit pairs have the ordinary single
unit channel. Let \(V\subset(0,\infty)\) be non-Borel and define

\[
 \mu_{a,b}=
 \begin{cases}
  \frac13\delta_{\kappa^0_{a,b}}
   +\frac23\delta_{\kappa^1_{a,b}},&a\in V,\\[2mm]
  \frac23\delta_{\kappa^0_{a,b}}
   +\frac13\delta_{\kappa^1_{a,b}},&a\notin V,
 \end{cases}
\]

for \(a,b>0\). Every individual class space is finite discrete, every
\(\mu_{a,b}\) is finite, nonzero, invariant, and gives both inequivalent
same-target channels positive mass, and every fiber map \(\tau_{a,b}\) is
measurable.

Nevertheless the target pushforward is the perfectly measurable associative
convolution

\[
 \mathsf M_{a,b}=\delta_{a+b}.
\]

It has unit, finite words, and positive character \(d=1\), so the target law
is deterministic addition. Formula (V3.3), however, returns the displayed
resolved split. For any fixed \(b>0\), the probability of the physically
declared channel family “channel 0” is \(1/3\) on \(V\) and \(2/3\) off
\(V\), hence is not Borel measurable in \(a\).

Thus even granting a valid target convolution does not make the resolved
law a Markov kernel. If the total channel event distinguishing channel 0 is
not declared measurable, then the purported physical distinction cannot be
queried globally and the resolved kernel is not typed at all. Either way,
the literal hypotheses do not prove the measurability asserted after
(V3.4).

## 4. Seat-M duties

### M1 — complete profile and sector groupoids

**Pass.** The version-2 profile arrows remain total invertible typed functors
with total measurable natural outcome isomorphisms. Identities, specified
inverses, and composites preserve every experiment, intervention, reader,
physical incidence, tensor, composition, and presentation action. Their
componentwise composition proves the profile groupoid. Compatible pairs of a
presentation isomorphism and its induced profile isomorphism similarly form
\(\mathsf{Sect}(B)\). Taking its isomorphism classes removes presentation
but retains the literal physical-structure coordinate.

The amendment does not weaken any of these definitions.

### M2 — marked restriction, descent, and deletion separation

**Pass.** \(\mathsf{Bnd}\) still has literal marked inclusions, componentwise
equality, identities, and associative embedding composition. Pullback is
contravariant on sector objects and arrows, obeys identity and composition,
and is presentation equivariant. The version-3 scope now makes the global
object literally the pseudo-limit/descent groupoid: objects carry coherent
restriction isomorphisms satisfying the cocycle, and arrows are compatible
families of component arrows.

Uniform unmarked deletion remains a separately typed Markov kernel. It
cannot choose an exact marked subobject, while marked pullback cannot supply
deletion probabilities.

### M3 — resolved class spaces, sigma algebras, and target maps

**Fail globally; pass fiberwise.** For a fixed \((a,b)\), the invariant
isomorphism-class space and its declared sigma algebra type an invariant
finite measure, and a groupoid-invariant measurable \(\tau_{a,b}\) descends
to that quotient. A nonsmooth or coarse quotient may fail to separate all
inequivalent objects measurably; version 3 correctly then proves only
set-level plurality, not positive measure-supported branching.

What is absent is a measurable bundle

\[
 p:\mathcal C\longrightarrow\mathsf S\times\mathsf S
\]

whose fiber is the resolved class space, together with joint measurable
\(\tau:\mathcal C\to\mathsf S\) and a kernel supported on the fibers. The
separate phrase “smallest declared sigma algebra” does not supply measurable
dependence on the input pair. The counterexample in Section 3 exploits
exactly this gap.

### M4 — target pushforward (V3.1)

**Finite measure for each pair: pass. Measurable kernel: not proved.** For
fixed \((a,b)\), pushforward gives a countably additive measure and

\[
 \mathsf M_{a,b}(\mathsf S)
 =\mu_{a,b}(\mathsf{Ch}(a,b))\in(0,\infty).
\]

But a kernel also requires
\((a,b)\mapsto\mu_{a,b}(\tau_{a,b}^{-1}A)\) to be measurable for every
measurable target set \(A\). Neither fiberwise measurability of \(\tau_{a,b}\)
nor pairwise finiteness of \(\mu_{a,b}\) implies this. The inherited
Definition-13 requirement can be imposed separately on \(\mathsf M\), as in
Section 3, but it still does not make \(\mu\) a resolved kernel.

### M5 — channel plurality without target plurality

**Pass.** The replacement definition correctly makes inequivalent resolved
physical channel objects primary. It does not require their target classes
to differ. Plurality is set-level. Measure-supported branching separately
requires two disjoint invariant measurable channel families of positive
\(\mu\)-mass. A common target can therefore support nontrivial resolved
branching and a deterministic target pushforward.

This also avoids the converse error: two labels, bases, or child history
values do not become channels unless retained physical incidence, trace, or
other exact selector-level data distinguish them.

### M6 — resolved normalization and target pushforward

**Pass per input pair; fail only in the global measurability claim.** For a
fixed pair,

\[
 \int \mathsf P^{\rm res}_{a,b}(d\kappa)
 =\frac{1}{d(a)d(b)}
   \int d(\tau\kappa)\mu_{a,b}(d\kappa)
 =1
\]

by (V3.1) and (V3.2). For every measurable target set \(A\),

\[
 \begin{aligned}
 (\tau_*\mathsf P^{\rm res}_{a,b})(A)
 &=\frac1{d(a)d(b)}
   \int_{\tau^{-1}A}d(\tau\kappa)\mu_{a,b}(d\kappa)\\
 &=\frac1{d(a)d(b)}\int_A d(c)\mathsf M_{a,b}(dc)
 =\mathsf P^{\rm tgt}_{a,b}(A).
 \end{aligned}
\]

Hence both fixed-input measures normalize and the pushforward identity is
exact. These calculations do not establish input measurability of the
resolved family; Section 3 shows that the missing conclusion can fail while
all displayed equalities hold.

### M7 — resolved and target gauge invariance

**Pass algebraically, conditional on well-typed kernels and finiteness.** The
pushforward of \(\mu^h\) is

\[
 \mathsf M^h_{a,b}(dc)
 =\frac{h(a)h(b)}{h(c)}\mathsf M_{a,b}(dc).
\]

Then

\[
 \frac{d^h(\tau\kappa)}{d^h(a)d^h(b)}\mu^h_{a,b}(d\kappa)
 =\frac{d(\tau\kappa)}{d(a)d(b)}\mu_{a,b}(d\kappa),
\]

and pushing forward gives identical target laws. The inherited transformed
finite-word condition prevents divergent target iterates. This identity
cannot cure a nonmeasurable input family: multiplying the Section-3 split by
a measurable target-dependent factor leaves its nonmeasurable within-target
ratio.

### M8 — required same-target based ring

**Pass.** With basis \(\{\mathbf1,a\}\), the target multiplication is

\[
 \mathbf1x=x\mathbf1=x,
 \qquad a^2=2a.
\]

It is associative. Every word of \(n\geq1\) copies of \(a\) has target raw
measure

\[
 2^{n-1}\delta_a,
\]

independently of bracketing, so all finite words are finite. The positive
character equations give \(d(\mathbf1)=1\) and
\(d(a)^2=2d(a)\), hence the unique positive value \(d(a)=2\). Resolved
counting assigns each of the two inequivalent channels probability \(1/2\),
and target pushforward assigns \(a\) probability one.

The control is a positive based ring/semiring control; it is not being
silently promoted to a rigid fusion category with duals.

### M9 — marginal versus resolved path coherence

**Pass.** The amendment restricts inherited finite-word closure to target
pushforwards and explicitly requires a separate resolved composition
category, measures, associators, and pentagon if channel paths are physical.

A fresh attack takes deterministic addition on \(\mathbb Z/4\) as the target
marginal, retains a path automorphism group
\(C_4=\langle g\rangle\), and assigns

\[
 \alpha(1,1,1)=g,
 \qquad \alpha(x,y,z)=1\ \text{otherwise}.
\]

For the quadruple \((1,1,1,1)\), the two pentagon products are \(g^2\) and
1. The target convolution remains associative while resolved path coherence
fails. Version 3 rejects the promotion exactly where it should.

### M10 — continuous positive-measure channel families

**Pass.** Let \(\mathsf S=\{\mathbf1,a\}\) with idempotent target product
\(a^2=a\). Let the resolved channels over \((a,a)\) be \([0,1]\), all with
target \(a\), and take Lebesgue measure. Then

\[
 \mathsf M_{a,a}=\delta_a,
 \qquad d(a)=1,
 \qquad \mathsf P^{\rm res}_{a,a}=\mathrm{Leb}_{[0,1]},
 \qquad \mathsf P^{\rm tgt}_{a,a}=\delta_a.
\]

Every individual resolved channel has zero mass, yet
\([0,1/2)\) and \([1/2,1]\) are disjoint invariant measurable families of
positive mass. The replacement definition uses positive-measure families,
not positive singleton probabilities, and therefore passes.

### M11 — automorphisms, measures, roots, and multiplicities

**Pass as provenance distinctions; physical choice remains open.** Take two
inequivalent same-target groupoid objects \(\kappa_0,\kappa_1\) with
automorphism groups of orders 2 and 6. Equal-orbit counting assigns weights
\((1,1)\); finite-groupoid cardinality assigns \((1/2,1/6)\). The latter has
target mass \(2/3\), positive character \(d(a)=2/3\) for the one-target
idempotent convolution, and resolved probabilities \((3/4,1/4)\). Equal
orbit counting instead gives target mass and character 2 and resolved
probabilities \((1/2,1/2)\).

Neither convention follows from point-freeness. Rooting can reduce an
automorphism stabilizer, and \(m\) identical spectators contribute a wreath
factor \(|\operatorname{Aut}X|^m m!\). Version 2 Definition 14, retained by
the amendment, keeps resolved counting, orbit weighting, groupoid
cardinality, and preparation pushforward as different provenances. No
physical measure or spectator-cancellation theorem is claimed.

### M12 — affected version-2 regressions

All amendment-affected category/measure regressions were rerun. The detailed
matrix is in Section 6. The literalized pseudo-limit, indexed-history, and
completion-axis scopes pass. History/channel separation, finite-word target
closure, positive-character normalization, gauge invariance, the
representation no-go, automorphism controls, and the positive controls all
survive. The new input-measurability regression fails for the reason in
Sections 2–4.

### M13 — resolved and target coordinates

**Pass at their conservative declared level.** Resolved and target laws are
logically independent:

- a primitive measurable target kernel may exist without resolved \(\mu\);
- multiple resolved laws can have one target pushforward;
- resolved and target families can both remain unconstructed; and
- uniqueness at one level need not imply uniqueness of a lift at the other.

The three values `UNCONSTRUCTED`, `FAMILY-CONSTRUCTED`, and
`UNIQUE-...-DERIVED` are exhaustive if “family” includes any constructed
non-derived family, including a singleton primitive postulate. A proven
nonexistence or nonnormalizability is already carried by the positive
character coordinate and leaves the corresponding law unconstructed. Under
that standard set-theoretic reading, no extra current coordinate is needed.

### M14 — contracts versus physical constructions

The version-2 profile, sector, restriction, descent, completion-axis, and
target convolution definitions remain mathematical contracts. Version 3
adds a correct fixed-input resolved/target disintegration contract but lacks
the measurable-bundle condition needed for a resolved kernel theorem.

No bounded physical sector census, resolved channel measure, channel
composition, positive character, resolved law, target law, or whole selector
has been extracted from Paper 13D. The same-target and continuous examples
are controls only. They select no physical branch.

### M15 — fresh countermodels

At least four fresh countermodels were required. Sections 3, 5, and 6 use
seven; they are collected in Section 5 for auditability.

## 5. Fresh semantic countermodels and controls

| ID | construction | result |
|---|---|---|
| CM1 | Non-Borel same-target two-channel split over deterministic addition, Section 3 | Required same-target example and decisive failure: target kernel is measurable, resolved law is not. |
| CM2 | Single fiberwise-measurable channel whose target is selected by a nonmeasurable input set | Shows pairwise target-map measurability alone does not make (V3.1) a target kernel. |
| CM3 | Three same-target channels of raw weights \(1,2,3\), giving \(\mathsf M_{a,a}=6\delta_a\) | Valid finite same-target branching: \(d(a)=6\), resolved probabilities \((1/6,1/3,1/2)\), deterministic target. |
| CM4 | Lebesgue continuum of same-target channels, Section M10 | Individual channels have zero mass while two invariant families have positive mass. |
| CM5 | Same-target objects with automorphism orders 2 and 6, Section M11 | Orbit and groupoid measures give different resolved laws and must not be swapped. |
| CM6 | Deterministic \(\mathbb Z/4\) target with non-cocycle \(C_4\)-valued associator, Section M9 | Target marginals associate; resolved pentagon fails. |
| CM7 | On \(\{\mathbf1\}\sqcup\mathbb N\), use \(\nu(n)=2^{-n}\), \(f(n)=2^n/n\), and \(\mathsf M_{a,b}=f(a)f(b)\nu\) for nonunits | Every pair is finite, but \(\int f\,d\nu=\sum 1/n=\infty\); inherited finite-word closure rejects it. |

For CM2, one may take input parameter \(x\in[0,1]\), a singleton channel
fiber, a discrete target \(\{0,1\}\), and
\(\tau_x=\mathbf1_V(x)\) for a non-Borel \(V\). Each singleton map is
measurable, while the pushed-forward mass of \(\{1\}\) is
\(\mathbf1_V(x)\). This isolates the target-kernel half of the same missing
joint-measurability condition.

CM3 is associative at target level because \(a^2=6a\), so a word of \(n\)
copies of \(a\) has raw measure \(6^{n-1}\delta_a\). Its positive character
is \(d(a)=6\), and its weighted resolved masses normalize exactly as stated.

## 6. Composite regression matrix

### Version-2 hostile controls affected by the amendment

| control | result | composite test |
|---|---|---|
| 1–3 profile totality and identity | PASS | Amendment leaves the complete invertible typed profile groupoid unchanged. |
| 4–6 restriction, automorphism, deletion | PASS | Literal marked functor, pseudo-limit scope, and stochastic deletion remain separate. |
| 7–12 global type and behavioral structure | PASS | Non-standard completions and hierarchical independent axes remain literal. |
| 13 history as channel | PASS | Child values and invariant coarse outputs remain in the one resolved Paper 13D generator fiber. |
| 14 staged trace erased | PASS | Retained trace structure may distinguish channels; accepted staged fusion remains a distinct process trace. |
| 15 deterministic union as branching | PASS | Paper 13D has one resolved fusion generator; general same-target controls do not promote it. |
| 16 desired probability inserted as measure | PASS | Both \(\mu\) and \(\mathsf M\) require prior provenance; the two-level no-go detects post-hoc encoding. |
| 17 support normalized without provenance | PASS | Plurality is explicitly weaker than positive measure-supported branching. |
| 18 orbit/groupoid swap | PASS | CM5 gives different numerical laws under the two declared bases. |
| 19 topology/groupoid selects Haar | PASS | Retained Definition 14 requires independent measure provenance. |
| 20 divergent raw iterate | PASS | CM7 fails the inherited finite-word target condition. |
| 21 marginal associativity implies pentagon | PASS | CM6 passes target associativity and fails resolved pentagon. |
| 22 rooted spectator wreath | PASS / OPEN | The factorial is recognized; no cancellation theorem or physical measure is promoted. |
| 23 context averaged away | PASS | A context distribution remains new state data, not automatic closure. |
| 24 hidden state closure | PASS | Undeclared phase, clock, history, or cache remains forbidden. |
| 25 measure/character promoted separately | PASS | The resolved and target \(h\)-gauge leaves both probability laws invariant. |
| 26 normalized representation as selection | PASS | The no-go now applies independently to resolved and target normalized kernels. |
| 27 character family called different physics | PASS | Deterministic additive character families still induce one resolved singleton law and one target law. |
| new joint resolved measurability | **FAIL** | CM1 satisfies all stated fiber hypotheses and a valid target convolution but gives a nonmeasurable resolved split. |

### Positive controls 45–54 and amendment controls

| control | result | reconstruction |
|---|---|---|
| 45 finite Frobenius–Perron | PASS | Fibonacci resolved slots normalize; target mass is their pushforward. |
| 46 countable deterministic | PASS | \(d_r(n)=r^n\) varies, while the one resolved channel and target addition laws are unchanged. |
| 47 continuous deterministic | PASS | Measurable characters are \(e^{\lambda a}\); resolved singleton and target laws remain deterministic. |
| 48 standard nonatomic inverse limit | PASS | The countable binary tower has the standard Borel Cantor completion. |
| 49 non-standard cylinder limit | PASS | For uncountable \(I\), \((\mathbb Z/5)^I\) with cylinder sigma algebra is non-countably generated and admits coordinatewise composition. |
| 50 hybrid sector | PASS | A discrete label convolution does not select a measure on a continuous fiber. |
| 51 contextual refusal | PASS | Context-indexed resolved measures or targets cannot be averaged without a context law. |
| 52 gauge representatives | PASS | The resolved \(h\)-formula and target pushforward give identical laws. |
| 53 normalized representation lacks provenance | PASS | Setting an already chosen resolved kernel to \(\mu\), or target kernel to \(\mathsf M\), explains neither. |
| 54 current Paper 13D fusion | PASS | One resolved generator and one target; bond alternatives are Gamma histories. |
| required two-channel same-target ring | PASS | \(a^2=2a\), \(d(a)=2\), resolved \((1/2,1/2)\), target \(\delta_a\). |
| continuous zero-point-mass branching | PASS | CM4 has positive disjoint families although every singleton has zero mass. |

## 7. Target and resolved gauge/no-go scope

The amendment correctly distinguishes two representation no-go statements.
If a target Markov convolution is already chosen, then
\(\mathsf M=\mathsf P^{\rm tgt},d=1\) is a representation, not a derivation.
If a normalized resolved kernel on a properly defined measurable channel
bundle is already chosen and its target pushforward is associative, then
\(\mu=\mathsf P^{\rm res},d=1\) likewise only re-encodes that law.

The second statement is conditional on the missing measurable-bundle/kernel
typing. As a fixed-input identity it is true; as a global Markov-kernel
theorem it cannot be applied until the resolved event sigma algebra and
input measurability exist.

The \(h\)-gauge is complete only for target-dependent scalar refactorizations
on the same resolved measurable object. It does not classify within-target
redistributions, refinements, disintegrations, or different groupoid bases.
Version 3 does not claim otherwise.

## 8. Accepted Paper 13D result

The stronger resolved-channel criterion does not refute the accepted-law
fork. For one fixed Paper 13D component family, the simultaneous n-ary fusion
generator, target boundary species, occurrence union, partition forgetting,
and structural syntax are fixed before cross-pair seeds are sampled. There
is one resolved generator isomorphism class and one target class.

Cross-bond values, and every invariant measurable coarse output of them, are
child history variables. Retaining them gives the corresponding
\(\mathbf\Gamma_D\) pushforward. It does not manufacture a second resolved
channel object or an autonomous \(\mu\). Primitive, staged, fused, and
disconnected whole complexes remain possible selector arguments with
unconstructed relative propensities.

## 9. Full reviewed version-3 product vector

The measurable-kernel defect invalidates one general amended theorem but
does not warrant a false physical promotion or a demotion of the independently
constructed sector-referent contract. All conservative current coordinates
therefore remain literal.

```text
P18-SECTOR-REFERENT-CONTRACT-CONSTRUCTED
P18-BOUNDED-SECTOR-CENSUS-UNCONSTRUCTED
P18-GLOBAL-SECTOR-COMPLETION-UNCONSTRUCTED
P18-CURRENT-GAMMA-STRUCTURAL-BRANCHING-FORK-PROVED
P18-NONTRIVIAL-STRUCTURAL-BRANCHING-UNCONSTRUCTED
P18-PHYSICAL-CHANNEL-MEASURE-UNCONSTRUCTED
P18-COMPOSITION-CLOSURE-UNPROVEN
P18-POSITIVE-CHARACTER-UNTESTED-NO-PHYSICAL-CHANNEL-MEASURE
P18-RESOLVED-CHANNEL-LAW-UNCONSTRUCTED
P18-TARGET-SECTOR-LAW-UNCONSTRUCTED
P18-WHOLE-SELECTOR-UNCONSTRUCTED
P18-ACTUALIZATION-UNCONSTRUCTED
P18-CHRONOLOGY-NOT-EVALUATED
P18-DIMENSION-NOT-EVALUATED
P18-SIGNATURE-NOT-EVALUATED
P18-METRIC-NOT-EVALUATED
P18-CURVATURE-NOT-EVALUATED
P18-GRAVITY-NOT-EVALUATED
```

## 10. Terminal Seat-M assessment

Version 3 correctly repairs the version-2 target-plurality defect. It admits
inequivalent same-target channels, separates set plurality from
positive-measure branching, normalizes resolved and target measures for each
input, preserves both levels under the gauge, handles continuous channel
families, and keeps marginal and path coherence distinct.

Its first unresolved defect is prior to those probability identities: the
fiber class spaces and pairwise measures do not assemble into a declared
measurable resolved-channel bundle and kernel. The same-target non-Borel
split proves that a valid measurable target convolution does not fill this
gap. Because the missing condition is a bounded mathematical typing
requirement and selects no physical answer, Seat M returns `REVISE`, preserves
the full vector above, and authorizes no implementation or repair.
