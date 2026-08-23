# ISP v17 — U-Gen C4 interference and actuality obstruction candidate

**Status:** ACTIVE AUTHOR-SIDE MATHEMATICS / NOT A PIN / NOT REVIEWED
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none

---

## 0. Question and result ceiling

C1–C3 isolate a positive diagonal layer, a relational correlation layer, and
the conditional scalar action character

$$
e^{i\kappa s}.
$$

None of those objects yet says what is actual. C4 asks the narrower exact
question:

> When does a strongly positive pair-history law define an ordinary
> probability law for histories or records, and what additional datum is
> required when one claims that a fine history or trajectory is actual?

The answer has four parts.

1. Real interference is exactly the obstruction to identifying the quantum
   measure with a Kolmogorov probability on the same full event algebra.
2. An ordinary probability law exists on a declared record partition exactly
   when the real cross terms vanish on that partition. Full complex
   decoherence is sufficient but stronger than necessary for additivity.
3. Record probabilities do not select probabilities inside hidden record
   fibers.
4. Even a complete family of pairwise first-order transition probabilities
   does not, in general, select a multi-time trajectory law.

The candidate conclusion is therefore not that actuality is impossible and
not that stochastic theories are incomplete because they do not determine a
particular random draw. It is the typed distinction

$$
\boxed{
\text{record probability}
\ne
\text{fine-history probability law}
\ne
\text{one realized sample}.}
$$

Irreducible chance may legitimately stop at the last arrow. It may not be used
to omit the probability law or the physical referent of the sample.

---

## 1. Finite pair-history setup

Let $\Omega$ be a nonempty finite set and let $\mathcal A=2^\Omega$. A
biadditive decoherence functional is a map

$$
D:\mathcal A\times\mathcal A\longrightarrow\mathbb C
$$

that is additive in each argument on disjoint unions. Assume throughout that

1. $D(A,B)=\overline{D(B,A)}$;
2. $D$ is strongly positive, meaning every finite matrix
   $[D(A_i,A_j)]$ is positive semidefinite; and
3. $D(\Omega,\Omega)=1$.

Define the event propensity

$$
\mu(A)=D(A,A)\ge0.
$$

As C2 emphasized, normalization is not $\operatorname{tr}D=1$. On atomic
histories $h_j$ it is

$$
\sum_{j,k}D_{jk}=1.
$$

The diagonal weights $D_{jj}$ therefore need not sum to one and are not
silently called probabilities.

---

## 2. Proposition C4-A — exact interference/additivity equivalence

### Statement

For every two disjoint events $A,B\in\mathcal A$,

$$
\mu(A\cup B)
=\mu(A)+\mu(B)+2\operatorname{Re}D(A,B).
$$

Consequently the following are equivalent:

1. $\mu$ is a finitely additive Kolmogorov probability on all of
   $\mathcal A$;
2. $\operatorname{Re}D(A,B)=0$ for every disjoint $A,B$; and
3. for distinct atomic histories $h_j,h_k$,

   $$
   \operatorname{Re}D_{jk}=0.
   $$

If any disjoint pair has nonzero real interference, no probability measure
$P$ on the same event algebra can satisfy $P(A)=\mu(A)$ for every event.

### Proof

Biadditivity and Hermiticity give

$$
\begin{aligned}
D(A\cup B,A\cup B)
&=D(A,A)+D(B,B)+D(A,B)+D(B,A)\\
&=\mu(A)+\mu(B)+2\operatorname{Re}D(A,B).
\end{aligned}
$$

Thus finite additivity is equivalent to vanishing real cross terms for all
disjoint events. Atomic vanishing is sufficient because every disjoint event
pair is a sum over disjoint atomic pairs, and it is necessary by choosing
singletons. Strong positivity supplies nonnegativity, while the printed
normalization supplies total mass one. QED.

### Scope

This proposition does not say that quantum theory uses negative probability.
It says that $\mu$ is not generally an ordinary additive measure on the fine
event algebra. Ordinary positive probabilities can still exist on suitable
coarse record algebras.

---

## 3. Exact two-history control

Let

$$
D=\frac14
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}.
$$

This matrix is positive semidefinite of rank one and

$$
D(\Omega,\Omega)=\sum_{j,k}D_{jk}=1.
$$

Nevertheless

$$
\mu(\{h_1\})=\mu(\{h_2\})=\frac14,
\qquad
\mu(\Omega)=1.
$$

