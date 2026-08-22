# An exact structural interferometer

## Recombination, records, and indivisible relational laws

### Abstract

This paper executes the smallest exact experiment capable of distinguishing
three claims that have repeatedly been conflated:

1. two alternatives belong to one common parent experiment;
2. their filter probabilities contain a Feynman interference term; and
3. the direct stochastic law is indivisible through the proposed
   intermediate carrier in the sense used by Barandes.

The two routes are operationally different structural transformations. One
retains a tensor decomposition and the other produces a fusion witness. They
are embedded in one reversible enlarged experiment, independently filterable,
and returned to one common final interface before readout. The route mixer is
the exact Paper 13D calibration

\[
 R=\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix}.
\]

With a relative phase `phi`, the common-parent law is

\[
 C_\phi=|R D_\phi R|^2
 =\frac1{625}
 \begin{pmatrix}
 337-288\cos\phi&288(1+\cos\phi)\\
 288(1+\cos\phi)&337-288\cos\phi
 \end{pmatrix}.
\]

The exact four-filter residual is nonzero at `phi=0` and `phi=pi`, changes
sign between them, and vanishes at `phi=pi/2`. A stable orthogonal route record
removes the phase dependence and gives the classical law `B^2`. Merely
resetting or discarding the record does not restore the phase dependence;
coherently reversing the record interaction does.

The Barandes restart test supplies an independent result. The unique candidate
in `C_phi=K_phi B` is

\[
 K_\phi=\frac1{175}
 \begin{pmatrix}
 63+288\cos\phi&112-288\cos\phi\\
 112-288\cos\phi&63+288\cos\phi
 \end{pmatrix}.
\]

It is stochastic exactly when

\[
 -\frac7{32}\leq\cos\phi\leq\frac7{18}.
\]

Thus Feynman filter interference and stochastic nondivision are related but
not identical diagnostics. At `phi=0` and `phi=pi` both are present; at
`phi=pi/2` neither is present; in part of the intervening phase range the
filter residual is nonzero although a positive restart kernel exists.

The abstract structural interferometer is therefore constructed. The accepted
Paper 13D law does not yet instantiate it: its fusion generator has no accepted
inverse structural dilation, and it has no route-phase operation or common
structural recombiner. This is a positive design result and an exact negative
instantiation result. It does not select a cosmological structure, reopen
Paper 17, or construct chronology, dimension, metric, or gravity.

## 1. Frozen status

This exact evaluation is governed by

`v16/note-paper21-structural-interferometer-pin.md`

with ordinary SHA-256

`7df73538f87a39e22a4aa221d4c94842620fb7c8329e68d072ea98a7c7e9f9f7`.

The pin was frozen before the calculations below. It fixes:

- the route meanings;
- the common source and complete reader;
- the matrix `R`;
- the phases `0`, `pi/2`, and `pi`;
- the four route-filter contexts;
- the four record contexts;
- the factorization test;
- twenty hostile controls; and
- a result-neutral outcome product.

No parameter, phase, route meaning, or outcome coordinate was selected after
evaluation. The experiment is exact mathematical physics, not a laboratory
measurement or numerical simulation.

## 2. One common typed experiment

### 2.1 Route carrier

Let the route space have orthonormal basis

\[
 |T\rangle,\qquad |F\rangle.
\]

The route names mean:

- `T`: a tensor-preserving structural operation whose middle witness retains
  the declared two-component partition;
- `F`: a fusion-changing structural operation whose middle witness has a
  fresh cross-component relation and no longer has that partition as a
  physical factorization.

These meanings are checked by a complete middle reader. They are not two
names for the same bit value.

### 2.2 Reversible structural dilation

Let `W` be an enlarged witness space containing distinguishable states

\[
 |w_0\rangle,\quad |w_T\rangle,\quad |w_F\rangle.
\]

Choose exact bijections, represented here by permutation unitaries,

\[
 U_T|w_0\rangle=|w_T\rangle,
 \qquad
 U_F|w_0\rangle=|w_F\rangle.
\]

They may be completed arbitrarily on the unused basis values so long as the
full maps are bijections. The controlled structural operation is

