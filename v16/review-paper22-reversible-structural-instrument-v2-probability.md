# Paper 22 v2 independent probability and instrument-normalization review

Date: 2026-08-21

Seat: **P — probability and instrument normalization**

Verdict: **REVISE**

First decisive semantic counterexample: **the advertised general
partial-record law is wrong or underdefined for a complex environment
overlap.** With the ordinary definition
`v=<e_T|e_F>`, the interference coordinate is
`Re(v e^{i phi})`, not `Re(v)`. Taking `v=i` and `phi=pi/2` gives a maximal
fringe (`Re(i*i)=-1`), whereas the printed rule gives zero fringe because
`Re(i)=0`. This fails the pinned exact record/visibility family.

An independent delta violation also survives: the v2 candidate replaces the
adjudicated uniform `[25]` cross-pair seed purification by a biased two-state
seed even though the pin authorizes changes only to source and functor
domains.

## 1. Integrity and review boundary

The repository state and complete allowed corpus authenticated before
scientific inspection:

| object | observed ordinary SHA-256 | required | result |
|---|---|---|---|
| repository HEAD | `42d815a` | `42d815a` | match |
| v2 review protocol | `88a2609988628e8e9fe1ad2c96a0b65a9cf230a2750feab2207bca5ebfcfd30e` | same | match |
| terminal Paper 13D law | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` | same | match |
| predecessor adjudication | `c261520aa142bf07a489f87cd0364628f094794c7523c03d8ba3dde05d824a07` | same | match |
| Paper 22 v2 pin | `a4c1c2ecd10edad73ed64b12f699c09d7cfd169d4cd264939990589554693627` | same | match |
| Paper 22 v2 candidate | `30340295ccd5f8371a9020cb76c0a93cc24ab14cbbf78f05c01a85ca5ce86468` | same | match |
| Paper 22 v2 construction note | `e90bdd14ca04742bb09eb3c9ec928b4aea04ff6429b0896158ce83170280a0ae` | same | match |

I read each listed artifact completely. The old candidate was used only
through the binding predecessor adjudication and immutable numerical
anchors. I did not inspect the frontier census, semantic input audit, Paper
23 material, any private regional investigation, or any sibling report. I
did not contact another seat.

No corpus file was edited. I inspected or ran no implementation, generated
result, sampler, or scientific code. I did not stage or commit. This assigned
report is the only file written.

## 2. Independent lens reconstruction

### 2.1 Gauge class and exact lift

Let

\[
 B=\frac1{25}\begin{pmatrix}9&16\\16&9\end{pmatrix}.
\]

A two-dimensional unitary with these squared moduli can be dephased by
diagonal input and output phases so that its first column is `(3,4)/5` and
one entry of the second column is positive. Column orthogonality then forces
the remaining relative sign. Up to those diagonal phases and simultaneous
transported mode exchange, the representative is

\[
 R=\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix}.
\]

Directly,

\[
 R^T R=I,\qquad \det R=1,\qquad |R|^2=B.
\]

The real representative and phase reference remain physical apparatus data
for a composed interferometer; `B` alone does not select their phase origin.

### 2.2 Coherent phase family

Writing `c=3/5`, `s=4/5`,

\[
 R D_\phi R
 =\begin{pmatrix}
 c^2-s^2e^{i\phi}&-cs(1+e^{i\phi})\\
 cs(1+e^{i\phi})&-s^2+c^2e^{i\phi}
 \end{pmatrix}.
\]

Therefore

\[
 C_\phi
 =\frac1{625}\begin{pmatrix}
 337-288\cos\phi&288(1+\cos\phi)\\
 288(1+\cos\phi)&337-288\cos\phi
 \end{pmatrix}.
\]

Every entry is nonnegative for real `phi`, and every column sums to one.
The three frozen values are

\[
 C_0=\frac1{625}\begin{pmatrix}49&576\\576&49\end{pmatrix},
\]

\[
 C_{\pi/2}=\frac1{625}\begin{pmatrix}337&288\\288&337\end{pmatrix},
 \qquad C_\pi=I.
\]

Thus the neutral tensor-input probabilities remain exactly `49/625` and
`576/625`.

### 2.3 Stable record and restart kernel

The stable orthogonal record removes the off-diagonal route terms and gives

\[
 B^2=\frac1{625}\begin{pmatrix}337&288\\288&337\end{pmatrix}.
\]

Also

\[
 B^{-1}=\frac17\begin{pmatrix}-9&16\\16&-9\end{pmatrix},
\]

so the unique candidate in `C_phi=K_phi B` is

\[
 K_\phi=\frac1{175}\begin{pmatrix}
 63+288\cos\phi&112-288\cos\phi\\
 112-288\cos\phi&63+288\cos\phi
 \end{pmatrix}.
\]

Its columns sum to one. Entrywise positivity is equivalent to

\[
 63+288\cos\phi\ge0,
 \qquad 112-288\cos\phi\ge0,
\]

hence exactly

\[
 -7/32\le\cos\phi\le7/18.
\]

The displayed immutable `B`, `R`, `C_phi`, special phases, `B^2`, `K_phi`,
positivity interval, and neutral odds all pass exact arithmetic regression.

### 2.4 Decisive partial-record calculation

Let the complete residual route states before recombination be
`|e_T>` and `|e_F>` and define

\[
 v=\langle e_T|e_F\rangle.
\]

For tensor input, the pre-recombination state is proportional to

\[
 c|T\rangle|e_T\rangle
 +s e^{i\phi}|F\rangle|e_F\rangle.
\]

After the second `R`, every interference cross term depends on

\[
 q_{\phi,v}=\operatorname{Re}(v e^{i\phi}),
\]

and the reduced mode law is

\[
 C_{\phi,v}
 =\frac1{625}\begin{pmatrix}
 337-288q_{\phi,v}&288(1+q_{\phi,v})\\
 288(1+q_{\phi,v})&337-288q_{\phi,v}
 \end{pmatrix}.
\tag{P.1}
\]

The candidate instead says that an overlap `v` multiplies the interference
term by `Re(v)`. No assumption that `v` is real and no definition absorbing
`phi` into `v` is given. For `v=i`, `phi=pi/2`, equation (P.1) has `q=-1`
and gives `C=I`; the printed rule has `Re(v)=0` and gives the classical
`B^2`. The two complete laws are different.

Equivalently, phase-scanned visibility depends on `|v|`, not `Re(v)`. The
stable-record endpoint `v=0` and fully erased endpoint `v=1` remain correct,
but the claimed general partial-record/visibility family does not. Because
the pin freezes that family and treats a failed numerical anchor as at least
`REVISE`, this counterexample is decisive.

### 2.5 Seed-purification delta

Paper 13D fixes an independent uniform seed

\[
 v_{ij}\in[25]
\]

for every new pair. Its fusion bond is one precisely for the first `9` seed
values when endpoint colors agree and for the first `16` when they differ.
The binding predecessor adjudication explicitly preserves **uniform seed
purification** on valid homogeneous fibers.

The v2 candidate instead introduces, for each cross pair,

\[
 |\sigma\rangle=(3/5)|0\rangle+(4/5)|1\rangle.
\tag{P.2}
\]

A source-controlled output flip can make the reduced bond probabilities of
(P.2) equal `9/25` or `16/25`, so this issue does not by itself refute the
reduced Paper 13D child kernel. It does change the complete query
purification: the preserved construction has 25 equiprobable seed basis
outcomes, while (P.2) has two outcomes of probabilities `9/25` and `16/25`.
A complete middle seed/apparatus reader distinguishes them.

No environment isometry, 25-state degeneracy complement, or theorem treating
this compression as an allowed dilation gauge is constructed. The candidate
therefore changes a local seed carrier and its open-query amplitudes while
claiming that only source and functor domains changed and that no seed bias
moved. This is an independent bounded-delta failure.

### 2.6 Commit isometry and all required inner products

For fixed admitted source `X`, define

\[
 |\Psi_{X,m}\rangle
 =|m_R\rangle\sum_{[H]}
 \sqrt{\Gamma_m([H]\mid[X])}
 |H\rangle|c_{[X],m,[H]}\rangle.
\]

The declared orthonormal labels give:

- same source, same mode: the norm is
  `sum_[H] Gamma_m([H]|[X])=1`;
- same source, different modes: the stable records are orthogonal;
- different histories inside one mode: history/exhaust labels kill every
  cross term; and
- different physical source fibers: the `[X]` exhaust index makes the images
  orthogonal in the optional external direct sum.

Thus equation (15) is a valid fiberwise isometry on its blank input subspace.
Isomorphic presentations belonging to one physical `[X]` are transported by
naturality rather than counted as distinct physical source fibers.

### 2.7 Complete joint normalization and conditioning

For every admitted fixed source, input mode, and phase,

\[
 \widehat\Gamma_{\phi,X}(m,[H]\mid j)
 =C_\phi(m\mid j)\Gamma_m([H]\mid[X])
\]

satisfies

\[
 \sum_m\sum_{[H]}\widehat\Gamma_{\phi,X}(m,[H]\mid j)
 =\sum_m C_\phi(m\mid j)=1.
\]

Whenever `C_phi(m|j)>0`, conditioning gives

\[
 \widehat\Gamma_{\phi,X}([H]\mid m,j)
 =\Gamma_m([H]\mid[X]).
\]

At `phi=pi`, one branch is null for each basis input, so conditioning that
branch is undefined. The proof itself invokes a positive marginal; the
theorem must remain support-scoped despite its unqualified lead sentence.
No normalization defect follows.

### 2.8 Dependent output and no dormant child

The accessible carrier is

\[
 \coprod_{m\in\{T,F\}}
 \{m_R\}\times\mathsf{Hist}(\mathsf Y_{m,s,X}),
\]

not a Cartesian product of tensor and fusion children. A realized output has
one selected history in one summand. The sealed exhaust stores an orthogonal
label for the selected source, mode, and history; it does not carry an active
copy of the unchosen child. The temporary query witness is uncomputed before
commit. The no-dormant-child claim passes at the accessible boundary.

### 2.9 Source-propensity noninheritance

Let `L_X` denote the normalized local joint kernel above. For any normalized
external source law `mu`,

\[
 P_\mu(X,m,[H])=\mu(X)L_X(m,[H])
\]

is normalized. Take, for example,

\[
 \mu_1=\delta_{X_0},\qquad
 \mu_2=\tfrac12\delta_{X_0}+\tfrac12\delta_{X_1}.
\]

They induce the same fiberwise conditional instrument wherever their support
overlaps and different source/root frequencies. Source-indexed exhaust
orthogonality supplies no amplitudes or weights between these sectors, and
the fixed local mode odds do not distinguish `mu_1` from `mu_2`.

The candidate correctly leaves source propensity, activity, and root law
unconstructed.

## 3. Mandatory predecessor regressions

| regression | disposition |
|---|---|
| heterogeneous active-sort source | killed: `(B_1^0,B_2^0)` fails source membership before any child or probability call |
| sort-changing source morphism | killed: no arrow crosses coproduct sort summands |
| zero/one-active target conflation | killed: restrictions remain record-indexed branchwise outputs with distinct formal/atomic target types |
| same-source multi-mark closure inferred from tensoring | killed: only external tensor of separately triggered source objects is defined |
| staged fusion identified with simultaneous fusion | killed: staged words retain additional traversed boundaries |

The predecessor's decisive heterogeneous counterexample is genuinely
repaired. In particular, choosing a phase at which the undefined fusion
branch would have zero mode weight cannot admit the source: refusal occurs at
the source predicate before `C_phi` is evaluated.

## 4. Required Seat P attacks

### P-A1 — undefined heterogeneous child assigned zero probability

Take the exact heterogeneous active pair
`B_1^0({i}),B_2^0({j})`, tensor input, and `phi=pi`, where the fusion mode
would have zero probability. Attempt to set an undefined fusion child to
zero mass.

**Result:** refused. The pair is not an object of the positive coproduct, so
neither the phase nor either child is evaluated. Totality is not rescued by
`0 * undefined`.

### P-A2 — two sources sharing an unindexed exhaust basis

Suppose distinct physical sources `X != X'` can use the same child label
`H`, mode `m`, and exhaust vector `c_{m,H}`. The two orthogonal source inputs
can then have coincident output vectors, violating isometry of an external
direct sum.

