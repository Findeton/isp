# Positive record histories for finite quantum processes

## Exact operational equivalence and the remaining ontology problem

Date: 2026-08-22

Status: **CONSTRUCTION — GREEN-UNREVIEWED; NO PHYSICAL RESULT AWARDED**

## Abstract

This paper asks whether an indivisible stochastic ontology can represent the
complete finite-dimensional quantum-process interface, rather than only an
isolated transition matrix. We prove a positive representation theorem for
every finite number of laboratory slots, arbitrary finite system dimensions,
general completely positive instruments, adaptive control, ancillas,
discard, entanglement, and finite-memory process tensors. The construction
uses a reversible dilation of the entire experiment, physical setting and
outcome registers, and an ordinary nonnegative probability measure on the
resulting record histories. Sequential composition is composition of typed
experimental programs followed by one whole-process evaluation; it is not
stochastic-kernel factorization at every slot. Tensor composition, convex
mixing, conditioning on recorded outcomes, and ignored-slot consistency are
preserved.

The same proof identifies a strict explanatory limit. Phase-sensitive data
cannot be removed from the complete contingent/process input. The map
$U\mapsto |U|^2$ is not functorial under sequential composition. Bell and
Peres--Mermin statistics forbid an experiment-independent local and
noncontextual value completion under their standard premises. Most
importantly, first-order indivisible transition laws do not determine a
Kolmogorov measure on microscopic trajectories: distinct path measures can
have identical licensed first-order laws. Quantum operational data therefore
determine a contextual family of positive record-history measures, but not a
unique configuration ontology or microscopic actual trajectory.

The earned construction-level ceiling is consequently
`P01-COMPOSITIONAL-OPERATIONAL-EQUIVALENCE-WITH-ONTOLOGY-DEBT`, not a derivation
of nature's ontology. Hilbert space can be removed from the list of asserted
beables, but equivalent phase-complete operational structure remains in the
construction. One actual recorded history may be postulated; its microscopic
completion and selection are not derived.

## 1. Question and scope

The frozen question is:

> Does there exist one uniform typed relational stochastic-history
> architecture whose operational quotient is naturally equivalent to the
> complete finite-dimensional quantum process interface over tiers Q0--Q3,
> and if so, what costs are unavoidable?

The answer is mixed:

1. **Yes at the operational record-history level.** Every registered quantum
   process has an ordinary positive stochastic representation, uniform in
   finite dimension and finite slot number, which respects the physical
   composition of experiments.
2. **No derivation of a complete microscopic ontology follows.** The
   representation retains phase-sensitive process data, uses externally
   supplied laboratory slot order, and leaves both its microscopic
   configuration basis and its non-Markovian trajectory realizer
   underdetermined.

The target is causally ordered finite-slot process tensors or quantum combs.
Indefinite-causal-order process matrices, continuous-variable systems, QFT,
spacetime, and gravity are outside the theorem. Standard-Borel outcome
instruments are covered by the measure-valued extension in Section 6; all
explicit controls use finite outcomes.

No statement in this paper is evidence that the stochastic representation is
the ontology used by nature. Exact empirical equivalence is precisely why a
later discriminator or an independently motivated principle is required.

## 2. Operational quantum target

### 2.1 Systems, events, and instruments

For a finite-dimensional Hilbert space $\mathcal H$, a quantum event from
$\mathcal H_A$ to $\mathcal H_B$ is a completely positive,
trace-nonincreasing linear map

$$
\mathcal I_a:\mathsf L(\mathcal H_A)\longrightarrow
\mathsf L(\mathcal H_B).
$$

A finite instrument is a family $\{\mathcal I_a\}_{a\in A}$ such that

$$
\sum_{a\in A}\mathcal I_a
$$

is trace preserving. The outcome probability and normalized conditional
state are

$$
p(a\mid\rho,\mathcal I)=\operatorname{tr}\mathcal I_a(\rho),
\qquad
\rho_a=\frac{\mathcal I_a(\rho)}{p(a\mid\rho,\mathcal I)}
$$

when $p(a\mid\rho,\mathcal I)>0$. The zero-probability event remains typed but
has no conditional state.

Classical randomization is physical: if an independent recorded coin chooses
$\mathcal I$ with probability $q$ and $\mathcal J$ with probability $1-q$,
the resulting operation is $q\mathcal I+(1-q)\mathcal J$.

### 2.2 Finite-slot processes

An $n$-slot process $W$ is the operational multilinear functional that maps a
compatible sequence of local CP events to a nonnegative joint probability,

$$
p_Q(a_1,\ldots,a_n\mid x_1,\ldots,x_n,W),
$$

including arbitrary finite ancillary extensions. It is normalized for every
sequence of deterministic instruments, affine under independently controlled
classical mixtures, and consistent when an ignored slot is filled with its
deterministic operation.

This is the causally ordered process-tensor/comb domain. Its slot order is
laboratory intervention order supplied by the comparator. It is not yet a
spacetime order or a fundamental time variable.

### 2.3 Realization lemma

**Lemma 1 (finite process realization).** Every finite-dimensional,
finite-slot process in Section 2.2 has a realization by a finite-dimensional
memory $M$, an initial state on system plus memory, and a sequence of
isometries between slots. Every finite-outcome instrument has an isometric
implementation with an orthogonal outcome record. All isometries can be
extended to unitaries after adding finite blank ancillas.

**Proof.** A CP map has a finite Kraus representation

$$
\mathcal I_a(\rho)=\sum_{\alpha=1}^{r_a}
K_{a\alpha}\rho K_{a\alpha}^{\dagger}.
$$

Instrument normalization gives

$$
\sum_{a,\alpha}K_{a\alpha}^{\dagger}K_{a\alpha}=I.
$$

Hence

$$
V_{\mathcal I}|\psi\rangle
=\sum_{a,\alpha}K_{a\alpha}|\psi\rangle
\otimes|a\rangle_R\otimes|\alpha\rangle_E
$$