\[
 U_{\rm str}
 =|T\rangle\!\langle T|\otimes U_T
  +|F\rangle\!\langle F|\otimes U_F.
\tag{1}
\]

While the routes are open, the middle reader distinguishes `w_T` from `w_F`.
Before recombination, the experiment applies `U_str^{-1}`. Consequently both
transmitted routes return the structural witness, all reversible ancillas,
and every unrecorded environment field to the same `w_0` value.

This is the essential physical condition. If any uncontrolled environment
retains a route-dependent state, the experiment belongs to the partial-record
family of Section 7 rather than the fully coherent context.

### 2.3 Why this is not a dormant lattice

The enlarged witness space is the carrier of one finite intervention. It is
not asserted to be a fundamental web of simultaneously existing structures.
Only one common source, two alternative transformations, and their reversible
apparatus are represented. The construction neither supplies a cosmological
state space nor assigns occurrence probabilities to arbitrary structures.

### 2.4 Complete sequence

For input route value `j`, the experiment performs:

1. prepare `|j,w_0>` and blank record/environment fields;
2. apply `R` to the route carrier;
3. apply the controlled structural operation (1);
4. optionally filter or record the open route;
5. apply the controlled structural inverse on every transmitted route;
6. apply `D_phi=diag(1,e^{i phi})`;
7. coherently reverse the route record only in the coherently-unrecorded
   context;
8. apply the same `R` as the recombiner; and
9. read the complete outcome `{0,1,loss}`.

All four filter contexts use this one source, this one final reader, and this
one apparatus law.

## 3. Exact common-parent law

Write

\[
 c=\frac35,\qquad s=\frac45,
 \qquad
 R=\begin{pmatrix}c&-s\\s&c\end{pmatrix}.
\]

With

\[
 D_\phi=\begin{pmatrix}1&0\\0&e^{i\phi}\end{pmatrix},
\]

the coherent route amplitude is

\[
 A_\phi=R D_\phi R
 =\begin{pmatrix}
 c^2-s^2e^{i\phi}&-cs(1+e^{i\phi})\\
 cs(1+e^{i\phi})&-s^2+c^2e^{i\phi}
 \end{pmatrix}.
\tag{2}
\]

The ordinary stochastic law is obtained entrywise:

\[
 C_\phi(z\mid j)=|A_\phi(z,j)|^2.
\]

Using `c^2 s^2=144/625` gives

\[
 C_\phi
 =\frac1{625}
 \begin{pmatrix}
 337-288\cos\phi&288(1+\cos\phi)\\
 288(1+\cos\phi)&337-288\cos\phi
 \end{pmatrix}.
\tag{3}
\]

Every entry is nonnegative because `cos phi` lies in `[-1,1]`. Every column
sums to one. The special phases are

\[
 C_0=\frac1{625}
 \begin{pmatrix}49&576\\576&49\end{pmatrix},
\tag{4}
\]

\[
 C_{\pi/2}=\frac1{625}
 \begin{pmatrix}337&288\\288&337\end{pmatrix},
\tag{5}
\]

and

\[
 C_\pi=\begin{pmatrix}1&0\\0&1\end{pmatrix}.
\tag{6}
\]

The complex amplitude in (2) is a genuine quantum-style representation: the
relative phase changes observed probabilities. It is secondary in this paper.
The directly reported physical objects are the normalized stochastic laws
(3)–(6).

## 4. Exact filter experiment

### 4.1 Common preparation

Use input route `j=0`. After the first mixer, the route amplitudes are

\[
 \frac35|T\rangle+\frac45|F\rangle.
\]

Blocking a route transfers its norm to the orthogonal outcome `loss`. It does
not change the preparation and it is never followed by conditional
renormalization.

### 4.2 All contexts at arbitrary phase

With denominator `625`, the complete distributions are

| context | `p(0)` | `p(1)` | `p(loss)` |
|---|---:|---:|---:|
| both `AB` | `337-288 cos(phi)` | `288(1+cos(phi))` | `0` |
| `T` only | `81` | `144` | `400` |
| `F` only | `256` | `144` | `225` |
| empty | `0` | `0` | `625` |

