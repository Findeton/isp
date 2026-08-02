# Independent hostile review B — quantum sufficiency, instruments, and process typing

**Status:** `ACCEPT AT DECLARED SCOPE / MINOR CLARIFICATIONS`

**Review role:** independent quantum-sufficiency, quantum-instrument, and process-typing reviewer

**Repository action:** read-only; no file was edited and no commit was made

## 1. Frozen review surface

I reviewed the following immutable artifacts:

- strict pin commit: `f00140c2d1242acca95023866dbef9c29e493ff2`
- paper commit: `044253de4fa1f66cebc56f15035a4731b00701bb`
- pin SHA-256: `7253d66856330b7f71538c5b7b6e398904a0f9edad4650ab4618091f06a87f1d`
- paper SHA-256: `9e957d1935d0e760e43431e2ed2d154c9370d0e6d1df331bf3815000b9d6a5e3`
- hostile-dispatch SHA-256: `101e5ba466393b0a78a409dd883bdbfb971c11d17928f674e54a2da69360b850`

I also checked the binding predecessor adjudication at `dba40d4a30e476ac0ed5e4fd1e1b484ddcbe6049`, especially its compact-convex Karoubi scope, the center-lift obstruction, and the corrected branch-memory minima.

## 2. Executive verdict

I found no fatal or major defect in the paper’s quantum-sufficiency or instrument claims.

At the explicitly declared finite, ancilla-saturated, same-interface, instrument-complete scope, the paper does construct:

1. a matrix-ordered effect dual of the earned minimal Karoubi process boundary; and
2. a unique finest admitted exact nondisturbing, exclusive, repeatable classical instrument.

The construction does not silently restore an algebraic center. Its primitive classical object is a complete flagged instrument. The outcome effects and postmeasurement branches remain typed, and physical admission is not inferred from abstract complete positivity alone.

The strongest justified disposition is therefore:

\[
\boxed{
\begin{aligned}
\texttt{RQ0-L0-MATRIX-ORDERED-MINIMAL-BOUNDARY}
&\quad\text{EARNED AT THE DECLARED ANCILLA-SATURATED SCOPE},\\
\texttt{RQ0-L0-OPERATIONAL-CLASSICAL-CORE}
&\quad\text{EARNED AT THE DECLARED INSTRUMENT-COMPLETE SCOPE}.
\end{aligned}
}
\]

`RQ0-L0-BLOCKED-AT-OPERATIONAL-CENTER` is not selected inside that positive scope. It remains the correct registered outcome for a law that fails complete-kernel compatibility or the required physical instrument closure.

The result is task-relative and one-chart-relative. It does not earn W3 selection, an actual record value, locality, overlap, topology, or causality.

## 3. Use of the predecessor theorem

The paper uses the predecessor minimum only as the adjudication permits:

\[
B_{\mathfrak F}=(X,e)
\in\operatorname{Kar}(\mathsf{Proc}_D).
\]

It does not assume that this object already has:

- an observable multiplication;
- a center;
- a tensor factorization;
- autonomous controls;
- a record PVM; or
- a spatial interpretation.

The new matrix structure is built from admitted ancillary tester data. The minimum idempotent is lifted only after imposing the complete-kernel gate. Ancilla saturation is printed as a physical scope condition, not presented as a theorem about arbitrary laboratory grammars.

This preserves the predecessor’s exact ontology: \(B_{\mathfrak F}\) is initially only a minimal repeatable process coarse-graining for a fixed future experiment.

## 4. Instrument and variance audit

### 4.1 Schrödinger and Heisenberg types

The pin begins with process branches

\[
M_r:B\longrightarrow B.
\]

Their Heisenberg pullbacks are

\[
m_r=M_r^\sharp:S\longrightarrow S,
\qquad
S=\mathcal E(B).
\]

The variance is correct. For a state \(\rho\) on \(S\), the subnormalized outcome branch is

\[
\rho_r=\rho\circ m_r,
\]

and its probability is

\[
\rho_r(1)=\rho(m_r(1))=\rho(q_r),
\qquad
q_r=m_r(1).
\]

The complete flagged Schrödinger map has type

\[
\widehat{\mathcal M}:B\longrightarrow\bigoplus_r B.
\]

