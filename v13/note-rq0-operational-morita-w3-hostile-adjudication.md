# Joint adjudication — operational Morita geometry of W3 records

**Status:** `CYCLE-CLOSED / HEADLINE-DOWNGRADE`

**Date:** 2026-08-01

**Governing pin:** `35a487877d357bbeb60e11df31e1c8b6f37e1b6e`

**Immutable paper:** `a1fa2c9cdd7f04189328c17357575abc72af54b4`

**Higher-stack/rigidification review:**
`88f053a393d8fcba716fdb6eab10f2a262b9ffc8`

**Operator-algebra/Morita review:**
`09263d5fd6547ee6fcba1869f2a3c09737a5c18d`

**CQM/instrument review:**
`80a26b19ff0388b4e4aac98d9b116f33ebf3dae2`

**Mode:** joint adjudication only; no review-time repair

---

## 1. Executive decision

All three independent reviews return `HEADLINE-DOWNGRADE`. The cumulative
paper headline

$$
\texttt{RQ0-L0-FULL-ADDRESSABILITY-FIBRATION}
$$

is withdrawn.

The CQM/instrument review supplies an exact counterexample at the first
registered rung. Because the pin's ladder is cumulative, that earliest valid
counterexample controls the cycle disposition even though the other two
reviews accepted the first rung at a less discriminating effect-level
reading.

None of the four new registered positive outcomes is earned:

$$
\boxed{
\begin{aligned}
&\texttt{RQ0-L0-COMPLETE-INSTRUMENT-W3}
&&\text{not earned},\\
&\texttt{RQ0-L0-MORITA-INVARIANT-W3-SEAMS}
&&\text{not earned},\\
&\texttt{RQ0-L0-EFFECTIVE-W3-SEAM-STACK}
&&\text{not earned},\\
&\texttt{RQ0-L0-FULL-ADDRESSABILITY-FIBRATION}
&&\text{not earned}.
\end{aligned}}
$$

The registered disposition of this successor is

$$
\boxed{\texttt{RQ0-L0-BLOCKED-AT-COMPLETE-INSTRUMENT-W3}.}
$$

This is a construction-level counterexample, not an absence verdict. The
paper successfully builds a candidate-independent complete **effect** law and
several correct conditional operator-algebraic structures. It does not retain
the complete CP instruments as part of the W3 object, and its general eraser
predicate can pass when no admitted outcome probability witnesses recovered
coherence.

The strongest positive registered repository result therefore remains the
antecedent

$$
\boxed{\texttt{RQ0-L0-ADDRESSABLE-W3-OPERATOR-SYSTEM},}
$$

with exactly the law-relative, admitted-repeatable-coarse-graining meaning
fixed by adjudication #76. Nothing in this cycle weakens that antecedent.

The strongest new unregistered package is:

> A source-relative, complete-effect-marked W3 candidate theory with an
> exact universal block theorem, sharp POVM-effect availability, algebraic
> cross-block erasure, finite classical actions, and pairwise transport under
> explicitly supplied endomorphism *-isomorphisms.

That package is useful analytical evidence. It is not complete-instrument
W3, a marked-Morita seam category, an effective stack, an addressability
fibration, or spatial localization.

---

## 2. Immutable evidence

The adjudication uses only the frozen pin, immutable paper, and three reports
committed verbatim before this decision:

| Artifact | SHA-256 | Size |
|---|---|---:|
| governing pin | `d7f83221c706e420d6c77e25fe645085cb7cb43cea2e75f629850623f2c99dac` | 22,181 bytes; 664 lines |
| immutable paper | `cb36418645f845fc35b9e1c77e71a37f1c5a9d6779cae8526a2dfba2ff138537` | 61,012 bytes; 1,853 lines |
| higher-stack report | `793407825637546c07a9223860964363da1cb2546a307673f71015dda1ee0f10` | 26,799 bytes; 658 lines |
| operator-algebra report | `1bce44ba2498ea5ba7e877ca2dbe9e867ae21e735431de0b6291022ab3c4aa35` | 28,935 bytes; 805 lines |
| CQM/instrument report | `8c135e8656a6fe3dc5330a977865bcad236dd40423cebf3f1202c25185ce4f14` | 28,274 bytes; 804 lines |