Each row sums to `625`. The single-route rows are phase independent, as they
must be: no relative phase can be observed with only one transmitted route.

### 4.3 Exact Feynman residual

For each complete outcome define

\[
 I_2(z)=p_{AB}(z)-p_T(z)-p_F(z)+p_\varnothing(z).
\]

Then

\[
 I_2(0)=-\frac{288}{625}\cos\phi,
 \qquad
 I_2(1)=\frac{288}{625}\cos\phi,
 \qquad
 I_2({\rm loss})=0.
\tag{7}
\]

The preregistered phase table is therefore

| phase | `I2(0)` | `I2(1)` | `I2(loss)` |
|---|---:|---:|---:|
| `0` | `-288/625` | `288/625` | `0` |
| `pi/2` | `0` | `0` | `0` |
| `pi` | `288/625` | `-288/625` | `0` |

The residual conserves complete probability:

\[
 \sum_z I_2(z)=0.
\]

It is therefore a redistribution between detected outcomes, not a missing
normalization term. Its sign reversal under the frozen phase scan rules out a
fixed positive mixture of the two single-route laws.

## 5. Stable records and the classical division

### 5.1 Recorded route

Let a record interaction write orthogonal values

\[
 |T\rangle|0_R\rangle\mapsto|T\rangle|T_R\rangle,
 \qquad
 |F\rangle|0_R\rangle\mapsto|F\rangle|F_R\rangle,
\]

with

\[
 \langle T_R|F_R\rangle=0.
\]

If the record remains in every lawful future, tracing or ignoring it removes
the cross term. The one-step probability law is

\[
 B=|R|^2
 =\frac1{25}\begin{pmatrix}9&16\\16&9\end{pmatrix}.
\tag{8}
\]

The recorded final law is the positive classical composition

\[
 B^2=\frac1{625}
 \begin{pmatrix}337&288\\288&337\end{pmatrix}.
\tag{9}
\]

It is independent of `phi`. The filter residual is zero in every outcome:
the both-route detected row `(337,288)/625` equals the sum of the transmitted
parts `(81,144)/625+(256,144)/625`.

### 5.2 Classical erasure is not coherent unrecording

A deterministic reset of the visible record cannot erase information from a
closed reversible world. Some environment value must retain whether the old
record was `T_R` or `F_R`. Those environment states remain orthogonal, so the
final detected law remains (9).

Thus

\[
 C_{\rm classically\ erased}=B^2.
\tag{10}
\]

Discarding, coarse-graining, overwriting, or forgetting the record does not
restore the interference term.

### 5.3 Coherent unrecording

If the record interaction itself is reversed before any uncontrolled copy is
made, both record values return to the same blank state. The complete law is
then restored:

\[
 C_{\rm coherently\ unrecorded,\phi}=C_\phi.
\tag{11}
\]

Equations (10) and (11) are experimentally distinct. This is the precise
difference between deleting a classical log entry and reversing the physical
write interaction.

### 5.4 Direct-minus-recorded residual

At arbitrary phase,

\[
 C_\phi-B^2
 =\frac{288\cos\phi}{625}
 \begin{pmatrix}-1&1\\1&-1\end{pmatrix}.
\tag{12}
\]

At `phi=0`, the exact difference is

\[
 \frac1{625}
 \begin{pmatrix}-288&288\\288&-288\end{pmatrix}.
\]

This is the quantitative change in division structure produced by a stable
route record.

## 6. The independent Barandes restart test

### 6.1 Unique continuation

The intermediate configuration law (8) is invertible:

\[
 B^{-1}=\frac17
 \begin{pmatrix}-9&16\\16&-9\end{pmatrix}.
\tag{13}
\]

Consequently any factorization

\[
 C_\phi=K_\phi B
\]

has the unique candidate

\[
 K_\phi=C_\phi B^{-1}
 =\frac1{175}
 \begin{pmatrix}
 63+288\cos\phi&112-288\cos\phi\\
 112-288\cos\phi&63+288\cos\phi
 \end{pmatrix}.
\tag{14}
\]

