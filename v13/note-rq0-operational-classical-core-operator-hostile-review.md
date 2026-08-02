# Independent hostile review A — operator systems and matrix order

**Status:** `COMPLETE / REPOSITORY-READ-ONLY`

**Review role:** finite-dimensional operator systems, matrix-ordered duality, completely positive maps, CP order projections, \(C^*\)-envelopes

**Date:** 2026-08-01

## Frozen review surface

| Artifact | Immutable identifier | SHA-256 |
|---|---|---|
| strict pin | `f00140c2d1242acca95023866dbef9c29e493ff2` | `7253d66856330b7f71538c5b7b6e398904a0f9edad4650ab4618091f06a87f1d` |
| analytical paper | `044253de4fa1f66cebc56f15035a4731b00701bb` | `9e957d1935d0e760e43431e2ed2d154c9370d0e6d1df331bf3815000b9d6a5e3` |
| hostile protocol | `43a624d773070c5cc3e07db6a73d75170555e94f` | `101e5ba466393b0a78a409dd883bdbfb971c11d17928f674e54a2da69360b850` |
| dispatch ledger | `91a7c5b308aa7dbef03bf5c95c43cb89adc85e5d` | not a scientific input |

I inspected the binding predecessor adjudication and independently reconstructed the operator-system, order-projection, finite-\(C^*\), and hostile operator-system arguments. I did not use either concurrent review.

# Executive verdict

\[
\boxed{\texttt{ACCEPT}}
\]

at the paper’s explicitly stated conditional scopes.

I found no operator-system or matrix-order counterexample to either positive rung. The two cumulative results are earned as follows:

\[
\boxed{
\begin{aligned}
\texttt{RQ0-L0-MATRIX-ORDERED-MINIMAL-BOUNDARY}
&:\ \textbf{EARNED AT FINITE ANCILLA-SATURATED SCOPE},\\
\texttt{RQ0-L0-OPERATIONAL-CLASSICAL-CORE}
&:\ \textbf{EARNED AT FINITE INSTRUMENT-COMPLETE SCOPE}.
\end{aligned}}
\]

The registered blocked result

\[
\texttt{RQ0-L0-BLOCKED-AT-OPERATIONAL-CENTER}
\]

is not selected at that scope.

This is a conditional operational theorem, not a universal theorem about every compact-convex Karoubi boundary. In particular, ancilla saturation, existence of a completely positive superchannel representative, and sequential/coarse-graining admission remain genuine hypotheses. The paper states those limitations rather than deriving them.

# 1. Complete tester dual

Let \(V_B\) carry the admitted matrix cones \(K_n(B)\). For a matrix of linear effects \(F=[f_{ij}]\), the paper declares \(F\geq0\) exactly when

\[
[x_{ab}]\longmapsto [f_{ij}(x_{ab})]_{(i,a),(j,b)}
\]

is positive on every admitted \(K_n(B)\).

This is the standard matrix-dual cone: \(F\) is precisely a completely positive map from the matrix-ordered process space into \(M_k\). The operator-system axioms follow as claimed:

1. scalar conjugation follows from A1;
2. direct sums preserve positivity, while coordinate compressions prove the converse direction needed for the matrix direct-sum axiom;
3. quotienting complete operational null directions makes the cones proper;
4. involution comes from conjugation of effects; and
5. A2 supplies the Archimedean matrix order unit.

Thus Theorem 2.1 is correct. It constructs an abstract operator system and does not insert an associative multiplication.

A2 is intentionally strong: the order-unit property is an operational-scope assumption, not a consequence of merely having some testers. This is correctly disclosed.

# 2. UCP pullback and the complete lift

For an admitted deterministic completely positive process map \(F:B\to C\),

\[
F^\sharp(a)=a\circ F
\]

has the stated contravariance:

\[
(GF)^\sharp=F^\sharp G^\sharp.
\]

At every matrix level, positivity follows by applying the positive effect matrix to the completely positive image of an admitted process. Determinism gives unitality, and A4 makes the pullback an admitted effect and preserves the operational null quotient. Proposition 2.2 is therefore correctly typed.

For a scalar Karoubi representative \(\widetilde e\), complete idempotence is exactly

\[
\widetilde e^2-\widetilde e\in N_\infty(X,X).
\]

Hence Proposition 3.1 is an exact quotient criterion, not an approximation. When \(\widetilde e\) is an admitted deterministic superchannel, its pullback is already UCP; complete-kernel compatibility then makes it idempotent.

The distinction between these two requirements is important:

- \(N_1=N_\infty\) upgrades scalar equality \(e^2=e\) to complete operational equality;
- it does not independently turn a merely positive affine map into a completely positive superchannel.

The paper meets this requirement by working with an admitted deterministic-superchannel representative and by restricting the positive rung to ancilla-saturated comb scope. The result must retain that exact scope.

The range of the resulting UCP idempotent,

\[
\operatorname{ran}e^\sharp,
\]

with inherited cones and unit, is an operator system. No Choi–Effros multiplication is needed for this conclusion.

# 3. Transpose-symmetrizer control

