# ISP v17 — E-Comp root readiness audit

**Status:** ACTIVE AUTHOR-SIDE ROOT AUDIT / NOT INDEPENDENT REVIEW
**Date:** 2026-08-23
**Scientific result awarded:** none
**Official authority created:** none

This audit independently rebuilds the revised E-Comp candidate after replacing
the artificial parity completion by a second fixed-unitary coherent
completion. It determines whether the private object is suitable for a future
authorization decision. It does not freeze bytes, dispatch reviewers, or
accept a theorem.

---

## 1. Root disposition

```text
EXACT ALGEBRA:                         PASS AUTHOR-SIDE
PROBABILITY/RECORD SEMANTICS:          PASS AUTHOR-SIDE
NONDIVISION AGAINST ALL 2-STATE K:     PASS AUTHOR-SIDE
COHERENT ENDPOINT-FIBER CLASSIFICATION: PASS AUTHOR-SIDE
ENDPOINT QUOTIENT NO-CONGRUENCE:        PASS AUTHOR-SIDE
FINITE UNIFORMITY:                     PASS AUTHOR-SIDE
ISOLATED-ENDPOINT GAUGE SCOPE:         PASS WITH BINDING DISTINCTION
BARANDES FIXED-LAW REFUTATION:         NO
PHYSICAL HADAMARD IDENTIFICATION:      NOT IN THE ANTECEDENT
FUTURE PIN READINESS:                  READY FOR AUTHORIZATION DECISION
INDEPENDENT REVIEW:                    REQUIRED
SCIENTIFIC RESULT:                     NONE
```

The revised construction is materially stronger than the discarded parity
version. Both separated nondivisible completions now arise by repeatedly using
one fixed unitary. The result no longer depends on an ad hoc empirically false
positive sequence.

The maximum legitimate future theorem remains narrow:

> A positive endpoint matrix, even together with carrier-relative
> nondivision and fixed-unitary uniformity, does not determine its
> phase-sensitive sequential law; indeed, the endpoint equivalence is not a
> congruence for sequential composition.

---

## 2. Exact antecedent

The base packet contains:

1. the configuration carrier $\mathcal C=\{0,1\}$;
2. basis preparations $p_j(i)=\delta_{ij}$;
3. one syntactic balanced primitive $b$ with isolated endpoint matrix

   $$
   G
   =
   \frac12
   \begin{pmatrix}
   1&1\\
   1&1
   \end{pmatrix};
   $$

4. a nondestructive configuration measurement

   $$
   P_m(i',r\mid i)=\delta_{i'i}\delta_{ri};
   $$

5. a final basis reader $P_f(r\mid i)=\delta_{ri}$; and
6. the declaration that $m$, but not an unmeasured $b$ boundary, is a division
   event.

The base packet does **not** contain a phase lift, a Hamiltonian, a repeated
gate law, a whole-word response table, or a statement that the symbol $b$ is a
fully calibrated laboratory Hadamard. Reading any of those into the antecedent
would beg the question.

---

## 3. Algebraic reconstruction

### 3.1 Standard-H completion

Let

$$
H
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
$$

Direct multiplication gives

$$
H^\dagger H=I_2,
\qquad
H^2=I_2,
\qquad
|H|^{\odot2}=G.
$$

Hence

$$
\Gamma^Q_n
=
|H^n|^{\odot2}
=
\begin{cases}
I_2,&n\text{ even},\\
G,&n\text{ odd}.
\end{cases}
$$

### 3.2 Markov completion

Because

$$
G^2
=
\frac14
\begin{pmatrix}
2&2\\
2&2
\end{pmatrix}
=G,
$$

the positive-kernel completion is

$$
\Gamma^M_0=I_2,
\qquad
\Gamma^M_n=G\quad(n\ge1).
$$

### 3.3 Alternative fixed-unitary completion

Let

$$
X=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad
V
=
e^{-i\pi X/4}
=
\frac1{\sqrt2}(I_2-iX)
=
\frac1{\sqrt2}
\begin{pmatrix}
1&-i\\
-i&1
\end{pmatrix}.
$$

Using $X^2=I_2$,

$$
V^\dagger V
=
\frac12(I_2+iX)(I_2-iX)
=I_2,
$$

and

$$
V^2
=
\frac12(I_2-iX)^2
=-iX,
\qquad
V^4=-I_2.
$$

Every entry of $V$ has squared modulus $1/2$, so

$$
|V|^{\odot2}=G.
$$

The complete positive rule is therefore

$$
\Gamma^V_n
=
|V^n|^{\odot2}
=
\begin{cases}
G,&n\text{ odd},\\
X,&n\equiv2\pmod4,\\
I_2,&n\equiv0\pmod4.
\end{cases}
$$

