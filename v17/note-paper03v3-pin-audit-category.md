# Paper 03 v3 independent pin audit — category and mathematics

## Hybrid instruments, retained records, and certified traces

Date: 2026-08-22

Status: **RESULT-NEUTRAL INDEPENDENT PIN AUDIT**

Disposition: **REVISE BEFORE CONSTRUCTION**

First exact blocker: a point-valued retained outcome in a nonatomic
standard-Borel record space does not determine a normal state on the pinned
$L^\infty$ classical factor. The normal-extension property supplies an
integrated normal instrument and an almost-everywhere posterior field; it does
not turn each actual record value into a normal $L^\infty$ state.

This audit awards no Paper 03 v3 result and changes no v2 probability or
physics. The finite direct-sum regime is coherent. The obstruction is confined
to the advertised continuous retained-record duality and to deterministic
record pullbacks unless the missing nonsingularity conditions are added.

## 0. Authentication and independence

The audit was performed at exact committed HEAD
`13f9e8ee2774e69695b010b1ca1be1e9dc452f2c`, whose sole parent is
`9318cce38187df5cdb8eb5b7ce9ef7b41bb264a5`. The frozen pin is the HEAD
artifact, not a working-tree substitute.

| Bound artifact | SHA-256 | Exact size |
|---|---|---:|
| `v17/note-paper03v3-hybrid-instrument-semantics-pin.md` | `ada49694c66911455c2980c896ea10f8741d668ebb8af909e2f061c9d6e6d9af` | 597 LF / 25,686 bytes |
| `v17/note-paper03v2-hostile-review-adjudication.md` | `74303ddd93b4aac35d3368760da4a0ad3d442570cb16320467076aa5f93ea358` | 476 LF / 22,617 bytes |
| `v17/paper-03v2-causal-frontier-relativistic-adequacy.md` | `93eaa95fba10831618512ab95447d3527ff5d8877ab5119237f73bb8c30e0181` | 958 LF / 36,711 bytes |
| `v17/note-paper02v2-hostile-review-adjudication.md` | `37e1ada87f17723c248896f77ce03012d809f088632abb50ed01d1b166bed135` | 381 LF / 19,166 bytes |
| `v17/note-paper01-hostile-review-adjudication.md` | `3320414cb8161da33fbce3b1b8d3838cd3989d315de792c24cf24c0c322c2bb1` | 314 LF / 13,844 bytes |
| `v17/paper-00-reality-first-programme.md` | `a9f8456763447eaa25a6a840e8f221f51d961ecd9c3ced649ae35a8616457cbe` | 476 LF / 21,268 bytes |

The v3 pin was read completely. The bound v2 adjudication and the relevant
boundary, kernel, and instrument definitions in the bound v2 construction
were independently checked. In particular, v2 defines $X_D$ as a space of
predictive objects **and retained record values**, and says that a boundary
value contains actual record values. No quantum audit, sibling report, future
candidate, code, or unbound later result was inspected. The sole writable
path was this audit.

## 1. Audit question and standard

The question is not whether a useful hybrid algebra exists. It does. The
question is whether every object and quantifier frozen in the pin can be
implemented simultaneously while preserving the v2 kernel semantics exactly.

The required square is especially strict:

1. `Ev` acts on point-valued boundary data, including retained record values;
2. every registered predictive state at a boundary determines a normal state
   on the one hybrid algebra $\mathcal O_D$;
3. every complete reader agrees under `Ev` and `Heis`; and
4. continuous retained outcomes are included under the named NEP/reference
   hypotheses, not merely finite coarse-grainings.

A construction that proves only an ensemble-integrated identity, while v2
still admits each point-valued boundary input, has changed the semantic
domain. A construction that silently identifies values modulo a null ideal
has changed what a retained record is. Either change requires a new pin.

## 2. First decisive counterexample

### 2.1 A minimal admitted packet

Take the quantum algebra to be trivial,

$$
\mathcal A=\mathbb C,
$$

and take the retained record space to be

$$
R=[0,1],\qquad \nu=\lambda,
$$

where $\lambda$ is Lebesgue measure. Let the instrument be the ordinary
uniform classical outcome instrument. It has the required integrated normal
extension

$$
\Phi:L^\infty([0,1],\lambda)\longrightarrow\mathbb C,
\qquad
\Phi([f])=\int_0^1 f,d\lambda,
$$

and it has a strongly measurable outcome/state kernel. Thus the example is
not an attack using a non-NEP instrument, a missing reference class, a null
normalization, or nonmeasurability. It is the most elementary positive member
of the pin's Section 3.2 regime.

