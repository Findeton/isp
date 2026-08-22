# Paper 22 independent probability, identifiability, and physical-scope review

Date: 2026-08-21

Seat: **P — probability, identifiability, and physical scope**

Verdict: **ACCEPT-WITH-SCOPE**

First decisive semantic counterexample: **none**

## 1. Review boundary and authentication

I authenticated the review protocol before scientific analysis. I then
authenticated every scientific object used against the protocol's immutable
corpus and read each authenticated object completely.

| object | observed ordinary SHA-256 | required SHA-256 | result |
|---|---|---|---|
| review protocol | `157531a09b1d90ae878bfc82cdfc325fa2642cbee4df4601afc865c1f529e907` | same | match |
| Paper 13D law | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` | same | match |
| Paper 13D terminal adjudication | `ae2c4ef066335c39a0b8057c897c947b06e4270be67d1ed3ec59bf8d6d0a00c9` | same | match |
| Paper 20 dependent-parent contract | `64111d7764bf70984b959e00bc1da30ad0d6c3ae7b5c6d51b94227ad2f5c35e6` | same | match |
| Paper 21 interferometer | `ca0f709b00906971c6aac2b25b12fea11f168411ab2f440ccc49d982aab4ba80` | same | match |
| Paper 21 pin | `7df73538f87a39e22a4aa221d4c94842620fb7c8329e68d072ea98a7c7e9f9f7` | same | match |
| Paper 22 pin | `de32c02ee1be613eef4a867dadf9bc1c84fc8ed492b764f7545bb54fb91a5ae4` | same | match |
| Paper 22 candidate | `6d75a072fb3c51c5c267448fd329895f94cd4f9ee4ba4d96ea9660be80c1c6b7` | same | match |

The Paper 22 pin and candidate were reauthenticated immediately before this
report was frozen. No moving-byte event occurred.

I did not read the frontier census, the Paper 22 single-seat audit, any Paper
23 file, or any sibling report. I did not communicate with another review
seat. I inspected or ran no implementation or scientific code, and I did not
stage or commit any file. The only file I wrote is this assigned report.

## 2. Independent probability reconstruction

### 2.1 Mixer and recorded law

Write

\[
 c=3/5,\qquad s=4/5,\qquad
 R=\begin{pmatrix}c&-s\\s&c\end{pmatrix}.
\]

Direct multiplication gives `R^T R=I` and `det R=1`. Entrywise squared
moduli give the column-stochastic recorded mode law

\[
 B=|R|^2
 =\frac1{25}\begin{pmatrix}9&16\\16&9\end{pmatrix}.
\]

Both entries in every column are positive and every column sums to one.

### 2.2 Coherent law

For `D_phi=diag(1,e^{i phi})`,

\[
 A_\phi=R D_\phi R
 =\begin{pmatrix}
 c^2-s^2e^{i\phi}&-cs(1+e^{i\phi})\\
 cs(1+e^{i\phi})&-s^2+c^2e^{i\phi}
 \end{pmatrix}.
\]

Consequently

\[
 C_\phi=|A_\phi|^2
 =\frac1{625}\begin{pmatrix}
 337-288\cos\phi&288(1+\cos\phi)\\
 288(1+\cos\phi)&337-288\cos\phi
 \end{pmatrix}.
\]

For every real admitted phase, the diagonal entry lies in `[49,625]/625`,
the off-diagonal entry lies in `[0,576]/625`, and each column sums exactly to
one. In particular,

\[
 C_0=\frac1{625}\begin{pmatrix}49&576\\576&49\end{pmatrix},\quad
 C_{\pi/2}=\frac1{625}\begin{pmatrix}337&288\\288&337\end{pmatrix},\quad
 C_\pi=I.
\]

Thus the neutral tensor input has route law

\[
 \Pr(T)=49/625,\qquad \Pr(F)=576/625.
\]

Both local process components have positive mass at the neutral input.

### 2.3 Recorded composition

Ordinary matrix multiplication gives

\[
 B^2=\frac1{625}\begin{pmatrix}337&288\\288&337\end{pmatrix}.
\]

This equals `C_{pi/2}` and is independent of the phase when an orthogonal
route record remains. Deterministic visible-record reset cannot change the
zero overlap of the complete environment states, while reversing the entire
write restores unit overlap and hence `C_phi`. This is the correct
probability distinction between classical erasure and coherent unrecording.

### 2.4 Restart calculation

The recorded matrix is invertible, with

\[
 B^{-1}=\frac17\begin{pmatrix}-9&16\\16&-9\end{pmatrix}.
\]

Therefore `C_phi=K_phi B` has exactly one candidate:

\[
 K_\phi=C_\phi B^{-1}
 =\frac1{175}\begin{pmatrix}
 63+288\cos\phi&112-288\cos\phi\\
 112-288\cos\phi&63+288\cos\phi
 \end{pmatrix}.
\]

Its columns always sum to one. It is entrywise nonnegative exactly when

\[
 -7/32\leq\cos\phi\leq7/18.
\]

At `phi=0` its off-diagonal entries are `-176/175`; at `phi=pi/2` it equals
`B`; at `phi=pi` it equals `B^{-1}` and has negative diagonal entries. The
candidate therefore reproduces the exact Paper 21 distinction between
filter interference and stochastic nondivision. It does not equate those
two tests.

### 2.5 Filters, loss, and no postselection

For tensor input, multiplying the transmitted one-route amplitudes by the
same recombiner gives, with denominator 625,

| context | `p(T)` | `p(F)` | `p(loss)` | row sum |
|---|---:|---:|---:|---:|
| both | `337-288 cos(phi)` | `288(1+cos(phi))` | `0` | `625` |
| tensor only | `81` | `144` | `400` | `625` |
| fusion only | `256` | `144` | `225` | `625` |
| neither | `0` | `0` | `625` | `625` |

Hence

\[
 I_2(T)=-288\cos\phi/625,\qquad
 I_2(F)=288\cos\phi/625,\qquad
 I_2(\mathrm{loss})=0.
\]

The residual sums to zero. Blocked mass is present in the complete outcome
space and is never renormalized away. Outcome conditioning in the later
commit is therefore not being used to repair an unnormalized filter law.

### 2.6 Complete instrument law

For a fixed admitted classical source `X`, the commit dilation uses one
orthogonal record/exhaust sector for each mode and physical Paper 13D history
orbit. Its accessible joint law is

\[
 \widehat\Gamma_{\phi,X}(m,[H]\mid j)
 =C_\phi(m\mid j)\Gamma_m([H]\mid[X]).
\]

This factorization follows from the orthogonal mode blocks of the displayed
isometry: the mode amplitude is formed first and the selected block then has
conditional squared norm `Gamma_m`. It is not a second normalization rule.
Because every accepted child law is normalized,

\[
 \sum_m\sum_{[H]}\widehat\Gamma_{\phi,X}(m,[H]\mid j)
 =\sum_m C_\phi(m\mid j)=1
\]

for every source, input mode, and admitted phase.

When `C_phi(m|j)>0`, division by the marginal gives exactly

\[
 \widehat\Gamma_{\phi,X}([H]\mid m,j)
 =\Gamma_m([H]\mid[X]).
\]

The claim is correctly support scoped. At tensor input and `phi=pi`, the
fusion probability is zero and the fusion conditional is undefined; the
candidate does not claim otherwise and does not delete the fusion component
from the instrument type.

### 2.7 Orbit and seed aggregation

For a physical history orbit `O=[H]`, the accepted child probability is

\[
 \Gamma_m(O\mid[X])
 =\sum_{h\in O}\widetilde\Gamma_m(h\mid X).
\]

The commit amplitude is the square root of this complete orbit mass, not the
square root of one representative's mass. Orthogonal seed/exhaust records
make different seed preimages add as probabilities after the exhaust trace.
The orbit cells partition the presented fiber, so their aggregate masses sum
to one even in the presence of automorphism fixed points. No automorphism
factor enters `C_phi`.

### 2.8 Source and cardinality independence

At fixed input mode and fixed apparatus phase, `C_phi` acts only on the
two-dimensional structural mode. Source cardinality changes the normalized
seed state and the conditional fusion history law, but exact query inversion
returns all of those fields to blank before recombination. The route marginal
therefore contains no source, spectator, cardinality, seed count, orbit size,
or enumeration factor.

This is conditional apparatus independence. The paper supplies no law for
choosing the input mode or phase, so an external source-dependent control
policy is outside the theorem.

## 3. Assigned claim dispositions

| required probability/scope check | disposition |
|---|---|
| exact `B`, `R`, `C_phi`, `B^2`, `K_phi` calculations | pass; independently reproduced above |
| normalization for every source, mode, and phase | pass for the declared per-source instrument; filters include loss |
| joint law and conditioned-child recovery | pass on every supported branch; zero-mass conditionals are correctly excluded |
| filter loss and no postselection | pass; all four rows sum to one before conditioning |
| orbit/seed probability aggregation | pass; full orbit mass and orthogonal exhaust aggregation are used |
| source/cardinality independence of local route odds | pass at fixed `j,phi`; no phase-policy law is implied |
| operational process plurality at neutral input | pass locally: two positive instrument components with different typed codomains and futures |
| activity/root nonidentifiability | pass; the conditional instrument is invariant under arbitrary external activity and root laws |
| arbitrary-propensity rewrite | not a naked rewrite, because filters, phase kickback, records, recombination, and typed commits constrain one common apparatus; nevertheless the route law is a new physical postulate, not inherited selection |
| exact Paper 17 ceiling | local structural-parent gate only; ensemble, chronology, dimension, actuality, and metric remain closed |

The positive outputs are whole-process **instrument components** at the local
triggered opportunity: the component map, dependent target type, complete
child history, and stable record are fixed before a reader. They are not only
two target configurations produced by one unchanged component. They are also
not a probability law over arbitrary global execution complexes.

## 4. Required fresh attacks

### P1. Different activity/root pair, same local instrument

Take two admitted source values `X0,X1`. Model A uses root law `delta_X0` and
offers the instrument at every eligible mark. Model B uses root law
`(delta_X0+delta_X1)/2` and offers it with probability one half, with a
distinct no-opportunity outcome otherwise. Conditional on a positive offer
at either source, both models use exactly the same `widehat Gamma_{phi,X}`.
They disagree on root frequencies and activity counts.

Result: the local instrument cannot identify either law. This confirms
Theorem 16 rather than defeating the candidate.

### P2. Phase-dependent source law

Let an external controller set `phi(X)=0` when the number of cross-active
pairs is even and `phi(X)=pi/2` when it is odd. Tensor-input route odds then
change from `(49,576)/625` to `(337,288)/625` with the source.

Result: unconditional source independence fails under this external policy,
but the candidate claims independence only at fixed apparatus phase and
constructs no policy for choosing that phase. The attack establishes a
permanent scope wall: phase scheduling cannot be imported as a derived
source or activity law.

### P3. Zero-probability conditioned branch

At tensor input and `phi=pi`, `C_pi(F|T)=0`. The expression
`widehat Gamma(H|F,T)` cannot be recovered by division.

Result: no contradiction. The child-recovery theorem explicitly assumes
positive marginal support, while the complete instrument remains normalized
and retains the zero-weight fusion component in its declared carrier. Any
unqualified every-phase conditioning claim would be false; this report does
not award one.

### P4. Source-dependent route propensity

For any function `p(X)` in `[0,1]`, the formal law

\[
 p(X)\Gamma_T(\cdot\mid X)
 \;\sqcup\;
 (1-p(X))\Gamma_F(\cdot\mid X)
\]

is normalized, dependent-output typed, dormant-child free, and has exact
conditional child recovery wherever its branch weight is positive. Those
properties alone therefore do not identify the Paper 22 route propensity.

Result: the candidate survives only under its honest reading. Its particular
`C_phi` is fixed by the newly postulated real mixer, fused-witness phase
coupling, and Born instrument, and is tested by the common filter/record
family. It is not derived from child recovery, Paper 13D, or structural typing
alone. It must never be advertised as an autonomous or uniquely necessary
propensity.

## 5. Additional fresh semantic controls

### F1. Lift-phase gauge in a composed interferometer

Let

\[
 U_\theta=R\,\operatorname{diag}(1,e^{i\theta}).
\]

Then `|U_theta|^2=B`, so the recorded matrix alone cannot distinguish it from
`R`. If the same displayed lift is used on both sides of an unchanged
`D_phi`, direct multiplication gives a law `C_{phi+theta}` up to endpoint
phases. Thus row/column phases that are harmless for a single recorded use
are not automatically harmless in a composed interferometer unless the wire
identification and phase-control origin are transported with them.

Result: the candidate is well defined because it explicitly fixes the real
`R`, the fused-witness projector, and `D_phi`; however, `B` alone does not
identify the neutral interferometric phase. The real lift and its phase
reference are part of the new Paper 22 apparatus postulate. This is the
strongest nonfatal scope qualification found in this review.

### F2. Random phase mixture

If an external preparation randomizes the phase with law `rho`, averaging
gives the same matrix formula with `cos(phi)` replaced by
`E_rho[cos(phi)]`. A symmetric uniform phase law removes the fringe and
returns `B^2` even without a stable route record.

Result: normalization survives, but phase preparation is empirically
relevant and is not selected by the instrument. The candidate correctly
treats `phi` as an apparatus input rather than a cosmological constant.

### F3. Reused or nonorthogonal exhaust label

If two different child-history orbits share a nonorthogonal exhaust state,
tracing the exhaust can retain off-diagonal terms between their accessible
history vectors. Complete lawful child effects could then distinguish the
output from the accepted classical Paper 13D mixture.

Result: the displayed commit explicitly chooses orthogonal
`c_{m,[H]}` states, so the attack is blocked. Orthogonality is substantive;
the partial trace alone would not have guaranteed exact child recovery.

### F4. Representative-mass substitution

Consider an orbit with two distinct labelled histories of masses `p1,p2`.
Replacing the orbit coefficient `sqrt(p1+p2)` by `sqrt(p1)` would lose `p2`
and generally destroy normalization after quotienting.

Result: equation (12) uses the already pushed-forward physical mass
`Gamma_m([H]|[X])=p1+p2`; the candidate passes. Fixed points remain once,
with their actual probability, rather than receiving an invented group-size
factor.

### F5. Collision between distinct sources

Two nonisomorphic classical sources can have overlapping accessible child
labels. A single coherent global isometry that omitted the source from its
exhaust could then map orthogonal source states to nonorthogonal outputs.

Result: the construction supplies `W_X` per fixed classical source object and
claims naturality under presentation isomorphisms; it does not supply a
coherent superposition or one common unitary across different source objects.
There is no local probability defect, but no global coherent-source law is
awarded.

### F6. Degenerate restriction

Delete occurrences until fewer than two nonempty active components remain.
The tensor and fusion predictive child descriptors then coincide. Pushing the
mode law to the merged structural descriptor gives mass
`C_phi(T|j)+C_phi(F|j)=1`.

Result: no probability is created or destroyed. The candidate correctly
separates the merged accessible structural class from the still-readable
apparatus component record until that record is erased.

### F7. Two disjoint triggered instruments

For disjoint fixed opportunities, the tensor product joint law has total mass

\[
 \left(\sum_{m,H}\widehat\Gamma^{(1)}(m,H)\right)
 \left(\sum_{n,G}\widehat\Gamma^{(2)}(n,G)\right)=1.
\]

Result: local tensor composition is normalized and order independent. It
does not assign the probability, placement, or order of the two
opportunities, so it supplies no scheduler or chronology.

### F8. Unrelated-control phase substitution

Replace the fusion query by a second tensor query while retaining the
projector on the fused query-witness subspace. Both route images then lie in
the tensor subspace, so the projector acts trivially and there is no
phase-dependent response.

Result: the candidate passes. Its fringe is attached to an operationally
fused witness, not merely to a renamed control-mode phase.

## 6. Common semantic questions

1. **Carrier typing:** The fixed classical source, structural mode, query
   witness, seed purification, complement, record, exhaust, and two dependent
   child codomains are sufficiently typed for the local probability theorem.
2. **No hiding:** A reversible query retains source/seed/complement data and
   uncomputes them; accessible committed fusion remains an irreversible
   channel. These claims are not conflated.
3. **Operational route meaning:** The complete open-query witnesses and the
   dependent commit codomains distinguish tensor and fusion independently of
   the printed bit.
4. **Exact uncomputation:** On the declared blank, per-source query subspace,
   the controlled inverse restores every route-distinguishing field. Any
   residual overlap below one moves to the partial-coherence family.
5. **Normalization/recovery:** The complete instrument is normalized, and
   supported conditioning returns the exact accepted children.
6. **Covariance/spectators/restriction/composition:** The probability laws use
   orbit aggregation, fixed-phase local odds, summed degenerate fibers, and
   normalized products. No autonomous schedule follows.
7. **Process status:** The positive outputs are inequivalent local instrument
   components, not merely target configurations, but they are not an
   arbitrary-global-process ensemble.
8. **Unconstructed physics:** Opportunity/activity, active-mark placement,
   root preparation, actuality, varying-history ensemble, chronology,
   dimension, and metric remain unidentified and unconstructed.

## 7. Claim-by-claim product disposition

| coordinate | disposition | scope |
|---|---|---|
| typed local instrument | constructed | fixed classical source and triggered local apparatus |
| reversible coherent query | constructed | per-source dilation on the declared blank subspace |
| reversible accessible erasing fusion | impossible | reversibility requires a distinguishing complement |
| structural probe interference | constructed | conditional on fixed real mixer and phase reference |
| dependent commit | constructed | one accessible dependent child per outcome |
| conditioned Paper 13D child recovery | constructed | positive-probability branches only |
| no dormant unchosen child | proved | sealed exhaust stores selected history/complement, not an active other child |
| presentation covariance | constructed | physical orbit mass; source isomorphisms transport the apparatus |
| restriction and spectator laws | constructed | fixed phase; degenerate restrictions merge and sum structural masses |
| local process components | constructed | local instrument-process fibers, not global execution-complex ensemble |
| autonomous opportunity/activity law | unconstructed | nonidentifiable from the conditional instrument |
| root law | unconstructed | nonidentifiable from the conditional instrument |
| Paper 17 structural-parent gate | open conditional on panel adjudication | local dependent-output parent only |
| Paper 17 varying-history ensemble gate | closed | no opportunity/placement/schedule law |
| Paper 17 chronology/dimension gate | closed | no global ensemble or operational chronology |
| actuality | unconstructed | normalized possibilities only |
| metric | unconstructed | no geometric interpretation follows |

## 8. Full product vector

```text
typed local instrument
  P22-TYPED-STRUCTURAL-INSTRUMENT-CONSTRUCTED

