# Integrated hybrid semantics for relativistic quantum procedures

## Atomic restart, continuous records, and certified concurrency

Date: 2026-08-22

Status: **GREEN-UNREVIEWED MATHEMATICS**

This construction is bound to the sole corrected Paper 03 v3.1 pin and its
terminal pre-construction adjudication. It changes no v2 probability,
instrument, state update, source, localization premise, physical parameter,
or comparator spacetime.

## Abstract

We construct a boundary-tagged category that gives one compositional
Heisenberg representation to retained classical records and quantum
operations on finite relativistic laboratory protocols. Finite and declared
atomic records are represented by central direct sums and admit exact normal
point states. Standard-Borel continuous records are represented by hybrid
von Neumann algebras relative to one proved boundary measure class. Exact
outcome samples remain in the stochastic kernel semantics, while dominated
ensemble laws map to normal hybrid states through an explicit predual
integration map `Ens`.

The construction proves representative independence and normality of `Ens`,
null-ideal preservation for deterministic and stochastic record maps,
complete finite instruments, conditional continuous instruments with the
normal extension property and exact target landing, decomposable continuous
feedback, a contravariant Heisenberg functor, and an integrated
`Ev`/`Ens`/`Heis` identity for every admitted finite path. The proof begins at
ensemble level and never evaluates an $L^\infty$ equivalence class at a
generic nonatomic point.

The causal-frontier path category, localized system--probe instruments,
no-signalling/steering distinction, Bell compatibility, positive histories,
presentation covariance, and complete operational quotient retain their v2
scope. Schedule equality is proved only through full two-layer exchange
certificates in every reachable adaptive context.

The construction deliberately returns the mixed point-restart result

```text
P03V31-FINITE-ATOMIC-POINT-RESTART-CONSTRUCTED
P03V31-NONATOMIC-POINT-RESTART-UNCONSTRUCTED
```

and does not identify a record, conditional state, frontier, or hybrid algebra
with actuality or ontology. The Lorentzian comparator remains declared.
Internal time, spacetime emergence, matter--geometry dynamics, and gravity
remain unconstructed.

Provisional ceiling:

```text
P03V31-RELATIVISTIC-QUANTUM-OPERATIONAL-ADEQUACY-WITH-GLOBAL-ONTOLOGY-DEBT
```

No coordinate is terminal before independent hostile review.

## 0. Frozen authority and immutability

This construction binds:

| Artifact | SHA-256 | Role |
|---|---|---|
| `v17/note-paper03v31-integrated-hybrid-semantics-pin.md` | `b7ec12ad25c3ac6327cb242ad39ba03e1af541e544f11d32cb86dbce908b5fca` | immutable construction contract |
| `v17/note-paper03v31-pin-audit-adjudication.md` | `613c006a5933db29cd29e3d1c6e3594fa044c4f1fb150d6f904882768588c96f` | sole construction authority |
| `v17/note-paper03v31-pin-audit-category.md` | `86eb3e42782e36685e5017b74fd790215b5296287a96bbb5d72d420f80d8a761` | binding category burdens |
| `v17/note-paper03v31-pin-audit-quantum.md` | `a25cf562d4f25b8fccebd3546e19ecccfde8fe3aac975ae047051c2c2319cb78` | binding instrument burdens |
| `v17/paper-03v2-causal-frontier-relativistic-adequacy.md` | `93eaa95fba10831618512ab95447d3527ff5d8877ab5119237f73bb8c30e0181` | unchanged physical mathematics |
| `v17/note-paper03v2-hostile-review-adjudication.md` | `74303ddd93b4aac35d3368760da4a0ad3d442570cb16320467076aa5f93ea358` | unchanged v2 scope |
| `v17/paper-00-reality-first-programme.md` | `a9f8456763447eaa25a6a840e8f221f51d961ecd9c3ced649ae35a8616457cbe` | reality-first wall |

The symbols introduced below organize the immutable v2 laws. They are not new
physical variables. A packet failing a conditional theorem is refused rather
than repaired by changing its probabilities.

## 1. Scientific scope and nonclaims

### Definition 1.1 — comparator packet

A registered comparator packet is

$$
\Xi=(M,\mathcal A,\mathfrak S,\mathsf L,
     \mathsf{Probe},\mathsf{Reader},\mathsf{Kernel},\mathsf{Mem}).
$$

Here:

- $M$ is an oriented, time-oriented, globally hyperbolic Lorentzian
  spacetime;
- $\mathcal A$ is a locally covariant algebra theory on the registered region
  net;
- $\mathfrak S$ is the admitted measurable class of quantum predictive
  states;
- $\mathsf L$ is a finite laboratory slot structure;
- probes, readers, kernels, records, sources, and calibrations are exact packet
  data; and
- $\mathsf{Mem}$ lists every quantum or classical coordinate that a licensed
  future may read.

The packet is a declared comparator. Nothing here selects it as the law or
state of the universe.

### Definition 1.2 — locally covariant variance

Let

$$
\mathcal A:\mathbf{Loc}\longrightarrow\mathbf{Alg}
$$

be covariant. For a proper `Loc` embedding $\psi:M\to N$, observables move by
$\alpha_\psi=\mathcal A(\psi)$ and states restrict by

$$
\psi^*\omega=\omega\circ\alpha_\psi.
$$

There is no canonical forward state extension. A full packet isomorphism is a
stronger object and is defined later.

### Nonclaims 1.3

This construction does not derive:

- a spacetime, causal order, dimension, signature, orientation, or metric;
- a QFT net, interacting four-dimensional model, preferred vacuum, or
  cosmological state;
- a collapse surface, actual outcome, or actual trajectory;
- a local hidden-variable or Bell-local completion;
- a unique Barandes configuration space or indivisible law;
- a microscopic event web, lattice, global clock, or foliation;
- internal time, matter--geometry dynamics, Einstein equations, or gravity.

## 2. Finite causal-frontier procedure category

### Definition 2.1 — slots and frontiers

Let

$$
\mathsf L=(V,\prec,\operatorname{supp},
           \operatorname{port},\operatorname{guard})
$$

where $V$ is finite and $\prec$ is a strict partial order. Supports, ports,
sources, and guards are typed. Guards read only records already produced by
predecessors. If one support lies wholly in the causal past of another, the
slot order respects that fact. An incomparable pair has no hidden port,
record, source, or memory dependence.

A frontier $D\subseteq V$ is a lower set. A slot $v\notin D$ is enabled only
when every predecessor lies in $D$ and its complete input interface is
present.

### Definition 2.2 — physical boundary schema

The v2 boundary schema is

$$
B_{\Xi,D}=(\Xi,D,\mathsf P_D,\mathsf R_D,
            \mathsf X_D,\mathsf{Mem}_D).
$$

It records open quantum/probe ports, retained record coordinates, the exact
standard-Borel predictive/sample space, and every future-readable memory
port. A boundary value is not an object type.

### Definition 2.3 — primitive arrows and path category

For each enabled slot and admitted mechanism,

$$
g_{v,m,D}:B_{\Xi,D}\longrightarrow B_{\Xi,D\cup\{v\}}.
$$

Preparation, localized coupling/instrument, trusted randomization,
controlled operation, record write/read, coarse-graining, discard, and
explicit skip are separate typed generators. An explicit skip consumes the
slot and is not an identity.

Let $G_\Xi$ be the resulting directed multigraph and define

$$
\mathcal P_\Xi=\operatorname{Path}(G_\Xi).
$$

### Theorem 2.4 — category and no illicit timelike reversal

$\mathcal P_\Xi$ is a small category. Matching paths compose by
concatenation, empty paths are identities, and composition is associative.
If $v_-\prec v_+$, then the later-first frontier is not a lower set and the
corresponding reverse primitive is absent by type.

**Proof.** The path category theorem gives the category laws. Lower-set
closure excludes completion of $v_+$ before $v_-$. No second admissibility
predicate is evaluated during composition. $\square$

