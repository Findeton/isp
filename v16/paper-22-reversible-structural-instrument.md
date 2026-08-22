# A typed reversible structural instrument

## Coherent structural query, physical commit, and the no-hiding boundary

### Abstract

Paper 21 constructed an exact structural interferometer but found that the
accepted Paper 13D law did not contain the reversible fusion route needed to
instantiate it. This paper constructs that missing object as a new local
instrument without modifying Paper 13D.

The construction has two necessarily different stages. A reversible query
stage coherently computes either a tensor-preserving or fusion-changing
structural witness, retains all information required by reversibility, and
then uncomputes every witness, seed, complement, and environment field before
the two modes recombine. A later commit stage records the recombined mode and
produces exactly one accessible child: either the accepted Paper 13D tensor
child or the accepted simultaneous-fusion child.

The separation is forced by a no-hiding theorem. If physical fusion maps two
distinct component partitions to the same fused target, it cannot be
reversible on that target alone. Every reversible dilation must retain
orthogonal complement states carrying the missing partition information.
Those states destroy route interference unless they are coherently uncomputed.
Consequently the reversible query is not renamed as physical erasing fusion,
and the committed accessible fusion remains an irreversible channel even
though its measurement dilation is reversible.

The exact structural mode law is not fitted. Requiring a two-mode reversible
lift of the accepted recorded matrix

\[
 B=\frac1{25}\begin{pmatrix}9&16\\16&9\end{pmatrix}
\]

fixes

\[
 R=\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix}
\]

up to input phases, output phases, and simultaneous basis relabeling. A
physical phase applied to the fused query-witness sector then kicks back onto
the structural mode and predicts the complete Paper 21 family `C_phi`,
including its filter residuals, record classicalization, erasure control,
visibility law, and phase-dependent Barandes factorization boundary. If the
fusion query is replaced by a tensor query, this phase response disappears;
the fringe is therefore not produced by an unrelated control qubit.

After recombination, the two outcome-indexed instrument components have
different typed codomains and different accepted futures. Their joint law is

\[
 \widehat\Gamma_{\phi,X}(m,H\mid j)
 =C_\phi(m\mid j)\Gamma_m(H\mid X),
 \qquad m\in\{T,F\},
\]

and follows from one dilation rather than an independently supplied selector
table. At the neutral setting and tensor input, both process components have
positive mass `49/625` and `576/625`. Conditioning exactly recovers the
accepted tensor and fusion child laws. The unchosen child is absent from the
accessible output.

This constructs a triggered, point-free, local structural instrument with
inequivalent process fibers. It does not say when such an opportunity occurs,
select an initial universe, or generate a covariant varying-size history
ensemble. The Paper 17 structural-parent gate opens conditionally on future
independent review of this candidate; its ensemble, chronology, and dimension
gates remain closed.

## 1. Status and frozen protocol

This mathematical candidate is evaluated under

`v16/note-paper22-reversible-structural-instrument-pin.md`

with ordinary SHA-256

`de32c02ee1be613eef4a867dadf9bc1c84fc8ed492b764f7545bb54fb91a5ae4`.

The pin was frozen before the following construction was evaluated. It binds
the accepted Paper 13D mathematical law, Paper 20's dependent-output contract,
and Paper 21's exact discriminator. It does not authorize implementation or
alter any prior artifact.

The present result is a candidate pending independent semantic review. No
code, numerical fit, random search, or Paper 17 output is used.

## 2. Why one map cannot do both jobs

### 2.1 Accessible physical fusion

Let `S` contain complete tensor-source values, including their component
partitions, and let `Y_F` contain accessible fused targets from which that
partition is physically absent. The accepted fusion channel has a map or
kernel supported on

\[
 f:S\times\Xi\longrightarrow Y_F,
\]

where `Xi` supplies fresh cross-pair seeds.

It is possible that distinct complete inputs `s1` and `s2`, or distinct
source partitions of the same union, satisfy

\[
 f(s_1,\xi_1)=f(s_2,\xi_2)=y.
\]

That loss of accessible partition information is part of the meaning of
physical fusion.

### Theorem 1 — finite reversible-erasure obstruction

If `f(s1)=f(s2)` for distinct `s1,s2`, no bijection from `S` to `Y_F` can
agree with `f` on both values. Every injective dilation

\[
 \widetilde f:S\longrightarrow Y_F\times E,
 \qquad
 \widetilde f(s)=(f(s),e(s)),
\]

must satisfy `e(s1) != e(s2)`.

#### Proof

If `e(s1)=e(s2)`, then `tilde f(s1)=tilde f(s2)`, contradicting injectivity.
Therefore the complement retains the distinction erased from the accessible
target. \(\square\)

### Theorem 2 — quantum no-hiding form

