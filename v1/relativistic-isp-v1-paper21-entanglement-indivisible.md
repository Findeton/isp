# Gauge-Invariant Process Entanglement in Indivisible Stochastic Processes

*From ZZ-Gate Phantoms to Bell Inequalities*

Author: Felix Robles Elvira

Department of Physics & Department of Philosophy, Harvard University

Date: Preprint · March 2026

Companion to "Entropy Structure of Indivisible Stochastic Processes" [1]
and to arXiv:2302.10778, 2309.03085, 2507.21192

## Abstract

Abstract.

We introduce a gauge-invariant process measure $E_\mathrm{cl}(A:B)$
for bipartite indivisible stochastic processes, building on the entropy framework
of the companion paper [

1

].
The measure is defined as a column-averaged KL divergence from the nearest product
transition law, has a closed form (Theorem 1), and satisfies basic non-negativity,
gauge-invariance, and local-stochastic monotonicity properties.
We show that the standard von Neumann entanglement entropy can assign a nonzero value
to the ZZ gate acting on a superposition input even though the isolated terminal
transition law has $\Gamma_\mathrm{ZZ} = I$; in that $\Gamma$-level sense the effect is a
terminal-basis artifact of the chosen lift/circuit rather than an intrinsic property of the terminal kernel itself.
We then show that $E_\mathrm{cl}$ applied to the full Bell-test circuit
$(H\otimes H)\cdot ZZ(\varphi)\cdot(H\otimes H) = XX(\varphi)$ correctly recovers
$H_b(\sin^2(\varphi/2))$ and the standard CHSH-violating joint laws at the full-circuit
level, demonstrating that the ISP framework is compatible with Bell's theorem.
We prove Bell-state recovery ($E_\mathrm{cl} = \ln 2$ for CNOT-based Bell preparation),
discuss the CHSH inequality in ISP language, discuss LOCC monotonicity as an open problem,
and provide supporting evidence and partial results for the entanglement-capacity
conjecture $E_\mathrm{cl} = \sup_{p_A \otimes p_B} I(A:B)[\Gamma(p_A\otimes p_B)]$.

## Introduction

The companion paper [1] establishes that within Barandes'
indivisible stochastic process (ISP) framework [2–4],
the Shannon entropy $S[p]$ of the configuration distribution is the unique entropy
determined by the transition matrix $\Gamma$ alone, while the von Neumann entropy
$S_\mathrm{vN}[\rho]$ is representation-dependent — not determined by $\Gamma$ alone,
but requiring the choice of a lifting $\Theta$ with $|\Theta_{ij}|^2 = \Gamma_{ij}$.

This paper develops the bipartite extension: *what is a natural, gauge-invariant
process-level measure of bipartite entanglement/correlation for an indivisible stochastic process?*
The standard answer — von Neumann entanglement entropy $S_\mathrm{vN}[\rho_A]$ —
is representation-dependent and therefore not determined by $\Gamma_{AB}$ alone at the
$\Gamma$-level of description.
We introduce a measure $E_\mathrm{cl}(A:B)$ defined entirely from $\Gamma_{AB}$,
prove its basic properties, and show that it reproduces the main full-circuit
correlation phenomena studied here, including Bell inequality violations.

A key example is the ZZ gate $U_\mathrm{ZZ}(\varphi) = \exp(-i\frac{\varphi}{2}\sigma_z\otimes\sigma_z)$.
Its transition matrix is $\Gamma_\mathrm{ZZ} = I_{4\times 4}$ (identity), giving
$E_\mathrm{cl} = 0$. Yet the von Neumann entanglement entropy for the superposition
input $|{+}{+}\rangle$ is $H_b(\sin^2(\varphi/2)) > 0$ — a value that is not fixed by
the isolated terminal transition law alone. Relative to the isolated
$\Gamma_\mathrm{ZZ}$ description, this is a *terminal-basis artifact*: the
Z-basis transition kernel by itself cannot witness the phase-entangling power of the
chosen ZZ Hamiltonian.
However, when the ZZ gate is embedded in the full Bell-test circuit with physical
Hadamard rotations (which are mandatory active operations in the ISP framework,
since "measuring in the X-basis" requires a physical Hamiltonian), the composed
transition law is $\Gamma_{XX}(\varphi)$ with $E_\mathrm{cl} = H_b(\sin^2(\varphi/2))$.
The point is not that standard quantum entanglement is fictitious; rather, the nonzero
$S_\mathrm{vN}$ belongs to a larger composed experiment and is not fixed by the isolated
terminal kernel $\Gamma_\mathrm{ZZ}$ by itself.

The paper is organized as follows.
Section II reviews the relevant background from [1] and
[2–4].
Section III introduces the $E_\mathrm{cl}$ measure, its closed form, and its properties.
Section IV proves the isolated terminal-kernel invisibility result and the Bell-test circuit result.
Section V develops the CHSH Bell inequality in ISP language.
Section VI discusses LOCC monotonicity.
Section VII addresses Conjecture 1 (entanglement capacity) with supporting evidence.
Section VIII discusses open questions and concludes.

## Background

### Indivisible stochastic processes

