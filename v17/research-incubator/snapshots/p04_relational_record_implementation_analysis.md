# Private implementation analysis: an invariant relational clock record

Status: off-tree, result-neutral, and not an authorized v17 unit

Bound base: ISP v17 commit `1e27457`

## 1. Question

The private successor investigation identified the invariant

$$
y=2\alpha-(1+q)\beta\pmod 7
$$

inside the rejected Paper 04 finite parent. This note asks a stricter question:

> Can $y$ be written into an ordinary classical pointer by a physical symmetric
> interaction, without dephasing the UCOH source or importing an external clock?

The answer separates into two levels.

1. **Global symmetric instrument:** yes, exactly.
2. **Typed sequential quantum-memory realization:** yes, exactly.
3. **Autonomously scheduled and spacetime-local apparatus:** not yet constructed.

This is progress, but not yet a physical clock.

## 2. Frozen action and invariant

On the commuting labels $(q,\alpha,\beta)$, the finite gauge action is

$$
g:(q,\alpha,\beta)
\longmapsto
(q,\alpha+(1+q)g,\beta+2g).
$$

Therefore

$$
\begin{aligned}
y'&=2[\alpha+(1+q)g]-(1+q)[\beta+2g]\\
&=2\alpha-(1+q)\beta\\
&=y.
\end{aligned}
$$

No gauge parameter, orbit representative, or fitted coefficient appears in this
cancellation. The coefficients are fixed by the frozen representation.

## 3. Exact PVM on the kinematic and physical spaces

Let

$$
E_y=
\sum_{\substack{q,\alpha,\beta:\\
2\alpha-(1+q)\beta=y}}
|q\rangle\langle q|_Q
\otimes|\alpha\rangle\langle\alpha|_A
\otimes|\beta\rangle\langle\beta|_B
\otimes I_M.
$$

Every joint basis tuple has one and only one value of $y$, so

$$
E_yE_{y'}=\delta_{yy'}E_y,
\qquad
\sum_yE_y=I.
$$

Gauge invariance gives

$$
U_gE_yU_g^\dagger=E_y,
\qquad
[E_y,P]=0,
$$

where $P=7^{-1}\sum_gU_g$ is the physical projector. Hence each $E_y$
restricts to a projection on $\mathcal H_{\rm phys}$ and the restricted PVM is
complete there.

This is a Dirac/relational observable of the finite constrained parent. It is not
the bare A or B phase observable.

## 4. Exact neutral-pointer premeasurement

Let $R_y\cong\mathbb C^7$ have orthonormal pointer states $|r\rangle$ and a
neutral gauge action. Let $X|r\rangle=|r+1\rangle$. Define

$$
V_{\rm rel}=\sum_y E_y\otimes X^y
$$

on parent plus pointer. Since the $E_y$ form a PVM, $V_{\rm rel}$ is unitary.
With the pointer initialized at $|0\rangle$,

$$
W_{\rm rel}|\psi\rangle
=V_{\rm rel}(|\psi\rangle\otimes|0\rangle)
=\sum_yE_y|\psi\rangle\otimes|y\rangle.
$$

Because every $E_y$ commutes with $U_g$,

$$
(U_g\otimes I_{R_y})W_{\rm rel}=W_{\rm rel}U_g.
$$

Thus the premeasurement is exactly symmetric and requires no transformation of
the output numeral. The corresponding instrument is

$$
\mathcal I_y(\rho)=E_y\rho E_y,
\qquad
\sum_y\operatorname{tr}\mathcal I_y(\rho)=1.
$$

Appending a classical direct-sum register after decohering the pointer in the
$|y\rangle$ basis gives an ordinary outcome packet. Unlike the rejected raw A
record, its label has one state-independent gauge law: the trivial action.

## 5. Exact UCOH nondisturbance

The two UCOH orbit components have

$$
(q,\alpha,\beta)=(0,s,2s)
$$

and

$$
(q,\alpha,\beta)=(1,2s,2s).
$$

Both satisfy $y=0$. Therefore the entire corrected UCOH state, including its
previously omitted relative phases, obeys