### Proposition 2.5 — no serialization clock

Completing two enabled incomparable slots in either order reaches the same
set frontier. No insertion rank or topological-sort index occurs in the
boundary. This removes a program-order artifact; it does not derive time.

## 3. Exact boundary regimes

Every boundary is assigned exactly one regime before semantic evaluation.

### Definition 3.1 — finite regime

For finite retained-record space $R_D$ and represented von Neumann quantum
algebra $\mathcal A_D$,

$$
\mathcal O_D
=\ell^\infty(R_D)\,\overline\otimes\mathcal A_D
\cong\bigoplus_{r\in R_D}\mathcal A_D.
$$

Every singleton is a central atom.

### Definition 3.2 — countable atomic regime

For countable $R_D$, use $\ell^\infty(R_D)$ with predual $\ell^1(R_D)$.
Each point used for restart must be a declared atom. The positive universal
construction in this paper is finite; countable scope is conditional on
normality and summability.

### Definition 3.3 — integrated standard-Borel regime

An integrated boundary supplies:

1. a standard-Borel record space $R_D$;
2. a represented sigma-finite von Neumann algebra $\mathcal A_D$ with
   separable predual;
3. one sigma-finite measure class $[\nu_D]$;
4. an exact standard-Borel predictive/sample space $X_D$;
5. measurable maps

   $$
   \mathsf r_D:X_D\to R_D,
   \qquad
   \mathsf e_D:X_D\to\mathfrak S_n(\mathcal A_D),
   $$

   where $\mathsf e_D(x)$ evaluates the complete exposed predictive quantum
   value as a normal state, and is Borel/strongly measurable in the
   predual-norm realization of the normal state space;
6. a class $\mathfrak E_D\subseteq\operatorname{Prob}(X_D)$ of admitted
   ensemble laws whose record marginals are dominated by $\nu_D$;
7. a strongly measurable conditional predual barycenter for every admitted
   ensemble; and
8. every future-relevant memory coordinate inside $\mathcal A_D$, $R_D$, or
   an explicitly evaluated typed factor.

Define

$$
\mathcal O_D
=\mathcal A_D\,\overline\otimes
 L^\infty(R_D,\nu_D).
$$

Because $\mathcal A_D$ has separable predual, we use the standard constant
direct-integral realization: an element of $\mathcal O_D$ is an essentially
bounded, weak-star measurable $\mathcal A_D$-valued field, modulo
$\nu_D$-almost-everywhere equality. Its normal predual is represented by
Bochner-integrable $(\mathcal A_D)_*$-valued fields. No canonical value of an
$L^\infty$ class at one nonatomic point is introduced by this realization.

The measure class is part of the type, not a physical state or probability
law.

### Definition 3.4 — tagged object

The hybrid object is

$$
\mathbf O_D=
(B_{\Xi,D},\mathcal O_D,\mathsf{Reg}_D,[\nu_D],
 X_D,\mathfrak E_D,\mathsf r_D,\mathsf e_D).
$$

The class field is omitted in the finite regime. Equal underlying algebras do
not identify different frontiers, port schemas, record schemas, or memory
interfaces.

### Proposition 3.5 — exact point-state split

For a finite or declared atomic $r$ and normal state $\rho$,

$$
\omega_{\rho,r}((A_s)_s)=\rho(A_r)
$$

is a normal hybrid state. If $\nu_D(\{r\})=0$, evaluation at $r$ is neither
well defined on $L^\infty(R_D,\nu_D)$ equivalence classes nor normal.

**Proof.** Atomic evaluation is the normal central-summand functional. In the
nonatomic case two representatives can differ at $r$ while defining the same
$L^\infty$ element; the alleged evaluation is not representative independent.
$\square$

Thus generic nonatomic point restart is refused without deleting the exact
sample from $X_D$.

## 4. Point-sample semantics

### Definition 4.1 — exact kernel functor

Each primitive $g:D\to E$ retains its v2 normalized Markov kernel

$$
K_g:X_D\longrightarrow\operatorname{Prob}(X_E).
$$

Define

$$
\operatorname{Ev}_\Xi:\mathcal P_\Xi\to\mathbf{Kern}
$$

by chronological kernel composition. Posterior versions in an integrated
packet are frozen Borel versions, understood physically only up to the
packet's declared almost-everywhere relation.

### Proposition 4.2 — functoriality

`Ev` sends empty paths to identity kernels and concatenation to kernel
composition.

**Proof.** This is the identity and associativity theorem for Markov kernels
on standard-Borel spaces. $\square$

No kernel is inferred by dividing through a zero-probability singleton.

## 5. The ensemble bridge

### Definition 5.1 — `Ens`

For $\Lambda_D\in\mathfrak E_D$, define

$$
\operatorname{Ens}_D(\Lambda_D)(F)
=\int_{X_D}
 \mathsf e_D(x)\bigl(F^\sharp(\mathsf r_D(x))\bigr)\,
 \Lambda_D(dx),
\qquad F\in\mathcal O_D.
$$

Here $F^\sharp$ is any weak-star measurable representative of the
$L^\infty$ class $F$. The displayed expression is a state-evaluation
integral, not the integral of an operator-valued placeholder. The theorem
below proves that it is independent of the chosen representative; the
notation does not assign a canonical $F(r)$ at a nonatomic point. Predual
strong measurability of $\mathsf e_D$ and weak-star measurability of
$F^\sharp$, together with separability of the predual, make the scalar
pairing measurable.

### Theorem 5.2 — normality and representative independence

`Ens` is a well-defined positive normalized normal functional on
$\mathcal O_D$.

**Proof.** Let

$$
\eta_D=(\mathsf r_D)_*\Lambda_D,
\qquad
h_D=\frac{d\eta_D}{d\nu_D}.
$$

Disintegrate $\Lambda_D$ over $r$ and write the supplied strongly measurable
conditional barycenter as $\bar\rho_r\in(\mathcal A_D)_*$. Then

$$
g_D(r)=h_D(r)\bar\rho_r
\in L^1(R_D,\nu_D;(\mathcal A_D)_*)
$$

because $g_D$ is positive and

$$
\int\lVert g_D(r)\rVert\,\nu_D(dr)=1.
$$

The constant direct-integral/predual identification in Definition 3.3 makes
this field a normal predual functional

$$
F\longmapsto
\int\langle g_D(r),F(r)\rangle\,\nu_D(dr).
$$

Disintegration gives Definition 5.1. If $F_1=F_2$ as $L^\infty$ classes,
they agree $\nu_D$-almost everywhere and hence $\eta_D$-almost everywhere;
the integral is representative independent. Positivity and normalization are
immediate from the state fields. $\square$

### Corollary 5.3 — atomic compatibility

In the finite/atomic regime,

$$
\operatorname{Ens}_D(\delta_{(\rho,r)})
=\omega_{\rho,r}.
$$

In the nonatomic regime such a Dirac law generally lies outside
$\mathfrak E_D$.

### Proposition 5.4 — no hidden future distinction

If two admitted laws have the same `Ens` state but a licensed continuation
distinguishes them, the boundary schema is incomplete.

**Proof.** Any Heisenberg arrow out of one hybrid state produces one value on
every reader. Different future values from equal input states contradict the
one-step duality theorem constructed below. The distinguishing memory must be
exposed or the continuation refused. $\square$

This is a future-sufficiency test, not an ontic identification of ensemble
decompositions.

## 6. Common domination and null ideals

### Definition 6.1 — common boundary class

One integrated boundary is admitted only when one $[\nu_D]$ dominates the
record marginal of every admitted incoming ensemble. For a finite or
countable family $\{\eta_n\}$, a positive mixture such as

$$
\nu_D=\sum_{n\ge1}2^{-n}\eta_n
$$

after normalization is a valid construction tool. It is not the actual law.