is an isometry. Every finite-dimensional isometry extends to a unitary on a
larger finite-dimensional space by completing an orthonormal basis.

For a process tensor, apply the same argument recursively to its positive
Choi operator and causal normalization constraints. Equivalently, use the
comb realization: the first causal trace constraint gives an initial memory
channel; removing its Choi factor leaves the next positive normalized comb;
finite induction yields a sequence of memory channels. Stinespring dilation
of each memory channel produces the claimed isometries. This is the
finite-dimensional content of the quantum-comb realization theorem. QED.

The constructive point is essential. We do not start with a table of outcome
probabilities. We first build the physical circuit, its setting controls,
memory, environment, and record registers.

## 3. The positive record-history construction

### 3.1 Typed experiment programs

For a target process $W$ and a finite adaptive experiment $e$, form a typed
program

$$
\mathcal P=(W,\rho,c,\{\mathcal I^{x_k}_{a_k}\}_{k=1}^{n},r),
$$

where $\rho$ is the contingent preparation when not already part of $W$,
$c$ is the physical classical-control rule, and $r$ is the final reader.
Adaptive settings $x_k$ are controlled by earlier setting/outcome registers,
not by an evaluator branch invisible to the physical program.

Programs compose by wiring output ports to compatible input ports before
evaluation. Parallel composition is disjoint tensor wiring. Discard is a
typed output termination implemented by a partial trace in the target and by
coarse-graining all unobserved dilation records in the stochastic image.

### 3.2 Reversible compilation

Use Lemma 1 to compile $\mathcal P$ into one reversible dilation

$$
U_{\mathcal P}:\mathcal H_{\rm src}\otimes\mathcal H_{\rm blank}
\longrightarrow
\mathcal H_{\rm out}\otimes\mathcal H_R\otimes\mathcal H_E.
$$

$R$ contains physical records of the settings actually used and outcomes
actually returned. $E$ contains unobserved dilation degrees of freedom. A
mixed source is purified or represented by a classical source register; the
choice is quotient gauge when it leaves every complete experiment unchanged.

Let $s$ label an orthogonal source configuration and $\omega(s)$ its
contingent probability. Let $h$ be a complete physical record string and
$\lambda$ a basis label in a chosen dilation presentation. Define

$$
\Gamma_{\mathcal P}(h,\lambda\mid s)
=\left|
\langle h,\lambda|U_{\mathcal P}|s,0\rangle
\right|^2.
$$

This is nonnegative and, by unitarity,

$$
\sum_{h,\lambda}\Gamma_{\mathcal P}(h,\lambda\mid s)=1.
$$

The physical record-history law is the pushforward

$$
\boldsymbol\Gamma_{\mathcal P}(h\mid\omega)
=\sum_s\omega(s)\sum_{\lambda}
\Gamma_{\mathcal P}(h,\lambda\mid s).
$$

The sum over $\lambda$, rather than one chosen Kraus or environment label,
is mandatory. A change of Kraus representation or environment basis may
redistribute the fine-grained terms while leaving the physical pushforward
unchanged.

### 3.3 Candidate packet

The constructed packet is

$$
\mathfrak S_{\rm rec}=
(\mathsf{Cfg}_{\rm rec},\mathsf{Hist}_{\rm rec},\mathsf{Exp}_{\rm dil},
\mathsf{State}_{Q},\boldsymbol\Gamma,\mathsf{Read},
\mathsf{Gauge}_{\rm dil},\mathsf{Act}).
$$

Its components are:

- $\mathsf{Cfg}_{\rm rec}$: typed physical source, setting, outcome, and
  persistent-record values;
- $\mathsf{Hist}_{\rm rec}(\mathcal P)$: the standard-Borel space of actual
  setting/outcome record strings for $\mathcal P$;
- $\mathsf{Exp}_{\rm dil}$: reversible-dilation programs modulo the complete
  gauge in Section 10;
- $\mathsf{State}_{Q}$: the operational preparation/process equivalence
  class, kept separate from the universal evaluation rule;
- $\boldsymbol\Gamma$: the pushforward law above;
- $\mathsf{Read}$: typed coarse-grainings of physical record strings;
- $\mathsf{Gauge}_{\rm dil}$: simultaneous changes of Hilbert presentation,
  Kraus frame, and unused dilation basis preserving the full program;
- $\mathsf{Act}$: one actual record history may be postulated, but is not
  selected by normalization.

This packet is relational in the limited but exact sense that only typed
port incidence, program wiring, and operationally distinguishable record
relations survive its presentation quotient. It assumes neither a lattice
nor geometry. It does retain laboratory control order.

### 3.4 Why this is not a terminal lookup table

The probability is not attached independently to each requested answer. The
same rules perform all of the following before any reader is applied:

1. compose CP events and process memory by port wiring;
2. construct their common reversible dilation;
3. transport physical setting and outcome records;
4. evaluate one normalized measure on complete record histories;
5. push that measure through any admitted reader.

Changing an instrument's post-measurement channel changes the compiled
dilation and later probabilities even when its immediate POVM is unchanged.
Adding a continuation acts on the same retained process object. This is a
uniform construction, not a finite answer catalogue.

## 4. Main operational theorem

**Theorem 1 (positive record-history representation).** For every causally
ordered finite-dimensional quantum process with finitely many slots and every
finite-outcome adaptive instrument experiment, the construction in Section 3
defines an ordinary normalized probability measure on typed physical record
histories such that:

1. all complete outcome probabilities equal the target quantum values;
2. physical classical mixtures are affine;
3. recorded-outcome conditioning agrees with quantum conditioning;
4. ignored slots agree with deterministic-operation insertion and record
   coarse-graining;
5. sequential program composition is natural under whole-process evaluation;
6. parallel composition is symmetric monoidal;
7. unused ancillas and dilation/Kraus presentation changes are non-kills;
8. process tomography separates precisely the target operational classes.

