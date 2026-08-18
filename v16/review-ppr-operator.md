# Independent hostile review of PPR — operator, representation, and quantum information seat

Date: 2026-08-18  
Seat: O — operator, representation, and quantum information  
Target: v16 Paper 3, `Contextual pullbacks and permanent records`  
Verdict: **REJECT**  
Proposed adjudicated primary: **`PPR-BLOCKED-AT-EVENT-ALGEBRA`**

## 1. Executive finding

The exact finite calculations are reproducible and, with one clarification to
the Bell test, mathematically correct.  The stable-null algorithm is a valid
greatest-fixed-subfamily construction for its declared finite continuation
graph.  The Kraus rotation, heterogeneous pullback, interference,
all-input-completeness, fixed-Bob, and rival-law numbers all rebuild exactly.

The candidate nevertheless does not construct the object its primary sentence
requires.  It constructs several neighboring operator fixtures and conjoins
their Boolean gate results.  There is no single history functional, event
algebra representation, or instrument packet in which:

1. the graph-individuated event atoms label the displayed history operators;
2. the stable-null observations and continuations are the continuations of
   those same history operators;
3. the record instrument is a coarse graining of that same event algebra; and
4. either `law-A` or `law-B` supplies all of those structures.

In particular, the gate that distinguishes a Kraus change from an event change
only conjoins an unrelated graph-signature Boolean with the Kraus calculation.
It never defines the map whose covariance would decide which Kraus isometries
preserve the relational event algebra.  Thus the paper cannot yet decide its
own representation-versus-event fork.  The exact components survive as
fixtures; the claimed contextual-pullback architecture does not yet exist as
one typed law.

This is not a complaint that the law is unselected.  It is an earlier typing
failure.  Under the frozen outcome order, the first applicable result is
`PPR-BLOCKED-AT-EVENT-ALGEBRA`.

## 2. Independence and target authentication

I read the frozen pin, both freeze notes, the immutable first-run chronology,
the repaired generic and physical sources, the data-only fixture, transcript,
receipt, generated paper, candidate-verification note, and the common hostile
protocol.  I did not import either PPR implementation into my reconstruction.
My independent arithmetic used a separate standard-library `Fraction` matrix
implementation in `/private/tmp/ppr_operator_independent.py`.  I did not read
or consult another review report.

The frozen hashes reproduce from the target commits:

| artifact | protocol value | independently observed |
|---|---:|---:|
| scorer | `c7f1cfb63b179746d0a66f28c1a6ec79975f8489a025d1196a2531d9fee069d6` | equal |
| fixture | `cecc3b0d3c7bf46503481fa7b422e915ba0ff6aac42e3cec5f61c395e565b389` | equal |
| transcript | `0c85efb4186e0faf6afc55f06184e9351bd6df621297ab2155745d7106e45b05` | equal |
| receipt | `dc88d6a2fbcf350785cc5f12cdcb8ea0805c4df6deaacac9ceffd34b1699c630` | equal |
| Paper 3 | `ca7b06e9e5540d81afb4a401beb66cb2834e3e74033fd742ac5257108a19654f` | equal |

The chronology also authenticates:

- pin commit `828b510a3229ae6330a55520b676a33e031c77a8` has no PPR core;
- core commit `f81a0ff3e67f5893a0eca3c1fbd4e83b599049df` has no physical fixture;
- fixture/scorer commit `e055ed69a75cbe8f996508ea1417d0ca76e8c451` has no result artifact;
- repaired-scorer commit `49e93ab964ee8b6670e70e5de845c8b322cdd78e` still has no result artifact;
- candidate commit `0f7a4b9bfc55be224143b2bc56bd4a5f5f51e5ee` supplies the three sealed results.

The first execution's `Invalid literal for Fraction: '9/25i'` refusal occurs
before physical gates or writes, and the subsequent source delta is confined
to the documented serialization-boundary repair.  The earlier freeze note's
mistyped pin commit is explicitly corrected forward in the fixture-freeze
note.