We follow the notation of [2–4].
A stochastic process on a configuration space $\mathcal{C} = \{1,\ldots,N\}$ is a family
of transition matrices $\Gamma(t\leftarrow t_0)$ with non-negative entries and unit column
sums, satisfying $p(t) = \Gamma(t\leftarrow t_0) p(t_0)$.
A process is *indivisible* if for every intermediate time $t'$, the algebraic
factorization $\widetilde\Gamma = \Gamma(t\leftarrow t_0)[\Gamma(t'\leftarrow t_0)]^{-1}$
has at least one negative entry — making it *pseudo-stochastic*.

Every quantum process corresponds to an indivisible stochastic process via the
*stochastic-quantum correspondence* [2]:
there exists a complex matrix $\Theta(t\leftarrow t_0)$ (the time-evolution operator,
unique up to Schur-Hadamard gauge transformations) with
$\Gamma_{ij} = |\Theta_{ij}|^2$.
The associated density matrix is
$\rho(t) = \Theta \bigl[\sum_j p_j(t_0) P_j\bigr] \Theta^\dagger$,
with $p_i(t) = \mathrm{Tr}[P_i \rho(t)]$.

### Schur-Hadamard gauge freedom and extra structure

The element-wise rephasing $\Theta_{ij} \to e^{i\phi_{ij}}\Theta_{ij}$ leaves
$\Gamma_{ij} = |\Theta_{ij}|^2$ invariant.
Following Barandes [4], this *Schur-Hadamard gauge freedom*
is a genuine $\Gamma$-level invariance of a specified time-evolution operator:
different entry-wise rephasings of $\Theta$ represent the same transition data.

This is a $\Gamma$-level lift statement. An arbitrary entry-wise rephasing preserves
the terminal transition matrix, but it need not preserve ordinary unitarity, the same
Hamiltonian generator, or the same sequential circuit factorization. Thus a
von-Neumann or state-vector entanglement value belongs to a chosen lift or chosen
full circuit, whereas $E_\mathrm{cl}$ below is deliberately restricted to what the
terminal transition law itself fixes.

Additional restrictions appear only after one adds structure not contained in $\Gamma$
alone. If a physical process is modeled as sequential Hamiltonians with amplitudes
$\Theta_1, \Theta_2, \Theta_3$, then a Schur-Hadamard rephasing of the already-composed
operator $\Theta_\mathrm{total} = \Theta_3\Theta_2\Theta_1$ is a genuine
$\Gamma_\mathrm{total}$-level gauge transformation. By contrast, independently rephasing
an intermediate $\Theta_k$ while holding the other factors fixed generally changes
$\Theta_\mathrm{total}$ and hence observable outcomes. The same distinction applies to
chosen dilations and subsystem decompositions: the broad $\Gamma$-level gauge freedom
remains, but not every rephasing of auxiliary ingredients is a symmetry of the enlarged
construction.

A quantity is *gauge-invariant* (in the ISP sense) if it depends only on $\Gamma$,
not on the particular lifting $\Theta$.
The Shannon entropy $S[p]$ is gauge-invariant; the von Neumann entropy $S_\mathrm{vN}[\rho]$
is not [1, Thm. 2].
$S_\mathrm{vN}$ is experimentally measurable (via state tomography) but is underdetermined
by $\Gamma$ alone — different liftings yield different values.

## The $E_\mathrm{cl}$ Process Entanglement Measure

### Definition and closed form

For a bipartite system $AB$ with $\mathcal{C}_{AB} = \mathcal{C}_A \times \mathcal{C}_B$
(sizes $N_A$ and $N_B$), we first consider a process-level measure that does not privilege
any specific input preparation. Absent such a preparation, the natural $\Gamma$-level choice
is to weight all input columns equally; Section IV.2 then introduces the corresponding
state-dependent variant.

**Definition 1**

(Process entanglement).

For a bipartite transition matrix $\Gamma_{AB}$, the

*process entanglement*

is
$$E_\mathrm{cl}(A:B)[\Gamma_{AB}] =
\min_{\substack{\Gamma_A,\,\Gamma_B \\ \text{col.-stochastic}}}
\frac{1}{N_A N_B}\sum_{j_A,j_B}\sum_{i_A,i_B}
\Gamma_{(i_Ai_B)(j_Aj_B)}\ln\frac{\Gamma_{(i_Ai_B)(j_Aj_B)}}{\Gamma_A(i_A|j_A)\,\Gamma_B(i_B|j_B)}.$$

**Theorem 1**

(Closed form).

The minimum in Definition 1 is attained by the average marginal transition matrices
$$\Gamma_A^*(i_A|j_A) = \frac{1}{N_B}\sum_{j_B}\sum_{i_B}\Gamma_{(i_Ai_B)(j_Aj_B)},
\qquad
\Gamma_B^*(i_B|j_B) = \frac{1}{N_A}\sum_{j_A}\sum_{i_A}\Gamma_{(i_Ai_B)(j_Aj_B)},$$
and the minimum value is
$$E_\mathrm{cl}(A:B) = \frac{1}{N_A N_B}\sum_{j_A,j_B,i_A,i_B}
\Gamma_{(i_Ai_B)(j_Aj_B)}\ln\frac{\Gamma_{(i_Ai_B)(j_Aj_B)}}{\Gamma_A^*(i_A|j_A)\,\Gamma_B^*(i_B|j_B)}.$$

Proof.

The key observation is that $\Gamma_A^*$ is

*independent of $\Gamma_B$*

: the
Lagrangian gradient with respect to $\Gamma_A(i_A|j_A)$ is
$-\frac{1}{N_AN_B}\sum_{j_B,i_B}\Gamma_{(i_Ai_B)(j_Aj_B)}/\Gamma_A(i_A|j_A) + \lambda_{j_A}$,
which contains no $\Gamma_B$ term.
Setting it to zero and applying the column-stochastic constraint
$\sum_{i_A}\Gamma_A^*(i_A|j_A) = 1$ (using $\sum_{i_A,i_B}\Gamma_{(i_Ai_B)(j_Aj_B)} = 1$
for each $(j_A,j_B)$, so $\sum_{j_B,i_A,i_B}\Gamma_{(i_Ai_B)(j_Aj_B)} = N_B$) gives
$q_{i_A}^* \propto \sum_{j_B,i_B}\Gamma_{(i_Ai_B)(j_Aj_B)} = N_B\,\Gamma_A^*(i_A|j_A)$.
Since $\Gamma_A^*$ does not depend on $\Gamma_B$, the two optimizations completely
decouple; the symmetric argument determines $\Gamma_B^*$, and joint global optimality follows.

$\square$

$E_\mathrm{cl}$ decomposes as the sum of three non-negative terms (Theorem 2 below):
average within-column mutual information, an $A$-marginal variation term, and a symmetric
$B$ term.

**Theorem 2**

(Decomposition).

Let $I_j(A:B) = \sum_{i_A,i_B}\Gamma_{(i_Ai_B)j}\ln
\frac{\Gamma_{(i_Ai_B)j}}{\Gamma_{A,j}(i_A)\,\Gamma_{B,j}(i_B)}$ be the column-$j$
mutual information, where $\Gamma_{A,j}$, $\Gamma_{B,j}$ are the column-wise marginals.
Then
$$E_\mathrm{cl}(A:B) =
\frac{1}{N_AN_B}\sum_j I_j(A:B) + V_A + V_B,$$
where $V_A, V_B \geq 0$ measure column-to-column variation of the marginals relative to
their column-averaged versions $\Gamma_A^*$, $\Gamma_B^*$.
All three terms are non-negative.

### Properties

**Proposition 1**

(Properties of $E_\mathrm{cl}$).

(a) *Non-negativity:* $E_\mathrm{cl}(A:B) \geq 0$, with equality iff
$\Gamma_{AB}(i_Ai_B|j_Aj_B) = \Gamma_A(i_A|j_A)\Gamma_B(i_B|j_B)$ column-wise.

(b) *Gauge invariance:* $E_\mathrm{cl}$ depends only on $\Gamma_{AB}$,
not on any choice of lifting $\Theta_{AB}$.

(c) *Computability:* $E_\mathrm{cl}$ is computable in $O(N_A^2 N_B^2)$ arithmetic
operations via Theorem 1.

(d) *Monotonicity under local stochastic operations (LSO):*
$E_\mathrm{cl}[(\Lambda_A\otimes\Lambda_B)\Gamma_{AB}] \leq E_\mathrm{cl}[\Gamma_{AB}]$
for any column-stochastic $\Lambda_A$, $\Lambda_B$.

Proof sketch.

(a) $D_\mathrm{KL} \geq 0$ with equality iff distributions coincide column-by-column.
(b) Immediate from Definition 1.
(c) Follows from Theorem 1.
(d) A local map $\Lambda_A\otimes\Lambda_B$ sends optimal marginals
$\Gamma_A^*\mapsto\Lambda_A\Gamma_A^*$, $\Gamma_B^*\mapsto\Lambda_B\Gamma_B^*$;
the data-processing inequality for KL divergence then gives the bound.

$\square$

**Remark 1**

(LOCC monotonicity).

Proposition 1(d) establishes monotonicity under local stochastic operations (LSO) —
product maps $\Lambda_A \otimes \Lambda_B$.
The standard criterion for an entanglement monotone is non-increase under the larger class
of

*local operations and classical communication*

(LOCC), where future operations
can be conditioned on classical communication of past measurement outcomes.
LOCC protocols are adaptive and create stochastic maps that are generally not product
maps; Proposition 1(d) does not directly imply LOCC monotonicity.
We conjecture that $E_\mathrm{cl}$ is also LOCC-monotone — the physical intuition is
that classical communication cannot create correlations in $\Gamma_{AB}$ — but a
rigorous proof requires a careful analysis of how LOCC transforms bipartite stochastic
transition matrices. We leave this as an open problem.

## The ZZ Gate: Terminal-Basis Phantom and Bell-Test Recovery

### Worked examples: XX, ZZ, and CNOT

For a 2-qubit gate $U$, set $\Gamma_{(i_Ai_B)(j_Aj_B)} = |\langle i_Ai_B|U|j_Aj_B\rangle|^2$
and compute $E_\mathrm{cl}$ via Theorem 1.

**Proposition 2**

(XX interaction).

For $U_\mathrm{XX}(\theta) = \exp(-i\tfrac{\theta}{2}\sigma_x\otimes\sigma_x)$,
$$E_\mathrm{cl}(A:B)[\Gamma_\mathrm{XX}(\theta)]
= H_b\!\left(\sin^2\tfrac{\theta}{2}\right)
= S_\mathrm{vN}[\rho_A^{(j)}]
= I(A:B)[p_\mathrm{out}^{(j)}] \quad \forall\,j,$$
where $H_b(q) = -q\ln q - (1-q)\ln(1-q)$ and $j$ denotes any computational-basis input.
The three quantities coincide because each column of $\Gamma_\mathrm{XX}$ has its
$A$-marginal independent of $j_B$, giving $V_A = V_B = 0$.

**Proposition 3**

(ZZ interaction — isolated terminal-kernel invisibility).

For $U_\mathrm{ZZ}(\varphi) = \exp(-i\tfrac{\varphi}{2}\sigma_z\otimes\sigma_z)$:
$$E_\mathrm{cl}(A:B)[\Gamma_\mathrm{ZZ}(\varphi)] = 0
\quad \text{and} \quad
I(A:B)[p_{AB}] = 0 \quad \forall\,\varphi \text{ and any product input.}$$
Yet for the superposition input $|{+}\rangle\!\otimes\!|{+}\rangle$,
$$S_\mathrm{vN}[\rho_A^{(+)}] = H_b\!\left(\sin^2\tfrac{\varphi}{2}\right) > 0
\quad \text{for } \varphi\neq 0,\pi.$$
The nonzero $S_\mathrm{vN}$ is therefore not determined by
$\Gamma_\mathrm{ZZ} = I_{4\times 4}$ alone. It is a property of a chosen lift and
of the larger preparation/circuit context, not of the isolated terminal transition
kernel by itself.

Proof.

$U_\mathrm{ZZ}$ is diagonal in the computational basis with
$U_\mathrm{ZZ}|j_Aj_B\rangle = e^{-i\varphi(-1)^{j_A+j_B}/2}|j_Aj_B\rangle$,
so $|\Theta_{(i_Ai_B)(j_Aj_B)}|^2 = \delta_{i_Aj_A}\delta_{i_Bj_B}$ and
$\Gamma_\mathrm{ZZ} = I_{4\times 4}$.
By Proposition 1(a), $E_\mathrm{cl} = 0$.
For $|{+}{+}\rangle = \frac{1}{2}\sum_{j_Aj_B}|j_Aj_B\rangle$, direct computation gives
$\rho_A = \frac{1}{2}I + \frac{\cos\varphi}{2}\sigma_x$ with eigenvalues
$\cos^2(\varphi/2)$, $\sin^2(\varphi/2)$, so
$S_\mathrm{vN}[\rho_A] = H_b(\sin^2(\varphi/2))$.
The off-diagonal elements of $\rho_A$ depend on the phases of $\Theta_\mathrm{ZZ}$;
a Schur-Hadamard transformation continuously varies $S_\mathrm{vN}[\rho_A]$ from
$0$ to $\ln 2$ while $\Gamma_\mathrm{ZZ} = I$ remains unchanged.

$\square$

**Remark 2**

(Why this is only a terminal-kernel statement).

The limitation is terminal-basis because the $|{+}{+}\rangle$ input itself requires a prior
physical Hamiltonian (a Hadamard gate) in the ISP framework — the framework's configuration
space $\mathcal{C}$ is the Z-basis, and $|{+}{+}\rangle$ is not a basis state.
Treating this input as "given" therefore implicitly encodes a prior operation, making
the analysis a composed experiment analyzed as if terminal.
The representation-dependent $S_\mathrm{vN}$ value of $H_b(\sin^2(\varphi/2))$
does carry real physical information about the composed experiment — as Proposition 4
below makes explicit.
What fails is only the inference that this value is already fixed by the isolated terminal
kernel $\Gamma_\mathrm{ZZ}$.
Likewise, the Hamiltonian generating $U_\mathrm{ZZ}$ fixes one particular physical
realization of $\Theta_\mathrm{ZZ}$, but this does not negate the broad Schur-Hadamard
gauge invariance of a specified terminal operator at the $\Gamma$ level.
It means instead that once ZZ is embedded in a particular circuit, not every independent
rephasing of internal steps is a symmetry of the larger construction.

**Proposition 4**

(Bell-test circuit recovers correct entanglement).

Let $U_\mathrm{Bell\text{-}test} = (H\otimes H)\cdot ZZ(\varphi)\cdot(H\otimes H)$.
Using $H\sigma_z H = \sigma_x$:
$$(H\otimes H)\,e^{-i\frac{\varphi}{2}\sigma_z\otimes\sigma_z}\,(H\otimes H)
= e^{-i\frac{\varphi}{2}\sigma_x\otimes\sigma_x} = U_\mathrm{XX}(\varphi).$$
Therefore
$$E_\mathrm{cl}(A:B)\bigl[\Gamma_{U_\mathrm{Bell\text{-}test}}\bigr]
= H_b\!\left(\sin^2\tfrac{\varphi}{2}\right) = S_\mathrm{vN}[\rho_A^{(+)}].$$
The ISP framework correctly predicts Bell correlations when physical basis-rotation
Hamiltonians are included as active operations in the full circuit.

Proof.

The identity $(H\otimes H)\cdot ZZ(\varphi)\cdot(H\otimes H) = XX(\varphi)$ follows
from $H\sigma_z H = \sigma_x$.
Apply Proposition 2: $E_\mathrm{cl}[\Gamma_{XX}(\varphi)] = H_b(\sin^2(\varphi/2))$.
The agreement with $S_\mathrm{vN}[\rho_A^{(+)}]$ follows from Proposition 5 below
(state-dependent formulation collapses to mutual information of output marginals for a pure input).

$\square$

### State-dependent entanglement and Bell-state recovery

When a specific initial state $p(t_0)$ is physically prepared, a state-weighted variant
captures the entangling power of the process for that preparation:

**Definition 2**

(State-dependent process entanglement).

$$E_\mathrm{cl}(A:B;\,p_0) =
\min_{\Gamma_A',\,\Gamma_B'}\;\sum_{j \in \mathcal{C}_{AB}} p_j(t_0)\;
D_\mathrm{KL}\!\bigl[(\Gamma_{AB})_{:j}\;\big\|\;(\Gamma_A'\otimes\Gamma_B')_{:j}\bigr].$$
When $p(t_0)$ is uniform, this reduces to Definition 1.
For a pure-state input concentrated on a single column $j_0$, the minimization collapses
to the mutual information of the output marginals of that column.

**Proposition 5**

(Bell-state recovery).

Let $U_\mathrm{Bell} = \mathrm{CNOT}\cdot(H\otimes I)$ and $p(t_0) = (1,0,0,0)^\top$
($|00\rangle$). Then
$$E_\mathrm{cl}(A:B;\,p_{00}=1)[\Gamma_{U_\mathrm{Bell}}] = \ln 2 = S_\mathrm{vN}[\rho_A].$$

Proof.

Since $p_j(t_0) = \delta_{j,00}$, the minimization is a single-column KL divergence.
Column $j=00$ of $\Gamma_{U_\mathrm{Bell}}$ maps $|00\rangle \to |\Phi^+\rangle
= \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$, giving output distribution
$(1/2, 0, 0, 1/2)^\top$ with marginals
$Q_A^* = Q_B^* = (1/2, 1/2)^\top$.
The KL divergence is
$E_\mathrm{cl} = \frac{1}{2}\ln\frac{1/2}{1/4} + \frac{1}{2}\ln\frac{1/2}{1/4} = \ln 2$.

$\square$

Proposition 5 recovers $S_\mathrm{vN}[\rho_A] = \ln 2$ for the Bell state via a
calculation on classical probability vectors, with no density matrices or Hilbert space.
For general initial states $p_0$, the minimum in Definition 2 also has an explicit
closed form — the same decoupling that makes Theorem 1 work applies here too.

Corollary 1 (Closed form for state-dependent entanglement).
The minimum in Definition 2 is attained at
$$\Gamma_A'^*(i_A|j_A) = \frac{\displaystyle\sum_{j_B,i_B} p_{j_Aj_B}\,\Gamma_{(i_Ai_B)(j_Aj_B)}}{\displaystyle\sum_{j_B} p_{j_Aj_B}},
\qquad
\Gamma_B'^*(i_B|j_B) = \frac{\displaystyle\sum_{j_A,i_A} p_{j_Aj_B}\,\Gamma_{(i_Ai_B)(j_Aj_B)}}{\displaystyle\sum_{j_A} p_{j_Aj_B}},$$
and the minimum value is
$E_\mathrm{cl}(A:B;\,p_0) = \sum_j p_j\,D_\mathrm{KL}\!\bigl[(\Gamma_{AB})_{:j}\;\big\|\;(\Gamma_A'^*\otimes\Gamma_B'^*)_{:j}\bigr]$.
When $p_0$ is uniform this reduces to Theorem 1.

Proof.
The Lagrangian gradient with respect to $\Gamma_A'(i_A|j_A)$ is
$-\sum_{j_B,i_B}p_{j_Aj_B}\Gamma_{(i_Ai_B)(j_Aj_B)}/\Gamma_A'(i_A|j_A) + \lambda_{j_A}$,
which is independent of $\Gamma_B'$.
Setting it to zero and normalising by $\sum_{i_A}\Gamma_A'^*(i_A|j_A)=1$, with
denominator $\sum_{j_B}p_{j_Aj_B}$ (the total weight on $j_A$-columns), gives the formula above.
The symmetric argument determines $\Gamma_B'^*$; the two optimisations decouple, giving
the unique global minimum.
$\square$

| Gate / experiment | $E_\mathrm{cl}$ | $S_\mathrm{vN}[\rho_A]$ (comp. basis input) | Gauge-invariant? |
| --- | --- | --- | --- |
| XX$(\theta)$ | $H_b(\sin^2\theta/2)$ | $H_b(\sin^2\theta/2)$ | Both yes |
| ZZ$(\varphi)$, comp.-basis input | $0$ | $0$ | Both yes |
| ZZ$(\varphi)$, superposition input $|{+}{+}\rangle^\dagger$ | $0$ | $H_b(\sin^2\varphi/2)$ (phantom) | $E_\mathrm{cl}$ yes; $S_\mathrm{vN}$ no |
| Bell-test circuit $(H\otimes H)\cdot ZZ\cdot(H\otimes H)$ | $H_b(\sin^2\varphi/2)$ | $H_b(\sin^2\varphi/2)$ | Both yes |
| CNOT | $\ln 2$ | $0$ (comp. basis input) | $E_\mathrm{cl}$ yes |
| Bell prep. $U_\mathrm{Bell}$, $p_{00}=1$ | $\ln 2$ | $\ln 2$ | Both yes |

$^\dagger$ The $|{+}{+}\rangle$ input requires a prior Hadamard; $S_\mathrm{vN}$ here is
chosen-lift/circuit dependent rather than fixed by the isolated terminal kernel. Gauge-dependence range: $[0, \ln 2]$.

## CHSH Bell Inequalities in ISP Language

Bell's theorem [9] rules out local hidden variable theories: no theory
where outcomes are predetermined by local variables independent of measurement settings
can reproduce all quantum predictions.
We now show explicitly that the ISP framework reproduces the standard CHSH violation.
The decisive point is that the family of setting-dependent joint distributions
$\{p(ab|xy)\}$ generated by the full circuits lies outside the local polytope.
The non-factorizability of each fixed transition matrix $\Gamma^{(xy)}$ is a useful
ISP-language witness of the process structure involved, but Bell nonlocality concerns
the full family of setting-dependent experiments rather than any single circuit in isolation.

### CHSH setup in the ISP framework

A CHSH experiment involves four measurement settings $(x,y) \in \{0,1\}^2$.
Each setting specifies local measurement bases for Alice ($x$) and Bob ($y$).
In standard QM, this is implemented by local unitaries $R_A^{(x)}$, $R_B^{(y)}$ applied
before terminal Z-basis detectors.
In the ISP framework, these local unitaries are physical Hamiltonians — active operations.
The complete circuit for setting $(x,y)$ is:
$$\Theta_\mathrm{total}^{(xy)} = \bigl(R_A^{(x)}\otimes R_B^{(y)}\bigr)
\cdot U_\mathrm{interaction}
\cdot \bigl(U_\mathrm{prep}\bigr),$$
with observable transition matrix $\Gamma_\mathrm{total}^{(xy)} = |\Theta_\mathrm{total}^{(xy)}|^2$.

For each fixed $(x,y)$, the joint output probability is
$p(ab|xy) = \Gamma_\mathrm{total}^{(xy)}(ab|\,j_0)$ for initial configuration $j_0$.
The ISP framework predicts the same $p(ab|xy)$ as the quantum Born rule,
since $\Gamma = |\Theta|^2$ by construction.

### Bell inequality violation and circuit-level non-factorizability

The CHSH inequality states: for any local hidden variable theory,
$$|S_\mathrm{CHSH}| = |C(0,0) + C(0,1) + C(1,0) - C(1,1)| \leq 2,$$
where $C(x,y) = E[(-1)^{a+b}|xy] = \sum_{a,b}(-1)^{a+b}p(ab|xy)$.
Quantum mechanics achieves $|S_\mathrm{CHSH}| \leq 2\sqrt{2}$ (Tsirelson bound).

**Proposition 6**

(ISP predicts CHSH violations).

Consider Bell-state preparation $U_\mathrm{Bell} = \mathrm{CNOT}\cdot(H\otimes I)$ from
$|00\rangle$ with four measurement circuits
$$\Theta^{(xy)} = \bigl(R_A^{(x)}\otimes R_B^{(y)}\bigr)\cdot U_\mathrm{Bell},\qquad
\Gamma^{(xy)} = |\Theta^{(xy)}|^2,$$
where $R_A^{(0)}=I$, $R_A^{(1)}=R_y(-\tfrac{\pi}{2})$,
$R_B^{(0)}=R_y(-\tfrac{\pi}{4})$, $R_B^{(1)}=R_y(\tfrac{\pi}{4})$, with
$R_y(\alpha) = \bigl(\begin{smallmatrix}\cos\frac{\alpha}{2}&-\sin\frac{\alpha}{2}\\\sin\frac{\alpha}{2}&\cos\frac{\alpha}{2}\end{smallmatrix}\bigr)$.
Then the ISP framework predicts
$$|S_\mathrm{CHSH}| = |C(0,0)+C(0,1)+C(1,0)-C(1,1)| = 2\sqrt{2},$$
where $C(x,y)=\sum_{a,b}(-1)^{a+b}\Gamma^{(xy)}(ab|00)$,
in violation of the local hidden variable bound $|S|\leq 2$.
Moreover, $E_\mathrm{cl}[\Gamma^{(xy)}]>0$ for all four settings.

Proof.

Let $c=\cos(\pi/8)$, $s=\sin(\pi/8)$, so that $c^2-s^2=1/\sqrt{2}$ and $2cs=1/\sqrt{2}$.
Since $U_\mathrm{Bell}|00\rangle = |\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle+|11\rangle)$,
the output state for each circuit with initial configuration $j_0=00$ is:

*Setting $(0,0)$:*

$(I\otimes R_y(-\tfrac{\pi}{4}))|\Phi^+\rangle
= \frac{1}{\sqrt{2}}[|0\rangle(c|0\rangle-s|1\rangle)+|1\rangle(s|0\rangle+c|1\rangle)]
= \frac{c|00\rangle - s|01\rangle + s|10\rangle + c|11\rangle}{\sqrt{2}}.$

*Setting $(0,1)$:*

$(I\otimes R_y(\tfrac{\pi}{4}))|\Phi^+\rangle
= \frac{c|00\rangle + s|01\rangle - s|10\rangle + c|11\rangle}{\sqrt{2}}.$

*Setting $(1,0)$:*

Using $R_y(-\tfrac{\pi}{2})|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle-|1\rangle)$ and
$R_y(-\tfrac{\pi}{2})|1\rangle = \frac{1}{\sqrt{2}}(|0\rangle+|1\rangle)$:
$(R_y(-\tfrac{\pi}{2})\otimes R_y(-\tfrac{\pi}{4}))|\Phi^+\rangle
= \tfrac{1}{2}\bigl[(c+s)|00\rangle + (c-s)|01\rangle + (s-c)|10\rangle + (c+s)|11\rangle\bigr].$