**Proof.** Insert each instrument isometry from Lemma 1 into the memory-channel
realization of $W$. Controlled isometries implement adaptive choices. The
amplitude for a complete outcome record $h=(x_1,a_1,\ldots,x_n,a_n)$ and
unobserved dilation label $\lambda$ is the matrix element of the resulting
global isometry. Summing its modulus square over $\lambda$ contracts exactly
the Kraus indices of the corresponding CP maps. Therefore

$$
\boldsymbol\Gamma_{\mathcal P}(h\mid\omega)
=p_Q(h\mid e,W).
$$

Linearity of the source mixture and an explicit classical coin gives
affinity. Conditioning is ordinary conditional probability on the physical
record event. Summing all outcomes at an ignored slot replaces its instrument
by the deterministic sum channel, proving consistency. Wiring dilations
before evaluation is associative up to typed unitary isomorphism, which proves
sequential naturality at the program level. Tensoring independent dilations
and source states multiplies amplitudes and hence product-history
probabilities; entangled sources and joint operations remain global rather
than factorized. Adding a blank unused ancilla multiplies by a unit-norm
factor. Unitary changes among Kraus/environment coordinates cancel under the
complete sum over $\lambda$. Finally, a separating process-tomography family
distinguishes two process tensors exactly when some complete program
probability differs. QED.

### 4.1 What sequential naturality does not mean

The theorem does not claim

$$
\Gamma_{g\circ f}=\Gamma_g\Gamma_f
$$

at every intermediate configuration. Composition in
$\mathsf{Exp}_{\rm dil}$ means wire the physical programs and evaluate the
resulting whole. Kernel multiplication is permitted only at a boundary whose
recorded state is future-sufficient.

This distinction is forced already by a Hadamard gate $H$. In its standard
basis,

$$
|H|^2=
\frac12
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}
=B,
\qquad H^2=I.
$$

But

$$
B^2=B\ne I=|H^2|^2.
$$

Thus modulus-squared endpoint kernels are not a functor under ordinary
stochastic-kernel composition. The phase-sensitive whole program is
irreducible at that cut.

## 5. State--law separation and phase completeness

### 5.1 Universal rule versus contingent process data

The fixed rule is:

> Given a typed operational process state, a typed experiment program, and a
> contingent source state, compose their reversible dilation and push its
> squared-amplitude measure to physical records.

The process state $W$, preparation $\rho$, and selected controls are arguments
of that rule. They are not universal constants. A future fundamental theory
would still have to explain which process resources and Hamiltonians nature
realizes.

This is a valid state--law separation for an operational representation. It
is not yet a derivation of a unique law of nature.

### 5.2 Coherence-retention theorem

**Proposition 2 (diagonal data are incomplete).** No translation whose
contingent state factors only through the diagonal probabilities in one fixed
configuration basis can reproduce all common continuations.

**Proof.** The states

$$
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},
\qquad
|-\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}
$$

have the same diagonal probability vector $(1/2,1/2)$. A fixed-basis
diagonal-only state map therefore identifies them. After the same Hadamard
continuation, however, they become $|0\rangle$ and $|1\rangle$, which a
computational-basis reader distinguishes with certainty. QED.

The necessary information may be represented by complex amplitudes, by an
operational process functional, or by some other phase-complete structure.
Calling it stochastic does not make it disappear.

### 5.3 Mixtures and purification

The state map is defined on operational density/process classes. Consequently
two ensemble decompositions of the same density operator remain identical
under every continuation unless the decomposition label is stored in a
physical record.

If $|\psi\rangle_{AE}$ and $|\phi\rangle_{AF}$ purify the same reduced state
on $A$, Schmidt decomposition gives equal nonzero Schmidt coefficients and an
isometry $V:E\to F$ satisfying

$$
|\phi\rangle_{AF}=(I_A\otimes V)|\psi\rangle_{AE}
$$

after enlarging the purifying space if needed. Such a change is dilation gauge
when $E,F$ are inaccessible; it becomes physical when an admitted experiment
acts differently on the purifying system.

## 6. Standard-Borel outcomes

Let $X$ be a standard-Borel outcome space and $B\mapsto\mathcal I_B$ a
countably additive CP instrument on finite-dimensional input/output systems.
Its Choi operator $J(B)$ is a positive matrix-valued measure. The finite
scalar measure

$$
\mu(B)=\operatorname{tr}J(B)
$$

dominates every matrix entry. The Radon--Nikodym theorem gives a measurable
positive matrix density $j(x)$ with

$$
J(B)=\int_B j(x)\,d\mu(x).
$$

Measurable spectral factorization yields a measurable Kraus density. It
defines an isometry into a separable direct-integral record space
$L^2(X,\mu)$, and the physical history law is the corresponding pushforward
measure on $X$. Standard-Borel regular conditional probabilities permit
finite adaptive induction.

Therefore Theorem 1 extends to standard-Borel outcomes, at the cost of a
separable rather than necessarily finite record ancilla. No unbounded system
Hilbert space is introduced; only the classical outcome register may be
infinite.

## 7. Instruments are more than effects

Consider the computational projectors $P_a=|a\rangle\langle a|$. Define two
qubit instruments with the same immediate effects:

$$
\mathcal I_a^{\rm L}(\rho)=P_a\rho P_a,
\qquad
\mathcal I_a^{\rm R}(\rho)=
\operatorname{tr}(P_a\rho)|0\rangle\langle0|.
$$

Both return

$$
p(a)=\operatorname{tr}(P_a\rho).
$$

Conditioned on $a=1$, however, the Lüders instrument leaves $|1\rangle$ while
the reset instrument leaves $|0\rangle$. A later $Z$ reader distinguishes them
with certainty.

