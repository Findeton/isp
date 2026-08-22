# Paper 22 independent quantum-instrument and no-hiding review

Date: 2026-08-21

Seat: **Q — quantum instrument and no-hiding**

Verdict: **REVISE**

First decisive semantic counterexample: **the stated source class admits an
active family whose components have different Paper 13D atomic boundary
sorts, but the inherited simultaneous-fusion generator exists only for a
family at one common sort.  For that admitted source the fusion child,
fusion query, and fusion commit are undefined.**

This is a repairable domain-typing defect, not a failure of the finite-mode
interference algebra.  On the fusion-compatible fixed-source fibers, the
query, no-hiding, probe, record, and commit calculations survive the attacks
below with the scope qualifications stated here.

## 1. Authentication, corpus boundary, and independence

The review protocol was authenticated before use:

| object | ordinary SHA-256 | result |
|---|---|---|
| Paper 22 review protocol | `157531a09b1d90ae878bfc82cdfc325fa2642cbee4df4601afc865c1f529e907` | exact |

Every scientific input used by this review was authenticated against the
protocol before analysis:

| immutable object | ordinary SHA-256 | result |
|---|---|---|
| Paper 13D law | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` | exact |
| Paper 13D terminal adjudication | `ae2c4ef066335c39a0b8057c897c947b06e4270be67d1ed3ec59bf8d6d0a00c9` | exact |
| Paper 20 dependent-parent contract | `64111d7764bf70984b959e00bc1da30ad0d6c3ae7b5c6d51b94227ad2f5c35e6` | exact |
| Paper 21 interferometer | `ca0f709b00906971c6aac2b25b12fea11f168411ab2f440ccc49d982aab4ba80` | exact |
| Paper 21 pin | `7df73538f87a39e22a4aa221d4c94842620fb7c8329e68d072ea98a7c7e9f9f7` | exact |
| Paper 22 pin | `de32c02ee1be613eef4a867dadf9bc1c84fc8ed492b764f7545bb54fb91a5ae4` | exact |
| Paper 22 candidate | `6d75a072fb3c51c5c267448fd329895f94cd4f9ee4ba4d96ea9660be80c1c6b7` | exact |

The Paper 22 pin and candidate were reauthenticated with those same exact
digests immediately before this report was frozen.

I did not read the frontier census, the single-seat Paper 22 input audit,
Paper 23 material, or any sibling report.  I did not contact another seat.
I inspected or ran no implementation or code, and I did not stage or commit
anything.  The present file is the only report I wrote.

## 2. Decisive counterexample

Paper 22 Section 3.1 declares an admitted source

\[
 X=(\{X_\alpha\}_{\alpha\in A\sqcup E},A)
\]

subject to three stated conditions: every component is a complete Paper 13D
boundary value on a nonempty occurrence set, the marked active family has at
least two components, and the remaining components are spectators.  It does
not require all active components to have one common atomic boundary sort.

Take `E` empty and `A={alpha,beta}`.  Let

\[
 X_\alpha\in B_1^0(\{i\}),\qquad
 X_\beta\in B_2^0(\{j\}).
\]

Both are complete Paper 13D boundary values on nonempty finite occurrence
sets, so this `X` satisfies the candidate's source definition.  Tensor is
defined, but Paper 13D supplies fusion only in the form

\[
 \Phi_s^{\{I_\alpha\}}:
 \boxtimes_\alpha B_s(I_\alpha)\longrightarrow B_s(\bigsqcup I_\alpha)
\]

for a single common sort `s`.  There is no inherited fusion arrow mixing
`B_1^0` and `B_2^0`.  Consequently all of the following expressions in the
candidate are undefined for this admitted source:

- `F(X)` in Section 3.3;
- `C_{F,X}`, `U_{F,X}`, and `U_{Q,X}` in Section 5;
- the fused-subspace projector used for phase kickback;
- `Gamma_F(.|X)` and the `F` block of `W_X`; and
- the normalization and totality statements quantified over every admitted
  positive source.

This is a direct counterexample to complete source typing and Theorem 14.
The review protocol makes ill-typing a scientific failure, so the frozen
candidate cannot receive `ACCEPT` merely because the repair is obvious.

The minimal repair is to define the source groupoid as a disjoint union over
Paper 13D atomic sorts and require that every marked active component lie in
one fixed sort `s`; all presentation morphisms must preserve `s`.  Spectator
typing should also be stated explicitly.  All query, commit, restriction,
and naturality quantifiers must then be restricted to this
fusion-compatible groupoid.  That is a revision of the declared domain and
must be frozen and reviewed; it is not silently supplied here.

## 3. Independent reconstruction on a well-typed fixed-source fiber

For this section only, fix a fusion-compatible complete classical source `X`
whose active components share one Paper 13D sort.  The construction then has
the following mathematical core.

### 3.1 No-hiding boundary

For a deterministic collision `f(s1)=f(s2)=y` with `s1 != s2`, an injective
dilation `s -> (f(s),e(s))` requires `e(s1) != e(s2)`.  Otherwise the two
joint outputs coincide.  In the Hilbert version,

\[
 W|s_k\rangle=|y\rangle|e_k\rangle
\]

for orthogonal basis inputs gives

\[
 0=\langle s_1|s_2\rangle
  =\langle y|y\rangle\langle e_1|e_2\rangle,
\]

so the complement states are orthogonal.  This correctly establishes the
claimed obstruction for deterministic basis collisions, which is the scope
needed after the stochastic fusion seed has been purified and retained.  It
does not prove a more general branchwise-orthogonality theorem for arbitrary
mixed accessible outputs, and the candidate should not be cited for that
stronger statement.

Thus reversible query and accessible erasing fusion cannot be the same map.
The source partition and seed remain in the query dilation; the accepted
fusion child is created only after recombination by an open-system commit.

### 3.2 Seed preparation and query

Let `P_X` be the cross-active unordered-pair set and

\[
 \Xi_X=[25]^{P_X},\qquad
 |\Omega_X\rangle=5^{-|P_X|}\sum_{\xi\in\Xi_X}|\xi\rangle.
\]

Because the blank seed state is orthogonal to every seed basis state,

\[
 |v_X\rangle=(|0_\Xi\rangle-|\Omega_X\rangle)/\sqrt2,
 \qquad S_X=I-2|v_X\rangle\langle v_X|
\]

is a reflection satisfying `S_X|0>=|Omega_X>` and `S_X^2=I`.  Uniformity
and permutation of pair coordinates make the initialized action natural.

The basis computations

\[
 C_{T,X}|X,0_Q\rangle=|X,T(X)\rangle,
\]

\[
 C_{F,X}|X,\xi,0_Q\rangle
   =|X,\xi,F(X,\xi)\rangle
\]

are injective because source and, on the fusion branch, seed are retained.
They therefore admit permutation-unitary extensions.  With

\[
 U_{T,X}=C_{T,X},\qquad
 U_{F,X}=C_{F,X}(S_X\otimes I),
\]

the controlled direct sum `U_{Q,X}` is unitary.  On the declared initialized
subspace its exact inverse restores source, seed, witness, complement, and
declared apparatus coordinates to their common input values.

This is an ideal closed-apparatus statement.  If an omitted environment
couples differently to the two routes, exact closure is false and the
partial-coherence law below applies.  The mathematics cannot certify the
absence of an unmodelled physical environment.

### 3.3 Lift and phase kickback

For a two-by-two unitary with entrywise moduli squared

\[
 B=\frac1{25}\begin{pmatrix}9&16\\16&9\end{pmatrix},
\]

three nonzero entries can be made positive by row and column phase choices;
column orthogonality forces the fourth sign.  Hence a representative is

\[
 R=\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix}
\]

up to input phases, output phases, and basis exchange.  This classification
is correct.  It does not make the physical use of this representative, its
orientation, or its phase-zero convention a consequence of `B`; those are
new Paper 22 apparatus hypotheses.

Let `Z_{Q,F}` project on the fused typed query-witness subspace.  Then

\[
 P_\phi=e^{i\phi Z_{Q,F}}
\]

acts by `e^{i phi}` on every fused witness and by one on every tensor witness.
On the initialized fixed-`X` subspace,

\[
 U_{Q,X}^{-1}P_\phi U_{Q,X}=D_\phi\otimes I,
 \qquad D_\phi=\operatorname{diag}(1,e^{i\phi}).
\]

The operation is structurally attached because replacing the `F` query by a
second tensor query places both images outside the fused projector and makes
the effective phase identity.  This is a physical phase-oracle postulate,
not a derivation of such an oracle from Paper 13D.

### 3.4 Probe algebra

Writing `c=3/5`, `s=4/5`,

\[
 A_\phi=RD_\phi R
 =\begin{pmatrix}
 c^2-s^2e^{i\phi}&-cs(1+e^{i\phi})\\
 cs(1+e^{i\phi})&-s^2+c^2e^{i\phi}
 \end{pmatrix}.
\]

Therefore

\[
 C_\phi=|A_\phi|^2
 =\frac1{625}\begin{pmatrix}
 337-288\cos\phi&288(1+\cos\phi)\\
 288(1+\cos\phi)&337-288\cos\phi
 \end{pmatrix}.
\]

All entries are nonnegative and every column sums to one.  For tensor input,
the full filter distributions, with denominator 625, are

| context | `T` | `F` | `loss` |
|---|---:|---:|---:|
| both | `337-288 cos(phi)` | `288(1+cos(phi))` | `0` |
| tensor only | `81` | `144` | `400` |
| fusion only | `256` | `144` | `225` |
| empty | `0` | `0` | `625` |

Thus

\[
 I_2(T)=-288\cos\phi/625,\quad
 I_2(F)=288\cos\phi/625,\quad I_2(loss)=0.
\]

An orthogonal stable route record removes the cross term and yields

\[
 B^2=\frac1{625}\begin{pmatrix}337&288\\288&337\end{pmatrix}.
\]

Resetting only the visible record leaves an orthogonal environment and hence
the same `B^2`; reversing the complete write before copying restores
`C_phi`.  If the complete residual route states have overlap
`gamma=<e_T|e_F>`, put `q_phi=Re(gamma e^{i phi})`.  The law is obtained from
`C_phi` by replacing `cos(phi)` with `q_phi`.  Phase-scan visibility is

\[
 \mathcal V_F=|\gamma|,\qquad
 \mathcal V_T=(288/337)|\gamma|.
\]

Finally,

\[
 B^{-1}=\frac17\begin{pmatrix}-9&16\\16&-9\end{pmatrix}
\]

gives the unique continuation

\[
 K_\phi=C_\phi B^{-1}
 =\frac1{175}\begin{pmatrix}
 63+288\cos\phi&112-288\cos\phi\\
 112-288\cos\phi&63+288\cos\phi
 \end{pmatrix}.
\]

It is stochastic exactly for
`-7/32 <= cos(phi) <= 7/18`.  These calculations exactly reproduce Paper 21
on a fusion-compatible ideal query fiber.

### 3.5 Commit, partial trace, and child recovery

For fixed `X`, the proposed commit maps the two mode basis inputs to

\[
 |m_R\rangle\sum_{[H]}
 \sqrt{\Gamma_m([H]\mid[X])}
 |H\rangle_Y|c_{m,[H]}\rangle_C.
\]

The normalized child law and orthogonal record blocks make the two images
orthonormal.  Choosing mutually orthogonal exhaust labels for distinct
histories makes the reduced `Y` state diagonal with weights `Gamma_m`; after
projection on `m` and tracing `C`, the joint classical law is

\[
 \widehat\Gamma_{\phi,X}(m,[H]\mid j)
 =C_\phi(m\mid j)\Gamma_m([H]\mid[X]).
\]

Summing histories and modes gives one.  For every positive mode marginal,
conditioning cancels `C_phi` and recovers the exact Paper 13D child law.  At
`phi=pi`, tensor input gives zero fusion mass, so fusion conditioning is
undefined there; the candidate correctly states recovery only when the
conditioning event is positive.

Each accessible component has only its selected dependent child.  The sealed
exhaust contains selected-history purification data, not an active copy of
the unchosen child.  This proves no dormancy at the accessible child boundary.
It does not remove the apparatus complement from a universal closed world;
opening that complement is explicitly a different experiment.

The displayed `W_X` is an isometry only fiber by fiber, with `X` a classical
external parameter.  It is not by itself one Stinespring isometry on coherent
superpositions of distinct source values.  A global direct-sum dilation would
have to retain an `X` label (for example in `c_{X,m,[H]}`) whenever different
sources can reach the same accessible history.  Nothing in the accepted
fixed-source stochastic instrument requires such a global coherent source
carrier, but no stronger claim is earned.

## 4. Protocol-mandated quantum attacks

### Q1. Route-dependent complement

Replace the claimed common blank by residual states `|e_T>` and `|e_F>`.
The cross term is multiplied by `gamma=<e_T|e_F>`.  If the states are
orthogonal, the law is `B^2`; if they are distinct but nonorthogonal,
visibility is reduced as above.  Full `C_phi` is recovered only for the same
state up to a physically irrelevant common phase.  The candidate survives
because its ideal query explicitly inverts all declared coordinates; the
attack fixes the exact closed-environment scope.

### Q2. Nonorthogonal or reused exhaust label

For two different histories `H != H'`, tracing a reused or nonorthogonal
exhaust produces the off-diagonal coefficient

