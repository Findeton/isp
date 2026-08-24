# ISP v17 — closed-system balance and conservation gate

## Why a stationary Gibbs law cannot be the missing fundamental selector by itself

**Status:** COMPLETE AUTHOR-SIDE MATHEMATICAL/PHYSICAL FEASIBILITY GATE / NOT A CANDIDATE / NOT INDEPENDENTLY REVIEWED

**Date:** 2026-08-24

**Scientific result awarded:** none

**Authority created:** none
**Official pin, model, review, experiment, gravity paper, Paper 04B successor, or ontology selection:** none

---

## 0. Executive result

The preceding CP-CQ kernel gate identified stable vacuum and detailed balance
as possible physical constraints on the free decoherence and diffusion
kernels. A new exact primary source now constructs finite hybrid
quantum--classical Lindblad dynamics with stationary canonical states. That
construction is real progress, but it does not select one physical law.

Two exact facts explain why.

First, detailed balance fixes forward/backward **ratios**, not the symmetric
conductances or absolute rates. For a finite state space with faithful
stationary law $\pi$, every reversible generator has off-diagonal rates

$$
k_{i\leftarrow j}=\frac{c_{ij}}{\pi_j},
\qquad
c_{ij}=c_{ji}\geq 0.
\tag{1}
$$

The stationary law and detailed-balance relation leave one nonnegative
conductance $c_{ij}$ per admitted undirected edge. Different conductances
produce different transients, correlations, noise spectra, and relaxation
rates. A stable state is therefore a constraint on a law, not generally a
selector of the law.

Second, primitive canonical thermalization on a **closed same carrier** is
incompatible with exact conservation of a nonconstant lower-bounded total
energy. Let $(\Phi_t)_{t\geq0}$ be any finite-dimensional positive
trace-preserving semigroup and let $H$ have ground energy $E_0$. If

$$
\operatorname{Tr}[H\Phi_t(\rho)]
=
\operatorname{Tr}[H\rho]
\quad
\text{for every state $\rho$ and every $t$},
\tag{2}
$$

then every state initially supported in the ground sector remains in that
sector. Consequently $\Phi_t$ cannot drive every state to the faithful Gibbs
state $e^{-\beta H}/Z$ at finite $\beta$ when $H$ has an excited sector. In
fact, the invariant ground-state face contains a stationary state, so the
faithful Gibbs state cannot be the unique stationary state.

This theorem needs positivity but not complete positivity, detailed balance,
or a Lindblad presentation. It is a carrier-accounting result: canonical
thermalization of a subsystem is compatible with exact conservation only
when the exchanged energy is carried by something else—an explicit bath,
reference, boundary flux, or larger closed system. On that enlarged carrier,
the total law may conserve energy while only the reduced subsystem
thermalizes.

The resulting disposition is

$$
\boxed{
\begin{gathered}
\text{HYBRID DETAILED-BALANCE THERMALIZERS: CONSTRUCTIBLE,}\\
\text{STATIONARY GIBBS STATE: DOES NOT SELECT RATES OR MECHANISMS,}\\
\text{EXACT SAME-CARRIER CONSERVATION + PRIMITIVE FINITE-$\beta$ THERMALIZATION: INCOMPATIBLE,}\\
\text{VACUUM INVARIANCE: CONSISTENT BUT NONSELECTING,}\\
\text{CLOSED-SYSTEM BATH/REFERENCE/BOUNDARY CARRIER: MUST BE EXPLICIT,}\\
\text{COVARIANT NON-MARKOVIAN GRAVITY AND INDIVISIBLE WHOLE-PROCESS LAWS: UNTESTED.}
\end{gathered}}
\tag{3}
$$

The author-side ceiling is