**Result:** killed by `c_[X],m,[H]`. The source-orbit index makes distinct
physical fibers orthogonal without assigning their probabilities.

### P-A3 — one local law, two source measures

Multiply the same normalized fiber law by `mu_1` and `mu_2` from Section
2.9.

**Result:** both extensions normalize and retain identical local
conditionals, while their root/source statistics differ. This confirms
noninheritance.

### P-A4 — phase postselected from the final mode

Define a retrospective rule that reports `phi=0` only on fusion outcomes and
`phi=pi` only on tensor outcomes. The resulting selected sample has distorted
mode odds and no phase variable fixed before the outcome.

**Result:** it is not one admitted instrument experiment. A phase must be an
input control or have a separately specified prior joint law. The candidate
correctly refuses post-hoc phase selection, but the local kernel cannot stop
an external analyst from making this invalid inference.

## 5. Additional fresh attacks and controls

### F1 — imaginary residual overlap

Set `v=i`, `phi=pi/2`. The printed `Re(v)` prescription gives zero
interference; direct partial trace gives `Re(v e^{i phi})=-1` and a maximal
fringe. **Survives and is decisive.**

### F2 — middle-reader seed discriminator

Use one homogeneous bond-carrying source with exactly one cross-active pair.
A middle seed reader sees 25 equiprobable outcomes in the preserved uniform
purification and two biased outcomes in equation (7). **Survives as a
bounded-delta violation**, even if a coarse bond reader sees the same
`9/25,16/25` marginal.