For

\[
P=\frac12(\operatorname{id}+\tau)
\]

on \(M_2\), positivity, unitality, and idempotence are immediate from positivity and involutivity of transposition.

With the paper’s unnormalized Choi convention,

\[
J(P)=\frac12\left(|\Omega\rangle\langle\Omega|+\mathsf F\right).
\]

The antisymmetric unit vector is orthogonal to \(\Omega\), and the swap has eigenvalue \(-1\) on it. Therefore

\[
\langle\psi^-|J(P)|\psi^-\rangle=-\frac12.
\]

The control is exact. It demonstrates precisely that scalar positivity and scalar idempotence cannot replace complete positivity.

# 4. Split projections

Let \(P\) be positive, idempotent, with \(I-P\geq0\). If

\[
0\leq y\leq x,\qquad x\in\operatorname{ran}P,
\]

then

\[
0\leq(I-P)y\leq(I-P)x=0,
\]

so \(y\in\operatorname{ran}P\). The positive cone in the range generates the range because \(P\) is positive and the ambient cone is generating. Lemma 5.1 is sound.

Now let \(P,Q\) both be split projections. For positive \(x\in\operatorname{ran}P\),

\[
0\leq Qx\leq x.
\]

The order-ideal property forces \(Qx\in\operatorname{ran}P\). The same argument applies to \(\operatorname{ran}(I-P)\), so \(Q\) is block diagonal for the decomposition induced by \(P\). Therefore

\[
PQ=QP.
\]

I attempted to construct noncommuting positive complementary projections on finite ordered spaces and operator systems. The proof excludes them under the printed hypotheses. Restricted physical laws can fail to admit their sequential composition, but that is not a counterexample to commutation.

# 5. Boolean closure and atomicity

Given commuting split projections,

\[
P\wedge Q=PQ,\qquad
P^\perp=I-P,\qquad
P\vee Q=P+Q-PQ
\]

are algebraically idempotent. Their CP complements are physically constructed by the displayed sequential branches:

\[
I-PQ=(I-P)+P(I-Q),
\]

\[
P\vee Q=P+(I-P)Q,
\]

\[
I-(P\vee Q)=(I-P)(I-Q).
\]

Thus sequential flagged composition plus finite classical coarse-graining is sufficient for admission of the Boolean operations.

A commuting family of idempotents on a finite-dimensional complex vector space is simultaneously diagonalizable. Every common diagonal entry is \(0\) or \(1\), so only finitely many such maps exist. The admitted split projections consequently form a finite atomic Boolean algebra.

Its nonzero atoms sum to the identity and are admitted branches. Every branch of any other complete exclusive-repeatable instrument is a split projection and hence a unique sum of atoms. The atomic instrument is therefore the unique finest instrument up to outcome permutation.

I found no finite operator-system counterexample to this conclusion. If sequential composition or coarse-graining is withheld, incomparable maximal instruments can remain; the paper explicitly presents that situation as failure of its admission hypothesis.

# 6. Finite \(C^*\)-algebra controls

## 6.1 Full factors

If \(P\) and \(I-P\) are CP on \(M_d\), then

\[
0\leq J(P)\leq J(\operatorname{id}).
\]

Since \(J(\operatorname{id})=|\Omega_d\rangle\langle\Omega_d|\) has rank one,

\[
J(P)=\lambda J(\operatorname{id}),\qquad 0\leq\lambda\leq1.
\]

Thus \(P=\lambda\operatorname{id}\), and idempotence gives \(\lambda\in\{0,1\}\). The core of a full matrix factor is correctly trivial.

## 6.2 Direct sums

For

\[
A=\bigoplus_kM_{d_k},
\]

CP domination \(0\leq_{\mathrm{CP}}P\leq_{\mathrm{CP}}\operatorname{id}\) and the CP Radon–Nikodym theorem place the derivative of \(P\) in the commutant of the minimal Stinespring representation of the identity. The distinct central characters make that commutant the block scalars, even when two matrix sizes happen to coincide. Hence

\[
P(a)=\sum_k\lambda_k z_ka,\qquad 0\leq\lambda_k\leq1.
\]

Idempotence forces \(\lambda_k\in\{0,1\}\). Therefore the split projections are exactly sums of central block filters. When those physical filters are admitted, the operational core is the set of minimal central sectors.

The \(M_2\oplus\mathbb C\), \(\mathbb C^n\), and Koashi–Imoto controls follow at their stated standard-channel scope.

# 7. Hostile operator system

For

\[
S=\operatorname{span}_{\mathbb C}
\{(I,I),(Z,Z),(X,2X+Z)\},
\]

write \(s_2=(X,2X+Z)\). Then

\[
s_2^2=(I,5I),
\]

so

\[
(I,0)=\frac{5s_0-s_2^2}{4},
\qquad
(0,I)=\frac{s_2^2-s_0}{4}
\]

belong to \(C^*(S)\). Multiplying the generators by these central block units recovers \(X\) and \(Z\) in each summand. Therefore

\[
C^*(S)=M_2\oplus M_2.
\]