In the record-history construction, the immediate reader coarse-grains both
dilations to the same $a$ distribution, while their retained output ports and
dilation programs differ. They therefore have different complete
continuation profiles. This passes the instrument-disturbance gate and shows
why terminal outcome tables are insufficient.

## 8. Composition, Bell correlations, and contextuality

### 8.1 Tensor composition

For independent programs with amplitudes $A(h,\lambda)$ and
$B(k,\eta)$,

$$
|A(h,\lambda)B(k,\eta)|^2
=|A(h,\lambda)|^2|B(k,\eta)|^2.
$$

Thus product states and product experiments factor exactly. Entangled source
states are not product inputs, so their joint record measure need not factor.
Discarding one output sums all of its record/environment alternatives and
agrees with the target partial trace. A blank unused ancilla contributes one
normalized factor and is a non-kill.

### 8.2 Exact CHSH control

Use $|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2$ and observables

$$
A_0=Z,\qquad A_1=X,
$$

$$
B_0=\frac{Z+X}{\sqrt2},\qquad
B_1=\frac{Z-X}{\sqrt2}.
$$

For outcomes $a,b\in\{-1,+1\}$,

$$
p(a,b\mid x,y)=\frac14
\left(1+ab\,\langle A_x\otimes B_y\rangle\right).
$$

The four correlations are

$$
E_{00}=E_{01}=E_{10}=\frac1{\sqrt2},
\qquad E_{11}=-\frac1{\sqrt2},
$$

so

$$
S=E_{00}+E_{01}+E_{10}-E_{11}=2\sqrt2.
$$

Every local marginal is $1/2$ independently of the remote setting. The
compiled record-history measure reproduces these values because the settings
are physical control records and the source is one entangled process state.

### 8.3 Bell premise ledger

The construction earns operational no-signalling. It does **not** earn an
Einstein-local ontic completion.

| Premise or property | Construction status |
|---|---|
| operational setting freedom | assumed in the registered experiment; no source-setting correlation added |
| operational no-signalling | constructed exactly |
| one pre-setting complete hidden variable | not constructed |
| parameter independence conditional on that variable | therefore unearned |
| outcome independence conditional on that variable | therefore unearned |
| Bell factorization | not satisfied or derived |
| global/contextual dependence of complete outcome law | present |
| superluminal causal influence | neither derived nor ruled out by the operational representation |
| relativistic locality | outside Paper 01 |

The standard obstruction is immediate. If a pre-setting variable $\lambda$
with measurement-independent density $\mu(\lambda)$ supplied local response
means $A_x(\lambda),B_y(\lambda)\in[-1,1]$, then

$$
\left|
A_0(B_0+B_1)+A_1(B_0-B_1)
\right|\le2
$$

for every $\lambda$, and averaging gives $|S|\le2$. Hence the exact quantum
control forbids that local factorized completion. A completed history that
already contains settings and outcomes cannot be relabeled a pre-setting
local cause; doing so merely hides the failed premise in the word “history.”

### 8.4 Peres--Mermin control

Use the commuting contexts

$$
\begin{array}{ccc}
X\otimes I&I\otimes X&X\otimes X\\
I\otimes Y&Y\otimes I&Y\otimes Y\\
X\otimes Y&Y\otimes X&Z\otimes Z.
\end{array}
$$

Every row product and the first two column products equal $+I$; the last
column product equals $-I$. A context-independent assignment of values
$v(O)\in\{-1,+1\}$ would make the product of the three row constraints $+1$.
The same nine values multiplied through the columns would have to give $-1$,
a contradiction.

The stochastic construction does not assign outcomes to all six
incompatible contexts simultaneously. The chosen commuting context and its
physical apparatus are part of the typed program; its actual outcomes are in
the record history. Therefore contextuality is physically typed rather than
stored as an invisible evaluator key. This is a contextual representation,
not a noncontextual explanation of the Peres--Mermin statistics.

## 9. Multi-time processes and three distinct notions of memory

### 9.1 Complete process translation

Lemma 1 and Theorem 1 apply to every finite-slot causally ordered process
tensor. The retained memory system in its dilation is a declared resource.
For a fixed finite process, it can be finite-dimensional, although its minimal
dimension may grow with system dimension and slot count.

Ignoring a slot inserts the deterministic channel and sums the corresponding
record. Adaptive control is a controlled physical operation. A separating
instrument basis reconstructs the process tensor from its probabilities, so
the record-history image retains every operational distinction in the target.

### 9.2 Operational Markov condition

A causal break at a slot discards the incoming system and prepares a new state
chosen independently of the past. A process is operationally Markov at that
cut exactly when, after every such break, all future statistics depend on the
new preparation but not on earlier controls or outcomes.

A sequence of system-only unitary channels is Markov in this sense. By
contrast, let a memory bit $M$ be uniformly random and retained by the
environment. At two successive times, overwrite a system bit $S$ with $M$.
At the middle time read $S$, then perform a causal break that prepares
$S=0$. The final output still equals the earlier value of $M$, and hence the
earlier outcome. This process is operationally non-Markovian.

### 9.3 CP divisibility does not decide process memory

In the memory-bit example, the one-time reduced map at each noninitial target
is the same completely depolarizing channel $D$. Thus

$$
\Lambda_{1:0}=D,
\qquad
\Lambda_{2:0}=D=I\circ D,
$$

so the displayed one-time family is CP-divisible. Nevertheless the causal
break detects memory. CP divisibility of reduced one-time maps is therefore
not sufficient for operational process Markovianity.

On the enlarged carrier $S+M$, the evolution can be represented by ordinary
memoryless controlled permutations. Memory and divisibility are always
relative to the declared carrier and intervention interface.

### 9.4 Barandes indivisibility is a different coordinate

The two-Hadamard example has no positive two-state restart factorization at
the unrecorded intermediate basis cut:

$$
|H^2|^2=I\ne |H|^2|H|^2=B.
$$