An archive of the candidate's runtime set, extracted without `.git`, produced
two byte-identical clean runs from an alien working directory.  Each run
matched the committed hashes above.  The receipt contains all eight payload
seals, and all eight recompute.  The fixture has no nested key named
`expected`, `result`, `verdict`, or `outcome`.  The scorer AST contains zero
floating-point constants.  The eight lens-relevant registered mutants I ran
(`event-mix`, `kraus-promote`, `pullback-half`,
`dark-reactivate-drop`, `null-promote`, `completeness-amplify`,
`transport-flatten`, and `seal-after-write`) all exited 1 and wrote no
artifact.

These checks authenticate the bytes and execution.  They do not cure the
missing joint packet.

## 3. Independent exact reconstruction

### 3.1 Kraus rotation and the precise gauge split

Put `a=3/5`, `b=4/5`, `K0=aI`, and `K1=bZ`.  The candidate's rotated family
is

$$
L_0=aK_0+bK_1,\qquad L_1=-bK_0+aK_1.
$$

The coefficient matrix is real orthogonal.  Direct superoperator expansion
gives

$$
\sum_j L_j\rho L_j^\dagger
=\sum_j K_j\rho K_j^\dagger,
\qquad
\sum_jL_j^\dagger L_j=I.
$$

The calibrated first outcome differs: for example,
`K0^dagger K0=(9/25)I`, while
`L0^dagger L0=diag(1,49/625)`.  Therefore the unconditioned channels are
equal and the two-outcome instruments are unequal, exactly as reported.

The correct gauge statement is two-tiered:

- after forgetting all Kraus/outcome labels, an isometric Kraus mixing is
  representation gauge for the channel;
- with a fixed outcome algebra, only isometries within each fixed outcome
  fiber preserve the instrument, together with calibrated outcome
  permutations/automorphisms;
- with a finer physical history algebra, an additional mixing is gauge only
  after one proves that it implements an automorphism or admitted refinement
  of that algebra and preserves every class operator/functional pairing.

The candidate proves the first two bullets in one example.  It supplies no map
needed to test the third.  Its graph-signature calculation is separate from
the Kraus indices.

As an extra isometry control, replacing `K0` by `-K0` while keeping `K1`
fixed is a nontrivial outcome-preserving Kraus isometry.  Both outcome
superoperators and every displayed statistic remain unchanged.  This is a
genuine representation gauge.  Whether the same phase is gauge for a
coherently summed history depends on the missing history-to-event map.

### 3.2 History split/merge

The displayed refinement is the identity

$$
\frac35 I+\frac45J
=\frac15I+\frac25I+\frac45J.
$$

It is exact.  It proves linear additivity of one coarse class operator.  It
does not prove that a full decoherence functional, record instrument,
continuation family, or event algebra is invariant under the split.  In
particular, if the two new spellings are separately recorded, their refined
instrument has more outcomes even though their coarse sum agrees.  The paper's
event-algebra invariance language is therefore broader than this control.

### 3.3 Multi-boundary stable null

Independently applying the pinned recurrence gives constraint-rank histories

$$
(1,1,1)\longrightarrow(1,2,1)\longrightarrow(2,2,1)
$$

in sorted `(cut,middle,final)` coordinates.  There are two strict rounds.  At
the cut, the present kernel has dimension `3`, while the stable kernel is

$$
\operatorname{span}\{e_2,e_3\}
$$

and has dimension `2`, agreeing with the receipt.

For the declared finite graph the construction is indeed greatest: if a
multi-boundary subfamily lies in every present kernel and every continuation
maps it into the corresponding target subfamily, induction places it in every
stage of the descending sequence, hence in its finite fixed point.  Conversely
the fixed point is invariant by construction.  This is a valid finite theorem.

It is not generated by the displayed relational law.  The observations and
continuations are a separate abstract fixture.  A newly appended typed probe