No sigma-finite measure dominates all $\{\delta_x:x\in[0,1]\}$. Such an
uncountable mutually singular family is refused, split into different
boundary schemas, or coarse-grained before admission.

### Lemma 6.2 — deterministic pullback

A measurable $f:R_D\to R_E$ induces

$$
f^*([u])=[u\circ f]
$$

from $L^\infty(R_E,\nu_E)$ to $L^\infty(R_D,\nu_D)$ if and only if

$$
f_*\nu_D\ll\nu_E.
$$

**Proof.** A target null set must have source-null preimage for representative
independence. This condition is exactly the displayed absolute continuity.
It is also sufficient. $\square$

The condition composes. A constant map between Lebesgue classes and a graph
append into an unrelated product class fail it.

### Lemma 6.3 — stochastic null-ideal preservation

A classical Markov kernel $Q:R_D\to\operatorname{Prob}(R_E)$ induces the
normal Markov operator

$$
(T_Qu)(r)=\int u(s)Q(r,ds)
$$

on the declared $L^\infty$ classes only if

$$
\nu_E(N)=0
\Longrightarrow
Q(r,N)=0
\quad\text{for }\nu_D\text{-almost every }r.
$$

This condition is sufficient and is stable under kernel composition.

**Proof.** The condition sends every representative of the zero target class
to the zero source class. Tonelli's theorem proves composition stability.
$\square$

For a quantum instrument the operator form is

$$
\Phi_g(1\otimes\chi_N)=0
\quad\text{in }\mathcal O_D
$$

for every $\nu_E$-null $N$. Target landing and normality must prove this; it
is not inferred from deterministic maps.

### Proposition 6.4 — ensemble closure

Every admitted primitive must prove

$$
\Lambda_D\in\mathfrak E_D
\Longrightarrow
\Lambda_DK_g\in\mathfrak E_E.
$$

Finite-path closure follows by induction. A primitive failing this condition
is outside the integrated theorem even if it works for one calibration state.

## 7. The hybrid operation category

### Definition 7.1 — arrows

Let $\mathbf{Hyb}_\Xi$ have the tagged objects $\mathbf O_D$. A morphism
written

$$
(D,E,\Phi)\in
\operatorname{Hom}_{\mathbf{Hyb}_\Xi}(\mathbf O_E,\mathbf O_D)
$$

has

$$
\Phi:\mathcal O_E\to\mathcal O_D
$$

normal unital CP in a represented $W^*$ packet. Finite $C^*$ packets may be
included as separately tagged components. Every arrow preserves the admitted
state and ensemble interfaces, target null ideal, and exposed memory schema.

### Theorem 7.2 — category

Composition and identity are

$$
(D,E,\Phi)\circ(E,F,\Psi)
=(D,F,\Phi\circ\Psi),
$$

$$
\operatorname{id}_{\mathbf O_D}
=(D,D,\operatorname{id}_{\mathcal O_D}).
$$

They make $\mathbf{Hyb}_\Xi$ a category.

**Proof.** Normal UCP maps are closed under composition. State/ensemble class
closure, null-ideal preservation, and exact memory interfaces compose by
their defining implications. Function composition is associative and the
identity maps are two-sided identities. Mismatched tags are not composable.
$\square$

An explicit skip may have the identity underlying algebra map while remaining
a nonidentity arrow because its boundary tags differ.

## 8. Complete instruments

### Theorem 8.1 — finite complete instrument

Let

$$
\mathcal J_s:\mathcal A_E\to\mathcal A_D
$$

be normal CP branch maps with

$$
\sum_s\mathcal J_s(1)=1.
$$

Define

$$
\widehat{\mathcal J}:
\bigoplus_s\mathcal A_E\longrightarrow\mathcal A_D,
\qquad
\widehat{\mathcal J}((A_s)_s)
=\sum_s\mathcal J_s(A_s).
$$

Then $\widehat{\mathcal J}$ is normal UCP.

**Proof.** Each matrix amplification is a sum of positive branch
amplifications, so the map is CP. Normality follows termwise for the finite
sum. Instrument normalization is exactly unitality. $\square$

A single branch is obtained by central-summand insertion and is generally
nonunital. The nonselective channel is obtained by diagonal restriction.
Neither is substituted for the complete record-bearing arrow.

### Proposition 8.2 — old-record retention

If $r$ is already retained and $s$ is newly measured, the complete arrow is

$$
(A_{r,s})_{r,s}
\longmapsto
\left(\sum_s\mathcal J_{r,s}(A_{r,s})\right)_r.
$$

It preserves the old fiber and appends the new result. Dropping $r$ is a
different discard mechanism.

### Exact control 8.3 — binary result followed by `I/X`

Let the future apply $I$ after result zero and $X$ after result one. The
Heisenberg controlled map sends

$$
A\longmapsto(A,XAX).
$$

Composition with the complete instrument gives

$$
\mathcal J_0(A)+\mathcal J_1(XAX),
$$

which is the exact v2 branchwise adaptive law. The nonselective sum alone
cannot produce this expression because it has erased the guard record.

### Definition 8.4 — admitted continuous instrument

For standard-Borel outcome space $(R,\Sigma)$, a continuous instrument is
admitted only when it supplies all of:

1. a countably additive normal CP instrument measure;
2. one state-independent normal UCP complete extension on the exact tagged
   source and target hybrid algebras;
3. the normal extension property or an explicitly stronger theorem;
4. landing in the declared target algebra rather than only an ambient
   $\mathcal B(\mathcal H)$;
5. a jointly measurable state/record posterior kernel for `Ev`;
6. deterministic and stochastic null-ideal preservation;
7. quantum-state and ensemble-class closure; and
8. the exact ensemble compatibility identity

   $$
   \operatorname{Ens}_E(\Lambda_DK_{\mathcal J})
   =\operatorname{Ens}_D(\Lambda_D)\circ\widehat{\mathcal J}
   $$

   for every admitted input ensemble, where both $K_{\mathcal J}$ and
   $\widehat{\mathcal J}$ are constructed from the same immutable v2
   instrument, outcome law, and posterior data.

Item 8 is a proof obligation on those common data, not permission to declare
two independently chosen semantic objects equal. Failure of the identity for
one admitted ensemble refuses the instrument from the v3.1 integrated
category.

Approximate NEP gives an approximate comparator theorem only. An instrument
without the exact data may remain terminal or be physically coarse-grained;
it is not promoted to the retained continuous theorem.

### Theorem 8.5 — continuous complete arrow

Every admitted continuous instrument defines one morphism of
$\mathbf{Hyb}_\Xi$ and one exact `Ev` kernel satisfying the one-step
integrated duality theorem of Section 11.

**Proof.** Items 2--4 give a single state-independent normal UCP
target-landing map. Items 5--7 type the kernel and ensure both sides of the
integrated identity are defined on the same admitted interfaces. Item 8 is
the required evaluated compatibility equation, with its two sides derived
from the same frozen instrument rather than fitted independently. Thus the
map and kernel form one primitive dual pair in the sense of Definition 11.1.
$\square$

This theorem is conditional admission, not a claim that every CP instrument
has NEP.

### Exact continuous existence control 8.6

Let $\mathcal A=M_2(\mathbb C)$, $R=[0,1]$ with Lebesgue class, and let $U$ be
a fixed unitary. Define

$$
\mathcal J(\Delta)(A)
=\lambda(\Delta)U^*AU.
$$

Its complete extension is

$$
\widehat{\mathcal J}(F)
=\int_0^1 U^*F(r)U\,dr.
$$

The map is normal UCP, sends target-null fields to zero, and lands in $M_2$.
In `Ev`, sample $r$ is uniform and the post-state is
$\rho\circ\operatorname{Ad}_{U^*}$, where here
$\operatorname{Ad}_{U^*}(A)=U^*AU$. For every input state and hybrid reader,
the two semantic evaluations agree by the displayed integral. Thus the
continuous theorem is nonvacuous, while no singleton is a normal restart
state.

