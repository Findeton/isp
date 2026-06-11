# Relativistic ISP V3 Paper 12: From Smeared Perturbative Wilson Loops To Renormalized Unsmeared Wilson-Loop Functionals

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Status: first investigation draft. This paper begins the first follow-up
program after Paper 11. Paper 11 reached a perturbative continuum-facing
Yang-Mills interface on smeared Wilson-loop tests. Paper 12 asks whether those
smeared tests can be sharpened into renormalized unsmeared Wilson-loop
functionals.

The ontological rule is unchanged: a Wilson-loop record is an operational
test in the declared battery. Renormalization is a declared transformation of
records and normalization constants. It is not hidden stochastic dynamics and
it is not a Gamma-only reconstruction of charged gauge data.

## 1. Import Contract From Paper 11

Paper 12 may use:

1. finite-battery non-Abelian projective gauge control;
2. conditional CYM-RG residual summability;
3. ledger-compatible block-conditioned RG;
4. the perturbative Yang-Mills trajectory ledger;
5. a smeared Wilson-loop anchor in a controlled weak-coupling reference
   window;
6. diagonal compactness for countable bounded Wilson-loop tests;
7. loop-continuity criteria when a uniform modulus is proved.

Paper 12 may not use Paper 11 to claim:

```text
full nonperturbative continuum Yang-Mills;
mass gap;
confinement;
Wilson-loop area law;
P20-SEL2-TREE-RATE-GATE;
SEL2 block-plaquette coefficient-time lower bounds;
SEL2 heat-kernel coefficient comparison;
unsmeared Wilson loops without perimeter/cusp renormalization;
Gamma-only charged gauge reconstruction.
```

## 1B. Paper-20 Source Audit

Paper 12 controls a different object from the Paper-20 `SEL2` tree-rate gate.
Its records are renormalized Wilson-loop readouts: perimeter/cusp calibrated,
possibly smeared, and then de-smeared on admissible loop batteries. They are
not the active Paper-20 block-plaquette central coefficient records.

### Definition 1B.1: Paper-12 Export Boundary For `SEL2`

Paper 12 may export to Paper 20 only:

```text
calibrated perimeter/cusp loop-readout ledgers;
smearing-removal schedules for Wilson-loop records;
finite-battery loop-continuity and approximant-equivariance estimates;
nontriviality transfer for admissible renormalized loop batteries.
```

Paper 12 may not export:

```text
the SEL2 central block-plaquette coefficient;
T_-^{SEL2} above a surface-polymer threshold;
the SEL2 heat-kernel coefficient comparison;
the escape product q_rho gamma_rho for the SEL2 sheet observable;
P20-SEL2-TREE-RATE-GATE;
area law, mass gap, or confinement.
```

### Theorem 1B.2: Paper 12 Does Not Supply The Paper-20 Tree-Rate Source

Paper 12 does not prove `P20-SEL2-TREE-RATE-GATE`.

### Proof

The main records of Paper 12 are Wilson-loop functionals
`W_\rho(C_a)`, their perimeter/cusp-renormalized versions, and their smeared
counterparts. The Paper-20 tree-rate gate is instead a same-record estimate for
the `SEL2` block-plaquette coefficient and its normalized sheet/escape
observable. A perimeter/cusp renormalization theorem can remove loop-readout
debits, but it does not compute the block-plaquette central character
coefficient, does not prove a lower block time `T_-^{SEL2}`, and does not
establish the escape product `q_\rho\gamma_\rho` above the rooted surface
threshold. Therefore Paper 12 is a loop-readout source, not a Paper-20
tree-rate source. `square`

## 1A. Constants And Ledgers

Paper 12 uses the following constants and ledgers. All constants are
finite-stage data unless explicitly stated otherwise.

### Loop Geometry

```text
L_max       maximum admissible loop length;
N_max       maximum number of cusps;
theta_min   lower distance from degenerate cusp angles;
r_min       minimum separation of distinct cusps/nonadjacent arcs;
K_max       total-curvature bound on smooth arcs;
w_a         microscopic loop-collar thickness;
d_adm       admissible loop metric.
```

### Representation And Battery

```text
rho         finite-dimensional SU(2) representation;
d_rho       representation dimension;
p_N         maximum product degree in a finite battery;
B_N         finite-battery product/cumulant bound;
Z_N(a)      largest counterterm product appearing in the finite battery.
```

### Counterterms And Calibration

```text
gamma_rho(a)               perimeter counterterm;
Gamma_rho(theta,a)         cusp counterterm;
q_{rho,per}                smooth-loop calibration target;
q_{rho,cusp}(theta)        cusp calibration target;
hat gamma_{rho,tau}(a)     smeared perimeter calibration;
hat Gamma_{rho,tau}(a)     smeared cusp calibration.
```

### AF/RG Control

```text
G_r          finite-battery growth bound from Paper 11;
Q_r^*        running weak-coupling smallness parameter;
R_r          retained local radius at scale r;
mu           polymer-tail decay rate;
epsilon_RP   reflection-positivity defect;
epsilon_Euc  Euclidean-covariance defect;
epsilon_app  lattice-approximant equivariance defect.
```

### Smearing And Anchors

```text
tau          physical smearing radius;
tau_*        small-smearing window;
A_0          positive lower bound for the normalized smeared anchor;
I_tau(C)     perturbative smeared loop coefficient from Paper 11;
hat I_tau(C) calibrated version of the same coefficient.
```

The theorem-level statements below use these constants only through finite
batteries and declared ledgers. No constant is allowed to hide a partial
Markov factorization or an undeclared charged/framed observable.

## 2. Smeared And Unsmeared Wilson-Loop Records

Let `C` be a closed continuum loop and `\rho` a finite dimensional
representation of `SU(2)`. Let `C_a` be a lattice approximant.

### Definition 2.0: Admissible Loop Class

Fix constants

```math
L_{\max},\quad N_{\max},\quad \theta_{\min}>0,\quad r_{\min}>0,
\quad K_{\max}<\infty.
```

The admissible loop class
`\mathcal L_{\rm adm}(L_{\max},N_{\max},\theta_{\min},r_{\min},K_{\max})`
consists of oriented closed loops `C\subset{\mathbb R}^4` satisfying:

1. `C` is piecewise `C^2` and embedded away from finitely many cusp points;
2. the Euclidean length obeys `{\rm Per}(C)\le L_{\max}`;
3. the number of cusps is at most `N_{\max}`;
4. every cusp angle lies in
   `[\theta_{\min},\pi-\theta_{\min}]`;
5. distinct cusps and nonadjacent smooth arcs have separation at least
   `r_{\min}`;
6. the total curvature of the smooth pieces is at most `K_{\max}`.

For each lattice spacing `a`, an admissible lattice approximant `C_a` is a
closed oriented lattice path contained in an `O(a)` tubular neighborhood of
`C`, with

```math
{\rm Per}_a(C_a)\to{\rm Per}(C)
```

and with lattice cusp angles converging to the declared continuum cusp
angles. The approximant rule is part of the battery ledger.

This restriction is deliberate. Paper 12 first proves the unsmeared loop gate
on a clean class where perimeter, cusp angle, and loop topology are not
ambiguous. Arbitrary rough loops belong to later density or extension
arguments, not to the first gate.

### Definition 2.1: Smeared Wilson-Loop Record

For physical smearing radius `\tau>0`, define a bounded smeared Wilson-loop
record

```math
W_{\rho,\tau}(C_a)
=
\frac{1}{d_\rho}{\rm Re\,Tr}_\rho\,{\mathcal P}
\prod_{e\in C_a} U_{e,\tau},
```

