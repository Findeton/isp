# Entropy Structure of Indivisible Stochastic Processes

*Gauge Invariance, Coherence, and Thermodynamic Interpretation*

Author: Felix Robles Elvira

Department of Physics & Department of Philosophy, Harvard University

Date: Preprint · March 2026

Companion to arXiv:2302.10778, 2309.03085, 2507.21192

## Abstract

Abstract.

Barandes' indivisible stochastic process framework reconstructs quantum dynamics from
first-order transition probabilities, but it leaves open which information-theoretic
quantities are fixed at the $\Gamma$ level and which require additional lift or dilation
data. We address that question. Our main results are:
(i)

*Gauge invariance*

— the Shannon entropy $S[p(t)]$ of the configuration distribution
is invariant under Schur–Hadamard gauge transformations of the time-evolution operator,
whereas the von Neumann entropy $S_\mathrm{vN}[\rho(t)]$ is not determined by the transition
matrix $\Gamma$ alone; this underdetermination reflects the coarse-grained character of the
$\Gamma$-based description, not the non-physicality of $S_\mathrm{vN}$;
(ii)

*Entropy–coherence identity*

— the entropy gap $S[p] - S_\mathrm{vN}[\rho]$
equals the relative entropy of coherence $C(\rho)$;
(iii)

*Non-monotone entropy*

— $S[p(t)]$ need not be monotone for indivisible
processes: qubit Rabi oscillations and a three-site tight-binding chain already furnish
explicit entropy-decrease phases, so the bare ISP formalism does not support an
$H$-theorem for coherent closed dynamics;
(iv)

*Pseudo-stochastic intermediate maps*

— negativity of inverse or intermediate
transition matrices is best interpreted as a witness of failed classical stochastic
factorization or reversal, not by itself as a thermodynamic second law.
These results sharpen the boundary between what is fixed by classical transition data alone
and what requires a finer quantum-amplitude description.
The companion paper [13] develops gauge-invariant process entanglement measures and worked
examples, including Bell-state preparation and full Bell-test circuits.
We close by outlining what additional ingredients — boundary conditions, decoherence,
subsystem structure, and a gauge-invariant notion of work — would be needed to promote the
present kinematic results into a genuine thermodynamic theory.

## Introduction

Barandes [1–3] has proposed that every quantum system can be understood
as an *indivisible stochastic process* on a classical configuration space, establishing
a precise mathematical correspondence between transition probabilities and quantum-mechanical
amplitudes. The framework is remarkable in recovering interference, entanglement, decoherence,
and the Born rule from stochastic foundations, without treating the Hilbert space, wave function,
or unitary group as primitive objects.

Yet the three foundational papers say little about which entropy notions are fixed by the
$\Gamma$-level description and which require additional amplitude or dilation structure.
This is the gap we address. Our aim is not to derive a full thermodynamic second law from
ISP dynamics alone, but to separate what is already determined by first-order transition
data from what becomes visible only after a lift $\Theta$ or a dilation is chosen.

The central question is therefore: *which entropy is fixed by an indivisible stochastic
process at the $\Gamma$ level?* There are two natural candidates. The *Shannon entropy*
$$S[p(t)] = -\sum_i p_i(t)\ln p_i(t)$$
is defined on the classical configuration distribution, the observable object in the
framework. The *von Neumann entropy*
$$S_\mathrm{vN}[\rho(t)] = -\mathrm{Tr}\bigl[\rho(t)\ln\rho(t)\bigr]$$
is defined on the auxiliary density matrix introduced by the stochastic–quantum correspondence.
We show that $S[p]$ is gauge-invariant while $S_\mathrm{vN}[\rho]$ is not uniquely determined
by $\Gamma$, making the former the natural entropy of the $\Gamma$-level/coarse-grained
description.

The paper is organized as follows.
Section II reviews the indivisible stochastic process framework.
Section III establishes the non-monotonicity of $S[p(t)]$.
Section IV proves the gauge invariance theorem and the entropy–coherence identity.
Section V summarizes gauge-invariant process entanglement results from the companion
paper [13], including the distinction between terminal-basis
phantoms and full-circuit Bell correlations.
Section VI discusses the thermodynamic interpretation, with particular attention to
the limits imposed by gauge scope and subsystem closure.
Section VII gives a conjectural discussion of work extraction and states explicitly
what remains unproved.
Section VIII collects open questions.

## Indivisible Stochastic Processes

### Definitions

We follow the notation of [1]. Let $\mathcal{C} = \{1,\ldots,N\}$ be a finite configuration space.

**Definition 1**

(Stochastic process).

A

*stochastic process*

on $\mathcal{C}$ is a family of $N\times N$ real matrices
$\{\Gamma(t\leftarrow t_0)\}_{t,t_0}$ with non-negative entries satisfying column normalization
$\sum_i \Gamma_{ij}(t\leftarrow t_0) = 1$ for all $j$. The configuration distribution at time
$t$ satisfies
$$p(t) = \Gamma(t\leftarrow t_0)\,p(t_0).$$

**Definition 2**

(Indivisibility [1]).

A stochastic process $\Gamma(t\leftarrow t_0)$ is

*indivisible*

if for every
intermediate time $t_0

<

t'

<

t$ there exists

*no*