## 9. Primitive constructor semantics

Every physical generator carries a pair

$$
g\longmapsto(K_g,\Phi_g)
$$

with exact tagged source and target.

| Primitive | `Ev` requirement | `Heis` requirement |
|---|---|---|
| identity | identity kernel | tagged identity |
| explicit skip | consumes slot; carries data | typed arrow; underlying map may be identity |
| preparation | exposed source and state | normalized CP source map |
| deterministic quantum channel | state update | normal UCP map |
| finite instrument | complete outcome/posterior kernel | direct-sum complete arrow |
| continuous instrument | jointly measurable posterior kernel | admitted target-landing normal extension |
| record append/write | exact new coordinate | nonsingular pullback on exact target class |
| record read/guard | depends only on present record | block/decomposable map |
| trusted randomization | randomizer retained and independent as declared | complete classical--quantum channel |
| coarse-graining | pushed record law | nonsingular pullback from coarse observables |
| discard | marginalizes coordinate | inclusion of record-independent observables |
| localized coupling | exact system--probe kernel | frozen complete induced instrument |
| ancillary probe | complete joint source | exact source/tensor interface |

A false guard is an explicit skip. A future result cannot guard a past slot.
A discarded or coarse-grained value cannot be read later unless it remains in
a separately exposed memory port.

### Proposition 9.1 — constructor completeness

If every primitive satisfies its one-step semantic identity and state/class
closure, every path built from the table is typed in both semantic layers.

**Proof.** The path is finite. Induct on its generators, using category and
kernel composition closure. $\square$

## 10. The contravariant Heisenberg functor

### Definition 10.1

For a physical path $p:D\to E$, let

$$
\operatorname{Heis}_\Xi(p):\mathbf O_E\to\mathbf O_D
$$

be reverse chronological composition of its primitive hybrid maps.

### Theorem 10.2 — functoriality

$$
\operatorname{Heis}_\Xi(\operatorname{id}_D)
=\operatorname{id}_{\mathbf O_D},
$$

and for $p:D\to E$, $q:E\to F$,

$$
\operatorname{Heis}_\Xi(q\circ p)
=\operatorname{Heis}_\Xi(p)
 \circ\operatorname{Heis}_\Xi(q).
$$

**Proof.** The empty physical path produces the tagged identity. Reverse
composition of the concatenated primitive list is the displayed composite.
Associativity follows from Theorem 7.2. The constructor table includes
records, controls, memory, discard, and coarse-graining, so the proof does not
silently omit classical outputs. $\square$

## 11. Integrated semantic compatibility

### Definition 11.1 — primitive dual pair

A primitive pair $(K_g,\Phi_g)$ is compatible when, for every admitted input
ensemble $\Lambda_D$,

$$
\operatorname{Ens}_E(\Lambda_DK_g)
=\operatorname{Ens}_D(\Lambda_D)\circ\Phi_g
$$

as normal states on the complete target hybrid algebra.

This equality quantifies over every hybrid reader, not one outcome or
tomographically incomplete family.

### Theorem 11.2 — one-step integrated duality

Every admitted primitive in Section 9 is a compatible pair.

**Proof.**

- Identity and deterministic quantum channels are ordinary state/map
  duality.
- Preparations and ancillary probes are source-state/tensor evaluation
  duality on their exact tagged interfaces.
- Finite instruments expand the left side by outcomes and the right side by
  the direct-sum formula of Theorem 8.1; the sums coincide termwise.
- An admitted continuous instrument includes the state-independent complete
  extension and joint posterior kernel whose defining instrument equation is
  the evaluated integral equality.
- Nonsingular record maps use change of variables on equivalence classes.
- Guards are blockwise or decomposable normal maps; Fubini--Tonelli gives the
  same integrated conditional action.
- Trusted randomization is the retained classical mixture channel with its
  declared independent source; its two evaluations coincide termwise or by
  the defining kernel integral.
- Coarse-graining and discard are marginal/pullback duals.
- Localized couplings inherit the exact system--probe instrument equation.

In every integrated case the proof is an equality of normal ensemble
functionals. It does not evaluate an $L^\infty$ class at each nonatomic point
before integration. $\square$

### Theorem 11.3 — every finite path

For every admitted $\Lambda_D$, finite path $p:D\to E$, and reader
$F\in\mathcal O_E$,

$$
\operatorname{Ens}_E
 (\Lambda_D\operatorname{Ev}_\Xi(p))(F)
=\operatorname{Ens}_D(\Lambda_D)
 (\operatorname{Heis}_\Xi(p)(F)).
$$

**Proof.** Induct on path length. The empty case is identity. Suppose the
result holds for $p:D\to E$ and let $g:E\to F$ be primitive. Ensemble closure
places $\Lambda_D\operatorname{Ev}(p)$ in $\mathfrak E_E$. Then

$$
\begin{aligned}
\operatorname{Ens}_F(\Lambda_D\operatorname{Ev}(p)K_g)
&=\operatorname{Ens}_E(\Lambda_D\operatorname{Ev}(p))\circ\Phi_g\\
&=\operatorname{Ens}_D(\Lambda_D)
  \circ\operatorname{Heis}(p)\circ\Phi_g\\
&=\operatorname{Ens}_D(\Lambda_D)
  \circ\operatorname{Heis}(g\circ p).
\end{aligned}
$$

The first equality is primitive ensemble duality, the second is the induction
hypothesis, and the third is Heisenberg functoriality. Kernel associativity is
the Markov tower property. $\square$

### Corollary 11.4 — no depth testing

The theorem holds for every finite admitted program. It is not an inference
from testing several continuation depths. It does not extend to an infinite
history without separate tightness, projective-limit, and convergence data.

## 12. Continuous feedback and conditioning

### Definition 12.1 — decomposable policy

A continuous feedback policy is a predeclared almost-everywhere measurable
field $r\mapsto\Phi_r$ of normal UCP maps with common tagged endpoints. It is
admitted when the corresponding decomposable map is normal UCP, lands in the
declared target algebra, preserves the ensemble class, and retains every
memory coordinate needed later.

### Theorem 12.2 — exact integrated feedback

An admitted continuous policy composes with every admitted finite prefix and
suffix while preserving Theorem 11.3. Two versions equal $\nu_D$-almost
everywhere have the same complete program predictions for every admitted
ensemble.

**Proof.** Every reachable record marginal is dominated by $\nu_D$ by path
closure. Therefore the version difference is null for every reachable input.
The decomposable arrow satisfies primitive duality, and Theorem 11.3 composes
it with the remaining finite path. $\square$

### Exact control 12.3 — phase feedback

Continue the uniform qubit instrument of Control 8.6 with

$$
V_r=e^{-irZ}.
$$

For final observable $A$, `Ev` predicts

$$
\int_0^1
(\rho\circ\operatorname{Ad}_{U^*})
(V_r^*AV_r)\,dr.
$$

The Heisenberg whole-program arrow gives

$$
\int_0^1 U^*V_r^*AV_rU\,dr,
$$

whose evaluation in $\rho$ is the same number. The policy uses the continuous
record without a point restart state.

### Proposition 12.4 — conditioning

A central event $\Delta$ with positive ensemble probability defines a
normalized conditional ensemble and normal hybrid state. A finite or atomic
positive point may define an exact branch state. A null singleton does not.

Conditioning changes a prediction given information. It does not choose which
outcome is actual.

## 13. Complete boundaries and division

### Definition 13.1 — future sufficiency

A boundary is sufficient for the licensed context family when

$$
\operatorname{Ens}_D(\Lambda_1)
=\operatorname{Ens}_D(\Lambda_2)
$$

implies equality of every complete future reader probability for every
licensed continuation.

### Theorem 13.2 — Heisenberg factorization implies sufficiency