Dually, the flagged Heisenberg map has type

\[
\widehat{\mathcal M}^{\sharp}:
\bigoplus_r S\longrightarrow S.
\]

The paper represents this map by its CP coordinate branches \(m_r\). Although the full direct-sum arrow is not printed every time, no variance reversal is used in a proof.

### 4.2 Forgetting the outcome

The condition

\[
\sum_r m_r=I_S
\]

means exactly that forgetting the retained classical outcome leaves the entire minimal effect boundary unchanged. Consequently,

\[
\sum_r\rho\circ m_r=\rho
\]

for every state \(\rho\), not merely for the distinguished experiment states.

This is stronger than merely leaving the parameter family invariant. It is appropriate on the rigid minimal boundary: an admitted deterministic endomorphism preserving the whole minimal experiment must be its identity.

### 4.3 Repeatability and exclusivity

The branch law

\[
m_sm_r=\delta_{sr}m_r
\]

is correctly typed. Relabelling \(r\leftrightarrow s\) also gives the equivalent opposite-order expression required when translating a sequential Schrödinger experiment into Heisenberg composition.

For two successive measurements,

\[
\Pr(s\text{ second},r\text{ first}\mid\rho)
=
\delta_{sr}\rho(q_r).
\]

Thus:

- a repeated read returns the same outcome;
- different outcomes are exclusive;
- the branch retains its postmeasurement process;
- summing the outcome recovers the unconditioned identity process.

No multiplication among the \(q_r\) is used. The Boolean algebra resides in the retained external outcome flag, exactly as the pin requires.

## 5. Maximality of the core

### 5.1 Every relevant instrument branch is captured

Let \(\{m_r\}_{r\in\Omega}\) be any admitted instrument satisfying the paper’s exact nondisturbance, exclusivity, and repeatability conditions.

For each \(r\),

\[
I_S-m_r=\sum_{s\neq r}m_s
\]

is CP. Under admitted classical coarse-graining, the two-outcome family

\[
\{m_r,I_S-m_r\}
\]

is an admitted flagged instrument. Therefore every branch of every instrument in the declared target class is an operational split projection.

There is no hidden restriction to a preselected family of maps.

### 5.2 No incomparable finest instruments survive closure

I tried to construct two incomparable finest instruments.

Let \(P\) and \(Q\) be branches from two admitted split instruments. Since \(P,I-P,Q,I-Q\) are positive, their ranges are complementary order ideals. Each map preserves both ideals of the other, forcing

\[
PQ=QP.
\]

Sequentially performing the two physical instruments produces the four CP branches

\[
PQ,\quad
P(I-Q),\quad
(I-P)Q,\quad
(I-P)(I-Q).
\]

They are exclusive, sum to the identity, and retain the joint flag. This is an admitted common refinement under the paper’s explicit sequential-composition closure.

Iterating the construction over the finite family of split projections yields the atomic joint instrument. Therefore two incomparable finest instruments cannot remain once the declared physical closure is enforced.

If sequential experiments are unavailable, this conclusion fails, and the paper correctly treats that as a different operational law rather than pretending that the refinement is admitted.

### 5.3 Finiteness and uniqueness

All split projections commute and are diagonalizable idempotents on one finite-dimensional vector space. In a common eigenbasis each has only zero and one as diagonal entries. Hence only finitely many distinct split projections exist.

Their Boolean atoms:

- are admitted CP branches;
- are pairwise exclusive;
- sum to the identity;
- form one complete retained instrument; and
- refine every other admitted exact repeatable instrument.

The finest instrument is unique up to outcome permutation.

### 5.4 Failed counterexamples

Several natural counterexamples do not defeat the theorem.

**Random coin.** On a factor, branches \(m_r=\lambda_rI\) can sum to \(I\), but repeatability requires

\[
\lambda_r^2=\lambda_r.
\]

Only one nonzero unit coefficient survives. A noisy random flag is nondisturbing but is not an exact repeatable record.

**Lüders measurement in \(M_d\).** The branches \(a\mapsto P_raP_r\) are repeatable, but their sum is the dephasing channel, not the identity on \(M_d\). It is therefore not nondisturbing for the entire minimal factor.