$$
E_0|\Psi_{\rm UCOH}\rangle=|\Psi_{\rm UCOH}\rangle,
\qquad
E_{y\ne0}|\Psi_{\rm UCOH}\rangle=0.
$$

Consequently

$$
W_{\rm rel}|\Psi_{\rm UCOH}\rangle
=|\Psi_{\rm UCOH}\rangle\otimes|0\rangle.
$$

The record is deterministic and the parent state is unchanged. This does not
violate information--disturbance: the output contains no information distinguishing
the q=0 and q=1 alternatives.

## 6. Nontrivial source discrimination

For the phase-sharp q=0 fixtures,

$$
\begin{array}{c|c|c|c}
\text{source}&\alpha&\beta&y\\
\hline
\mathrm{U0}&s&2s&0\\
\mathrm{UAO}&1+s&2s&2\\
\mathrm{UBO}&s&1+2s&-1\equiv6
\end{array}
$$

The record therefore distinguishes two independently shifted relational
preparations from the synchronized control while remaining invariant under the
common gauge orbit.

For U1, $q=1$, $\alpha=2s$, and $\beta=2s$, again giving $y=0$. For USTOP,
$q=6$ and $\alpha=0$, so $y=0$. The latter is a required non-kill: an invariant
label does not make the stopped A sector an operational clock.

UA0 and UA1 are not sharp in all three inputs of $y$ and require the full Born
distribution of the PVM. No sharp value is inferred from their abbreviated orbit
notation.

## 7. Why this does not repair Paper 04

Paper 04 froze a seven-valued standalone A record $\alpha$ and claimed that it
transformed as a classical record while q remained coherent. The new outcome $y$
has a different operational meaning and requires access to A, B, and Q jointly.

Replacing $\alpha$ by $y$ would therefore change:

- the outcome space;
- the measurement interaction;
- the apparatus inputs;
- the future reader family;
- the clock interpretation.

It is legitimate successor mathematics, not an editorial repair of the rejected
candidate.

## 8. Global interaction versus physical locality

The exact unitary can be written abstractly as

$$
V_{\rm rel}:
|q,\alpha,\beta,r\rangle
\longmapsto
|q,\alpha,\beta,r+2\alpha-(1+q)\beta\rangle.
$$

As a finite-dimensional unitary commuting with the gauge representation, it has a
symmetric Hamiltonian logarithm: choose spectral phases of $V_{\rm rel}$ and set
$H_{\rm rel}$ so that $V_{\rm rel}=e^{-iH_{\rm rel}}$; functional calculus keeps
$[H_{\rm rel},U_g\otimes I]=0$.

This proves in-principle symmetric implementability. By itself it does not prove
locality, bounded interaction complexity, or autonomous switching.

The raw reversible arithmetic suggests the formal decomposition

$$
r\leftarrow r+2\alpha,
\qquad
r\leftarrow r-\beta,
\qquad
r\leftarrow r-q\beta.
$$

The composed map is invariant. The individual partial values are not. This does not
prevent a typed quantum implementation; it prevents treating those partial values as
classical records.

### 8.1 Exact typed sequential factorization

Use one seven-state quantum memory $R$ with running value $r$. Define three
reversible controlled-addition gates:

$$
\begin{aligned}
F_1:&\quad r_1=r_0+2\alpha,\\
F_2:&\quad r_2=r_1-\beta,\\
F_3:&\quad r_3=r_2-q\beta.
\end{aligned}
$$

With $r_0=0$, the final value is $r_3=y$. The correct gauge representations of
the successive memory boundaries are

$$
\begin{array}{c|c}
\text{boundary}&\text{memory transformation}\\
\hline
R_0&r_0\mapsto r_0\\
R_1&r_1\mapsto r_1+2(1+q)g\\
R_2&r_2\mapsto r_2+2qg\\
R_3&r_3\mapsto r_3.
\end{array}
$$

The intertwiners are exact. For $F_1$,

$$
r_0+2[\alpha+(1+q)g]
=r_1+2(1+q)g.
$$

