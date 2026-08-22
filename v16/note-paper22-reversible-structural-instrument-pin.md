# Paper 22 reversible structural instrument pin

Date: 2026-08-21

Status: **FROZEN BEFORE MATHEMATICAL EVALUATION — RESULT NEUTRAL**

## 1. Question

Construct one typed structural instrument in which tensor-preserving and
fusion-changing transformations are operational alternatives of one common
parent, can be coherently queried and recombined, and can subsequently be
committed as genuine dependent structural outputs.

The construction must answer, rather than evade, the obstruction:

> Can a transformation that physically forgets a component partition be
> reversible without retaining that partition elsewhere?

It must distinguish:

1. a reversible coherent **fusion query**;
2. a stable **fusion commit** with a physical fused child; and
3. an autonomous law saying when the instrument itself occurs.

Only the first two are in scope. The third is not to be invented here.

## 2. Bound inputs

| artifact | role | ordinary SHA-256 |
|---|---|---|
| `v16/paper-13d-typed-executable-gamma.md` | accepted mathematical calibration and tensor/fusion children | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` |
| `v16/paper-20-predictive-structural-parent.md` | dependent-output and no-dormancy contract | `64111d7764bf70984b959e00bc1da30ad0d6c3ae7b5c6d51b94227ad2f5c35e6` |
| `v16/paper-21-exact-structural-interferometer.md` | exact discriminator | `ca0f709b00906971c6aac2b25b12fea11f168411ab2f440ccc49d982aab4ba80` |
| `v16/note-paper21-structural-interferometer-pin.md` | frozen filter and factorization controls | `7df73538f87a39e22a4aa221d4c94842620fb7c8329e68d072ea98a7c7e9f9f7` |

Nothing in this pin alters Paper 13D. Paper 22 is a new candidate law and may
not be described as inherited until its additional operations are separately
accepted.

## 3. Common source

An input consists of:

```text
X = (finite typed component family, physically marked active subfamily A,
     unmarked spectator family E, complete Paper 13D boundary values)