The two singleton propensities sum to $1/2$, not one. The missing $1/2$ is the
real interference term. No ordinary probability on
$\{\varnothing,\{h_1\},\{h_2\},\Omega\}$ equals this $\mu$ on every event.

This is an exact normalization control against replacing
$D(\Omega,\Omega)=1$ by $\operatorname{tr}D=1$.

### 3.1 Weak-but-not-medium control

Let

$$
D_{\rm wm}=
\begin{pmatrix}
1/2&i/4\\
-i/4&1/2
\end{pmatrix}.
$$

Its eigenvalues are $1/4$ and $3/4$, so it is positive definite, and the sum
of all entries is one. On the singleton partition,

$$
\operatorname{Re}(D_{\rm wm})_{12}=0,
\qquad
(D_{\rm wm})_{12}\ne0.
$$

Thus $\mu$ is the ordinary fair probability on the full two-atom event
algebra even though the pair-history kernel retains a nonzero imaginary
cross term. Probability additivity does not imply that every compositionally
relevant correlation has disappeared.

### 3.2 Total-cancellation-is-not-consistency control

Let

$$
D_{\rm tc}=
\begin{pmatrix}
1/3&1/12&-1/12\\
1/12&1/3&0\\
-1/12&0&1/3
\end{pmatrix}.
$$

Its leading principal minors are positive and

$$
\det D_{\rm tc}=\frac7{216}>0,
$$

so it is positive definite. The off-diagonal real terms cancel in the total:

$$
D_{\rm tc}(\Omega,\Omega)=1,
\qquad
\sum_j(D_{\rm tc})_{jj}=1.
$$

Nevertheless,

$$
\mu(\{h_1,h_2\})
=\frac56
\ne
\frac23
=\mu(\{h_1\})+\mu(\{h_2\}).
$$

Checking only normalization of all record atoms therefore misses
coarse-graining failure.

---

## 4. Proposition C4-B — probability on a declared record partition

Let

$$
\mathcal R=\{R_1,\ldots,R_m\}
$$

be a partition of $\Omega$, and let $\mathcal B(\mathcal R)$ be the Boolean
algebra generated by unions of its cells.

### Statement

The following are equivalent:

1. $\mu$ restricted to $\mathcal B(\mathcal R)$ is an ordinary probability
   measure;
2. for every $i\ne j$,

   $$
   \operatorname{Re}D(R_i,R_j)=0.
   $$

When these conditions hold, the unique probability on the record atoms is

$$
p_i=\mu(R_i),
\qquad
\sum_i p_i=1.
$$

The stronger condition

$$
D(R_i,R_j)=0
\quad(i\ne j)
$$

is often called medium decoherence. It implies the displayed condition but is
not necessary merely for the Kolmogorov sum rules. C4 calls the real-part
condition **weak decoherence/consistency** and prints which condition a claim
uses.

### Proof

Necessity follows by applying Proposition C4-A to every two record cells.
For sufficiency, if $I,J$ are disjoint index sets, biadditivity gives

$$
\operatorname{Re}D
\left(\bigcup_{i\in I}R_i,\bigcup_{j\in J}R_j\right)
=\sum_{i\in I,j\in J}\operatorname{Re}D(R_i,R_j)=0.
$$

Proposition C4-A then gives additivity on the generated algebra. Positivity
and normalization are inherited. QED.

### Two prohibitions

1. The single equation $\sum_i\mu(R_i)=1$ is not enough: it can result from a
   cancellation among several cross terms.
2. Decoherence of one partition does not license probabilities for an
   incompatible refinement. The refinement must pass its own cross-term
   test.

---

## 5. Proposition C4-C — hidden refinement is not selected by records

Let $\pi:H\to I$ be a surjection from a finite hidden-history set to record
labels. Write $H_i=\pi^{-1}(i)$ and let $p$ be a probability on $I$.

### Statement

Every probability $P$ on $H$ with pushforward $\pi_*P=p$ has the form

$$
P(h)=p_i q_i(h),
\qquad h\in H_i,
$$

where $q_i$ is a probability on $H_i$ for every $i$ with $p_i>0$. Conversely,
every such family defines a lift of $p$.

The lift is unique exactly when every positive-probability fiber $H_i$ is a
singleton. If some $p_i>0$ and $|H_i|\ge2$, there are continuum many lifts.

### Proof