$$
C_{\rm new}=(0,0,1,0):\mathbb Q^4\longrightarrow\mathbb Q
$$

reactivates `e2` and reduces the stable cut null dimension from `2` to `1`.
This does not contradict the paper's explicit grammar-relative caveat.  It
does show that sentences using “ever” must always carry the registered-grammar
quantifier locally.

### 3.4 Mandatory extra null dilation

I added a fifth cut coordinate that every observation and continuation
annihilates.  This is a nonminimal event-algebra-preserving null dilation not
listed among the scorer's mutants.  The exact result is:

| quantity | frozen fixture | null-dilated fixture |
|---|---:|---:|
| present cut null dimension | 3 | 4 |
| stable cut null dimension | 2 | 3 |
| quotient rank | 2 | 2 |

Thus the physical quotient is unchanged up to the evident isomorphism, but
sealed claim C1's two null dimensions move.  Since the pin explicitly lists
null dilation as comparison gauge, C1 must be labelled a presentation-dependent
fixture regression, not a physical invariant.  No headline screen probability
or quotient rank moves.

### 3.5 Pullback and common future

The independent product is

$$
U_\alpha^\dagger U_\beta=
\begin{pmatrix}
0&1&0\\
-3/5&0&-4/5
\end{pmatrix}.
$$

All four reached basis pairs obey

$$
\langle U_\alpha x,U_\beta V_{\rm grow}y\rangle
=\langle x,(U_\alpha^\dagger U_\beta)V_{\rm grow}y\rangle.
$$

This is an adjoint identity, not an independently selective dynamical law.
It is nevertheless useful bookkeeping and correctly kills the half-pullback
tamper.

Appending a zero row to both continuations is a nonminimal common-endpoint
dilation and leaves the pullback exactly unchanged.  In contrast, adding a
new allowed future effect `E=diag(1,0,0)` changes the contextual pairing to

$$
U_\alpha^\dagger E U_\beta=
\begin{pmatrix}
-36/125&9/25&-48/125\\
-48/125&12/25&-64/125
\end{pmatrix}.
$$

The choice of common endpoint, its inner product/effect algebra, and the
continuation maps therefore remains law/context data.  The pullback removes a
second, inconsistent cut-level pairing only after those data are supplied; it
does not derive them.  The paper partly says this under “contextual,” but the
plain-language claim that no extra ruler is needed needs this qualification.

### 3.6 Coherent, dangling, partial, and one-outcome controls

Every displayed positive class operator is all-input complete, not merely
normalized on `|0>`.  My exact reconstruction gives:

| control | claimed | independent result |
|---|---:|---:|
| reconvergent coherent screen 0 | `49/625` | `49/625` |
| reconvergent decohered screen 0 | `337/625` | `337/625` |
| dangling Hermitian cross operator | zero | zero |
| dangling record probability | `256/625` | `256/625` |
| partial coherent screen 0 | `361/15625` | `361/15625` |
| partial decohered screen 0 | `6121/15625` | `6121/15625` |
| partial absolute shift | `1152/3125` | `1152/3125` |
| partial shift divided by `mu=4/5` | `288/625` | `288/625` |
| one-outcome total | `1` | `1` |
| later coherent probe | `1/50` | `1/50` |
| later decohered probe | `1/2` | `1/2` |

For the dangling control the vanishing is structural at this fixture: its
coherent overlap is proportional to `i Z diag(3/5,1)`, which is
anti-Hermitian because the two real diagonal factors commute.  It does not
imply that the whole process is entanglement breaking.

The partition routine provides a coordinate-support classical-label test.
For its positive block fixture, disjoint output supports do permit recovery of
the classical block label.  It does not construct a recovery channel, and its
multiple-maximal control uses a continuation with zero columns.  Consequently
the routine is not a general quantum recoverability theorem and cannot by
itself promote “support separation” to permanence beyond the registered
coordinate grammar.

### 3.7 Completeness, Bell witness, and fixed Bob