```

The active subfamily has at least two nonempty components. The mark is an
operational address transported by every presentation isomorphism. It is not
a component enumeration or a hidden time label.

The spectator family is carried identically. All route probabilities must be
independent of spectator identity and enumeration.

## 4. Dependent structural outputs

The accessible child fiber is

\[
 \mathsf Y_X
 =\mathsf Y_{T,X}\sqcup\mathsf Y_{F,X}.
\]

- `Y_T,X` retains the active component partition and has no new cross-active
  bond.
- `Y_F,X` applies the accepted simultaneous Paper 13D fusion law to the
  active family, drops that partition from the accessible target, carries
  spectators, and includes every accepted fresh cross-pair field.

The two fibers must be distinguished by complete lawful future behavior, not
by a naked output bit.

## 5. Structural-mode carrier

Use a two-dimensional mode carrier with physically typed basis

\[
 |T\rangle,\qquad |F\rangle.
\]

The basis meaning is fixed by the controlled transformations of Sections 6
and 9. Swapping printed labels together with every controlled operation is a
presentation change; swapping only the final decoder is a different physical
instrument.

The recorded mode law must recover

\[
 B=\frac1{25}\begin{pmatrix}9&16\\16&9\end{pmatrix}.
\]

Among two-mode reversible lifts of `B`, use the real orientation-preserving
representative

\[
 R=\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix}
\]

only if its uniqueness up to row phases, column phases, and simultaneous
basis relabeling is proved. Applying `R` to the structural mode is a new
physical hypothesis even if its moduli were accepted previously.

The relative phase operation

\[
 D_\phi=\operatorname{diag}(1,e^{i\phi})
\]

is an admitted apparatus control, not a parameter selected by a downstream
dimension result. The neutral setting is `phi=0`; held-out controls are
`pi/2` and `pi`.

## 6. Reversible query dilation

For each input `X`, construct natural reversible maps

\[
 U_{T,X},U_{F,X}
\]

on an enlarged query/witness/complement carrier.

The tensor query must compute a complete tensor witness. The fusion query
must compute a complete fusion witness and all accepted cross-pair outcomes.
It may purify stochastic seeds, but every purification register and every
phase convention must be explicit.

The controlled query is

\[
 U_{Q,X}
 =|T\rangle\!\langle T|\otimes U_{T,X}
  +|F\rangle\!\langle F|\otimes U_{F,X}.
\]

A complete middle reader must distinguish the two active witnesses. Before
route recombination, `U_Q,X^{-1}` must return:

- the source;
- the query witness;
- seed/purification registers;
- reversible complements; and
- every uncontrolled environment field

to one common value. If any field remains route dependent, the full-coherence
claim fails.

## 7. Mandatory no-hiding theorem

If two distinct tensor presentations have the same physically fused target,
a reversible map to that target alone is impossible. Every reversible
dilation must retain distinguishing complement states.

The paper must prove this both:

- for finite basis-state bijections; and
- for a quantum isometry, where the complement states must be orthogonal.

Consequences that must be enforced:

1. the reversible fusion query is not called irreversible physical fusion;
2. its complement is uncomputed before interference;
3. the final fused child is produced only in the post-recombination commit;
4. the complement is not exposed as part of the accepted child future; and
5. no claim of global fundamental reversibility is made for the accessible
   Paper 13D fusion channel.

## 8. Coherent probe stage

For mode input `j`, define the both-route probe by

\[
 V_{\phi,X}
 =(R D_\phi\otimes I)
 U_{Q,X}^{-1}U_{Q,X}
 (R\otimes I),
\]

with route filters, stable route record, classical record erasure, and
coherent unrecording inserted exactly as in Paper 21.

The complete probe reader includes all structural and complement fields. A
successful ideal probe must place probability one on their common blank
value before reporting the `0/1` mode marginal.

Every Paper 21 filter, record, visibility, and Barandes restart result must be
recovered without fitting a new table.

## 9. Post-recombination commit stage

After recombination, the output mode controls one instrument component:

\[
 \mathcal I_{T,X}:X\longrightarrow\mathsf Y_{T,X},
 \qquad
 \mathcal I_{F,X}:X\longrightarrow\mathsf Y_{F,X}.
\]

The `T` component must recover the accepted tensor child law. The `F`
component must recover the accepted simultaneous fusion child law, including
full orbit pushforward of all cross-pair outcomes.

The full measurement/process dilation may retain an explicit apparatus
complement and stable outcome record. The accessible conditioned child may
not contain an active copy of the unchosen child. Conditioning on `T` or `F`
must recover the corresponding accepted child future exactly.

The parent joint law must have the form

\[
 \widehat\Gamma_{\phi,X}(m,H\mid j)
 =C_\phi(m\mid j)\,\Gamma_m(H\mid X),
 \qquad m\in\{T,F\},
\]

only if this factorization follows from the one constructed instrument rather
than being imposed as an independent selector table.

## 10. Physical process fibers

The parent is a quantum/stochastic instrument: a family of outcome-indexed
transformations whose sum is normalized. The history bundle is the dependent
sum of the complete `T` and `F` component histories.

The process-outcome map must retain the instrument component, target type,
and complete child history. It may not infer the process class from a final
bit through an untyped decoder.

The paper must decide explicitly whether these are inequivalent
whole-process fibers in the sense required by Paper 20, or only target
configuration fibers. This coordinate cannot be awarded by terminology.

## 11. Point-free naturality

For every presentation isomorphism `g:X->X'`, require naturality of:

- the active mark and spectator split;
- tensor and fusion child functors;
- the query dilations and their inverses;
- seed purification and complete seed pushforward;
- filters, phase operation, and mode record;
- commit components;
- complete readers; and
- every conditional child future.

No probability may depend on component enumeration, occurrence labels, seed
exposure order, representative choice, or automorphism count. When multiple
seed values descend to one physical child, their probabilities are summed;
representative mass is forbidden.

## 12. Restriction, spectators, and composition

The candidate must test:

1. rooted spectator invariance;
2. deletion/restriction of occurrences and cross-pair seeds;
3. deletion that empties a component;
4. collapse of `T/F` distinction after restriction;
5. tensoring two disjoint instruments;
6. fusion of disjoint marked active families; and
7. composition with every accepted child future.

An autonomous schedule for repeated opportunities is not supplied by these
local composition laws and must remain unconstructed.

## 13. Required theorems

1. Typed source and dependent-output totality.
2. Operational tensor/fusion distinction.
3. No-hiding/no-reversible-erasure theorem.
4. Query-unitarity and exact inverse closure.
5. Minimal orthogonal-lift theorem for `R`.
6. Exact Paper 21 probe recovery.
7. Stable-record classicalization.
8. Classical-erasure/coherent-unrecord separation.
9. Normalized two-component instrument theorem.
10. Exact conditioned Paper 13D child recovery.
11. No-dormant-unchosen-child theorem.
12. Point-free naturality.
13. Rooted spectator invariance.
14. Restriction/deletion compatibility.
15. Process-fiber classification.
16. Activity/root-law noninheritance.
17. Paper 17 gate adjudication.