If every licensed continuation has a Heisenberg arrow on the complete hybrid
boundary and Theorem 11.3 holds, equal hybrid states give equal future
profiles.

**Proof.** Each future probability is evaluation of the same Heisenberg
reader in the equal input state. $\square$

### Proposition 13.3 — frontier and record are insufficient alone

A lower-set frontier, retained record, or exact sample does not by itself
prove Definition 13.1. Hidden process memory, an omitted source correlation,
or a future-dependent decomposition label is an exact counterexample. Such a
boundary must be refined or the continuation refused.

The construction therefore distinguishes:

```text
protocol frontier
retained record
positive conditioning event
future-sufficient division
actual outcome/history
```

No implication among the last four is assumed beyond the theorems printed.

## 14. Certified concurrency

### Definition 14.1 — complete exchange certificate

For co-enabled incomparable primitives $g_v,g_w$, a certificate contains:

1. equality of complete composed `Heis` maps;
2. equality of complete frozen `Ev` kernel representatives;
3. exact tagged source and target objects;
4. exact output-record permutation and occurrence multiplicity;
5. source, probe, apparatus, and memory lineage; and
6. measure-class/null-ideal compatibility.

Equality on one input state, one reader, one marginal, or only after
integration is not an exact certificate.

### Definition 14.2 — exchange congruence

Let $\sim_{\rm ex}$ be the least category congruence generated by complete
certified squares. It is an identification after semantics, not a partial
composition rule.

### Theorem 14.3 — reachable finite schedule equality

If every reachable co-enabled incomparable pair is certified in every
reachable record context, all linear extensions of the finite slot partial
order give the same complete `Ev` kernel and `Heis` map up to the declared
record permutation.

**Proof.** Any two finite linear extensions are connected by adjacent swaps
of incomparable elements. The reachable-context hypothesis supplies a valid
complete certificate at each intermediate swap. Apply the congruence
successively. $\square$

Uncertified serializations remain distinct procedures. This theorem derives
no microscopic causal order, time coordinate, or foliation.

## 15. Localized relativistic instruments

### Definition 15.1 — system--probe scheme

A registered localized scheme contains

$$
s=(\mathcal A,\mathcal B,K,\Theta,\sigma,\mathsf E),
$$

where $K$ is a compact coupling region, $\mathcal B$ is the probe theory,
$\sigma$ is the incoming probe state, $\Theta$ is the frozen
outgoing-to-incoming scattering automorphism, and $\mathsf E$ is a finite
POVM or admitted standard-Borel probe instrument.

For a positive probe effect $B$,

$$
\mathcal J_{s,B}(A)
=(\operatorname{id}\otimes\sigma)\Theta(A\otimes B).
$$

### Theorem 15.2 — complete CP instrument

$\mathcal J_{s,B}$ is CP. For a complete finite POVM $\{B_r\}$,

$$
\sum_r\mathcal J_{s,B_r}
=\mathcal J_{s,1},
\qquad
\mathcal J_{s,1}(1)=1.
$$

In a represented $W^*$ packet the maps are normal when the scattering and
slice maps are normal.

**Proof.** Positive probe compression, the star automorphism, and the positive
slice are CP. Completeness and linearity give normalization. $\square$

For continuous outcomes, admission additionally requires Definition 8.4.

### Theorem 15.3 — localization scope

Under the registered Fewster--Verch localized-coupling hypotheses and named
Haag property or exact substitute, the induced observable is localized in
the causal hull of $K$. The complete nonselective operation acts identically
on registered observables spacelike to that hull.

This is a theorem for admitted system--probe schemes, not arbitrary CP maps.

### Definition 15.4 — factorizing multiprobe family

A family enters a concurrency theorem only when all coupling regions,
supports, sources, probes, and correlations are typed and the complete
scattering maps obey the named causal-factorization identity. Independent
probes use the declared product source. A correlated source is a different
joint mechanism.

The complete maps and kernels then supply the exchange certificate of
Definition 14.1.

## 16. No-signalling, steering, and Bell predicates

### Theorem 16.1 — nonselective no-signalling

Let $\{B_a\}$ be a complete localized instrument in one region and $D_b$ a
registered spacelike reader effect. Then

$$
\sum_a p(a,b\mid\omega)
=\omega(\mathcal J_{A,1}(D_b))
=\omega(D_b).
$$

**Proof.** Sum the complete local outcome instrument, then use Theorem 15.3.
Microcausal commutation alone is not substituted for operation locality.
$\square$

### Proposition 16.2 — selective steering

For a retained positive-support event $\Delta$,

$$
p(b\mid\Delta,\omega)
=\frac{p(\Delta,b\mid\omega)}{p(\Delta\mid\omega)}
$$

may differ from $p(b\mid\omega)$. This is steering, not signalling: comparing
the conditional subensemble requires the random classical record. A
nonatomic singleton is replaced by a positive event or an almost-everywhere
posterior statement; it is not normalized as a point state.

### Proposition 16.3 — Bell ledger

A Bell-local completion requires a setting-independent source measure and

$$
p(a,b\mid x,y,\lambda)
=p_A(a\mid x,\lambda)p_B(b\mid y,\lambda).
$$

The split/type-I qubit control gives $S=2\sqrt2$ with unbiased marginals. QFT
Bell theorems provide existential observable/state controls under their own
hypotheses, not exact localized probe realizations for every ideal observable.

Einstein causality, operational no-signalling, parameter independence,
outcome independence, measurement independence, and Bell factorization are
therefore kept distinct.

## 17. Presentation, packet transport, and operational quotient

### Definition 17.1 — full presentation transport

A presentation isomorphism transports:

- the comparator, supports, slot incidence, ports, and guards;
- quantum and hybrid algebras;
- record spaces, regime tags, and measure classes;
- sample spaces, ensemble classes, and normal-state evaluation maps;
- all posterior/control fields modulo the transported null ideal;
- every `Ev` kernel and `Heis` map;
- sources, probes, apparatus, memory, and readers; and
- record and operation occurrence multiplicity.

A continuous record bijection must carry one measure class equivalently to
the other. Coordinate bijection without null-ideal transport is insufficient.

### Theorem 17.2 — transported semantics

A full packet isomorphism induces an isomorphism of path and hybrid categories
and intertwines `Ev`, `Ens`, and `Heis`. Every transported complete program
has the same transported joint law.

**Proof.** Primitive source/target types and all paired semantic maps
intertwine by definition. Induction over finite paths plus Theorem 11.3 gives
the result. $\square$

A proper `Loc` embedding still supplies observable transport and state
pullback only. It is not a full experiment pushforward.

### Definition 17.3 — complete operational equivalence

For parallel procedures in one admitted packet, write $p\sim_{\rm op}p'$ if
every compatible prefix, ancillary probe, adaptive continuation, record
operation, coarse-graining, discard, and complete reader gives the same joint
law in every admitted state and context, in both semantic layers at their
printed equality level.

### Theorem 17.4 — congruence and quotient

$\sim_{\rm op}$ is a category congruence on the reachable constructor-complete
interface. Hence

$$
q_{\rm rel}^{(31)}:
\mathcal P_{\rm rel}^{(31)}
\longrightarrow
\mathcal Q_{\rm rel}^{(31)}
$$

exists and has the ordinary quotient universal property.

**Proof.** Pre- and postcomposition and every registered constructor produce
another frozen context. Equality under all complete contexts is preserved.
Quotienting a category by a congruence gives the result. $\square$

The quotient is reachable and packet scoped. New readers or boundary schemas
may refine it. No microscopic inverse is inferred.

## 18. Positive histories and prefix coherence

### Definition 18.1 — history law

For a finite path, iterate its complete primitive `Ev` kernels. The history
records the frontier, exact retained sample values, and complete exposed
predictive values. Standard-Borel branches are measure kernels, not assumed
point densities.

Denote the resulting measure by $\Gamma_p$.