The paper was committed before review dispatch. Every reviewer was
repo-read-only and used scratch space only. Each complete report was frozen
in its own commit. The paper has not been edited, repaired, or rescored.

---

## 3. Why the stricter first-rung review governs

The stack and operator reviewers correctly rebuilt the paper's block theorem,
singleton rejection, branch count, objectwise imprimitivity transport, and
Karoubi control. They consequently called the first rung
`RQ0-L0-COMPLETE-INSTRUMENT-W3` earned.

The instrument reviewer tests a distinction those rebuilds did not test:

$$
\boxed{
\text{a complete family of outcome effects}
\ne
\text{a retained complete CP instrument}.
}
$$

It also closes the paper's eraser predicate into a full admitted experiment
and shows that a nonzero individual complex cross term need not change any
admitted complete-readout probability.

Both findings directly invoke binding clauses of the pin:

1. the W3 object must contain actual branches of complete admitted source and
   readout instruments, not only their normalized-state or POVM shadows; and
2. erasure must connect coherence to the written alternatives and a complete
   admitted experiment, not merely to an arbitrary matrix element.

An exact counterexample to a universal registered theorem defeats that rung
even when every displayed benchmark happens to pass. The disagreement is
therefore resolved in favor of the instrument review. The first two reports'
positive calculations survive at their narrower effect-level scope; their
rung assignment does not.

---

## 4. First obstruction I — the W3 tuple forgets its instruments

The ambient marking does contain outcome-indexed CP instruments. The problem
is the object later called complete-instrument W3.

Its selected source is recorded as normalized postselected states

$$
S=(\rho_\alpha)_{\alpha\in A},
$$

while a genuine preparation instrument from a trivial input has CP branches

$$
\mathcal P_\alpha(1)=p_\alpha\rho_\alpha.
$$

Different nonzero branch weights, and for a nontrivial source boundary
different branch dynamics, collapse to the same displayed $S$. Ambient
membership of an instrument does not make the omitted branch map part of the
candidate datum.

At the output, sharp readability retains the POVM effects $(e_j)$ and a
coarse outcome map through

$$
V^*\!\left(\sum_{\ell(j)=r}e_j\right)=p_r.
$$

It does not retain the corresponding CP branches. Hence it cannot distinguish
the Lüders instrument

$$
\mathcal L_r(\rho)=P_r\rho P_r
$$

from a measure-and-reprepare instrument

$$
\mathcal J_r(\rho)=\operatorname{Tr}(P_r\rho)\tau_r,
$$

because both have

$$
\mathcal L_r^*(I)=P_r=\mathcal J_r^*(I)
$$

while their state changes and future continuation laws differ. For
$P_A=Q_0+Q_1$, $\tau_A=Q_0$, and input $Q_1$,

$$
\mathcal L_A(Q_1)=Q_1,
\qquad
\mathcal J_A(Q_1)=Q_0.
$$

The paper therefore constructs complete source-branch **state** scope and
complete output **effect** scope, not a W3 object retaining complete quantum
instruments and their disturbance semantics.

---

## 5. First obstruction II — algebraic erasure can be operationally silent

The paper defines coherent erasure using an individual off-diagonal complex
number

$$
z=
\rho_\alpha\!\left(U^*(q_kE^*(a)q_\ell)\right)
\ne0.
$$

For $k\ne\ell$, the inserted operator is generally neither self-adjoint nor
positive. Its value under a state is a useful algebraic matrix coefficient,
but it is not automatically the probability of a closed CP experiment.

The instrument review gives a complete four-level countermodel. Let