Let an isometry map orthogonal source basis states to a common accessible
fused state:

\[
 W|s_k\rangle=|y\rangle|e_k\rangle,
 \qquad k=1,2.
\]

Then

\[
 \langle e_1|e_2\rangle=0.
\]

#### Proof

An isometry preserves inner products, so

\[
 0=\langle s_1|s_2\rangle
  =\langle y|y\rangle\langle e_1|e_2\rangle.
\]

Since `y` is normalized, the complement states are orthogonal. \(\square\)

### Consequence

A reversible dilation of fusion necessarily creates which-partition
information outside the accessible fused field. It can be used coherently
only if that information is later returned to one common blank state. The
same dilation cannot simultaneously be called a completed erasing fusion and
an interference-ready route.

This forces the query/commit separation below.

## 3. Typed source and child functors

### 3.1 Source groupoid

An admitted source is

\[
 X=(\{X_\alpha\}_{\alpha\in A\sqcup E},A),
\]

where:

- each `X_alpha` is a complete Paper 13D boundary value on a nonempty finite
  occurrence set;
- `A` is a physically marked active family containing at least two
  components; and
- `E` is a spectator family.

A presentation morphism transports occurrence labels, component labels,
complete boundary fields, and the active mark together. It cannot change
which physical components were marked.

This defines a groupoid `Src`. No probability is assigned over its objects.

The finite carrier is used because it is the accepted Paper 13D calibration,
not because relational reality or spacetime is assumed to be a discrete web.
The query/commit architecture itself only needs a measurable source groupoid,
a two-mode control fiber, reversible dilations, and dependent child channels;
finite sums become direct integrals in a non-discrete extension. No such
extension is awarded here.

### 3.2 Tensor child

The tensor child functor `T` retains the active component partition, carries
all spectators, and introduces no cross-active pair field:

\[
 T(X)=\boxtimes_{\alpha\in A\sqcup E}X_\alpha.
\]

Its accepted conditional law is denoted

\[
 \Gamma_T(H\mid X).
\]

### 3.3 Fusion child

Let `I_A` be the disjoint union of the active occurrence sets. The fusion
child functor applies the accepted simultaneous Paper 13D fusion only to `A`:

\[
 F(X)=\Phi^{A}(\boxtimes_{\alpha\in A}X_\alpha)
       \boxtimes\boxtimes_{\epsilon\in E}X_\epsilon.
\]

It drops the active partition from the accessible fused target, retains all
within-component bonds, and draws every cross-active bond simultaneously from
the accepted law. Its conditional history law is

\[
 \Gamma_F(H\mid X).
\]

### Theorem 3 — operational distinction

`T(X)` and `F(X)` are predictively distinct whenever at least two active
nonempty components admit a cross pair.

#### Proof

The complete tensor future has an active component partition and no
cross-active bond address. The complete fusion future has one fused active
component and a positive cross-active bond law. These are different typed
probe/future contracts even on the branch where every realized cross bond is
zero. No presentation isomorphism converts one contract into the other.
\(\square\)

### 3.4 Predictive outcome descriptor

For either component define

\[
 \kappa_m(X)
 =[\mathsf Y_{m,X},\Gamma_m^{\rm Fut}]_{\sim_{\rm pred}},
\]

where two accessible child boundaries are predictively equivalent exactly
when every aligned accepted future intervention and complete reader has the
same probability law. The instrument outcome descriptor is `kappa_m`, not the
printed symbol `m`. Theorem 3 proves `kappa_T != kappa_F` on every positive
source. Thus the stable mode record reports an already typed predictive class;
it does not manufacture structural identity by decoding a bit.

## 4. Structural mode and its calibrated reversible lift

### 4.1 Physical mode basis

Let

\[
 \mathcal H_M=\operatorname{span}\{|T\rangle,|F\rangle\}.
\]

The basis is operationally defined by which query and commit component it
controls. It is not an output bit later decoded by convention.

The tensor source preparation uses input mode `j=T`. The `F` input remains an
admitted calibration control.

### Theorem 4 — minimal two-mode lift

Let `U` be a two-dimensional unitary satisfying

\[
 |U_{ij}|^2
 =B_{ij},
 \qquad
 B=\frac1{25}\begin{pmatrix}9&16\\16&9\end{pmatrix}.
\]

Then, up to diagonal input phases, diagonal output phases, and simultaneous
exchange of the physical mode basis, `U` is represented by

\[
 R=\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix}.
\tag{1}
\]

#### Proof

Row and column phases make three selected nonzero entries real and positive.
Their fixed moduli are `3/5,4/5,3/5`. Orthogonality of the two columns forces
the remaining `4/5` entry to have the opposite sign. Normalization is already
fixed by `B`. The remaining choices are precisely the stated phase gauges and
basis exchange. \(\square\)