**Two incompatible sharp instruments.** Complementary positivity makes their branches order projections, so the commutation theorem rules them out at the declared scope.

**Different outcome spaces.** The theorem concerns exact repeatable endomorphism instruments on the same minimal boundary. Outcome-specific interfaces not re-encodable as such endomorphisms lie outside the registered scope rather than refuting it.

## 6. Finite quantum-statistical controls

### 6.1 Classical algebra

For

\[
A=\mathbb C^n,
\]

the coordinate-sector maps form \(n\) mutually exclusive CP branches summing to the identity. With the standard filters admitted, the operational core is the complete \(n\)-point classical experiment.

### 6.2 Full quantum factor

For \(A=M_d\), if \(P\) and \(I-P\) are CP, then

\[
0\le J(P)\le J(I).
\]

Since \(J(I)\) has rank one, \(J(P)=\lambda J(I)\), so \(P=\lambda I\). Idempotence forces \(\lambda\in\{0,1\}\).

Thus the exact repeatable operational core of a full factor is trivial. This agrees with the no-information-without-disturbance intuition: a full irreducible quantum experiment has no nontrivial classical sector readable while its entire process is unchanged.

### 6.3 Mixed algebra

For

\[
A=M_2\oplus\mathbb C,
\]

the standard central filters produce two core outcomes. They reveal only the direct-sum sector. They do not resolve the qubit state inside \(M_2\).

### 6.4 Physically unavailable center

For an abstract \(\mathbb C^2\) whose coordinate filters are not admitted process branches, no two-outcome physical core follows. The only nonzero core atom is the identity.

This control is load bearing. It shows that the paper maximizes over admitted instruments, not over mathematical decompositions of an ambient representation.

## 7. Koashi–Imoto and Kuramochi comparison

At the explicitly restricted state-experiment scope, the recovery claim is correct.

For a finite family of states in minimal sufficient form,

\[
H\simeq
\bigoplus_r H_r^Q\otimes H_r^N,
\]

\[
\rho_\theta\simeq
\bigoplus_r
p(r\mid\theta)\,
\rho_{\theta,r}^Q\otimes\omega_r^N,
\]

the minimal observable algebra is abstractly

\[
M_{\min}\simeq
\bigoplus_r B(H_r^Q).
\]

Equivalently, in the displayed representation it is

\[
\bigoplus_r B(H_r^Q)\otimes I_{H_r^N}.
\]

With all standard central-sector instruments admitted, the atomic core maps are multiplication by the minimal central block units. Their probabilities are precisely

\[
p(r\mid\theta).
\]

No exact repeatable nondisturbing branch resolves an irreducible \(B(H_r^Q)\) factor, and the \(H_r^N\) degrees of freedom are statistically redundant.

Therefore the operational core agrees with the Koashi–Imoto/Kuramochi classical part at this ordinary operator-algebraic scope. The paper does not extend the state theorem by fiat to arbitrary Karoubi process boundaries; it uses it only as a comparison control.

## 8. Corrected branch-memory audit

The paper retains the common failure sink and does not postselect it away.

### Preserving task

All source labels induce the same complete preserving experiment, so the corrected minimum is

\[
M_{\mathrm{pres}}=\mathbb C.
\]

Its core is trivial.

### Eraser task

The outcome laws are

\[
q_j(\bot)=\frac34,
\qquad
q_j(k)=\frac14\delta_{jk}.
\]

The five likelihood vectors—one common failure vector and four label-specific success vectors—are distinct minimal classical classes. Hence

\[
M_{\mathrm{erase}}=\mathbb C^5.
\]

Its standard core is the complete five-outcome eraser experiment, not a selected inherited memory partition.

### Retained tomographic task

The corrected minimum is

\[
M_{\mathrm{tomo}}=M_4\oplus\mathbb C.
\]

Its standard core distinguishes only:

\[
\text{success},\qquad\text{failure}.
\]

For every source label \(j\), this core has distribution

\[
\left(\frac14,\frac34\right).
\]

It therefore contains no classical correlation with \(j\).

The paper’s negative conclusion is correct:

\[
\boxed{
\text{none of these three task-relative cores selects the familiar W3
memory seam, an inherited partition seam, or the additional complex seam.}
}
\]