## 14. Hostile controls

1. `T/F` are renamed output bits with no middle structural witness.
2. The fusion query drops the source partition while claiming reversibility.
3. A hidden complement retains route information at recombination.
4. A purification seed is silently traced before the inverse.
5. The query inverse restores the visible witness but not its environment.
6. The accepted eraser is misused as an inverse fusion.
7. Classical deletion is called coherent unrecording.
8. Separate parent probabilities are assigned to the two components.
9. `R` is used without proving the minimal lift and gauge freedom.
10. A downstream result selects the route phase.
11. The route phase directly changes fusion seed probabilities.
12. Filters change the common source or final reader.
13. Blocked probability is renormalized away.
14. The final `T/F` correspondence is swapped without changing the physical
    controlled commit.
15. Both child structures are retained in a product output.
16. The unchosen child is hidden as active apparatus memory.
17. The reversible complement is exposed to accepted child futures, changing
    conditional recovery.
18. Seed representatives are counted instead of physical orbit mass.
19. An automorphism changes the route odds.
20. Spectators change local odds.
21. Deletion creates or destroys probability.
22. Two local instruments are serialized and the loop order is called time.
23. The triggered instrument is called an autonomous activity law.
24. The input source is called a selected cosmological root.
25. A local branch family is called a varying-size universe ensemble.
26. Target plurality is called whole-process plurality without testing the
    process map.
27. A finite Hilbert carrier is called a fundamental discrete ontology.
28. A complex representation is called ontologically primary.
29. The instrument is used to select dimension or geometry.
30. A successful local instrument is said to complete Paper 17.

## 15. Outcome product

```text
P22-TYPED-STRUCTURAL-INSTRUMENT-UNCONSTRUCTED / CONSTRUCTED
P22-REVERSIBLE-STRUCTURAL-QUERY-UNCONSTRUCTED / CONSTRUCTED
P22-REVERSIBLE-ERASING-FUSION-POSSIBLE / IMPOSSIBLE
P22-STRUCTURAL-PROBE-INTERFERENCE-UNCONSTRUCTED / CONSTRUCTED
P22-DEPENDENT-STRUCTURAL-COMMIT-UNCONSTRUCTED / CONSTRUCTED
P22-CONDITIONED-PAPER13D-CHILD-RECOVERY-UNCONSTRUCTED / CONSTRUCTED
P22-NO-DORMANT-UNCHOSEN-CHILD-UNPROVEN / PROVED
P22-POINT-FREE-NATURALITY-UNCONSTRUCTED / CONSTRUCTED
P22-RESTRICTION-AND-SPECTATOR-LAWS-UNCONSTRUCTED / CONSTRUCTED
P22-INEQUIVALENT-PROCESS-FIBERS-UNCONSTRUCTED / CONSTRUCTED
P22-AUTONOMOUS-ACTIVITY-LAW-UNCONSTRUCTED / CONSTRUCTED
P22-ROOT-LAW-UNCONSTRUCTED / CONSTRUCTED
P22-P17-STRUCTURAL-PARENT-GATE-CLOSED / OPEN
P22-P17-VARYING-HISTORY-ENSEMBLE-GATE-CLOSED / OPEN
P22-P17-CHRONOLOGY-DIMENSION-GATE-CLOSED / OPEN
P22-ACTUALIZATION-UNCONSTRUCTED / CONSTRUCTED
P22-METRIC-UNCONSTRUCTED / CONSTRUCTED
```

The product is dependency aware. A successful query does not automatically
award commit, child recovery, process plurality, activity, or Paper 17.

## 16. Stop rules

A semantic rejection occurs if:

- fusion erasure is called reversible without an explicit complement;
- any complement remains at coherent recombination;
- conditioned child laws differ from Paper 13D;
- child identity is a naked decoder rather than predictive behavior;
- presentation changes alter probabilities;
- the complete instrument is not normalized; or
- a downstream desired dimension fixes an upstream choice.

Code, serialization, performance, or formatting defects are not scientific
counterexamples. No implementation is authorized by this pin.

## 17. Permanent walls

The candidate may construct a local triggered instrument. It may not thereby
claim:

- that the instrument occurs autonomously;
- that its source is cosmologically selected;
- that its phase is a law constant;
- that one branch becomes actual;
- that repeated use has a covariant opportunity law;
- that an operational chronology is complete;
- that a dimension, signature, scale, topology, metric, curvature, or gravity
  is selected; or
- that finite typed carriers are fundamental discrete spacetime atoms.