Equation (1) is therefore the minimal reversible lift of the accepted
recorded mode law. The claim that this lift physically acts on structural
modes is nevertheless a new Paper 22 hypothesis, not a theorem of Paper 13D.

### 4.2 Phase control

The effective relative-mode operation is

\[
D_\phi=|T\rangle\!\langle T|
       +e^{i\phi}|F\rangle\!\langle F|.
\tag{2}
\]

Equivalently,

\[
 D_\phi=e^{i\phi Z_F},
 \qquad Z_F=|F\rangle\!\langle F|.
\]

This fixes a typed one-parameter reversible control acting only on the
structural mode. Section 5.3 derives it by phase kickback from a physical
projector on the open structural query. It is not an unspecified phase
inserted into child histories or an unrelated mode rotation.

`phi` is an apparatus input. The neutral instrument uses `phi=0`; `pi/2` and
`pi` are held-out controls. No cosmological or geometric result selects it.

## 5. Exact reversible query

### 5.1 Cross-pair seed state

For source `X`, let `P_X` be the set of unordered cross-active occurrence
pairs. Paper 13D assigns an independent uniform seed in `[25]` to every pair:

\[
 \Xi_X=[25]^{P_X},
 \qquad
 \mu_X(\xi)=25^{-|P_X|}.
\]

Introduce a blank seed value orthogonal to the seed basis and the normalized
state

\[
 |\Omega_X\rangle
 =5^{-|P_X|}\sum_{\xi\in\Xi_X}|\xi\rangle.
\tag{3}
\]

The coefficient is exact because `sqrt(25^{-|P_X|})=5^{-|P_X|}`.

The Householder reflection through

\[
 |v_X\rangle
 =\frac{|0_\Xi\rangle-|\Omega_X\rangle}{\sqrt2}
\]

defines a canonical unitary

\[
 S_X=I-2|v_X\rangle\!\langle v_X|
\]

with

\[
 S_X|0_\Xi\rangle=|\Omega_X\rangle,
 \qquad S_X^{-1}=S_X.
\tag{4}
\]

Presentation morphisms merely permute `P_X` and the seed basis, so (3) and
(4) are natural.

### 5.2 Reversible witness computation

Let `Q` be a query register whose typed basis includes a blank value, complete
tensor witnesses, and complete fused witnesses. Reversible basis
computations are defined by

\[
 C_{T,X}:|X,0_Q\rangle
 \longmapsto |X,T(X)\rangle,
\]

and

\[
 C_{F,X}:|X,\xi,0_Q\rangle
 \longmapsto |X,\xi,F(X,\xi)\rangle.
\]

The source and seed remain present, so both maps are injective on their
declared subspaces and extend by inverse pairing to permutations of the full
basis.

Set

\[
 U_{T,X}=C_{T,X},
 \qquad
 U_{F,X}=C_{F,X}(S_X\otimes I),
\tag{5}
\]

and

\[
 U_{Q,X}
 =|T\rangle\!\langle T|\otimes U_{T,X}
  +|F\rangle\!\langle F|\otimes U_{F,X}.
\tag{6}
\]

The orthogonal mode projectors make (6) unitary. Its inverse is obtained by
reversing each controlled block.

### Theorem 5 — exact query closure

For every admitted source and both structural modes,

\[
 U_{Q,X}^{-1}U_{Q,X}
 |m,X,0_\Xi,0_Q\rangle
 =|m,X,0_\Xi,0_Q\rangle.
\tag{7}
\]

Every source, seed, query witness, partition complement, and reversible
apparatus coordinate returns to its common blank value.

#### Proof

Each block in (6) is unitary. The fusion block reverses the fused-witness
computation and then applies the self-inverse seed preparation (4). The
orthogonal mode blocks do not mix. Equation (7) follows directly. \(\square\)

### 5.3 What the query is and is not

During the open query, a complete middle reader can distinguish the tensor
and fused witnesses. The fusion block retains the source partition and seed
because Theorems 1–2 require it. It is therefore a reversible fusion query,
not the final accessible Paper 13D fusion.

After (7), none of those fields remains available to distinguish the mode.
This is the exact condition needed for recombination.

### 5.3 Structural phase kickback

Let `Z_Q,F` be the point-free projector on the fused typed subspace of the
open query register. It is defined by the complete query target type, not by
the printed mode label. Apply while the query is open

\[
 P_\phi=e^{i\phi Z_{Q,F}}.
\tag{8}
\]

`P_phi` leaves every classical structural field and every seed probability
unchanged. It multiplies a complete fused query witness by `e^{i phi}` and a
tensor query witness by one. Hence, on the blank source/query subspace,