$$
q_i=|i\rangle\langle i|,
\qquad
p_A=q_0+q_1,
\qquad
p_B=q_2+q_3.
$$

Use a complete computational source and choose the write columns

$$
\begin{aligned}
U|0\rangle&=(|0\rangle+|2\rangle)/\sqrt2,&
U|1\rangle&=(|1\rangle+|3\rangle)/\sqrt2,\\
U|2\rangle&=(|0\rangle-|2\rangle)/\sqrt2,&
U|3\rangle&=(|1\rangle-|3\rangle)/\sqrt2.
\end{aligned}
$$

Each source branch has at most one fine component in either coarse sector, so
the paper's write-correlation condition holds. A matched no-write control
with a superposition of $q_0$ and $q_1$ supplies the required within-sector
failure.

Admit the complete readouts

$$
(p_A,p_B)
\qquad\text{and}\qquad
(a,I-a),
$$

where

$$
a=|\chi\rangle\langle\chi|,
\qquad
|\chi\rangle=(|0\rangle+i|2\rangle)/\sqrt2.
$$

Let the preserving channel be the coarse dephasing

$$
V^*=\mathcal D_R,
\qquad
\mathcal D_R(x)=p_Axp_A+p_Bxp_B,
$$

and take $E^*=\operatorname{id}$ as the candidate eraser. Universal block
preservation and the sharp $(p_A,p_B)$ pullback both hold.

For the first written branch

$$
|\psi\rangle=(|0\rangle+|2\rangle)/\sqrt2,
$$

the paper's eraser term is

$$
z=\langle\psi|q_0aq_2|\psi\rangle=-\frac{i}{4}\ne0.
$$

But the actual probability contrast vanishes:

$$
\langle\psi|a|\psi\rangle
-
\langle\psi|\mathcal D_R(a)|\psi\rangle
=z+\bar z=0.
$$

Both probabilities equal $1/2$. The same equality holds for every outcome in
the declared output effect system. Thus the paper accepts a full candidate
whose alleged recovered coherence changes no admitted complete-readout
probability.

The paper's branch-memory benchmark is not refuted: its chosen cross terms are
positive real and do give a nonzero contrast. What fails is the general
registered theorem. A benchmark-specific success cannot repair this
counterexample.

---

## 6. Mathematics retained from the immutable paper

### 6.1 Candidate-independent complete-effect semantics

The output operator system

$$
\mathcal E_D(x)
=
\operatorname{span}_{\mathbb C}
\{I,e_j:e_j\text{ is an admitted outcome effect}\}
$$

is fixed by the admitted law before a candidate record is examined. It
correctly prevents the old favorable-singleton selection.

For a finite record PVM $(p_r)$, the dephasing map

$$
\mathcal D_R(b)=\sum_rp_rbp_r
$$

has fixed operator system equal to the block-diagonal commutant. Hence

$$
\mathcal D_RT(a)=T(a)
\iff
p_rT(a)p_s=0\quad(r\ne s)
\iff
T(\mathcal E)\subseteq C_R'.
$$

This theorem, the complete $Z$-versus-$ZX$ discriminator, and the full-matrix
unitary negative all survive.

### 6.2 Classical action and fine/coarse structure

At the stated finite sharp scope, a unital *-homomorphism

$$
\lambda:\mathbb C^\Omega\to\mathcal L_A(M)
$$

is equivalent to a PVM in the endomorphism algebra, and a map of finite
outcome sets gives the fine-to-coarse action. This is a sound internal
packaging of an already selected sharp record question. It does not select a
unique record or actual atom.

The stronger phrase “Frobenius object inside the combined correspondence/CP
architecture” is not earned because that ambient dagger-monoidal typing was
not supplied. The finite classical C*-algebra and its module action are the
secure result.

### 6.3 Pairwise transported markings

For an explicitly supplied imprimitivity bimodule, tensoring boundary modules
induces the endomorphism *-isomorphism