\[
 \sqrt{\Gamma(H)\Gamma(H')}
 \langle c_{H'}|c_H\rangle |H\rangle\langle H'|.
\]

That is not the classical Paper 13D child state under a reader capable of
seeing history coherence.  Paper 22 explicitly chooses orthogonal
`c_{m,[H]}` and therefore kills this attack for its declared channel.  The
fixed outcome record makes the two mode blocks orthogonal as well.

### Q3. Source collision across two `W_X`

Let distinct sources `X` and `X'` have a common output label `[H]`, and reuse
the same `c_{m,[H]}`.  The orthogonal inputs `|m,X>` and `|m,X'>` then have
overlapping, possibly identical, images, so `direct-sum_X W_X` is not an
isometry.  The candidate avoids contradiction only because it defines a
separate `W_X` for each classical source and never constructs coherent source
superpositions.  A universal dilation claim would fail without source-indexed
exhaust or retained source data.  This is a binding scope limit.

### Q4. Phase acting only on an unrelated control mode

Replace the fusion query by a second tensor query while leaving the mode
carrier present.  Since both query images lie in the tensor subspace,
`Z_{Q,F}` vanishes on both and `U_Q^{-1}P_phi U_Q=I`.  The fringe no longer
responds to `phi`.  The candidate passes: its phase is attached to the fused
witness type, although the availability of that phase oracle remains a new
physical hypothesis.

## 5. Additional independent semantic controls

These are fresh controls beyond the four attacks mandated for Seat Q.

### F1. Heterogeneous active boundary sorts — decisive

The `B_1^0/B_2^0` source constructed in Section 2 is admitted by the frozen
source definition but has no Paper 13D fusion.  This falsifies totality and
sets the verdict to `REVISE`.

### F2. Mixer gauge becomes an interferometer phase offset

Take another single-step lift `U=R diag(1,e^{i theta})`; it has the same
entrywise law `B`.  If the same representative is naively used in both mixer
slots,

\[
 |U D_\phi U|^2=|R D_{\phi+\theta}R|^2,
\]

up to irrelevant outer column phases.  Hence `B` alone does not select the
neutral fringe or the zero of `phi`.  The candidate survives only by
postulating the real `R` implementation and its phase calibration.  The
minimal-lift theorem is a gauge classification, not an autonomous selection
theorem.

### F3. Seed-dependent purification phases

Replace the uniform purification by

\[
 5^{-|P_X|}\sum_\xi e^{i\theta_\xi}|\xi\rangle.
\]

Seed probabilities and the Paper 13D child law are unchanged.  If the same
preparation is exactly inverted, the fused-subspace phase still kicks back as
one common `e^{i phi}`.  If a seed-dependent phase or seed copy survives the
inverse, it contributes to `gamma` and reduces or shifts the fringe.  Thus
the candidate's explicit matched preparation/inverse passes, while no
ontological significance or autonomous selection attaches to the positive
purification gauge.

### F4. Arbitrary off-initial-subspace extensions

Injective basis computations admit many permutation-unitary extensions.
Two arbitrary extensions need not commute with presentation transport on
unused basis states.  All advertised probabilities use the initialized blank
subspace, on which the action is natural and the inverse exact.  Accordingly
the candidate earns a natural initialized instrument, not a canonical global
unitary on every unused query basis vector.  A stronger global-naturality
claim would require an equivariant extension construction.

### F5. Opened exhaust and coherent child effects

Permit accepted futures to act jointly on `Y` and `C`.  They can distinguish
purifications and, with nontrivial exhaust operations, need not reproduce the
Paper 13D stochastic future.  The candidate expressly seals `C`, so exact
child recovery holds only for the declared accessible boundary.  This attack
confirms rather than defeats the open-system scope.

### F6. Zero-probability conditioned branch

At tensor input and `phi=pi`, `C_pi(F|T)=0`.  No conditional fusion law exists
for that control setting.  Paper 22 includes the fusion component in the
instrument carrier and states equation (15) only for positive marginals, so
it does not manufacture a conditional distribution on a null event.

### F7. Filter loss complement

A reversible dilation of a blocker must retain enough information to keep
orthogonal blocked route states orthogonal, even if the accessible reader
coarse-grains them to one `loss` outcome.  This does not affect the displayed
detected probabilities or normalization, because loss is never renormalized
away.  It does mean that the inherited filter table is an accessible
instrument law, not a claim that every microscopic loss state is literally
one pure vector.  Leakage from loss back into transmitted routes would again
be measured by a nonunit `gamma` and is outside the ideal control.

## 6. Claim-by-claim dispositions

| claim | disposition |
|---|---|
| typed source and dependent-output totality | **fails as stated**; heterogeneous active sorts are admitted but not fusible |
| operational tensor/fusion distinction | passes on every fusion-compatible positive source |
| finite no-hiding theorem | passes for deterministic collisions |
| Hilbert no-hiding theorem | passes for orthogonal inputs with a common pure accessible output; no stronger mixed-output theorem awarded |
| seed preparation | normalized, exact, and natural on initialized fibers |
| reversible witness computation | injective and unitarily extendible on a well-typed fixed-source fiber |
| exact inverse/environment closure | exact for all declared closed-apparatus registers; external leakage is not ruled out by mathematics |
| minimal orthogonal lift of `B` | gauge classification passes; physical representative and phase zero remain postulates |
| fused-witness phase kickback | passes on the initialized fiber; tensor substitution removes the phase response |
| `C_phi`, filters, and normalization | exact |
| stable record classicalization | exact `B^2` |
| classical erasure versus coherent unrecording | correctly distinguished |
| partial coherence and visibility | exact with overlap `gamma` |
| Barandes factorization | exact positivity interval `[-7/32,7/18]` for `cos(phi)` |
| commit isometry | passes per fixed source with orthogonal record/exhaust labels |
| exhaust partial trace | recovers the classical child law on the sealed accessible boundary |
| no dormant unchosen child | passes for accessible outputs; apparatus capability is not an active child |
| conditioned Paper 13D recovery | exact on every positive-probability branch |
| per-source `W_X` | only a fiberwise isometry; no global source-coherent Stinespring map is constructed |
| presentation covariance | passes on initialized, fusion-compatible fibers; not total on the frozen overbroad source groupoid |
| rooted spectators | passes for independently added unmarked spectators |
| restriction/deletion | passes on compatible fibers, including the declared degenerate structural quotient; does not repair the original source-domain defect |
| local process fibers | genuine outcome-indexed local instrument components, not merely final bits |
| Hilbert/Stinespring representation | operational representation of the triggered instrument, not an autonomous selector |
| activity/opportunity law | correctly unconstructed |
| root law | correctly unconstructed |
| actuality, ensemble, chronology, dimension, metric | correctly unconstructed |

## 7. Full product vector

The coordinates are returned independently for the frozen candidate, with
local scoped positives retained even though the total source theorem fails.

```text
typed local instrument
  P22-TYPED-STRUCTURAL-INSTRUMENT-UNCONSTRUCTED-AS-STATED
  (heterogeneous admitted active sorts defeat totality)

reversible coherent query
  P22-REVERSIBLE-STRUCTURAL-QUERY-CONSTRUCTED
  (fusion-compatible fixed-source initialized fibers only)

reversible accessible erasing fusion
  P22-REVERSIBLE-ERASING-FUSION-IMPOSSIBLE
  (deterministic/pure-output collision scope proved)

structural probe interference
  P22-STRUCTURAL-PROBE-INTERFERENCE-CONSTRUCTED
  (ideal closed, fusion-compatible query fibers)

dependent commit
  P22-DEPENDENT-STRUCTURAL-COMMIT-CONSTRUCTED
  (per-source instrument; no global coherent source carrier)

conditioned Paper 13D child recovery
  P22-CONDITIONED-PAPER13D-CHILD-RECOVERY-CONSTRUCTED
  (positive-probability branches and sealed exhaust only)

no dormant unchosen child
  P22-NO-DORMANT-UNCHOSEN-CHILD-PROVED
  (accessible dependent child boundary)

presentation covariance
  P22-POINT-FREE-NATURALITY-UNCONSTRUCTED-AS-GLOBALLY-CLAIMED
  P22-POINT-FREE-NATURALITY-CONSTRUCTED-ON-FUSION-COMPATIBLE-FIBERS

restriction and spectator laws
  P22-RESTRICTION-AND-SPECTATOR-LAWS-CONSTRUCTED
  (within the fusion-compatible and declared degenerate families)

local process components
  P22-INEQUIVALENT-PROCESS-FIBERS-CONSTRUCTED
  (local triggered instrument scope)

autonomous opportunity/activity law
  P22-AUTONOMOUS-ACTIVITY-LAW-UNCONSTRUCTED

root law
  P22-ROOT-LAW-UNCONSTRUCTED

Paper 17 structural-parent gate
  P22-P17-STRUCTURAL-PARENT-GATE-CLOSED-PENDING-REVISION-AND-REVIEW

Paper 17 varying-history ensemble gate
  P22-P17-VARYING-HISTORY-ENSEMBLE-GATE-CLOSED

Paper 17 chronology/dimension gate
  P22-P17-CHRONOLOGY-DIMENSION-GATE-CLOSED

actuality
  P22-ACTUALIZATION-UNCONSTRUCTED

metric
  P22-METRIC-UNCONSTRUCTED
```

## 8. Strongest honest interpretation and permanent walls

The strongest surviving result is this:

> For each fusion-compatible complete classical source, Paper 22 specifies an
> ideal triggered hybrid quantum/stochastic instrument.  Its reversible query
> coherently computes and exactly uncomputes operationally distinct tensor
> and fusion witnesses; a separately postulated fused-witness phase oracle
> and calibrated real mixer produce the exact Paper 21 interference family;
> and a per-source commit isometry yields exactly one accessible Paper 13D
> child after its sealed exhaust is traced.  The accessible fusion is not
> reversible, and no unchosen child is active in the output.

It does not yet define that instrument on every source admitted by its own
frozen `Src` definition.  It also does not construct a universal coherent
source-space Stinespring dilation, a canonical off-blank unitary extension,
or an experimental guarantee that no external environment leaks route
information.  The matrix `B` does not select the physical structural-mode
identification, the real mixer convention, the phase zero, or the phase
oracle; those are result-neutral local hypotheses of the candidate.

Nothing here constructs or identifies an autonomous opportunity/activity
law, a distribution of active marks, a root state, an actuality rule, a
varying-history ensemble, chronology, dimension, signature, topology, scale,
metric, curvature, gravity, continuum physics, or a fundamental discrete or
complex ontology.  A local positive coordinate cannot promote any of those
global coordinates.

## 9. Required revision

Before acceptance, a replacement candidate should:

1. restrict and explicitly type `Src` so every active family is in one common
   Paper 13D fusion sort, with source morphisms preserving that sort;
2. propagate that domain through `F`, `U_F`, the fused projector, `W_X`, all
   totality/naturality statements, and restriction controls;
3. state unambiguously that `W_X` is a classical-source-indexed isometry, or
   construct a source-retaining global dilation with collision-proof exhaust
   labels; and
4. retain the explicit distinction between the `B` gauge classification and
   the independently postulated physical mixer/phase calibration.

The first item is mandatory and decides this verdict.  Items 3–4 bind the
strongest quantum scope and prevent later promotion of a fiberwise
Stinespring representation into autonomous source selection.

## 10. Freeze statement

This report is frozen as the sole Seat Q artifact.  Its ordinary post-freeze
SHA-256, LF line count, and byte count are returned with the panel delivery;
they are necessarily external to the bytes whose ordinary hash they report.
No normalized self-hash convention is used.
