# A homogeneous-source reversible structural instrument

## Typed coherent query, dependent commit, and the no-hiding boundary

### Abstract

We construct a point-free triggered structural instrument on a precisely
typed source domain. The source is a finite unordered family of active
complete boundary values of one common atomic sort, together with arbitrarily
typed spectators. Two child experiments are available on every admitted
source: formal tensor preservation and one simultaneous fusion at the common
sort. Heterogeneous active families are outside the domain and are refused
before a query, fusion, child, or probability is evaluated.

The instrument separates a reversible query from a physical commit. The query
coherently computes tensor and fusion witnesses, applies a phase to the fused
witness, and uncomputes every seed, witness, complement, and environment field
before recombination. The commit then writes a stable mode record and exposes
exactly one dependent child. A finite no-hiding theorem explains why these
must be different stages: irreversible fusion cannot be a reversible map on
the accessible fused target alone.

The numerical law is unchanged from the frozen local construction. Its mode
lift is

$$
R=
\begin{pmatrix}
3/5&-4/5\\
4/5&3/5
\end{pmatrix},
\qquad
B=|R|^2=
\frac1{25}
\begin{pmatrix}
9&16\\
16&9
\end{pmatrix}.
$$

A phase on the fused query witness gives

$$
C_\phi=|R\,\operatorname{diag}(1,e^{i\phi})R|^2.
$$

For a fixed admitted source, mode, and apparatus phase, the accessible joint
law is the product of this mode law and the accepted conditional child law.
This is not a probability distribution over source objects or an occurrence
law for the instrument.

Restrictions that retain at least two homogeneous active components stay in
the positive source groupoid. Restrictions leaving zero or one active
component are instead typed branchwise and retain the already written mode
record; they do not trigger a new opportunity or identify a formal tensor
target with an atomic fusion target. Composition is limited to external
tensor products of separately typed instruments. The result is a total local
instrument on homogeneous source fibers. It supplies no activity, root,
chronology, dimension, metric, gravity, or actualization law.

## 1. Binding scope

The mathematical object is bound by the frozen homogeneous-source pin with
ordinary SHA-256
`a4c1c2ecd10edad73ed64b12f699c09d7cfd169d4cd264939990589554693627`.
Its accepted atomic sorts, tensor products, simultaneous fusion maps, and
conditional child kernels are those of the terminal typed law. The earlier
local construction fixes the numerical mode, query, and commit core, while
its adjudicated heterogeneous-source totality claim is not inherited.

This paper changes only source and functor domains. It introduces no fitted
coefficient, phase, seed bias, channel weight, dimension, or geometry.

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

## 5. Fiberwise reversible query

All coherent equations in this section are indexed by one fixed classical
source (X\in\mathsf{Src}^{\ge2}_s). There is no coherent superposition or
probability law over different source objects.

### 5.1 Purified seed

For every unordered cross-active pair address `p`, introduce a seed qubit
with the fixed purification

$$
|\sigma\rangle_p
=
\frac35|0\rangle_p+\frac45|1\rangle_p.
\tag{7}
$$

The tensor query leaves these addresses outside its accessible child witness.
The fusion query reversibly computes the accepted fused witness from the
complete source and seed. Seed labels transform with occurrence addresses;
their serialization is not physical.

### 5.2 Controlled witness computation

Let the mode basis be (|T\rangle,|F\rangle). On each fixed source fiber,
define reversible computations

$$
Q_{T,X}:
|X,z,0_W,0_C\rangle
\longmapsto
|X,z,w_T(X,z),c_T(X,z)\rangle,
$$

$$
Q_{F,X}:
|X,z,0_W,0_C\rangle
\longmapsto
|X,z,w_F(X,z),c_F(X,z)\rangle.
\tag{8}
$$

Here `C` is exactly the reversible complement required by Theorems 2 and 3.
The controlled query is

$$
Q_X
=
|T\rangle\!\langle T|\otimes Q_{T,X}
+
|F\rangle\!\langle F|\otimes Q_{F,X}.
\tag{9}
$$