$$
\Theta_X^M:
\mathcal L_A(M)
\overset{\cong}{\longrightarrow}
\mathcal L_B(M\otimes_A X).
$$

When every state, effect, channel, instrument, comparison, scalar context and
classical action is explicitly transported through these isomorphisms, all
displayed effect-level W3 equations have the same values. This pairwise
transport theorem is correct.

It is invariance under an exact transported marking induced by an
imprimitivity module. It is not yet a theorem on a constructed marked
operational Morita localization.

### 6.4 Matrix-spectator calculation

For the standard $\mathbb C$--$M_n$ imprimitivity module,

$$
\mathcal L_{M_n}
\bigl(H\otimes\mathbb C^{1\times n}\bigr)
\cong B(H).
$$

Transporting exactly the old marking therefore does not add a spectator
observable. This objectwise calculation survives. It is a declared
presentation change, not a black-box discovery of inaccessibility, and the
paper does not prove the pin's fully general $A\leftrightarrow A\otimes M_n$
case.

### 6.5 Full CP Karoubi arrow

The underlying CP Karoubi category is sound: a corner arrow satisfies

$$
h=fhe.
$$

For two noncommuting dephasings, $h=e_me_n$ satisfies the corner equation and
is noninvertible. This correctly restores an irreversible arrow omitted by an
earlier construction.

It does not establish the seam-compatible addressability category, because
the general record-interface compatibility equation remains undefined.

### 6.6 Fixed branch-memory classification

At the benchmark's explicit source, atomic-action, terminal-readout and
effect-law postulates, the finite partition calculation yields exactly

$$
6\text{ candidates of type }2+1+1
\quad\sqcup\quad
3\text{ candidates of type }2+2.
$$

These are nine effect-level W3 candidates. The printed unsigned permutation
lift proving the $S_4$ action is false, but independent exact enumeration in
two reviews finds corrected signed-monomial lifts and recovers the abstract
$S_4$ action with the same two partition-type orbits. The corrected result is
external analytical evidence; it is not a valid proof inside the immutable
paper.

---

## 7. Independent failures above the first rung

The cumulative failure already withholds every later registered result. The
three reports also identify independent defects that must not be hidden by
that dependency.

### 7.1 The marked operational Morita localization is not constructed

The paper mixes correspondences, CP maps, states, effects, instruments and
scalar contexts without defining a single typed bicategory, double category,
equipment or multi-sorted process category in which all constructors and
markings compose.

It names

$$
\mathbf{Pres}_D[\mathcal W_{\mathrm{Mor}}^{-1}]
$$

without defining the marked 1-morphisms and 2-morphisms, horizontal
composition, coherence, localization universal property, or W3 action on
every localized arrow. W3 objects are defined, but W3 morphisms are not.

The objectwise equivalence theorem therefore does not produce the registered
Morita-invariant W3 category or pseudofunctor.

### 7.2 Ineffective isotropy confuses equality with equivalence

The rigidification kernel is defined using a strictly identity action, while
the spectator conclusion uses transformations naturally isomorphic to the
identity. The paper supplies neither a strictification, a bicategorical
2-kernel, a specified family of natural transformations, nor a 1-truncation
identifying 2-isomorphic arrows.

It also does not construct the asserted raw $U(n)$ spectator isotropy inside
the proposed seam groupoid. Consequently the matrix-spectator calculation
does not yield the registered effective stack.

### 7.3 The physical-spectator proposition is misstated

The induced endomorphism map $\Theta_X$ is surjective. Hence an operator in
the induced endomorphism algebra cannot fail to lie in its image, contrary to
the proposition's hypothesis.

The meaningful discriminator is whether a new effect lies outside the image
of the transported **admitted marked effect family**, or whether the physical
boundary object has been enlarged. The concrete physical-spectator control
uses the latter and remains useful; the general proposition as written is
vacuous.

### 7.4 The addressability morphism condition is undefined