Every column of (14) sums to one. Positivity requires both distinct entries
to be nonnegative:

\[
 63+288\cos\phi\geq0,
 \qquad
 112-288\cos\phi\geq0.
\]

Therefore a positive stochastic restart exists exactly when

\[
 -\frac7{32}\leq\cos\phi\leq\frac7{18}.
\tag{15}
\]

No other `K` can repair a failure of (15), because `B` is invertible.

### 6.2 Frozen phases

At `phi=0`,

\[
 K_0=\frac1{175}
 \begin{pmatrix}351&-176\\-176&351\end{pmatrix}.
\tag{16}
\]

At `phi=pi/2`,

\[
 K_{\pi/2}=\frac1{175}
 \begin{pmatrix}63&112\\112&63\end{pmatrix}
 =B.
\tag{17}
\]

At `phi=pi`,

\[
 K_\pi=\frac17
 \begin{pmatrix}-9&16\\16&-9\end{pmatrix}
 =B^{-1}.
\tag{18}
\]

The first and third candidates contain negative entries. The middle candidate
is a valid stochastic law and gives `C_{pi/2}=B^2`.

### 6.3 The two tests are not equivalent

The filter residual is nonzero whenever `cos(phi)` is nonzero. The restart
kernel is nonpositive only outside the interval (15). Hence there are phases
with

\[
 0<|\cos\phi|,
 \qquad
 -\frac7{32}\leq\cos\phi\leq\frac7{18},
\]

for which the Feynman residual is nonzero while a positive `K_phi` exists.

This does not contradict either diagnostic. They ask different questions:

- the filter residual compares four physical intervention contexts within
  one parent experiment;
- the restart test asks whether one direct endpoint law admits a positive
  factorization through a specified intermediate carrier.

The strongest joint result is therefore phase scoped. At `phi=0` and
`phi=pi`, the experiment exhibits both structural filter interference and
native stochastic nondivision. At `phi=pi/2`, it exhibits neither. In part of
the remaining phase range it exhibits filter interference without native
nondivision through `B`.

## 7. Partial route information

Let `|e_T>` and `|e_F>` be all residual witness, record, and environment states
immediately before recombination, and define

\[
 \gamma=\langle e_T|e_F\rangle,
 \qquad |\gamma|\leq1,
 \qquad q_\phi=\operatorname{Re}(\gamma e^{i\phi}).
\]

The complete reduced stochastic law is

\[
 C_{\phi,\gamma}
 =\frac1{625}
 \begin{pmatrix}
 337-288q_\phi&288(1+q_\phi)\\
 288(1+q_\phi)&337-288q_\phi
 \end{pmatrix}.
\tag{19}
\]

This formula includes:

- full unrecorded coherence: `gamma=1`;
- a perfect stable route record: `gamma=0`;
- classical erasure with an orthogonal environment trace: `gamma=0`;
- exact coherent unrecording: `gamma=1`; and
- imperfect structural uncomputation: `0<|gamma|<1`.

Scanning `phi`, detector `1` has visibility

\[
 \mathcal V_1
 =\frac{p_{\max}-p_{\min}}{p_{\max}+p_{\min}}
 =|\gamma|,
\tag{20}
\]

whereas detector `0` has

\[
 \mathcal V_0=\frac{288}{337}|\gamma|.
\tag{21}
\]

For full coherence these become `1` and `288/337`. For a stable orthogonal
record both vanish. The visibility is therefore a direct audit of residual
which-route information, not an independent postulate about collapse.

## 8. Presentation checks

### 8.1 Route-label swap

Swap `T` and `F` everywhere: in the controlled structural operations, filters,
record values, and phase convention. The two single-route rows exchange, while
their sum, the both-route law, the filter residual, the visibility, and the
factorization result remain unchanged. The physical predictions therefore do
not depend on which route is printed first.

### 8.2 Serialization

Changing the order in which the controlled blocks are stored does not change
the operator (1), because the route projectors are orthogonal. No loop index or
serialization position enters (2)–(21).

### 8.3 Complete outcome typing