For $p_i>0$, define $q_i(h)=P(h)/p_i$. Pushforward equality gives

$$
\sum_{h\in H_i}q_i(h)=1.
$$

The converse follows by summing $p_iq_i$ over each fiber. If a positive fiber
contains two elements, continuously varying their conditional weights while
holding all other coordinates fixed produces continuum many distinct lifts.
QED.

### Consequence

A stable decoherent record law fixes what frequencies and conditional records
are predicted. It does not identify an unobserved microscopic path inside the
record fiber. Choosing uniform weights, maximum entropy, shortest code,
Markov completion, or a preferred basis is an additional rule.

---

## 6. Proposition C4-D — pairwise transition laws do not select a trajectory

The two-target counterexample in Paper 01 already proves that root-conditioned
target marginals do not determine their coupling. The following control is
stronger: even all one- and two-time distributions can agree.

Let $X_1,X_2,X_3\in\{0,1\}$. Define

$$
P_{\rm even}(x_1,x_2,x_3)
=\begin{cases}
1/4,&x_1\oplus x_2\oplus x_3=0,\\
0,&\text{otherwise},
\end{cases}
$$

and

$$
P_{\rm odd}(x_1,x_2,x_3)
=\begin{cases}
1/4,&x_1\oplus x_2\oplus x_3=1,\\
0,&\text{otherwise}.
\end{cases}
$$

### Statement

$P_{\rm even}$ and $P_{\rm odd}$ have identical one-time marginals and
identical two-time joint distributions. Hence every first-order conditional

$$
P(X_j=b\mid X_i=a)=\frac12
\qquad(i\ne j)
$$

agrees wherever it is defined. Yet

$$
P_{\rm even}(X_1\oplus X_2\oplus X_3=0)=1,
$$

while

$$
P_{\rm odd}(X_1\oplus X_2\oplus X_3=0)=0.
$$

Therefore a complete table of pairwise first-order transition laws does not,
in general, determine a Kolmogorov tower on complete trajectories.

### Proof

Fix any values of one or two bits. In either parity sector there are exactly
$2^{3-k-1}$ compatible strings after fixing $k=1$ or $k=2$ bits. With uniform
weight on the four strings, every one-bit distribution is fair and every
two-bit distribution is uniform on four pairs. The three-bit parity event
separates the laws exactly. QED.

### Scope wall

This is not a claim that every first-order law has multiple realizers. It is a
counterexample to universal uniqueness. A law may add a complete Kolmogorov
tower, a higher-order consistency axiom, or a dynamics that uniquely generates
one. That addition must be printed and charged.

---

## 7. Three distinct actuality coordinates

C4 separates three questions that are often compressed into the phrase “one
history actually happens.”

### A. Referent

What is the candidate sample point?

- a completed laboratory record;
- a fine configuration trajectory;
- a truth valuation/coevent;
- a particle configuration plus guiding state;
- a collapse-flash or mass-density history;
- a branch-relative record; or
- no microscopic referent beyond operational records.

### B. Law

What mathematical object supplies chances for that referent?

- a Kolmogorov measure on complete paths;
- first-order $\Gamma$ laws plus an equivalence class of realizers;
- a decoherence functional plus a declared consistent partition;
- a quantum measure plus preclusion/coevent rules;
- modified stochastic dynamics; or
- universal unitary dynamics without a single-history chance law.

### C. Realized sample

Which allowed outcome occurs in one run?

An irreducibly stochastic theory is not required to derive a hidden
deterministic selector for this final draw. Demanding one would merely replace
chance with a seed and move the question. The scientific obligations are to
specify the referent and its probability law, and to say which parts are
empirically identifiable.

---

## 8. Thin and thick trajectory claims

For routing purposes C4 introduces two explicitly local labels. They are not
claims about Barandes's preferred terminology.

1. **Thin event actuality:** only the configurations at licensed targets or
   stable records are asserted as actual. No joint value at every unrecorded
   cut is claimed.
2. **Thick trajectory actuality:** one complete fine path through a declared
   family of boundaries is asserted as actual.

Thin actuality can be compatible with first-order $\Gamma$ without selecting
a full realizer, but it is not a complete microscopic path ontology. Thick
actuality requires either a complete path measure or a clearly stated
non-Kolmogorov actuality rule. Proposition C4-D shows that first-order data do
not supply that object in general.

---

## 9. No inference from occurrence to unique law

