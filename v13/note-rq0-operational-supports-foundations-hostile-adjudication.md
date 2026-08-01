# Adjudication — RQ0-L0 analytical foundations hostile review

**Date:** 2026-07-31  
**Governing pin:** `ef69ddb8bfc350b5bceb23ec1f5d42eb4735d037`  
**Reviewed note:** `c952e0b0feaf8436a76bf034ea5dfc384d93b733`  
**Frozen hostile report:** `6baa2185aee7d27ccd28295757e530d7b0e8d158`  
**External verdict:** `REJECT`  
**Adjudication:** `REJECT — ACCEPTED`  
**Scientific RQ0-L0 outcome:** null

## 1. Decision

The hostile verdict is accepted. The provisional headline

$$
\texttt{RQ0-L0-INTRINSIC-CHART-GROUPOID}
$$

is withdrawn as an earned result. The note does not earn
`RQ0-L0-PULLBACK-CLOSED-PROCESS-COVER`, and it also does not earn
`RQ0-L0-FOUNDATIONS-NO-INTRINSIC-SUPPORT`: it has not proved that no coherent
operational language can determine intrinsic support. Its own proposed
language fails before that question can be settled.

The analytical cycle therefore closes with no registered scientific L0 rung.
Several narrow formal lemmas survive and remain useful antecedents. They do
not constitute a quantum chart, physical localization, or a localization
no-go theorem.

No definition, proof, example or interpretation in the reviewed note is
repaired here. This adjudication records what survives and halts the cycle.

## 2. Independent check of the fatal category obstruction

Definition 2.1 makes the operational presentation a finite category and maps
it functorially to finite-dimensional complex Hilbert spaces. In particular,
the endomorphism set of the distinguished boundary is finite.

Let the branch-memory seed use

$$
U=\operatorname{CNOT}(H_2\otimes I),
\qquad
V=H_2\otimes I,
$$

the preparation $\eta=|00\rangle$, the alternative projector
$Q=|00\rangle\langle00|$, and the probe $f=\langle00|$. Direct calculation
gives

$$
U|00\rangle
=
\frac{|00\rangle+|11\rangle}{\sqrt2},
$$

and hence

$$
fVQU\eta=\frac12.
$$

If every displayed W3 composite is an arrow, this scalar is represented by an
endomorphism $c$ of the distinguished boundary. Because the endomorphism set
is finite, two positive powers coincide:

$$
c^m=c^n
\qquad(m<n).
$$

Functoriality then gives

$$
2^{-m}=2^{-n},
$$

which is impossible. The contradiction does not depend on faithfulness of the
representation. Equality in the source is already enough.

This independently confirms F1. The problem is not that finite quantum
systems are impossible. It is that a category with finitely many arrows is
closed under arbitrarily repeated composition, while ordinary exact quantum
amplitudes generate infinitely many distinct scalar composites. A finite
typed presentation with only declared partial compositions might avoid this
obstruction, but that is not the object defined in the reviewed note.

The same definition also leaves the scalar unit, additive/dagger structure,
zero arrows, exact projector equations and congruence compatibility with
those equations under-specified. Those omissions matter to W3 and `Rec`.

**Adjudication of F1:** accepted at `FATAL` severity.

## 3. Independent check of the direct-sum completion claim

The displayed synchronized-amplitude identity is correct:

$$
\frac{f\oplus f}{\sqrt2}
(a\oplus a)
\frac{\eta\oplus\eta}{\sqrt2}
=fa\eta.
$$

The branch-memory matrices also have the stated preserve/erase behaviour at
matrix level. Those facts do not construct the two claimed amplitude
instruments.

The reviewed note does not provide their boundary objects, hom-sets,
composition tables, congruences, complete admitted families or gauge actions.
In addition:

1. $a\oplus I$ is not typed when $a$ has different source and target cuts
   unless an additional identification supplies the second summand map.
2. $P_r\oplus0$ is not a projector resolution of the whole direct-sum
   boundary, so a block inclusion does not preserve identities and resolutions
   as the proposed strong map requires.
3. The new completions are not retested against the definition's complete
   preparation, probe and continuation quantifiers.