The $n=0$ case belongs to the last branch.

### 3.4 Normalization and primitive agreement

$I_2$, $X$, and $G$ have nonnegative entries and unit column sums. Thus every
$\Gamma^a_n$, $a\in\{Q,M,V\}$, is column stochastic. Moreover,

$$
\Gamma^Q_0=\Gamma^M_0=\Gamma^V_0=I_2,
$$

and

$$
\Gamma^Q_1=\Gamma^M_1=\Gamma^V_1=G.
$$

All three completions therefore share every stochastic datum in the base
packet.

---

## 4. Operational separators

At the unmeasured two-step word $bb$,

$$
\Gamma^Q_2=I_2,
\qquad
\Gamma^M_2=G,
\qquad
\Gamma^V_2=X.
$$

For preparation $0$, the final distributions are respectively

$$
(1,0),
\qquad
(1/2,1/2),
\qquad
(0,1).
$$

Consequently,

$$
d_{\rm TV}(Q,M)=\frac12,
\qquad
d_{\rm TV}(V,M)=\frac12,
\qquad
d_{\rm TV}(Q,V)=1.
$$

The reader is measure determining on the two-point configuration carrier. The
separator cannot be dismissed as an unread or gauge-only coordinate.

The held-out table follows without new inputs:

| $n$ | $\Gamma^Q_n$ | $\Gamma^M_n$ | $\Gamma^V_n$ |
|---:|---|---|---|
| 3 | $G$ | $G$ | $G$ |
| 4 | $I_2$ | $G$ | $I_2$ |
| 6 | $I_2$ | $G$ | $X$ |
| 7 | $G$ | $G$ | $G$ |
| 8 | $I_2$ | $G$ | $I_2$ |
| 10 | $I_2$ | $G$ | $X$ |

The recurrence both separates and reconverges. It is not a depth-two patch.

---

## 5. Strong nondivision proof

The Markov completion is divisible at the intermediate carrier because

$$
\Gamma^M_2=G^2.
$$

For either coherent completion, suppose the unmeasured intermediate
configuration were a division event. Then some column-stochastic continuation
$K$ would have to satisfy

$$
\Gamma_2=KG.
$$

But

$$
\operatorname{rank}(KG)
\le
\operatorname{rank}(G)
=1,
$$

whereas

$$
\operatorname{rank}(I_2)
=
\operatorname{rank}(X)
=2.
$$

Therefore neither $Q$ nor $V$ factors through **any** stochastic continuation
on the printed two-state carrier. The proof does not assume time homogeneity or
that the later factor equals $G$.

This is the exact sense in which both completed laws are nondivisible at the
unmeasured cut.

The statement is not dimension independent. A larger hidden intermediate
carrier may permit a factorization. Such a dilation changes the declared
ontology and is an explicit outside branch, not a counterexample to the
carrier-relative result.

---

## 6. Actual measurement/division control

For the measured program

$$
\mathtt{prep}_0;b;m;b;r,
$$

the first block gives

$$
P(R_1=a)=\frac12.
$$

The physical reader copies the configuration and starts the next conditioned
block from $a$. Since the one-step endpoint matrix is $G$ in every completion,

$$
P(R_2=c\mid R_1=a)=\frac12.
$$

Thus all three laws give the same complete retained-record distribution,

$$
P(R_1=a,R_2=c)=\frac14
\qquad(a,c\in\{0,1\}).
$$

The unmeasured separation and the measured-middle agreement are therefore both
real consequences of one block/division semantics. No cached mixture or
discarded record is used.

For longer programs, already retained records remain literal prefixes and each
post-measurement block begins from its positive-support recorded
configuration. No joint trajectory is asserted inside an unmeasured block.

---

## 7. Uniformity audit

Each completion has one finite evaluator:

1. $Q$: compute the parity of $n$ or power the fixed algebraic matrix $H$;
2. $M$: return $I_2$ at $n=0$ and $G$ otherwise; and
3. $V$: reduce $n$ modulo $4$ or power the fixed algebraic matrix $V$.

No per-depth array, oracle digit sequence, target-process input, or post-result
parameter is needed. This proves syntactic uniformity only. It does not prove
that one rule is ontologically simpler, physically cheaper, or selected by
nature.

---

## 8. Source-faithful scope

The primary Barandes formulation supplies, for each model:

1. a fixed configuration space;
2. contingent standalone probabilities;
3. first-order transition matrices from allowed division events to arbitrary
   target times; and
4. no general requirement that an intermediate target be a division event.

Its minimal law of total probability is exactly the endpoint relation