For $F_2$,

$$
[r_1+2(1+q)g]-(\beta+2g)
=r_2+2qg.
$$

For $F_3$,

$$
[r_2+2qg]-q(\beta+2g)=r_3.
$$

Thus

$$
G_{i}F_i=F_iG_{i-1}
$$

at every stage, where $G_i$ is the system gauge action together with the displayed
memory action at boundary $i$.

The intermediate $R_1$ and $R_2$ objects must carry their full quantum algebras.
Their Q-controlled transformation laws are legitimate quantum-memory actions but
not actions on a classical center. No observer may read or decohere $r_1$ or $r_2$
as a classical numeral without changing the experiment. At $R_3$ the action is
trivial, so the pointer may be classicalized in the $r_3$ basis.

This is exactly the kind of typed-boundary repair that was missing in Paper 13C's
future grammar and Paper 04's raw A record. The invariant does not need every
intermediate expression to be invariant; it needs every intermediate carrier and
arrow to have the correct type.

### 8.2 What remains physically open

The factorization supplies an itinerant quantum-memory architecture:

- $F_1$ couples A to the memory;
- $F_2$ couples B to the memory;
- $F_3$ couples Q, B, and the memory, or an equivalent further ancilla
  decomposition.

It still does not derive:

1. where these systems are located;
2. whether the required interactions are local in an independently established
   spacetime;
3. what physical controller orders $F_1,F_2,F_3$;
4. how switching is made autonomous without a background laboratory clock;
5. whether a bounded two-body symmetric decomposition exists for the frozen
   interaction resources;
6. whether the final pointer becomes stable or redundantly objective.

For a laboratory experiment, an externally scheduled sequence is legitimate and
must be declared. For a fundamental emergence claim, using that schedule as the
origin of chronology would be circular.

### 8.3 Exact time-independent laboratory controller

Time-dependent switching can be removed without changing the three gates. Introduce
a four-state quantum program register $C$ with basis $|0\rangle,\ldots,|3\rangle$.
Let

$$
U_0=I,
\qquad
U_1=F_1,
\qquad
U_2=F_2F_1,
\qquad
U_3=F_3F_2F_1,
$$

and define the controlled dressing

$$
\mathcal W=\sum_{j=0}^3|j\rangle\langle j|_C\otimes U_j.
$$

On the bare program chain use the fixed Hamiltonian

$$
H_C=
\sqrt3(|1\rangle\langle0|+|0\rangle\langle1|)
+2(|2\rangle\langle1|+|1\rangle\langle2|)
+\sqrt3(|3\rangle\langle2|+|2\rangle\langle3|).
$$

This is the spin-$3/2$ $2J_x$ matrix. It has exact perfect transfer

$$
e^{-iH_C\pi/2}|0\rangle=e^{i\varphi}|3\rangle
$$

for an irrelevant global phase $e^{i\varphi}$. The dressed, time-independent
Hamiltonian

$$
H_{\rm aut}=\mathcal W(H_C\otimes I)\mathcal W^\dagger
$$

has transition terms

$$
|j+1\rangle\langle j|_C\otimes F_{j+1}+\text{h.c.}
$$

with the same fixed couplings. Therefore

$$
e^{-iH_{\rm aut}\pi/2}
(|0\rangle_C\otimes|\psi\rangle\otimes|0\rangle_R)
=e^{i\varphi}|3\rangle_C\otimes
U_3(|\psi\rangle\otimes|0\rangle_R).
$$

At the transfer time, the program has completed the invariant-record computation
without an externally changed Hamiltonian.

The symmetry is also exact. Let $G_j(g)$ be the system-plus-memory representation
at typed boundary $j$ from Section 8.1 and define

$$
\mathcal G_g=\sum_{j=0}^3|j\rangle\langle j|_C\otimes G_j(g).
$$

Because $G_{j+1}(g)F_{j+1}=F_{j+1}G_j(g)$, every dressed hopping term commutes
with $\mathcal G_g$, and hence

$$
[H_{\rm aut},\mathcal G_g]=0.
$$