*Setting $(1,1)$:*

$(R_y(-\tfrac{\pi}{2})\otimes R_y(\tfrac{\pi}{4}))|\Phi^+\rangle
= \tfrac{1}{2}\bigl[(c-s)|00\rangle + (c+s)|01\rangle - (c+s)|10\rangle + (c-s)|11\rangle\bigr].$

Squaring amplitudes gives the joint output probabilities $p(ab|xy) = \Gamma^{(xy)}(ab|00)$:

| Setting $(x,y)$ | $p(00)$ | $p(01)$ | $p(10)$ | $p(11)$ |
| --- | --- | --- | --- | --- |
| $(0,0)$ | $c^2/2$ | $s^2/2$ | $s^2/2$ | $c^2/2$ |
| $(0,1)$ | $c^2/2$ | $s^2/2$ | $s^2/2$ | $c^2/2$ |
| $(1,0)$ | $(c+s)^2/4$ | $(c-s)^2/4$ | $(c-s)^2/4$ | $(c+s)^2/4$ |
| $(1,1)$ | $(c-s)^2/4$ | $(c+s)^2/4$ | $(c+s)^2/4$ | $(c-s)^2/4$ |

The correlators $C(x,y)=p(00)-p(01)-p(10)+p(11)$ are:
$$C(0,0)=C(0,1)=c^2-s^2=\tfrac{1}{\sqrt{2}},\quad
C(1,0)=\tfrac{(c+s)^2-(c-s)^2}{2}=2cs=\tfrac{1}{\sqrt{2}},\quad
C(1,1)=\tfrac{(c-s)^2-(c+s)^2}{2}=-2cs=-\tfrac{1}{\sqrt{2}}.$$
Hence $S_\mathrm{CHSH}=C(0,0)+C(0,1)+C(1,0)-C(1,1)=4/\sqrt{2}=2\sqrt{2}$.