### Theorem 18.2 — normalization and quantum agreement

$\Gamma_p$ is a normalized positive measure for every admitted finite path,
and every complete registered reader has the same law under $\Gamma_p$ as
under the composed quantum instrument.

**Proof.** Complete primitive kernels are normalized. Repeated kernel
composition preserves total mass. At each cylinder step, the unchanged v2
kernel is the outcome/posterior law of the same frozen quantum instrument, so
the primitive branch-instrument identity and induction identify every
registered finite cylinder probability. Theorem 11.3 independently
identifies every complete final hybrid-reader expectation, and measurable
pushforward identifies each registered reader law.
$\square$

### Theorem 18.3 — prefix coherence

Marginalizing every complete suffix returns the literal performed-prefix law.

**Proof.** Repeatedly integrate normalized suffix kernels. $\square$

Prefix coherence is not factorization through every intermediate frontier.
Only a future-sufficient boundary licenses restart.

### Cost theorem 18.4

The positive predictive object may carry global entanglement and complete
process memory. It is contextual, background dependent, packet indexed, and
unselected. `Ens` removes no such cost; it only gives the admitted ensemble a
normal hybrid representation.

Thus $\Gamma_p$ is an operational positive-history representation, not a
selected local microontology or actuality law.

## 19. Contextuality, fibers, and scalar ontology

### Proposition 19.1 — same-slot contextuality control

In a declared finite split/type-I calibration, the two preparation measures

$$
\tfrac12\delta_{|0\rangle\langle0|}
+\tfrac12\delta_{|1\rangle\langle1|}
$$

and

$$
\tfrac12\delta_{|+\rangle\langle+|}
+\tfrac12\delta_{|-\rangle\langle-|}
$$

have the same barycentric density operator and distinct supports. Their
procedure types survive before operational quotienting. A system-facing
positive assignment need not factor through the predictive quotient.

No procedure-name tag is inserted as a hidden physical variable.

### Proposition 19.2 — idle-fiber nonselection

For any normalized standard probability space $(Z,\zeta)$,

$$
\widetilde\Gamma_p=\Gamma_p\otimes\zeta
$$

with projection to the original predictive object preserves every registered
prediction. No invariant required to be natural under this admitted
projection selects the idle fiber or its prior.

This is a scoped underdetermination theorem. It neither asserts that the
fiber exists nor eliminates physically coupled hidden structure.

Complex amplitudes remain indispensable in the phase-complete quantum
comparator representation. This construction neither proves them ontic nor
eliminates them through diagonal probabilities.

## 20. Covariance and physical frames

### Theorem 20.1 — no undeclared scheduling frame

Jointly transported packet data obey Theorem 17.2, and fully certified
incomparable serializations obey Theorem 14.3. Therefore no undeclared
coordinate chart, source-code order, or scheduling foliation changes a
registered law in the certified domain.

### Proposition 20.2 — physical rest-frame control

Let $\beta_v$ be a boost automorphism and let an admitted KMS, material, or
apparatus state $\omega$ be noninvariant. Then for some observable $A$,

$$
\omega(A)\ne\omega(\beta_v(A)).
$$

The state selects a physical rest frame without violating covariance of the
law under jointly transported data.

The construction therefore proves scheduling covariance, not universal
fixed-state invariance and not absence of every idle microscopic frame.

## 21. Operator-algebra and continuum firewalls

### Proposition 21.1 — type-III-safe formulation

All core formulas use normal positive functionals, effects, and normal CP
maps. They require no intrinsic regional density matrix, trace, finite Kraus
list, or tensor factor.

### Proposition 21.2 — split control

A matrix/tensor calibration is admitted only for a separated inclusion with a
collar and a verified type-I intermediate factor or exact substitute. It does
not extend automatically to touching regions or gauge-constrained algebras.

### Proposition 21.3 — Reeh--Schlieder cost

Dense local action on a cyclic vector does not give deterministic bounded-cost
remote preparation. Norm growth, success probability, postselection, source,
and record cost remain in the packet. The complete operation still obeys
Theorem 16.1.

### Type walls 21.4

Observable algebras, charged fields, gauge actions, sectors, edge/center
variables, particle descriptions, records, and histories are distinct types.
No gauge group, charge spectrum, particle ontology, preferred Fock
representation, or actualized sector is selected.

The abstract-net result constructs no interacting $3+1$ theory. A free-field,
finite-mode, lattice, or split control is not universal dynamics. Cutoff
removal requires a separate renormalization/convergence theorem. Relative
Cauchy evolution describes response to a declared background perturbation; it
is not metric dynamics or gravity.

## 22. Target-theorem disposition

| Target | Construction disposition | Exact boundary |
|---|---|---|
| V31-T1 | `CONSTRUCTED-INHERITED` | finite v2 frontier/path category unchanged |
| V31-T2 | `CONSTRUCTED` | one fully tagged hybrid object per admitted boundary |
| V31-T3 | `CONSTRUCTED` | complete finite direct-sum arrow is normal UCP |
| V31-T4 | `CONSTRUCTED-FINITE / CONDITIONAL-ATOMIC` | exact normal point state only at an atom |
| V31-T5 | `CONSTRUCTED-CONDITIONALLY` | common class and strong predual field required |
| V31-T6 | `REFUSAL-CONSTRUCTED` | generic nonatomic point state/restart absent |
| V31-T7 | `CONSTRUCTED-CONDITIONALLY` | every deterministic pullback proves nonsingularity |
| V31-T8 | `CONSTRUCTED-CONDITIONALLY` | NEP/landing/posterior/class closure per instrument |
| V31-T9 | `CONSTRUCTED` | tagged hom-sets and total matched composition |
| V31-T10 | `CONSTRUCTED` | contravariant `Heis` functor |
| V31-T11 | `CONSTRUCTED-CONDITIONALLY` | ensemble-level primitive theorem plus induction |
| V31-T12 | `CONSTRUCTED-CONDITIONALLY` | measurable decomposable continuous policies |
| V31-T13 | `CONSTRUCTED` | discard/coarse targets remove unavailable reads |
| V31-T14 | `CONSTRUCTED` | positive events/atoms condition; null point refused |
| V31-T15 | `CONSTRUCTED-CONDITIONALLY` | full packet/null-ideal/field/multiplicity transport |
| V31-T16 | `CONSTRUCTED-SCOPED` | reachable constructor-complete contexts |
| V31-T17 | `CONSTRUCTED-CONDITIONALLY` | complete two-layer exchange square |
| V31-T18 | `CONSTRUCTED-CONDITIONALLY` | every reachable co-enabled context certified |
| V31-T19 | `CONSTRUCTED-INHERITED-SCOPED` | localized no-signalling/steering/Bell quantifiers |
| V31-T20 | `CONSTRUCTED-INHERITED` | normalized positive histories and prefixes |
| V31-T21 | `REFUSAL/CONDITIONAL-CONTROLS-CONSTRUCTED` | frame/type-III/split/gauge/continuum walls |
| V31-T22 | `DISTINCTION-CONSTRUCTED` | record, conditioning, division, actuality separate |
| V31-T23 | `COMPATIBILITY-INCOMPLETE-AS-REQUIRED` | no selected Barandes configuration/law/trajectory |
| V31-T24 | `UNCONSTRUCTED-AS-REQUIRED` | ontology, time, spacetime, gravity |

Conditional construction means the theorem is proved for every packet that
supplies and verifies the displayed hypotheses. It does not assert that every
QFT instrument or outcome family satisfies them.

## 23. Two-way controls