### F3 — null-branch conditional

At tensor input and `phi=pi`, `C_pi(F|T)=0`. Dividing by that marginal is
undefined. **Killed only by the positive-support qualification in the proof;**
the theorem statement should not be read more broadly.

### F4 — phase gauge in a composed lift

Let `U_theta=R diag(1,e^{i theta})`. It has the same squared moduli `B`, but
using it on both sides of an unchanged phase element shifts the observable
family to `C_{phi+theta}` up to endpoint phases. **Killed by treating the real
`R` and phase origin as fixed apparatus hypotheses, not by `B` alone.**

### F5 — representative instead of orbit mass

If a physical history orbit contains labelled representatives of masses
`p_1,...,p_k`, using `sqrt(p_1)` in the commit would lose the other masses.
The candidate instead uses the accepted physical
`Gamma_m([H]|[X])=sum_r p_r`. **Killed; normalization uses full orbit mass.**

### F6 — degenerate pushforward mistaken for a new opportunity

Restrict a committed branch until no active component remains. Its inherited
mode mass still sums with the other branch to one, but the formal tensor unit
and empty atomic boundary remain distinct record-indexed targets. Assigning a
fresh `C_phi` would double-trigger the apparatus. **Killed by branchwise
restriction and retained `m_R`.**

### F7 — source-indexed exhaust misread as source amplitude