After the measurement, v2's `Ev` boundary value contains the actual retained
record $r\in[0,1]$. To reproduce a complete classical reader at that boundary,
the corresponding hybrid boundary state would have to act as point
evaluation:

$$
\delta_r([f])=f(r).
$$

### 2.2 The required state does not exist

Point evaluation is not well defined on $L^\infty([0,1],\lambda)$ equivalence
classes. For example,

$$
[\chi_{\{r\}}]=[0]
$$

because $\lambda(\{r\})=0$, whereas point evaluation would assign the two
representatives the values $1$ and $0$. Equivalently, the $L^\infty$ null
ideal has erased precisely the point that the retained boundary value says is
present.

Normal states on the commutative von Neumann algebra
$L^\infty([0,1],\lambda)$ are represented by $L^1(\lambda)$ densities. No such
density is the Dirac law at a nonatomic point. Tensoring with a quantum algebra
does not cure the classical obstruction: restricting any proposed normal
state on

$$
\mathcal A_D\,\overline\otimes\,L^\infty(R,\nu)
$$

to the central classical factor would still have to yield the impossible
point state.

Therefore the following frozen requirements cannot all hold:

- v2's point-valued retained record at the boundary;
- pin Section 3.2's nonatomic $L^\infty$ record factor;
- pin Section 7.1's normal boundary-state requirement;
- exact classical readers and adaptive controls at that boundary; and
- V3-T10 for every admitted packet.

This is an exact semantic/type counterexample. It is independent of the
quantum dynamics and changes no probability.

### 2.3 Why NEP does not repair the counterexample

The normal-extension property is exactly the right hypothesis for an
**integrated** complete instrument. The Okamura--Ozawa formulation also relates
NEP to measuring-process realizability and to strongly measurable posterior
families for normal input states. Those posterior families are defined only
almost everywhere with respect to the outcome law.

None of those facts supplies a normal state for each singleton outcome of a
nonatomic measure. The pin itself correctly refuses a point posterior at a
null singleton. It then reintroduces the same impossible pointwise demand by
requiring every point-valued retained boundary state to be normal on
$\mathcal O_D$.

The unconditioned joint record law is normal. An almost-everywhere controlled
future can also be represented at the level of that joint law. Those true
statements do not prove a duality on every v2 boundary value.

## 3. Finite direct-sum regime: coherent positive control

No analogous obstruction occurs for a finite retained set $R_D$. The algebra

$$
\mathcal O_D=\bigoplus_{r\in R_D}\mathcal A_D
$$

has one central atom for each exact record value. Point records are normal
states, guarded controls are block-diagonal maps, and event projections are
literal central summands.

For a finite instrument $\{\mathcal J_s\}_{s\in S}$,

$$
\widehat{\mathcal J}((A_s)_s)
=\sum_s\mathcal J_s(A_s)
$$

is CP, and it is unital exactly when
$\sum_s\mathcal J_s(1)=1$. Inserting an observable into one summand recovers a
branch CP map; restricting to the diagonal recovers the nonselective map.
Neither restriction is confused with the complete normalized arrow.

With a pre-existing record $r$, the construction must use the fiberwise
version

$$
\bigoplus_{(r,s)}\mathcal A_E
\longrightarrow
\bigoplus_r\mathcal A_D,
\qquad
(A_{r,s})_{r,s}
\longmapsto
\left(\sum_s\mathcal J_{r,s}(A_{r,s})\right)_r.
$$

This is an implementation obligation, not a new postulate. It provides the
binary measurement followed by the retained-result $I/X$ guard required by
the pin.

## 4. A second exact typing condition: measurable is not enough

Even after the boundary-state issue is repaired, the standard-Borel primitive
table needs a missing condition. A measurable map

$$
f:(R,\nu)\longrightarrow(S,\mu)
$$

induces a well-defined pullback

$$
f^*:L^\infty(S,\mu)\longrightarrow L^\infty(R,\nu),
\qquad [g]\longmapsto[g\circ f],
$$

only when

$$
f_*\nu\ll\mu.
$$

Mere measurability does not suffice. Let both spaces carry Lebesgue measure
and let $f(x)=0$. Then $[\chi_{\{0\}}]=[0]$ in the target algebra, but their
putative pullbacks are respectively $[1]$ and $[0]$. Thus the pullback is not
well defined.

The same issue occurs for deterministic record append into a product measure:
the image graph can be null in the target while its preimage is the entire
source. The construction cannot repair this by choosing representatives.
Every record write, coarse-graining, packet transport, and presentation map
must explicitly preserve the relevant measure class in the correct direction.