Since the computations are injective on the finite typed basis when all input
and complement fields are retained, they extend to unitaries on each fiber.

Let (Pi_{F,X}) be the projector onto the physically typed fused-witness
sector. Apply

$$
D_{\phi,X}=e^{i\phi\Pi_{F,X}}
$$

and then (Q_X^{-1}). The full query block is

$$
U_{Q,X}(\phi)=Q_X^{-1}D_{\phi,X}Q_X.
\tag{10}
$$

### Theorem 4 — exact query closure

After (10), the source, seed, witness, complement, and uncontrolled
environment fields equal their common pre-query states for both modes. The
only route-dependent remainder is the phase on the mode carrier.

**Proof.** Equation (10) is compute, phase on a predicate of the computed
witness, and exact inverse-compute. All computed basis data are restored.
The eigenvalue of the fused-witness projector is copied back as a relative
phase before the inverse erases the witness. (square)

This is phase kickback, not accessible fusion. Calling it physical erasing
fusion would contradict the no-hiding theorems.

## 6. Exact mode and probe law

### Theorem 5 — minimal calibrated lift

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
\tag{11}
$$

**Proof.** The entry moduli are fixed by `B`. Orthogonality forces opposite
relative signs in one column and fixes the second column once the first is
chosen. Row/column phases and simultaneous basis exchange are the remaining
gauge. (square)

Use (11), the query phase, and (11) again. The coherent mode map is

$$
R D_\phi R,
\qquad
D_\phi=\operatorname{diag}(1,e^{i\phi}).
$$

### Theorem 6 — probe probability

The complete probe law is

$$
C_\phi
=
|R D_\phi R|^2
=
\frac1{625}
\begin{pmatrix}
337-288\cos\phi&288(1+\cos\phi)\\
288(1+\cos\phi)&337-288\cos\phi
\end{pmatrix}.
\tag{12}
$$

At (phi=0),

$$
C_0
=
\frac1{625}
\begin{pmatrix}49&576\\576&49\end{pmatrix}.
$$

At (phi=\pi/2),

$$
C_{\pi/2}=B^2
=
\frac1{625}
\begin{pmatrix}337&288\\288&337\end{pmatrix}.
$$

At (phi=\pi), (C_\pi=I).

**Proof.** Direct multiplication gives diagonal amplitude
((9-16e^{i\phi})/25) and off-diagonal amplitude
(12(1+e^{i\phi})/25). Squared moduli give (12). (square)

If a stable which-route record is written between the two lifts, the cross
terms vanish and the law is (B^2). If the record and every environmental
copy are reversibly erased before recombination, (12) is restored. A partial
record with overlap `v` multiplies only the interference term by
(\operatorname{Re}v).

The unique stochastic continuation through the proposed two-state cut is

$$
K_\phi=C_\phi B^{-1}
=
\frac1{175}
\begin{pmatrix}
63+288\cos\phi&112-288\cos\phi\\
112-288\cos\phi&63+288\cos\phi
\end{pmatrix}.
\tag{13}
$$

It is positive exactly when

$$
-\frac7{32}\le \cos\phi\le\frac7{18}.
\tag{14}
$$

Thus the same local instrument exhibits coherent nondivision, stable-record
division, and erasure recovery without changing its source domain.

## 7. Fiberwise dependent commit

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
\tag{15}
$$

The exhaust labels are orthonormal and source indexed. Their purpose is to
dilate the already specified child kernel, not to define amplitudes among
sources.

### Theorem 7 — fiberwise isometry

Equation (15) is an isometry on the declared blank input subspace for every
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
\tag{16}
$$

It is not a product containing both child systems. The complement/exhaust is
inaccessible after the declared commit boundary.

### Theorem 8 — joint law, normalization, and child recovery

For mode input `j`, phase `phi`, and fixed admitted source `X`, the accessible
joint law is

$$
\widehat\Gamma_{\phi,X}(m,[H]\mid j)
=
C_\phi(m\mid j)\Gamma_m([H]\mid[X]).
\tag{17}
$$

It normalizes, and conditioning on `m` recovers the exact accepted child law.