The fact that exactly one outcome is recorded in a run does not distinguish
among probability laws that agree on the record algebra. Conversely, the
nonuniqueness of laws does not imply that several outcomes occur in one run.

Formally, let

$$
\Phi_{\rm rec}:\mathcal M\longrightarrow\mathsf{Prob}(I)
$$

map candidate microscopic models to their registered record law. Observing
one actual record, or even identifying $\Phi_{\rm rec}(M)$ exactly, determines
at most the empirical fiber

$$
\Phi_{\rm rec}^{-1}(p).
$$

It does not select a representative unless an experiment refines the quotient
or an independently justified physical principle adds invariant content.

---

## 10. Exact mutant and hostile-control battery

Any future C4 review must test at least these controls.

1. **Trace-normalized mutant:** silently substitutes $\operatorname{tr}D=1$
   for $D(\Omega,\Omega)=1$.
2. **Diagonal-probability mutant:** calls $D_{jj}$ probabilities before
   checking additivity.
3. **Medium/weak conflation:** requires $D(R_i,R_j)=0$ when only real-part
   consistency is claimed, or uses weak consistency to claim loss of all
   phase-sensitive composition data.
4. **Total-cancellation mutant:** checks only $\sum_i\mu(R_i)=1$.
5. **Partition laundering:** transfers probabilities from one decoherent
   partition to an untested refinement.
6. **Uniform-fiber selector:** inserts equal hidden weights by hand.
7. **Maximum-entropy selector:** calls an inference convention a physical law.
8. **Random-seed regress:** treats a sampled seed as an explanation of the
   probability law.
9. **Pairwise-completeness mutant:** assumes all pair marginals determine a
   multi-time distribution.
10. **Outcome/law conflation:** criticizes a stochastic theory merely because
    it does not deterministically derive the realized sample.
11. **Operational-cut invasion:** infers an unmeasured path by inserting a
    measurement that changes the physical experiment.
12. **Decoherence-as-collapse mutant:** treats suppression of record
    interference as selection of one outcome.

---

## 11. Candidate outcome ladder

| Level | Candidate meaning |
|---|---|
| C4-L0 | typed setup or normalization fails |
| C4-L1 | interference identity and finite controls survive |
| C4-L2 | partition probability equivalence survives |
| C4-L3 | hidden-refinement and pairwise-realizer nonselection survive |
| C4-L4 | an independently motivated actuality law is identified and passes held-out operational tests |
| C4-L5 | the law scales uniformly and yields an empirical or invariant advantage over standard quantum descriptions |

C4-L4 and C4-L5 are empty in this candidate. No actuality law has been
constructed or selected.

---

## 12. Maximum legitimate author-side claim

If the mathematics survives future independent review, the maximum claim is:

> For a finite normalized strongly positive pair-history law, real
> interference is exactly the obstruction to treating its quantum measure as
> an ordinary probability on the same event algebra. A declared record
> partition carries ordinary probabilities exactly under weak decoherence,
> but those probabilities do not select hidden within-record histories.
> Moreover, even complete pairwise first-order transition data need not select
> a multi-time Kolmogorov realizer. A one-history ontology must therefore type
> its referent and law separately from the irreducible random occurrence of
> one allowed sample.

It would not establish:

1. that fine histories do or do not exist;
2. that one interpretation of quantum theory is true;
3. that decoherence alone solves the measurement problem;
4. that Barandes's ontology is inconsistent;
5. that a deterministic outcome selector is required;
6. a native U-Gen member;
7. a collapse mechanism;
8. QFT, internal time, spacetime, or gravity.

---

## 13. Author verdict

```text
C4 INTERFERENCE IDENTITY:        EXACT AUTHOR-SIDE
FULL-EVENT KOLMOGOROV LAW:       IFF REAL INTERFERENCE VANISHES
RECORD-PARTITION PROBABILITY:    IFF WEAKLY DECOHERENT
MEDIUM DECOHERENCE:              STRONGER / NOT SILENTLY REQUIRED
HIDDEN RECORD REFINEMENT:        NOT SELECTED
PAIRWISE FIRST-ORDER REALIZER:   NOT UNIQUE IN GENERAL
ACTUAL RANDOM SAMPLE:            MAY BE IRREDUCIBLE CHANCE
ACTUALITY REFERENT AND LAW:      MUST BE TYPED
NATIVE ACTUALITY LAW:            ABSENT
SCIENTIFIC RESULT:               NONE
```