Pin Section 4.2's general state-class admission sentence can accommodate this
restriction, but Sections 5 and 12/C6 currently call a merely measurable map a
pullback. The frozen primitive contract therefore needs the nonsingularity
condition printed, together with compatible input/output reference classes.

## 5. Category and functor audit outside the blocker

Subject to the two repairs above, the categorical architecture is coherent.

### 5.1 Objects and arrows

For a fixed packet, selected finite direct sums with unital CP arrows form a
category. Represented $W^*$ hybrid objects with admitted normal UCP arrows also
form a category: identities are normal UCP, and composition preserves
normality, complete positivity, and unitality. If a packet crosses from a
continuous raw outcome to a finite retained coarse-graining, the exact
cross-regime arrow and its measure-class compatibility must be declared rather
than inferred from the word “measurable.”

Different target record or quantum schemas correctly give different boundary
objects. A common typed sum/joint interface is a valid alternative. Equality
of lower sets alone is not an interface identification.

### 5.2 Contravariant functor

Once each primitive is an actual arrow with exact endpoints, reverse
chronological composition gives

$$
\operatorname{Heis}_\Xi(q\circ p)
=\operatorname{Heis}_\Xi(p)\circ\operatorname{Heis}_\Xi(q).
$$

The empty path gives the identity. The pin has a display-level omission in
Section 6: the left side of the identity equation is absent. The only coherent
reading is

$$
\operatorname{Heis}_\Xi(\operatorname{id}_{B_{\Xi,D}})
=\operatorname{id}_{\mathcal O_D}.
$$

That omission is editorial and does not alter the first semantic blocker.

### 5.3 Boundary closure, discard, coarse-graining, and control

The Heisenberg directions are correct:

- discarding a record physically maps to inclusion of record-independent
  observables;
- coarse-graining maps coarse observables back to fine observables, provided
  the pullback is nonsingular;
- a retained-record guard is decomposable/block diagonal over an already
  present classical coordinate; and
- after discard or coarse-graining, a future operation cannot read a removed
  or finer coordinate because its source schema lacks that coordinate.

Explicit skip has a different frontier target from identity and therefore
cannot be silently collapsed to it.

### 5.4 Packet transport

Transporting only coordinates is insufficient. In the standard-Borel regime,
a packet isomorphism must include a Borel isomorphism whose pushforward sends
the source measure class to the target measure class, a normal algebra
isomorphism on quantum factors, and intertwiners for every primitive arrow and
kernel. With these data, hybrid transport is coherent and exact multiplicity
can be retained. A proper embedding still gives no canonical forward state
extension.

### 5.5 Certified trace congruence

The concurrency correction is mathematically sound. Equality of complete
`Ev` kernels and complete `Heis` maps on each supplied commuting square,
including output permutation and source lineage, generates a category
congruence. Both functors descend through the least such congruence.

For a finite poset, any two linear extensions are connected by adjacent swaps
of incomparable elements. Hence all-linearization equality follows only when
every reachable co-enabled swap in the protocol is certified. The pin's
reachable-context and full-certification qualifications are exactly what is
needed. No hidden microscopic clock or universal commutativity follows.

## 6. Fresh category/mathematics attacks

These attacks are independent of the pin's numbered list. `BLOCKER` means an
exact frozen-contract failure; `PASS/OBLIGATION` means the architecture can
handle the attack only if the stated construction duty is printed.

| ID | Fresh attack | Result |
|---|---|---|
| A1 | Retain an exact $r$ drawn from a nonatomic law and demand its normal hybrid boundary state | **BLOCKER:** point evaluation is erased by the $L^\infty$ null ideal |
| A2 | Replace an ensemble normal state by one of its zero-mass point outcomes | **BLOCKER:** disintegration is a.e.; normality does not descend to each point |
| A3 | Pull back $L^\infty$ along the measurable constant map $x\mapsto0$ with Lebesgue classes | **BLOCKER:** pullback is representative dependent unless $f_*\nu\ll\mu$ |
| A4 | Append a deterministic continuous value into a target carrying a nonatomic product reference class | **BLOCKER AS STATED:** the image graph may be target-null; an explicitly compatible target class is required |
| A5 | Measure after an existing retained value and forget the old fiber index in the complete arrow | **PASS/OBLIGATION:** use the fiberwise $\bigoplus_{r,s}\to\bigoplus_r$ arrow |
| A6 | Use an uncountable mutually singular registered family while asserting one sigma-finite dominating class | **PASS ONLY BY ADMISSION:** the packet must exhibit common domination; it is not automatic |
| A7 | Replace $\nu$ by an equivalent density and then by a singular Dirac measure | **PASS:** the first gives the canonical null-ideal isomorphism; the second must be refused |
| A8 | Read a discarded record in a later guard | **PASS:** the later source schema has no such coordinate, so the composite is untyped |
| A9 | Coarse-grain a fine record and later condition on the forgotten fine value | **PASS:** the required fine central projection is absent from the boundary object |
| A10 | Treat a finite branch insertion as an arrow of the normalized hybrid category | **PASS:** the insertion/branch is nonunital and is only a recovery map, not the complete arrow |
| A11 | Certify one scalar exchange but permute retained outputs differently | **PASS:** full-map/kernel equality plus explicit output permutation is required |
| A12 | Substitute an approximating NEP instrument for an exact one | **PASS:** only an explicitly approximate comparator result is available |