Yet as a process with a controllable middle slot, its future after a causal
break depends only on the newly prepared quantum state; no environment memory
is present. Hence stochastic nondivision at a proposed configuration cut does
not imply operational process memory.

Conversely, the memory-bit process is non-Markovian on $S$ but divisible on
the complete $S+M$ boundary. Operational memory on a subsystem does not imply
native nondivision on every enlarged carrier.

The implication table is therefore:

| Notion | What it asks | Implication established here |
|---|---|---|
| stochastic division | does a positive sufficient restart kernel exist on this boundary carrier? | neither equivalent to nor implied by process Markovianity without matched carrier/interface |
| operational process Markov | does a causal break remove all detectable past influence? | stronger multi-time intervention statement than one-time CP divisibility |
| enlarged-state memory | can an added physical memory make evolution Markov? | possible for every finite process realization, at a resource cost |
| CP divisibility | do reduced one-time channels factor through CPTP maps? | not sufficient for operational Markovianity |
| interference nondivision | does an unrecorded alternative admit a positive classical restart? | can occur in a memoryless closed unitary process |
| record stability | do allowed futures transport distinguishable record sectors? | independent of whether an earlier unrecorded cut divided |

### 9.5 First-order process data are not process-tensor complete

Two laboratories can have the same unperturbed source-to-target distribution
while differing under a middle intervention. In one, an environment copies
the intervened middle system into memory and returns it later. In the other,
the environment discards the middle system and prepares the same unperturbed
final state. With the registered unperturbed preparation both give the same
endpoint law; a middle flip distinguishes them.

Therefore a family of unperturbed first-order transition matrices does not
determine the complete process tensor. Complete instruments are not optional
decoration: they specify the counterfactual physical interventions by which
memory is operationally defined.

## 10. Decoherence, transported records, erasure, and uncomputation

### 10.1 One common model

Let $S$ be a path qubit, $R$ a record qubit, and $E$ an environment qubit.
Start with

$$
|+\rangle_S|0\rangle_R|0\rangle_E.
$$

The record writer is a controlled-NOT from $S$ to $R$:

$$
V_{SR}|+00\rangle
=\frac{|000\rangle+|110\rangle}{\sqrt2}.
$$

If $R$ is ignored, the reduced path state is $I/2$. A Hadamard recombiner then
returns outcome $0$ with probability $1/2$. Without the record writer, it
returns $0$ with probability $1$.

### 10.2 Sector transport is not erasure

Applying $X_R$ swaps the record labels:

$$
\frac{|000\rangle+|110\rangle}{\sqrt2}
\longmapsto
\frac{|010\rangle+|100\rangle}{\sqrt2}.
$$

The two sectors remain orthogonal and perfectly readable once the known
transport is accounted for. In typed form, if $P_r^{\rm in}$ and
$P_r^{\rm out}$ are the corresponding projectors, stability is

$$
P_r^{\rm out}F=FP_r^{\rm in}.
$$

A fixed-projector commutator test would incorrectly call this erasure.

### 10.3 Coherent uncomputation

Applying the inverse of every known record-writing and transport operation
returns

$$
|+\rangle_S|0\rangle_R|0\rangle_E,
$$

and the fringe is fully restored. Thus no record is absolutely permanent
under all possible quantum operations.

### 10.4 Irreversible local loss

Now copy $R$ to $E$ before locally uncomputing $R$:

$$
\frac{|000\rangle+|110\rangle}{\sqrt2}
\longmapsto
\frac{|000\rangle+|111\rangle}{\sqrt2}
\longmapsto
\frac{|000\rangle+|101\rangle}{\sqrt2}.
$$

$R$ is blank, but $E$ still carries which-path information. Tracing out $E$
leaves $S$ maximally mixed, so the local fringe remains $1/2$. Only a coherent
inverse acting on every carrier of the information restores the fringe.

The physical distinction is therefore not “record versus no record label.” It
is whether distinguishable which-alternative information remains anywhere in
the complete controlled system and whether the admitted future can access or
uncompute it.

### 10.5 Actuality

The record-history measure assigns alternatives and probabilities. Orthogonal
records explain why alternatives cease to interfere for a restricted reader;
they do not select one alternative. This construction permits the explicit
postulate

> one physical record history occurs in each run with the displayed
> probability law,

but does not derive that postulate or a random-selection mechanism.
Microscopic configuration values at unrecorded intermediate cuts remain a
separate, unresolved issue.

## 11. Complete gauge packet

### 11.1 Kraus and dilation gauge

If

$$
K'_{a\beta}=\sum_\alpha u^{(a)}_{\beta\alpha}K_{a\alpha}
$$

with $u^{(a)}$ unitary on an unobserved Kraus space, then

$$
\sum_\beta K'_{a\beta}\rho K_{a\beta}^{\prime\dagger}
=\sum_\alpha K_{a\alpha}\rho K_{a\alpha}^{\dagger}.
$$

Therefore a naked Kraus index is not a beable. Dilation environments related
by an isometry on an inaccessible complement are likewise gauge at the
registered interface.

### 11.2 Basis changes

A simultaneous unitary conjugation of the state, operations, port maps,
record projectors, and readers is a change of representation. A basis change
applied only to the state or only to the claimed configuration projectors is
not gauge: it changes the physical experiment.

Quantum operational data do not, by themselves, select one preferred
configuration PVM from all possible maximal commuting algebras. A candidate
that asserts one as the fundamental beable algebra owes an additional
physical discriminator or principle.

### 11.3 Reader independence

The physical record-history measure is constructed before diagnostic
coarse-graining. Readers are measurable maps on the same record space. Adding
or removing a diagnostic reader therefore does not redefine the history
quotient. A physical continuation or measurement interaction can change the
history law, but a post hoc relabeling of its output cannot.

## 12. The microscopic trajectory is not determined

### 12.1 First-order realizer theorem

**Theorem 3 (nonunique microscopic realizers).** Licensed first-order
transition probabilities from a conditioning boundary to target boundaries do
not, in general, determine a probability measure on complete microscopic
trajectories.