All blocked norm is retained as `loss`; all stochastic matrices have complete
column sums; and no zero-probability output is deleted from the carrier. The
interference result is not an artifact of postselection.

## 9. Hostile-control results

| control | result | reason |
|---|---|---|
| route tags only | killed | the complete middle reader distinguishes `w_T,w_F` |
| irreversible fusion | kills current-Gamma instantiation | no coherent recombination is then defined |
| residual environment route record | moves to (19) | visibility falls with `|gamma|` |
| filter changes source | killed by construction | all contexts share input `j=0` |
| renormalized blocking | killed | loss is explicit |
| different final readers | killed | one `{0,1,loss}` reader is fixed |
| phase changes structural witness | killed | `D_phi` acts only on route |
| post-hoc phase | killed | three phases were frozen |
| hidden record in unrecorded context | killed | complete pre-recombination fields define `gamma` |
| erasure equals uncompute | killed | equations (10) and (11) differ |
| recorded law not classical | killed | exact law is `B^2` |
| positive continuation exists | detected exactly | condition (15) reports it rather than hiding it |
| post-hoc enlarged carrier | killed | the tested carrier is fixed as `B` |
| separately fitted amplitudes | killed | one `R,D_phi` generates all contexts |
| route-label dependence | killed | Section 8.1 |
| serialization route | killed | Section 8.2 |
| calibration renamed as process evidence | killed | current-Gamma audit remains separate |
| apparatus called selector | killed | no root or activity law is assigned |
| initial state selected | killed | preparation is an experimental input |
| chronology/geometry promotion | killed | permanent walls remain closed |

## 10. Current Paper 13D instantiation audit

### 10.1 What Paper 13D supplies

The accepted law supplies:

- the exact configuration mixer `R` and stochastic calibration `B`;
- the coherent two-step endpoint law `C_0`;
- a typed tensor operation;
- a physically distinct fusion operation;
- complete interventions and readers on its declared experiment carrier;
- stable records and a stable-future subcategory;
- an executable record eraser outside that stable subcategory; and
- the exact native nondivision witness (16).

These objects calibrate every number used in this experiment and provide
honest tensor-versus-fusion route meanings.

### 10.2 What Paper 13D does not supply

The accepted law does not contain:

1. a single coherent route carrier on which tensor and fusion are alternatives
   of one amplitude-level parent;
2. an accepted inverse or reversible dilation of physical fusion;
3. a route phase operation;
4. a common structural recombiner;
5. route filters whose blocked norm lands in one common loss sector; or
6. a theorem that every external environment field has been returned to one
   common value before recombination.

Its record eraser is deliberately a many-to-one future-boundary control. It is
not an inverse of fusion and not a quantum eraser for structural route
information.

### 10.3 Exact instantiation verdict

Therefore:

- the abstract structural interferometer is constructed;
- the current Paper 13D structural-route instantiation is unconstructed;
- the current Paper 13D reversible structural dilation is unconstructed; and
- current-Gamma structural interference is unconstructed.

This is not a failure of the accepted Paper 13D probabilities. It identifies
the precise additional physical law required for the common-parent program:
a typed, reversible, amplitude-sensitive structural instrument whose route
alternatives can be recombined without residual route information.

## 11. Interpretation

### 11.1 Feynman lesson

An amplitude decomposition becomes operationally meaningful only when the
alternatives can be opened, closed, and recombined inside one common setup.
Here those controls exist in the abstract experiment, and equation (7) is the
direct context comparison. The result is stronger than drawing two diagrams
and assigning them complex numbers independently.

### 11.2 Barandes lesson

The physical content may be stated entirely as ordinary transition
probabilities. At phases violating (15), the intermediate two-state
configuration is not a lawful restart point even though it appears in the
amplitude representation. When a stable route record is created, `B^2=BB`
becomes a lawful division. The record changes the permissible conditioning
structure; it does not merely add an inert label.

### 11.3 Joint lesson

Neither viewpoint may be used as a shortcut for the other. A filter residual
is a comparison across interventions. Nondivision is a factorization property
of a fixed direct law and carrier. A stable record can create a division, but
classical deletion of that record does not reconstruct coherence.