**Proof.** Summing first over histories gives `1` for each selected child;
summing over modes gives the column normalization of (C_\phi). Division by
the positive mode marginal cancels that factor and leaves (Gamma_m).
(square)

For tensor input and neutral phase,

$$
\Pr(T)=\frac{49}{625},
\qquad
\Pr(F)=\frac{576}{625}.
\tag{18}
$$

Both triggered process components therefore occur with positive local
conditional probability. Equation (17) does not say how often the source or
instrument occurs.

### Theorem 9 — no dormant unchosen child

The accessible selected block contains one mode record and one history in
the corresponding target fiber. It contains no active register for the
unchosen child.

**Proof.** This follows from the coproduct type (16), not from tracing a
factor out of a product of two live children. The reversible query was already
uncomputed before commit; its temporary witness is not a dormant child.
(square)

## 8. Point-free covariance

Let (g:X\to X') be a source-groupoid arrow in the same sort summand.
Transport acts on component and occurrence addresses, complete fields,
witnesses, histories, readers, records, and source-indexed exhaust labels.

### Theorem 10 — naturality of the complete instrument

The following assignments commute with every such `g`:

1. tensor and fusion child experiments;
2. seed purification;
3. tensor and fusion witness computation;
4. the fused-witness projector and phase operation;
5. inverse query and common-state closure;
6. outcome-indexed commit;
7. complete child readers and accepted futures; and
8. the joint law (17).

**Proof.** Every construction is indexed by transported physical incidence
and complete source data. The mode basis is transported with its controlled
operations, not relabeled alone. The numerical matrices act only on this
typed two-mode carrier. The accepted child kernels are equivariant, and the
exhaust labels transform as ([X],m,[H]). Hence both paths around each
naturality square have identical typed outputs and probabilities. (square)

Serialization order and loop order are absent from the source object and
cannot change the law.

## 9. Covariant restriction

Let `J` select a covariant subfamily of occurrences and restrict a realized
source and history.

### 9.1 Positive restriction

If at least two nonempty active components of the common sort survive, then

$$
\operatorname{res}_J X\in\mathsf{Src}^{\ge2}_s.
$$

### Theorem 11 — positive restriction naturality

On this domain, restriction commutes with both child functors, witness
queries, the commit, complete readers, and presentation transport. Removed
seed addresses are marginalized by normalization of their fixed product
state.

**Proof.** The retained active sort does not change. Tensor restriction acts
componentwise. Simultaneous fusion restriction keeps exactly the retained
incidence and marginalizes deleted random addresses. Product seed factors on
deleted addresses have total weight one. Equivariance supplies the remaining
squares. (square)

### 9.2 Zero- and one-active restriction

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
\tag{19}
$$

The tensor branch may land in the formal monoidal unit or a formal one-factor
tensor. The fusion branch lands in the corresponding atomic boundary type.

### Theorem 12 — branchwise degenerate restriction

Equation (19) is a total typed restriction of already realized histories. It
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

## 10. External composition only

For disjoint admitted classical sources (X_1,X_2), define

$$
\mathcal I_{X_1}\boxtimes\mathcal I_{X_2}.
\tag{20}
$$

It has two source objects, two active marks, two mode carriers, two records,
and two exhaust systems.

### Theorem 13 — external tensor naturality

Equation (20) is a typed natural external product. Symmetric braiding gives
order independence of the two formal factors.

**Proof.** Each factor is already total on its own homogeneous source fiber.
Their tensor product acts independently on disjoint carriers; bifunctoriality
and symmetric braiding supply the natural comparison. No internal union of
active marks is formed. (square)

This theorem does not assert that two active marks inside one larger source
commute. No same-source multi-mark object is defined. It also does not replace
one simultaneous n-ary fusion by a staged binary word; the latter traverses
additional physical boundaries and remains a different history.

## 11. Triggered process plurality and noninheritance

### Theorem 14 — local process plurality

For every admitted source, the tensor and simultaneous-fusion commits are
distinct triggered whole-process fibers. At neutral tensor input both have
positive probability, (18).

**Proof.** Proposition 2 gives a complete operational distinction while the
route is open, and the commit writes different stable mode records and lands
in different dependent target types. Equation (18) gives positive local
weights. (square)

### Theorem 15 — noninheritance

The family (X\mapsto\widehat\Gamma_{\phi,X}) determines neither a
probability law over source objects nor an activity, root, size, chronology,
dimension, metric, curvature, gravity, or actuality law.

**Proof.** Every equation is conditional on a supplied classical `X`, active
mark, mode input, and apparatus phase. Source-indexed exhaust labels guarantee
orthogonality but carry no amplitudes among sources. Multiplying (17) by any
normalized external source propensity produces a joint extension with the
same local instrument, showing that the local law does not select that
propensity. No later geometric object occurs in any definition. (square)

## 12. Hostile-control matrix

The following controls are part of the mathematical object.

| control | exact disposition |
|---|---|
| heterogeneous (B^0_1,B^0_2) active pair | refused by coproduct membership before fusion |
| sort-changing source arrow | absent from every source hom-set |
| empty active family as positive source | refused by cardinality predicate |
| one-active family as positive source | refused by cardinality predicate |
| formal tensor unit equals empty atomic boundary | type equality refused |
| formal one-factor tensor equals its atomic factor | type equality refused without alignment |
| degenerate restriction triggers new mode law | refused; (19) only transports a realized branch |
| degenerate restriction drops record | refused; (m_R) is a field of (19) |
| same-source two-mark commutation | unconstructed, never inferred from (20) |
| staged binary word equals simultaneous fusion | refused by distinct traversed-boundary trace |
| different sources share unindexed exhaust | killed by ([X]) in (c_{[X],m,[H]}) |
| exhaust orthogonality selects source odds | false; no coefficients on the external direct sum |
| spectator sort changes (C_\phi) | false; spectator is identity-carried and mode law is fixed |
| route-dependent residue after query | killed by (Q_X^{-1}D_{\phi,X}Q_X) closure |
| reversible query called accessible erasing fusion | killed by Theorems 2--4 |
| accessible dormant unchosen child | killed by coproduct target (16) |
| naked mode-label swap | changes typed controls and is not a gauge arrow |
| output decoder changed at fixed instrument | different instrument, not a relabeling |
| phase selected after downstream output | outside the fixed-input experiment |
| mutation of (B,R,C_\phi), neutral odds, or child kernel | changes immutable law and is refused |
| activity/root odds inferred from local odds | contradicted by Theorem 15 |
| chronology/dimension/metric/gravity/actuality inferred | absent from definitions and refused by Theorem 15 |

The heterogeneous predecessor counterexample is therefore rejected at the
first source predicate rather than hidden behind a zero-probability branch.

## 13. Product-valued outcome

The construction yields

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
  CONSTRUCTED

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

These are independent coordinates, not a ladder. The strongest honest claim
is a point-free triggered local structural instrument on homogeneous source
fibers.

## 14. Permanent boundary

Even acceptance of this construction would not explain why a source exists,
which active family is selected, how often the instrument occurs, or what
cosmological state prepares it. It supplies no coherent source superposition,
physical regional referent, localized reverse intervention at every later
generator, complete chronology, varying-size physical ensemble, dimension,
Lorentzian signature, order-plus-valuation metric, clock, radar, scale,
curvature, backreaction, Einstein dynamics, continuum limit, QFT, or
actualization.

The next scientific use, if independently accepted, is as one local input to
a separately pinned structural-opportunity or regional-response experiment.
Its local conditional probabilities cannot choose that future experiment.

## References

1. W. K. Wootters and W. H. Zurek, “A single quantum cannot be cloned,”
   *Nature* 299, 802–803 (1982).
2. S. L. Braunstein and A. K. Pati, “Quantum information cannot be completely
   hidden in correlations,” *Physical Review Letters* 98, 080502 (2007).
3. R. P. Feynman and A. R. Hibbs, *Quantum Mechanics and Path Integrals*,
   McGraw–Hill (1965).