The corner equation $h=fhe$ is exact, but “carry the seam observability maps”
has no displayed equation. Pointwise preservation, outcome relabelling,
operator-system inclusion, classical-action intertwining and span
preservation are inequivalent choices.

Without choosing one and proving closure, the morphism sets of
$\mathsf{Addr}(s)$, their pseudofunctorial transport and their Grothendieck
fibration are not constructed. Restricting benchmark idempotent objects to
identities also does not remove nonidentity CP morphisms between those
objects.

### 7.5 The printed symmetry proof is false

For many output permutations, the displayed unsigned choice

$$
T_2=P,
\qquad
T_1=V^*PV,
\qquad
T_0=U^*T_1U
$$

does not satisfy all four named-process intertwining equations. Independent
exact checks find failure for sixteen of twenty-four pure permutations.
Signed-monomial lifts recover the intended abstract group, but that is a
repair not present in the immutable proof.

---

## 8. Registered outcome disposition

| Registered outcome | Joint disposition | Reason |
|---|---|---|
| `RQ0-L0-COMPLETE-INSTRUMENT-W3` | **NOT EARNED** | The object drops CP-instrument witnesses and its individual eraser cross term has an exact complete-law operational false positive. |
| `RQ0-L0-MORITA-INVARIANT-W3-SEAMS` | **NOT EARNED** | Cumulative failure; independently, the marked bicategory/localization, W3 morphisms and pseudofunctor are not constructed. |
| `RQ0-L0-EFFECTIVE-W3-SEAM-STACK` | **NOT EARNED** | Cumulative failure; independently, strict versus natural isotropy is unresolved and the printed symmetry lift is false. |
| `RQ0-L0-FULL-ADDRESSABILITY-FIBRATION` | **NOT EARNED** | Cumulative failure; independently, record-compatible fiber arrows and pseudofunctorial descent are undefined. |
| `RQ0-L0-BLOCKED-AT-COMPLETE-INSTRUMENT-W3` | **SELECTED** | First exact obstruction in the cumulative pin. |
| antecedent `RQ0-L0-ADDRESSABLE-W3-OPERATOR-SYSTEM` | **PRESERVED** | The prior law-relative effect transport, sharp-proposition transport and admitted-idempotent coarse-graining theorem is not reopened. |

The later blocked labels are not selected because the first registered
failure occurs earlier. Their independent findings remain binding evidence
for any possible successor.

---

## 9. Ontological meaning

The new paper does not establish a new kind of quantum region.

It establishes that a physically declared complete **effect interface** can
test whether every admitted outcome question has become block diagonal with
respect to a candidate sharp record. It also shows how that sharp classical
question behaves under exact changes of module presentation.

It does not yet establish that the complete measurement **process**—including
outcome-conditioned state change and future continuation—is retained by the
record object. Nor does its general eraser test guarantee an observable
interference difference in the admitted law.

Accordingly:

$$
\boxed{
\text{sharp record question and effect-level evidence}
\ne
\text{complete record instrument}
\ne
\text{actual fact}
\ne
\text{localized region}.
}
$$

No selected truth value, W6 fact co-reference, event token, autonomous
subsystem, physical overlap, spatial locality, topology, influence, causal
order, Lorentzian geometry, field theory or gravity follows.

---

## 10. Closure and stopping rule

The operational-Morita W3 cycle is closed at

$$
\boxed{\texttt{RQ0-L0-BLOCKED-AT-COMPLETE-INSTRUMENT-W3}.}
$$

The immutable paper and all three reviews remain historical evidence. No
review-time repair is made. The antecedent terminal result remains
`RQ0-L0-ADDRESSABLE-W3-OPERATOR-SYSTEM` at its existing scope.

No successor, repair, overlap, localization, `RQ0-T1`, `RQ0-C1`, topology,
influence, causality, geometry, spacetime, field or gravity work is authorized
by this adjudication. Halt and request explicit authorization before any
further cycle.