*Non-factorizability.*

For settings $(0,0)$ and $(0,1)$, the marginals of column $j=00$ are $p_A=(1/2,1/2)$ and
$p_B=(1/2,1/2)$, so the product reference is $(1/4,1/4,1/4,1/4)^\top$, which differs from
$(c^2/2, s^2/2, s^2/2, c^2/2)^\top$ since $c\neq s$; hence $I(A:B)[p(\cdot|xy)]>0$ and
$E_\mathrm{cl}[\Gamma^{(xy)}]\geq E_\mathrm{cl}(A:B;\,p_{00}=1)>0$.
The same argument applies to settings $(1,0)$ and $(1,1)$.

$\square$

Proposition 6 makes the ISP-language account of Bell's theorem explicit:
the family of full-circuit distributions $\{p(ab|xy)\}$ generated by the setting-dependent
transition laws lies outside the local polytope, so the framework is not a local hidden
variable theory.
The fact that each $\Gamma_\mathrm{total}^{(xy)}$ is non-factorizable
($E_\mathrm{cl} > 0$) provides a gauge-invariant witness of the correlation structure
present within each fixed circuit, but Bell nonlocality is a statement about the full
family of setting-dependent distributions rather than any single $E_\mathrm{cl}$ value.
Note that $E_\mathrm{cl}[\Gamma_\mathrm{ZZ}] = 0$ (the ZZ gate by itself is non-entangling
in the Z-basis) is completely consistent with this: the Bell test requires the full circuit,
whose $E_\mathrm{cl}$ is non-zero.

