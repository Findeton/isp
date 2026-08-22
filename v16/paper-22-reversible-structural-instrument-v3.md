# A homogeneous-source reversible structural instrument on the bound apparatus

## Typed coherent query, dependent commit, and the exact partial-visibility law

### Abstract

We complete the twice-adjudicated homogeneous-source structural instrument
with exactly two repairs and no new physical hypothesis. The source domain,
both child functors, the commit, both restriction laws, external composition,
and every exact numerical anchor are inherited verbatim from the adjudicated
v2 survivors. The first repair restores the bound fine-seed apparatus of the
original Paper 22 construction: one independent uniform `[25]` seed per
unordered cross-active pair, its Householder purification, reversible
witness computations reading seeds as data, and exact uncomputation before
recombination. The second repair states and proves the general
partial-record interference law with complex environment overlap
`gamma = <e_T|e_F>`: the interference coordinate is
`q_phi = Re(gamma e^{i phi})`, not `Re(v)`. The registered regression
control `gamma = i`, `phi = pi/2` yields `C = I_2` — deterministic return —
where the rejected candidate's false `Re(v)` rule predicted phase
independence. The result is the complete triggered local instrument on
homogeneous source fibers: fiberwise reversible query on the bound
apparatus, dependent commit with exact child recovery, and the exact local
mode law including the full partial-visibility family. It supplies no
activity, root, chronology, dimension, metric, gravity, or actualization
law.

## 1. Binding scope

The mathematical object is bound by the frozen Paper 22 v3 pin with
ordinary SHA-256
`317413256dda84eac1213000660575b9b0d30f6d25e58f09515e230005c0c83e`.
The pin binds the terminal conditional law, the exact Paper 21
interferometer, both predecessor candidates and adjudications, and the
downstream Paper 23 preparation pin. This paper is the one authorized
successor under the v2 adjudication's stopping rule; it introduces no
fitted coefficient, phase, seed bias, channel weight, dimension, or
geometry.

The two repairs are exactly:

1. **Restoration (Section 5).** Every apparatus object is the v1
   construction at its printed content: seed space `Xi_X = [25]^{P_X}`,
   uniform product law `mu_X = 25^{-|P_X|}`, purified state
   `|Omega_X>`, Householder preparation `S_X`, fine-seed witness
   computations, and exact closure. The v2 substitutions (biased qubit,
   coarse bond bit, undefined fine-to-coarse isometry) are absent.
2. **Partial visibility (Theorem 7).** The general complex-overlap law (V)
   replaces the false `Re(v)` sentence, with all four pin-registered
   consequences proved as named results.

Sections 2–4 and 8–14 are the v2 adjudicated survivors at unchanged
content; their numbering follows the v2 paper.

## 2. Atomic sorts and homogeneous sources

Let `Sort` denote the set of accepted atomic boundary sorts. A sort includes
all stage, record, and endpoint qualifiers carried by the boundary type. For
each sort `s` and finite occurrence set `I`, let

$$
B_s(I)
$$

be the set of complete legal boundary values of that sort on `I`.

### Definition 1 — positive source object

For fixed `s`, an object of the positive source groupoid

$$
\mathsf{Src}^{\ge 2}_s
$$

is a tuple

$$
X=
\left(
s,
\{X_\alpha\}_{\alpha\in A},
\{X_\epsilon\}_{\epsilon\in E},
A
\right)
$$

such that:

1. `A` is a finite physically marked family of at least two nonempty active
   components;
2. each active component has the common sort `s`,
   (X_\alpha\in B_s(I_\alpha));
3. the active occurrence sets are pairwise disjoint;
4. every active value is complete and legal;
5. each spectator (X_\epsilon\in B_{s_\epsilon}(I_\epsilon)) is complete
   and legal, with no requirement that (s_\epsilon=s); and
6. no component order, serialization order, loop index, or history identifier
   is data of the object.

The total positive source is the coproduct

$$
\mathsf{Src}^{\ge2}_{\mathrm{hom}}
=
\coprod_{s\in\mathsf{Sort}}
\mathsf{Src}^{\ge2}_s.
\tag{1}
$$

The displayed decomposition and active mark form part of the experimental
frame. They do not change the fields of the underlying tensor boundary

$$
\underline X=
\left(\boxtimes_{\alpha\in A}X_\alpha\right)
\boxtimes
\left(\boxtimes_{\epsilon\in E}X_\epsilon\right).
\tag{2}
$$

### Definition 2 — source arrows

An arrow in (mathsf{Src}^{\ge2}_s) consists of accepted presentation maps,
component and occurrence bijections, and spectator transports preserving:

- the common active sort `s`;
- the active/spectator mark;
- every complete boundary field; and
- the unordered incidence of the active family.

There is no arrow between distinct coproduct summands. In particular, a
relabeling cannot turn a heterogeneous active family into a homogeneous one.

### Proposition 1 — decidability and refusal

Membership in (1) is decided entirely from source-side type and completeness
data. It neither evaluates nor inspects a proposed fusion child, mode result,
probability, or downstream observable.

**Proof.** Finiteness, nonemptiness, pairwise disjointness, completeness, and
equality of the active sort are predicates on the supplied source. If any
predicate fails, no object of a coproduct summand exists and hence no child
functor can be called. If they all pass, the unique summand is indexed by the
common sort. None of these tests mentions a target. (square)

### Exact source controls

Choose two complete singleton values

$$
X_i,X_j\in B^0_1(\{i\}),B^0_1(\{j\}).
$$

They form a legal homogeneous active pair. A complete spectator of sort
(B^0_2) may be appended and leaves the active summand unchanged. By contrast,

$$
X_i\in B^0_1(\{i\}),
\qquad
Y_j\in B^0_2(\{j\})
$$

do not form an object of (1). Their active sorts differ, so the pair is
refused before simultaneous fusion is evaluated. A purported source arrow
that changes (B^0_1) to (B^0_2) is absent for the same reason.

These are type refusals, not zero-probability events.

## 3. The two child experiment functors

Fix (X\in\mathsf{Src}^{\ge2}_s).

### Definition 3 — tensor child

The tensor target type is

$$
\mathsf Y_{T,s,X}
=
\left(\boxtimes_{\alpha\in A}B_s(I_\alpha)\right)
\boxtimes
\left(\boxtimes_{\epsilon\in E}B_{s_\epsilon}(I_\epsilon)\right).
\tag{3}
$$

The tensor child experiment is

$$
\mathcal T_s(X)
=
\left(
\underline X,
\operatorname{id}_{\underline X},
\mathsf Y_{T,s,X},
\Gamma_{T,s,X}
\right).
\tag{4}
$$

The identity is the accepted tensor history on the formal tensor source. It
does not identify the formal tensor object with one atomic boundary.

### Definition 4 — fusion child

The fusion target type is

$$
\mathsf Y_{F,s,X}
=
B_s\!\left(\bigsqcup_{\alpha\in A}I_\alpha\right)
\boxtimes
\left(\boxtimes_{\epsilon\in E}B_{s_\epsilon}(I_\epsilon)\right).
\tag{5}
$$

Let

$$
\Phi_s^{\{I_\alpha\}_{\alpha\in A}}
$$

be the accepted single simultaneous (A)-ary fusion generator at sort `s`.
Then

$$
\mathcal F_s(X)
=
\left(
\underline X,
\Phi_s^{\{I_\alpha\}}
\boxtimes\operatorname{id}_E,
\mathsf Y_{F,s,X},
\Gamma_{F,s,X}
\right).
\tag{6}
$$

At a bond-carrying sort, fusion is a stochastic arrow. The functor therefore
assigns a typed experiment and a conditional history kernel, not one
deterministic target value. It introduces neither a binary fold nor a physical
bracketing order.

### Theorem 1 — total typed child pair

Equations (4) and (6) define total natural child-experiment functors on every
summand (mathsf{Src}^{\ge2}_s).

**Proof.** Every active component has the one sort required by the accepted
simultaneous fusion generator; every occurrence family is finite, nonempty,
and pairwise disjoint; and every component value is complete. Thus both the
formal tensor and the single simultaneous fusion arrow have typed sources and
targets. Spectators are carried by their own identity arrows and need not
share the active sort. Accepted presentation maps transport the complete
family, its unordered incidence, and the Paper 13D tensor and fusion arrows.
Equivariance of the accepted kernels supplies the naturality squares. No
undefined value is assigned probability zero. (square)

### Proposition 2 — operational distinction

The two children are operationally different on every positive source. The
tensor target retains the active partition and has no cross-active bond
address. The fusion target is one atomic boundary on the union and, where the
sort carries bonds, has the accepted positive cross-active bond law. A
complete child reader can distinguish these interfaces.

This distinction is typed and predictive. It is not the renaming of a route
bit.

## 4. Why query and commit are separate

### Theorem 2 — finite reversible-erasure obstruction

Let (f:S\to Y) be a many-to-one accessible fusion map on a finite set. No
bijection on `S` can implement `f` as its only output. Every reversible
extension

$$
\widetilde f:S\longrightarrow Y\times C
$$

must distinguish any (x\ne x') with (f(x)=f(x')) in the complement:

$$
\widetilde f(x)=(f(x),c_x),
\quad
\widetilde f(x')=(f(x),c_{x'}),
\quad
c_x\ne c_{x'}.
$$

**Proof.** Injectivity of (widetilde f) forbids equal output pairs for
distinct inputs. (square)

### Theorem 3 — pure quantum no-hiding form

Let (V:\mathcal H_S\to\mathcal H_Y\otimes\mathcal H_C) be an isometry. If
two orthogonal inputs have the same pure accessible state (|y\rangle), then

$$
V|x_k\rangle=|y\rangle|c_k\rangle
$$

with orthogonal complement states (langle c_0|c_1\rangle=0).

**Proof.** Purity of the reduced state forces a product vector with first
factor (|y\rangle). Isometry preserves the zero inner product, so the second
factors are orthogonal. (square)

Consequently a reversible fusion query must retain the partition information
temporarily. If that complement remains readable, it carries which-route
information and prevents interference. The query must therefore uncompute it
before recombination. The later accessible fusion commit is a different,
generally irreversible, child channel.

## 5. Fiberwise reversible query on the bound apparatus

All coherent equations in this section are indexed by one fixed classical
source (X\in\mathsf{Src}^{\ge2}_s). There is no coherent superposition or
probability law over different source objects.

This section is repair 1. Every apparatus object below is the v1 candidate,
Sections 5.1–5.3, at its printed content, now placed on the adjudicated
homogeneous domain. The nine-versus-sixteen split appears only as the
accepted Paper 13D beta clause `beta(a,u) = a` for `u < 9` and `1-a`
otherwise; it is read by witness computations and never redefined, repartitioned,
or coarse-grained inside this instrument.

### 5.1 Cross-pair seed space and purification

For source `X`, let `P_X` be the set of unordered cross-active occurrence
pairs. The accepted Paper 13D seed law assigns an independent uniform seed
in `[25]` to every pair:

$$
 \Xi_X=[25]^{P_X},
 \qquad
 \mu_X(\xi)=25^{-|P_X|}.
$$

Introduce a blank seed value orthogonal to the seed basis and the normalized
state

$$
 |\Omega_X\rangle
 =5^{-|P_X|}\sum_{\xi\in\Xi_X}|\xi\rangle.
\tag{7}
$$

The coefficient is exact because `sqrt(25^{-|P_X|})=5^{-|P_X|}`.

The Householder reflection through

$$
 |v_X\rangle
 =\frac{|0_\Xi\rangle-|\Omega_X\rangle}{\sqrt2}
$$

defines a canonical unitary

$$
 S_X=I-2|v_X\rangle\!\langle v_X|
$$

with

$$
 S_X|0_\Xi\rangle=|\Omega_X\rangle,
 \qquad S_X^{-1}=S_X.
\tag{8}
$$

Presentation morphisms merely permute `P_X` and the seed basis, so (7) and
(8) are natural.

### Theorem 4 — seed preparation naturality on the bound apparatus

For every source arrow (g:X\to X'), the transport of (|Omega_X>) is
(|Omega_{X'}>), the transport of (S_X) is (S_{X'}), and the blank value is
fixed.

**Proof.** A source arrow is a bijection of occurrence sets together with
accepted presentation maps. It permutes `P_X` and hence the seed basis
factorwise. The uniform superposition (7) is invariant under any basis
permutation, so its transported vector is (|Omega_{X'}>). The Householder
vector (|v_X>) is a fixed linear combination of two transported states, so
(S_{X'}) is the transport of (S_X). The blank `|0_Xi>` is a single basis
state carried to the corresponding blank. (square)

### 5.2 Reversible witness computations

Let `Q` be a query register whose typed basis includes a blank value,
complete tensor witnesses, and complete fused witnesses. Reversible basis
computations are defined by

$$
 C_{T,X}:|X,0_Q\rangle
 \longmapsto |X,T(X)\rangle,
$$

and

$$
 C_{F,X}:|X,\xi,0_Q\rangle
 \longmapsto |X,\xi,F(X,\xi)\rangle.
$$

The tensor computation reads no seed: the tensor child retains the partition
and draws no cross-pair seed. The fusion computation reads the complete seed
assignment `xi` as data: the accepted fused witness `F(X,xi)` is the typed
value generated by the accepted simultaneous fusion kernel from the complete
source and its cross-pair seeds. The source and seed remain present, so both
maps are injective on their declared subspaces and extend by inverse pairing
to permutations of the full basis.

Set

$$
 U_{T,X}=C_{T,X},
 \qquad
 U_{F,X}=C_{F,X}(S_X\otimes I),
\tag{9}
$$

and

$$
 U_{Q,X}
 =|T\rangle\!\langle T|\otimes U_{T,X}
  +|F\rangle\!\langle F|\otimes U_{F,X}.
\tag{10}
$$

The orthogonal mode projectors make (10) unitary. Its inverse is obtained by
reversing each controlled block.

### Theorem 5 — exact query closure

For every admitted source and both structural modes,

$$
 U_{Q,X}^{-1}U_{Q,X}
 |m,X,0_\Xi,0_Q\rangle
 =|m,X,0_\Xi,0_Q\rangle.
\tag{11}
$$

Every source, seed, query witness, partition complement, and reversible
apparatus coordinate returns to its common blank value.

**Proof.** Each block in (10) is unitary. The fusion block reverses the
fused-witness computation and then applies the self-inverse seed preparation
(8). The orthogonal mode blocks do not mix. Equation (11) follows directly.
(square)

### 5.3 What the query is and is not

During the open query, a complete middle reader can distinguish the tensor
and fused witnesses on the fine `[25]`-indexed register. The fusion block
retains the source partition and seed because Theorems 1–2 require it. It is
therefore a reversible fusion query, not the final accessible Paper 13D
fusion.

After (11), none of those fields remains available to distinguish the mode.
This is the exact condition needed for recombination. A seed value present
at recombination would be caught by Theorem 5: closure returns every seed
address to blank, and any residual seed trace is a detectable violation of
(11).

### 5.4 Structural phase kickback

Let `Z_{Q,F}` be the point-free projector on the fused typed subspace of the
open query register. It is defined by the complete query target type, not by
the printed mode label. Apply while the query is open

$$
 P_\phi=e^{i\phi Z_{Q,F}}.
\tag{12}
$$

`P_phi` leaves every classical structural field and every seed probability
unchanged. It multiplies a complete fused query witness by `e^{i phi}` and a
tensor query witness by one. Hence, on the blank source/query subspace,

$$
 U_{Q,X}^{-1}P_\phi U_{Q,X}
 =D_\phi\otimes I,
 \qquad
 D_\phi=\operatorname{diag}(1,e^{i\phi}).
\tag{13}
$$

Equation (13) is physical phase kickback: the relative mode phase is
generated by an operation on the structural witness while that witness
exists, and all structural registers are nevertheless blank afterward.

If the `F` query is replaced by a second tensor query, both images lie in
the tensor subspace. Then `P_phi` acts as the identity on both modes and the
effective relative phase is zero for every requested `phi`. This
substitution is a held-out discriminator between a structural phase and an
unrelated mode-only phase shifter.

## 6. Exact mode and coherent probe law

### Theorem 6 — minimal calibrated lift

The two-mode real orthogonal lift of

$$
B=
\frac1{25}
\begin{pmatrix}9&16\\16&9\end{pmatrix}
$$

is, up to diagonal input phases, diagonal output phases, and simultaneous
exchange of the physically transported modes,

$$
R=
\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix}.
\tag{14}
$$

**Proof.** The entry moduli are fixed by `B`. Orthogonality forces opposite
relative signs in one column and fixes the second column once the first is
chosen. Row/column phases and simultaneous basis exchange are the remaining
gauge. (square)

With both routes open, the mode amplitude is exactly

$$
 A_\phi=R D_\phi R,
$$

and the coherent probe law is

$$
 C_\phi=|A_\phi|^2
 =\frac1{625}
 \begin{pmatrix}
 337-288\cos\phi&288(1+\cos\phi)\\
 288(1+\cos\phi)&337-288\cos\phi
 \end{pmatrix}.
\tag{15}
$$

Every column sums to one. At (phi=0), (C_0) has diagonal `49/625` and
off-diagonal `576/625`. At (phi=pi/2), (C_{pi/2}=B^2). At (phi=pi),
(C_pi=I).

**Proof.** Direct multiplication gives diagonal amplitude
((9-16e^{i\phi})/25) and off-diagonal amplitude
(12(1+e^{i\phi})/25). Squared moduli give (15). (square)

## 7. The exact partial-visibility law

This section is repair 2. It replaces the rejected candidate's sentence
multiplying the interference term by `Re(v)`. The law is stated in the pin
before construction; what follows is its derivation and its four registered
consequences.

Let `|e_T>` and `|e_F>` be all residual witness, record, and environment
states immediately before recombination — the fields not returned to blank
by a partial uncomputation — and define the overlap

$$
 \gamma=\langle e_T|e_F\rangle,
 \qquad |\gamma|\leq 1,
 \qquad
 q_\phi=\operatorname{Re}\!\left(\gamma\,e^{i\phi}\right).
\tag{16}
$$

### Theorem 7 — general partial-visibility law

For arbitrary complex `gamma` with `|gamma|<=1`, the complete reduced probe
law after recombination is

$$
 C_{\phi,\gamma}
 =\frac1{625}
 \begin{pmatrix}
 337-288\,q_\phi&288(1+q_\phi)\\
 288(1+q_\phi)&337-288\,q_\phi
 \end{pmatrix}.
\tag{17}
$$

**Proof.** Fix the input mode and let `b_T`, `b_F` be its first-lift route
amplitudes: `(b_T,b_F)=(3/5,4/5)` for tensor input and `(b_T,b_F)=(-4/5,3/5)`
for fusion input. After the kickback (13), the open-route state is

$$
 b_T|T\rangle|e_T\rangle+b_F e^{i\phi}|F\rangle|e_F\rangle,
$$

with residual overlap `gamma=<e_T|e_F>`. The second lift sends detector `j`
the amplitude `b_TR_{jT}|e_T>+b_FR_{jF}e^{i\phi}|e_F>`. Its Born probability
is

$$
 p_j
 =(b_Tr_{jT})^2+(b_Fr_{jF})^2
 +2\,\mathrm{Re}\!\left(b_Tr_{jT}\,\overline{b_Fr_{jF}}\,e^{i\phi}\,\gamma\right),
$$

where `r_{jT}`, `r_{jF}` denote the entries of `R`. The baseline terms are
`gamma`-independent sums of squared moduli and evaluate, for both inputs,
to `337/625` on the diagonal detector and `288/625` on the crossed detector.
The interference term carries the route-amplitude product
`(b_Tr_{jT})(b_Fr_{jF})=\pm144/625`, whose magnitude with the leading
factor `2\operatorname{Re}(\cdot)` gives exactly the coefficient
`288/625`; substituting (16), it contributes
`-(288\,q_\phi)/625` to each diagonal entry and
`+(288\,q_\phi)/625` to each off-diagonal entry. Collecting terms for
both inputs gives (17).
Normalization: each column equals the `gamma=0` baseline plus `q_phi` times
a signed matrix whose columns sum to zero, so every column of (17) sums to
one for every admissible `gamma`. Entrywise positivity: for `|q_phi|<=1`
every entry of (17) lies in `[0,1]` because `337-288q in [49,625]` and
`288(1+q)in[0,576]`; hence (17) is a genuine stochastic matrix for every
admissible `gamma`. (square)

The proof shows where the rejected candidate's rule fails: the interference
factor is the full complex rotation `gamma e^{i phi}` projected onto the
real axis, not `gamma` alone.

### Corollary 7.1 — registered regression control

At `gamma = i` and `phi = pi/2`:

$$
 q_\phi=\operatorname{Re}\!\left(i\,e^{i\pi/2}\right)
 =\operatorname{Re}(i\cdot i)=\operatorname{Re}(-1)=-1,
$$

so

$$
 C_{\pi/2,\,i}
 =\frac1{625}
 \begin{pmatrix}
 337+288&288(1-1)\\
 288(1-1)&337+288
 \end{pmatrix}
 =I_2.
$$

Every input mode returns deterministically from its own detector. The
environment states `|e_T> = i|e_0>`, `|e_F> = -|e_0>` represent the same
ray and retain no which-route information; their overlap is
`gamma=<e_T|e_F>=i`, and the interference phase cancels the route phase
exactly at this setting.
The rejected candidate's rule `Re(v) = 0` instead left the law
phase-dependent at `B^2` here, which is false. More generally, along
`gamma = e^{i\theta}` the law is (15) with `phi` shifted by `+theta`: a
pure fringe displacement preserving the coherent-row visibilities
`(288/337)` and `1`.

### Corollary 7.2 — endpoint laws

- `gamma = 1`: (17) is (15), the coherent law `C_phi`.
- `gamma = 0`: (17) is `B^2` — a stable orthogonal route record, or a
  classical erasure leaving an orthogonal environment trace.
- complete reversible erasure of every record copy: the residual states
  return to a common blank, `gamma = 1`, and (15) is restored.

### Corollary 7.3 — visibility audit

Scanning `phi` at fixed `gamma`: the `288(1+q_phi)` row ranges over
`288(1\pm|\gamma|)`, giving visibility `|gamma|`; the `337-288q_phi` row
ranges over `337\pm288|\gamma|`, giving visibility `(288/337)|gamma|`. For
full coherence these are `1` and `288/337`; for a stable record both
vanish. Visibility is a direct audit of residual which-route information,
not an independent postulate.

### Corollary 7.4 — scope

The unique stochastic continuation `K_phi = C_phi B^{-1}` and its positivity
interval `(-7/32 <= cos phi <= 7/18)` remain certified at `gamma = 1` scope.
No generalized continuation through arbitrary `gamma` is constructed or
claimed here.

## 8. Fiberwise dependent commit

For each fixed admitted source `X`, let ([H]) range over physical complete
history classes of the selected child experiment and let
(Gamma_m([H]\mid[X])) be its accepted normalized conditional law.

### Definition 5 — commit isometry

On the blank output subspace define

$$
W_X|m,X,0_Y,0_C,0_R\rangle
=
|m_R\rangle
\sum_{[H]}
\sqrt{\Gamma_m([H]\mid[X])}
|H\rangle_Y|c_{[X],m,[H]}\rangle_C.
\tag{18}
$$

The exhaust labels are orthonormal and source indexed. Their purpose is to
dilate the already specified child kernel, not to define amplitudes among
sources.

### Theorem 8 — fiberwise isometry

Equation (18) is an isometry on the declared blank input subspace for every
admitted source.

**Proof.** Within fixed `m`, orthogonality of complete history/exhaust labels
and normalization of (Gamma_m) give unit norm. Distinct modes have
orthogonal stable record states. Distinct classical source fibers have
source-indexed orthogonal exhaust labels if embedded in an optional external
direct sum. (square)

### Definition 6 — accessible dependent output

The accessible output is the dependent sum

$$
\mathsf Y_X
=
\coprod_{m\in\{T,F\}}
\{m_R\}\times\mathsf{Hist}(\mathsf Y_{m,s,X}).
\tag{19}
$$

It is not a product containing both child systems. The complement/exhaust is
inaccessible after the declared commit boundary.

### Theorem 9 — joint law, normalization, and child recovery

For mode input `j`, phase `phi`, fixed admitted source `X`, and residual
overlap `gamma`, the accessible joint law is

$$
\widehat\Gamma_{\phi,\gamma,X}(m,[H]\mid j)
=
C_{\phi,\gamma}(m\mid j)\Gamma_m([H]\mid[X]).
\tag{20}
$$

For the constructed instrument `gamma=1` by exact closure (11), which
recovers the printed `C_phi` form. It normalizes, and conditioning on
`m` recovers the exact accepted child law.

**Proof.** Summing first over histories gives `1` for each selected child;
summing over modes gives the column normalization of (C_{phi,gamma}).
Division by the positive mode marginal cancels that factor and leaves
(Gamma_m).
(square)

For tensor input and neutral phase,

$$
\Pr(T)=\frac{49}{625},
\qquad
\Pr(F)=\frac{576}{625}.
\tag{21}
$$

Both triggered process components therefore occur with positive local
conditional probability. Equation (20) does not say how often the source or
instrument occurs.

### Theorem 10 — no dormant unchosen child

The accessible selected block contains one mode record and one history in
the corresponding target fiber. It contains no active register for the
unchosen child.

**Proof.** This follows from the coproduct type (19), not from tracing a
factor out of a product of two live children. The reversible query was
already uncomputed before commit; its temporary witness is not a dormant
child. (square)

## 9. Point-free covariance

Let (g:X\to X') be a source-groupoid arrow in the same sort summand.
Transport acts on component and occurrence addresses, complete fields,
witnesses, histories, readers, records, and source-indexed exhaust labels.

### Theorem 11 — naturality of the complete instrument

The following assignments commute with every such `g`:

1. tensor and fusion child experiments;
2. seed space, uniform seed law, and Householder purification;
3. tensor and fusion witness computations on the fine seed register;
4. the fused-witness projector and phase operation;
5. inverse query and common-state closure;
6. the residual-overlap functional (gamma) and the law (17);
7. outcome-indexed commit;
8. complete child readers and accepted futures; and
9. the joint law (20).

**Proof.** Every construction is indexed by transported physical incidence
and complete source data. The mode basis is transported with its controlled
operations, not relabeled alone. The seed superposition and reflection are
natural by Theorem 4. The witness computations are natural because the
accepted fusion kernel is equivariant in the seed assignment. The overlap
(16) transports as an inner product of transported residual states, so (17)
is natural in `gamma` and `phi`. The numerical matrices act only on the
typed two-mode carrier. The accepted child kernels are equivariant, and the
exhaust labels transform as ([X],m,[H]). Hence both paths around each
naturality square have identical typed outputs and probabilities. (square)

Serialization order and loop order are absent from the source object and
cannot change the law.

## 10. Covariant restriction

Let `J` select a covariant subfamily of occurrences and restrict a realized
source and history.

### 10.1 Positive restriction

If at least two nonempty active components of the common sort survive, then

$$
\operatorname{res}_J X\in\mathsf{Src}^{\ge2}_s.
$$

### Theorem 12 — positive restriction naturality

On this domain, restriction commutes with both child functors, witness
queries, the commit, complete readers, and presentation transport. Removed
seed addresses are marginalized by normalization of their fixed product
state.

**Proof.** The retained active sort does not change. Tensor restriction acts
componentwise. Simultaneous fusion restriction keeps exactly the retained
incidence and marginalizes deleted random addresses. Product seed factors on
deleted addresses have total weight one. Equivariance supplies the remaining
squares. (square)

### 10.2 Zero- and one-active restriction

If fewer than two active components survive, the restricted object is not a
new positive source. For a realized branch define

$$
\mathsf{Res}_J(X,m,H)
=
\left(
m_R,
\operatorname{res}_J\mathsf Y_{m,s,X},
\operatorname{res}_J H
\right).
\tag{22}
$$

The tensor branch may land in the formal monoidal unit or a formal one-factor
tensor. The fusion branch lands in the corresponding atomic boundary type.

### Theorem 13 — branchwise degenerate restriction

Equation (22) is a total typed restriction of already realized histories. It
does not identify the tensor and fusion targets, trigger a new mode
opportunity, or assign a new (C_\phi) law.

**Proof.** The branch record chooses the dependent target before restriction.
Ordinary target/history restriction is then defined within that branch. The
formal tensor unit and an empty atomic boundary, and likewise a formal
one-factor tensor and its atomic factor, are different types unless an
additional alignment is supplied. None is supplied here. The inherited
branch weight is a pushforward of the parent law, not a new intrinsic law on
the restricted target. (square)

Erasing the stable mode record is a separate physical operation. It is not a
quotient hidden inside restriction.

## 11. External composition only

For disjoint admitted classical sources (X_1,X_2), define

$$
\mathcal I_{X_1}\boxtimes\mathcal I_{X_2}.
\tag{23}
$$

It has two source objects, two active marks, two mode carriers, two records,
and two exhaust systems.

### Theorem 14 — external tensor naturality

Equation (23) is a typed natural external product. Symmetric braiding gives
order independence of the two formal factors.

**Proof.** Each factor is already total on its own homogeneous source fiber.
Their tensor product acts independently on disjoint carriers; bifunctoriality
and symmetric braiding supply the natural comparison. No internal union of
active marks is formed. (square)

This theorem does not assert that two active marks inside one larger source
commute. No same-source multi-mark object is defined. It also does not
replace one simultaneous n-ary fusion by a staged binary word; the latter
traverses additional physical boundaries and remains a different history.

## 12. Triggered process plurality and noninheritance

### Theorem 15 — local process plurality

For every admitted source, the tensor and simultaneous-fusion commits are
distinct triggered whole-process fibers. At neutral tensor input both have
positive probability, (21).

**Proof.** Proposition 2 gives a complete operational distinction while the
route is open, and the commit writes different stable mode records and lands
in different dependent target types. Equation (21) gives positive local
weights. (square)

### Theorem 16 — noninheritance

The family (X\mapsto\widehat\Gamma_{\phi,X}) determines neither a
probability law over source objects nor an activity, root, size, chronology,
dimension, metric, curvature, gravity, or actuality law.

**Proof.** Every equation is conditional on a supplied classical `X`, active
mark, mode input, and apparatus phase. Source-indexed exhaust labels
guarantee orthogonality but carry no amplitudes among sources. Multiplying
(20) by any normalized external source propensity produces a joint extension
with the same local instrument, showing that the local law does not select
that propensity. No later geometric object occurs in any definition.
(square)

## 13. Hostile-control matrix

The following controls are part of the mathematical object.

| control | exact disposition |
|---|---|
| heterogeneous (B^0_1,B^0_2) active pair | refused by coproduct membership before fusion |
| sort-changing source arrow | absent from every source hom-set |
| empty active family as positive source | refused by cardinality predicate |
| one-active family as positive source | refused by cardinality predicate |
| formal tensor unit equals empty atomic boundary | type equality refused |
| formal one-factor tensor equals its atomic factor | type equality refused without alignment |
| degenerate restriction triggers new mode law | refused; (22) only transports a realized branch |
| degenerate restriction drops record | refused; (m_R) is a field of (22) |
| same-source two-mark commutation | unconstructed, never inferred from (23) |
| staged binary word equals simultaneous fusion | refused by distinct traversed-boundary trace |
| different sources share unindexed exhaust | killed by ([X]) in (c_{[X],m,[H]}) |
| exhaust orthogonality selects source odds | false; no coefficients on the external direct sum |
| spectator sort changes (C_\phi) | false; spectator is identity-carried and mode law is fixed |
| route-dependent residue after query | killed by (U_{Q,X}^{-1}P_\phi U_{Q,X}) closure |
| reversible query called accessible erasing fusion | killed by Theorems 2–3 and 5 |
| accessible dormant unchosen child | killed by coproduct target (19) |
| naked mode-label swap | changes typed controls and is not a gauge arrow |
| output decoder changed at fixed instrument | different instrument, not a relabeling |
| phase selected after downstream output | outside the fixed-input experiment |
| mutation of (B,R,C_\phi), neutral odds, or child kernel | changes immutable law and is refused |
| biased seed carrier `|sigma>=(3/5)|0>+(4/5)|1>` | outside the bound apparatus; refused by Section 5.1 |
| coarse bond bit or fine-to-coarse isometry | not constructed; the fine seed is retained and uncomputed |
| `[25]` repartitioned inside the instrument | forbidden; `beta`'s nine/sixteen split is read, never redefined |
| interference term written as `Re(v)` | false by Theorem 7 and Corollary 7.1 |
| seed traced at recombination | caught as a violation of closure (11) |
| activity/root odds inferred from local odds | contradicted by Theorem 16 |
| chronology/dimension/metric/gravity/actuality inferred | absent from definitions and refused by Theorem 16 |

The heterogeneous predecessor counterexample is therefore rejected at the
first source predicate rather than hidden behind a zero-probability branch.

## 14. Product-valued outcome

```text
P22V3-HOMOGENEOUS-SOURCE-GROUPOID:        CONSTRUCTED

P22V3-TOTAL-TENSOR-FUSION-CHILD-PAIR:     CONSTRUCTED

P22V3-FIBERWISE-REVERSIBLE-QUERY:         CONSTRUCTED
  (bound uniform fine seed; exact closure; kickback)

P22V3-FIBERWISE-COMMIT-INSTRUMENT:        CONSTRUCTED

P22V3-EXACT-LOCAL-MODE-LAW:               CONSTRUCTED
  (coherent C_phi; B^2; neutral odds 49/625, 576/625)

P22V3-PARTIAL-VISIBILITY-LAW:             CONSTRUCTED
  (Theorem 7 with Corollaries 7.1–7.4; gamma=i control exact)

P22V3-POSITIVE-RESTRICTION-NATURALITY:    CONSTRUCTED

P22V3-DEGENERATE-BRANCHWISE-RESTRICTION:  CONSTRUCTED

P22V3-EXTERNAL-TENSOR-COMPOSITION:        CONSTRUCTED

P22V3-SAME-SOURCE-MULTIMARK-COMPOSITION:  UNCONSTRUCTED

P22V3-SIMULTANEOUS-FUSION-ALGEBRA:        UNCONSTRUCTED

P22V3-ACTIVITY-ROOT-LAW:                  UNCONSTRUCTED

P22V3-PHYSICAL-REGIONAL-REFERENT:         UNCONSTRUCTED

P22V3-CHRONOLOGY-DIMENSION-METRIC-GR:     UNCONSTRUCTED

P22V3-ACTUALIZATION:                      UNCONSTRUCTED
```

These are independent coordinates, not a ladder. The strongest honest claim
is the complete triggered local structural instrument on homogeneous source
fibers, on the bound apparatus, with the exact partial-visibility family.

## 15. Permanent boundary

Even acceptance of this construction would not explain why a source exists,
which active family is selected, how often the instrument occurs, or what
cosmological state prepares it. It supplies no coherent source superposition,
physical regional referent, localized reverse intervention at every later
generator, complete chronology, varying-size physical ensemble, dimension,
Lorentzian signature, order-plus-valuation metric, clock, radar, scale,
curvature, backreaction, Einstein dynamics, continuum limit, QFT, or
actualization.

The next scientific use, if independently accepted, is as one local input to
the separately pinned Paper 23 structural-opportunity investigation, which
binds an accepted instrument only through its own fresh hash-bound freeze.
Its local conditional probabilities cannot choose that future experiment.

## References

1. W. K. Wootters and W. H. Zurek, "A single quantum cannot be cloned,"
   *Nature* 299, 802–803 (1982).
2. S. L. Braunstein and A. K. Pati, "Quantum information cannot be completely
   hidden in correlations," *Physical Review Letters* 98, 080502 (2007).
3. R. P. Feynman and A. R. Hibbs, *Quantum Mechanics and Path Integrals*,
   McGraw–Hill (1965).