Attach arbitrary phases to the orthogonal external source sectors. Every
fiberwise accessible law is unchanged and no interference effect between
sources is defined. **Killed; orthogonality is typing, not a source state.**

## 6. All twenty-two hostile controls

| # | control | semantic disposition |
|---:|---|---|
| 1 | heterogeneous `(B_1^0,B_2^0)` active pair | refused before child evaluation |
| 2 | sort-changing source morphism | absent |
| 3 | empty active positive source | refused |
| 4 | one-active positive source | refused |
| 5 | tensor unit identified with empty atomic boundary | refused as type equality |
| 6 | one-factor tensor identified with atomic factor | refused without alignment |
| 7 | restriction forges a new opportunity | refused; only branch pushforward exists |
| 8 | restriction silently drops stable record | killed; `m_R` retained |
| 9 | same-source two-mark commutation | unconstructed, not inferred |
| 10 | staged fusion replaces simultaneous n-ary fusion | refused; history types differ |
| 11 | distinct sources share unindexed exhaust | killed by `[X]` index |
| 12 | exhaust orthogonality selects source amplitudes | false; no inter-source coefficients |
| 13 | spectator identity changes `C_phi` | false at fixed input controls |
| 14 | route-dependent residue after uncomputation | formal compute-phase-inverse closes on the initialized fiber |
| 15 | reversible query renamed accessible erasing fusion | explicitly refused by no-hiding split |
| 16 | accessible dormant unchosen child | killed by dependent coproduct |
| 17 | naked mode-label swap | not a gauge unless all typed controls transport |
| 18 | output decoder changed at fixed instrument | a different instrument |
| 19 | `phi` chosen after downstream result | excluded; attack P-A4 shows why |
| 20 | mutation of `B,R,C_phi`, neutral odds, or child kernel | main displayed anchors unchanged; however the full partial-record law fails and the seed purification moved |
| 21 | activity/root inferred from local odds | killed by two-source-measure construction |
| 22 | chronology/dimension/metric/gravity/actuality inferred | absent and explicitly unconstructed |