| ID | Positive control | Hostile control | Construction result |
|---|---|---|---|
| C1 | finite direct-sum record | branch list alone | complete UCP arrow only |
| C2 | binary result drives later `I/X` | nonselective sum drives guard | exact branchwise formula only in positive arm |
| C3 | complete arrow unital | individual branch unital | branch generally nonunital |
| C4 | atomic point normal | nonatomic evaluation | exact split proved |
| C5 | dominated joint law | nonatomic Dirac | `Ens` only for admitted law |
| C6 | a.e. posterior field | canonical null posterior | latter refused |
| C7 | one common boundary class | per-route classes | latter is not one object |
| C8 | nonsingular pullback | merely measurable constant map | latter refused |
| C9 | graph-compatible append | blind product class | latter singular |
| C10 | equivalent classes | singular class replacement | only former is packet gauge |
| C11 | faithful state as technical domination | physical prior/selector | latter forbidden |
| C12 | tagged explicit skip | empty path | distinct arrows |
| C13 | present record guards future | future record guards past | latter untyped |
| C14 | measurable decomposable field | nonmeasurable/unbounded field | latter refused |
| C15 | all memory exposed | hidden cache | latter breaks duality |
| C16 | discard removes coordinate | later read | latter untyped |
| C17 | positive event conditioning | null point normalization | latter refused |
| C18 | evaluated all-reader identity | scalar outcome agreement | latter insufficient |
| C19 | complete map/kernel exchange | one-state equality | latter insufficient |
| C20 | every reachable swap certified | one initial square | latter no global theorem |
| C21 | output permutation explicit | silent record reorder | latter refused |
| C22 | product source exposed | hidden correlation | latter a joint mechanism |
| C23 | transport null ideal/multiplicity | coordinate-only relabel | latter incomplete |
| C24 | full packet isomorphism | proper embedding state push | latter unavailable |
| C25 | nonselective no-signalling | selected steering | predicates separated |
| C26 | physical KMS/material frame | law-level preferred foliation | no inference between them |
| C27 | normal type-III functional | universal density/trace | latter refused |
| C28 | split with collar | touching/gauge tensor split | latter refused |
| C29 | record retained by typed future | erasure/discard | persistence grammar relative |
| C30 | future-sufficient boundary | frontier/sample alone | latter not division |
| C31 | law over possible records | actual sample selection | actuality absent |
| C32 | laboratory slot protocol | microscopic event web/time | latter absent |
| C33 | declared comparator spacetime | emergent geometry | latter absent |
| C34 | exact v2 physical input | parameter retuning | no retuning performed |

## 24. Mandatory hostile attacks

Each attack has an exact construction response.

1. **Uniform point evaluation.** On $[0,1]$ with Lebesgue class, two
   representatives differing at one point refute point evaluation; T6 fires.
2. **Null representative swap.** `Ens` is unchanged by Theorem 5.2 because
   every admitted marginal is dominated.
3. **Nonatomic Dirac input.** The law lies outside $\mathfrak E_D$ and is not
   used as a restart state.
4. **Positive coarse event.** Proposition 12.4 constructs its normalized
   conditional ensemble.
5. **Declared atom.** Proposition 3.5 constructs its exact normal point state.
6. **Uncountable singular routes.** Definition 6.1 refuses a common object.
7. **Constant Lebesgue pullback.** Lemma 6.2 detects the singular delta
   pushforward.
8. **Null graph append.** The target must carry a graph-dominating class or a
   different schema.
9. **Equivalent versus singular class.** Only equivalent classes give the
   same tagged null ideal.
10. **Faithful state promoted to prior.** Definition 6.1 and the type wall
    forbid the promotion.
11. **Non-NEP instrument.** Definition 8.4 refuses retained exact continuous
    control.
12. **Approximate NEP promoted to exact.** The result remains approximate or
    terminal.
13. **Ambient-only extension.** Failure to land in $\mathcal O_D$ rejects the
    arrow.
14. **No measurable posterior kernel.** `Ev` and one-step duality remain
    unconstructed for that instrument.
15. **Same `Ens`, hidden memory.** Proposition 5.4 refines or refuses the
    boundary.
16. **Same scalar record law, different quantum fields.** All-reader duality
    detects the difference.
17. **Finite measurement plus `I/X`.** Control 8.3 reproduces the exact law.
18. **Branch as complete arrow.** Nonunitality and missing central output
    reject it.
19. **Nonselective sum as record-bearing arrow.** The sum erases the guard and
    fails Control 8.3.
20. **New measurement drops old fiber.** Proposition 8.2 requires the old
    record coordinate.
21. **Skip collapsed to identity.** Exact endpoint tags keep them distinct.
22. **Mismatched target schemas called parallel.** Hom typing rejects them.
23. **Future-result guard.** The source boundary lacks the record.
24. **Read after discard.** The target schema has no such coordinate.
25. **Fine read after coarse-graining.** It is absent unless explicitly
    retained as separate memory.
26. **Nonmeasurable continuous guard.** Definition 12.1 refuses it.
27. **Null version made visible by singular preparation.** The preparation is
    a new route requiring a new class/schema before evaluation.
28. **Unevaluated `Ens` integral.** Definition 5.1 and Theorem 5.2 require the
    normal-state evaluation.
29. **One-reader duality.** Definition 11.1 requires equality as normal states
    on the complete algebra.
30. **Presentation collapses occurrences.** Definition 17.1 carries exact
    multiplicity.
31. **Packet transport omits measure class.** It is not a full packet
    isomorphism.
32. **Proper-embedding state push.** Definition 1.2 supplies pullback only.
33. **One-state exchange certificate.** Definition 14.1 requires full maps and
    kernels.
34. **Output permutation omitted.** The certificate is incomplete.
35. **Source correlation hidden.** Definition 15.4 treats it as a different
    joint mechanism.
36. **Initial-only certification.** Theorem 14.3 quantifies over every
    reachable adaptive context.
37. **Uncertified incomparable exchange.** The paths remain distinct.
38. **Arbitrary antichain schedule theorem.** Frontier incomparability alone
    supplies no certificate.
39. **Steering called signalling.** The selected record cost distinguishes
    the predicates.
40. **Commutation called no-signalling.** Theorem 16.1 requires complete
    localized operation identity.
41. **QFT Bell observable called probe realization.** Proposition 16.3 keeps
    the existential and instrument claims separate.
42. **Every local state called density matrix.** Proposition 21.1 refuses it.
43. **Arbitrary gauge/touching split.** Proposition 21.2 refuses it.
44. **KMS frame called fundamental foliation.** Proposition 20.2 classifies it
    as contingent state/apparatus data.
45. **Retained record called permanent.** Discard or erasure ends its typed
    availability.
46. **Continuous sample called division.** Definition 13.1 requires future
    sufficiency; T6 also blocks point restart.
47. **Conditioning called actualization.** Proposition 12.4 expressly denies
    the inference.
48. **Slot/record counted as duration or volume.** Nonclaims 1.3 block it.
49. **Hybrid algebra called ontology.** Cost Theorem 18.4 blocks selection.
50. **Import of v16 geometry/selector/FLRW/fusion.** Frozen authority contains
    no such input.
51. **Physical parameter changed.** The construction contains no fit or new
    physical constant.
52. **Paper 04 opened early.** Downstream remains closed pending terminal
    hostile adjudication.

## 25. Independent-audit attacks absorbed into construction

The audits add the following nonredundant checks.

1. A dominated scalar marginal without a strongly measurable predual
   barycenter fails Definition 3.3.
2. A predictive object not evaluable as a normal state on the complete
   exposed algebra fails Definition 3.3.
3. A one-step output outside $\mathfrak E_E$ fails Proposition 6.4 and blocks
   path induction.
4. A singularly larger technical class changes the tagged object even if its
   new sector is unused.
5. Two disjoint append graphs need one class dominating both or different
   schemas.
6. A mixed atomic/nonatomic class permits restart only at its declared atoms.
7. Pointwise UCP maps with a nonmeasurable matrix coefficient do not define a
   decomposable arrow.
8. Same underlying CP map with different endpoint tags remains two arrows.
9. A.e.-equal controls are not exact frozen-kernel exchange evidence.
10. A coarse result cannot revive discarded fine memory.
11. A positive coarse conditioning does not make each contained singleton
    positive.