**Proof by exact counterexample.** Let $X_0=0$ be fixed and let
$X_1,X_2\in\{0,1\}$. Suppose the licensed first-order laws are

$$
p(X_1=0\mid X_0=0)=p(X_1=1\mid X_0=0)=\frac12,
$$

$$
p(X_2=0\mid X_0=0)=p(X_2=1\mid X_0=0)=\frac12.
$$

Define realizer $R_+$ by

$$
p_{R_+}(0,0)=p_{R_+}(1,1)=\frac12
$$

for $(X_1,X_2)$, and realizer $R_-$ by

$$
p_{R_-}(0,1)=p_{R_-}(1,0)=\frac12.
$$

Both have exactly the licensed first-order marginals. Yet

$$
p_{R_+}(X_1=X_2)=1,
\qquad
p_{R_-}(X_1=X_2)=0.
$$

If $t_1$ is not a conditioning event, the first-order law contains no value
that chooses between them. QED.

The example is not a failure of ordinary probability. Each realizer is a
perfectly valid Kolmogorov law. The failure is identifiability: the minimalist
indivisible process specifies an equivalence class of realizers, not one path
measure.

### 12.2 What quantum experiments determine

Quantum process tomography determines all probabilities for admitted
interventions and records. It does not determine simultaneous values for
unperformed incompatible experiments, nor a joint microscopic configuration
at every unrecorded target time.

One may add a complete non-Markovian realizer as new contingent or nomological
data. But then one must answer:

1. why that realizer rather than another member of the equivalence class;
2. whether its microscopic correlations have any operational discriminator;
3. whether it respects the complete gauge and contextual experiment family;
4. whether it introduces Bell-nonlocal, measurement-dependent, retrocausal,
   or otherwise global structure;
5. whether its path probabilities remain consistent when a formerly
   unrecorded cut is turned into a physical intervention.

Maximum entropy, stationarity, a random seed, or a convenient Markov
extension would each be an additional principle. None follows from the
first-order law or from normalization.

### 12.3 No experiment-independent counterfactual table

The Bell and Peres--Mermin controls prove a second limitation. No one positive
experiment-independent table of local, context-independent pre-existing
outcomes can reproduce the registered domain under the usual independence
premises. The positive object constructed here is instead a compatible family
indexed by physical experiment programs. Only the selected settings and their
outcomes occur in the actual record history.

That contextuality is not a defect in probability theory. It is a constraint
on what can be placed in one common sample space while retaining the stated
physical independence and locality assumptions.

### 12.4 Ontology coordinate

$\mathsf{Hist}_{\rm rec}$ is complete for operational records but incomplete
as a microscopic trajectory ontology. A dilation basis label $\lambda$ cannot
simply fill the gap: it changes under Kraus and environment gauge, and a
sequence of such labels still needs a joint path measure not fixed by the
record laws.

The correct construction-level coordinate is therefore

```text
P01-STOCHASTIC-RECORD-HISTORY-REFERENT-CONSTRUCTED
P01-MICROSCOPIC-HISTORY-REFERENT-INCOMPLETE
P01-CONFIGURATION-ONTOLOGY-UNDERDETERMINED
```

## 13. Audit of the stochastic--quantum correspondence

### 13.1 What the established theorem says

Barandes defines a finite indivisible stochastic process using a configuration
space, target times, conditioning times, first-order transition probabilities,
standalone probabilities, and random variables. His stochastic--quantum
theorem proves that every such process can be represented as a subsystem of a
unistochastic process and hence by unitary Hilbert-space dynamics after a
dilation.

That direction is exact and relevant. It does not by itself prove that the
minimal first-order object is a complete multi-time instrument/process-tensor
theory. The reverse claim that a comprehensive quantum system, including its
measurement devices, can be modeled stochastically requires the complete
device/process construction audited in this paper.

### 13.2 Where this paper agrees

The present construction supports four central insights:

1. measurement devices belong inside the physical model;
2. ordinary nonnegative probabilities can describe the resulting records;
3. intermediate kernel factorization is not required at unrecorded cuts;
4. wavefunctions and dilation coordinates need not be declared beables.

It also confirms the importance of system-relative division events and the
fact that a closed unitary experiment may be indivisible when expressed only
through basis transition probabilities.

### 13.3 Where the stronger interpretation remains open

Barandes explicitly notes that the minimalist process is compatible with many
complete Kolmogorov towers, called non-Markovian realizers. Theorem 3 gives the
smallest exact example of that nonuniqueness. Saying that only one trajectory
actually occurs does not select its joint law or explain which intermediate
configuration facts are physically meaningful.

Likewise, a Hilbert representation may be gauge without phase-complete
continuation structure being dispensable. Proposition 2 proves that some
complete contingent/process datum must distinguish equal-diagonal,
different-phase preparations. The physical question is not whether one uses
the word “wavefunction”; it is where the experimentally necessary coherence
information lives.

Finally, the cited indivisible-process work leaves Bell locality to future
analysis. Paper 01 reproduces the Bell statistics and prints their premise
cost, but it does not infer relativistic locality from temporal
non-Markovianity.

## 14. Translation packet and naturality

### 14.1 Forward translation $J$

$J$ sends:

- a quantum system to its typed operational ports and allowed physical record
  interfaces;
- a preparation/process state to its operational equivalence class and a
  reversible preparation/memory dilation;
- an instrument to an outcome-recording isometry class;
- a finite process experiment to the wired whole-program dilation;
- a target outcome to the corresponding physical record reader.

No one Kraus representation, purification, or environment basis is retained
as physical.

### 14.2 Reverse operational translation $K$

On the image of $J$, $K$ maps a stochastic record program to the multilinear
functional obtained by evaluating its complete record probabilities under
all admitted instruments. Complete positivity and causal normalization follow
from the retained dilation class.