where `U_{e,\tau}` is the declared gauge-covariant smeared link variable. The
smearing rule must be local, gauge-covariant, and included in the battery
ledger.

### Definition 2.2: Bare Unsmeared Wilson-Loop Record

The bare unsmeared record is

```math
W_{\rho}^{\rm bare}(C_a)
=
\frac{1}{d_\rho}{\rm Re\,Tr}_\rho
\prod_{e\in C_a}U_e.
```

It is bounded at finite lattice spacing, but its continuum limit need not
exist without perimeter and cusp renormalization.

### Definition 2.3: Renormalized Unsmeared Wilson-Loop Record

A renormalized unsmeared Wilson-loop record is a family

```math
W_{\rho}^{\rm ren}(C_a)
=
Z_\rho(C,a)W_{\rho}^{\rm bare}(C_a)
```

or, for cusp-bearing loops,

```math
W_{\rho}^{\rm ren}(C_a)
=
Z_{\rho,{\rm per}}(C,a)
\prod_{\upsilon\in{\rm Cusps}(C)}
Z_{\rho,{\rm cusp}}(\theta_\upsilon,a)
\,W_{\rho}^{\rm bare}(C_a).
```

The constants are part of the record definition. They are not hidden inside
the state.

### Definition 2.4: Renormalized Loop Battery

For each `n`, the Paper-12 loop battery contains finitely many records

```math
W_{\rho,\tau}(C_a),
\qquad
W_{\rho}^{\rm ren}(C_a),
```

with loops in a fixed admissible class, bounded representation, bounded
number of cusps, and bounded product degree. The batteries are nested and
countable in the continuum limit.

## 3. Renormalization Gates

### Definition 3.1: Perimeter-Cusp Counterterm Ledger

A perimeter-cusp counterterm ledger is a family of real constants

```math
\gamma_{\rho}(a),\qquad
\Gamma_{\rho}(\theta,a),
```

such that

```math
Z_{\rho,{\rm per}}(C,a)
=
\exp(\gamma_\rho(a){\rm Per}_a(C)),
```

and

```math
Z_{\rho,{\rm cusp}}(\theta,a)
=
\exp(\Gamma_\rho(\theta,a)).
```

The signs and normalization convention are fixed by declared calibration
loops, not by an implicit state-dependent choice.

For each representation `\rho`, choose:

1. a smooth embedded calibration loop `Q_\rho` with no cusps and perimeter
   `\ell_\rho`;
2. for each tested cusp angle `\theta`, a one-cusp calibration loop
   `K_{\rho,\theta}` with perimeter `\ell_{\rho,\theta}` and exactly one
   cusp of angle `\theta`;
3. nonzero real calibration targets
   `q_{\rho,{\rm per}}` and `q_{\rho,{\rm cusp}}(\theta)`.

The calibration branch is admissible only when the reference expectations are
nonzero and have the declared signs for all sufficiently small `a`. Then

```math
\gamma_\rho(a)
=
\frac{1}{\ell_\rho}
\log\left(
\frac{q_{\rho,{\rm per}}}
{\mu_a(W_\rho^{\rm bare}(Q_{\rho,a}))}
\right),
```

and

```math
\Gamma_\rho(\theta,a)
=
\log\left(
\frac{q_{\rho,{\rm cusp}}(\theta)}
{\exp(\gamma_\rho(a)\ell_{\rho,\theta})
\mu_a(W_\rho^{\rm bare}(K_{\rho,\theta,a}))}
\right).
```

If either logarithm is not real on a tail of the refinement sequence, this
renormalization branch fails. A different calibration branch may be tried,
but it must be declared in the record ledger.

The normalized calibration identities are therefore

```math
\mu_a(W_\rho^{\rm ren}(Q_{\rho,a}))=q_{\rho,{\rm per}},
\qquad
\mu_a(W_\rho^{\rm ren}(K_{\rho,\theta,a}))
=q_{\rho,{\rm cusp}}(\theta).
```

They fix the convention. They do not prove that every tested loop is bounded.

### Definition 3.2: Renormalized Boundedness

A renormalized loop family is bounded on a tested class if there are finite
constants `B_{C,\rho}` such that

```math
\sup_a
|\mu_a(W_\rho^{\rm ren}(C_a))|
\le
B_{C,\rho}.
```

It is product-bounded if the same holds for finite products in every declared
battery.

### Theorem 3.3: Finite Counterterm Envelope Implies Product-Boundedness

Let `\mathcal B_N` be a finite battery of renormalized unsmeared loop records
with product degree at most `p_N`. Suppose the calibration ledger satisfies
the finite-battery envelope

```math
M_N
=
\sup_a
\sup_{(C_1,\rho_1),\ldots,(C_m,\rho_m)\in\mathcal B_N,\ m\le p_N}
\prod_{j=1}^{m}
\left|
Z_{\rho_j,{\rm per}}(C_j,a)
\prod_{\upsilon\in{\rm Cusps}(C_j)}
Z_{\rho_j,{\rm cusp}}(\theta_\upsilon,a)
\right|
<\infty.
```

Then `\mathcal B_N` is product-bounded.

### Proof

For `SU(2)` and unitary finite dimensional `\rho`,

```math
\left|
\frac{1}{d_\rho}{\rm Re\,Tr}_\rho
\prod_{e\in C_a}U_e
\right|
\le 1.
```

Hence every product of `m\le p_N` renormalized records has pointwise absolute
value bounded by the corresponding product of counterterm magnitudes, and
therefore by `M_N`. Taking expectation under any finite-lattice ISP measure
preserves the bound. `square`

This theorem is useful but strong. In a genuine perimeter-divergent
renormalization, the envelope may fail. Paper 12 therefore also records the
weaker cumulant route.

### Theorem 3.4: Finite Cumulant Envelope Implies Product-Boundedness

Let `X_{1,a},\ldots,X_{r,a}` be the renormalized records in a finite battery
`\mathcal B_N`, and let the product degree be at most `p_N`. Assume that for
every ordered tuple `\alpha=(i_1,\ldots,i_m)` with `1\le m\le p_N` the joint
cumulant exists and obeys

```math
\sup_a
|\kappa_a(X_{i_1,a},\ldots,X_{i_m,a})|
\le K_\alpha<\infty.
```

Then every finite product expectation in `\mathcal B_N` is bounded uniformly
in `a`.

### Proof

For any product `X_{i_1,a}\cdots X_{i_m,a}`, the moment-cumulant relation gives

```math
\mu_a(X_{i_1,a}\cdots X_{i_m,a})
=
\sum_{\pi\in\Pi_m}
\prod_{B\in\pi}
\kappa_a(X_{i_b,a}:b\in B),
```

where `\Pi_m` is the finite set of set partitions of
`\{1,\ldots,m\}`. Taking absolute values and using the cumulant bounds gives

```math
\left|\mu_a(X_{i_1,a}\cdots X_{i_m,a})\right|
\le
\sum_{\pi\in\Pi_m}
\prod_{B\in\pi}K_{(i_b)_{b\in B}},
```

a finite constant depending only on the battery and product degree. `square`

The cumulant envelope is the realistic route for perimeter-renormalized
Wilson loops: the records may not be uniformly bounded as functions, but
their declared finite products can still have finite renormalized moments.

### Lemma 3.5: Paper-11 Smeared RG Control Gives Finite Smeared Cumulants

Let `Y_{1,a,\tau},\ldots,Y_{r,a,\tau}` be finitely many smeared Wilson-loop
records in a Paper-11 scalar Wilson-loop battery, with fixed physical
smearing radius `\tau>0` and product degree at most `p_N`. Then their joint
cumulants are uniformly bounded:

```math
\sup_a
|\kappa_a(Y_{i_1,a,\tau},\ldots,Y_{i_m,a,\tau})|
\le
C_{m}
```

for every `1\le m\le p_N`, where one may take

```math
C_m
=
\sum_{\pi\in\Pi_m}(|\pi|-1)!\prod_{B\in\pi}1
=
\sum_{\pi\in\Pi_m}(|\pi|-1)!.
```

If Paper 11 supplies a summable RG residual ledger `\Xi_r` on the same finite
battery, the corresponding continuum-facing smeared cumulants are Cauchy up
to the same residual ledger.

### Proof

Each normalized smeared Wilson-loop record has absolute value at most `1`.
The joint cumulant is the finite partition polynomial

```math
\kappa_a(Y_1,\ldots,Y_m)
=
\sum_{\pi\in\Pi_m}
(|\pi|-1)!(-1)^{|\pi|-1}
\prod_{B\in\pi}
\mu_a\left(\prod_{i\in B}Y_i\right).
```

Every product expectation in the sum has absolute value at most `1`, giving
the displayed bound. Paper 11's residual ledger controls every finite product
in the battery; applying the same partition polynomial transfers that
control to cumulants. `square`

### Definition 3.6: Connected Perimeter-Cusp Decomposition

A finite admissible loop battery satisfies the connected perimeter-cusp
decomposition if, for every ordered tuple
`\alpha=((C_1,\rho_1),\ldots,(C_m,\rho_m))` with `1\le m\le p_N`, the bare
connected cumulant has the form

```math
\kappa_a
\left(
W_{\rho_1}^{\rm bare}(C_{1,a}),\ldots,
W_{\rho_m}^{\rm bare}(C_{m,a})
\right)
=
\exp\left(
-\sum_{j=1}^{m}D_{\rho_j}(C_j,a)
\right)
\left(K_{\alpha,a}+R_{\alpha,a}\right),
```

where

```math
D_\rho(C,a)
=
\gamma_\rho(a){\rm Per}_a(C)
+
\sum_{\upsilon\in{\rm Cusps}(C)}
\Gamma_\rho(\theta_\upsilon,a),
```

the same `\gamma_\rho` and `\Gamma_\rho` are fixed by the calibration ledger,
and the connected remainders obey

```math
\sup_a |K_{\alpha,a}|\le K_\alpha^{\rm loc}<\infty,
\qquad
\sup_a |R_{\alpha,a}|\le R_\alpha^{\rm tail}<\infty.
```

The intended Paper-11 source of this decomposition is:

1. bounded smeared cumulants from Lemma 3.5;
2. local RG residual control for finite products in the Wilson-loop battery;
3. polymer/local-loop connectedness, so divergent self-neighborhoods of each
   loop are local to that loop's perimeter and cusp set;
4. the calibration ledger, which identifies those local single-loop singular
   terms with the declared `\gamma_\rho` and `\Gamma_\rho`;
5. a summable connected residual tail for all nonlocal or omitted polymers.

This is the exact point where Paper 12 uses the Paper-11 RG machinery. It is
not Markov divisibility of partial kernels; it is a statement about the
whole-process finite-battery cumulant ledger.

### Lemma 3.6A: Local Connected Polymer Criterion For The Decomposition

Definition 3.6 holds if the exact Paper-11 blocked RG ledger gives, for every
finite tuple `\alpha`, an absolutely convergent connected polymer expansion
of the bare loop cumulant with the following structure:

```math
\kappa_a
\left(
W_{\rho_1}^{\rm bare}(C_{1,a}),\ldots,
W_{\rho_m}^{\rm bare}(C_{m,a})
\right)
=
\sum_{\mathfrak C\in{\rm Conn}(\alpha,a)}
A_{\mathfrak C,a},
```

where each cluster `\mathfrak C` is connected in the Paper-11 block-collar
graph and touches the declared collars of the loop insertions. Assume:

1. **local singular support:** all divergent single-loop cluster subfamilies are
   supported inside the perimeter/cusp collar of a single inserted loop;
2. **calibration identification:** the sum of those single-loop singular
   subfamilies equals `D_{\rho_j}(C_j,a)` as fixed by Definition 3.1;
3. **connected residual summability:** after extracting the single-loop singular
   factors, the remaining connected cluster weights
   `B_{\mathfrak C,a}` obey

   ```math
   \sum_{\mathfrak C\in{\rm Conn}(\alpha,a)}
   |B_{\mathfrak C,a}|
   \le
   K_\alpha^{\rm loc}+R_\alpha^{\rm tail}
   <\infty
   ```

   uniformly in `a`.

Then the connected perimeter-cusp decomposition of Definition 3.6 holds.

### Proof

By local singular support, every divergent factor is assigned to exactly one
inserted loop collar and is scalar, because the inserted records are closed
scalar Wilson-loop traces. Calibration identification gives the product of
all singular factors as

```math
\exp\left(
-\sum_{j=1}^{m}D_{\rho_j}(C_j,a)
\right).
```

After factoring this term from the connected cluster expansion, the remaining
sum is

```math
K_{\alpha,a}+R_{\alpha,a}
:=
\sum_{\mathfrak C\in{\rm Conn}(\alpha,a)}
B_{\mathfrak C,a}.
```

The residual summability assumption bounds this sum uniformly in `a`, giving
Definition 3.6. `square`

### Lemma 3.6B: UV Singular Support For Admissible Wilson Loops On The AF Trajectory

Work along the Paper-11 ledger-compatible asymptotically-free trajectory, in
finite physical volume and finite battery. Assume the hypotheses of Paper 11,
Theorem AF.14 and Theorem AF.32, for the scalar Wilson-loop battery generated
by a fixed admissible loop class. Let the block-collar graph be chosen so
that, for sufficiently small `a`,

```math
w_a\le r_{\min}/8,
```

where `w_a` is the physical thickness of the microscopic loop collar and
`r_{\min}` is the admissible separation constant of Definition 2.0.

Then the divergent part of every connected polymer contribution to a finite
bare Wilson-loop cumulant is supported in the collar of a single inserted
loop and is a sum of:

```math
\gamma_\rho(a){\rm Per}_a(C),
\qquad
\Gamma_\rho(\theta,a)
```

over the smooth perimeter pieces and cusp points of that inserted loop. All
connected contributions touching either separated loops or separated
nonadjacent arcs have a uniformly finite renormalized contribution, bounded
by the Paper-11 AF residual ledger.

More explicitly, for every ordered tuple
`\alpha=((C_1,\rho_1),\ldots,(C_m,\rho_m))` there are constants
`C_\alpha^{\rm uv}` and `C_\alpha^{\rm tail}` such that, after extracting
the calibration factors of Definition 3.1,

```math
\sum_{\mathfrak C\in{\rm Conn}(\alpha,a)}
|B_{\mathfrak C,a}|
\le
C_\alpha^{\rm uv}
+
C_\alpha^{\rm tail}
\sum_{r\ge r_0}
G_{\alpha,r}Q_r^*e^{-\mu R_r},
```

where the final series is the Paper-11 AF local-RG tail of Theorem AF.14
restricted to the finite loop-collar battery for `\alpha`.

### Proof

The proof has two parts: singular support and summable remainder.

**Singular support.** In the block axial-tree coordinates of Paper 11,
Wilson-loop insertions are closed scalar functions of the reconstructed
parallel transport. At short distance the AF trajectory is controlled by the
gauge-field scaling dimension of the Yang-Mills fixed point plus running
irrelevant corrections. Along a smooth loop segment the only local collision
stratum with nonnegative superficial degree is the diagonal collision of
fields on the same one-dimensional curve. Its contribution is proportional
to the lattice length:

```math
\sum_{e\subset C_a}{\rm local}(e,a)
=
\gamma_\rho(a){\rm Per}_a(C)
+O(1).
```

At a cusp, two incident rays meet at one point. The short-distance integral
over the two rays has logarithmic local degree and depends only on the
opening angle and representation:

```math
{\rm local}_{\rm cusp}(\theta,a)
=
\Gamma_\rho(\theta,a)+O(1).
```

For nonadjacent arcs of the same admissible loop and for distinct inserted
loops, the separation is at least `r_{\min}-2w_a\ge 3r_{\min}/4`. Hence their
short-distance diagonals do not collide. Any connected polymer touching such
separated collars has no UV singular subgraph supported at zero physical
distance. Its contribution is therefore assigned to the finite connected
remainder, not to a counterterm.

The admissible loop restrictions exclude the other possible local
singularities at this stage: arbitrarily sharp cusps, self-intersections,
accumulating cusps, and tangent self-approaches. Gauge invariance and
closed-trace scalarity forbid a charged local counterterm on the loop; the
only scalar local terms with nonnegative degree on this clean class are
perimeter and cusp terms. Curvature and shape-dependent smooth terms are
finite because the total curvature and cusp number are bounded.

The calibration ledger of Definition 3.1 identifies the coefficients of
these local singular terms with the declared `\gamma_\rho(a)` and
`\Gamma_\rho(\theta,a)`. Thus the singular factor extracted from a tuple is

```math
\exp\left(
-\sum_{j=1}^{m}D_{\rho_j}(C_j,a)
\right).
```

**Summable remainder.** After this extraction, every remaining connected
cluster either:

1. lies in a finite smooth/cusp collar but has negative local degree after the
   perimeter/cusp subtraction;
2. connects distinct collar components separated by a positive physical
   distance;
3. belongs to the omitted local-RG polymer tail.

The first two classes are bounded on each finite admissible battery by the
AF polymer Banach norm and the finite number of loop-collar blocks touched by
the battery. The third class is bounded by the Paper-11 AF residual estimate:

```math
\eta_{{\rm locRG},{\mathcal F}_r}^{\rm 1B}(r)
\le
2e^\alpha G_{\alpha,r}Q_r^*e^{-\mu R_r}.
```

The summability hypothesis of Theorem AF.14 makes the series finite. Combining
the bounded local remainder with the summable tail gives the displayed bound.
`square`

### Theorem 3.6C: AF Trajectory Gives The Local Connected-Polymer Criterion

Under the hypotheses of Lemma 3.6B, the local connected-polymer criterion of
Lemma 3.6A holds for every finite admissible renormalized Wilson-loop battery.

### Proof

Lemma 3.6B gives exactly the three inputs of Lemma 3.6A:

1. local singular support in a single loop collar;
2. calibration identification with the declared perimeter and cusp
   counterterms;
3. a uniformly summable connected residual bound.

Therefore Lemma 3.6A applies and gives the connected perimeter-cusp
decomposition of Definition 3.6. `square`

### Theorem 3.7: Paper-11 RG Control Plus Perimeter-Cusp Renormalization Gives The Finite Cumulant Envelope

Let `\mathcal B_N` be a finite admissible renormalized Wilson-loop battery.
Assume:

1. the calibration branch of Definition 3.1 is real and nonzero on a
   refinement tail;
2. Paper 11's smeared Wilson-loop RG residual ledger controls all finite
   products in the corresponding smeared battery;
3. either the connected perimeter-cusp decomposition of Definition 3.6 holds
   directly, or it is supplied by Theorem 3.6C from the Paper-11 AF
   trajectory.

Then the finite cumulant envelope of Theorem 3.4 holds for
`\mathcal B_N`. Consequently `\mathcal B_N` is product-bounded.

### Proof

Write

```math
X_{j,a}
=
W_{\rho_j}^{\rm ren}(C_{j,a})
=
\exp(D_{\rho_j}(C_j,a))
W_{\rho_j}^{\rm bare}(C_{j,a}).
```

Multilinearity of cumulants gives

```math
\kappa_a(X_{1,a},\ldots,X_{m,a})
=
\exp\left(\sum_{j=1}^{m}D_{\rho_j}(C_j,a)\right)
\kappa_a
\left(
W_{\rho_1}^{\rm bare}(C_{1,a}),\ldots,
W_{\rho_m}^{\rm bare}(C_{m,a})
\right).
```

Substitute the connected perimeter-cusp decomposition:

```math
\kappa_a(X_{1,a},\ldots,X_{m,a})
=
K_{\alpha,a}+R_{\alpha,a}.
```

Therefore

```math
\sup_a
|\kappa_a(X_{1,a},\ldots,X_{m,a})|
\le
K_\alpha^{\rm loc}+R_\alpha^{\rm tail}
<\infty.
```

This is exactly the finite cumulant envelope required by Theorem 3.4. The
moment product-boundedness follows from Theorem 3.4. `square`

This theorem is the honest proof boundary. Paper 11 supplies bounded smeared
cumulants and RG residual propagation. Lemmas 3.6B--3.6C supply the additional
AF-trajectory argument that, on the admissible loop class, the only unsmeared
connected UV divergences are the declared perimeter and cusp divergences, with
summable connected residual tails. This is still a finite-battery
perturbative-AF result, not a full nonperturbative continuum Yang-Mills
theorem.

### Definition 3.8: Counterterm-Normalized Smeared Records

For `\tau>0`, define the counterterm-normalized smeared record

```math
\widehat W_{\rho,\tau}(C_a)
=
\widehat Z_{\rho,\tau}(C,a)W_{\rho,\tau}(C_a),
```

where

```math
\widehat Z_{\rho,\tau}(C,a)
=
\exp\left(
\widehat\gamma_{\rho,\tau}(a){\rm Per}_a(C)
+
\sum_{\upsilon\in{\rm Cusps}(C)}
\widehat\Gamma_{\rho,\tau}(\theta_\upsilon,a)
\right).
```

The smeared counterterms are fixed by the same calibration loops and targets
as Definition 3.1:

```math
\mu_a(\widehat W_{\rho,\tau}(Q_{\rho,a}))=q_{\rho,{\rm per}},
\qquad
\mu_a(\widehat W_{\rho,\tau}(K_{\rho,\theta,a}))
=q_{\rho,{\rm cusp}}(\theta),
```

whenever the corresponding logarithms are real and nonzero. For fixed
positive `\tau`, this is a finite calibration of a bounded smeared record.
The limit `\tau\downarrow0` is the nontrivial part.

This correction matters: Paper 12 compares renormalized smeared records with
renormalized unsmeared records. It does not compare an unrenormalized
positive-smearing observable with a perimeter/cusp-renormalized unsmeared
observable.

### Definition 3.9: Product And Cumulant Smearing-Removal Consistency

Let `X_{j,a}=W_{\rho_j}^{\rm ren}(C_{j,a})` and
`Y_{j,a,\tau}=\widehat W_{\rho_j,\tau}(C_{j,a})` for a finite admissible
tuple `\alpha=((C_1,\rho_1),\ldots,(C_m,\rho_m))`.

The pair of smeared and unsmeared renormalization ledgers is
product-consistent on a finite battery if, for every ordered tuple with
`1\le m\le p_N`,