12. A statewise family $\Phi_\rho$ is not one physical Heisenberg arrow.
13. Statewise posterior versions without a jointly measurable kernel fail
    `Ev` admission.
14. Stochastic singularization is detected by Lemma 6.3 even when every
    deterministic map passes.
15. An unbounded $L^1$ state density is allowed; essential boundedness is not
    incorrectly imposed on $h$.
16. A delayed two-step hidden-memory read fails Proposition 5.4.
17. A nonlinear future access to an ensemble decomposition is extra exposed
    physics or is refused.
18. An infinite-horizon claim is not obtained from Theorem 11.3.
19. A posterior version chosen after seeing a null sample is forbidden
    post-hoc selection.
20. A positive source atom mapped to a target-null point fails Lemma 6.2.

No attack requires changing the pin or a physical law.

## 26. Product

| Coordinate | Provisional construction status | Exact boundary |
|---|---|---|
| input | `BOUND` | immutable v2 mathematics and v3.1 authority |
| slot-skeleton | `DECLARED-LABORATORY-PROTOCOL` | finite partial order, not ontology |
| frontier | `CONSTRUCTED-TYPE` | lower set, not automatic division |
| boundary | `CONSTRUCTED-TAGGED` | complete ports, records, regime, class, memory |
| sample-semantics | `CONSTRUCTED-INHERITED` | exact point-valued v2 `Ev` kernels |
| ensemble-semantics | `CONSTRUCTED-CONDITIONALLY` | dominated laws and strong predual fields |
| hybrid-object | `CONSTRUCTED` | finite exact; integrated conditional |
| heisenberg-functor | `CONSTRUCTED` | normal UCP opposite-category semantics |
| integrated-compatibility | `CONSTRUCTED-CONDITIONALLY` | every admitted law/path/reader |
| point-restart | `FINITE/ATOMIC-CONSTRUCTED; NONATOMIC-GENERIC-UNCONSTRUCTED` | no fictitious Dirac state |
| presentation | `CONSTRUCTED` | tags, classes, fields, kernels, maps, multiplicity |
| quotient | `CONSTRUCTED-SCOPED` | constructor-complete reachable interface |
| covariance | `CONSTRUCTED-CONDITIONALLY` | full packet isomorphism only |
| state-class | `CONDITIONAL-ADMISSION` | common class, normal evaluation, path closure |
| instrument | `FINITE-CONSTRUCTED; CONTINUOUS-CONDITIONAL` | NEP/landing/posterior/null ideal |
| causal-factorization | `CONSTRUCTED-CONDITIONALLY` | complete localized maps and sources |
| certified-schedule | `CONSTRUCTED-CONDITIONALLY` | all reachable co-enabled contexts |
| no-signalling | `CONSTRUCTED-SCOPED` | complete nonselective localized operation |
| steering | `CONSTRUCTED-CONTROL` | selected positive event and record cost |
| bell | `CONSTRUCTED-EXISTENTIAL-COMPATIBILITY` | no universal exact localized probe |
| positive-model | `CONSTRUCTED-WITH-COSTS` | global/contextual/memory-bearing/unselected |
| context | `CONSTRUCTED-SCOPED` | registered procedures and complete contexts |
| fibers | `CONSTRUCTED-SCOPED` | idle extension nonselection only |
| type-III | `REFUSAL/MODEL-SPECIFIC` | normal functional/map formulation |
| split | `CONDITIONAL-CONTROL` | collar and split hypothesis |
| gauge | `TYPED-UNSELECTED` | no universal factorization/sector ontology |
| particles | `TYPED-UNSELECTED` | no preferred Fock ontology |
| continuum | `ABSTRACT-COMPARATOR-CONDITIONAL` | no interacting model derived |
| UV | `SCOPED-REFUSAL` | no cutoff-removal theorem |
| preferred-frame | `NO-UNDECLARED-SCHEDULING-FRAME` | physical state/apparatus frames allowed |
| record | `CONSTRUCTED-OPERATIONALLY` | exact sample; normal point state iff atomic |
| division | `FUTURE-SUFFICIENCY-TEST-REQUIRED` | frontier/record/sample alone insufficient |
| actuality | `UNCONSTRUCTED` | no branch or trajectory selector |
| barandes | `COMPATIBLE-BUT-INCOMPLETE` | no selected configuration/law/state/trajectory |
| ontology | `GLOBAL-PREDICTIVE-CANDIDATE-UNSELECTED` | hybrid algebra is representation |
| downstream | `CLOSED` | no internal time, spacetime, or gravity |

## 27. Outcome and physical meaning

The provisional strongest construction rung is

```text
P03V31-RELATIVISTIC-QUANTUM-OPERATIONAL-ADEQUACY-WITH-GLOBAL-ONTOLOGY-DEBT
```

subject to independent review.

What has been constructed is precise:

- relativistic finite laboratory protocols form a genuine causal-frontier
  category;
- complete retained finite outcomes are single normalized hybrid arrows;
- admitted continuous outcomes and feedback have exact integrated normal
  semantics;
- every admitted finite program has matching stochastic and Heisenberg
  predictions;
- finite/atomic restart survives while generic nonatomic point restart is
  correctly refused;
- records, conditioning, divisions, and actuality remain distinct;
- localized no-signalling, steering, Bell compatibility, covariance, and
  physical-frame controls retain their exact premise ledgers; and
- arbitrary serialization is removed only on the fully certified domain.

What has not been constructed is equally decisive:

- the predictive state has not been selected as physical ontology;
- one actual sample or trajectory has not been selected;
- a Barandes configuration space and universal indivisible law have not been
  derived;
- the declared Lorentzian comparator has not become dynamical;
- laboratory slots have not become microscopic events or time;
- no scale, dimension, signature, metric, stress tensor coupling, curvature
  dynamics, or Einstein equation has been derived.

The construction improves the operational bridge to relativistic quantum
theory. It does not shorten the physical route to gravity by relabeling its
technical objects.

## 28. Review boundary

Before any terminal result, the exact frozen bytes of this paper must pass:

1. a result-neutral construction audit;
2. a frozen hostile-review protocol;
3. mutually blind category/operator-algebra, quantum/probability, and
   ontology/relativity reviews; and
4. independent joint adjudication.

Any semantic counterexample lowers the earliest affected coordinate. A prose,
serialization, or implementation defect cannot retune the physics. There is
no implementation stage in Paper 03 v3.1.

Paper 04 remains closed.

## References

- R. Brunetti, K. Fredenhagen, and R. Verch, “The generally covariant
  locality principle — a new paradigm for local quantum physics,” 2003.
  https://arxiv.org/abs/math-ph/0112041
- C. J. Fewster and R. Verch, “Quantum fields and local measurements,” 2020.
  https://arxiv.org/abs/1810.06512
- C. J. Fewster and R. Verch, “Measurement in Quantum Field Theory,” 2023.
  https://arxiv.org/abs/2304.13356
- K. Okamura and M. Ozawa, “Measurement theory in local quantum physics,”
  2016. https://arxiv.org/abs/1501.00239
- B. Coecke, C. Heunen, and A. Kissinger, “Categories of quantum and classical
  channels,” 2014. https://arxiv.org/abs/1305.3821
- C. J. Fewster, “The split property for locally covariant quantum field
  theories in curved spacetime,” 2016. https://arxiv.org/abs/1601.06936
- C. J. Fewster and R. Verch, “Dynamical locality and covariance,” 2012.
  https://arxiv.org/abs/1106.4785
- S. J. Summers and R. Werner, “Maximal violation of Bell's inequalities is
  generic in quantum field theory,” 1987.
  https://doi.org/10.1007/BF01207366

These sources support the stated measurement, covariance, and representation
scope. They do not select ontology, actuality, spacetime, or gravity.