reversible coherent query
  P22-REVERSIBLE-STRUCTURAL-QUERY-CONSTRUCTED

reversible accessible erasing fusion
  P22-REVERSIBLE-ERASING-FUSION-IMPOSSIBLE

structural probe interference
  P22-STRUCTURAL-PROBE-INTERFERENCE-CONSTRUCTED

dependent commit
  P22-DEPENDENT-STRUCTURAL-COMMIT-CONSTRUCTED

conditioned Paper 13D child recovery
  P22-CONDITIONED-PAPER13D-CHILD-RECOVERY-CONSTRUCTED-ON-SUPPORT

no dormant unchosen child
  P22-NO-DORMANT-UNCHOSEN-CHILD-PROVED

presentation covariance
  P22-POINT-FREE-NATURALITY-CONSTRUCTED

restriction and spectator laws
  P22-RESTRICTION-AND-SPECTATOR-LAWS-CONSTRUCTED

local process components
  P22-INEQUIVALENT-PROCESS-FIBERS-CONSTRUCTED-LOCAL-INSTRUMENT-SCOPE

autonomous opportunity/activity law
  P22-AUTONOMOUS-ACTIVITY-LAW-UNCONSTRUCTED

root law
  P22-ROOT-LAW-UNCONSTRUCTED

Paper 17 structural-parent gate
  P22-P17-STRUCTURAL-PARENT-GATE-OPEN-CONDITIONAL-ON-ADJUDICATION