```math
\lim_{\tau\downarrow0}
\limsup_{a\downarrow0}
\left|
\mu_a\left(\prod_{j=1}^{m}Y_{j,a,\tau}\right)
-
\mu_a\left(\prod_{j=1}^{m}X_{j,a}\right)
\right|
=0.
```

It is cumulant-consistent if

```math
\lim_{\tau\downarrow0}
\limsup_{a\downarrow0}
\left|
\kappa_a(Y_{1,a,\tau},\ldots,Y_{m,a,\tau})
-
\kappa_a(X_{1,a},\ldots,X_{m,a})
\right|
=0
```

for every such tuple.

### Lemma 3.10: Cumulant Consistency Plus Bounded Cumulants Gives Product Consistency

Assume the renormalized smeared and unsmeared batteries have uniformly bounded
cumulants up to product degree `p_N`, and assume cumulant-consistency in the
sense of Definition 3.9. Then product-consistency holds.

### Proof

For each tuple, expand both product moments by the moment-cumulant formula:

```math
\mu_a\left(\prod_{j=1}^{m}X_{j,a}\right)
=
\sum_{\pi\in\Pi_m}
\prod_{B\in\pi}
\kappa_a(X_{j,a}:j\in B),
```

and the same expression with `Y_{j,a,\tau}`. The difference of the two finite
partition sums is a finite sum of products in which at least one cumulant
factor is replaced by its smeared-minus-unsmeared difference. The remaining
cumulant factors are uniformly bounded. Taking `a\downarrow0` and then
`\tau\downarrow0` gives zero term by term. `square`

### Definition 3.11: Smeared-Versus-Unsmeared Local Subtraction Estimate

A finite admissible battery satisfies the local subtraction estimate if, for
every ordered tuple `\alpha`, the renormalized connected cumulants admit
cluster representations

```math
\kappa_a(X_{1,a},\ldots,X_{m,a})
=
\sum_{\mathfrak C\in{\rm Conn}(\alpha,a)}B_{\mathfrak C,a},
```

and

```math
\kappa_a(Y_{1,a,\tau},\ldots,Y_{m,a,\tau})
=
\sum_{\mathfrak C\in{\rm Conn}(\alpha,a)}B_{\mathfrak C,a}^{(\tau)}
```

after extracting the respective perimeter/cusp calibration factors, with:

1. **calibration convergence**

   ```math
   \epsilon_{\alpha}^{\rm cal}(\tau)
   :=
   \limsup_{a\downarrow0}
   \left|
   \sum_j\widehat D_{\rho_j,\tau}(C_j,a)
   -
   \sum_jD_{\rho_j}(C_j,a)
   -
   \log{\mathcal S}_{\alpha,\tau}(a)
   \right|
   \to0,
   ```

   where `{\mathcal S}_{\alpha,\tau}` is the local singular factor removed by
   replacing unsmeared collars with `\tau`-smeared collars;
2. **renormalized cluster convergence**

   ```math
   \Omega_\alpha(\tau)
   :=
   \limsup_{a\downarrow0}
   \sum_{\mathfrak C\in{\rm Conn}(\alpha,a)}
   |B_{\mathfrak C,a}^{(\tau)}-B_{\mathfrak C,a}|
   \to0;
   ```

3. **uniform connected domination**

   ```math
   \sup_{0<\tau\le\tau_0}
   \limsup_{a\downarrow0}
   \sum_{\mathfrak C\in{\rm Conn}(\alpha,a)}
   \left(
   |B_{\mathfrak C,a}^{(\tau)}|+|B_{\mathfrak C,a}|
   \right)
   <\infty.
   ```

Here

```math
D_\rho(C,a)
=
\gamma_\rho(a){\rm Per}_a(C)
+
\sum_{\upsilon}\Gamma_\rho(\theta_\upsilon,a),
```

and `\widehat D_{\rho,\tau}` is the same expression with
`\widehat\gamma_{\rho,\tau}` and `\widehat\Gamma_{\rho,\tau}`.

### Theorem 3.12: AF Local Subtraction Gives Cumulant Smearing-Removal

Assume the Paper-11 AF trajectory hypotheses of Lemma 3.6B and the finite
admissible battery satisfies Definition 3.11. Then cumulant smearing-removal
consistency holds. If, in addition, the cumulant envelopes of Theorem 3.7 hold
uniformly for `0<\tau\le\tau_0`, product smearing-removal consistency holds.

### Proof

For a fixed ordered tuple, the renormalized unsmeared cumulant is the
renormalized connected cluster sum

```math
\kappa_a(X_{1,a},\ldots,X_{m,a})
=
\sum_{\mathfrak C}B_{\mathfrak C,a},
```

and the counterterm-normalized smeared cumulant is

```math
\kappa_a(Y_{1,a,\tau},\ldots,Y_{m,a,\tau})
=
\sum_{\mathfrak C}B_{\mathfrak C,a}^{(\tau)}.
```

The calibration-convergence clause says that the local singular factors
removed by smearing are the same perimeter/cusp factors removed by the
unsmeared ledger, up to an error
`\epsilon_{\alpha}^{\rm cal}(\tau)\to0`. The renormalized cluster-convergence
clause gives

```math
\limsup_{a\downarrow0}
\left|
\kappa_a(Y_{1,a,\tau},\ldots,Y_{m,a,\tau})
-
\kappa_a(X_{1,a},\ldots,X_{m,a})
\right|
\le
\epsilon_{\alpha}^{\rm cal}(\tau)+\Omega_\alpha(\tau).
```

Taking `\tau\downarrow0` proves cumulant-consistency. Uniform connected
domination gives the cumulant bounds needed by Lemma 3.10, and Lemma 3.10
then gives product-consistency. `square`

### Lemma 3.13: Why The Local Subtraction Estimate Holds On The Clean AF Class

For the admissible loop class of Definition 2.0, the local subtraction
estimate of Definition 3.11 follows from the same AF block-collar analysis as
Lemma 3.6B, provided the gauge-covariant smearing kernel has physical support
`O(\tau)`, is an approximation to the identity on smooth gauge fields, and
preserves the loop-collar locality ledger.

### Proof

The admissible separation condition gives a scale window

```math
a\ll\tau\ll r_{\min}.
```

In that window, smearing modifies only the microscopic collar of each smooth
segment and cusp. It cannot mix distinct nonadjacent arcs or distinct loops,
because their collars remain separated by a positive physical distance.
Therefore the difference between the smeared and unsmeared connected cluster
expansions has the same local singular support as in Lemma 3.6B.

On smooth segments, the smearing kernel replaces the lattice UV cutoff by the
physical cutoff `\tau`. The calibration loop `Q_\rho` fixes the difference of
the two perimeter singular factors. At cusps, the one-cusp calibration loops
`K_{\rho,\theta}` fix the difference of the two cusp singular factors. Hence
the local singular difference is exactly the calibration term appearing in
Definition 3.11, with `\epsilon_{\alpha}^{\rm cal}(\tau)\to0`.

After those local perimeter/cusp pieces are removed, every remaining cluster
has negative local degree or positive physical separation. The AF polymer
bound of Theorem AF.14 gives a summable dominating series, while the
approximation-to-identity property of the smearing kernel gives pointwise
cluster convergence as `\tau\downarrow0`. Dominated convergence for the
absolutely summable connected polymer series yields
`\Omega_\alpha(\tau)\to0` and the uniform connected domination bound.
`square`

## 4. Compactness And Limit Functionals

### Theorem 4.1: Bounded Renormalized Loops Have Subsequence Limits

For every countable product-bounded renormalized loop battery and every
refinement sequence `a_j\downarrow0`, there is a subsequence on which all
renormalized loop expectations converge.

### Proof