\[
 U_{Q,X}^{-1}P_\phi U_{Q,X}
 =D_\phi\otimes I.
\tag{9}
\]

Equation (9) is physical phase kickback: the relative mode phase is generated
by an operation on the structural witness while that witness exists, and all
structural registers are nevertheless blank afterward.

If the `F` query is replaced by a second tensor query, both images lie in the
tensor subspace. Then `P_phi` acts as the identity on both modes and the
effective relative phase is zero for every requested `phi`. This substitution
is a held-out discriminator between a structural phase and an unrelated
mode-only phase shifter.

## 6. Probe law and held-out controls

### 6.1 Coherent probe

With both routes open, define

\[
 V_{\phi,X}
 =(R\otimes I)
 U_{Q,X}^{-1}P_\phi U_{Q,X}
 (R\otimes I).
\tag{10}
\]

By Theorem 5 and equation (9), the structural registers factor in their
common blank state and the mode amplitude is exactly

\[
 A_\phi=R D_\phi R.
\]

Hence the direct ordinary stochastic mode law is

\[
 C_\phi=|A_\phi|^2
 =\frac1{625}
 \begin{pmatrix}
 337-288\cos\phi&288(1+\cos\phi)\\
 288(1+\cos\phi)&337-288\cos\phi
 \end{pmatrix}.
\tag{11}
\]

Every column sums to one.

### 6.2 Paper 21 recovery

Because all route filters and route records act on `H_M` while the complete
query inverse remains controlled by the same mode, the exact Paper 21 results
follow without new probabilities:

- both-route filter residuals are

\[
 I_2(T)=-\frac{288}{625}\cos\phi,
 \qquad
 I_2(F)=\frac{288}{625}\cos\phi;
\]

- a stable orthogonal route record gives

\[
 B^2=\frac1{625}\begin{pmatrix}337&288\\288&337\end{pmatrix};
\]

- deterministic record deletion leaves `B^2`;
- coherent reversal of the record interaction restores `C_phi`;
- residual environment overlap `gamma` replaces `cos(phi)` by
  `Re(gamma e^{i phi})`; and
- the unique Barandes continuation through `B` is

\[
 K_\phi=\frac1{175}
 \begin{pmatrix}
 63+288\cos\phi&112-288\cos\phi\\
 112-288\cos\phi&63+288\cos\phi
 \end{pmatrix}.
\]

It is positive exactly for

\[
 -\frac7{32}\leq\cos\phi\leq\frac7{18}.
\]

### Theorem 6 — structural probe interference

The query alternatives are operationally different while open, have no
residual distinguishing field after the inverse, and reproduce the complete
phase, filter, record, erasure, visibility, and nondivision family frozen in
Paper 21.

#### Proof

Operational distinction is Theorem 3 applied to the query witnesses. Exact
uncomputation is Theorem 5. The relative phase is generated from the fused
query type by equation (9); replacing that query by tensor removes the phase
response. The remaining calculation is equation (11), so every Paper 21
derivation applies unchanged.
\(\square\)

## 7. The commit instrument

### 7.1 Outcome-indexed isometry

After recombination, introduce a blank accessible child register `Y`, a
sealed apparatus-exhaust register `C`, and a stable outcome record `R_m`.

For each physical Paper 13D history orbit `[H]`, choose orthogonal exhaust
basis states `|c_{m,[H]}>`. Fix their phases by the positive-amplitude gauge
and define the isometry on the blank input subspace by

\[
 W_X|m,X,0_Y,0_C,0_R\rangle
 =|m_R\rangle
  \sum_{[H]}
 \sqrt{\Gamma_m([H]\mid[X])}
   |H\rangle_Y|c_{m,[H]}\rangle_C.
\tag{12}
\]

Any alternative phase on one term is exactly absorbed by the opposite
rephasing of its private exhaust basis vector, so it is a dilation gauge and
not a physical parameter. In the fusion component, (12) may be realized
directly from the uniform seed state (3); histories in one physical orbit
receive the sum of their seed probabilities.

The orthogonal outcome record and exhaust states make (12) an isometry. Like
every measurement isometry, it can be extended on a larger apparatus space to
a unitary. Its accessible child channel is obtained by restricting lawful
child futures to `Y` and not exposing `C`.

### 7.2 Instrument components

Let `P_m` project onto record `m`. The two completely positive instrument
components are

\[
 \mathcal I_{m,X}(\rho)
 =\operatorname{tr}_C
  \bigl[P_m W_X\rho W_X^\dagger P_m\bigr].
\tag{13}
\]

Their codomains are dependent:

\[
 \mathcal I_{T,X}:X\to\mathsf Y_{T,X},
 \qquad
 \mathcal I_{F,X}:X\to\mathsf Y_{F,X}.
\]