$$
\boxed{
\text{BCG-L2 — DETAILED-BALANCE NONSELECTION AND CLOSED-CARRIER OBSTRUCTION.}
\tag{4}
$$

This is not a no-go theorem against CP-CQ gravity, classical gravity,
thermalization, or Barandes-style indivisible stochastic laws. It rules out
one proposed shortcut: a canonical stationary state plus detailed balance
cannot, by themselves, choose a fundamental closed-system gravity law while
also supplying exact same-carrier conservation.

---

## 1. Binding scope and honesty rules

1. The exact theorems are finite-dimensional.
2. The conserved observable in the closed-carrier theorem is nonconstant and
   bounded below.
3. Conservation means Equation (2) for every admitted state, not merely zero
   drift in one stationary state or approximate conservation on one run.
4. Primitive thermalization means convergence of every initial state to one
   faithful stationary state. The uniqueness corollary is stated separately.
5. A finite-temperature Gibbs state is faithful in finite dimension.
6. Vacuum **invariance**, vacuum **attraction**, finite-temperature
   equilibration, and metastability are distinct claims.
7. The classical detailed-balance theorem assumes a finite continuous-time
   Markov generator. Its conductance parameterization is exact at that scope.
8. The positive-semigroup theorem does not assume Markov divisibility through
   microscopic happenings; it applies only if a time-indexed positive
   semigroup is claimed.
9. No theorem is extrapolated to an unbounded Hamiltonian without domain and
   spectral control.
10. No global positive energy is assumed to exist in arbitrary general-
    relativistic spacetimes.
11. A Hamiltonian constraint $H\approx0$ is not silently treated as an
    ordinary positive global energy.
12. Local covariant conservation, boundary-charge conservation, and global
    Hamiltonian conservation are kept distinct.
13. Quantum detailed balance is not assumed to be a fundamental arrow of
    time.
14. A KMS state requires a supplied automorphism flow and state; it is not a
    source of either by definition.
15. A Stinespring or bipartite embedding proves representability, not the
    material reality or state of the enlarged carrier.
16. An external bath is legitimate in an effective laboratory theory. It is
    incomplete as the outside of a purported fundamental law of the universe.
17. Microcanonical or fixed-charge relaxation is not ruled out.
18. Relational, non-Markovian, or all-at-once laws may evade the semigroup
    premise, but must reconstruct conservation and the reduced equilibrium
    rather than inherit them.
19. MG0 remains a discriminator preflight. It may not select an ontology
    before distinct complete matter laws make different gravity-sensitive
    predictions.
20. No official model, pin, review, Paper 04B parent, Paper 05, Paper 06/07,
    apparatus, or successor follows.

---

## 2. Exact dependencies and primary-source receipts

The direct repository dependencies are:

| artifact | exact role | inherited ceiling |
|---|---|---|
| `v17_mg0_postquantum_classical_gravity_family_pre_authorization_readiness_audit.md` | separates the CP-CQ theorem class, members, constraints, scattering, and dilation controls | CQG-L2 |
| `v17_mg0_cpcq_kernel_selection_and_joint_closure_feasibility_gate.md` | parameterizes the weak-field CP kernel freedom and identifies stable balance as a possible lever | KSG-L2 |
| `v17_mg0_common_matter_geometry_contract.md` | types the future common-law and conservation duties | no result |
| `v17_mg0_selector_controls_and_benchmark.md` | supplies hostile carrier, noise, and conservation controls | no result |

The two direct dependency hashes at construction time are:

```text
6607ef80595962de797aca6c5ac04b6073630e73e7f0e640aae03a555f20bf65  v17_mg0_postquantum_classical_gravity_family_pre_authorization_readiness_audit.md
76f58d121b3faaa489e2e486270b8f08b0561e6d66a6a4715a2910dea6322149  v17_mg0_cpcq_kernel_selection_and_joint_closure_feasibility_gate.md
```

Six additional exact-version primary sources were downloaded to temporary
storage, converted to text, and read directly.

| source | exact version | bytes | SHA-256 | role and ceiling |
|---|---:|---:|---|---|
| Adrián A. Budini, [*Hybrid quantum-classical dynamics with stationary thermal states*](https://arxiv.org/abs/2604.02484v2) | `2604.02484v2` | 569430 | `91ad6b52239844c2bc21b1c0d6e02b4ea76f17e6e410282f6c82d210e82bf146` | hybrid canonical states and detailed-balance Lindblad families; finite/open-system construction, not gravity closure |
| Brandão, Horodecki, Oppenheim, Renes, and Spekkens, [*The Resource Theory of Quantum States Out of Thermal Equilibrium*](https://arxiv.org/abs/1111.3882v3) | `1111.3882v3` | 463786 | `ac35cd8390596ee2c380ab8d4c1e2772c94ac6e2dd8c4201f645441f5ec481be` | energy-preserving transformations plus an explicit thermal bath; subsystem thermodynamics, not closed-universe dynamics |
| Tupkary, Dhar, Kulkarni, and Purkayastha, [*Searching for Lindbladians obeying local conservation laws and showing thermalization*](https://arxiv.org/abs/2301.02146v2) | `2301.02146v2` | 2309858 | `b4e9d440248cdcecf3c7373d24e7627de18f87920949503b49e4cfc67e1a5b0c` | local conservation and thermalization for a system partly coupled to a bath; not exact same-carrier global conservation |
| Victor V. Albert and Liang Jiang, [*Symmetries and conserved quantities in Lindblad master equations*](https://arxiv.org/abs/1310.1523v2) | `1310.1523v2` | 1190933 | `64e1434b4bb68a046bd543e1ad4e4db4ad66d75b11adf6670fe076912d17d687` | steady-state/conserved-observable structure; no gravity or hybrid ontology claim |
| Franco Fagnola and Federico Girotti, [*Irreducibility of Quantum Markov Semigroups, uniqueness of invariant states and related properties*](https://arxiv.org/abs/2512.11517v1) | `2512.11517v1` | 468580 | `1dd943d6380ecedb4633b9f5e55a43839e655d7d4029446a74e3fbf335c4b1c1` | equivalence of irreducibility, primitivity, and faithful relaxation under stated hypotheses; prior-art boundary for the finite corollary below |
| Gough, Ratiu, and Smolyanov, [*Noether's Theorem for Dissipative Quantum Dynamical Semigroups*](https://arxiv.org/abs/1410.7711v1) | `1410.7711v1` | 144017 | `0417c0d80f554081d9f125764d284a7ac3b3328ef8bb7c2a64e48fb9cf63ca63` | constants as Heisenberg fixed points and nontrivial constants versus unique relaxation; prior art, not a gravity theorem |

The inherited exact sources remain in the two dependency ledgers. In
particular:

- Oppenheim and Reznik establish that relational Lindblad constructions can
  reconcile some conservation and locality duties without choosing rates;
- Hotta, Murk, and Terno show both a quantum-channel embedding and an explicit
  symmetry-without-conservation control;
- the canonical and covariant CP-CQ gravity papers do not yet close one common
  nonlinear matter-coupled member; and
- the weak-field CP trade-off constrains but does not select the kernel.

No review article is used to enlarge a primary claim.

The semigroup facts in Section 7 are not presented as a new general theory of
quantum Markov semigroups. Fagnola--Girotti and
Gough--Ratiu--Smolyanov place irreducibility, faithful relaxation, fixed-point
algebras, and conserved observables in the established literature. The
contribution here is the elementary lower-bounded ground-face proof and its
strict carrier-accounting use inside the frozen MG0 question.

---

## 3. Four different meanings of “stable vacuum”

The phrase must be split before it can constrain a theory.

### 3.1 Vacuum invariance

For a state $\rho_0$,

$$
\Phi_t(\rho_0)=\rho_0
\quad\text{for every }t\geq0.
\tag{5}
$$

This only says that the vacuum does not spontaneously leave itself.

### 3.2 Vacuum attraction

For every admitted initial state,

$$
\lim_{t\to\infty}\Phi_t(\rho)=\rho_0.
\tag{6}
$$

This is a dissipative preparation claim. If nonvacuum states lose energy, the
recipient of that energy must be represented in a closed theory.

### 3.3 Faithful thermal equilibrium

At finite inverse temperature $\beta$,

$$
\rho_\beta=\frac{e^{-\beta H}}{Z_\beta}
\tag{7}
$$

has support on every finite-energy sector in finite dimension. Making it the
unique attractor erases initial energy information from the reduced carrier.

### 3.4 Constraint-sector or microcanonical equilibrium

A closed total system can remain inside a fixed charge sector,

$$
\rho(t)=P_q\rho(t)P_q,
\tag{8}
$$

while subsystems approach canonical-looking marginals. This does not require
the total closed system to mix across different total energies.

Equations (5)--(8) are not interchangeable. The CP-CQ gravity audit requires
a nonexciting vacuum and controlled fluctuations. It does not thereby receive
an external heat bath, a temperature, a preferred time flow, or unique
thermalizing rates.

---

## 4. Detailed-balance conductance theorem

Let $X=\{1,\ldots,n\}$ and let $\pi_i>0$ with $\sum_i\pi_i=1$. Use the column
convention

$$
\dot p_i=\sum_j K_{ij}p_j,
\qquad
K_{ij}=k_{i\leftarrow j}\geq0\quad(i\ne j),
\qquad
K_{jj}=-\sum_{i\ne j}k_{i\leftarrow j}.
\tag{9}
$$

Detailed balance with respect to $\pi$ is

$$
\pi_j k_{i\leftarrow j}
=
\pi_i k_{j\leftarrow i}.
\tag{10}
$$

### Theorem B1 — reversible-generator parameterization

Equation (10) holds if and only if there is a symmetric family

$$
c_{ij}=c_{ji}\geq0
\tag{11}
$$

such that Equation (1) holds on every admitted edge.

#### Proof

Given a detailed-balance generator, set

$$
c_{ij}=\pi_j k_{i\leftarrow j}.
\tag{12}
$$

Equation (10) makes $c_{ij}=c_{ji}$. Conversely, any symmetric nonnegative
$c$ inserted into Equation (1) satisfies Equation (10). The diagonal entries
in Equation (9) then ensure normalization. Summing by pairs proves
$K\pi=0$. $\square$

### Corollary B1.1 — stationary-state nonselection

Fixing $\pi$, detailed balance, and an edge graph leaves one nonnegative
conductance per undirected edge. If the positive-conductance graph is
connected, $\pi$ is the unique stationary distribution, but the generator is
still not unique.

### Corollary B1.2 — relationally observable freedom

Multiplying every $c_{ij}$ by a common constant changes the relaxation scale.
Changing conductance ratios changes route probabilities and correlation
profiles even after a global time rescaling. Thus the freedom is not merely a
choice of time units whenever at least two competing routes are physically
readable.

### Relation to the new hybrid source

Budini's hybrid thermal generators impose relations of the form

$$
\frac{\gamma_{ij}}{\gamma_{ji}}
=e^{-\beta(\varepsilon_i-\varepsilon_j)}.
\tag{13}
$$

The source also explicitly permits positive combinations of generators that
each satisfy detailed balance and exhibits multiple different mechanisms
with the same stationary hybrid thermal state. This is a positive
construction of equilibrium, not a rate-selection theorem.

---

## 5. Exact rational control

Take energies

$$
(E_0,E_1,E_2)=(0,1,2)
\tag{14}
$$

and the Gibbs weights for $e^{-\beta}=1/2$,

$$
\pi=\left(\frac47,\frac27,\frac17\right).
\tag{15}
$$

Choose conductances

$$
c_{01}=\frac1{14},
\qquad
c_{12}=\frac1{21},
\qquad
c_{02}=\frac1{28}.
\tag{16}
$$

Equations (1) and (9) give the exact generator

$$
K=
\begin{pmatrix}
-3/16 & 1/4 & 1/4\\
1/8 & -5/12 & 1/3\\
1/16 & 1/6 & -7/12
\end{pmatrix}.
\tag{17}
$$

Direct rational arithmetic gives

$$
K\pi=0,
\qquad
E^TK=left(\frac14,-\frac1{12},-\frac56\right).
\tag{18}
$$

The same law is exactly Gibbs-stationary and detailed-balanced, yet it does
not conserve the energy expectation for arbitrary initial distributions.
Scaling or changing the conductances preserves the equilibrium law while
changing the dynamics.

The reconstruction was checked with exact `Rational` arithmetic in Ruby. No
floating-point or fitted quantity enters Equation (18).

---

## 6. Classical same-carrier conservation theorem

Let the finite states carry energies $E_i$. Exact energy conservation for
every distribution is

$$
E^TK=0.
\tag{19}
$$

### Theorem B2 — detailed balance plus exact conservation permits only isoenergetic edges

Assume full-support detailed balance and Equation (19). Then

$$
k_{i\leftarrow j}>0
\quad\Longrightarrow\quad
E_i=E_j.
\tag{20}
$$

#### Proof

Let $G_0$ be the states with minimum energy $E_0$. For any $j\in G_0$,
Equation (19) gives

$$
0
=
\sum_{i\ne j}k_{i\leftarrow j}(E_i-E_0).
\tag{21}
$$

Every term is nonnegative, so every transition from $j$ to a higher-energy
state has zero rate. Full-support detailed balance then sets every reverse
transition into $j$ to zero. Remove the minimum-energy sector and repeat the
argument on the remaining finite energy levels. Only transitions within an
equal-energy sector survive. $\square$

### Corollary B2.1

If the energy takes more than one value, a detailed-balanced generator that
conserves that energy for every state cannot be irreducible across the whole
state space and cannot canonically thermalize between energy sectors.

### Physical reading

A canonical Markov thermalizer describes energy exchange with a carrier not
included in the reduced state. Calling the reduced state “the closed
universe” removes the place where that energy goes.

---

## 7. Positive-semigroup closed-carrier theorem

The classical proof is not an artifact of choosing jump coordinates.

Let $\mathcal A$ be a finite-dimensional matrix algebra or finite hybrid
classical--quantum block algebra. Let $(\Phi_t)_{t\geq0}$ be a positive,
trace-preserving semigroup on its state space. Complete positivity is allowed
but not required.

Let $H=H^\dagger$ be a nonconstant observable with minimum eigenvalue $E_0$,
and let $P_0$ project onto its ground sector.

### Theorem B3 — ground-face invariance

If Equation (2) holds, then

$$
\rho=P_0\rho P_0
\quad\Longrightarrow\quad
\Phi_t(\rho)=P_0\Phi_t(\rho)P_0
\quad\text{for every }t\geq0.
\tag{22}
$$

#### Proof

Set $A=H-E_0I\succeq0$. A ground-supported state has
$\operatorname{Tr}(A\rho)=0$. Conservation gives

$$
\operatorname{Tr}[A\Phi_t(\rho)]=0.
\tag{23}
$$

Both $A$ and $\Phi_t(\rho)$ are positive. Therefore
$A^{1/2}\Phi_t(\rho)A^{1/2}$ is positive with zero trace and hence vanishes.
The support of $\Phi_t(\rho)$ lies in $\ker A=\operatorname{ran}P_0$.
$\square$

### Corollary B3.1 — no primitive faithful Gibbs attractor

If $H$ has an excited sector and $\beta<\infty$, then

$$
\rho_\beta=\frac{e^{-\beta H}}{Z_\beta}
\tag{24}
$$

has support outside $P_0$. Equation (22) prevents a ground-supported initial
state from converging to $\rho_\beta$. The semigroup therefore cannot be
primitive with faithful Gibbs attractor $\rho_\beta$.

### Corollary B3.2 — no unique faithful Gibbs stationary state

The ground-state face is nonempty, compact, convex, and invariant. A
finite-dimensional continuous positive semigroup has a stationary state in
that face, obtained for example from a convergent subsequence of Cesàro time
averages. It is distinct from the faithful Gibbs state. Therefore the latter
cannot be the unique stationary state.

### Corollary B3.3 — conserved charges retain information

Exact conservation of a nontrivial lower-bounded charge partitions the state
space into invariant faces or sectors. A unique stationary state independent
of the initial charge is impossible on the same carrier.

---

## 8. Three qubit controls

Let

$$
H=\Delta|1\rangle\langle1|,
\qquad
\Delta>0.
\tag{25}
$$

### 8.1 Dephasing control

For

$$
\mathcal L(\rho)=\gamma(Z\rho Z-\rho),
\tag{26}
$$

$\mathcal L^\dagger(H)=0$. Every diagonal population is retained. Every Gibbs
state is stationary, but none is selected and no population thermalization
occurs.

### 8.2 Finite-temperature amplitude-damping control

Let

$$
\mathcal L(\rho)
=
\gamma_\downarrow\mathcal D[\sigma_-](\rho)
+
\gamma_\uparrow\mathcal D[\sigma_+](\rho),
\qquad
\frac{\gamma_\uparrow}{\gamma_\downarrow}=e^{-\beta\Delta}.
\tag{27}
$$

This has the finite-temperature Gibbs state as its unique attractor when both
rates are positive, but

$$
\mathcal L^\dagger(H)
=
\Delta\left(
\gamma_\uparrow|0\rangle\langle0|
-
\gamma_\downarrow|1\rangle\langle1|
\right)
\ne0.
\tag{28}
$$

The reduced qubit exchanges energy with an implicit environment.

### 8.3 Enlarged-carrier control

Let a system $S$ interact with a bath $B$ through a unitary satisfying

$$
[U,H_S+H_B]=0.
\tag{29}
$$

The reduced state of $S$ may thermalize while the total energy is conserved.
The physical input now includes at least $B$, its state, its spectrum, its
coupling, and the approximation by which a Markov semigroup emerges. This is
the standard honest escape and exactly why the carrier cannot be omitted.

---

## 9. What the result says about CP-CQ gravity

### 9.1 The stable state does not choose the kernel

The CP-CQ kernel gate left a positive decoherence function and diffusion slack
at fixed mean response. Requiring a stationary state may relate drift and
diffusion, but it cannot generally determine every symmetric conductance,
spectral density, rate, or memory kernel. Budini's exact hybrid construction
confirms this nonuniqueness rather than closing it.

### 9.2 A bath cannot sit outside a fundamental universe

For an effective laboratory or cosmological open subsystem, a bath is
legitimate. For a fundamental common matter--geometry law, it must be part of
the common carrier or appear as an explicit boundary condition. Otherwise
friction, diffusion, and equilibration violate the programme's conservation
and declared-input walls.

### 9.3 Canonical equilibrium is likely reduced, not root-level

The physically coherent closed-system route is

$$
\boxed{
\begin{aligned}
&\text{one closed matter--geometry--reference carrier}\
&\quad+\text{exact constraint/charge or boundary-flux balance}\
&\quad+\text{microcanonical or sector-preserving whole-process law}\
&\qquad\Downarrow\ \text{controlled reduction}\
&\text{subsystem KMS/detailed balance/canonical behavior}.
\end{aligned}}
\tag{30}
$$

Equation (30) is an admissibility target, not a constructed theory.

### 9.4 The covariant family remains untested

The covariant CP-CQ path-integral family is not a finite Markov semigroup and
does not automatically possess a global lower-bounded Hamiltonian. Theorem B3
therefore does not refute it. That family still owes:

1. a physical tensor-kernel selector;
2. nonlinear matter-coupled constraint closure;
3. local and boundary-flux conservation;
4. a controlled vacuum/state prescription;
5. readers and one-run actuality where claimed;
6. a fixed-geometry QFT limit;
7. a classical GR limit; and
8. held-out empirical transfer.

---

## 10. General-relativistic translation firewall

The following objects must not be merged.

| object | exact duty | why Theorem B3 may not apply directly |
|---|---|---|
| ADM Hamiltonian | generator plus constraints and boundary terms | physical Hamiltonian may reduce to a boundary charge |
| Hamiltonian constraint | vanishes on physical states | not a nonconstant positive energy on the physical space |
| local stress-energy conservation | $\nabla_\mu T^{\mu\nu}=0$ or joint extension | not a single global bounded charge in arbitrary spacetime |
| asymptotic energy | boundary charge under asymptotic conditions | requires declared boundary class |
| KMS state | equilibrium relative to an automorphism flow | flow and state are supplied structure |
| cosmological state | contingent boundary/initial condition | not a universal dynamical selector |

If the total Hamiltonian is a constraint equal to zero, exact conservation is
trivial on the physical surface and cannot choose the stochastic kernel. If a
positive asymptotic charge exists, its boundary carrier and flux must be
included. If neither exists, “energy conservation” must be replaced by the
actual local constraint and balance equations before any stability theorem is
claimed.

---

## 11. Barandes-facing consequence

The result neither promotes nor refutes an indivisible stochastic ontology.

A Barandes-style whole-process law may avoid a microscopic Markov semigroup,
external time, and intermediate classical trajectories. That is a genuine
logical opening. It does not remove the physical duties:

1. identify the contingent configuration or boundary state;
2. define the complete indivisible law without importing the quantum process;
3. derive the conserved relational charge or boundary balance;
4. identify the carrier of energy and momentum exchange;
5. derive why a reduced subsystem looks KMS or detailed-balanced;
6. distinguish a stable actual record from a stationary predictive state; and
7. predict a held-out complete process.

Theorem B3 says that simply replacing a quantum thermal semigroup by an
ordinary-positive stochastic semigroup does not solve the closed-system
problem. The missing physics is the common carrier and its whole-process
balance law, not the sign of the probabilities.

---

## 12. Hostile controls

### 12.1 State-versus-law attacks

1. A Gibbs state is supplied and called a derived law.
2. The inverse temperature $\beta$ is fitted to the scored data.
3. A KMS flow is supplied and then called emergent time.
4. A stationary distribution is used to infer transition rates.
5. A vacuum vector is used to infer the interacting Hamiltonian.
6. Cosmological boundary data are called universal couplings.

### 12.2 Conservation attacks

7. Conservation is checked only in the stationary state.
8. Mean conservation on one preparation is called operator conservation.
9. Symmetry covariance is substituted for $\mathcal L^\dagger Q=0$.
10. System energy is confused with system-plus-bath energy.
11. Missing energy is assigned to an unrecorded noise field.
12. Boundary flux is omitted from a global charge.
13. A Hamiltonian constraint is treated as an ordinary positive energy.
14. Local first-moment balance hides higher-moment growth.
15. Conservation is restored only after fitting a friction term.

### 12.3 Equilibrium attacks

16. Vacuum invariance is called vacuum attraction.
17. Metastability is called a stationary state.
18. Zero-temperature damping is called closed-system conservation.
19. A canonical law is imposed on a closed fixed-energy universe.
20. Detailed balance ratios are used to hide free conductances.
21. A common rescaling is dismissed while relative edge rates remain free.
22. A disconnected generator is called primitive.
23. Degenerate-sector mixing is called full thermalization.

### 12.4 Carrier and representation attacks

24. A Stinespring ancilla is declared physically real without a state or
    coupling provenance.
25. A bath is hidden in a Lindblad coefficient.
26. An external laboratory clock is hidden in semigroup time.
27. A Markov approximation is promoted to an exact universal law.
28. The classical register in a bipartite embedding is called a discovered
    ontology.
29. A quantum dilation is called a native positive source.
30. A target spectral density is inserted as an “environment.”

### 12.5 Scope attacks

31. The finite theorem is extrapolated to unbounded QFT.
32. A lower-bounded spectrum is assumed for an indefinite gravitational
    constraint.
33. The Markov theorem is applied to an indivisible whole-process law.
34. Local conservation in a bath-coupled subsystem is called total closed-
    universe conservation.
35. One CP-CQ member donates its stable state to a different covariant member.
36. A no-go at fixed geometry is called a theorem about all quantum gravity.

---

## 13. Escape taxonomy and exact new debts

| escape | what it legitimately changes | new debt |
|---|---|---|
| explicit thermal bath | makes subsystem thermalization compatible with total conservation | bath state, spectrum, coupling, size, backreaction, and ultimate closure |
| finite reference or work store | carries exchanged charge relationally | reference degradation, records, and conservation proof |
| microcanonical total law | preserves total energy sector | derive canonical subsystem behavior and typicality without answer import |
| boundary-flux law | permits regional nonconservation with global balance | define boundaries, fluxes, gluing, and covariance |
| non-Markovian memory | removes semigroup approximation | physical memory carrier and complete composition law |
| all-at-once/indivisible law | removes intermediate divisibility and possibly external time | derive operational arrows, balance, and reduced equilibrium |
| exact conservation violation | retains a primitive thermalizer as fundamental | quantitative violation, experimental bounds, and gravity compatibility |
| no lower-bounded charge | evades the ground-face proof | separate stability, vacuum, and runaway control |

None is a free repair. Each changes the physical object and must be declared
before evaluation.

---

## 14. Outcome ladder

### BCG-L0 — equilibrium vocabulary only

“Stable,” “thermal,” “vacuum,” and “conserved” are not assigned distinct
typed equations.

### BCG-L1 — stationary hybrid class reconstructed

A primary-source hybrid thermal family and its detailed-balance conditions
are reconstructed, but rate selection and closed-system conservation are not
tested.

### BCG-L2 — balance nonselection and carrier obstruction

The conductance freedom is parameterized, exact finite controls are supplied,
and same-carrier conservation is proved incompatible with primitive faithful
thermalization for a nonconstant lower-bounded charge.

**Current level.**

### BCG-L3 — explicit closed carrier

One model prints the bath/reference/boundary carrier, total state, conserved
charges, and an exact joint law without target leakage.

### BCG-L4 — reduced balance derived

The same model derives the subsystem stationary/KMS/detailed-balance law from
its closed microcanonical or constraint-preserving dynamics.

### BCG-L5 — covariant matter--geometry closure

The same member has nonlinear constraints, local and boundary conservation,
interacting matter, stable vacuum, complete readers, and both QFT and GR
limits.

### BCG-L6 — prospective empirical readiness

Parameters are independently fixed and the member makes a complete held-out
gravity-sensitive prediction against a genuinely different complete matter
law.

No official rung follows from this author-side ladder.

---

## 15. Maximum legitimate claim

The strongest justified statement is:

> Finite hybrid quantum--classical detailed-balance semigroups with canonical
> stationary states exist. The stationary state and detailed-balance relation
> do not select a unique generator: they leave symmetric edge conductances,
> mechanisms, and rate scales free. More generally, a finite-dimensional
> positive trace-preserving semigroup that exactly conserves a nonconstant
> lower-bounded observable on the same carrier preserves its ground-state
> face. It therefore cannot have a faithful finite-temperature Gibbs state as
> a primitive attractor or unique stationary state. Canonical thermalization
> with exact conservation is coherent only as reduced dynamics of an enlarged
> carrier, or after relaxing one of the stated assumptions.

The following claims are barred:

1. detailed balance is impossible in CP-CQ dynamics;
2. CP-CQ gravity is impossible;
3. gravity must be quantized;
4. every stable vacuum requires an external thermal bath;
5. closed systems cannot equilibrate within fixed charge sectors;
6. a covariant whole-process law is ruled out;
7. Barandes's ontology is refuted;
8. conservation always requires a global positive Hamiltonian in GR;
9. Budini's hybrid thermal construction is defective; or
10. a common matter--geometry law has been constructed.

---

## 16. Routing decision

```text
HYBRID THERMAL SEMIGROUPS:             CONSTRUCTIBLE
DETAILED-BALANCE RATE RATIOS:          FIXED BY GIBBS WEIGHTS
SYMMETRIC CONDUCTANCES/RATE SCALES:    FREE
STATIONARY STATE AS LAW SELECTOR:      FAILS
VACUUM INVARIANCE:                     CONSISTENT / NONSELECTING
VACUUM ATTRACTION ON SAME CLOSED CARRIER: CONSERVATION OBSTRUCTION
FINITE-BETA PRIMITIVE THERMALIZATION:  REQUIRES ENERGY-EXCHANGE CARRIER
MICROCANONICAL/SECTOR EQUILIBRATION:    OPEN AND NOT REFUTED
COVARIANT NON-MARKOVIAN CP-CQ MEMBER:  UNTESTED
INDIVISIBLE WHOLE-PROCESS ESCAPE:      LOGICALLY OPEN / BALANCE LAW OWED
AUTHOR-SIDE CEILING:                   BCG-L2
FREEZE-READY GRAVITY MEMBER:           NONE
OFFICIAL MG0 AUTHORITY:                NONE
ONTOLOGY OR QUANTUM-GRAVITY VERDICT:   NONE
```

The next admissible physics question is not “which temperature should be
inserted?” It is whether one source-fixed closed matter--geometry--reference
carrier can derive both exact relational balance and the reduced
equilibrium/noise law. That question remains downstream of complete matter
laws and requires no model construction here.