Both growth instruments satisfy `sum_j K_j^dagger K_j=I` as operator
identities.  On the Bell state they both give

$$
\rho_B=\frac12I,
$$

while the incomplete amplifier gives `diag(1/2,2)`, exactly as reported.

The general fixed-Bob statement is correct, including changing Alice output
dimension, but the paper should prove it.  For every Bob effect `X`,

$$
\operatorname{Tr}\!\left[X\,\operatorname{Tr}_{A'}
\sum_j(K_j\otimes I)\rho(K_j^\dagger\otimes I)\right]
=\operatorname{Tr}\!\left[
\left(\sum_jK_j^\dagger K_j\otimes X\right)\rho\right]
=\operatorname{Tr}[(I\otimes X)\rho].
$$

This proves only unconditional no-signalling for a fixed Bob tensor factor.
It says nothing about conditioned branches, remote steering, reconvergence, or
how to identify Bob after the Bob algebra itself changes.  The paper's open
list correctly retains those debts.

The scorer's Bell-purity rows are calculated on the untouched Bell density
matrix rather than on the channel output.  That gate alone is not a channel
test.  Independently applying the reconstructed local unitary class operator
to Alice's Bell half leaves joint purity `1` and Bob purity `1/2`; hence the
intended non-entanglement-breaking witness is correct.  The implementation
should gate that evolved state directly.

### 3.8 Rival law rows

Both displayed weight rows produce unitary `2 x 2` class operators.  Their
held-out screen pairs independently reproduce as

$$
(49/625,576/625),\qquad (0,1).
$$

Thus this particular local safety surface does not select between them.  What
does not follow is the paper's stronger sentence that both laws satisfy “the
same construction”: the scorer never equips either law with the stable-null,
record, pullback, comparison, or signalling packets tested elsewhere.

## 4. Operator-level literature and attribution boundary

The external antecedents are accurately characterized but do not fill the
candidate's missing bridge:

- Craig's positive decoherence functional gives a semi-inner-product geometry
  on history operators; it does not select which relational graph events are
  the physical history atoms ([arXiv:quant-ph/9704031](https://arxiv.org/abs/quant-ph/9704031)).
- Gudder proves Hilbert-space representation results for decoherence
  functionals, with strong positivity governing quantum-measure
  representability; the candidate never constructs the one functional whose
  quotient, records, and graph laws it combines
  ([arXiv:1011.1694](https://arxiv.org/abs/1011.1694)).
- Kretschmann--Schlingemann--Werner concerns Stinespring representations and
  their continuity.  It licenses representation analysis of a fixed channel,
  not a preferred event algebra
  ([arXiv:quant-ph/0605009](https://arxiv.org/abs/quant-ph/0605009)).
- Chiribella--D'Ariano--Perinotti type composed quantum networks through combs
  and link products.  Their framework does not identify the candidate's
  separately declared graph histories with its Kraus indices
  ([arXiv:0904.4483](https://arxiv.org/abs/0904.4483)).

No citation is falsely quoted.  The issue is attribution by analogy: the
papers provide precedents after a process/event packet is typed, while PPR has
not typed that packet jointly.

## 5. Findings, most severe first

### O-F1 — FATAL — the claimed joint law is a conjunction of unrelated fixtures

The primary classifier combines booleans extracted from separate matrices and
graphs.  There is no common history space, no one strongly positive
functional, and no operator-valued representation of the graph event algebra.
`law-A` and `law-B` are tested only in the relational-wedge fixture.  Therefore
the sentence “two laws satisfy the same construction” is not a measured fact.

**Kill:** the positive primary is not earned.  Select the earliest frozen
block, `PPR-BLOCKED-AT-EVENT-ALGEBRA`.

**Required repair:** build one packet in which every graph-history atom has a
typed class operator; its coarse event algebra maps to calibrated instrument
outcomes; one complete-history functional generates the displayed cross
terms; and its licensed continuation family generates both the null quotient
and record tests.  Run both rival laws through that same packet.

**Replacement sentence:**

> The registered fixtures separately realize a graph event catalogue, a
> channel/instrument representation split, a continuation-stable null family,
> contextual Gram pullbacks, and finite record controls; this paper does not
> yet construct one law in which those structures are jointly typed.

### O-F2 — MAJOR — the candidate cannot classify Kraus gauge relative to its event algebra

The event gate checks only that two graph signatures differ.  The Kraus gate
then conjoins that Boolean without mapping either Kraus label to either graph
event.  The forbidden-mixing conclusion is therefore a declaration rather
than a discriminator.

**Required repair:** supply and gate the event-algebra representation and test
the full stabilizer: block-isometric Kraus changes within calibrated outcomes,
admitted event automorphisms, admitted refinements, and an explicit cross-event
mixing negative.

**Replacement sentence:**

> The exact rotation proves that unconditioned-channel equivalence is weaker
> than calibrated-instrument equivalence; whether it mixes distinct relational
> histories is undecided until those histories are mapped to the instrument's
> outcome algebra.

### O-F3 — MAJOR — the history split proves one linear identity, not event-algebra invariance

Splitting `3/5` into `1/5+2/5` preserves one coarse class operator.  It does
not preserve a refined instrument if the two children are separately
recorded, and no decoherence-functional or continuation naturality square is
tested.

**Required repair:** define admissible refinement morphisms, show the
functional and all calibrated coarse instruments commute with them, and add a
recorded-split negative control.

**Replacement sentence:**

> The displayed split is a coarse class-operator additivity check; no general
> history-refinement invariance theorem is claimed.

### O-F4 — MAJOR — null dilation moves a sealed numeric claim

The extra null coordinate leaves quotient rank and all physical screens
unchanged but moves C1 from `3 -> 2` to `4 -> 3`.  Null dilation is explicitly
inside the pin's comparison gauge, so those dimensions are not physical
invariants.

**Required repair:** render quotient rank/isomorphism class as the invariant;
label raw null dimensions as fixture coordinates; add the dilation to the
representation battery.

**Replacement sentence:**

> In the frozen presentation the null dimensions change from 3 to 2; under a
> pure null dilation those raw dimensions change while the quotient rank and
> every admitted statistic remain invariant.

### O-F5 — MAJOR — pullback derivation is conditional on freely supplied future data

`U_alpha^dagger U_beta` is forced by adjunction after a common endpoint,
endpoint inner product/effect algebra, and two continuations are chosen.  A
new future effect changes it exactly.  The paper mostly acknowledges
contextuality but overstates the result in its plain-language and concluding
ontology sentences.

**Required repair:** state the conditional theorem, type admissible changes of
future context, and prove compatibility only on overlaps of contexts actually
declared to encode the same fact.

**Replacement sentence:**

> Once a common future context and its continuation maps are part of the law,
> their Gram pullback is the unique pairing reproducing that context's cross
> terms on reached subspaces; choosing the future context remains law data.

### O-F6 — MAJOR — support separation is not general quantum recoverability

The finite support rule gives a readable classical coordinate label in the
positive fixture, but no recovery channel is constructed and the ambiguous
partition control is not a complete continuation.  The operator theorem is
therefore narrower than “recoverable through all licensed futures” unless
licensed futures are explicitly restricted to this coordinate-support class.

**Required repair:** either construct recovery instruments for every claimed
record sector and future, or rename the result support-separation at the
registered basis grammar.  Completeness/trace preservation must be a gate for
physical continuation examples.

**Replacement sentence:**

> At the registered coordinate-support grammar, the positive fixture retains
> a perfectly distinguishable classical sector label and the eraser does not;
> general continuation-stable quantum recoverability is not proved.

### O-F7 — MINOR — Bell non-entanglement-breaking intent is correct but the gate tests the input

The purity gate evaluates the bare Bell state.  Applying the candidate's local
unitary supplies the intended witness and independently passes, so the paper's
narrow conclusion survives.

**Required repair:** gate joint and marginal purity after the local class
operator, or gate the class operator's unitarity together with the theorem
that local unitaries preserve Schmidt rank.

**Replacement sentence:**

> Applying the reconstructed local unitary to one half of a Bell state leaves
> joint purity 1 and reduced purity 1/2, so this channel is not entanglement
> breaking.

### O-F8 — MINOR — the general fixed-Bob theorem needs its operator proof in the paper

The theorem is true and my proof above covers arbitrary finite Alice output
dimension, but the delivered gate displays only one Bell input and two
instruments.

**Required repair:** include the Heisenberg-dual proof, with the fixed Bob
factor and unconditional scope in the theorem statement.

**Replacement sentence:**

> For a fixed Bob tensor factor, every all-input-complete local Alice
> instrument preserves Bob's unconditioned marginal, including when Alice's
> output dimension grows; conditioned steering and a changing Bob algebra are
> outside this theorem.

## 6. Protocol questions answered from this seat

1. **Are the 25 rows and primary index internally correct?** Yes as software
   outputs; every operator-level load-bearing number I rebuilt agrees.  The
   index is not semantically licensed because its booleans do not inhabit one
   packet.
2. **Is the event algebra calibrated enough to restrict Kraus gauge?** No.
   The graph and Kraus labels are never connected.
3. **What is the stable-null quantifier?** Greatest invariant null family for
   the declared finite continuation graph only; it is not law-generated here.
4. **Are pullbacks sufficient?** Yes for the cross terms of a fixed supplied
   future context on reached subspaces.  Endpoint, effect algebra, and
   continuations remain free law/context data.
5. **Does the record test prove durable availability?** It proves a finite
   coordinate-support distinguishability claim in enumerated maps, not a
   general CP-recovery theorem.
6. **Are quotient and record one object?** No; they are parallel fixtures.
7. **Is the heterogeneous carrier the graph-rewritten carrier?** No typed
   operator identification is supplied in this candidate.
8. **Does the graph do irreducible predictive work?** The operator seat can
   verify distinct path products, but without the missing event/operator weld
   that does not establish one irreducible joint packet.
9. **Is the non-flat loop generated or declared?** Its phase operator is
   declared as fixture data; the screen response is exact.
10. **Do rival laws move a calibrated observable?** Yes, within the local
    wedge fixture; they are not shown to satisfy all other packet components.
11. **What wording survives?** The exact arithmetic, finite stable-null
    theorem, conditional pullback identity, interference/completeness rows,
    and fixed-Bob theorem survive with the replacements above.
12. **Does the primary change?** Yes, to
    `PPR-BLOCKED-AT-EVENT-ALGEBRA`.

## 7. Minimal adjudication and repair/kill list

1. Reject the frozen positive primary; record the exact fixture numbers as
   surviving calibration evidence.
2. Select `PPR-BLOCKED-AT-EVENT-ALGEBRA` as the earliest applicable frozen
   outcome.
3. Require one typed graph-history-to-class-operator/instrument packet before
   any representation-invariance claim is restored.
4. Run stable-null, record, pullback, comparison, signalling, and both rival
   laws inside that same packet rather than conjoining separate fixtures.
5. Add the outcome-preserving Kraus phase, pure null dilation, new future
   effect, recorded-split, evolved-Bell, and complete recovery controls.
6. Treat raw null dimensions and all context-specific pullbacks as
   presentation/context data; publish only quotient and closed operational
   invariants as gauge-invariant content.

The result is not inconsistent, and no exact quantum calculation is killed.
The construction has simply stopped one rung earlier than its headline.

## 8. Self-authentication

Canonical self-digest convention: replace the 64 hexadecimal characters in
the next field by 64 ASCII zeroes, preserve every other byte, and compute
SHA-256 over the complete UTF-8 file.

Canonical report SHA-256: `871d12e0fba5ebf72159f75f7fc55d4ccf93ff7c873b8777c09e705ea74b571b`