The CHSH quantity $S_\mathrm{CHSH}$ involves four distinct experiments, each with its own
$\Gamma_\mathrm{total}^{(xy)}$.
There is therefore no single $E_\mathrm{cl}$ number that captures
"the Bell nonlocality" of the setup; the relevant objects are the family of joint
distributions $\{p(ab|xy)\}$ together with, as a complementary process-level summary,
the set $\{E_\mathrm{cl}[\Gamma^{(xy)}]\}_{x,y}$.
Each element of the latter is positive, and the combined set of joint distributions
$\{p(ab|xy)\}$ lies outside the local polytope.

## Monotonicity Under Local Operations and Classical Communication

Proposition 1(d) establishes LSO monotonicity: $E_\mathrm{cl}$ is non-increasing under
product stochastic maps $\Lambda_A \otimes \Lambda_B$.
The standard criterion for an entanglement monotone in quantum information
[10] is non-increase under the larger class LOCC.

An LOCC protocol between Alice and Bob proceeds in rounds: in each round, one party
performs a local measurement, communicates the outcome classically to the other, and
the other party's subsequent operation is conditioned on the received outcome.
In the ISP framework, a local measurement by Alice corresponds to applying a local
stochastic transition matrix $\Lambda_A^{(a)}$ conditioned on her outcome $a$,
followed by the classical channel that transmits $a$ to Bob, after which Bob applies
$\Lambda_B^{(a)}$.