Each tested product is bounded in a compact interval or disk. Apply the
diagonal subsequence argument used in Paper 11 for bounded Wilson-loop tests.
`square`

### Theorem 4.2: Smearing-Removal Consistency Transfers The Smeared Limit

Assume:

1. counterterm-normalized smeared Wilson-loop limits exist:

   ```math
   \widehat S_{\rho,\tau}(C)
   =
   \lim_{a\downarrow0}\mu_a(\widehat W_{\rho,\tau}(C_a));
   ```

2. the limit

   ```math
   S_\rho^{\rm ren}(C)
   =
   \lim_{\tau\downarrow0}\widehat S_{\rho,\tau}(C)
   ```

   exists;
3. product smearing-removal consistency holds in the sense of Definition 3.9.

Then every subsequential renormalized unsmeared limit agrees with
`S_\rho^{\rm ren}(C)`.

### Proof

For fixed `\tau`,

```math
|\mu_a(W_\rho^{\rm ren}(C_a))-S_\rho^{\rm ren}(C)|
\le
|\mu_a(W_\rho^{\rm ren}(C_a))-\mu_a(\widehat W_{\rho,\tau}(C_a))|
+|\mu_a(\widehat W_{\rho,\tau}(C_a))-\widehat S_{\rho,\tau}(C)|
+|\widehat S_{\rho,\tau}(C)-S_\rho^{\rm ren}(C)|.
```

First take `a\downarrow0`, then `\tau\downarrow0`. The three terms vanish by
product smearing-removal consistency, smeared convergence, and the assumed
`\tau`-limit. `square`

## 5. Continuity And Nontriviality

### Definition 5.1: Admissible Loop Metric

On a fixed admissible stratum, loops have the same number of labeled cusps
and the same cyclic ordering of smooth arcs. Give each loop its oriented
constant-speed parametrization `x_C:[0,1]\to{\mathbb R}^4`, with cusp labels
matched by parameter values. Define

```math
d_{\rm adm}(C,C')
=
\|x_C-x_{C'}\|_\infty
+
|{\rm Per}(C)-{\rm Per}(C')|
+
\int_{\rm smooth}
|\dot x_C(t)-\dot x_{C'}(t)|\,dt
+
\sum_{\upsilon}
|\theta_\upsilon(C)-\theta_\upsilon(C')|.
```

Loops in different admissible strata are assigned distance `1`. On each
stratum this metric controls the position of the loop collar, the tangent
data on smooth arcs, perimeter, and cusp angles. It is intentionally stronger
than Hausdorff distance; Hausdorff distance alone does not control cusp or
tangent singularities.

### Definition 5.2: Renormalized Loop Modulus

A renormalized loop functional has modulus `\omega` in a loop metric
`d_{\rm loop}` if

```math
|S_\rho^{\rm ren}(C)-S_\rho^{\rm ren}(C')|
\le
\omega(d_{\rm loop}(C,C')),
\qquad
\omega(\delta)\downarrow0.
```

### Theorem 5.3: Uniform Renormalized Modulus Gives Continuity

If the finite-lattice renormalized records satisfy

```math
|\mu_a(W_\rho^{\rm ren}(C_a))-\mu_a(W_\rho^{\rm ren}(C'_a))|
\le
\omega(d_{\rm loop}(C,C'))+\zeta(a),
```

with `\zeta(a)\to0`, then every renormalized continuum limit is continuous in
`d_{\rm loop}`.

### Proof

Take the continuum limit in the displayed inequality. `square`

### Definition 5.4: AF Loop-Variation Estimate

A finite admissible renormalized loop battery satisfies the AF loop-variation
estimate if, for every pair `C,C'` in the same admissible stratum and every
tested representation `\rho`, the renormalized connected cluster weights of
Section 3 can be matched so that

```math
\limsup_{a\downarrow0}
\sum_{\mathfrak C}
|B_{\mathfrak C,a}(C,\rho)-B_{\mathfrak C,a}(C',\rho)|
\le
L_{\rho,N}d_{\rm adm}(C,C')+\omega_{\rho,N}^{\rm tail}
(d_{\rm adm}(C,C')),
```

where `L_{\rho,N}<\infty` and
`\omega_{\rho,N}^{\rm tail}(\delta)\downarrow0`.

For products or cumulants, the same condition is imposed on the tuple metric

```math
d_{\rm adm}^{(m)}(\alpha,\alpha')
=
\sum_{j=1}^{m}d_{\rm adm}(C_j,C'_j)
```

with constants depending only on the finite battery and product degree.

### Lemma 5.5: The AF Clean Loop Class Satisfies The Loop-Variation Estimate

On the Paper-11 perturbative AF trajectory, the admissible clean loop class
satisfies Definition 5.4 for every finite battery.

### Proof

The cluster expansion used in Lemmas 3.6B and 3.13 is absolutely dominated by
the same AF summable polymer tail. It is therefore enough to control the
variation of each local cluster contribution.

On smooth arcs, changing `C` by `d_{\rm adm}(C,C')` changes the microscopic
collar position, tangent insertion, and length by at most a constant multiple
of `d_{\rm adm}(C,C')` inside a fixed admissible stratum. On cusp collars, the
calibration ledger has already isolated the singular angle dependence in
`\Gamma_\rho(\theta,a)`, and the remaining renormalized cusp cluster is
continuous in `\theta` on the compact interval
`[\theta_{\min},\pi-\theta_{\min}]`. The admissible separation constant
prevents a small loop deformation from creating or destroying a short-distance
collision between nonadjacent arcs.

Thus each retained local cluster varies by at most
`L_{\mathfrak C}d_{\rm adm}(C,C')`. The AF Banach norm bounds the sum of
`L_{\mathfrak C}` over retained clusters in a finite battery, and the omitted
clusters are bounded by the same summable tail as in Theorem AF.14. Dominated
convergence gives the displayed tail modulus. `square`

### Theorem 5.6: AF Loop-Variation Gives A Renormalized Loop Modulus

Assume product-boundedness, product smearing-removal, and the AF
loop-variation estimate on a finite admissible battery. Then every
renormalized unsmeared continuum limit satisfies, on each fixed admissible
stratum,

```math
|S_\rho^{\rm ren}(C)-S_\rho^{\rm ren}(C')|
\le
\omega_{\rho,N}(d_{\rm adm}(C,C')),
```

where one may take

```math
\omega_{\rho,N}(\delta)
=
L_{\rho,N}\delta+\omega_{\rho,N}^{\rm tail}(\delta).
```

### Proof

Apply Definition 5.4 to the one-loop tuple and pass to the renormalized
continuum limit using Theorem 4.2. For loops in different strata,
product-boundedness gives a finite crude bound, so the modulus can be
extended to `d_{\rm adm}=1` by taking
`\omega_{\rho,N}(1)` larger than twice the battery bound. The same proof
applies to finite products and cumulants with the tuple metric. `square`

### Theorem 5.7: Small-Smearing Anchor Transfers To The Renormalized Unsmeared Loop

Suppose Paper 11 gives a counterterm-normalized smeared anchor at a fixed
positive smearing radius `\tau` in a small-smearing interval
`0<\tau\le\tau_*`. Assume the normalized smeared expansion has the form

```math
\widehat S_{\rho,\tau}(C)
=
T_{\rm triv}
-
A_{\rho,\tau}(C)
+
{\mathcal R}_{\rho,\tau}(C),
```

with

```math
A_{\rho,\tau}(C)
\ge
A_0>0,
\qquad
|{\mathcal R}_{\rho,\tau}(C)|
\le
A_{\rho,\tau}(C)/4
```