The exact experiment therefore supplies the discriminator sought after Paper
20. It does not yet supply the physical structural instrument to which that
discriminator must be applied.

## 12. Outcome product

```text
abstract structural interferometer
  P21-ABSTRACT-STRUCTURAL-INTERFEROMETER-CONSTRUCTED

four-filter common-parent response
  P21-FILTER-INTERFERENCE-CONSTRUCTED

Barandes restart test
  P21-STOCHASTIC-NONDIVISION-CONSTRUCTED
  (phase scoped by -7/32 <= cos(phi) <= 7/18)

stable record
  P21-STABLE-RECORD-CLASSICALIZATION-CONSTRUCTED

erasure versus uncomputation
  P21-ERASURE-RECOHERENCE-SEPARATION-CONSTRUCTED

partial route information
  P21-PARTIAL-COHERENCE-LAW-CONSTRUCTED

accepted Paper 13D route parent
  P21-CURRENT-GAMMA-STRUCTURAL-ROUTES-UNCONSTRUCTED

accepted Paper 13D reversible structural dilation
  P21-CURRENT-GAMMA-REVERSIBLE-STRUCTURAL-DILATION-UNCONSTRUCTED

accepted Paper 13D structural interference
  P21-CURRENT-GAMMA-STRUCTURAL-INTERFERENCE-UNCONSTRUCTED

structural root/activity law
  P21-STRUCTURAL-INITIAL-STATE-UNSELECTED

Paper 17 global chronology/dimension gate
  P21-P17-GLOBAL-GATE-CLOSED

metric
  P21-METRIC-UNCONSTRUCTED
```

## 13. What the next construction must do

The next physics object should not be another selector fitted to final
structures. It should be one typed structural instrument with:

1. a common preparation;
2. at least two operationally inequivalent structural routes;
3. a complete reversible dilation of every route;
4. route-local filters and a phase-sensitive control;
5. a common recombining interface and complete reader;
6. stable-record and coherent-unrecord controls;
7. a directly normalized stochastic law on every context;
8. point-free covariance under presentation changes; and
9. a derivation or independent physical motivation for its amplitude law.

Only after such an instrument is accepted may the experiment in this paper be
applied to the actual `Gamma` rather than to an exact calibrated candidate.
If it passes, it would establish that structural alternatives can participate
in one indivisible law. It would still not select a cosmological root or prove
that a generated family has chronology, dimension, or geometry.

## 14. Scope walls

This experiment does not prove:

- that tensor and fusion occur with the route weights `9/25` and `16/25` in
  nature;
- that Paper 13D fusion is reversible;
- that the amplitude `R D_phi R` is the fundamental structural law;
- that any one structural history is actual;
- that an ensemble of structures is selected;
- that stable happenings form a global clock;
- that a dimension is selected;
- that Lorentzian signature, scale, metric, curvature, or gravity emerges; or
- that an empirical apparatus currently implements the proposed structural
  transformations.

The strongest honest result is exact and narrower:

> A single reversible common-parent experiment can make tensor-preserving and
> fusion-changing structural alternatives interfere, can turn that
> interference into a classical division by writing a stable record, and can
> distinguish classical record deletion from genuine coherent uncomputation.
> The accepted Paper 13D law calibrates this construction but does not yet
> contain the reversible structural instrument needed to instantiate it.

## References

- Jacob A. Barandes, [The Stochastic-Quantum Theorem](https://philosophyofphysics.lse.ac.uk/articles/10.31389/pop.186).
- R. P. Feynman, R. B. Leighton, and M. Sands, [The Feynman Lectures on Physics, Vol. III, Chapter 3](https://www.feynmanlectures.caltech.edu/III_03.html).
- Rafael D. Sorkin, [Quantum mechanics as quantum measure theory](https://arxiv.org/abs/gr-qc/9401003).
- Murray Gell-Mann and James B. Hartle, [Equivalent sets of histories and multiple quasiclassical domains](https://arxiv.org/abs/gr-qc/9509054).