A1 is the first decisive semantic counterexample. A3 independently blocks the
primitive contract if “measurable pullback” is read literally. The remaining
attacks establish that the finite and certified-concurrency parts do not need
new physics.

## 7. Target and product consequences

The frozen pin cannot presently earn V3-T10 for every admitted packet. Since
the incompatibility already occurs at a retained boundary object, an unchanged
construction would encounter the outcome

`P03V3-HYBRID-BOUNDARY-TYPE-FAILURE`

before it could earn the dual-semantics rung. This audit does not award that
rung; it determines only that construction under the present pin is not
authorized by coherent mathematics.

The following coordinates remain feasible at finite-record or appropriately
repaired scope: input, slot-skeleton, frontier, boundary, procedure,
hybrid-object, heisenberg-functor, state-kernel, presentation, quotient,
covariance, state-class, instrument, causal-factorization,
certified-schedule, no-signalling, steering, bell, positive-model, context,
fibers, type-III, split, gauge, particles, continuum, UV, preferred-frame,
record, division, actuality, barandes, ontology, and downstream. The
`semantic-compatibility` coordinate is exactly where the nonatomic point-law
duality fails. No downstream coordinate is promoted by this audit.

## 8. Minimal result-neutral repair choices

There are three honest forward choices. None retunes a v2 probability,
instrument, or physical parameter, but each changes the frozen v3 semantic
contract and therefore requires a successor pin.

1. **Finite retained theorem only.** Keep continuous outcomes terminal unless
   a declared finite/countable atomic coarse-graining is retained. This uses
   the pin's existing fallback and yields the cleanest construction.
2. **Integrated continuous duality.** Keep point-valued records in `Ev`, but
   quantify the normal $L^\infty$ pairing only over normal ensemble laws and
   a.e. posterior/control fields. Explicitly refuse a normal hybrid state for
   each point boundary value. The relation between point kernels and ensemble
   algebra states must be newly typed.
3. **Point-separating classical observables.** Replace the $L^\infty$ quotient
   by a pointwise classical observable object that admits evaluation states.
   This changes the claimed $W^*$ target and requires fresh closure,
   normality, and transport proofs.

Every choice must also require nonsingularity
$f_*\nu_{\rm source}\ll\nu_{\rm target}$ for each deterministic record
pullback, or supply compatible reference classes that prove it.

The first choice is the smallest and already supports the mandatory adaptive
qubit control. The second is the natural route if continuous retained control
is scientifically important. The third is the largest mathematical change.

## 9. Disposition

**REVISE BEFORE CONSTRUCTION.**

The finite/direct-sum category, complete-instrument distinction,
contravariant composition, boundary schema closure, packet intertwiners, and
certified trace congruence are internally coherent and do not change v2
physics. The standard-Borel retained-record theorem is not coherent with the
bound v2 point-boundary semantics: an actual nonatomic record value is not a
normal state, or even a well-defined evaluation state, on its
$L^\infty$ equivalence-class algebra.

Construction should not begin under this pin. Freeze one result-neutral
successor choosing finite-only or integrated continuous semantics, print the
nonsingular pullback condition, and run the same independent audits again.
Paper 04, spacetime, and gravity remain closed. This is a mathematical typing
repair, not a reason to alter any quantum probability or physical claim.

## 10. Report authentication

Report line count: `000422`

Report byte count: `019117`

Normalized self-SHA-256: `4fdf704b233e1fbc49cb9551e0f4906e15a9b1b8003c243b9459f5567cefeb10`

Normalization rule: replace the 64 hexadecimal characters on the preceding
line by 64 ASCII zeroes, preserve every other byte, and compute SHA-256. The
report ends in one LF and contains no trailing horizontal whitespace.