The key difficulty is that the conditioned operation $\Lambda_B^{(a)}$ depends on $a$,
making the overall map
$\sum_a q_a (\Lambda_A^{(a)} \otimes \Lambda_B^{(a)})$
a convex combination of product maps, not a product map itself.
Standard arguments from quantum information use strong subadditivity to prove LOCC
monotonicity [10]; a direct stochastic analog would require controlling expressions of the form
$\sum_a q_a E_\mathrm{cl}[(\Lambda_A^{(a)}\otimes\Lambda_B^{(a)})\Gamma_{AB}]
\leq E_\mathrm{cl}[\Gamma_{AB}]$,
which would follow from Proposition 1(d) together with a suitable global convexity property
of $E_\mathrm{cl}$ in $\Gamma_{AB}$. The column-wise KL structure makes such a result plausible,
but we do not prove it here.

**Conjecture 2**

(LOCC monotonicity).

$E_\mathrm{cl}(A:B)$ is non-increasing under all finite-round LOCC protocols between
Alice and Bob.

We provide the following partial result supporting Conjecture 2.

**Proposition 7**

(Conditional convex-combination monotonicity).

If $E_\mathrm{cl}[\Gamma_{AB}]$ is convex in $\Gamma_{AB}$, then for any LOCC protocol expressible as a
convex combination of LSO maps,
$$E_\mathrm{cl}\!\left[\sum_a q_a (\Lambda_A^{(a)}\otimes\Lambda_B^{(a)})\Gamma_{AB}\right]
\leq \sum_a q_a E_\mathrm{cl}\!\left[(\Lambda_A^{(a)}\otimes\Lambda_B^{(a)})\Gamma_{AB}\right]
\leq E_\mathrm{cl}[\Gamma_{AB}].$$

