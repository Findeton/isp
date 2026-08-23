# ISP v17 — Bell-current actuality comparator

**Status:** ACTIVE AUTHOR-SIDE STANDARD-QUANTUM COMPARATOR / NOT A PIN / NOT REVIEWED
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none

---

## 0. Question and attribution

C4 proved that record probabilities do not select a fine path law. This
comparator asks
whether known quantum physics already contains a principled positive law for
an actual configuration trajectory.

The strongest finite answer is the Bell-type quantum-current construction.
Given a quantum state, Hamiltonian, configuration observable, and external
time, it produces an ordinary positive Markov jump law whose marginals remain
Born distributed.

The core jump formula and its minimality classification are published results,
not a v17 discovery. The comparator reconstructs their finite content exactly and uses it
as a reality-first control for the native U-Gen question.

The decisive hierarchy is

$$
\boxed{
\text{Born equivariance}
\;<\;
\text{quantum-current matching}
\;<\;
\text{minimal no-counterflow law}.}
$$

Each step adds information. Only the last step selects the familiar minimal
jump rates within the finite current-matching class.

Primary mathematical source:

- Dürr, Goldstein, Tumulka, and Zanghì,
  [*Quantum Hamiltonians and Stochastic Jumps*](https://arxiv.org/abs/quant-ph/0303056),
  arXiv:quant-ph/0303056v3.

---

## 1. Finite configuration setup

Let

$$
\mathcal Q=\{1,\ldots,N\}
$$

be a finite configuration carrier. Let $\mathcal H=\mathbb C^N$ with
configuration projectors

$$
P_i=|i\rangle\langle i|.
$$

Let $H=H^\dagger$ and let $\psi(t)$ satisfy

$$
i\hbar\dot\psi=H\psi.
$$

Define Born weights

$$
p_i=|\psi_i|^2
$$

and the oriented quantum edge current

$$
J_{ij}
=\frac{2}{\hbar}
\operatorname{Im}
\bigl(\overline{\psi_i}H_{ij}\psi_j\bigr).
$$

The index convention is that positive $J_{ij}$ is net flow from configuration
$j$ to configuration $i$.

For the exact rate classification, first restrict to the instantaneous support

$$
S_t=\{i:p_i(t)>0\}.
$$

Zero-support configurations are treated separately in Section 8.

---

## 2. Proposition BC-A — quantum continuity equation

### Statement

The current is antisymmetric,

$$
J_{ji}=-J_{ij},
$$

and the Born weights obey

$$
\dot p_i=\sum_jJ_{ij}.
$$

### Proof

Hermiticity gives

$$
\overline{\psi_j}H_{ji}\psi_i
=\overline{\overline{\psi_i}H_{ij}\psi_j},
$$

so their imaginary parts have opposite signs.

Using $\dot\psi=-iH\psi/\hbar$,

$$
\begin{aligned}
\dot p_i
&=2\operatorname{Re}(\overline{\psi_i}\dot\psi_i)\\
&=\frac2\hbar
\operatorname{Im}
\left(\overline{\psi_i}\sum_jH_{ij}\psi_j\right)\\
&=\sum_jJ_{ij}.
\end{aligned}
$$

QED.

### Gauge scope

$J$ is unchanged by a global phase of $\psi$. It is also covariant under a
simultaneous rephasing of the configuration basis, $H$, and $\psi$. It is not
independent of the chosen configuration observable $\{P_i\}$.

---

## 3. Markov traffic and net current

Let $\sigma_{ij}\ge0$ be an instantaneous jump rate from $j$ to $i$ for
$i\ne j$. Define the directed probability traffic

$$
C_{ij}=\sigma_{ij}p_j\ge0
$$

and its antisymmetric net current

$$
K_{ij}=C_{ij}-C_{ji}.
$$

The master equation is

$$
\dot p_i
=\sum_{j\ne i}
\bigl(\sigma_{ij}p_j-\sigma_{ji}p_i\bigr)
=\sum_jK_{ij}.
$$

The comparator calls the rates **Born equivariant at the instant** when this equation
equals the quantum $\dot p_i$.

It calls them **standard-current matching** when the stronger edgewise
equation

$$
K_{ij}=J_{ij}
$$

holds for every ordered pair.

---

## 4. Proposition BC-B — complete finite equivariant-rate classification

### Statement

Assume $p_i>0$ on the finite carrier. Every Born-equivariant jump law is
obtained as follows.

1. Choose an antisymmetric current $K$ satisfying

   $$
   \sum_jK_{ij}=\dot p_i.
   $$

2. Choose an arbitrary symmetric nonnegative traffic matrix

   $$
   S_{ij}=S_{ji}\ge0
   \qquad(i\ne j).
   $$

3. Set

   $$
   C_{ij}=K_{ij}^{+}+S_{ij},
   \qquad
   \sigma_{ij}=\frac{C_{ij}}{p_j},
   $$

   where $x^+=\max(x,0)$.

Conversely, every equivariant jump law has this form, with

$$
K=C-C^T,
\qquad
S_{ij}=\min(C_{ij},C_{ji}).
$$

### Proof

For an antisymmetric $K$,

$$
K_{ij}=K_{ij}^{+}-K_{ji}^{+}.
$$

Adding the same symmetric traffic $S_{ij}$ to both directions therefore gives

$$
C_{ij}-C_{ji}=K_{ij}.
$$

The divergence condition gives the required master equation.

Conversely, every nonnegative $C$ has antisymmetric part
$K=C-C^T$. On each unordered pair, if $K_{ij}\ge0$, then

$$
C_{ij}=K_{ij}+C_{ji},
$$

so $S_{ij}=C_{ji}=\min(C_{ij},C_{ji})$. The other orientation is identical.
Thus $C=K^++S$ uniquely. QED.

### Interpretation

Born equivariance fixes only the divergence of $K$, not its edgewise values.
For $N\ge3$, one may add divergence-free cycle currents. Even after $K$ is
fixed, symmetric counter-traffic $S$ remains arbitrary.

---

## 5. Proposition BC-C — standard-current and minimal-rate classification

### Statement

Within the standard-current class $K=J$, every rate law is

$$
\boxed{
\sigma_{ij}
=\frac{J_{ij}^{+}+S_{ij}}{p_j},
\qquad
S_{ij}=S_{ji}\ge0.}
$$

The unique member with no simultaneous counterflow on any unordered edge is

$$
\boxed{
\sigma^{\min}_{ij}
=\frac{J_{ij}^{+}}{p_j}.}
$$

It is also the unique member that minimizes every edge traffic
$C_{ij}+C_{ji}$ and the total instantaneous expected jump rate.

### Proof

Set $K=J$ in Proposition BC-B. On each unordered pair,

$$
C_{ij}+C_{ji}
=|J_{ij}|+2S_{ij}.
$$

Therefore every edge traffic, and hence

$$
\lambda
=\sum_{i\ne j}C_{ij}
=\sum_{i<j}|J_{ij}|+2\sum_{i<j}S_{ij},
$$

is minimized uniquely by $S=0$. In that case exactly one of the two directed
rates on each edge can be nonzero. QED.

### Critical scope wall

Minimality is a theorem only after the following inputs are fixed:

1. the Born distribution $p$;
2. the complete edge current $J$, not merely its divergence;
3. the configuration carrier and projector packet;
4. a Markov jump ontology; and
5. the “least traffic/no counterflow” selection criterion.

Born equivariance by itself does not select the minimal Bell rates.

---

## 6. Proposition BC-D — cycle freedom beyond standard current

For $N=2$, every antisymmetric current is fixed by its divergence, so
equivariance fixes $K=J$ once $\dot p$ is fixed.

For $N\ge3$, let $Z$ be any antisymmetric divergence-free current,

$$
\sum_jZ_{ij}=0.
$$

Then

$$
K=J+Z
$$

has the same Born divergence as $J$ and therefore defines another equivariant
class.

### Exact three-cycle control

For a static uniform distribution on three configurations, take $J=0$ and

$$
Z_{12}=Z_{23}=Z_{31}=z>0,
$$

with reverse entries fixed by antisymmetry. Every row sum vanishes. The
directed cycle therefore preserves the same static Born distribution while
producing persistent ontic motion.

Thus even selecting the smallest rates for each chosen $K$ does not recover
the quantum-current law from equivariance. One must first select $K=J$.

---

## 7. Exact two-state traffic control

Let

$$
p_1=p_2=\frac12,
\qquad
J_{12}=\frac14.
$$

The minimal rates are

$$
\sigma^{\min}_{12}=\frac12,
\qquad
\sigma^{\min}_{21}=0.
$$

Adding symmetric traffic $S_{12}=1/8$ gives

$$
\sigma_{12}=\frac34,
\qquad
\sigma_{21}=\frac14.
$$

Both have the same net probability current:

$$
\sigma_{12}p_2-\sigma_{21}p_1=\frac14.
$$

Single-time Born evolution and standard current therefore do not reveal the
extra bidirectional traffic.

---

## 8. Zero-support and existence wall

If $p_j=0$, the displayed rate quotient cannot be used naively. For a quantum
state, $\psi_j=0$ implies

$$
J_{ij}=0
$$

for every $i$ at that instant. Rates out of a zero-probability source state do
not affect the instantaneous law and are not identified by equivariance.

The correct theorem is therefore support-relative. A global process also
requires control of:

1. approach to nodes where $p_j\to0$;
2. integrability and finiteness of total rates;
3. absence of infinitely many jumps in finite time;
4. measurability in time; and
5. initial distribution.

The finite instantaneous classification does not prove global existence.

---

## 9. Same marginals, different path records

Take a static fair two-state distribution and quantum current $J=0$.

- Minimal current matching gives $S=0$: the configuration never jumps.
- Choose $S_{12}=s>0$: both jump rates are

  $$
  r=\frac{s}{1/2}=2s.
  $$

Both laws retain the fair distribution at every time. But, starting in the
stationary distribution,

$$
P_S(Q_{t+\tau}=Q_t)
=\frac{1+e^{-2r\tau}}2,
$$

whereas the minimal law gives probability one.

The traffic parameter is therefore absent from all single-time marginals but
present in multi-time path records. Whether those path records are physically
available depends on the theory's intervention and apparatus law; inserting a
monitor is not automatically a passive revelation of the unmonitored path.

---

## 10. Graph locality and symmetry do not automatically select minimality

If $H_{ij}=0$, then $J_{ij}=0$. Requiring jumps only on the Hamiltonian graph
forbids traffic on absent edges. It still allows symmetric $S_{ij}>0$ on every
present edge.

Likewise, if a symmetry permutes equivalent edges, one may choose a symmetric,
symmetry-invariant $S$ on those edges. Therefore

$$
\text{Hamiltonian adjacency}+
\text{symmetry}+
\text{equivariance}
$$

does not generally force $S=0$.

Minimality is a genuine additional selection principle, not merely a
restatement of covariance.

---

## 11. What this construction supplies

Conditional on $(\mathcal Q,P,H,\psi,t)$ and a rate selection, the Markov
generator plus initial distribution defines a complete positive path law.
This fills the formal C4 coordinates:

$$
\mathcal X_{\rm act}
=\{\text{configuration paths }Q_t\},
$$

and

$$
\mathsf P_{\rm act}
=\text{the Markov path measure generated by }\sigma.
$$

One sample path can then occur by irreducible chance. No further deterministic
outcome selector is required.

---

## 12. What it imports

The construction does not derive:

1. the configuration carrier $\mathcal Q$;
2. the configuration PVM/POVM $P$;
3. complex state $\psi$;
4. Hamiltonian $H$ and its couplings;
5. the Born density;
6. external time $t$;
7. quantum current rather than another equivariant current;
8. minimality rather than symmetric traffic;
9. the apparatus coupling that turns paths into records;
10. relativistic locality, QFT regularization, or gravity.

It is therefore a complete actuality-law **comparator**, but not yet a native
ordinary-positive explanation of quantum physics.

---

## 13. Relation to Barandes

Integrating a time-dependent Markov generator produces transition matrices

$$
\Gamma(t\leftarrow t_0).
$$

Thus the minimal-current law provides one explicit complete Kolmogorov
realizer and its first-order transition family. But it is deliberately Markov
and depends on phase-complete quantum inputs. It does not derive the generic
indivisible/non-Markovian $\Gamma$ architecture and cannot be attributed to
Barandes without an additional bridge.

Its proper role in v17 is:

1. proof that a positive actual-configuration path law can be mathematically
   complete;
2. a control showing exactly which quantum data can generate it;
3. a classification of what Born marginals and quantum current fail to
   select; and
4. a target against which a genuinely native indivisible law must earn an
   advantage.

---

## 14. Hostile-control battery

1. **Equivariance/current conflation:** infers $K=J$ from equal divergences.
2. **Two-state laundering:** proves uniqueness on two states and generalizes
   past cycle currents.
3. **Counter-traffic deletion:** sets $S=0$ without naming minimality.
4. **Minimality-as-empiricism:** treats least jumps as experimentally selected
   without path records.
5. **Zero-denominator mutant:** divides by $p_j=0$.
6. **Global-existence leap:** promotes instantaneous rates to a complete
   nonexplosive process without proof.
7. **Configuration import:** assumes a preferred PVM because it was used to
   write matrix entries.
8. **Hamiltonian import:** calls the path law native while receiving $H$ and
   $\psi$.
9. **Markov/indivisible conflation:** calls a Bell process a derivation of
   Barandes indivisibility.
10. **Monitor laundering:** treats an inserted path detector as revealing the
    unmonitored experiment.
11. **Stationary-marginal blindness:** compares only $p_t$ and misses traffic.
12. **Symmetry overclaim:** assumes covariance eliminates symmetric traffic.
13. **QFT overclaim:** ignores cutoffs and configuration-observable choices.
14. **Gravity overclaim:** replaces configuration by geometry without solving
    constraint time, gauge, measure, or backreaction.

---

## 15. Exact author verification controls

The finite identities were checked independently of the prose.

### 15.1 Complex continuity control

With $\hbar=1$,

$$
\psi=\frac1{\sqrt3}(1,i,1)^T
$$

and

$$
H=
\begin{pmatrix}
1&1+i&-i\\
1-i&2&2\\
i&2&0
\end{pmatrix},
$$

the exact current matrix is

$$
J=
\begin{pmatrix}
0&2/3&-2/3\\
-2/3&0&-4/3\\
2/3&4/3&0
\end{pmatrix}.
$$

Its row sums are

$$
(0,-2,2),
$$

which equal the independently evaluated $\dot p$ from the Schrödinger
equation. Antisymmetry also holds entrywise.

### 15.2 Exhaustive traffic-decomposition control

For all $4^6=4096$ directed traffic assignments on the six off-diagonal edges
of a three-state carrier with entries in

$$
\{0,1/5,2/5,3/5\},
$$

the reconstruction

$$
K=C-C^T,
\qquad
S_{ij}=\min(C_{ij},C_{ji}),
\qquad
C=K^++S
$$

was exact.

### 15.3 Registered nonselection controls

The two-state example reconstructs rates $(1/2,0)$ and $(3/4,1/4)$ with the
same net current $1/4$. The three-cycle has exactly zero divergence. For the
static symmetric two-state chain, the path-persistence probability remains

$$
\frac{1+e^{-2r\tau}}2,
$$

distinct from the minimal frozen path while preserving the same fair
one-time law.

These checks validate the finite algebra only. They do not test nature or
establish global process existence.

---

## 16. Comparator outcome ladder

| Level | Candidate meaning |
|---|---|
| BC-L0 | current or rate typing fails |
| BC-L1 | finite continuity and equivariant-rate classification survive |
| BC-L2 | standard-current/symmetric-traffic and minimality theorems survive |
| BC-L3 | complete path-law comparator and dependency ledger survive |
| BC-L4 | an independently motivated native current/minimality principle predicts held-out path records |
| BC-L5 | the law scales to interacting QFT and an empirically controlled gravity interface |

BC-L4 and BC-L5 are empty. No native current principle, passive path-record
experiment, or gravity law has been constructed.

---

## 17. Maximum legitimate author-side claim

If the reconstruction survives future independent review:

> On a finite positive-support configuration carrier, every Born-equivariant
> Markov jump law is a choice of an antisymmetric current with the required
> divergence plus arbitrary symmetric traffic. Requiring the full quantum
> current removes divergence-free cycle freedom but leaves symmetric
> counter-traffic. The Bell-type minimal rates are the unique no-counterflow,
> least-jump member. Conditional on the quantum state, Hamiltonian,
> configuration observable, external time, and minimality rule, they supply a
> complete positive actual-configuration path law. They do not derive those
> inputs or select a native ISP ontology.

It would not establish:

1. that the minimal process is nature's ontology;
2. that Born equivariance selects quantum current;
3. that least traffic is a physical law;
4. a Barandes-native indivisible generator;
5. an empirical deviation from quantum mechanics;
6. relativistic QFT without regularization;
7. internal time, spacetime, or gravity.

---

## 18. Author verdict

```text
QUANTUM CONTINUITY:              EXACT / SOURCE-RECONSTRUCTED
BORN EQUIVARIANT CURRENT:        DIVERGENCE ONLY
STANDARD QUANTUM CURRENT:        STRONGER DECLARED INPUT
SYMMETRIC COUNTER-TRAFFIC:       FREE UNDER CURRENT MATCHING
MINIMAL BELL RATES:              UNIQUE NO-COUNTERFLOW MEMBER
COMPLETE POSITIVE PATH LAW:      YES, CONDITIONAL ON QUANTUM INPUTS
NATIVE ISP ACTUALITY LAW:        NOT FOUND
EMPIRICAL MINIMALITY TEST:       NOT CONSTRUCTED
QFT / GRAVITY RESULT:            NONE
SCIENTIFIC RESULT:               NONE
```