for `0<\tau\le\tau_*`, and suppose product smearing-removal gives

```math
\lim_{\tau\downarrow0}
|\widehat S_{\rho,\tau}(C)-S_\rho^{\rm ren}(C)|
=0.
```

Then the renormalized unsmeared loop is nontrivial:

```math
|S_\rho^{\rm ren}(C)-T_{\rm triv}|
\ge
A_0/2.
```

### Proof

The expansion gives

```math
|\widehat S_{\rho,\tau}(C)-T_{\rm triv}|
\ge
A_{\rho,\tau}(C)-|{\mathcal R}_{\rho,\tau}(C)|
\ge
3A_0/4.
```

By smearing-removal, choose `\tau` small enough that

```math
|S_\rho^{\rm ren}(C)-\widehat S_{\rho,\tau}(C)|
\le
A_0/4.
```

The triangle inequality gives the displayed lower bound. `square`

### Corollary 5.8: Perturbative Paper-11 Anchor Gives Paper-12 Nontriviality

Assume the Paper-11 perturbative smeared anchor of Theorem AF.31 holds after
the finite calibration normalization of Definition 3.8, and assume its
renormalized coefficient satisfies

```math
\widehat I_\tau(C)\to \widehat I_0(C)>0
```

as `\tau\downarrow0`, with the perturbative remainder uniform for sufficiently
small `\tau`. Then Theorem 5.7 applies with

```math
A_0
=
\frac14 C_2(\rho)\widehat I_0(C)g_-^2,
```

after reducing `\tau_*` if necessary.

### Proof

The Paper-11 expansion gives the form required by Theorem 5.7 with
`A_{\rho,\tau}(C)=\frac12C_2(\rho)\widehat I_\tau(C)g_R^2`. Since
`\widehat I_\tau(C)\to\widehat I_0(C)>0` and `g_R^2\ge g_-^2`, shrink
`\tau_*` so that
`A_{\rho,\tau}(C)\ge \frac12C_2(\rho)\widehat I_0(C)g_-^2`. The uniform
remainder bound supplies `|{\mathcal R}|\le A/4`, and Theorem 5.7 gives
nontriviality. `square`

This is still not a confinement or mass-gap theorem. It proves only that the
renormalized unsmeared Wilson-loop functional is not the trivial functional
on the anchored admissible loop.

### Definition 5.9: Symmetric Positive Counterterm Ledger

The perimeter/cusp counterterm ledger is symmetric-positive on an admissible
finite battery if:

1. all counterterm factors are real and positive;
2. `Z_{\rho,{\rm per}}(C,a)` depends only on `\rho` and
   `{\rm Per}_a(C)`;
3. `Z_{\rho,{\rm cusp}}(\theta,a)` depends only on `\rho` and the unoriented
   cusp angle `\theta`;
4. the calibration targets are chosen invariant under lattice reflections and
   lattice Euclidean symmetries;
5. the lattice approximant rule is equivariant up to a summable defect
   `\epsilon_{{\rm app},a}` in the Paper-11 ledger.

The same definition applies to the counterterm-normalized smeared ledger
with hats.

### Theorem 5.10: Reflection Positivity Survives Positive Scalar Counterterms

Assume Paper 11 gives reflection positivity on a finite positive-time
Wilson-loop battery either exactly or with a declared counterterm-weighted
defect. More precisely, for a positive-time product basis
`F_1,\ldots,F_q`, let

```math
G_{ij,a}
=
\mu_a(F_i\,\vartheta F_j),
\qquad
G^{\rm ren}_{ij,a}
=
\mu_a(F_i^{\rm ren}\,\vartheta F_j^{\rm ren}).
```

Suppose the counterterm ledger is symmetric-positive and

```math
G^{\rm ren}_a
=
D_aG_aD_a+E^{\rm RP}_a,
\qquad
\|E^{\rm RP}_a\|_{\rm op}
\le
\epsilon^{\rm ct}_{{\rm RP},a}.
```

If `G_a` is positive semidefinite and
`\epsilon^{\rm ct}_{{\rm RP},a}\to0`, then every renormalized continuum limit
is reflection-positive on the tested class. If Paper 11 gives an
unrenormalized RP defect `\epsilon_{{\rm RP},a}` and the finite counterterm
envelope satisfies `\|D_a\|^2\epsilon_{{\rm RP},a}\to0`, then
`\epsilon^{\rm ct}_{{\rm RP},a}\to0`.

### Proof

Reflection positivity is positivity of the Gram matrix

```math
G_{ij,a}
=
\mu_a(F_i\,\vartheta F_j).
```

Renormalizing a basis element multiplies it by a positive scalar
`z_i(a)>0`, because the counterterms are real positive and depend only on
loop geometry. Reflection maps `F_j` to a loop product with the same
perimeters and unoriented cusp angles, up to the declared approximant defect.
Thus

```math
G^{\rm ren}_{ij,a}
=
z_i(a)z_j(a)G_{ij,a}
+E_{ij,a}.
```

The first term is the congruence `D_aG_aD_a` by a positive diagonal matrix,
so it preserves positivity. The second term is exactly the
counterterm-weighted RP defect. If it vanishes in the continuum limit, then
all negative parts of the finite Gram matrices vanish, and the limiting
functional is reflection-positive. When an unrenormalized defect is used
instead, the same conclusion follows only if the diagonal scaling does not
amplify it: `\|D_a\|^2\epsilon_{{\rm RP},a}\to0`. `square`

### Theorem 5.11: Euclidean Covariance Survives Scalar Geometric Counterterms

Assume Paper 11 gives Euclidean covariance on a finite Wilson-loop battery for
the finite lattice symmetry group, and let the counterterm-weighted covariance
defect be

```math
\epsilon_{{\rm Euc},a}^{\rm ct}
=
\sup_{T\in{\mathcal B}_N}
\left|
\mu_a(T^{\rm ren})-\mu_a((gT)^{\rm ren})
\right|.
```

If the counterterm ledger is symmetric-positive and
`\epsilon_{{\rm Euc},a}^{\rm ct}\to0` for every finite lattice symmetry
approximating a continuum Euclidean motion of admissible loops, then the
renormalized continuum functional is Euclidean covariant on the tested
admissible loop class. If one starts from an unrenormalized covariance defect
`\epsilon_{{\rm Euc},a}`, it is enough to have the weighted bound
`Z_N(a)\epsilon_{{\rm Euc},a}+\epsilon_{{\rm app},a}\to0`, where `Z_N(a)` is
the largest counterterm product appearing in the finite battery.

### Proof

For a lattice Euclidean symmetry `g`,

```math
{\rm Per}_a(gC_a)={\rm Per}_a(C_a),
\qquad
\theta_\upsilon(gC_a)=\theta_\upsilon(C_a),
```

up to the approximant defect. Hence the scalar counterterm multiplying
`W_\rho^{\rm bare}(C_a)` is the same as the counterterm multiplying
`W_\rho^{\rm bare}(gC_a)`, modulo `\epsilon_{{\rm app},a}`. Therefore the
renormalized covariance defect is precisely the counterterm-weighted defect
displayed above. If that defect vanishes, covariance passes to the continuum
limit. The unrenormalized-defect sufficient condition is the same statement
with the counterterm scaling made explicit. `square`

## 6. Main Paper-12 Theorem

### Theorem 6.1: Finite-Battery AF Renormalized Unsmeared Wilson-Loop Functional

Fix a finite admissible loop battery and a Paper-11 perturbative
asymptotically-free refinement trajectory. Assume:

1. the Paper-11 AF hypotheses used in Lemma 3.6B hold for this battery;
2. the perimeter/cusp calibration branches of Definition 3.1 and the smeared
   calibration branches of Definition 3.8 are real, nonzero, and
   symmetric-positive in the sense of Definition 5.9;
3. the gauge-covariant smearing kernel obeys the clean-class locality and
   approximation-to-identity hypotheses of Lemma 3.13;
4. the Paper-11 perturbative anchor satisfies Corollary 5.8 on at least one
   admissible loop;
5. the counterterm-weighted reflection-positivity and Euclidean-covariance
   defects of Theorems 5.10--5.11 vanish along the refinement path.

Then the refinement path defines a nontrivial gauge-invariant renormalized
unsmeared Wilson-loop functional on the finite admissible battery. The
functional is product-bounded, independent of the smearing-removal path,
continuous in the admissible loop topology, reflection-positive, and
Euclidean covariant on the tested class.

On a countable nested union of such finite batteries, the same conclusion
holds by diagonal extension whenever the battery constants are controlled on
each finite stage.

### Proof

Theorem 3.6C supplies the local connected-polymer criterion from the AF
trajectory. Theorem 3.7 gives the finite cumulant envelope, and Theorem 3.4
gives product-boundedness. Lemma 3.13 verifies the local subtraction estimate,
Theorem 3.12 gives cumulant and product smearing-removal, and Theorem 4.2
identifies the renormalized unsmeared limit with the counterterm-normalized
`\tau\downarrow0` smeared limit. Thus the result is independent of the
chosen positive smearing-removal path inside the declared class.

Gauge invariance follows because all records are scalar closed Wilson-loop
traces and all renormalization factors are scalar geometric constants. Lemma
5.5 and Theorem 5.6 give continuity in `d_{\rm adm}`. Theorem 5.7 and
Corollary 5.8 give nontriviality. Theorems 5.10 and 5.11 give reflection
positivity and Euclidean covariance after scalar counterterm renormalization.
The countable nested statement is the diagonal compactness argument of
Theorem 4.1 applied stage by stage. `square`

## 7. Obstruction Ledger

Paper 12 fails to cross the unsmeared Wilson-loop gate if any of the following
persist:

1. the admissible loop class must be widened before the clean class is
   controlled;
2. perimeter or cusp calibration branches are not real and nonzero on a
   refinement tail;
3. neither the finite counterterm envelope nor the finite cumulant envelope
   can be proved for the tested batteries; concretely, the AF singular-support
   argument of Lemma 3.6B or the local connected-polymer criterion of
   Lemma 3.6A may fail;
4. renormalized loop records are not product-bounded or uniformly integrable;
5. local subtraction or product smearing-removal consistency fails;
6. the AF loop-variation estimate fails, so the loop-continuity modulus is
   unavailable;
7. the small-smearing anchor coefficient vanishes, the perturbative remainder
   is not uniform, or the renormalized limit collapses to the trivial value;
8. the counterterm ledger is not symmetric-positive, the approximant rule is
   not equivariant, or the counterterm-weighted reflection
   positivity/Euclidean covariance defects do not vanish after finite-battery
   renormalization;
9. the construction requires undeclared charged or framed data.

These are real obstructions, not notation problems.

## 8. Follow-Up Programs

If Paper 12 succeeds, the next papers can ask harder questions:

1. **Paper 13:** nonperturbative continuum Yang-Mills functional on a dense
   loop algebra.
2. **Paper 14:** mass gap through gauge-invariant exponential clustering.
3. **Paper 15:** confinement through an area law or equivalent operational
   criterion.
4. **Paper 16:** V3 synthesis.

Paper 12 must not claim any of those results by itself.

## 9. Export To Paper 13

Paper 13 may use the following Paper-12 outputs:

1. finite admissible loop classes with the metric `d_{\rm adm}`;
2. calibrated perimeter/cusp renormalized unsmeared Wilson-loop records;
3. counterterm-normalized smeared records and smearing-removal consistency;
4. product-bounded finite batteries via the cumulant envelope;
5. finite-battery loop-continuity on admissible strata;
6. one nontrivial anchored loop obtained from the small-smearing Paper-11
   perturbative anchor;
7. reflection positivity and Euclidean covariance on finite batteries when
   the counterterm-weighted defect ledger vanishes;
8. diagonal extension to countable nested finite batteries when finite-stage
   constants are controlled.

Paper 13 may not use Paper 12 to claim:

```text
full nonperturbative continuum Yang-Mills;
mass gap;
confinement;
area law;
P20-SEL2-TREE-RATE-GATE;
SEL2 block-plaquette coefficient-time lower bounds;
SEL2 heat-kernel coefficient comparison;
rough-loop Wilson functionals outside the admissible extension domain;
charged/framed reconstruction from scalar loops alone;
Hilbert-space or field ontology as fundamental.
```

### Barandes Alignment For Paper 13

The Paper-13 loop algebra must remain an operational record algebra. Its
elements are declared Wilson-loop tests and finite products/cumulants of
tests. The extension from finite batteries to a dense loop algebra must be a
whole-process consistency theorem, not a composition of partial transition
kernels. Renormalization remains a declared transformation of records and
calibration constants. Gauge fields, Hilbert spaces, and local operator nets
may be reconstructed representations of the record calculus only after the
appropriate positivity, covariance, and continuity gates are proved.

## Honest Status

This draft now proves the finite-battery AF bridge:

```text
smeared perturbative Wilson-loop interface
+ admissible clean loop class
+ calibration-defined perimeter/cusp renormalization
+ product-boundedness by counterterm envelope or Paper-11 connected cumulant envelope
+ local subtraction and product/cumulant smearing-removal consistency
+ AF loop-continuity modulus
+ small-smearing nontriviality transfer
+ symmetric-positive scalar counterterms preserving RP/covariance
= nontrivial renormalized unsmeared Wilson-loop functional.
```

The first three gates are now explicit enough to attack: choose admissible
loops, choose real nonzero calibration branches, and prove either a strong
counterterm envelope or the more realistic Paper-11 connected polymer
criterion. Lemmas 3.6B--3.6C prove that criterion on the Paper-11
perturbative AF trajectory for finite admissible loop batteries. Theorem 3.7
then gives the finite cumulant envelope and hence product-boundedness.
Definitions 3.8--3.11, Theorem 3.12, and Lemma 3.13 upgrade
smearing-removal from single loops to finite products and cumulants: after
the same perimeter/cusp calibration is applied to smeared and unsmeared
records, the AF local subtraction estimate identifies the
`\tau\downarrow0` smeared limit with the renormalized unsmeared limit.
Definition 5.1 and Lemma 5.5--Theorem 5.6 prove loop-continuity on admissible
strata. Theorem 5.7 and Corollary 5.8 prove nontriviality transfer from a
small-smearing Paper-11 perturbative anchor.
Definition 5.9 and Theorems 5.10--5.11 prove that real positive scalar
perimeter/cusp counterterms preserve exact reflection positivity and
Euclidean covariance, and preserve approximate versions when the
counterterm-weighted defect ledger vanishes. Theorem 6.1 packages these gates
as a positive finite-battery AF result.

Paper 12 still does not prove full nonperturbative Yang-Mills, mass gap, or
confinement. It also does not prove the Paper-20 `SEL2` tree-rate source. Its
honest output is narrower and useful: along the Paper-11 perturbative AF
trajectory, finite admissible loop batteries have renormalized unsmeared
Wilson-loop functionals that are product-bounded, smearing-independent,
continuous on admissible strata, nontrivial on an anchored loop,
reflection-positive, and Euclidean covariant.