No active register for the other child occurs in either component.

### 7.3 Exact joint law

Combining the probe (10) with the commit isometry, the complete accessible
history law is

\[
 \widehat\Gamma_{\phi,X}(m,[H]\mid j)
 =C_\phi(m\mid j)\Gamma_m([H]\mid[X]).
\tag{14}
\]

This is not an imposed selector factorization. The first factor is the squared
mode amplitude produced before the commit; the second is the conditional norm
inside the selected block of the one isometry (12).

### Theorem 7 — normalization

For every admitted source, input mode, and phase,

\[
 \sum_m\sum_{[H]}
 \widehat\Gamma_{\phi,X}(m,[H]\mid j)=1.
\]

#### Proof

Each column of `C_phi` sums to one and each accepted child law `Gamma_m` is
normalized. Summing (14) first over histories and then over modes gives one.
Equivalently, the sum of the two trace-nonincreasing maps (13) is
trace-preserving on the declared input. \(\square\)

### Theorem 8 — exact child recovery

Whenever `C_phi(m|j)>0`,

\[
 \widehat\Gamma_{\phi,X}([H]\mid m,j)
 =\Gamma_m([H]\mid[X]).
\tag{15}
\]

Thus conditioning on `T` recovers the accepted tensor child and conditioning
on `F` recovers the accepted simultaneous fusion child, including complete
orbit mass.

#### Proof

Divide (14) by its mode marginal `C_phi(m|j)`. \(\square\)

### 7.4 Neutral and held-out structural laws

Use tensor input `j=T`. At the neutral phase,

\[
 \Pr(T\mid X)=\frac{49}{625},
 \qquad
 \Pr(F\mid X)=\frac{576}{625}.
\tag{16}
\]

At the held-out phases,

\[
 \phi=\frac\pi2:
 \quad
 \Pr(T\mid X)=\frac{337}{625},
 \quad
 \Pr(F\mid X)=\frac{288}{625},
\tag{17}
\]

and

\[
 \phi=\pi:
 \quad
 \Pr(T\mid X)=1,
 \quad
 \Pr(F\mid X)=0.
\tag{18}
\]

The zero in (18) is a valid controlled extinction, not deletion of the `F`
type from the instrument.

## 8. No dormant unchosen child

### Theorem 9 — dependent-output exclusivity

Conditioned on outcome `m`, the accessible target contains one child in
`Y_m,X` and no active value in `Y_not-m,X`.

#### Proof

The codomain of the component (13) is the `m` summand of the dependent
disjoint union. Equation (12) contains a selected-history exhaust label, not
an active register carrying the other child. Projecting onto `m` annihilates
the other component before the accessible target is formed. \(\square\)

The apparatus still contains the physical operations capable of implementing
both components, just as any instrument does. Hardware availability is not a
simultaneously realized alternative structure. The outcome record and sealed
exhaust contain the selected branch only.

### 8.1 Why the exhaust is not silently deleted

The exhaust is explicit in the dilation and excluded from accepted child
futures by the instrument boundary. If it were made available to those
futures, equation (15) would fail because the child would have a new readable
partition/seed record. The local instrument is therefore an open-system
channel with a complete dilation, not a claim that the accessible fusion is a
globally reversible law of the entire universe.

This restriction is physical and testable: opening the exhaust is a different
experiment and may recover which-branch information.

## 9. Point-free covariance

Let `g:X->X'` be a source-presentation isomorphism. It transports:

- the active and spectator families;
- tensor and fusion child histories;
- cross-pair seed coordinates;
- query witnesses;
- mode-controlled operations;
- complete readers; and
- apparatus exhaust labels.

The uniform seed state (3) is invariant under the induced permutation. The
classical computations commute with transport because Paper 13D tensor and
fusion are equivariant. `R` and `D_phi` act on the physical mode type and are
independent of presentation. Equation (12) uses the already pushed-forward
physical child law.

### Theorem 10 — naturality

The query, probe, commit components, joint law, and every conditioned child
future commute with `g`. In particular,