Proof.

The first inequality is convexity of $E_\mathrm{cl}$ in $\Gamma_{AB}$.
The second is Proposition 1(d) applied to each term.

$\square$

Proposition 7 therefore provides only partial support for Conjecture 2.
The needed convexity has not been proved in full generality; the column-wise KL structure
makes it plausible, and our numerical checks on tested two-qubit gates support it,
but a general proof is lacking.
Full LOCC monotonicity for adaptive multi-round protocols remains open and may require
either establishing that global convexity or developing a different argument entirely.

## Entanglement Capacity: Supporting Evidence for Conjecture 1

**Proposition 8**

(Common zero set).

$E_\mathrm{cl}(A:B)[\Gamma_{AB}] = 0$ if and only if
$\sup_{p_A\otimes p_B} I(A:B)[\Gamma_{AB}(p_A\otimes p_B)] = 0$.

Proof.

($\Rightarrow$) If $E_\mathrm{cl}=0$ then $\Gamma_{(i_Ai_B)(j_Aj_B)}
= \Gamma_A^*(i_A|j_A)\Gamma_B^*(i_B|j_B)$ column-wise, so for any product input
$p_A\otimes p_B$ the output is $(\Gamma_A^*p_A)\otimes(\Gamma_B^*p_B)$, giving
$I(A:B)=0$ for all product inputs.
($\Leftarrow$) If $E_\mathrm{cl}>0$ then by Proposition 1(a) some column $j^*$ of
$\Gamma_{AB}$ is not a product distribution; the pure input $p_0=\delta_{j^*}$ yields
$E_\mathrm{cl}(A:B;\,p_{j^*}=1) = I(A:B)[(\Gamma_{AB})_{:j^*}] > 0$.

$\square$

Proposition 8 establishes that the two sides of Conjecture 1 share the same zero set.
The quantitative equality — that the distance-to-product-channel and the
maximum-output-mutual-information are numerically equal — is a stronger claim akin to
the entangling-power conjecture in quantum information [12].

**Conjecture 1**

(Entanglement capacity).

For any bipartite stochastic $\Gamma_{AB}$,
$$E_\mathrm{cl}(A:B)[\Gamma_{AB}] = \sup_{p_A\otimes p_B}\, I(A:B)\bigl[\Gamma_{AB}(p_A\otimes p_B)\bigr],$$
where the supremum is over all product input distributions.
If true, $E_\mathrm{cl}$ equals the maximum classical correlations the process can generate
from any product input — its

*entanglement capacity*

.

We provide three representative supporting checks of Conjecture 1.

*XX gate.*
Column $j$ of $\Gamma_\mathrm{XX}(\theta)$ has marginals independent of $j_B$, so
$I_j(A:B) = H_b(\sin^2(\theta/2))$ for all $j$.
The uniform input $p_A = p_B = (1/2, 1/2)$ achieves this mutual information and equals
$E_\mathrm{cl} = H_b(\sin^2(\theta/2))$. ✓

*ZZ gate.*
For any product input, the output distribution is
$p_\mathrm{out}(i_Ai_B) = p_A(i_A)p_B(i_B)$ (since $\Gamma_\mathrm{ZZ} = I$),
giving $I(A:B) = 0$ for all product inputs.
Hence $\sup = 0 = E_\mathrm{cl}$. ✓