$$
p(t)=\Gamma(t\leftarrow t_0)p(t_0).
$$

At that minimal discrete-block scope, all three E-Comp families are legitimate
first-order endpoint assignments. $Q$ and $V$ are individually unistochastic;
$M$ is an ordinary divisible stochastic control. If a future reviewer insists
that the word “indivisible” exclude every divisible model, $M$ may be removed
from the strict subclass without affecting the $Q/V$ nondivision theorem.

Barandes may instead declare the complete $\Gamma(t\leftarrow t_0)$ at every
target as part of one fixed physical law. If so, the law already contains the
choice among $I_2$, $G$, $X$, or another endpoint at the two-step target.
E-Comp does not refute that model. It proves only that this choice is not
derived from the isolated matrix $G$ or from nondivision.

The source usually treats target time as continuous and assumes an identity
limit when continuity is intended. E-Comp is a discrete typed program lemma;
it makes no continuous-time, time-reversal, Hamiltonian, or internal-clock
claim.

Primary source checked:

- Jacob A. Barandes, *Quantum Systems as Indivisible Stochastic Processes*,
  arXiv:2507.21192v1, especially Sections 2.2, 3.1, 3.5, and the axioms in
  Section 5: <https://arxiv.org/html/2507.21192v1>.

---

## 9. Gauge and physical-identification audit

$H$ and $V$ are different phase lifts of the same isolated positive matrix
$G$. At the isolated endpoint, the lift is not observable and must not be
declared ontic.

Explicitly,

$$
V
=
H\odot
\begin{pmatrix}
1&-i\\
-i&-1
\end{pmatrix},
$$

whose second factor has entrywise unit modulus.

The completed laws are different objects:

$$
|H^2|^{\odot2}=I_2,
\qquad
|V^2|^{\odot2}=X.
$$

With the same physical preparation and final configuration reader, they give
different retained outcome probabilities. A legitimate gauge transformation
of one complete representation must transform the entire experiment while
preserving those probabilities. It cannot turn this separator into equality
while leaving the physical reader frozen.

The correct conclusion is therefore not “the phase of $H$ is physical.” It is:

> The isolated stochastic endpoint packet omits the cross-depth
> phase/composition alignment required to determine the complete law.

If the antecedent were enlarged to include full process tomography of a
laboratory Hadamard—including its phase-sensitive continuations—then $V$ would
no longer be an admissible realization of that calibrated primitive. That
would be additional empirical input and would make this particular
nonselection question disappear by supplying the missing datum.

### 9.1 Exact no-congruence theorem

Define the positive endpoint map on a fixed configuration basis by

$$
q(U)=|U|^{\odot2}.
$$

The E-Comp example is the exact failure of $q$ to preserve multiplication:

$$
q(H)=q(V)=G,
$$

but

$$
q(H^2)=I_2,
\qquad
q(V^2)=X,
\qquad
q(H)^2=q(V)^2=G.
$$

Define $U\sim V$ iff $q(U)=q(V)$. If this equivalence were a congruence, then
$H\sim V$ twice would imply $HH\sim VV$. It does not, because $q(H^2)=I_2$
and $q(V^2)=X$. Equivalently, if a binary operation $\star$ on endpoint images
satisfied $q(U_2U_1)=q(U_2)\star q(U_1)$ universally, the common input pair
$(G,G)$ would have to map to both $I_2$ and $X$. No such operation exists.

Thus isolated endpoint laws form a quotient that forgets data needed by
sequential composition. A phase-sensitive theory needs more than a pointwise
choice of lift. It needs a rule that transports or aligns the missing
composition information across wiring, tensor product, intervention,
conditioning, and measurement, while remaining invariant under genuine
complete-representation gauge changes.

### 9.2 Constructive clue: a composition lift

One possible mathematical target is therefore a functorial or cocyclic
**composition lift** over the typed experiment category:

1. its projection gives the positive endpoint law;
2. its composition gives the correct whole-program law;
3. different gauge choices give naturally equivalent complete experiments;
4. it is uniform across program size and system composition; and
5. it is fixed nomological data rather than a per-experiment answer table.

Calling some realizations a “connection” is presently an analogy and a
classification target, not an accepted physical field. Nothing here
identifies the lift with a gauge field, spacetime connection, gravitational
connection, or ontic complex amplitude. Those identifications would require
independent operational and dynamical evidence.

### 9.3 Exact balanced-lift family

The two coherent witnesses belong to the family

$$
U_\theta
=
\frac1{\sqrt2}
\begin{pmatrix}
1&e^{i\theta}\\
e^{i\theta}&-e^{2i\theta}
\end{pmatrix}.
$$

The two columns have unit norm and inner product zero, so $U_\theta$ is unitary
for every real $\theta$. Also