The operational-core theorem resolves center lift for a fixed task. It does not resolve task selection.

## 9. Task selection and actuality audit

I found no task-selection or actuality overclaim.

The paper repeatedly and correctly separates:

\[
\text{fixed future task}
\neq
\text{task-independent W3 boundary},
\]

and

\[
\text{classical outcome interface}
\neq
\text{selected actual outcome}.
\]

It also makes no claim of:

- W6 fact co-reference;
- token identity;
- autonomous subsystem control;
- physical overlap;
- spatial locality; or
- causal order.

The word “boundary” remains explicitly restricted to a task-relative process interface inside one chart.

## 10. Findings by severity

### Fatal findings

None.

### Major-but-bounded findings

None.

### Minor finding B1 — ambiguous marginal wording in Proposition 4.2

The sentence

> “Forgetting either flag leaves the state of every admitted effect in \(S\) unchanged”

is potentially read as saying that a state conditioned on the other retained outcome equals the original state. That is not the calculation.

The exact identities are:

\[
\sum_s \rho\circ m_rm_s=\rho\circ m_r,
\]

\[
\sum_r \rho\circ m_rm_s=\rho\circ m_s,
\]

and only after forgetting both outcomes does one recover \(\rho\).

The proof uses the correct marginal equations. The sentence should be read as: forgetting either one of two repeated flags leaves the other one-run marginal unchanged. This is a wording issue and does not affect any rung.

### Scope clarification B2 — “admitted CP branch” must retain its process predual

A CP endomorphism of the abstract operator system is not physical merely because it is mathematically CP.

For the theorem’s operational interpretation, an admitted \(m_r:S\to S\) must be the tester pullback of an admitted process branch \(M_r:B\to B\), and the complete flagged family must exist in the physical process category.

The pin requires this, the paper repeatedly says “admitted,” and the unavailable-\(\mathbb C^2\) control enforces it. The adjudication should retain this as part of the rung’s exact meaning.

### Scope clarification B3 — maximality is exact and repeatable

The core is maximal among finite instruments satisfying all of:

- same-boundary process typing;
- complete retained flag;
- exact unconditioned identity;
- exact exclusivity;
- exact repeatability; and
- the declared physical closure.

It does not classify every noisy, approximate, one-shot, or merely state-family-preserving measurement. This restriction is explicit and scientifically appropriate, but it is load bearing.

### Scope clarification B4 — state-level recovery requires standard admission

Recovery of the Koashi–Imoto/Kuramochi classical part requires the standard central-sector instruments to be physically admitted. It is not a theorem that every abstract minimal process object comes with those branches.

The paper states this qualification correctly.

## 11. Rung grading

| Registered outcome | Grade | Reason |
|---|---|---|
| `RQ0-L0-MATRIX-ORDERED-MINIMAL-BOUNDARY` | **EARNED AT DECLARED SCOPE** | The inherited Karoubi minimum is not promoted to an algebra; admitted ancilla-complete testers supply the matrix order, and complete-kernel compatibility is an explicit gate. |
| `RQ0-L0-OPERATIONAL-CLASSICAL-CORE` | **EARNED AT DECLARED SCOPE** | Every admitted exact repeatable branch is a split projection; all such projections commute; physical closure constructs their joint refinement; finite atoms give the unique finest complete instrument. |
| `RQ0-L0-BLOCKED-AT-OPERATIONAL-CENTER` | **NOT SELECTED IN THE POSITIVE SCOPE** | No instrument-typing or sufficiency counterexample blocks the theorem under its printed assumptions. The blocked result remains correct when those assumptions fail. |

## 12. Exact disposition

\[
\boxed{\texttt{ACCEPT AT DECLARED FINITE SCOPE}}
\]

with one minor wording clarification and three binding scope clarifications.

The exact scientific endpoint is:

\[
\boxed{
\text{fixed future task}
\longrightarrow
\text{minimal sufficient Karoubi process boundary}
\longrightarrow
\text{unique finest admitted exact nondisturbing repeatable classical
instrument}.
}
\]

This endpoint is not a W3 seam, an actual fact, a local chart, or spacetime.