*CNOT gate.*
For input $p_A = (1/2, 1/2)$, $p_B = (1, 0)$:
the output distribution is $p(00) = 1/2$, $p(11) = 1/2$,
giving $I(A:B) = \ln 2 = E_\mathrm{cl}[\Gamma_\mathrm{CNOT}]$. ✓
The supremum is achieved at a non-uniform product input — demonstrating that Conjecture 1
may require non-uniform optima.

Conjecture 1 would imply a chain of equalities
$E_\mathrm{cl}(A:B) = \sup_{p_0\,\mathrm{pure}} E_\mathrm{cl}(A:B;\,p_0)$,
linking the gate-level and state-dependent formulations.
For all gates tested, the supremum in Conjecture 1 is achieved at a product input on the
boundary of the simplex (a "semi-pure" input in at least one party), suggesting a
vertex characterization may be provable.
Proving Conjecture 1 for general $N_A, N_B$ is an open problem.

## Discussion and Conclusions

We have introduced a natural gauge-invariant process measure $E_\mathrm{cl}(A:B)$ for
indivisible stochastic processes, proved its closed form and basic properties, and shown
its compatibility with Bell inequality violations when full circuits are treated explicitly.
The central results are:

1. $E_\mathrm{cl}$ is a natural $\Gamma_{AB}$-level measure of non-factorizable process
  structure: it is defined from $\Gamma_{AB}$ alone (gauge-invariant by construction),
  computable in $O(N_A^2 N_B^2)$, and non-increasing under local stochastic operations.
  We do not claim here that it is the unique possible ISP notion of entanglement.
2. Schur-Hadamard gauge freedom is broad at the level of a specified
  $\Gamma$-associated operator. Additional phase data become physically relevant only
  after one fixes a particular circuit decomposition, Hamiltonian realization, or dilation.
3. The von Neumann entanglement entropy $S_\mathrm{vN}[\rho_A]$ for the ZZ gate
  with superposition input is chosen-lift/circuit dependent and invisible to any Z-basis experiment at the isolated $\Gamma_\mathrm{ZZ}$ level.
  It can still carry real physical information, but only about the larger prepared-and-measured
  circuit rather than the terminal kernel by itself.
4. $E_\mathrm{cl}$ applied to the full Bell-test circuit
  $(H\otimes H)\cdot ZZ(\varphi)\cdot(H\otimes H) = XX(\varphi)$ correctly recovers
  $H_b(\sin^2(\varphi/2))$, reproducing Bell correlations.
  The ISP framework is fully compatible with Bell's theorem.
5. The CHSH inequality is violated in the ISP framework because the joint transition
  distributions $\{p(ab|xy)\}$ generated by the setting-dependent circuits lie outside
  the local polytope. The non-factorizability of each
  $\Gamma_\mathrm{total}^{(xy)}$ ($E_\mathrm{cl} > 0$) is a useful gauge-invariant witness
  of the accompanying circuit-level process structure, but no single $E_\mathrm{cl}$ value
  by itself exhausts the Bell claim.
6. Bell-state preparation from $|00\rangle$ gives $E_\mathrm{cl}(A:B;\,p_{00}=1) = \ln 2$,
  recovering the standard entanglement entropy without density matrices or Hilbert space.
7. LOCC monotonicity and entanglement-capacity remain open. What is established here is
  LSO monotonicity, a conditional convex-combination LOCC bound under an unproved convexity
  assumption, and several supporting checks of Conjecture 1.

Open questions include: full proof of LOCC monotonicity (Conjecture 2); proof of the
entanglement-capacity characterization (Conjecture 1); a more principled characterization
of when the uniformly weighted process measure should be preferred over the state-dependent
version; extending $E_\mathrm{cl}$ to
continuous-variable systems; and characterizing the set of joint distributions
$\{E_\mathrm{cl}[\Gamma^{(xy)}]\}_{x,y}$ that are achievable by indivisible processes
(an analogue of the quantum correlation polytope for stochastic transition matrices).

## References

1. [1] Anonymous, "Entropy Structure of Indivisible Stochastic Processes,"
  companion paper, preprint (2026).
2. [2] J. A. Barandes, "The Stochastic-Quantum Correspondence,"
  arXiv:2302.10778 (2023); *Brit. J. Phil. Sci.* (2025).
3. [3] J. A. Barandes, "The Stochastic-Quantum Theorem,"
  arXiv:2309.03085 (2023).
4. [4] J. A. Barandes, "Quantum Systems as Indivisible Stochastic Processes,"
  arXiv:2507.21192 (2025).
5. [5] T. Baumgratz, M. Cramer, and M. B. Plenio,
  "Quantifying Coherence,"
  *Phys. Rev. Lett.* **113**, 140401 (2014).
6. [6] V. Vedral, M. B. Plenio, M. A. Rippin, and P. L. Knight,
  "Quantifying Entanglement,"
  *Phys. Rev. Lett.* **78**, 2275 (1997).
7. [7] M. B. Plenio and S. Virmani,
  "An introduction to entanglement measures,"
  *Quant. Inf. Comput.* **7**, 1–51 (2007).
8. [8] T. M. Cover and J. A. Thomas,
  *Elements of Information Theory*, 2nd ed. (Wiley, 2006).
9. [9] J. S. Bell, "On the Einstein Podolsky Rosen paradox,"
  *Physics* **1**, 195–200 (1964).
10. [10] G. Vidal, "Entanglement monotones,"
  *J. Mod. Opt.* **47**, 355–376 (2000).
11. [11] B. S. Cirel'son, "Quantum generalizations of Bell's inequality,"
  *Lett. Math. Phys.* **4**, 93–100 (1980).
12. [12] P. Zanardi, C. Zalka, and L. Faoro,
  "Entangling power of quantum evolutions,"
  *Phys. Rev. A* **62**, 030301(R) (2000).