4. One synchronized diagram generating the synchronized arrows does not prove
   that every W3-positive diagram has only the whole ambient envelope.
5. Merely counting two exchanged embedded charts does not prove that their
   groupoid is inequivalent to the synchronized result.

The construction therefore establishes an exact matrix identity, not a pair
of objects in the declared category with different intrinsic chart
groupoids. The localization-grounding theorem and its claimed exhaustive
trilemma do not follow.

**Adjudication of F2:** accepted at `FATAL` severity.

## 4. Internal W3 data and generated envelopes

The note makes real conceptual progress by removing `access_operations` from
the W3 support claim. It derives preserve, erase and `Other` classes from the
admitted continuation family, retains historical occurrence separately from
continuation-relative availability, and uses the same projectors in W3 and
the record algebra.

However, it selects the boundary cuts, write candidate, purported no-write
candidate, fine and coarse projector resolutions, and their refinement map
before running W3. Those choices can already encode the desired process
decomposition. Failure of correlation by the candidate $N$ also does not by
itself establish the physical interpretation “nothing was written.”

For a separately coherent closure system of strict subobjects, the
intersection of every closed subobject containing a fixed diagram is indeed
the unique least closed envelope. That is a standard closure-operator result.
It is conditional on the closure system being well defined. The note does not
equip each proposed subinstrument with the gauge data needed to make it an
object of the advertised strong-map category, and it does not define the
boundary gauge as an action by strong automorphisms. Thus the gauge-covariant
specialization is not proved.

The surviving result is:

> In a separately specified finite closure system of strict operational
> subobjects, a fixed selected diagram has a unique least closed envelope, and
> closure-system isomorphisms transport it.

It does not say that the envelope is proper, independently addressable,
uniquely selected by the ambient process, or support-neutral.

**Adjudication of F3 and F4:** accepted at `MAJOR` severity.

## 5. Physical pullbacks and record descent

Definition 7.1 correctly states a pullback universal property in the broad
category $\mathbf{QIns}^{\mathrm{str}}_{\mathrm{fin}}$. Theorem 7.3 proves a
different statement: literal intersection is a meet in the poset of strict
closed subinstruments of one already fixed ambient presentation.

A pullback in a subcategory is not automatically a pullback in a larger
category. The note does not prove that independently presented strong
embeddings possess strict images, that every compatible cone factors through
the literal intersection, or that the inclusion of the fixed-ambient poset
creates pullbacks. The theorem therefore establishes only a fixed-presentation
meet.

The projector-compression calculation used for `Rec` is sound under its
stated reducing and exact W3-compatibility hypotheses. Those hypotheses
already require the source record resolution and the whole record diagram to
be transported correctly. Consequently `Rec` is a conditional contravariant
Boolean functor on a category defined to contain only compatible maps; it is
not a theorem that candidate physical chart maps carry descending records.

Terminal RQ0-A remains a valid antecedent at its own declared finite scope:
there, the region maps and projector pullbacks were explicitly constructed.
It does not establish intrinsic chart discovery or the broader pullback
theorem proposed here.

**Adjudication of F5 and F7:** accepted at `MAJOR` severity.

## 6. Symmetry and groupoid scope

The no-selection theorem is correct. If a group acts transitively on more than
one candidate and the available data are invariant, no invariant rule selects
one member.

What follows is only non-selection. The theorem does not identify physical
symmetry with boundary gauge, prove that an action groupoid is the unique
physical output, or include chart isomorphisms that do not extend to ambient
automorphisms. An invariant orbit, a quotient, physical multiplicity and a
groupoid are distinct possibilities whose correct use depends on independently
specified ontology.

**Adjudication of F6:** accepted at `MAJOR` severity. The group-theoretic
no-selector lemma survives; the intrinsic-chart-groupoid headline does not.

## 7. Controls and support-smuggling lemma

The controls adjudicate as follows:

| Control | Adjudicated status |
|---|---|
| Public `Q8` | Survives as a support-smuggling negative: its subgroup orbit is intrinsic algebra, while its W3-to-subgroup attachment is supplied through `access_operations`. |
| Terminal RQ0-A | Survives only as a declared-region, declared-map physical-overlap antecedent. |
| Heterogeneous tensor product | Not proved under the all-continuations envelope rule; selected factor boundary types can plant the answer. |
| Symmetric copies | Only the abstract no-selector lemma survives; proper internal W3 envelopes were not constructed. |
| Synchronized no-proper-chart | Not proved; the completion is not an instrument in the stated class and one generating diagram does not exhaust all W3 diagrams. |

The $M_2(\mathbb C)\to\mathbb C$ no-retraction argument is correct: simplicity
of $M_2(\mathbb C)$ prevents a unital $*$-homomorphic retraction onto scalar
matrices. It usefully separates a split operational retract from a generic
channel or conditional expectation.

The support-smuggling theorem is also correct at its exact narrow scope. If a
localization rule changes when only an external support label changes, it
cannot factor through the data obtained after forgetting that label. This is
a forgetful-fibre identifiability lemma. It rules out recovery that follows
the independently attached label; it is not a general no-go theorem for
internally grounded localization.

**Adjudication of F8 and F9:** accepted at their frozen severities.

## 8. Claim disposition

### Secure narrow results

1. External-support dependence is non-identifiable after the support field is
   forgotten.
2. The public `Q8` record-to-subgroup attachment is an instance of that
   defect.
3. A fixed diagram has a least envelope in any separately valid finite
   closure system of strict subobjects.
4. Strict subobjects of one fixed ambient object have intersections as meets.
5. Reducing projector compression preserves the corresponding finite Boolean
   algebra and composes contravariantly.
6. A transitive action on multiple candidates has no invariant member
   selector.
7. The inclusion of scalar matrices into $M_2(\mathbb C)$ has no unital
   $*$-homomorphic retraction.
8. The synchronized direct-sum formula preserves the selected realized matrix
   amplitudes.

### Withdrawn or unearned claims

- a coherent finite exact amplitude-instrument category containing the W3
  seed;
- internally derived proper quantum process charts;
- gauge-covariant generated envelopes in the stated strong-map category;
- an intrinsic chart groupoid as the forced physical output;
- physical pullbacks of independently presented charts;
- a generally populated physical record functor;
- the direct-sum localization-grounding counterexample;
- the heterogeneous tensor and symmetric-copy positive chart controls;
- a pullback-closed process cover;
- independent addressability;
- any spatial, topological, causal, geometric, field or gravitational claim.

## 9. Ontological disposition

The cycle has clarified a constraint, not found locality.

Stable records cannot acquire a physical “where” from an independently
attached support list. But moving the support information into selected
boundary types, admitted projector refinements or a stipulated embedding
category does not solve the problem. Those structures can carry the same
localization information in less visible form.

The honest present ontology remains:

- amplitude processes and W3-stable record seams are meaningful antecedents;
- declared quantum regions and their projector-compatible overlaps exist in
  terminal RQ0-A at its finite constructed scope;
- no intrinsic rule yet turns an unpartitioned amplitude process into proper
  quantum charts;
- no general physical overlap of independently recovered charts has been
  constructed;
- no spatial meaning attaches to “chart” at this stage.

The first unresolved analytical obligation is to specify a coherent process
language—likely with finite generators and declared partial typed composites,
rather than finitely many arrows closed under every iteration—that contains
the W3 examples without using boundary/projector choices to plant support.
Only after that language exists can envelope, addressability, physical
pullback and groupoid questions be asked again.

This paragraph identifies an obligation; it does not authorize a repair.

## 10. Final disposition and halt

The external `REJECT` is accepted without modification of the reviewed note.
The analytical cycle closes as:

$$
\boxed{
\begin{aligned}
\text{review disposition} &= \texttt{REJECT — ACCEPTED},\\
\text{scientific RQ0-L0 outcome} &= \texttt{null},\\
\text{strongest surviving content} &= \text{conditional formal lemmas only}.
\end{aligned}}
$$

`RQ0-T1`, `RQ0-C1`, topology, influence, causality, geometry, spacetime,
fields and gravity remain closed. No implementation or analytical successor
is authorized. **HALT and request explicit user authorization before any
further work.**