$$
q(U_\theta)=G
$$

for every $\theta$. Direct multiplication gives

$$
q(U_\theta^2)
=
\begin{pmatrix}
\cos^2\theta&\sin^2\theta\\
\sin^2\theta&\cos^2\theta
\end{pmatrix}.
$$

$\theta=0$ gives the $H$ witness and $\theta=-\pi/2$ gives the $V$ witness.
Except when $\cos^2\theta=1/2$, the two-step matrix has rank two and is
nondivisible through the rank-one carrier $G$.

Thus the isolated positive endpoint fiber contains a continuum of coherent
composition outcomes. This is an algebraic classification statement. Only
computable or otherwise physically specified $\theta$ values belong to the
finite-effective law stratum; the exact E-Comp witnesses use fixed algebraic
values and do not depend on a noncomputable parameter.

---

## 10. Hostile reconstruction

### A1 — “$V$ is an invented nonquantum law”

Refuted. $V$ is one fixed unitary and its entire family is obtained by unitary
powers followed by the Born endpoint map.

### A2 — “$H$ and $V$ are gauge, so the separator is fake”

Refuted at complete-law scope. They are indistinguishable at the isolated
endpoint but yield different final physical record laws after two uses. The
missing object is the consistent composition/gauge connection.

### A3 — “A different stochastic intermediate kernel may factor $I$ or $X$”

Refuted by rank: every $KG$ has rank at most one.

### A4 — “The Markov control is not indivisible”

True but nonblocking. $M$ witnesses endpoint nonselection; the $Q/V$ pair alone
witnesses nondivision nonselection.

### A5 — “The symbol $b$ already means Hadamard”

Refuted by the printed grammar. It means a balanced positive endpoint. Full
Hadamard calibration is deliberately absent.

### A6 — “Known experiments choose $H$”

Correct after complete calibration. That selects a member empirically; it does
not derive the member from $G$ or from nondivision.

### A7 — “The law lacks a joint microscopic trajectory”

Correct and scoped. The candidate supplies first-order laws from division
records to targets, matching the minimal indivisible interface. It makes no
Kolmogorov-tower or hidden-path claim.

### A8 — “Measurement merely deletes interference by fiat”

The measurement is an explicitly registered physical record operation. The
candidate assumes its division status as part of the base control; it does not
derive decoherence universally. This is sufficient for the paired control but
cannot earn a measurement theory.

### A9 — “The recurrence is a lookup table”

Refuted. $H$, $G$, and $V$ are fixed finite evaluators. The held-out values are
algebraic consequences.

### A10 — “One successful lemma supplies the universal stochastic generator”

Refuted. The lemma identifies missing phase-composition information. It does
not construct the principle that supplies it for arbitrary instruments,
systems, or interactions.

### A11 — “A dilation defeats the theorem without changing the model”

Refuted as stated. A larger intermediate carrier is a new extension and must be
registered and charged. The candidate makes no no-dilation claim.

---

## 11. Reality-identification accounting

The candidate would not shrink the empirical equivalence class after complete
Hadamard data are included; those data already distinguish the three rules.
Its gain is instead a necessity/nonselection result:

$$
\boxed{
G
+\text{ carrier-relative nondivision}
+\text{ fixed-unitary uniformity}
\not\Rightarrow
\text{ calibrated phase-sensitive law}
}.
$$

This identifies a missing physical input more sharply than the discarded
parity construction. It also prevents a future theory from claiming that the
word “indivisible” alone explains quantum interference.

The next constructive question, outside E-Comp, is whether an independently
motivated stochastic-native principle generates the phase-sensitive family
without importing a Hilbert process table. That is the later U-Gen question,
not an earned result.

---

## 12. Authorization recommendation

E-Comp is now suitable for a future narrow authorization decision. Its private
manifest hashes and format checks have been rebuilt. A valid authorization
would cover only:

1. exact pin freeze;
2. three blind reviews under the drafted contract; and
3. one terminal adjudication.

It should not authorize a replacement completion after freeze, an automatic
v2, Paper 04B repair, Paper 05, chronology, spacetime, gravity, code, or a claim
about Barandes beyond the printed source scope.

Q-Cut remains the higher-leverage next scientific unit because it supplies a
scalable information lower bound. E-Comp is the cleaner prior lemma: it locates
the phase-composition datum that endpoint positivity and nondivision fail to
provide.

Present state:

```text
ACTIVE AUTHOR-SIDE ROOT AUDIT COMPLETE
NO BYTES FROZEN
NO REVIEWS DISPATCHED
NO RESULT ACCEPTED
NO OFFICIAL UNIT OPENED
```
