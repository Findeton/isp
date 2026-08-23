# ISP v17 — U-Gen U0-T3 history Markovization and physical-closure theorems

**Status:** ACTIVE AUTHOR-SIDE MATHEMATICS / NOT A PIN / NOT REVIEWED
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none
**Candidate, implementation, or target data bound:** no

This file locates exactly where a claim of ordinary-positive indivisibility
can carry physical content. It proves that finite complete transcript laws are
always Markovizable on a target-built history state, constructs their minimal
predictive quotient, and shows why neither construction supplies a physical
ontology or a native law. It then gives the correct carrier-relative placement
test and joins it to the finite reversible-positive obstruction already found
in PC5.

The results are configuration-form neutral. Finite alphabets are used for the
exact theorem and hostile controls, not as a claim that reality is discrete,
lattice-like, externally timed, or trajectory-based.

---

## 0. Executive result

The mathematical facts are:

$$
\boxed{
\text{every finite controlled transcript law}
\Longrightarrow
\text{a full-history Markov representation}
}
\tag{1}
$$

and

$$
\boxed{
\text{every finite controlled transcript law}
\Longrightarrow
\text{a minimal predictive quotient}
}
\tag{2}
$$

but both arrows use the complete law being represented. They are therefore
representation theorems, not source-completion laws.

The physical conclusion is:

$$
\boxed{
\text{indivisibility is meaningful only relative to a declared,
independently justified carrier and intervention interface.}
}
\tag{3}
$$

Arbitrary history-state dilation cannot refute a native candidate. Omission of
an independently evidenced reference or memory can invalidate its witness.
No finite experiment establishes absolute ontic completeness.

---

## 1. Finite controlled complete-process object

Fix a finite horizon $T\ge1$. At each laboratory slot $t$ let

$$
C_t
$$

be a finite licensed control alphabet and let

$$
R_t
$$

be a finite complete-record alphabet. Null results, failures, erasures, and
retained apparatus records must be explicit members when physically present.

For every open-loop control word

$$
c_{0:T-1}=(c_0,\ldots,c_{T-1}),
$$

let

$$
P_{c_{0:T-1}}(r_{0:T})
\tag{4}
$$

be a normalized ordinary-positive transcript law. Assume **prefix
causality**: for each $t$, the marginal law of $r_{0:t}$ depends only on
$c_{0:t-1}$ and not on controls placed after the cut. Write that marginal as

$$
p_t(r_{0:t}\mid c_{0:t-1}).
\tag{5}
$$

This slot order is supplied laboratory syntax. Nothing in the theorem derives
external time, a causal order for the universe, or spacetime.

Define the observed history at cut $t$ by

$$
h_t=(c_{0:t-1},r_{0:t})
\in
\mathcal H_t.
\tag{6}
$$

Only positive-support histories are used for empirical conditionals. Values
off support will be completed arbitrarily and cannot bear a scientific claim.

---

## 2. Full-history Markovization

### Theorem HM.A — finite controlled history-state representation

Every family (4) satisfying prefix causality has a controlled
ordinary-positive Markov representation whose state at cut $t$ is the full
history $H_t=h_t$.

For $p_t(h_t)>0$, define

$$
k_t(r_{t+1}\mid h_t,c_t)
=
\frac{
p_{t+1}(r_{0:t+1}\mid c_{0:t})
}{
p_t(r_{0:t}\mid c_{0:t-1})
}.
\tag{7}
$$

For zero-support $h_t$, choose any normalized distribution on $R_{t+1}$.
Define the state transition kernel