For every registered quantum process,

$$
KJ(W)\simeq_{\rm op}W.
$$

The equivalence is natural under sequential wiring, tensor wiring,
coarse-graining, controlled mixtures, and recorded conditioning.

### 14.3 Why $JK$ is not ontological identity

Different dilations, environment frames, and non-Markovian microscopic
realizers can have the same complete record functional. $JK$ therefore returns
an operational equivalence class, not the original hidden presentation or one
unique microscopic history space.

This is the exact sense in which the result is a natural operational
equivalence and still only an ontological representation.

## 15. Registered controls

| Control | Result | Evidence in this paper |
|---|---|---|
| C1 phase completeness | PASS | Proposition 2 and the common Hadamard continuation |
| C2 general dimension | PASS | finite-dimensional Kraus/Stinespring/comb induction, no dimension lookup |
| C3 instrument disturbance | PASS | Lüders versus reset instruments in Section 7 |
| C4 CHSH | PASS operationally | exact $2\sqrt2$ law and premise ledger in Section 8 |
| C5 Peres--Mermin | PASS contextually | six exact product constraints, no counterfactual value table |
| C6 product/entangled separation | PASS | tensor proof and entangled CHSH source |
| C7 process memory | PASS | Markov unitary sequence and causal-break memory-bit process |
| C8 nondivision translation | PASS | two-Hadamard nondivision separated from process memory and CP divisibility |
| C9 record triad | PASS | sector transport, coherent uncompute, leaked-environment control |
| C10 convex randomization | PASS | explicit physical coin and affinity of the law |
| C11 gauge packet | PASS at operational scope | Kraus, dilation, basis, reader distinctions in Section 11 |
| C12 v16 regression | NONCONTRADICTION ONLY | no v16 constants imported; its state/law, nondivision, grammar-relative record, and eraser walls agree structurally |

The C12 row does not claim a byte-level or object-level embedding of Paper 13D.
That historical model remains a separate finite reference.

## 16. Hostile-attack disposition

### 16.1 Representation attacks 1--7

- Phase is retained in the complete operational process datum and tested by a
  common continuation.
- Probabilities are derived from a wired dilation, not copied into terminal
  rows.
- Hilbert data are openly retained as nomological/representational input; no
  elimination claim is made.
- Kraus indices are summed and declared gauge.
- No configuration basis is claimed fundamental without a discriminator.
- The proof is uniform for all finite dimensions.
- No tomography family is selected after observing candidate differences.

### 16.2 Composition attacks 8--14

- Whole continuation equivalence, not one reader, defines $\simeq_{\rm op}$.
- Tensor is defined on complete programs, ports, records, and states.
- Entanglement remains a global source state rather than pre-agreed local
  outcomes.
- Blank unused ancillas are exact non-kills.
- Discard is record/environment marginalization.
- Physical instrument mixing is affine.
- Postselection retains the success record and probability.

### 16.3 Bell/contextuality attacks 15--20

- The source does not depend on later settings in the registered CHSH
  experiment.
- No-signalling is not called ontic locality.
- The construction admits global contextual outcome dependence and states
  that its relativistic causal interpretation is unconstructed.
- Measurement contexts and controls are physical program records.
- No context-independent Peres--Mermin assignment is asserted.
- Neither “retrocausal” nor “all-at-once” is used without a separate law.

### 16.4 Multi-time attacks 21--26

- Instrument slots are not automatically stochastic divisions.
- Memory/environment dimension is declared and finite for each finite target;
  no uniform constant bound is claimed.
- Ignored-slot consistency follows from deterministic-channel insertion.
- Memory is tested by a causal break.
- CP indivisibility and stochastic nondivision remain distinct.
- Program order is explicitly laboratory control order, not emergent time.

### 16.5 Record/ontology attacks 27--36

- A transported sector swap is a non-kill.
- Alleged uncomputation fails when $E$ retains which-path information.
- Stable records are not actualization.
- Microscopic trajectory incompleteness is printed as a product coordinate.
- Readers do not define the underlying record measure.
- All dilation fibers are summed; no representative mass is used.
- Absent variables are not assigned uniform distributions.
- No hidden order is promoted to chronology.
- Contingent process/preparation data remain separate from the evaluator rule.
- No cosmological or root selector is imported.

### 16.6 Scope attacks 37--42

- The theorem is finite-dimensional and finite-slot, with standard-Borel
  classical outcomes; it is not QFT.
- Laboratory order is not spacetime order.
- Operational equivalence is not ontological uniqueness.
- Exact representation is not empirical evidence for ISP.
- The ontology debt is not a no-go theorem against all relational models.
- No Paper 13D constant or binary carrier enters the proof.

## 17. Quantifier and resource ledger

| Item | Exact scope |
|---|---|
| system dimension | every finite dimension |
| slots | every fixed finite number; no uniform infinite-time limit claimed |
| outcomes | finite explicitly; standard-Borel by Section 6 |
| operations | arbitrary CP trace-nonincreasing events and normalized instruments |
| ancillas | arbitrary finite quantum ancillas; separable classical record ancilla for standard-Borel outcomes |
| process class | causally ordered finite-slot process tensors/combs |
| construction | explicit/existential via finite dilation; no finite catalogue |
| memory | finite for each finite process; minimal dimension and uniform scaling not fixed |
| contextuality | physical experiment-context dependence allowed and required |
| law/state | universal evaluation rule fixed; process/preparation data contingent or controlled |
| actuality | one actual record history postulated only; selection not derived |
| time | external laboratory slot order supplied by target |
| geometry | absent |

## 18. Result product

This is a construction result awaiting the frozen independent review required
by the pin. Its proposed product is:

```text
target        P01-QUANTUM-PROCESS-TARGET-BOUND
referent      P01-STOCHASTIC-RECORD-HISTORY-CONSTRUCTED
               + P01-MICROSCOPIC-HISTORY-REFERENT-INCOMPLETE
state-law     P01-STATE-LAW-SEPARATION-CONSTRUCTED-AT-OPERATIONAL-SCOPE
single        P01-ALL-FINITE-SINGLE-SYSTEM-CORRESPONDENCE
instrument    P01-COMPLETE-INSTRUMENT-TRANSLATION
sequential    P01-SEQUENTIAL-NATURALITY-SCOPED-TO-WHOLE-PROGRAM-EVALUATION
tensor        P01-TENSOR-NATURALITY
bell          P01-BELL-NOSIGNALING-REPRODUCED-WITH-GLOBAL-CONTEXTUAL-HISTORY
               + P01-BELL-LOCAL-COMPLETION-UNCONSTRUCTED
context       P01-CONTEXTUALITY-PHYSICALLY-TYPED
multitime     P01-FINITE-CAUSALLY-ORDERED-MULTITIME-PROCESS-EQUIVALENCE
memory        P01-MEMORY-INDIVISIBILITY-RELATION-CLASSIFIED
record        P01-DECOHERENCE-RECORD-ERASURE-TRIAD
equivalence   P01-NATURAL-OPERATIONAL-EQUIVALENCE
hilbert       P01-HILBERT-SECONDARY-AS-BEABLE
               + P01-PHASE-COMPLETE-CONTINUATION-STRUCTURE-REQUIRED
ontology      P01-CONFIGURATION-ONTOLOGY-UNDERDETERMINED
actuality     P01-ONE-ACTUAL-RECORD-HISTORY-POSTULATED
               + P01-MICROSCOPIC-ACTUALITY-UNCONSTRUCTED
preferred     P01-PREFERRED-STRUCTURE-COST-PRESENT
               (configuration algebra and laboratory slot order)
```

The proposed overall ceiling is:

```text
P01-COMPOSITIONAL-OPERATIONAL-EQUIVALENCE-WITH-ONTOLOGY-DEBT
```

No coordinate is terminal until independent mathematics/composition, quantum
information/foundations, and ontology/physics reviews are adjudicated.

## 19. What has and has not been learned

### 19.1 Positive result

Ordinary probability and one actual record history are compatible with the
full finite-dimensional, causally ordered quantum-process interface. Quantum
interference does not require negative probabilities on actual records. It
requires that one not insert positive stochastic restart kernels at cuts that
discard phase-sensitive continuation information.

This substantially strengthens a single-transition correspondence: devices,
disturbance, adaptive instruments, entanglement, contextuality, and process
memory can all be handled in one compositional whole-experiment construction.

### 19.2 Negative result

The construction is not yet a new fundamental theory. It uses the complete
quantum process as input, and it cannot derive:

- a preferred configuration algebra;
- a unique non-Markovian microscopic path measure;
- Bell-local causal structure;
- why one record outcome occurs;
- a unique Hamiltonian, process state, or cosmological state;
- internal time, spacetime, or gravity.

Replacing amplitudes by the complete family of their record probabilities
does not remove equivalent phase-complete continuation content. It changes
the proposed beables and clarifies division, but does not yet explain why the
quantum process law has its form.

### 19.3 The next physical question

The next authorized question is not dimension selection. It is whether a
candidate configuration ontology can be selected by operational facts or a
deeper physical principle, and whether its phase-complete indivisible law can
be formulated without merely re-encoding the quantum process functional.

Before that question opens, this construction must survive the three frozen
review lenses. No implementation is scientifically useful until the
mathematical product is accepted.

## 20. Primary-source spine

1. Jacob A. Barandes, [“Quantum Systems as Indivisible Stochastic
   Processes”](https://arxiv.org/html/2507.21192v1), especially the minimalist
   first-order law, division events, non-Markovian realizers, measurement
   devices, gauge discussion, and explicit Bell-locality deferral.
2. Jacob A. Barandes, [“The Stochastic-Quantum
   Theorem”](https://arxiv.org/html/2309.03085v2), for the theorem that every
   finite indivisible stochastic process embeds as a subsystem of a
   unistochastic process.
3. Giulio Chiribella, Giacomo M. D'Ariano, and Paolo Perinotti,
   [“Theoretical framework for quantum
   networks”](https://arxiv.org/abs/0904.4483), for quantum combs, link
   composition, and realization by memory channels.
4. Felix A. Pollock et al., [“Non-Markovian quantum processes: complete
   framework and efficient
   characterisation”](https://arxiv.org/abs/1512.00589), for the operational
   finite multi-time process target.
5. Felix A. Pollock et al., [“Operational Markov condition for quantum
   processes”](https://arxiv.org/abs/1801.09811), for causal-break
   Markovianity and operational memory.
6. John S. Bell, [“On the Einstein--Podolsky--Rosen
   paradox”](https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195), for the
   local-factorization obstruction.
7. Wojciech H. Zurek, [“Decoherence, einselection, and the quantum origins of
   the classical”](https://arxiv.org/abs/quant-ph/0105127), for the standard
   system--apparatus--environment record framework.
8. Giulio Chiribella, Giacomo M. D'Ariano, and Paolo Perinotti,
   [“Informational derivation of quantum
   theory”](https://arxiv.org/abs/1011.6451), for purification as a structural
   rather than merely calculational principle.
9. Giulio Chiribella, Giacomo M. D'Ariano, and Paolo Perinotti,
   [“Realization schemes for quantum instruments in finite
   dimensions”](https://arxiv.org/abs/0810.3211), for continuous-outcome
   instrument dilation in finite system dimension.

These sources supply comparator theorems and conceptual constraints. The
bridges used in the result are reconstructed above at the stated scope.

## 21. Frozen construction boundary

This manuscript contains mathematics only. It has not been independently
reviewed, adjudicated, implemented, or empirically tested. It authorizes no
successor, no code, and no promoted coordinate. The next legitimate event is
a frozen result-neutral review protocol bound to these bytes.