genuine stochastic matrix
$\widetilde\Gamma(t\leftarrow t')$ such that
$$\Gamma(t\leftarrow t_0) = \widetilde\Gamma(t\leftarrow t')\,\Gamma(t'\leftarrow t_0).$$
Equivalently, the algebraic "intermediate" matrix $\widetilde\Gamma = \Gamma(t\leftarrow t_0)
[\Gamma(t'\leftarrow t_0)]^{-1}$ has at least one negative entry for some $(t,t',t_0)$.
We call such $\widetilde\Gamma$

*pseudo-stochastic*

.

**Definition 3**

(Stochastic–quantum correspondence [1,2]).

Every stochastic process arising from quantum dynamics is associated with a complex
$N\times N$

*time-evolution operator*

$\Theta(t\leftarrow t_0)$ via
$$\Gamma_{ij}(t\leftarrow t_0) = |\Theta_{ij}(t\leftarrow t_0)|^2.$$
The corresponding density matrix for initial distribution $p(t_0)$ is
$$\rho(t) = \Theta(t\leftarrow t_0)\!\left[\sum_j p_j(t_0)\,P_j\right]\Theta^\dagger(t\leftarrow t_0),$$
where $P_j = |j\rangle\langle j|$ are configuration projectors. One verifies
$p_i(t) = \mathrm{Tr}[P_i\,\rho(t)]$.

### Gauge freedom

The decomposition $\Gamma_{ij} = |\Theta_{ij}|^2$ is not unique. Any element-wise phase
rotation

$$\Theta'_{ij}(t) = e^{i\phi_{ij}(t)}\,\Theta_{ij}(t), \qquad \phi_{ij}\in\mathbb{R},$$

leaves $\Gamma_{ij}$ invariant because $|\Theta'_{ij}|^2 = |\Theta_{ij}|^2$.
This *Schur–Hadamard gauge freedom* [1] is a novel symmetry
without a classical analogue: it modifies the density matrix $\rho$ without affecting
any observable transition probability.

Different gauge choices yield different density matrices but the same
$\Gamma$-level transition data for a specified time-evolution operator.
This observation is the key to understanding which entropy is fixed at that level of
description.

*Scope of the gauge freedom.*
Barandes presents the Schur–Hadamard freedom broadly: once a time-evolution operator
$\Theta(t\leftarrow t_0)$ has been specified, any entry-wise rephasing
$\Theta' = e^{i\phi}\odot\Theta$ yields the same transition matrix
$\Gamma = |\Theta|^2$ and therefore the same $\Gamma$-level physics.
In that sense the gauge acts at the level of the chosen operator itself,
not merely for one especially restricted class of terminal examples.

This is a statement about $\Gamma$-level lift freedom, not an assertion that every
entry-wise rephasing is again the same closed-system unitary Hamiltonian evolution.
Arbitrary Schur–Hadamard rephasings preserve the transition probabilities, but they
need not preserve ordinary matrix unitarity, a chosen Hamiltonian factorization, or a
particular circuit realization. Whenever $S_\mathrm{vN}$ or coherence is discussed
below, those quantities are therefore attached to a chosen lift or chosen enlarged
physical realization, while $S[p]$ is the quantity fixed by $\Gamma$ alone.

Additional restrictions appear only after one adds structure that is *not* contained
in $\Gamma$ alone. If a laboratory procedure is modeled as sequential operations with amplitudes
$\Theta_1, \Theta_2, \Theta_3$, the composed evolution is
$\Theta_\mathrm{total} = \Theta_3\Theta_2\Theta_1$ (ordinary matrix product).
A Schur–Hadamard rephasing of the already-composed operator $\Theta_\mathrm{total}$ is a genuine
$\Gamma_\mathrm{total}$-level gauge transformation. By contrast, independently rephasing an
internal factor, such as $\Theta_2 \to e^{i\phi_{ij}}\odot\Theta_2$ while
holding $\Theta_1, \Theta_3$ fixed, generally changes $\Theta_\mathrm{total}$,
hence changes $\Gamma_\mathrm{total}$ and observable probabilities.
The same distinction arises for chosen dilations or subsystem decompositions:
the broad $\Gamma$-level gauge freedom remains, but not every rephasing of auxiliary
ingredients is a symmetry of the enlarged construction.

$t_0$

$t'$

$t$

$\Gamma(t\leftarrow t_0)$ — valid stochastic ($\Gamma_{ij}\geq 0$)

$\Gamma(t'\leftarrow t_0)$

$\widetilde\Gamma(t\leftarrow t')$ — pseudo-stochastic!

**Figure 0.**
Schematic of indivisibility. The full transition $\Gamma(t\leftarrow t_0)$ is a valid
stochastic matrix (non-negative entries), but any intermediate factorization
$\Gamma(t\leftarrow t_0) = \widetilde\Gamma(t\leftarrow t')\Gamma(t'\leftarrow t_0)$
forces $\widetilde\Gamma$ to have negative entries for some $t'$.

## Non-Monotone Shannon Entropy

### Failure of the classical H-theorem

For classical divisible dynamics, monotone entropic quantities are usually relative
entropies to a stationary distribution; in the special unital/bistochastic case this
reduces to monotonicity of the Shannon entropy itself. All such arguments use genuine
stochastic propagation between intermediate times. ISP evolution lacks that structure,
so one should expect entropy oscillations rather than a general $H$-theorem for $S[p(t)]$
in coherent closed examples.

**Theorem 1**

(Explicit failure of monotonicity).

There exist indivisible stochastic processes generated by non-trivial Hamiltonians,
initial distributions $p(t_0)$, and times $t_0

<

t_1

<

t_2$ such that
$S[p(t_2)]

<

S[p(t_1)]$.
In particular, the ISP framework does not support a general $H$-theorem for
$S[p(t)]$ in coherent closed dynamics.

Proof.

We exhibit an explicit family. For $N=2$ with $\Theta(t) = e^{-i\omega t\sigma_x/2}$
and mixed initial distribution $p(t_0) = (1-\varepsilon, \varepsilon)$, the configuration
probabilities are
$$p_0(t) = (1-\varepsilon)\cos^2\!\tfrac{\omega t}{2} + \varepsilon\sin^2\!\tfrac{\omega t}{2},
\quad p_1(t) = 1-p_0(t).$$
Since $p(t+T) = p(t)$ with $T = 2\pi/\omega$, the entropy $S[p(t)] = -p_0\ln p_0 - p_1\ln p_1$
is periodic. For $\varepsilon \neq \tfrac{1}{2}$ and $\omega\neq 0$, $S$ achieves its maximum
at $t = \pi/(2\omega)$ (where $p_0 = p_1 = \tfrac{1}{2}$) and returns to its initial
value at $t = \pi/\omega$. Hence $S$ decreases on $[\pi/(2\omega), \pi/\omega]$.
The process is indivisible on those intervals because the intermediate matrix
$\widetilde\Gamma_{01} = [p_0(t) - p_0(t')]/[1 - 2p_0(t')]$ goes negative whenever
$p_0(t)

<

p_0(t')$, which holds precisely during the entropy-decreasing phase.

$\square$

The entropy decrease is not, by itself, a violation of the second law. It is the familiar
behavior of reversible coherent dynamics, rewritten at the level of configuration
probabilities. The contribution of Theorem 1 is therefore structural: within the ISP
framework, non-monotonicity is tied to the failure of intermediate stochastic
factorization. Any thermodynamic arrow requires extra physical input — decoherence,
coarse-graining, or effective openness — not merely indivisibility.

**Remark 1**

(Scope of non-monotonicity).

Theorem 1 should not be read as saying that every classical divisible process has
monotone Shannon entropy. That is false in general: for non-unital Markov dynamics
the monotone quantity is typically a relative entropy to the stationary distribution,
not $S[p]$ itself. The point here is narrower. In the ISP setting, a decrease of the
configuration-basis Shannon entropy during coherent closed evolution is compatible with
time-reversal symmetry and is naturally accompanied by failure of intermediate
stochastic factorization. For the qubit example, $\widetilde\Gamma$ has a negative entry
exactly on the entropy-decreasing intervals. In higher dimensions, pseudo-stochasticity
is a useful witness of non-divisibility, but its relation to the sign of $\dot S$
depends on the state and on the chosen entropy functional.

### Example: qubit Rabi oscillations

For $N=2$, $\Theta(t) = e^{-i\omega t\sigma_x/2}$, initial distribution
$p(t_0) = (1-\varepsilon, \varepsilon)$, one computes:

$$S[p(t)] = -p_0(t)\ln p_0(t) - p_1(t)\ln p_1(t), \qquad
S_\mathrm{vN}[\rho(t)] = -(1-\varepsilon)\ln(1-\varepsilon) - \varepsilon\ln\varepsilon = \mathrm{const}.$$

The von Neumann entropy is constant because unitary evolution preserves eigenvalues of $\rho$.
The Shannon entropy oscillates strictly above $S_\mathrm{vN}$ except at integer multiples of
$\pi/\omega$ where $\rho(t)$ is diagonal and the two coincide.
By Corollary 1, $S[p(t)] - S_\mathrm{vN} = C(\rho(t))$, so in this example every decrease of
$S[p(t)]$ is mirrored by a decrease of the configuration-basis coherence $C(\rho)$ for the
chosen lift, with $S_\mathrm{vN}$ remaining fixed. The oscillation is therefore best read as
a redistribution between classical uncertainty (measured by $S[p]$) and basis-dependent
coherence, not as entropy production or dissipation.

$\varepsilon$:

0.100

Figure 1.
Qubit Rabi oscillations. Blue: Shannon entropy $S[p(t)]$ (nats).
Red (dashed): von Neumann entropy $S_\mathrm{vN}[\rho(t)]$ = constant.
Green: entropy gap $C(\rho(t)) = S[p(t)]-S_\mathrm{vN}[\rho(t)]$ (relative entropy of coherence).
The entropy-decrease phase ($\pi/2 < \omega t/\pi < 1$, $3\pi/2 < \omega t/\pi < 2$, …)
corresponds exactly to the indivisible interval where $\widetilde\Gamma_{01} < 0$.
Adjust $\varepsilon$ (initial minority population) to explore different regimes.
At $\varepsilon = 0.5$ the system is already maximally mixed and $S[p]$ is constant.

### Example: three-site tight-binding chain

Consider $N=3$ with Hamiltonian
$H = (|1\rangle\langle 2| + |2\rangle\langle 3| + \mathrm{h.c.})/\sqrt{2}$
(tridiagonal, nearest-neighbour hopping). Its eigenvalues are $E = -1, 0, +1$ and the
corresponding eigenvectors are
$$|{-}1\rangle = \tfrac{1}{2}(1,-\sqrt{2},1)^\top,\quad
|0\rangle = \tfrac{1}{\sqrt{2}}(1,0,-1)^\top,\quad
|{+}1\rangle = \tfrac{1}{2}(1,\sqrt{2},1)^\top.$$
Starting from a pure configuration $p(0) = (1,0,0)$, the time-dependent occupation
probabilities are

$$p_1(t) = \tfrac{1}{4}(1+\cos t)^2, \quad
p_2(t) = \tfrac{1}{2}\sin^2\!t, \quad
p_3(t) = \tfrac{1}{4}(1-\cos t)^2.$$

The Shannon entropy rises from $0$ to a maximum of $\tfrac{3}{2}\ln 2$ nats at
$t_\star = \pi/2$ and returns to $0$ at $t = \pi$, where all
probability has transferred to site 3.

Figure 2.
Three-site tight-binding chain starting from site 1 ($p(0)=(1,0,0)$).
Solid blue: Shannon entropy $S[p(t)]$.
Dashed lines: individual occupation probabilities $p_1, p_2, p_3$.
The entropy peaks midway through the transfer and is exactly symmetric, reflecting
the time-reversal symmetry of the Hamiltonian. The falling half of each arch
($t > \pi/2$) is the non-monotone entropy-decreasing phase.

### Entropy rate and the unital classical limit

Beyond the existence of entropy-decreasing phases, one can give a precise local criterion
for *when* $\dot S[p]$ changes sign.
Define the *time-local generator* $K(t)$ of the process by
$$\dot{p}(t) = K(t)\,p(t), \qquad K(t) := \dot\Gamma(t\leftarrow t_0)\,[\Gamma(t\leftarrow t_0)]^{-1},$$
which exists whenever $\Gamma(t\leftarrow t_0)$ is invertible.
Since $\mathbf{1}^T\Gamma = \mathbf{1}^T$ holds at all times, differentiating gives
$\mathbf{1}^T K(t) = 0$: the columns of $K(t)$ sum to zero.
For a divisible (Markovian) process the incremental map $I + \epsilon K(t)$ is a valid
stochastic matrix for small $\epsilon > 0$, which forces $K_{ij}(t) \geq 0$ for $i\neq j$.
For an *indivisible* process, $K_{ij}(t)$ can become negative — this is the
infinitesimal counterpart of pseudo-stochasticity:
$$\widetilde\Gamma(t+\epsilon\leftarrow t) = I + \epsilon K(t) + O(\epsilon^2),$$
so $K_{ij}(t) < 0$ for some $i\neq j$ is exactly the condition that this infinitesimal
intermediate transition matrix is pseudo-stochastic.

**Proposition 2**

(Entropy-rate formula).

The rate of change of the Shannon entropy satisfies
$$\dot S[p(t)] = \sum_{i \neq j} K_{ij}(t)\,p_j(t)\,\ln\frac{p_j(t)}{p_i(t)}.$$
In particular:
(i)

*Unital divisible limit*

— if $K_{ij}(t)\geq 0$ for all $i\neq j$ and the
incremental maps $I+\epsilon K(t)$ are bistochastic (equivalently, the uniform distribution
is stationary), then $\dot S[p(t)] \geq 0$.
(ii)

*Indivisible case*

— if $K_{ij}(t)

<

0$ for some $i\neq j$, entropy decrease
$\dot S

<

0$ becomes possible for suitable $p(t)$.

Proof.

$\dot S = -\sum_i \dot p_i \ln p_i = -\sum_{i,j} K_{ij} p_j \ln p_i$.
Using $K_{ii} = -\sum_{j\neq i} K_{ji}$ and collecting terms:
$\dot S = \sum_{i\neq j} K_{ij} p_j (\ln p_j - \ln p_i) = \sum_{i\neq j} K_{ij} p_j \ln(p_j/p_i)$.
For part (i): when $I+\epsilon K$ is bistochastic, Shannon entropy cannot decrease under the
infinitesimal step $p\mapsto (I+\epsilon K)p$; dividing by $\epsilon$ and taking
$\epsilon\to0^+$ gives $\dot S \geq 0$.

$\square$

### Explicit generator: qubit Rabi oscillator

For the qubit Rabi oscillator of Section III.2, the transition matrix is doubly stochastic
with $g(t):=\Gamma_{00}(t)=\Gamma_{11}(t)=\cos^2\!\tfrac{\omega t}{2}$ and
$\Gamma_{01}(t)=\Gamma_{10}(t)=1-g(t)$.
A direct computation gives

$$K(t) = \dot\Gamma(t)\Gamma(t)^{-1}
= \frac{\dot g(t)}{2g(t)-1}\begin{pmatrix}1 & -1 \\ -1 & 1\end{pmatrix},
\qquad K_{01}(t) = -\frac{\dot g(t)}{2g(t)-1}.$$

Substituting $\dot g(t) = -\frac{\omega}{2}\sin\omega t$ and
$2g(t)-1 = \cos\omega t$ yields the remarkably clean formula

$$K_{01}(t) = \frac{\omega}{2}\tan\omega t,$$

which is *independent of the initial condition $\varepsilon$*.
Inserting into Proposition 2:
$$\dot S[p(t)] = K_{01}(t)\,(p_1 - p_0)\ln\frac{p_1}{p_0},$$
where $(p_1 - p_0)\ln(p_1/p_0) \geq 0$ always (zero only when $p_0 = p_1$).
Therefore
$$\operatorname{sgn}\bigl(\dot S[p(t)]\bigr) = \operatorname{sgn}\bigl(K_{01}(t)\bigr)
= \operatorname{sgn}\bigl(\tan\omega t\bigr).$$
Entropy increases precisely when $0 < \omega t \bmod 2\pi < \pi/2$ or
$\pi < \omega t \bmod 2\pi < 3\pi/2$, and decreases in the complementary intervals
— exactly the phases identified in Theorem 1.
The sign of the single off-diagonal generator entry $K_{01}$ is a complete, computable
criterion for the direction of entropy flow at every instant.
The pole at $\omega t = \pi/2 + n\pi$ (where $p_0 = p_1 = \tfrac{1}{2}$) reflects the
singularity of $\Gamma^{-1}$ when $\Gamma$ becomes the maximally mixed uniform matrix.

## Gauge Invariance and Entropy at the $\Gamma$ Level

**Theorem 2**

(Gauge invariance of $S[p]$, gauge dependence of $S_\mathrm{vN}$).

(a) The Shannon entropy $S[p(t)]$ is invariant under every Schur–Hadamard gauge
transformation $\Theta_{ij}\mapsto e^{i\phi_{ij}}\Theta_{ij}$.

(b) The von Neumann entropy $S_\mathrm{vN}[\rho(t)]$ is gauge-dependent for generic
mixed initial distributions: there exist $\phi_{ij}$ such that
$S_\mathrm{vN}[\rho'(t)] \neq S_\mathrm{vN}[\rho(t)]$.

**Proof of (a).**

Under the gauge, $|\Theta'_{ij}|^2 = |e^{i\phi_{ij}}\Theta_{ij}|^2 = |\Theta_{ij}|^2$,
so $\Gamma'_{ij} = \Gamma_{ij}$, hence $p'(t) = p(t)$, hence $S[p'(t)] = S[p(t)]$.

$\square$

**Proof of (b).**

The density matrix transforms as
$$\rho'(t)_{kl} = \sum_j p_j(t_0)\,e^{i(\phi_{kj}-\phi_{lj})}\Theta_{kj}\Theta^*_{lj}.$$
Diagonal entries ($k=l$) are unchanged: $\rho'_{kk} = \rho_{kk} = p_k(t)$. Off-diagonal entries
acquire relative phases $e^{i(\phi_{kj}-\phi_{lj})}$ and thus the off-diagonal

*magnitude*

$|\rho'_{kl}|$ changes for generic $\phi$. Since the eigenvalues of the Hermitian matrix $\rho$
depend on its off-diagonal elements, $S_\mathrm{vN}[\rho']\neq S_\mathrm{vN}[\rho]$ in general.
We give an explicit counterexample in Sec. IV.2.

$\square$

Theorem 2 establishes that the Gibbs–Shannon entropy $S[p]$ is determined directly by the
transition probabilities $\Gamma$, whereas $S_\mathrm{vN}$ is not. Among the two candidate
entropies considered in this paper, $S[p]$ is therefore the natural entropy of the
$\Gamma$-level description.
The von Neumann entropy $S_\mathrm{vN}[\rho]$, while experimentally measurable via quantum
state tomography, requires specifying a $\Theta$ lifting $\Gamma$ and is therefore
representation-dependent within this description (see Section IV.3 for the full discussion).

### The entropy–coherence identity

**Proposition 1**

(Entropy–coherence identity).

For any density matrix $\rho$ with diagonal $p_i = \rho_{ii}$,
$$S[p] - S_\mathrm{vN}[\rho] = C(\rho) \geq 0,$$
where $C(\rho) = S[\rho_\mathrm{diag}] - S_\mathrm{vN}[\rho]$ is the relative entropy
of coherence [

4

] and $\rho_\mathrm{diag}$ is $\rho$ with all off-diagonal entries set to zero.

Proof.

$\rho_\mathrm{diag}$ is diagonal with eigenvalues $p_i = \rho_{ii}$, so
$S_\mathrm{vN}[\rho_\mathrm{diag}] = -\sum_i p_i\ln p_i = S[p]$.
Therefore $S[p] - S_\mathrm{vN}[\rho] = S_\mathrm{vN}[\rho_\mathrm{diag}] - S_\mathrm{vN}[\rho] = C(\rho)$.
Non-negativity $C(\rho)\geq 0$ follows from the data-processing inequality for the
completely-positive dephasing map $\mathcal{D}: \rho\mapsto\rho_\mathrm{diag}$,
which can only increase entropy.

$\square$

**Corollary 1**

(Entropy decomposition for a chosen lift).

For any chosen lift whose diagonal distribution is $p(t)$, the $\Gamma$-level entropy admits the decomposition
$$S[p(t)] = S_\mathrm{vN}[\rho(t)] + C(\rho(t)),$$
where both terms on the right depend on the chosen lift, but their sum is fixed by $\Gamma$.
In particular, any gauge transformation that increases $S_\mathrm{vN}$ must decrease $C$
by the same amount, and vice versa.

**Proposition 3**

(Pure-state gauge invariance).

If the initial distribution is concentrated on a single configuration, $p_j(t_0) = \delta_{jk}$,
then for all $t$ and every gauge choice:
(i) $S_\mathrm{vN}[\rho(t)] = 0$ — the density matrix remains pure;
(ii) $C(\rho(t)) = S[p(t)]$ — the entire Shannon entropy is coherence;
(iii) $S_\mathrm{vN}$ is trivially gauge-invariant (identically zero).
Consequently, the gauge-dependence of $S_\mathrm{vN}$ established in Theorem 2(b) is
exclusively a

*mixed-state phenomenon*

: it requires a mixed initial distribution
$p(t_0)$ with support on at least two configurations.

Proof.

For $p_j(t_0) = \delta_{jk}$, the density matrix is
$\rho(t) = \Theta(t)|k\rangle\langle k|\Theta^\dagger(t)$, a rank-one projector.
Its eigenvalues are $\{1,0,\ldots,0\}$ for every lifting $\Theta$ of $\Gamma$, giving
$S_\mathrm{vN}[\rho(t)] = 0$ independent of gauge.
Part (ii) follows from Proposition 1: $C(\rho) = S[p] - S_\mathrm{vN}[\rho] = S[p]$.
For part (iii): under the Schur–Hadamard gauge $\Theta_{ij}\to e^{i\phi_{ij}}\Theta_{ij}$,
$\rho'(t)_{lm} = e^{i(\phi_{lk}-\phi_{mk})}\rho_{lm}(t)$, so $|\rho'_{lm}| = |\rho_{lm}|$.
Since the eigenvalues of a rank-one projector are $\{1,0,\ldots,0\}$ regardless, $S_\mathrm{vN}$
is unchanged.

$\square$

This is a strong constraint. It says the gauge freedom acts as a "transfer" between coherence
and von Neumann entropy, leaving the $\Gamma$-level entropy $S[p]$ unchanged. From a resource-theory
perspective [4], the total resource is fixed by the gauge-invariant quantity $S[p]$;
what changes under gauge is how that resource is partitioned into coherence vs. mixed-state
entropy. For pure initial states, all of $S[p]$ is coherence and there is no ambiguity.

### Explicit gauge example: qubit at $\omega t = \pi/2$

Take $N=2$, initial distribution $p(t_0) = (0.7, 0.3)$ (a mixed state), and evaluate at
$\omega t = \pi/2$ where $\Theta = \frac{1}{\sqrt{2}}\bigl(\begin{smallmatrix}1&-i\\-i&1\end{smallmatrix}\bigr)$.
The configuration distribution at this time is $p = (0.5, 0.5)$, so $S[p] = \ln 2 \approx 0.693$ nats,
independent of gauge.

Under the Schur–Hadamard gauge with $\phi_{01} = \phi$, $\phi_{00}=\phi_{10}=\phi_{11}=0$,
the off-diagonal element of the density matrix becomes
$\rho_{01}(\phi) = \tfrac{i}{2}(0.7 - 0.3e^{i\phi}),$
giving $|\rho_{01}|^2 = \tfrac{1}{4}(0.58 - 0.42\cos\phi).$
The eigenvalues are $\lambda_\pm = \tfrac{1}{2}\pm\tfrac{1}{2}\sqrt{0.58-0.42\cos\phi}$,
yielding $S_\mathrm{vN}(\phi) = -\lambda_+\ln\lambda_+ - \lambda_-\ln\lambda_-$.
At $\phi=0$: $\lambda_\pm = 0.7, 0.3$ and $S_\mathrm{vN} \approx 0.611$ nats.
At $\phi=\pi$: $\lambda_\pm = 1, 0$ and $S_\mathrm{vN} = 0$.
The gauge parameter continuously interpolates between these values while $S[p] = \ln 2$ throughout.

Figure 3.
Gauge dependence of entropy for the qubit at $\omega t = \pi/2$, initial distribution
$(0.7, 0.3)$. Blue (flat): gauge-invariant Shannon entropy $S[p] = \ln 2$.
Red (dashed): von Neumann entropy $S_\mathrm{vN}(\phi)$ — continuously variable from
$0.611$ nats (at $\phi=0$) to $0$ (at $\phi=\pi$), corresponding to a transition from
a mixed to a pure density matrix. Green: coherence $C(\rho)=S[p]-S_\mathrm{vN}$.
The gauge transformation acts as a "transfer" between $S_\mathrm{vN}$ and $C$, leaving
their sum fixed.

### Representational completeness and the physical status of $S_\mathrm{vN}$

The results of Sections IV.1–IV.2 establish that $S[p]$ is directly determined by the
transition matrix $\Gamma$, while $S_\mathrm{vN}[\rho]$ and $C(\rho)$ are
individually sensitive to the choice of lifting $\Theta$ with $|\Theta_{ij}|^2 = \Gamma_{ij}$.
Before proceeding, we address a tension this raises about the scope of the ISP framework.

*The completeness question.*
The ISP framework [1–3] assigns physical reality to the
transition probabilities $\Gamma_{ij}$ and treats $\Theta$ as an auxiliary device for
computing them.
Under this view, any two $\Theta$, $\Theta'$ with $|\Theta_{ij}|^2 = |\Theta'_{ij}|^2$
describe the same physical process.
Two observations developed in this paper are in tension with a strict completeness claim:

1. *Composability and extra structure (Section II.2).* At the level of a specified
  time-evolution operator, all Schur–Hadamard-related lifts encode the same $\Gamma$
  and are gauge-equivalent. But when a laboratory process is modeled with a particular
  circuit factorization or dilation, independent rephasings of internal factors generally
  change the composed operator and the observable $\Gamma_\mathrm{total}$.
  This means that once one enriches the description beyond bare transition data,
  phase information in the chosen embedding can become physically relevant.
2. *Operational measurability of $S_\mathrm{vN}$.* The von Neumann entropy is
  experimentally measurable via quantum state tomography.
  Its gauge dependence within the ISP framework means the $\Gamma$-based description
  cannot assign it a unique value: two lifts $\Theta$, $\Theta'$ of the same $\Gamma$
  give different density matrices and different $S_\mathrm{vN}$ values.
  This is a representational limitation of the $\Gamma$-level description,
  not evidence that $S_\mathrm{vN}$ is unphysical.

*Our position.*
We adopt the following interpretation, consistent with all results proved here.
The ISP framework, by working with $\Gamma = |\Theta|^2$, performs a well-defined
*coarse-graining*: it retains transition probabilities and discards the phases of
$\Theta$.
The broad gauge symmetry concerns what is fixed at that $\Gamma$ level;
composability tells us how additional phase data can re-enter once one asks for
a specific embedding into a larger experiment or dilation.
Within this coarse-grained description:

- $S[p]$ is directly determined by $\Gamma$ (Theorem 2).
- $S_\mathrm{vN}[\rho]$ and $C(\rho)$ are individually underdetermined — their values
  depend on which $\Theta$ lifts $\Gamma$, making them *representation-dependent* rather than gauge-invariant in the $\Gamma$-based sense.
  They are not fictitious: $S_\mathrm{vN}$ is measurable.
  The $\Gamma$-based description simply lacks the resolution to predict it uniquely.
- The identity $S[p] = S_\mathrm{vN}[\rho] + C(\rho)$ holds for every lift,
  with the sum fixed by $\Gamma$ and the individual terms depending on the lift.
  Gauge freedom acts as a transfer between $S_\mathrm{vN}$ and $C$ that leaves
  their sum — the physically determined quantity — invariant.

This has a clean practical implication: the ISP framework identifies precisely which
information-theoretic quantities are determined by classical process data alone
($S[p]$, $I(A:B)$, and the process entanglement measure $E_\mathrm{cl}$ of the
companion paper [13]) and which require the full quantum-amplitude
description ($S_\mathrm{vN}$, $C(\rho)$, quantum entanglement entropy).
The latter are not asserted to be fictitious — they lie beyond the resolution of the
coarse-grained $\Gamma$-level description.

**Remark 2**

(Scope of Theorem 2).

Theorem 2 is sometimes read as asserting that the von Neumann entropy is
"not a physical observable."
This reading is too strong.
The precise statement is: within the ISP framework's $\Gamma$-based description,
$S_\mathrm{vN}[\rho]$ has no unique representative — different lifts $\Theta$,
$\Theta'$ of the same $\Gamma$ produce different values of $S_\mathrm{vN}$.
This does not negate the broad Schur–Hadamard gauge invariance of a specified
time-evolution operator.
It says instead that once one goes beyond bare $\Gamma$ data by fixing a particular
circuit factorization, Hamiltonian realization, or dilation, additional phase information
may become physically relevant.
The broad $\Gamma$-level gauge freedom and the physical significance of extra embedding
data are compatible claims.

## Process Entanglement

The bipartite extension of the entropy framework — including a gauge-invariant process
entanglement measure, its relation to Bell inequality violations, and the
active-basis-measurement composability analysis — is developed in full in the companion
paper [13].
We summarize the key results for completeness.

A *process entanglement measure* $E_\mathrm{cl}(A:B)[\Gamma_{AB}]$ is defined as the
column-averaged KL divergence of the joint transition law from the nearest product law
$\Gamma_A \otimes \Gamma_B$.
It has a closed form (Theorem 4 of [13]), is non-negative and
gauge-invariant by construction, and the companion paper gives partial evidence for
monotonicity under local stochastic operations.

Applied to the standard two-qubit gates:

- *XX gate* $U_\mathrm{XX}(\theta)$: $E_\mathrm{cl} = H_b(\sin^2(\theta/2))$,
  agreeing with $S_\mathrm{vN}[\rho_A]$ and $I(A:B)$ for all computational-basis inputs.
- *ZZ gate* $U_\mathrm{ZZ}(\varphi)$: $\Gamma_\mathrm{ZZ} = I_{4\times 4}$, so
  $E_\mathrm{cl} = 0$. The nonzero $S_\mathrm{vN}[\rho_A^{(+)}] = H_b(\sin^2(\varphi/2))$
  for superposition input is chosen-lift/circuit dependent and is not fixed by the
  isolated terminal Z-basis transition kernel.
- *Full Bell-test circuit* $(H\otimes H)\cdot ZZ(\varphi)\cdot(H\otimes H) = XX(\varphi)$:
  $E_\mathrm{cl} = H_b(\sin^2(\varphi/2)) > 0$.
  The ISP framework correctly recovers Bell correlations when physical basis-rotation
  Hamiltonians are included as active operations in the full circuit.
- *CNOT gate* : $E_\mathrm{cl} = \ln 2$.
  Bell-state preparation from $|00\rangle$ gives $E_\mathrm{cl}(A:B;\,p_{00}=1) = \ln 2$,
  recovering the standard von Neumann entanglement entropy without invoking density matrices.

The CHSH Bell inequality is fully compatible with the ISP framework:
each measurement setting $(x,y)$ corresponds to a distinct physical circuit
$\Gamma_\mathrm{total}^{(xy)}$ with non-factorizable joint transition law
($E_\mathrm{cl} > 0$), yielding the same joint probabilities $p(ab|xy)$ as the quantum
Born rule.
The set $\{p(ab|xy)\}$ lies outside the local polytope for $\varphi \neq 0,\pi$,
reproducing the Bell violation.
Non-factorizability of $\Gamma_\mathrm{total}^{(xy)}$ — measured by $E_\mathrm{cl}$ — is
the ISP-language expression of Bell nonlocality.

## Thermodynamic Interpretation and Limits

### Dilation, open systems, and entropy bookkeeping

By the dilation theorem [2], every indivisible stochastic process on
$\mathcal{C}$ can be embedded as a subsystem of a *unistochastic* process on an enlarged
configuration space $\mathcal{C}_\mathrm{tot} = \mathcal{C}\times\mathcal{C}_\mathrm{aux}$ with
a unitary lift $\Theta_\mathrm{tot}$. For any chosen dilation, the joint classical
distribution obeys the exact identity

$$S[p(t)] = S[p_\mathrm{tot}(t)] - S[p_\mathrm{aux}(t)] + I(\mathrm{sys}:\mathrm{aux})(t),$$

where $I(\mathrm{sys}:\mathrm{aux}) = S[p] + S[p_\mathrm{aux}] - S[p_\mathrm{tot}] \geq 0$
is the mutual information between system and auxiliary degrees of freedom. This relation is
useful as bookkeeping: changes in the subsystem entropy can be traded against changes in
auxiliary entropy and system–auxiliary correlations. It provides a natural language for
discussing information backflow.

Two cautions are essential. First, Barandes' theorem paper emphasizes that subsystem
marginals do *not* generically inherit a closed ISP law. Thus the dilation picture is an
interpretive aid, not by itself a closed thermodynamic dynamics for the subsystem.
Second, no general monotonicity statement for the Shannon entropy of the dilated
configuration distribution follows from unistochasticity alone: coherent closed dynamics can
produce oscillatory configuration-basis entropies at both the subsystem and dilated levels.
Accordingly, the identity above should be read as a decomposition of entropy bookkeeping,
not as a standalone derivation of an $H$-theorem.
Third, the ISP formalism does not by itself furnish an objective mechanism of decoherence
or a thermodynamic arrow.
Still, invoking decoherence does not mean abandoning ISP.
In Barandes' picture one may treat the closed subject-plus-environment composite within the
same stochastic-quantum framework, typically by a larger unistochastic evolution, while the
observed subsystem acquires approximate division events as correlations are continually
exported into a large environment.
At the reduced level the operative physics is then standard open-system decoherence expressed
in ISP language: microscopic indivisibility may survive in principle at the composite level
even when it becomes operationally hidden in subsystem thermodynamics.

With those caveats, the auxiliary sector still offers a useful intuition. When $S[p(t)]$
decreases, one natural interpretation is that previously established system–auxiliary
correlations are being unwound or redirected. This is closely analogous to non-Markovian
information backflow, but turning that intuition into a thermodynamic theorem requires
additional assumptions about coarse-graining, decoherence, and control protocols.

### Pseudo-stochastic inverse maps and obstruction to stochastic reversal

**Theorem 3**

(Pseudo-stochastic inverse maps).

Let $\Gamma \in \mathbb{R}^{N\times N}$ be a column-stochastic matrix that is invertible
but not a permutation matrix. Then $\Gamma^{-1}$ has at least one negative entry and is
therefore pseudo-stochastic.

Proof.

First observe that $\Gamma^{-1}$ automatically inherits the column-sum-one property of $\Gamma$:
since $\mathbf{1}^T\Gamma = \mathbf{1}^T$, we have $\mathbf{1}^T = \mathbf{1}^T\Gamma\Gamma^{-1} = \mathbf{1}^T\Gamma^{-1}$.
Now suppose for contradiction that $M := \Gamma^{-1}$ is a genuine stochastic matrix with
$M_{ij}\geq 0$ and $\sum_i M_{ij}=1$. Then $\Gamma M = I$ implies
$(\Gamma M)_{ii} = \sum_k \Gamma_{ik}M_{ki} = 1$ and $(\Gamma M)_{ij} = 0$ for $i\neq j$.
Summing over $i$: $\sum_i\sum_k\Gamma_{ik}M_{ki}=N$.
But since $\Gamma$ is column-stochastic and $M$ is column-stochastic, every column of
$\Gamma M$ has entries summing to 1 via $\sum_i(\Gamma M)_{ij} = \sum_i\sum_k\Gamma_{ik}M_{kj}
= \sum_k M_{kj} = 1$.
For $\Gamma M = I$ to hold, all off-diagonal entries of a matrix with unit column sums must be
zero — forcing each column to be a standard basis vector.
Hence $\Gamma M$ is the identity only if $M$ and $\Gamma$ are both permutation matrices.
This contradicts the assumption that $\Gamma$ is not a permutation matrix.

$\square$

**Remark 3**

(Birkhoff intuition in the doubly stochastic case).

For doubly stochastic examples — in particular, many unistochastic ones — the conclusion is
consistent with Birkhoff's theorem: if both $\Gamma$ and $\Gamma^{-1}$ were doubly
stochastic, the identity $\Gamma\Gamma^{-1}=I$ would force both matrices to be
permutations. Theorem 3 itself is more elementary and does not require double
stochasticity; its content is simply that a nonnegative column-stochastic matrix with a
nonnegative inverse must be a permutation. Its value here is interpretive:
if $\Gamma^{-1}$ contains negative entries, the reverse map cannot be realized as an
autonomous classical stochastic transition law on the same configuration space. This is a
kinematic witness of failed stochastic reversibility, not by itself a thermodynamic second law.

**Remark 4**

(Physical interpretation).

For a

*forward*

indivisible process, $\Gamma(t\leftarrow t_0)$ is a valid stochastic
matrix by construction. Theorem 3 says that the

*reverse*

transition
$\Gamma^{-1}(t\leftarrow t_0) = \Gamma(t_0\leftarrow t)$ is pseudo-stochastic whenever
$\Gamma$ is not a permutation. The negative entries should therefore be read as an
obstruction to describing the reverse evolution as an ordinary stochastic process with the
same state space and observables. Whether that obstruction becomes physical irreversibility
depends on additional ingredients — bath coupling, coarse-graining, preparation constraints,
and the admissible control operations.

### Arrow of time from boundary conditions and decoherence

The indivisible stochastic framework is time-symmetric: $\Gamma(t\leftarrow t_0)$ is
defined for both $t > t_0$ and $t < t_0$, and the laws do not single out a preferred
time direction. Theorem 1 shows that $S[p]$ can oscillate. A macroscopic arrow of time
therefore cannot be obtained from indivisibility alone.

**Conjecture 1**

(Route to an effective thermodynamic arrow).

For an indivisible process prepared in a low-entropy initial state and coupled to an
environment that decoheres recurrences on a timescale $\tau_D$, the

*coarse-grained,
experimentally accessible*

entropy should exhibit an extended initial rise with strongly
suppressed revivals.

This conjecture isolates the extra ingredients that lie beyond the bare ISP kinematics.
*Ingredient 1 (low-entropy boundary condition):* a Past-Hypothesis-type preparation
makes an initial entropy increase typical.
*Ingredient 2 (decoherence and coarse-graining):* environmental coupling suppresses
the phase information required for coherent revivals and can generate approximate division
events for the observed subsystem.
*Ingredient 3 (effective subsystem closure):* one must identify observables and
control operations for which a reduced thermodynamic description is meaningful.
Only after these additions does it become reasonable to speak of a thermodynamic arrow.
Theorem 3 then supplies, at most, a witness that exact microscopic reversal is not
representable as an autonomous stochastic map at the chosen coarse-graining level.
Conjecture 1 should therefore be read as a route by which familiar low-entropy and
decoherence assumptions can be imported into the ISP setting, not as a derivation of the
arrow of time from ISP kinematics alone.
Invoking decoherence here is not a retreat to a different framework:
the closed subject-plus-environment evolution may still be described within ISP,
while the coarse-grained subsystem appears approximately divisible because environmental
correlations continually wash out the phase relations needed for revivals.

## Conjectural Work Extraction

One can formally define a nonequilibrium free-energy-like quantity using the
gauge-invariant entropy:
$$F(t) = U(t) - T\,S[p(t)], \qquad U(t) = \sum_i E_i\,p_i(t),$$
where $E_i$ are the configuration energies and $T$ the temperature of a heat bath.
Without an explicit control protocol this is only a bookkeeping device. A decrease in
$S[p(t)]$ at fixed energies suggests an increase in nonequilibrium free energy; it does
*not* by itself prove that work can be extracted operationally.

**Conjecture 2**

(Work extraction bound).

The maximum additional work extractable from a protocol that exploits an indivisible
entropy-decrease phase, relative to a classical Markovian benchmark with the same
instantaneous marginals, is
$$W_\mathrm{extra} \leq T\,\Delta S_\mathrm{decrease},$$
where $\Delta S_\mathrm{decrease} = S[p(t_\mathrm{max})] - S[p(t_\mathrm{min})]$ is the
total entropy decrease over one indivisible cycle. This conjecture is motivated by extending the known result for
non-Markovian processes [

6

] to the maximally non-Markovian (indivisible) case.

**Remark 5**

(Status of Conjecture 2).

The bound $W_\mathrm{extra} \leq T\Delta S_\mathrm{decrease}$ is motivated by
the Landauer analogy and the result of [

6

] for non-Markovian (but divisible)
processes, but it remains unproved for the indivisible case.
A rigorous proof would require: (i) a precise definition of "work" and "heat" for an
agent coupling to an indivisible process mid-cycle, consistent with the gauge-invariant
entropy $S[p]$; (ii) an explicit measurement-and-feedback protocol on the combined
system-plus-agent degrees of freedom, including the back-action of intervention on the
subsequent ISP law $\Gamma$ rather than treating the pre-intervention law as fixed;
(iii) a fluctuation-theorem-level analysis of the work statistics; and
(iv) verification that the bound is tight (i.e.\ achievable, not merely an upper bound).
The Landauer analogy provides suggestive evidence but not a proof.
We flag this as a central open thermodynamic question raised by this work.

For the qubit Rabi oscillator at $\varepsilon \to 0$:
$\Delta S_\mathrm{decrease} = \ln 2 - 0 = \ln 2$ nats per cycle,
giving the benchmark scale $W_\mathrm{extra} \leq T\ln 2 \approx 0.693\,k_BT$ per cycle
*if* Conjecture 2 is correct and *if* a suitable mid-cycle protocol can be
implemented. At present this should be read only as an order-of-magnitude guide, not as an
established bound.

A further caveat concerns coherence. In the unitary examples of Section III, the identity
$S[p(t)] = S_\mathrm{vN}[\rho(t)] + C(\rho(t))$ implies that decreases of $S[p(t)]$ are
accompanied by decreases of the configuration-basis coherence $C(\rho)$ for a chosen lift.
This makes it tempting to interpret coherence as the resource consumed by intervention
during the entropy-decrease phase. But that interpretation remains lift-dependent and
protocol-dependent. To turn it into a theorem one would need an explicit
measurement-and-feedback model showing how much work can be extracted, how the intervention
changes the subsequent ISP law, and why the result is gauge-invariant. Until then,
"coherence as thermodynamic fuel" should be read as heuristic shorthand rather than an
established consequence.
In particular, a mid-cycle intervention cannot be treated as a passive readout of a
pre-existing entropy drop: it will generally modify the subsequent transition law and may
destroy the very coherence responsible for the entropy-decrease interval it attempts to
exploit. Absent a self-consistent controller model, Conjecture 2 remains a formal analogy,
not an operational bound.

## Discussion and Open Questions

We have identified the Shannon entropy $S[p]$ as the entropy naturally determined by the
$\Gamma$-level description of an indivisible stochastic process, established by its gauge
invariance (Theorem 2).
The von Neumann entropy $S_\mathrm{vN}[\rho]$ and the relative entropy of coherence
$C(\rho)$ are individually representation-dependent within the $\Gamma$-based description,
though their sum is gauge-invariant. The natural entropy of the $\Gamma$-level description
is $S[p]$; this is consistent with the Gibbs–Boltzmann formulation of classical
statistical mechanics ($-\sum p_i\ln p_i$) arising as the appropriate entropy when
only transition probabilities — not quantum amplitudes — are treated as fundamental.
This is not a retroactive justification of Gibbs but rather an identification of the
coarse-graining level at which $S[p]$ is the natural entropy functional;
$S_\mathrm{vN}$ remains the correct entropy when the full quantum state $\rho$ is
accessible (e.g., via state tomography or energy-basis measurements).

The non-monotone entropy of Theorem 1 and the pseudo-stochastic inverse-map criterion of
Theorem 3 do *not* by themselves provide a complete stochastic-process-language
derivation of the second law. What they show is more limited and, in some ways, more
precise: bare ISP dynamics allows coherent entropy oscillations, while pseudo-stochasticity
marks the failure of intermediate or reversed evolution to be represented by ordinary
stochastic maps on the same coarse-grained state space. To obtain a macroscopic arrow one
must add boundary conditions, decoherence, and a justified reduced-system thermodynamic
description. Those additions need not abandon ISP at the closed-system level:
they can be modeled by enlarging to a system-plus-environment process and then asking when
the observed subsystem acquires approximate division events and suppressed revivals.
In that sense the present framework still translates the thermodynamic-arrow
problem into ISP language more than it solves it.

Several important questions remain open:

1. *Gauge scope and composability.* How should one distinguish the broad Schur–Hadamard gauge equivalence of a specified
  $\Gamma$-level time-evolution operator from the narrower invariances that survive
  after choosing a particular circuit decomposition or dilation? A definitive answer
  would sharpen the distinction between genuine gauge redundancy and phase data that
  become physically relevant only after extra structure is imposed.
2. *Subsystem closure in dilations.* Barandes' theorem shows that subsystem marginals do not generically define closed
  ISP laws. What additional assumptions make a reduced thermodynamic description
  controlled rather than merely heuristic?
3. *Variational characterization and two-formulation equivalence.* Conjecture 3 of the companion paper [ 13 ] proposes
  $E_\mathrm{cl}(A:B)[\Gamma_{AB}]
  = \sup_{p_A\otimes p_B}I(A:B)[\Gamma_{AB}(p_A\otimes p_B)]$.
  If true, it would simultaneously identify the gate-level measure as the entanglement
  capacity and link the two complementary formulations of $E_\mathrm{cl}$ of
  [ 13 ]. Proving or disproving this for general $N_A, N_B$ is an open
  problem. Does the alternating minimization algorithm of [ 13 ]
  always converge to the global minimum?
4. *Fluctuation theorems.* The Jarzynski equality $\langle e^{-\beta W}\rangle = e^{-\beta\Delta F}$ and
  Crooks fluctuation theorem rely on controlled thermodynamic protocols. Their
  generalisation to indivisible processes requires a stochastic-process-language
  definition of "work" and "heat" consistent with the gauge-invariant entropy $S[p]$.
5. *Kolmogorov–Sinai entropy rate.* For a continuous-time indivisible process, does the limit
  $\lim_{\tau\to 0} S[p(t+\tau) | p(t)] / \tau$ exist? Does it relate to Lyapunov
  exponents as in classical chaos?
6. *Signed entropy and quantum advantage.* The pseudo-stochastic intermediate matrix $\widetilde\Gamma$ has negative entries
  analogous to Wigner function negativity. Is there a signed entropy functional
  $S_\mathrm{signed}[\widetilde\Gamma]$ that serves as a resource measure for
  quantum computational advantage in the same way that Wigner negativity does?
7. *Thermodynamic limit and indivisibility.* Does indivisibility survive in the $N\to\infty$ (thermodynamic) limit, or does
  coarse-graining restore an effective Markovian description? The answer determines
  whether macroscopic thermodynamics can directly observe indivisible entropy oscillations.

## Conclusions

We have initiated the study of entropy within Barandes' indivisible stochastic process
framework. The central results are:

1. The Shannon entropy $S[p(t)]$ is determined directly by the transition
  matrix $\Gamma$ and is the natural entropy of the $\Gamma$-level description.
2. The von Neumann entropy $S_\mathrm{vN}[\rho]$ is representation-dependent: it requires
  specifying a lifting $\Theta$ of $\Gamma$ and is therefore not uniquely determined by
  classical process data. It is physically measurable (via state tomography) but lies beyond
  the resolution of the $\Gamma$-based coarse-graining (Section IV.3).
  The identity $S[p]-S_\mathrm{vN}[\rho] = C(\rho)$ holds for every lifting, with the
  sum gauge-invariant and the individual terms representation-dependent.
  The relevant gauge freedom is genuine at the level of a specified $\Gamma$-associated
  operator, while extra phase data become physically relevant only after one fixes a
  particular circuit embedding or dilation.
3. $S[p(t)]$ need not be monotone for indivisible processes;
  the bare ISP formalism does not furnish an $H$-theorem for coherent closed dynamics.
  Indivisibility is the structural condition behind the failure of intermediate
  stochastic factorization, and pseudo-stochastic intermediate maps provide a useful
  witness of that failure.
4. Negativity of inverse or intermediate transition matrices is best understood as a
  computable obstruction to classical stochastic factorization or reversal at the chosen
  coarse-graining level. It is a kinematic statement, not by itself a thermodynamic law.
5. A macroscopic arrow of time requires additional ingredients — low-entropy boundary
  conditions, decoherence, coarse-graining, and effective subsystem closure — and remains
  conjectural in the ISP setting. Invoking decoherence need not abandon ISP at the
  composite-system level; rather, it typically means that a larger closed
  system-plus-environment process is described within the same framework while the
  observed subsystem acquires approximate division events and suppressed revivals.
  At present the framework reformulates that problem
  more than it resolves it.
6. The gauge-invariant process entanglement measure $E_\mathrm{cl}(A:B)$ and its
  Bell-test compatibility are developed in the companion paper [ 13 ].
  The key conceptual lesson is that full circuits, not isolated terminal-basis kernels,
  carry the relevant nonlocal process structure.
7. Any work-extraction interpretation is presently conjectural. The coherence identity
  suggests a resource-theoretic reading of entropy-decrease phases, but a rigorous
  statement requires an explicit protocol, a gauge-invariant definition of work, and a
  back-action-consistent model of how intervention changes the subsequent ISP law.

These results sharpen the entropy bookkeeping of the stochastic–quantum correspondence and
delineate the limits of the $\Gamma$-level description. The framework already supports
precise statements about gauge invariance, coherence, and process-level correlation
structure; by contrast, irreversibility, thermodynamic arrows, and work extraction still
require additional physical input beyond bare ISP kinematics.

## References

1. [1] J. A. Barandes, "The Stochastic-Quantum Correspondence,"
  arXiv:2302.10778 (2023);
  *Brit. J. Phil. Sci.* (2025).
2. [2] J. A. Barandes, "The Stochastic-Quantum Theorem,"
  arXiv:2309.03085 (2023).
3. [3] J. A. Barandes, "Quantum Systems as Indivisible Stochastic Processes,"
  arXiv:2507.21192 (2025).
4. [4] T. Baumgratz, M. Cramer, and M. B. Plenio,
  "Quantifying Coherence,"
  *Phys. Rev. Lett.* **113**, 140401 (2014).
5. [5] S. M. Carroll, *From Eternity to Here*
  (Dutton, 2010); see also D. Albert,
  *Time and Chance* (Harvard Univ. Press, 2000).
6. [6] B. Bylicka, M. Tukiainen, J. Piilo, D. Chruściński, and S. Maniscalco,
  "Thermodynamic power of non-Markovianity,"
  *Sci. Rep.* **6**, 27989 (2016).
7. [7] J. Goold, M. Huber, A. Riera, L. del Rio, and P. Skrzypczyk,
  "The role of quantum information in thermodynamics,"
  *J. Phys. A* **49**, 143001 (2016).
8. [8] H.-P. Breuer, E.-M. Laine, J. Piilo, and B. Vacchini,
  "Colloquium: Non-Markovian dynamics in open quantum systems,"
  *Rev. Mod. Phys.* **88**, 021002 (2016).
9. [9] Á. Rivas, S. F. Huelga, and M. B. Plenio,
  "Entanglement and Non-Markovianity of Quantum Evolutions,"
  *Phys. Rev. Lett.* **105**, 050403 (2010).
10. [10] H.-P. Breuer and F. Petruccione,
  *The Theory of Open Quantum Systems*
  (Oxford Univ. Press, 2002).
11. [11] T. M. Cover and J. A. Thomas,
  *Elements of Information Theory*, 2nd ed.
  (Wiley, 2006).
12. [12] M. M. Wolf, J. Eisert, T. S. Cubitt, and J. I. Cirac,
  "Assessing Non-Markovian Quantum Evolution,"
  *Phys. Rev. Lett.* **101**, 150402 (2008).
13. [13] Anonymous, "Gauge-Invariant Process Entanglement in Indivisible Stochastic
  Processes: From ZZ-Gate Phantoms to Bell Inequalities,"
  companion paper, preprint (2026).