$$
K_t(h'\mid h_t,c_t)
=
\begin{cases}
k_t(r_{t+1}\mid h_t,c_t),
&h'=(h_t,c_t,r_{t+1}),\\
0,&\text{otherwise}.
\end{cases}
\tag{8}
$$

With initial law $p_0(r_0)$, the product of these kernels reproduces (4)
exactly on every transcript.

### Proof

Prefix causality makes the numerator in (7) well defined without reference to
later controls. Normalization follows by summing the numerator over
$r_{t+1}$ and recovering its denominator. Equation (8) is therefore a
stochastic kernel. Along an on-support transcript, multiplication gives

$$
p_0(r_0)
\prod_{t=0}^{T-1}
\frac{p_{t+1}(r_{0:t+1}\mid c_{0:t})}
     {p_t(r_{0:t}\mid c_{0:t-1})}
=
p_T(r_{0:T}\mid c_{0:T-1})
\tag{9}
$$

by telescoping. A zero-support prefix cannot later acquire positive
probability, so the arbitrary off-support completion is empirically idle.
$\square$

### Corollary HM.A1 — adaptive policies

If $c_t$ is chosen by a deterministic or stochastic policy depending only on
$h_t$, append the policy kernel before $K_t$. The joint control--record law is
again Markov on $H_t$ and reproduces the adaptive transcript distribution.

### Corollary HM.A2 — no absolute finite-law non-Markovizability

No finite controlled transcript law can prove that *every mathematically
possible* enlarged positive state representation is non-Markovian. The full
history is always one such representation.

This corollary does not say that the observed past is a present physical
configuration, that nature stores it, or that a Barandes minimalist law
selects this complete realizer.

---

## 3. Predictive equivalence and the smallest exact predictor

The history state retains more than prediction may need. Fix a cut $t$ and
let $\Pi_{t:}$ be the licensed set of future adaptive control policies. For
positive-support histories $h,h'\in\mathcal H_t$, define

$$
h\sim_t h'
\quad\Longleftrightarrow\quad
P(r_{t+1:T}\mid h,\pi)
=
P(r_{t+1:T}\mid h',\pi)
\quad
\text{for every }\pi\in\Pi_{t:}.
\tag{10}
$$

Let

$$
S_t=[H_t]_{\sim_t}
\tag{11}
$$

be the predictive class.

### Theorem HM.B — future sufficiency and descended dynamics

$S_t$ is sufficient for every licensed future transcript law. Moreover, the
history-state transition descends to a controlled Markov kernel on
$S_t$.

### Proof

Future sufficiency is the definition of (10). If $h\sim_t h'$, choose a
future policy whose first action is any fixed $c_t$ and whose later actions
are arbitrary. Equality of all future laws implies equality of the joint law
of the next record and every later continuation. Hence it also implies
equality of the distribution of

$$
(r_{t+1},[H_{t+1}]_{\sim_{t+1}})
$$

given $h,c_t$ and $h',c_t$. The transition therefore depends only on the
class $S_t$, not on its representative. $\square$

### Theorem HM.C — deterministic minimality

Let

$$
Z_t=f_t(H_t)
\tag{12}
$$

be any deterministic statistic sufficient for every licensed future policy.
Then there is a unique function $g_t$ on the attained values of $Z_t$ such
that

$$
S_t=g_t(Z_t).
\tag{13}
$$

Consequently,

$$
|\mathsf{im}(S_t)|
\le
|\mathsf{im}(Z_t)|.
\tag{14}
$$

### Proof

If $f_t(h)=f_t(h')$, sufficiency of $Z_t$ says that every licensed future law
is equal after $h$ and $h'$. Thus $h\sim_t h'$. Mapping an attained statistic
value to that common equivalence class is well defined and unique, proving
(13)--(14). $\square$

The theorem is finite and controlled. It does not import stationarity,
ergodicity, a bi-infinite sequence, or a physical time variable.

---

## 4. The answer-import proposition

### Proposition HM.D — predictive-state construction has zero source credit

The maps

$$
P\longmapsto\{K_t^{\rm hist}\}
\quad\text{and}\quad
P\longmapsto\{S_t,K_t^S\}
\tag{15}
$$

are functions **of the complete process law $P$**. Therefore they cannot, by
themselves, explain or predict $P$ from a weaker target-independent source
packet.

### Proof

The history kernels use the conditional ratios of $P$ in (7). The equivalence
relation (10) compares all future conditionals of $P$, and its descended
kernels use those same conditionals. Evaluating either construction therefore
requires the target law or information sufficient to recover it before the
putative generator acts. Under U0-T2, that is an equivalent-input compiler,
not a native derivation. $\square$

Minimality changes the storage cost of a supplied answer; it does not reverse
the dependency arrow.

This proposition does not ban learning. If a fixed algorithm sees only a
licensed calibration subset, freezes before target opening, and predicts
held-out processes, the prediction is genuine at that transfer scope. The
learned state still does not become physical ontology by minimality alone, and
the algorithm's inductive bias, training information, refits, and resource
costs remain inputs to the U0 ledger.

### Corollary HM.D1 — predictive ontology is underselected

Even after $S_t$ is constructed, the same transcript law admits arbitrarily
many empirically equivalent enlargements

$$
(S_t,J_t),
\tag{16}
$$

where $J_t$ evolves independently and is unread. The transcript law alone
therefore does not select either the minimal predictor or an enlarged state as
what physically exists.

---

## 4.1 Exact parity control

Let $R_0,R_1,R_2\in\{0,1\}$ and assign probability $1/4$ to each transcript
satisfying

$$
R_0\oplus R_1\oplus R_2=0,
$$

and zero otherwise. Every pairwise marginal is uniform, but

$$
R_2=R_0\oplus R_1
$$

with certainty. The latest record $R_1$ is not future sufficient. The full
history $(R_0,R_1)$ is, and its minimal predictive quotient at that cut is the
two-valued statistic

$$
S_1=R_0\oplus R_1.
$$

This is a useful exact control because the compression is real while its
physical interpretation is not selected. One obtains $S_1$ only by knowing
the three-record law. Calling this parity bit a hidden physical memory would
therefore reverse the U0 dependency arrow unless an independent preparation,
reader, intervention, or transfer experiment identifies it.

---

## 5. Physical closure and licensed division

Let $C_t$ now denote a candidate's proposed physical boundary carrier, not a
laboratory control alphabet.

### Definition HM.1 — source closure

$C_t$ is **source-closed at experimental scope $\mathcal E$** only if every
independently evidenced constituent, reference, retained record, memory
channel, and communication port capable of affecting registered futures is
included, or its influence is excluded by a preregistered isolation/erasure
control.

### Definition HM.2 — predictive sufficiency

$C_t$ is **future sufficient at $\mathcal E$** when, for all licensed future
policies,

$$
P(F\mid C_t,h_t,\pi)=P(F\mid C_t,\pi)
\tag{17}
$$

for every registered future event $F$ and positive-support past $h_t$.

### Definition HM.3 — licensed physical division

A cut is a licensed physical division at scope $\mathcal E$ only when the
carrier is source-closed, future sufficient, readable/repreparable to the
claimed resolution, and stable under the licensed future grammar.

This is deliberately stronger than algebraic factorization through a formal
label and weaker than a claim of ultimate ontic completeness.

### Theorem HM.E — placement alternatives

At a tested cut, the evidence supports only the following classification.

1. **Closed division.** If $C_t$ is source-closed and future sufficient, the
   complete law factors through a licensed physical restart on $C_t$ at the
   declared scope.
2. **Evidenced enlargement.** If $C_t$ is not future sufficient and an
   independently identified reference or memory $M_t$ carries the residual
   dependence, the joint carrier $(C_t,M_t)$ must be tested. The original
   witness was subsystem memory, not yet native indivisibility of the closed
   experiment.
3. **Interface nondivision.** If $C_t$ fails future sufficiency and no
   independently warranted enlargement is known, the result is nondivision
   on the tested interface. It is not a proof that no hidden dilation exists.
4. **Native-candidate indivisibility.** Promotion to a native-law claim also
   requires that the candidate derive its carrier/interface from a
   target-independent source rule, use one fixed law across held-out
   processes, pass U0-T2, and show nonfactorization for every licensed positive
   restart without omitting declared physical state.

### Proof

Items 1--3 follow directly from Definitions HM.1--HM.3 and conditional
independence. Item 4 adds the provenance conditions needed to distinguish a
physical hypothesis from the universal history-state construction of HM.A or
the target-built quotient of HM.B. None of the items quantifies over every
logically possible ontology, so no absolute completeness claim follows.
$\square$

---

## 6. Exact omitted-memory control

Let a physical memory/reference bit $M$ be uniformly random. At the first
registered read, set

$$
X_0=M.
\tag{18}
$$

At the middle cut, perform a complete system causal break and prepare
$X_1=0$. At the final read, let the physical memory set

$$
X_2=M.
\tag{19}
$$

Then

$$
P(X_2=X_0\mid\operatorname{do}(X_1=0))=1.
\tag{20}
$$

The system-only carrier is operationally non-Markovian: the future depends on
the past across the break. The joint carrier $(X,M)$ has an ordinary positive
memoryless realization. If $M$ is independently physically evidenced, calling
the system-only witness fundamental indivisibility is wrong.

This control does not imply that every observed nondivision has a physical
memory bit. HM.A can always invent a mathematical history memory; HM.E demands
independent physical warrant.

---

## 7. Exact interference-nondivision control

Let

$$
H=\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix},
\qquad
B=|H|^{\odot2}
=\frac12
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}.
\tag{21}
$$

Then

$$
|H^2|^{\odot2}=I,
\qquad
B^2=B\ne I.
\tag{22}
$$

Thus the proposed intermediate two-value configuration does not supply the
positive restart needed to compose the two transformations. Yet the closed
unitary comparator contains no external environment memory, and a genuine
middle causal break removes the earlier coherent continuation.

This separates two questions:

1. can an unrecorded configuration seam be divided by an ordinary-positive
   restart; and
2. does an external memory carry detectable past information across an
   intervention?

Neither answer implies the other without a matched carrier and interface.
The matrix is a quantum comparator, not a native U0 input.

---

## 8. Finite reversible-positive boundary

### Theorem HM.F — stochastic inverse implies permutation

Let $K$ and $L$ be $m\times m$ column-stochastic matrices with

$$
LK=I_m.
\tag{23}
$$

Then $K$ and $L$ are inverse permutation matrices.

### Proof

Write $e_j$ for the $j$th point distribution. Since

$$
LKe_j=e_j,
\tag{24}
$$

the extreme point $e_j$ is a convex combination, with weights given by the
$j$th column of $K$, of columns of $L$. Every column of $L$ receiving positive
weight must therefore equal $e_j$.

Hence the supports of two distinct columns of $K$ are disjoint: a shared
index would force one column of $L$ to equal two distinct point
distributions. There are $m$ nonempty pairwise disjoint supports inside an
$m$-element set, so every support is a singleton. Column normalization makes
its sole entry one. Thus $K$ is a permutation matrix, and (23) makes $L$ its
inverse. $\square$

### Corollary HM.F1 — location of reversible capacity

If a finite source-closed carrier represents every exactly reversible
physical generator by a positive kernel and represents its inverse on the
same carrier, those generators act by permutations. Nontrivial reversible
quantum-process capacity cannot reside in stochastic mixing on that carrier.

It can still reside in one or more of:

1. a continuous or otherwise infinite physical carrier;
2. independently warranted reference or memory variables;
3. transformation/preparation/measurement context;
4. a non-Markov whole-process composition law;
5. a non-positive secondary representation;
6. nonuniform advice, which earns no native credit; or
7. an empirical deviation from the quantum comparator.

This is resource displacement, not a selection of ontology. A deterministic
continuous carrier can carry arbitrarily rich structure, and a finite
indivisible law need not supply a positive inverse at every unrecorded seam.

---

## 9. Unified distinction table

| Coordinate | Exact question | What a positive answer does not prove |
|---|---|---|
| history Markovization | can the whole observed past be called a state? | that nature stores that state |
| predictive quotient | what is the smallest exact predictor derived from the complete law? | that the predictor is ontic or independently generated |
| operational Markovity | does a causal break screen all registered past influence? | positive division on every proposed configuration seam |
| stochastic division | does a positive restart exist on this declared carrier? | absence or presence of environment memory |
| source closure | were all independently evidenced carriers and ports included? | future sufficiency or ultimate ontic completeness |
| native indivisibility | does one target-independent physical law fail every licensed restart on its justified carrier? | impossibility of arbitrary mathematical dilation |
| finite positive reversibility | does a positive inverse exist on the same finite carrier? | that positivity, continuous carriers, or whole laws are impossible |

---

## 10. Hostile controls for the next native candidate

Any U0 candidate must survive at least these attacks.

1. **Full-past renaming:** call $h_t$ the fundamental configuration and hide
   that its transition kernel was computed from the target law.
2. **Predictive-state renaming:** construct $S_t$ after tomography and claim
   the minimality theorem derived it from physical premises.
3. **Reference omission:** discard a readable memory/reference, obtain
   system-only non-Markovity, and promote it to native indivisibility.
4. **Advice reference:** place target answers in a physical token and count
   its readability as explanatory grounding.
5. **Formal-slot time:** infer fundamental time or chronology from fixture
   indices.
6. **Formal-seam division:** demand factorization through every written
   intermediate symbol despite no retained future-sufficient record.
7. **Missing-division escape:** refuse factorization at a stable retained
   future-sufficient boundary.
8. **Positive-inverse overreach:** require a stochastic inverse for a
   physically irreversible or unlicensed operation.
9. **Finite-carrier overreach:** use HM.F to reject continuous, contextual, or
   indivisible positive laws outside its class.
10. **Off-support tuning:** encode predictions in arbitrary conditional values
    after impossible histories.
11. **Hidden precision:** compress the complete process into digits of one
    latent real and count one parameter.
12. **Memory laundering:** add an exponentially growing state but omit its
    predictive information and physical preparation cost.
13. **Markov/Barandes conflation:** equate operational process Markovity,
    stochastic division, CP divisibility, and minimalist-law indivisibility.
14. **Realizer selection:** choose one convenient complete Markovized realizer
    and attribute its details to a first-order law that did not select it.
15. **Nelson inheritance:** use a trajectory, Euclidean space, Brownian noise,
    external time, or phase field merely because it gives an available
    sufficient state.
16. **Quantum fallback:** conclude that Hilbert ontology is fundamental if one
    positive carrier fails.

---

## 11. Result and non-result ledger

### Exact author-side mathematics

1. every finite prefix-causal controlled transcript law has a full-history
   positive Markov representation;
2. every such law has a deterministic minimal predictive quotient relative
   to the licensed future policies;
3. both constructions consume the complete process law and therefore have no
   native source-completion credit;
4. source closure, predictive sufficiency, and ontic completeness are
   distinct;
5. omitted physical memory and interference nondivision occupy different
   coordinates; and
6. a finite stochastic kernel with a stochastic inverse is a permutation.

### Not established

This file does not establish:

1. a physical configuration domain;
2. a native indivisible stochastic law;
3. a unique complete realizer of a Barandes first-order law;
4. absolute ontic completeness;
5. a fundamental predictive or history state;
6. a group, reference, phase, clock, action, bundle, or holonomy;
7. quantum theory from stochastic principles;
8. a failure of ordinary-positive ontology;
9. QFT, locality, spacetime, or gravity; or
10. an official pin, review, paper, or scientific result.

---

## 12. Consequence for U0

The next native candidate cannot earn progress merely by supplying a
Markovian state. It must answer, before target opening:

1. what physical evidence fixes or constrains its configuration carrier;
2. which references and memory channels belong to the carrier;
3. how contingent state is prepared;
4. how interventions and readers act;
5. which boundaries are genuine divisions and why;
6. what one uniform law generates complete records at unrecorded seams;
7. how the same law transfers without refit to held-out processes; and
8. where every predictive, contextual, memory, composition, and precision
   resource is charged.

Only after those answers exist can nondivision distinguish a native physical
hypothesis from a target-built representation. This author-side result does
not open U0-T4, an implementation, a candidate pin, or a review cycle.