This closes the time-dependent-switching loophole for a supplied laboratory time
parameter.

### 8.4 Why autonomy is not chronology

The construction still presupposes:

- preparation of the program at endpoint $|0\rangle$;
- the Schrödinger evolution parameter used to define $e^{-iH_{\rm aut}t}$;
- knowledge or detection of the transfer condition;
- a final classicalization interaction;
- the oriented labeling of the program graph and the chosen initial boundary.

The Hamiltonian is reversible and contains the Hermitian-conjugate backward hops.
Starting at $|3\rangle$ implements the reverse computation. No thermodynamic arrow
or native causal precedence has been derived.

Accordingly, the exact conclusion is:

> The relational-record instrument can be run by one time-independent symmetric
> laboratory Hamiltonian. It cannot use that laboratory autonomy as evidence that
> time or chronology emerged from the parent.

An irreversible autonomous completion would require an open-system sink,
metastable amplification, or a larger stochastic law. Each introduces a physical
environment, low-entropy boundary condition, or directed transition structure that
must be declared and tested rather than hidden in the word `record'.

## 9. A general relational-record theorem

Let a group $G$ act unitarily by permuting a joint orthonormal basis $|x\rangle$,
and let $f:X\to Y$ be invariant:

$$
f(gx)=f(x).
$$

Then

$$
E_y=\sum_{x:f(x)=y}|x\rangle\langle x|
$$

is a $G$-invariant PVM, and the neutral-pointer isometry

$$
W_f=\sum_yE_y\otimes|y\rangle
$$

is covariant. For any two basis alternatives $x,x'$, the Lüders channel preserves
their cross term exactly if and only if $f(x)=f(x')$:

$$
\sum_yE_y|x\rangle\langle x'|E_y
=\mathbf1_{f(x)=f(x')}|x\rangle\langle x'|.
$$

Thus a relational classical record preserves precisely those coherences it does
not distinguish. This is the sharp positive counterpart of the center and
information--disturbance no-go theorems.

For non-basis actions, standard-Borel spaces, continuous groups, and POVMs, the
same idea requires measurable invariant maps, disintegration/null-class control,
and a covariant Naimark or instrument construction. Those generalizations remain
future theorem obligations.

## 10. What the record means physically

The value $y$ is an invariant synchronization/offset relation. It is not a value of
an absolute clock and not a value of either clock considered alone.

This is consistent with the operational core of relativity: clock coordinates gain
physical meaning through comparisons, coincidences, and signal protocols. But one
invariant comparison does not yet supply:

- successive happenings;
- orientation or chronology;
- a calibrated duration scale;
- a worldline or localization map;
- radar distance;
- Lorentzian signature;
- a metric;
- gravitational dynamics.

The orbit parameter $s$ remains gauge in the finite parent. A sequence cannot be
manufactured by sorting its values.

## 11. Barandes lift requirements

In a Barandes-style ontology, the Hilbert-space unitary and PVM are secondary
representations. To promote the result to a physical record one would need an
enlarged configuration space containing:

$$
(\text{parent configuration},\text{apparatus configuration},r_y),
$$

and one indivisible stochastic law for the full interaction whose final apparatus
configuration has the same $y$ probabilities.

The following must be independent outputs:

1. actual outcome $r_y$;
2. stable future readability of $r_y$;
3. whether the interaction creates a division event;
4. whether redundant readers become correlated with $r_y$;
5. whether the premeasurement coherence is only representational or has a native
   stochastic interference witness.

Hilbert-space decoherence alone cannot fill these fields.

### 11.1 Two distinct successor tiers

The result must be split before review.

**Tier L -- laboratory operational test.** Use the supplied Paper 03 causal
schedule and comparator spacetime to implement the typed gates, classicalize the
final pointer, and measure covariance, visibility, disturbance, and redundancy.
This is empirically meaningful but cannot derive time because laboratory order is
an input.

**Tier N -- native ontological lift.** Supply one configuration space and one
indivisible stochastic law for parent, travelling memory, apparatus, and final
record. Ask whether the same law produces the output statistics and an actual
stable configuration without importing the laboratory schedule as native time.

The stochastic--quantum correspondence can establish existence of stochastic
representations for suitable quantum processes, but operational equivalence does
not select one unique microscopic configuration basis or law. Therefore Tier L
cannot automatically award Tier N. Robust pointer records can constrain an
ontological proposal; they cannot by themselves choose it without a selection
theorem.

### 11.2 Minimum native-lift contract

A future native lift must bind, before seeing its result:

1. one fixed system configuration space $\mathcal C_{\rm sys}$;
2. apparatus/program/memory configuration variables, including final $y$;
3. one full indivisible law $\Gamma_{\rm full}$ shared by every registered
   preparation, intervention, eraser, and reader;
4. the operational coarse-graining from complete configurations to Paper 03
   packets;
5. the symmetry action on configurations and proof that the coarse-graining
   descends;
6. the contingent initial distribution separately from the law;
7. the whole-history probability, not separately tuned one-step kernels;
8. the actual final configuration variable;
9. stable-future and eraser subcategories;
10. an exact division test on the complete native boundary;
11. a statement of whether the external target/conditioning-time parameter remains
    fundamental or is only a laboratory comparator;
12. a nonselection ledger listing every operationally equivalent alternative lift.

It must reproduce one frozen family of complete experiments, including the
coherent eraser and future-reader controls, rather than merely the final Born
distribution. Otherwise an arbitrary classical hidden-variable sampler could be
mistaken for the indivisible law.

## 12. Minimum successor controls

1. Raw A numeral substituted for $y$.
2. Gauge representative $s$ inserted into the outcome.
3. UCOH q label leaked into an ancillary register.
4. Final $y=0$ retained while an intermediate ancilla keeps which-q information.
5. Neutral pointer asserted without checking the intertwining equation.
6. Joint PVM replaced by separate A/B measurements that dephase UCOH.
7. Global symmetric unitary called local.
8. Nonlocal joint apparatus hidden behind a circuit diagram.
9. External phase reference used to implement a noncovariant partial gate.
10. q=6 invariant output interpreted as a running A clock.
11. Deterministic UCOH output called informationally complete.
12. Sharp UAO/UBO controls used to infer sharp UA0/UA1 values.
13. Pointer decoherence called an actual Barandes configuration.
14. One invariant relation promoted to chronology.
15. Algebraic Hamiltonian logarithm claimed to be physically natural or boundedly
    local.
16. Continuous-group extension claimed from the finite proof.

## 13. Exact redundant-reader extension

Once the final invariant pointer has value $y$, it may be copied into neutral
orthogonal memory registers without copying an arbitrary quantum state. For $m$
initially blank fragments $E_1,\ldots,E_m$, define

$$
C_m:
|y\rangle_R|0\rangle_{E_1}\cdots|0\rangle_{E_m}
\longmapsto
|y\rangle_R|y\rangle_{E_1}\cdots|y\rangle_{E_m}.
$$

This map extends to a unitary by modular controlled additions. Because every
register is gauge neutral and the control value is invariant, $C_m$ is symmetric.
It broadcasts only the commuting classical label $y$, so it does not violate
no-cloning or no-broadcasting.

After the relational premeasurement and copying, the global coherent state is

$$
\sum_{y,y'}E_y\rho E_{y'}
\otimes|y\rangle\langle y'|_R
\otimes\bigotimes_{k=1}^m|y\rangle\langle y'|_{E_k}.
$$

Unitary copying alone has not selected an outcome. If an inaccessible fragment is
traced out, or if an explicit pointer dephasing channel $\Delta_y$ is applied, the
accessible state becomes

$$
\rho_{\rm br}
=\sum_yE_y\rho E_y
\otimes|y\rangle\langle y|_R
\otimes\bigotimes_{k=1}^m|y\rangle\langle y|_{E_k}.
$$

Every fragment contains the same perfectly distinguishable classical label. This
is an exact broadcast record for the coarse-grained relational observable. It is
stronger than a diagonal reduced state and stronger than a mutual-information
plateau: independent readers can measure their fragments in the registered basis,
agree with probability one, and leave the other fragments unchanged.

For UCOH, $E_0\rho E_0=\rho$, so the extension writes only zero and does not disturb
the parent state. For a superposition of distinct $y$ sectors, the accessible
classical record removes precisely the cross-$y$ coherences, as required by the
information--disturbance theorem.

### 13.1 Stability category

Let $Z_y$ denote the joint record-sector projector on pointer and fragments. Define
the licensed stable-future class by channels $\Phi$ satisfying

$$
\Phi^\dagger(Z_y)=Z_y
$$

for every $y$, together with complete exposure of any future-readable memory. This
class is closed under composition and tensoring with record-neutral spectators.
Every licensed future preserves perfect readability of $y$.

An eraser must be a separately typed process outside this class. A reversible
eraser can reset the visible pointer only by exporting $y$ to another memory; a
genuine many-to-one effective erasure requires discarding or coarse-graining that
memory. Thus the eraser control must distinguish:

- visible reset;
- recoverable hidden record;
- operational erasure relative to a declared reader family;
- ontological destruction, if that notion is admitted at all.

### 13.2 Stable and objective do not mean complete division

Even when $y$ is perfectly stable and redundantly objective, the conditional state
inside $E_y\mathcal H$ may retain information relevant to later outcomes. Two
histories with the same $y$ can therefore have different lawful futures. The record
is a complete division only if the enlarged stochastic law proves exact future
sufficiency given the complete boundary, not merely the pointer value.

The coordinates remain separate:

$$
\text{stable record}
\not\Rightarrow
\text{objective record}
\not\Rightarrow
\text{complete division}
\not\Rightarrow
\text{actuality}.
$$

The first implication can fail when only one durable copy exists. The second fails
when hidden system/controller memory affects the future. The third fails in a pure
Hilbert description because a broadcast mixture still does not specify which
configuration actually obtains.

## 14. Empirical discriminator

The successor can compare two instruments on the same coherent source.

### Arm R -- invariant relational record

Measure $y$ and verify:

- deterministic UCOH value;
- retained interference visibility;
- nonidentity covariance;
- discrimination of shifted relational controls.

### Arm A -- raw sector-sensitive reading

Attempt to record the frame-dependent A reading with enough information to
distinguish the two rate sectors. Measure:

- record distinguishability;
- loss of UCOH interference visibility;
- symmetry/reference resource cost;
- record redundancy and entropy production.

The direct comparison tests the prediction:

> Coherence is protected by relational degeneracy, not by a general exemption from
> measurement disturbance.

This is empirically meaningful without invoking gravity.

## 15. Disposition

The invariant relational record is mathematically real and exactly compatible with
the rejected parent's surviving finite constrained structure. It is the strongest
positive successor seed found so far.

The next scientific gate is not another coordinate transformation. It is:

> Can the invariant joint measurement be realized by a fully typed, symmetry-
> respecting physical apparatus with no hidden reference, and can its final pointer
> become a stable or objective record under a single enlarged law?

Until that is frozen, reviewed, and constructed, the correct status is:

```text
RELATIONAL-INVARIANT-PVM-CONSTRUCTED-OFFTREE
SYMMETRIC-GLOBAL-PREMEASUREMENT-CONSTRUCTED-OFFTREE
TYPED-SEQUENTIAL-QUANTUM-MEMORY-CONSTRUCTED-OFFTREE
TIME-INDEPENDENT-SYMMETRIC-LAB-CONTROLLER-CONSTRUCTED-OFFTREE
SPACETIME-LOCAL-APPARATUS-UNCONSTRUCTED
BACKGROUND-FREE-AUTONOMOUS-CHRONOLOGY-UNCONSTRUCTED
EXACT-REDUNDANT-OPERATIONAL-RECORD-CONSTRUCTED-OFFTREE
BARANDES-CONFIGURATION-LIFT-UNCONSTRUCTED
CHRONOLOGY-NONE
GRAVITY-NONE
```
