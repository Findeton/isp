# Paper 21 preparatory investigation

## Structural recombination in an enlarged indivisible stochastic parent

Date: 2026-08-21

Status: **PHYSICS-FIRST, RESULT-NEUTRAL INVESTIGATION — NO IMPLEMENTATION**

## Abstract

Paper 20 constructed a common-parent type and showed that the accepted
Paper 13D law already induces a point-free distribution over predictive target
configurations. It also proved that the same law has a Dirac marginal on
whole-process architecture. This note investigates the next discriminator:
if a future parent law genuinely contains alternative process structures,
what experiment would establish whether those alternatives combine as
ordinary stochastic branches or exhibit structural interference?

The Barandes and Feynman viewpoints can be reconciled without assuming that
complex amplitudes are fundamental. Feynman's physical distinction is between
alternatives that remain distinguishable and alternatives that can recombine.
Barandes identifies interference directly in ordinary stochastic language as
the discrepancy between a complete indivisible law and every positive law
obtained by inserting an intermediate stochastic division. The joint
criterion therefore requires both a typed recombination experiment and a
failure of positive factorization. A Hilbert-space or amplitude
representation is secondary.

The investigation yields four main results.

1. A precise finite stochastic recombination witness is available without
   complex amplitudes.
2. A stable route record forces classical summation throughout the
   record-preserving grammar; stable outcomes and coherent routes are not the
   same coordinate.
3. Erasing a record does not by itself restore interference. Recoherence is a
   new property of the complete erased experiment.
4. The accepted Gamma already supplies an exact configuration-level
   calibration of this architecture, but it contains no analogous parent,
   filters, or recombiner for inequivalent whole-process structures.

Consequently this investigation does not yet unblock global Paper 17. It
defines exactly what must be built and how a genuinely quantum structural
claim would be discriminated from an arbitrary stochastic wrapper.

## 1. Bound scope

This investigation binds:

| artifact | role | ordinary SHA-256 |
|---|---|---|
| `v16/paper-13d-typed-executable-gamma.md` | accepted typed indivisible law | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` |
| `v16/paper-20-predictive-structural-parent.md` | common-parent and predictive-quotient result | `64111d7764bf70984b959e00bc1da30ad0d6c3ae7b5c6d51b94227ad2f5c35e6` |
| `v16/note-paper20-predictive-structural-parent-adjudication.md` | internal Paper 20 scope | `18ea13e2bd609439d2cb4e2a03c1f0c4f0fbf7e37e2e38bba15272570001ac14` |

Paper 20 has nonblind internal acceptance only. Nothing here promotes its
review status.

No Paper 17 output, dimension statistic, geometry, parameter fit, source code,
or generated case is used.

## 2. The question

Let one physical preparation admit two candidate structural routes, `A` and
`B`, which later feed a common complete output interface. The question is not
merely whether a probability distribution can be written over the labels.
It is:

> Does one independently fixed indivisible law assign a direct final law that
> cannot be reproduced by any lawful positive restart through the proposed
> structural-route variable, and can the alternatives be physically filtered,
> recorded, and recombined within one covariant experiment family?

Three claims must remain separate:

1. **structural selection:** one stable process outcome is realized;
2. **structural nondivision:** a proposed intermediate structural variable is
   not a lawful stochastic restart point; and
3. **structural interference:** a controlled recombination/filter experiment
   exposes nonclassical additivity relative to that same physical family.

Nondivision does not automatically construct the filters. A nonzero
cross-context residual does not automatically prove nondivision. A complete
claim requires both routes of evidence.

## 3. Minimal typed experiment family

### 3.1 Common preparation and final effect

Freeze one complete source type `S`, preparation `s`, final target type `T`,
and complete equivariant reader `R`. The reader outcome space includes an
explicit loss/refusal value `bottom`. This ensures that blocking a route
produces a subnormalized detection measure inside one normalized complete
experiment, rather than silently renormalizing the surviving events.

Let `E` be any measurable final reader event not containing `bottom`.

### 3.2 Physical route filters

The family requires physical filters

\[
 F_{AB},\quad F_A,\quad F_B,\quad F_\varnothing,
\]

where `F_AB` leaves both routes available, `F_A` blocks only `B`, `F_B`
blocks only `A`, and `F_empty` blocks both. They must be typed interventions
on the same complete apparatus, not four unrelated kernels assigned after the
fact.

The filter algebra must satisfy the intended intersection laws on complete
physical states. At minimum,

\[
 F_A F_B=F_B F_A=F_\varnothing,
 \qquad
 F_A F_{AB}=F_A,
 \qquad
 F_B F_{AB}=F_B.
\tag{1}
\]

Any disturbance outside the declared filtered route must be retained in the
complete target and tested. A source-intensity change, postselection, or
context-specific normalization invalidates the interference comparison.

### 3.3 Route-record and erased controls

The family also requires:

- a recorded experiment `Sigma_rec` that writes a distinguishable stable
  route record `r in {A,B}`;
- a record-preserving future grammar;
- an eraser experiment `Sigma_erase` outside that grammar; and
- a complete erased-target reader.

The eraser is a control, not a theorem of recoherence.

### 3.4 Common-parent requirement

Every context must be a declared intervention or restriction of one frozen
parent experiment family. Merely listing four normalized probability tables
is insufficient, because any desired interference pattern can be encoded as
context dependence.

## 4. Feynman operational witness

For a common preparation and final event `E`, define the unrenormalized
detection probabilities

\[
 p_X(E)
 =\Gamma(R\in E\mid s,F_X),
 \qquad
 X\in\{AB,A,B,\varnothing\}.
\]

The exact second-order filter residual is

\[
 I_2(E)
 =p_{AB}(E)-p_A(E)-p_B(E)+p_\varnothing(E).
\tag{2}
\]

### Proposition 1 — classical exclusive-route additivity

If the filtered family differs only by removal of two mutually exclusive
classical route contributions and retains a common background contribution,
then `I_2(E)=0` for every final event.

#### Proof

Write

\[
 p_{AB}=p_0+p_A^{\rm route}+p_B^{\rm route},
 \quad
 p_A=p_0+p_A^{\rm route},
 \quad
 p_B=p_0+p_B^{\rm route},
 \quad
 p_\varnothing=p_0.
\]

Substitution in equation (2) cancels every term. \(\square\)

A nonzero `I_2` is therefore a Feynman-style operational interference
witness after the filter-consistency duties pass. By itself it does not prove
that a fundamental complex amplitude exists.

### 4.1 Three-route held-out control

For three routes, define

\[
\begin{split}
 I_3(E)={}&p_{ABC}(E)-p_{AB}(E)-p_{AC}(E)-p_{BC}(E)\\
          &+p_A(E)+p_B(E)+p_C(E)-p_\varnothing(E).
\end{split}
\tag{3}
\]

Ordinary complex-amplitude quantum mechanics with ideal filters has
second-order interference but no irreducible third-order term. A future
structural quantum claim should therefore freeze equation (3) as a held-out
control. `I_3=0` constrains a supplied law; it does not select its state or
amplitudes.

## 5. Barandes stochastic witness

### 5.1 Direct and divided laws

Let `B(lambda|s)` be the experimentally calibrated source-to-route matrix in
the recorded control, and let

\[
 C(z\mid s)
\]

be the direct source-to-final transition law of the unrecorded recombination
experiment.

A lawful stochastic restart at the structural cut would require a stochastic
matrix `K(z|lambda)` such that

\[
 C=KB.
\tag{4}
\]

The route is natively indivisible when no such positive normalized `K`
exists on the complete declared carrier.

For finite carriers define the exact distance to divisibility

\[
 \delta_{\rm div}(C,B)
 =\min_{K\in\mathsf{Stoch}}
   \max_s\frac12\sum_z|C_{zs}-(KB)_{zs}|.
\tag{5}
\]

Then `delta_div>0` is a quantitative nondivision certificate. Enlarging the
carrier, adding a history identifier, or changing the experiment gives a
different claim and must be declared before evaluation.

### Proposition 2 — invertible-cut certificate

If `B` is square and invertible, equation (4) has the unique algebraic
candidate

\[
 K=CB^{-1}.
\]

The proposed cut is not a positive stochastic division whenever this matrix
has a negative entry or fails normalization.

#### Proof

Right multiplication by `B^{-1}` gives uniqueness. Every lawful finite
conditional-probability matrix is entrywise nonnegative and column
normalized. \(\square\)

### 5.2 Joint promotion rule

Call a result **operational structural interference** only when:

1. the filter family is physically coherent and equation (2) is nonzero for
   a preregistered complete event; and
2. the direct law fails positive factorization through the same proposed
   structural-route carrier.

The first condition supplies Feynman's recombination evidence. The second
supplies Barandes's indivisible-stochastic content. Requiring both rejects a
contextual collection of unrelated probability tables and a purely algebraic
negative-kernel calculation with no physical route experiment.

## 6. Stable records and interference are complementary coordinates

### Theorem 1 — stable-record classicality inside the stable grammar

Suppose the route record `r` is perfectly readable, its sectors are disjoint,
and every licensed future preserves those sectors. Then every coarse final
event satisfies

\[
 P(E)=\sum_r P(E\mid r)P(r).
\tag{6}
\]

No lawful stable-grammar reader is sensitive to a relative phase between the
route sectors.

#### Proof

The stable record partitions the complete outcome space into disjoint
measurable sectors. The ordinary law of total probability gives equation
(6). Sector-preserving futures and readers have no cross-sector effect.
\(\square\)

Thus a **stable structural outcome** and an **unrecorded coherent structural
route** are not the same object. A happening may become stable after the
recombination opportunity has closed, but it cannot remain a perfectly
distinguishable route and simultaneously interfere under the same
record-preserving future grammar.

### Theorem 2 — forgetting is not recoherence

Let a deterministic eraser map every recorded pair `(r,z)` to the same
record-free value `z`. Its probability law is

\[
 P_{\rm erase}(z)=\sum_r P(r,z).
\tag{7}
\]

This operation cannot create an interference cross term absent from the
recorded joint law.

#### Proof

Equation (7) is the ordinary pushforward of a positive measure under a
many-to-one map. It sums existing masses and contains no additional signed or
phase-sensitive term. \(\square\)

Recoherence after erasure is possible only if the complete erased experiment
has a separately defined indivisible law whose final probabilities differ
from equation (7). Erasure is necessary in some laboratory designs but never
sufficient by itself.

## 7. Exact two-state calibration

The accepted Paper 13D matrices at `g=1/2` are

\[
 B=\frac1{25}
 \begin{pmatrix}9&16\\16&9\end{pmatrix},
 \qquad
 C=\frac1{625}
 \begin{pmatrix}49&576\\576&49\end{pmatrix}.
\tag{8}
\]

The recorded two-step law is

\[
 B^2=\frac1{625}
 \begin{pmatrix}337&288\\288&337\end{pmatrix}.
\tag{9}
\]

The direct-minus-recorded residual is

\[
 C-B^2
 =\frac1{625}
 \begin{pmatrix}-288&288\\288&-288\end{pmatrix}.
\tag{10}
\]

The unique putative continuation through the intermediate two-state carrier
is

\[
 CB^{-1}
 =\frac1{175}
 \begin{pmatrix}351&-176\\-176&351\end{pmatrix}.
\tag{11}
\]

Its negative entries prove native nondivision.

This is already a complete Barandes-style stochastic interference
calibration. Its intermediate alternatives are configuration alternatives
inside one accepted primitive process. Renaming them `tensor` and `fusion`
would not turn equation (11) into structural-process interference.

## 8. Exact phase-shifter discriminator template

The real amplitude representative

\[
 R=\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix}
\]

suggests a useful held-out template. Insert a physically controlled relative
phase

\[
 D_\phi=\operatorname{diag}(1,e^{i\phi})
\]

between two occurrences of `R`. The resulting ordinary stochastic endpoint
law is

\[
 C_\phi=|R D_\phi R|^2
 =\frac1{625}
 \begin{pmatrix}
 337-288\cos\phi&288(1+\cos\phi)\\
 288(1+\cos\phi)&337-288\cos\phi
 \end{pmatrix}.
\tag{12}
\]

It has three exact controls:

\[
 C_0=C,
 \qquad
 \langle C_\phi\rangle_{\langle\cos\phi\rangle=0}=B^2,
 \qquad
 C_\pi=I.
\tag{13}
\]

Equation (12) is not imported into the accepted theory. A structural
phase-shifter must be an independently typed physical operation, and all
values of `phi` must be predicted by one frozen law. Without that operation,
equation (12) is only an amplitude representation chosen after the stochastic
law.

### Proposition 3 — a fringe does not make amplitudes ontologically primary

Even if a physical family realizes equation (12), its observed probabilities
are an ordinary family of stochastic matrices. The phase representation is
physically useful because it compresses and predicts the family, but the
probability data alone do not prove that complex amplitudes are the primitive
ontology.

This is the Barandes correction to a naive Feynman reading. The decisive
physics is the complete indivisible family and its noncommuting or
phase-sensitive controls, not the decorative attachment of square roots to
one probability table.

## 9. When the word quantum is earned

A structural parent should be promoted beyond a generic indivisible
stochastic law only after all of the following are supplied.

1. One shared lift or stochastic-quantum representation covers every source,
   filter, phase control, reader, tensor, and composition context.
2. The lift makes held-out predictions not already inserted as independent
   context tables.
3. A physical structural phase operation changes final statistics as
   predicted.
4. A route record removes the residual and a separately tested recoherence
   operation can restore it.
5. Three-route or higher controls satisfy the declared quantum interference
   hierarchy.
6. The state or boundary condition is frozen independently of the observed
   fringe.

Complex amplitudes are then an exceptionally effective representation of the
whole physical law. This still does not prove that the amplitudes are the
fundamental ontology.

## 10. What recombination can and cannot select

Structural interference constrains the joint parent law. It can reject:

- independently normalized branch tables;
- a selector bit with no filters;
- arbitrary branch phases with no phase shifter;
- a classical checkpoint imposed at a nondivision;
- a record eraser advertised as automatic recoherence; and
- amplitudes fitted independently in every context.

It does not by itself select:

- the initial structural state;
- the activity rate of the parent opportunity;
- a cosmological root law;
- the number of structural channels;
- the physical phase-shifter Hamiltonian;
- a dimension, geometry, or metric; or
- which outcome becomes actual.

This is where the Barandes separation between stochastic dynamics and an
initial probability distribution remains important. A complete physical
model may legitimately contain both an indivisible structural law and an
independently prepared or cosmological structural state.

## 11. Current-Gamma audit

### 11.1 What is present

The accepted Gamma supplies:

1. the exact direct law `C`;
2. the exact proposed-cut law `B`;
3. the exact recorded/divided control `B^2`;
4. the negative unique continuation (11);
5. stable record sectors under a declared future grammar;
6. an executable eraser outside that grammar; and
7. point-free complete readers.

This is enough to calibrate configuration-level stochastic interference,
record stability, and erasure as separate coordinates.

### 11.2 What is absent

The accepted Gamma does not supply:

1. two inequivalent whole-process routes inside one parent;
2. structural route filters `F_A,F_B`;
3. a structural record-writing version of that same parent;
4. a structural recombiner;
5. a physical structural phase shifter;
6. a recoherence experiment after structural record erasure; or
7. a probability law over repeated varying-size process architectures.

Therefore the exact Paper 13D interference control cannot be promoted by
renaming its intermediate configurations as process structures.

## 12. The smallest honest next construction

The next construction should be one typed structural interferometer with:

\[
 \text{common source}
 \longrightarrow
 \{A,B\}\text{ structural opportunity}
 \longrightarrow
 \text{common final interface}.
\]

It must include, from the beginning:

1. an unmarked primitive both-route law;
2. two physical route blockers and a double-block control;
3. a route-marking apparatus with a stable complete record;
4. a record-preserving final reader;
5. a separate eraser experiment;
6. a proposed recoherence operation;
7. one common complete loss outcome;
8. point-free transport of every mark and reader;
9. exact tensor-spectator controls;
10. exact child-future recovery;
11. a varying-size/projective extension only after the finite experiment
    passes; and
12. no Paper 17 output in its construction or parameter choice.

A record-controlled choice between tensoring and fusion would be a useful
laboratory calibration of the parent type. It would not yet be a cosmological
selector, because the control coupling and initial record preparation would
remain apparatus data.

## 13. Hostile controls

Any successor must kill or classify at least these controls.

1. Four unrelated context tables imitate a nonzero `I_2`.
2. Blocking a route changes source intensity and is then renormalized.
3. A hidden postselection variable creates an apparent fringe.
4. The two filters act on different target readers.
5. Route labels are serialization indices rather than physical addresses.
6. A coarse reader hides filter disturbance in another field.
7. The route mark is erasable but was never stable.
8. A stable record is retained while interference is nevertheless claimed.
9. Erasure is treated as recoherence without evaluating the erased law.
10. A positive continuation exists on the complete carrier but is missed on a
    coarse two-state carrier.
11. A negative continuation is repaired by adding a hidden history identifier
    after seeing the result.
12. The structural routes have identical complete future behavior.
13. An accepted configuration alternative is merely renamed as a process
    architecture.
14. Square-root amplitudes are fitted independently to each context.
15. Relative phases exist but no operation changes them.
16. A phase shifter changes unrelated apparatus fields.
17. A classical context variable reproduces the fringe and is not tested by
    composition constraints.
18. A direct-sum dilation supplies dormant unchosen hardware.
19. The recorded experiment changes the route dynamics beyond writing a
    record, without that change being retained.
20. A downstream dimension fit chooses the phase, state, or parent law.
21. A two-route quantum claim fails a held-out three-route `I_3` control.
22. An isomorphic tensor spectator changes local route odds.
23. Presentation relabeling changes the fringe.
24. Representative mass replaces orbit mass.
25. The initial structural state is silently absorbed into the dynamics.
26. A one-shot laboratory switch is promoted to a cosmological activity law.
27. A structural activity law is promoted to actualization.
28. Nondivision is promoted to geometry or time direction.
29. Finite route labels are promoted to a discrete ontology.
30. The experiment has no extension to repeated or varying-size histories.

## 14. Decision ladder

```text
P21-STRUCTURAL-PARENT-UNCONSTRUCTED
P21-STRUCTURAL-FILTER-FAMILY-CONSTRUCTED
P21-STRUCTURAL-NONDIVISION-CONSTRUCTED
P21-STRUCTURAL-RECORDED-DIVISION-CONSTRUCTED
P21-STRUCTURAL-ERASURE-CONSTRUCTED
P21-STRUCTURAL-RECOHERENCE-UNCONSTRUCTED
P21-OPERATIONAL-STRUCTURAL-INTERFERENCE-CONSTRUCTED
P21-SHARED-STOCHASTIC-QUANTUM-LIFT-CONSTRUCTED
P21-FUNDAMENTAL-COMPLEX-AMPLITUDE-UNPROVEN
P21-STRUCTURAL-INITIAL-STATE-UNSELECTED
P21-VARYING-SIZE-STRUCTURAL-LAW-UNCONSTRUCTED
P21-P17-GLOBAL-GATE-CLOSED
P21-ACTUALIZATION-UNCONSTRUCTED
P21-METRIC-UNCONSTRUCTED
```

The current investigation itself supports the more conservative vector:

```text
P21-BARANDES-STOCHASTIC-INTERFERENCE-CRITERION-CONSTRUCTED
P21-FEYNMAN-FILTER-INTERFERENCE-CRITERION-CONSTRUCTED
P21-RECORD-INTERFERENCE-COMPLEMENTARITY-CONSTRUCTED
P21-ERASURE-RECOHERENCE-DISTINCTION-CONSTRUCTED
P21-EXACT-TWO-STATE-CALIBRATION-CONSTRUCTED
P21-CURRENT-GAMMA-CONFIGURATION-INTERFERENCE-CALIBRATION-PRESENT
P21-CURRENT-GAMMA-STRUCTURAL-PROCESS-ALTERNATIVES-UNCONSTRUCTED
P21-CURRENT-GAMMA-STRUCTURAL-RECOMBINER-UNCONSTRUCTED
P21-QUANTUM-STRUCTURAL-PARENT-UNCONSTRUCTED
P21-STRUCTURAL-INITIAL-STATE-UNSELECTED
P21-P17-GLOBAL-GATE-CLOSED
P21-ACTUALIZATION-UNCONSTRUCTED
P21-METRIC-UNCONSTRUCTED
```

## 15. Literature boundary

- Jacob Barandes, *The Stochastic-Quantum Correspondence*:
  https://arxiv.org/abs/2302.10778
- Jacob Barandes, *Quantum Systems as Indivisible Stochastic Processes*:
  https://arxiv.org/abs/2507.21192
- Feynman, Leighton, and Sands, *The Feynman Lectures on Physics*, Vol. III,
  Chapter 3: https://www.feynmanlectures.caltech.edu/III_03.html
- Rafael Sorkin, *Quantum Mechanics as Quantum Measure Theory*:
  https://arxiv.org/abs/gr-qc/9401003
- Murray Gell-Mann and James Hartle, *Strong Decoherence*:
  https://arxiv.org/abs/gr-qc/9509054
- J. J. Halliwell, *A Review of the Decoherent Histories Approach to Quantum
  Mechanics*: https://arxiv.org/abs/gr-qc/9407040

The Barandes sources support the interpretation of interference as a failure
of stochastic divisibility and Hilbert space as a secondary representation.
Feynman supplies the physical distinguishability/recombination criterion.
Sorkin supplies the interference hierarchy. Decoherent-histories work
supports the distinction between stable generalized records and coherent
alternative histories. None of these sources supplies the missing ISP
structural parent, filters, state, or activity law.

## 16. Conclusion

The Barandes-Feynman combination is coherent and sharper than either an
arbitrary selector bit or a premature sum over structures.

The primitive object should be one complete positive indivisible stochastic
law on an enlarged structural experiment family. Feynman-style filters and a
recombination apparatus make the routes physical. Barandes-style
nonfactorization establishes interference without requiring complex
amplitudes as ontology. A shared Hilbert representation becomes useful only
after it predicts the whole family, including held-out phase and record
controls.

The accepted Gamma already proves that this architecture works for
configuration alternatives. It does not yet contain structural-process
alternatives. The next genuinely new physics is therefore a typed structural
interferometer, not another probability formula and not an implementation.

Even a successful structural interferometer would constrain the parent law
rather than select the cosmological initial state. Global Paper 17 reopens
only after a repeated varying-size whole-process law is independently fixed,
or after the desired result is proved invariant over its remaining state-law
residue.