The only proper nonzero ideals delete one summand. Neither is a boundary ideal:

- deleting the second block changes \(\|s_2\|\) from \(\sqrt5\) to \(1\);
- deleting the first changes
  \[
  \|-3s_1+s_2\|
  \]
  from \(\sqrt{10}\) to \(\sqrt8\).

Hence

\[
C_e^*(S)=M_2\oplus M_2.
\]

A general element

\[
\alpha(I,I)+\beta(Z,Z)+\gamma(X,2X+Z)
\]

is central only when \(\beta=\gamma=0\). Thus

\[
S\cap Z(C_e^*(S))=\mathbb C(I,I).
\]

Now suppose \(P\) and \(I-P\) were a nontrivial CP split. The map

\[
s\mapsto(Ps,(I-P)s)
\]

is a unital complete-order isomorphism from \(S\) onto the operator-system direct sum of its two ranges; its inverse is addition. \(C^*\)-envelopes preserve this direct sum, so \(P(1)\) would be a nontrivial central projection in \(C_e^*(S)\) already lying in \(S\). No such element exists.

If \(P(1)=\lambda1\), idempotence gives \(\lambda^2=\lambda\). For \(\lambda=0\), positivity and the order-unit property imply \(P=0\); for \(\lambda=1\), the same argument gives \(I-P=0\). Thus no nontrivial split evades Theorem 8.2.

The hostile system therefore has the trivial operational core even though its envelope has center \(\mathbb C^2\). This control passes.

# 8. Findings by severity

## Fatal findings

None.

## Major-but-bounded findings

None.

## Minor finding

### M1 — literal marginal wording in Proposition 4.2

The probability formula is correct, but the sentence

> “Forgetting either flag leaves the state of every admitted effect in \(S\) unchanged”

is too broad if read as marginalizing only one flag in the two-run joint experiment while retaining the other. Summing over one index leaves the other subnormalized branch, not the unconditional state. What follows from

\[
\sum_rm_r=I_S
\]

is that discarding the complete outcome flag of one application makes that application nondisturbing; discarding both flags in the repeated experiment returns the original state. This wording issue does not affect Definition 4.1, the split theorem, or either registered rung.

## Scope clarifications

### S1 — ancilla saturation is a hypothesis

\[
N_1=N_\infty
\]

is sufficient to lift scalar idempotence, but it is not proved for arbitrary restricted tester grammars. The paper correctly labels it as a physical scope condition.

### S2 — complete positivity is independent of kernel equality

The complete-kernel equality does not turn a merely positive predecessor map into a CP map. The positive rung additionally requires an admitted deterministic-superchannel representative. That requirement is present in the paper and must remain in the terminal wording.

### S3 — admission closure is physical

Boolean maximality is over all physically admitted split instruments only when their sequential compositions and retained classical coarse-grainings are also admitted. Without that postulate, the theorem correctly downgrades to a family of possibly incomparable instruments.

### S4 — the core is not an algebraic center in general

The Boolean structure belongs to the retained outcome flag. No product among the effects \(q_r=m_r(1)\) is established on a generic operator system. The paper observes this distinction consistently.

# 9. Rung grading

| Registered rung | Grade | Reason |
|---|---|---|
| `RQ0-L0-MATRIX-ORDERED-MINIMAL-BOUNDARY` | **EARNED** | A1–A4 construct the operator-system dual; an admitted deterministic CP representative plus complete-kernel idempotence gives the UCP Karoubi lift. |
| `RQ0-L0-OPERATIONAL-CLASSICAL-CORE` | **EARNED** | Complementary CP projections commute; physical closure makes them a finite atomic Boolean algebra; its atoms give the unique finest admitted complete instrument. |
| `RQ0-L0-BLOCKED-AT-OPERATIONAL-CENTER` | **NOT SELECTED** | No matrix-lift, common-refinement, maximality, uniqueness, or required-control failure occurs at the declared positive scope. |

# 10. Exact first disposition

\[
\boxed{
\begin{array}{c}
\textbf{ACCEPT}\\[1mm]
\texttt{RQ0-L0-MATRIX-ORDERED-MINIMAL-BOUNDARY}\ \textbf{EARNED}\\
\texttt{RQ0-L0-OPERATIONAL-CLASSICAL-CORE}\ \textbf{EARNED}\\
\texttt{RQ0-L0-BLOCKED-AT-OPERATIONAL-CENTER}\ \textbf{NOT SELECTED}
\end{array}}
\]

The strongest secure interpretation is:

> For a finite one-chart minimal process boundary whose deterministic idempotent has an admitted completely positive representative, whose complete tester doctrine is ancilla-saturated, and whose physical instrument law is closed under sequential flagged composition and finite classical coarse-graining, the tester dual is a matrix-ordered operator system and all physically admitted nondisturbing repeatable classical questions possess one canonical finest joint instrument, possibly trivial.

Nothing in this review promotes that instrument to an actual outcome, task-independent W3 seam, autonomous subsystem, local region, overlap, topology, causal structure, field, or gravitational object.