Controls 1--19 and 21--22 pass at their claimed scope. Control 20 passes for
the narrow displayed matrices and accepted reduced child kernels but not for
the complete frozen local architecture: Sections 2.4 and 2.5 give two
independent failures.

## 7. Common-gate summary

1. The homogeneous source coproduct is source-side and point-free.
2. Heterogeneous sources and sort-changing arrows are refused before
   probability.
3. Both accepted child experiments are total on each homogeneous summand;
   stochastic fusion is retained as a kernel.
4. Presentation and spectator transports do not enter local mode odds.
5. Positive restriction marginalizes independent seed factors; degenerate
   restriction remains branchwise and record indexed.
6. External tensor products normalize; they imply neither an internal
   multi-mark source nor a simultaneous-fusion algebra.
7. The fiberwise commit isometry, joint normalization, supported child
   recovery, and no-dormant-child claim pass.
8. The general partial-record probability theorem and the claimed
   source-domain-only delta do not pass.
9. No source propensity, activity, root, regional referent, chronology,
   dimension, metric, gravity, or actuality law is constructed.

## 8. Full product vector

```text
P22V2-HOMOGENEOUS-SOURCE-GROUPOID:
  CONSTRUCTED

P22V2-TOTAL-TENSOR-FUSION-CHILD-PAIR:
  CONSTRUCTED

P22V2-FIBERWISE-REVERSIBLE-QUERY:
  CONSTRUCTED

P22V2-FIBERWISE-COMMIT-INSTRUMENT:
  CONSTRUCTED

P22V2-EXACT-LOCAL-MODE-LAW:
  UNCONSTRUCTED

P22V2-POSITIVE-RESTRICTION-NATURALITY:
  CONSTRUCTED

P22V2-DEGENERATE-BRANCHWISE-RESTRICTION:
  CONSTRUCTED

P22V2-EXTERNAL-TENSOR-COMPOSITION:
  CONSTRUCTED

P22V2-SAME-SOURCE-MULTIMARK-COMPOSITION:
  UNCONSTRUCTED

P22V2-SIMULTANEOUS-FUSION-ALGEBRA:
  UNCONSTRUCTED

P22V2-ACTIVITY-ROOT-LAW:
  UNCONSTRUCTED

P22V2-PHYSICAL-REGIONAL-REFERENT:
  UNCONSTRUCTED

P22V2-CHRONOLOGY-DIMENSION-METRIC-GR:
  UNCONSTRUCTED

P22V2-ACTUALIZATION:
  UNCONSTRUCTED
```

The reversible-query coordinate records that equations (8)--(10) define a
fiberwise compute-phase-uncompute query. It does **not** ratify the claim that
its two-state seed purification is the unchanged predecessor purification.
The exact-local-mode-law coordinate is demoted because the pin includes the
partial record/visibility family, for which the candidate's general formula
fails.

## 9. Verdict and exact surviving scope

**REVISE.** The predecessor's heterogeneous-source, degenerate-restriction,
composition, and source-indexing failures are repaired. The exact principal
mode matrices and the normalized fiberwise commit also survive. Nevertheless,
the protocol makes a failed numerical anchor or mandatory local control at
least `REVISE`; the complex-overlap counterexample defeats the advertised
general partial-record law. Separately, the seed purification is not the
uniform purification preserved by the adjudication, so the candidate is not
the promised source/functor-only replacement.

The strongest surviving result is a homogeneous-source, triggered,
fiberwise query-and-commit instrument with the exact displayed
`B,R,C_phi,B^2,K_phi` anchors, normalized joint law, supported child recovery,
dependent output, branchwise restriction, and external tensor composition.
It is not yet the exact frozen v2 local instrument as a whole.

No automatic repair is authorized. Nothing here constructs a same-source
multi-mark law, fusion algebra, source measure, activity or root law,
physical regional referent, chronology, dimension, metric, curvature,
gravity, actualization, or a coherent law over source objects.

## 10. Freeze convention

This report is frozen by its final write. Its ordinary whole-file SHA-256,
LF line count, and byte count are computed afterward and supplied in the
review handoff. They are external because embedding a whole-file digest in
the same bytes would mutate the frozen object; no normalized self-hash
ceremony is used.