Paper 17 varying-history ensemble gate
  P22-P17-VARYING-HISTORY-ENSEMBLE-GATE-CLOSED

Paper 17 chronology/dimension gate
  P22-P17-CHRONOLOGY-DIMENSION-GATE-CLOSED

actuality
  P22-ACTUALIZATION-UNCONSTRUCTED

metric
  P22-METRIC-UNCONSTRUCTED
```

## 9. Strongest honest interpretation and permanent walls

The strongest supported interpretation is one new, triggered, local
structural instrument. At a fixed classical source and fixed apparatus
controls, it coherently queries operationally distinct tensor and fusion
witnesses, erases every query-side route record by exact inversion, and then
commits exactly one dependent Paper 13D child. At the neutral calibration it
assigns positive mass to two inequivalent local instrument-process
components. Its complete filter, record, and phase controls make this more
than a naked output-bit decoder.

The real structural mixer, its physical identification with the two query and
commit components, the fused-witness phase coupling, the phase reference, and
the Born instrument rule are Paper 22 physical hypotheses. The accepted
matrix `B`, dependent typing, normalization, and conditional child recovery
do not uniquely derive those hypotheses or their route propensity.

Permanently outside this result are a law that offers opportunities, a
distribution of active marks, a source-dependent or cosmological phase
policy, a root distribution, a coherent law over distinct source objects, an
actualization rule, an autonomous varying-history ensemble, a scheduler,
chronology, dimension, topology, signature, scale, metric, curvature,
gravity, continuum physics, and any claim that the finite Hilbert/Stinespring
representation is ontologically fundamental.

## 10. Final verdict and freeze convention

**ACCEPT-WITH-SCOPE.** No decisive semantic counterexample was found. The
probability construction is exact and normalized at its declared local
triggered scope. Acceptance must bind the support qualification for
conditioning and the fact that the real lift/phase reference and local route
law are newly postulated apparatus physics, not an inherited autonomous
selector.

This file is frozen by its final write. Its ordinary whole-file SHA-256, LF
line count, and byte count are computed after that write and supplied in the
review handoff. They are intentionally external: embedding a whole-file hash
inside the same bytes would change the object, and the protocol requires no
normalized self-hash ceremony.