\[
 \widehat\Gamma_{\phi,X'}
 (m,g[H]\mid j)
 =\widehat\Gamma_{\phi,X}(m,[H]\mid j).
\]

#### Proof

Naturality holds generator by generator as described above and is preserved
by composition, direct sum, tensor product, adjoint, and partial trace over
the transported exhaust. When several seed values descend to one physical
history orbit, equation (12) and the trace in (13) sum their orthogonal
probabilities. No representative mass is used. \(\square\)

## 10. Spectators, restriction, and local composition

### Theorem 11 — rooted spectator invariance

Adding an unmarked independent spectator changes neither `C_phi` nor the
conditional active child law.

#### Proof

The mode operations act only on `A`. Paper 13D tensor carries the spectator
as a product factor, fusion acts only on the marked active family, and every
mode coefficient is source independent. Hence the joint law factors as the
old instrument law tensor the spectator law. \(\square\)

### Theorem 12 — restriction compatibility

Restricting occurrence sets transports the instrument to the correspondingly
restricted source and marginalizes deleted independent cross-pair seeds.

#### Proof

The seed state is a tensor product over unordered cross pairs. Partial trace
over deleted seed coordinates leaves the same uniform product state on
retained pairs. Accepted Paper 13D tensor/fusion restriction commutes with its
evaluation. `C_phi` is independent of occurrence cardinality. Therefore the
restricted joint law equals the pushforward of (14). \(\square\)

Restriction removes empty active components. If fewer than two nonempty
active components remain, the result lands in a declared degenerate control
family, not in the positive structural-opportunity domain. In that control,
tensor and fusion accessible futures are predictively identical, the
structural quotient merges them, and their masses are summed. The stable
process-outcome record still distinguishes the two apparatus components until
that record is itself erased. Structural identity and process-history
identity are not conflated, and deletion never forges a new fusion
opportunity.

### 10.1 Tensor and disjoint active families

Two independently triggered instruments on disjoint sources tensor to the
product instrument. Two disjoint marked active families inside one larger
source have commuting query and commit maps because their source, seed, and
child registers are disjoint. This proves order independence of their
auxiliary evaluation.

It does not supply a probability that either opportunity occurs, and an
implementation loop order is not physical time.

### 10.2 Accepted futures

After outcome `m`, every accepted Paper 13D future composable with child
`Y_m,X` may be appended. Equation (15) then gives exactly the accepted child
future law. The stable `m` record makes the branch a complete local division
for those declared futures.

## 11. Are these whole-process fibers?

### 11.1 Instrument process map

A quantum instrument is an outcome-indexed family of transformations, not a
single stochastic channel followed by an arbitrary decoder. Define

\[
\operatorname{Proc}(m,H)=[\mathcal I_{m,X},H].
\]

Each complete history contains the common reversible probe followed by one
typed commit component. A `T` history contains the tensor commit and a value
in its tensor-history fiber; an `F` history contains the simultaneous-fusion
commit, its cross-pair generation, and a value in its fusion-history fiber.
The component is therefore part of the physical history type before any
reader is chosen.

The two values have different typed codomains, different complete histories,
and different lawful future algebras. The stable outcome record is generated
by the instrument itself.

### Theorem 13 — local process plurality

At the neutral setting and tensor input, the process pushforward has two
positive, predictively inequivalent components:

\[
 \operatorname{Proc}_*\widehat\Gamma_{0,X}
 =\frac{49}{625}\delta_{[\mathcal I_T]}
  +\frac{576}{625}\delta_{[\mathcal I_F]}.
\tag{19}
\]

#### Proof

The probabilities are (16). Predictive inequivalence follows from Theorem 3
and exact child recovery from Theorem 8. Because the instrument components
themselves carry the dependent target types, no external result-bit decoder
defines (19). \(\square\)

This is genuine local instrument-process plurality in the sense requested by
Paper 20. It is not a probability law over arbitrary global execution
complexes.

## 12. What fixes the probability and what remains postulated

The construction does not choose an arbitrary pair of structural weights.
Its probability family follows from:

1. the accepted recorded matrix `B`;
2. minimal reversible two-mode lifting, Theorem 4;
3. the new physical identification of that mode with the controlled
   tensor/fusion query and commit;
4. the point-free fused-witness projector and its phase kickback (8); and
5. the Born probability rule for the reversible mode experiment.

Items 1 and the conditional child laws are inherited calibrations. Items 2
and 5 are standard reversible-amplitude structure. Items 3–4 are the
substantive new Paper 22 physical hypotheses. The query-substitution control
tests that item 4 is structurally attached. The construction is therefore
independently specified and testable but not derived from Paper 13D alone.

The amplitude representation earns operational content because the phase,
filters, records, erasure, and recombination all change held-out
probabilities. It still need not be declared ontologically more fundamental
than the complete family of ordinary instrument probabilities.

## 13. Hostile-control audit

| attack | result |
|---|---|
| renamed route bits | killed by complete middle witnesses and typed commits |
| reversible partition erasure | disproved by Theorems 1–2 |
| hidden complement at recombination | fails Theorem 5 and moves to partial coherence |
| seed traced before inverse | fails exact query closure |
| visible-only inverse | complete reader detects nonblank environment |
| Paper 13D eraser used as unfusion | type mismatch; eraser acts on records, not partitions |
| classical deletion called unrecording | Paper 21 `B^2` control survives |
| independent selector table | absent; law follows from one dilation |
| arbitrary square-root matrix | killed by Theorem 4 and phase gauges |
| dimension-selected phase | forbidden; phases frozen independently |
| phase changes fusion seeds | false; seed state (3) is phase independent |
| identity query substituted for fusion | structural phase response vanishes by Section 5.3 |
| filter changes source/reader | killed by common probe typing |
| postselected renormalization | loss remains a complete outcome in probe controls |
| swapped naked decoder | changes controlled commit and is a different instrument |
| product of both active children | absent by Theorem 9 |
| unchosen active child hidden in apparatus | exhaust stores only selected history/complement |
| exhaust exposed to child future | explicitly changes experiment and invalidates recovery |
| representative seed mass | killed by orbit pushforward in Theorem 10 |
| automorphism-dependent odds | `C_phi` is source independent |
| spectator-dependent odds | killed by Theorem 11 |
| deletion loses normalization | killed by Theorem 12 |
| loop order called time | disjoint operations commute; no chronology awarded |
| trigger called activity law | rejected in Section 14 |
| input called root law | rejected in Section 14 |
| local branches called universe ensemble | rejected in Section 15 |
| target-only plurality | strengthened to typed instrument components in Theorem 13 |
| finite carrier called ontology | rejected; construction is a local accepted-family control |
| amplitudes called primitive | not claimed |
| geometry selects instrument | prohibited by frozen chronology |
| local success completes Paper 17 | rejected in Section 15 |

No pinned semantic attack defeats the constructed local instrument.

### Theorem 14 — complete typed totality

For every admitted positive source, input mode, frozen phase control, route
filter, and record context, the candidate returns a normalized value in one
declared dependent child or in the complete probe loss carrier. Every query
and commit component has an exact typed source and target.

#### Proof

Sections 3–5 define the source, both child functors, the complete query
carrier, and invertible query maps. Section 6 supplies the normalized probe
and explicit loss handling inherited from Paper 21. Sections 7–8 define the
two component codomains and prove instrument normalization. The degenerate
restriction controls of Section 10 have a declared merged target. No clause
returns an undeclared value. \(\square\)

### Theorem 15 — record and unrecord separation

A stable orthogonal mode record changes the probe law from `C_phi` to `B^2`.
Deterministically resetting its visible value leaves `B^2`, while applying the
inverse record interaction before any uncontrolled copy restores `C_phi`.

#### Proof

The complete query fields are blank by Theorem 5, so the only off-diagonal
mode factor is the inner product of the two record/environment states. It is
zero for an orthogonal record and remains zero after a many-to-one visible
reset because the discarded information is in the environment. It returns to
one only when the full write is inverted. Substitution in the partial
coherence law of Section 6 gives the three stated matrices. \(\square\)

## 14. Missing activity, root, and actuality laws

The source `X`, active mark `A`, input mode `j`, and apparatus phase are
experimental inputs. Equation (14) is conditional on the instrument being
applied. It does not provide:

- a propensity for an opportunity to occur;
- a covariant distribution of active marks;
- a waiting-time or activity law;
- a law for the initial structural source;
- a cosmological boundary state; or
- a rule selecting one realized history.

Repeatedly applying the instrument according to an externally supplied list
would introduce precisely the hidden scheduler or global clock the project
has excluded. The local tensor/composition laws do not repair that absence.

### Theorem 16 — activity and root noninheritance

The conditional instrument law identifies neither an opportunity/activity
kernel nor a root distribution.

#### Proof

Let `a(o|x)` be any normalized law for whether and where an opportunity is
offered, and let `nu(x)` be any normalized source law. For every positive
opportunity, the conditional outcome/history law remains equation (14),
independently of `a` and `nu`. Distinct pairs `(a,nu)` therefore agree on every
law constructed in this paper and disagree on opportunity frequency and root
statistics. Those data are not identifiable from the triggered instrument.
\(\square\)

## 15. Paper 17 adjudication

Paper 20 identified a dependent-output parent with positive mass on
inequivalent process fibers as one route through its structural-parent gate.
Theorem 13 constructs such a local triggered parent, subject to future
independent acceptance of this candidate.

Therefore the product is:

- **structural-parent gate:** conditionally open after semantic acceptance;
- **autonomous varying-history ensemble gate:** closed;
- **complete operational chronology gate:** closed;
- **dimension-selection gate:** closed.

Paper 17 may use the accepted instrument as a local interventional building
block. It may not generate an ensemble by choosing a sequence, density, or
placement of applications after seeing a desired dimension.

The next missing physics is no longer a structural selector weight. It is a
covariant opportunity/activity law—or a proof that one complete parent law
generates its own opportunities without an external scheduler.

### Theorem 17 — exact Paper 17 boundary

If this candidate is independently accepted, it satisfies Paper 20's local
dependent-output structural-parent condition but does not determine a
varying-history ensemble, chronology, or dimension.

#### Proof

Theorem 13 gives positive mass to two predictively inequivalent instrument
components, establishing the local parent condition. Theorem 16 exhibits
arbitrarily many opportunity and root laws with the same local instrument.
Those alternatives generate different numbers, placements, and dependency
patterns of committed structures. Hence the local law cannot determine the
global ensemble required by Paper 17, and no downstream chronology or
dimension test is yet licensed. \(\square\)

## 16. Outcome product

```text
typed local instrument
  P22-TYPED-STRUCTURAL-INSTRUMENT-CONSTRUCTED

reversible coherent query
  P22-REVERSIBLE-STRUCTURAL-QUERY-CONSTRUCTED

reversible accessible erasing fusion
  P22-REVERSIBLE-ERASING-FUSION-IMPOSSIBLE

structural probe
  P22-STRUCTURAL-PROBE-INTERFERENCE-CONSTRUCTED

dependent commit
  P22-DEPENDENT-STRUCTURAL-COMMIT-CONSTRUCTED

conditioned child laws
  P22-CONDITIONED-PAPER13D-CHILD-RECOVERY-CONSTRUCTED

unchosen child
  P22-NO-DORMANT-UNCHOSEN-CHILD-PROVED

presentation covariance
  P22-POINT-FREE-NATURALITY-CONSTRUCTED

restriction and spectators
  P22-RESTRICTION-AND-SPECTATOR-LAWS-CONSTRUCTED

local process components
  P22-INEQUIVALENT-PROCESS-FIBERS-CONSTRUCTED

autonomous occurrence
  P22-AUTONOMOUS-ACTIVITY-LAW-UNCONSTRUCTED

initial state
  P22-ROOT-LAW-UNCONSTRUCTED

Paper 17 structural parent
  P22-P17-STRUCTURAL-PARENT-GATE-OPEN-CONDITIONAL-ON-REVIEW

Paper 17 varying histories
  P22-P17-VARYING-HISTORY-ENSEMBLE-GATE-CLOSED

Paper 17 chronology and dimension
  P22-P17-CHRONOLOGY-DIMENSION-GATE-CLOSED

actuality
  P22-ACTUALIZATION-UNCONSTRUCTED

metric
  P22-METRIC-UNCONSTRUCTED
```

## 17. Strongest honest interpretation

The construction proves that a quantum-style structural operation can be
typed without treating a fused structure as secretly reversible:

> Tensor and fusion may be coherently queried as alternative reversible
> computations, provided every partition and seed record is uncomputed before
> recombination. After recombination, one outcome-indexed instrument may
> commit exactly one tensor or fused child with probabilities fixed by the
> common mode law. The committed accessible fusion is an irreversible channel;
> only its larger measurement dilation is reversible.

This is the same architecture used whenever quantum theory represents an
irreversible measurement or channel by a reversible system-apparatus
interaction. Here it is applied to relational structure with the additional
requirements of typed dependent outputs, point-free covariance, exact child
recovery, and no dormant unchosen child.

## 18. Permanent scope walls

The candidate does not prove:

- that the structural instrument exists in nature;
- that Paper 13D itself already contains it;
- that the neutral phase is a cosmological law constant;
- that opportunities occur with any frequency;
- that a global structure or source is selected;
- that any possible branch becomes actual;
- that repeated outputs form a locally finite causal order;
- that a spacetime dimension is selected;
- that the mode carrier is a fundamental discrete entity; or
- that signature, topology, scale, metric, curvature, gravity, or continuum
  physics has emerged.

## References

- Jacob A. Barandes, [The Stochastic-Quantum Theorem](https://philosophyofphysics.lse.ac.uk/articles/10.31389/pop.186).
- R. P. Feynman, R. B. Leighton, and M. Sands, [The Feynman Lectures on Physics, Vol. III, Chapter 3](https://www.feynmanlectures.caltech.edu/III_03.html).
- Giulio Chiribella, Giacomo M. D'Ariano, and Paolo Perinotti, [Theoretical framework for quantum networks](https://arxiv.org/abs/0904.4483).
- Masanao Ozawa, [Mathematical foundations of quantum information: measurement and foundations](https://arxiv.org/abs/1201.5334).
- Bob Coecke, Chris Heunen, and Aleks Kissinger, [Categories of quantum and classical channels](https://arxiv.org/abs/1408.0049).
- Yoon-Ho Kim et al., [A delayed choice quantum eraser](https://arxiv.org/abs/quant-ph/9903047).
- Berthold-Georg Englert, [Fringe visibility and which-way information](https://doi.org/10.1103/PhysRevLett.77.2154).
