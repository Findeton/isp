# Independent hostile Review A — quantum statistics, sufficiency, and randomization

**Status:** `COMPLETE / INDEPENDENT / REPOSITORY-READ-ONLY`

**Date:** 2026-08-01

**Role:** independent reviewer in classical and quantum statistical experiments, Le Cam/Blackwell comparison, CP sufficiency, minimax randomization, and finite quantum statistics

**Artifacts reviewed:**

- strict pin commit `93444340f86e6db260c6836b21d4c8d493ee3219`;
- immutable paper commit `7e81dce3ef5267892face7b9579047fae78ccc54`;
- binding antecedent HEAD `9436b0713f33ad0fa2db4435058efc08261d00bd`, including the operational-comb hostile adjudication and the branch-memory counterexample.

The printed hashes were independently reproduced:

- pin SHA-256: `d073e3b3f9a7cfffd8cfcf0e1feb27a7e5bd0e48ed1810d2eadc15ca6baff41d`;
- paper SHA-256: `5cca95256f2100d10dafa80f9facf34dc3c88fa3e9bb9f3b9ee102232030d053`.

No repository file was edited.

## Executive verdict

The paper’s abstract compact-convex minimal-retract theorem is sound. I found no finite counterexample to Theorem 4.2 under its printed hypotheses. Proposition 3.1 is also correct as a finite-dimensional convex duality statement.

The paper nevertheless contains two material errors:

1. the branch-memory analysis discards the explicitly retained success/sink flag when identifying its minimal experiments; and
2. the Choi-factor swap does not prove Proposition 6.1 in its stated family-level existential form.

There is also an incompletely printed typing hypothesis for bundling several future tasks and a failure to perform the full registered branch-memory census by superchannel equivalence, center, minimality, and deficiency.

These defects are major but bounded. They do not refute the first two abstract rungs. They do refute several advertised controls and supporting propositions. The paper remains correct that a canonical physical center has not been obtained.

The rung decision is:

| Registered rung | Review A decision |
|---|---|
| `RQ0-L0-FUTURE-EXPERIMENT` | **EARNED AT THE DECLARED COMPATIBLE, ADMITTED-BUNDLE SCOPE**, subject to the explicit common-flag and bundle-admission qualifications below |
| `RQ0-L0-MINIMAL-SUFFICIENT-BOUNDARY` | **EARNED AT COMPACT-CONVEX KAROUBI SCOPE** |
| `RQ0-L0-CANONICAL-CLASSICAL-CENTER` | **NOT EARNED** |
| `RQ0-L0-W3-MARKOV-BOUNDARY` | **NOT EARNED / NOT REACHED CUMULATIVELY** |

The first registered obstruction remains

\[
\boxed{\texttt{RQ0-L0-BLOCKED-AT-CENTER-LIFT}.}
\]

There is no fatal error forcing an earlier registered block.

## 1. Typed future experiments

The main construction is statistically legitimate when read with its declared compatibility assumptions.

A complete past instrument is represented by

\[
\widehat{\mathcal P}_\theta(\rho)
=
\sum_a |a\rangle\langle a|\otimes\mathcal P_{\theta,a}(\rho),
\]

so CP branches, subnormalized weights, physical outcomes, and disturbances remain in one deterministic flagged process. For an individual branch \(x_\theta=p_\theta\bar x_\theta\), the common embedding

\[
\widehat x_\theta
=
p_\theta|1\rangle\langle1|\otimes\bar x_\theta
+
(1-p_\theta)|0\rangle\langle0|\otimes\omega_{\rm sink}
\]

correctly retains the weight without supplying a copy of \(\theta\). A common binary success flag with a common sink is physical conditioning, not parameter leakage.

Two qualifications must be made explicit.

First, the notation \(A_\theta\) is dangerous. To obtain one experiment type, all past flags must be embedded in a common, \(\theta\)-independent output profile. Disjoint flag alphabets tagged by the setting would reveal \(\theta\) by construction. The claimed common \(K_{\tau_c}\) is valid only when the chart supplies a common outcome handle and no setting register is passed to the future.

Second, individual admission of future tasks does not alone imply admission of their tagged bundle in a restricted laboratory category. A deterministic bundle requires either:

- a classical selector input, retained as part of the output-process type; or
- a fixed strictly positive distribution \(q_t\) and the normalized flagged channel
  \[
  L_{\mathfrak F}(x)=\bigoplus_t q_tL_t(x).
  \]

An unweighted direct sum of deterministic channels is not trace preserving. The unrestricted finite-comb category admits the controlled construction, but a restricted \(\mathsf{Proc}_D\) must explicitly be closed under the chosen selector or flagged randomization. This is a scope qualification, not a counterexample once bundle admission is included among the hypotheses.

With those conditions, the task flag reveals which future task is being queried, not the past parameter. The paper otherwise obeys the no-selected-record rule.

## 2. Exact simulation, deficiency, and Proposition 3.1

Exact simulation uses one admitted map \(\Gamma\), independent of \(\theta\). Reflexivity, transitivity, downstream monotonicity, and reversible-presentation covariance follow exactly as stated.

The compactness argument also correctly proves

\[
\delta_D(\mathsf E\Vert\mathsf G)=0
\quad\Longleftrightarrow\quad
\mathsf E\succeq_D\mathsf G
\]

at the declared scope. Without compactness only the forward implication would be automatic; the paper does not make that overclaim.

Proposition 3.1 is correct. For

\[
z=(y_\theta-\Gamma x_\theta)_\theta
\]

in the \(\ell^\infty\)-sum of copies of \(V_Y\),

\[
\|z\|_{\ell^\infty}
=
\max_{\sum_\theta\|g_\theta\|_*\le 1}
\sum_\theta g_\theta(z_\theta),
\]

because the dual of a finite \(\ell^\infty\)-sum is the corresponding \(\ell^1\)-sum. The objective is continuous and affine in both \(\Gamma\) and \(g\); compact convex minimax therefore gives exactly

\[
\delta_D(\mathsf E\Vert\mathsf G)
=
\max_{g\in\mathcal B_1}
\left[
\sum_\theta g_\theta(y_\theta)
-
\max_\Gamma\sum_\theta g_\theta(\Gamma x_\theta)
\right].
\]

No sign or \(\ell^1/\ell^\infty\) reversal is present.

The resulting witness is automatically a separating dual functional. Its interpretation as an admitted operational decision problem additionally requires the dual ball to be generated by the balanced convex hull of admitted tester-outcome evaluations. The paper states this qualification after the proposition. This is consistent with finite process randomization theory, rather than a substitute for its stronger complete-test versions; see [Jenčová’s process-comparison treatment](https://arxiv.org/abs/2002.04240).

## 3. The minimum-rank theorem

No finite counterexample to Lemma 4.1 or Theorem 4.2 exists under the printed hypotheses.

Let \(e\) be a minimum-rank stabilizing idempotent and let \(f=efe\) be a Karoubi endomorphism fixing every \(x_\theta\). Every \(f^n\) remains in the compact endomorphism hom-set. Hence the powers are bounded in finite dimension and the Cesàro averages converge to the projection \(p\) onto \(\operatorname{Fix}(f)\). Closedness and convexity make \(p\) admitted.

Because \(f=efe\), every fixed vector lies in \(\operatorname{ran}e\). If \(f\neq e\), its restriction to \(\operatorname{ran}e\) is not the identity; otherwise \(f=efe=e\). Consequently,

\[
\operatorname{Fix}(f)\subsetneq\operatorname{ran}e,
\qquad
\operatorname{rank}p<\operatorname{rank}e.
\]

The limit \(p\) is a lower-rank stabilizing idempotent, contradicting minimality. Rigidity follows.

For a sufficient \(\Gamma:X\to Y\) with recovery \(R\), the maps

\[
a=\Gamma e,\qquad b=eR
\]

are correctly typed Karoubi morphisms and \(ba=eR\Gamma e\) fixes the experiment. Rigidity gives \(ba=e\), so \((X,e)\) is a retract of every sufficient representative. Applying rigidity to maps between two such representatives proves that their comparison maps are mutual inverses.

No ordinary-comb splitting is proved. The result belongs to

\[
\operatorname{Kar}(\mathsf{Proc}_D),
\]

unless an additional physical splitting theorem is supplied. The paper says this plainly.

Minimum rank is invariant under the reversible presentations actually defined. If \(U\) is an admitted object isomorphism, then

\[
e\longmapsto UeU^{-1},
\qquad
\operatorname{rank}(UeU^{-1})=\operatorname{rank}e.
\]

A noninvertible addition of a spectator is not a presentation isomorphism. For merely sufficient, mutually simulable ambient representations, Theorem 4.2 compares their minimal Karoubi cores rather than asserting equality of the ambient ranks.

The result is thus stronger physically than normalized-Choi state sufficiency: its coarse-grainings and recoveries are admitted process superchannels. It remains weaker than an ordinary wire boundary, autonomous subsystem, observable algebra, or spatial interface.

## 4. Relation to known minimal sufficiency and Proposition 5.1

The distinction from the established state theorem is correct. Minimal sufficient state experiments are unique up to normal algebra isomorphism under CP/Schwarz comparison, after the usual faithful-support reduction; see [Kuramochi](https://arxiv.org/abs/1701.03394) and [Jenčová–Petz](https://arxiv.org/abs/math-ph/0412093). That theorem supplies more algebraic structure but applies to state experiments, not automatically to combs.

Proposition 5.1 is correct, although its proof suppresses one step. If restriction to \(Z(M_{\min})\) is sufficient, the original experiment is CP-equivalent to an abelian experiment. Taking the minimal sufficient representative of that abelian experiment still gives an abelian algebra. Uniqueness then makes \(M_{\min}\) isomorphic to an abelian algebra, hence abelian. The converse is immediate.

The finite controls check out:

- the classical likelihood vectors identify exactly the two blocks \(\{a,b\}\) and \(\{c,d\}\);
- the displayed Koashi–Imoto family has minimal algebra \(M_2\oplus\mathbb C\), center \(\mathbb C^2\), and a redundant \(N\)-factor;
- two distinct nonorthogonal pure qubit states force the irreducible algebra \(M_2\);
- the within-sector states have identical center statistics and
  \[
  \|\rho_0-\rho_1\|_1=\sqrt2,
  \]
  so any common reconstruction has worst-case error at least \(\sqrt2/2\).

These examples correctly separate a nontrivial center from center-only sufficiency.

## 5. Major finding: Proposition 6.1 is not proved as stated

**Classification:** major-but-bounded.

The Choi calculation itself is correct. Under

\[
\operatorname{Tr}_B J(\Phi)=I_A,
\]

the factor swap sends a replacer Choi operator \(I_A\otimes\rho_B\) to \(\rho_A\otimes I_B\), whose output trace is \(2\rho_A\), not generally \(I_A\). Thus the swap CPTP map on normalized Choi states is not a deterministic superchannel on all qubit channels.

What this proves is:

> a particular CPTP map between normalized Choi matrices need not lift to a deterministic superchannel.

It does not prove the literal Proposition 6.1:

> existence of CP equivalence between two valid Choi-state families does not imply existence of process equivalence between those channel families.

To prove that existential statement, the paper would need two valid channel families, reversible state-level CP maps between them, and a proof that no parameter-independent deterministic superchannel realizes the family comparison. The supplied singleton identity-channel observation cannot do this: although the factor swap fixes that Choi state, the identity superchannel also fixes the identity channel, so that family is process-equivalent.

The pin’s narrower “nonliftable shadow” control survives: an arbitrary state-level witness cannot itself certify process sufficiency without checking superchannel normalization. The stronger family-level proposition must be withheld.

The operator-system example supplies an independent and correct readout obstruction. The norm witnesses exclude both proper block ideals as boundary ideals, so

\[
C_e^*(S)=M_2\oplus M_2,
\]

while neither central block projector belongs to \(S\). Multiplication in the envelope creates those projectors; the original operational linear interface does not contain them. This correctly blocks any general guarantee that an algebraic envelope center is already an admitted readout.

## 6. The task-smuggling theorem

Theorem 7.1 is correct.

For a finite PVM \(P\), choose faithful block-diagonal density matrices obtained by sufficiently small self-adjoint perturbations of a full-rank reference state so that their affine hull is the trace-one self-adjoint hyperplane of

\[
A_P=\bigoplus_rP_rB(H)P_r.
\]

A linear CP endomorphism fixing this family fixes the traceless directions and one reference state, hence all of \(A_P\). The experiment is rigid on \(A_P\), so its minimal algebra is \(A_P\), with center generated by the \(P_r\).

The wording “affine span is the self-adjoint state space” should be read as “affine hull of the state space”; this is minor.

The theorem does not silently assume a center in a purported derivation. It deliberately begins with the desired PVM to prove that a matching dephasing task can plant that center. It is a valid circularity detector.

## 7. Exact qubit W3 control

The one-step qubit control is correctly calculated.

The \(Z\)-readout distributions are

\[
p_0=(3/4,1/4),\qquad p_1=(1/4,3/4),
\]

which form a minimal two-point classical experiment. Resetting both branches to \(|+\rangle\) gives identical \((1/2,1/2)\) statistics and therefore fails the write discriminator.

No classical-bit decoder can reconstruct both original pure states: the equation

\[
\frac34\sigma_0+\frac14\sigma_1=\rho_0
\]

with pure \(\rho_0\) forces both positive-weight components to equal \(\rho_0\), contradicting reconstruction of the distinct \(\rho_1\). Compactness of the decoder set then makes the deficiency strictly positive. The printed coherence norm

\[
\left\|\rho_i-\mathcal D_Z(\rho_i)\right\|_1
=
\frac{\sqrt3}{2}
\]

is exact.

The deficiency notation in Proposition 8.1 should specify direction. The proof establishes zero recovery defect for the preserving classical experiment and positive deficiency in the direction “classical center simulates retained quantum experiment.” This is a minor notational issue.

The task supplies the \(Z\)-classical output by design, so this is properly described only as nonemptiness of the criterion, not derivation of a generic center. The paper observes that limit.

## 8. Major finding: the branch-memory weight is dropped

**Classification:** major-but-bounded.

Section 9 explicitly retains each source branch with weight \(p=1/4\) through the common success/sink embedding. Its later minimal-experiment identifications then silently analyze only the normalized success branch.

For the preserving task, the full output law is

\[
q_j^{\rm pres}
=
\frac34\delta_{\rm sink}
+
\frac14\left(\frac14,\frac14,\frac14,\frac14\right),
\]

which is independent of \(j\). The conclusion that the preserving minimum is trivial remains correct.

For the eraser task, however, the full deterministic output is

\[
q_j^{\rm erase}
=
\frac34\delta_{\rm sink}
+
\frac14\delta_j,
\]

not the deterministic law \(\delta_j\). The sink does not carry information about \(j\), but it cannot be discarded under Blackwell equivalence: on a sink occurrence no parameter-independent recovery can recreate \(j\).

The likelihood vectors of the five outcomes are

\[
\ell_{\rm sink}=(3/4,3/4,3/4,3/4),
\]

and

\[
\ell_k=(0,\ldots,1/4,\ldots,0),\qquad k=0,1,2,3.
\]

No two are proportional. Therefore the ordinary minimal sufficient statistic is the identity on five outcome classes, and the minimal classical algebra is

\[
\mathbb C^5,
\]

not \(\mathbb C^4\).

The same defect affects the retained-output and tomography claims. With the original weighted branch parameters, the four retained written states are flagged erasure states, not four pure states. Their classical minimum is again \(\mathbb C^5\). A tomographically spanning success family with the same retained sink yields, at state-experiment scope,

\[
M_4\oplus\mathbb C,
\]

with a nontrivial success/sink center, rather than \(M_4\) with scalar center.

Likewise, matching dephasing tasks give

\[
(M_2\oplus\mathbb C\oplus\mathbb C)\oplus\mathbb C_{\rm sink}
\]

for a \(2+1+1\) PVM and

\[
(M_2\oplus M_2)\oplus\mathbb C_{\rm sink}
\]

for a \(2+2\) PVM, unless the parameter class is explicitly replaced by weight-one deterministic preparations. Merely “enlarging” the original branch family does not perform that replacement.

Several qualitative conclusions survive:

- the preserving minimum is trivial;
- no-write remains strictly more informative than write under that terminal preserving task;
- the eraser task does not select an inherited coarse seam;
- candidate-matched dephasings remain circular;
- no canonical familiar memory PVM is selected.

But the advertised sequence

\[
\mathbb C\longrightarrow\mathbb C^4\ \text{or}\ M_4
\]

and Theorem 9.1’s “perfect fine label” statement are false for the experiment actually defined.

The pin also required the nine inherited seams and the complex rank-two seam to be classified by superchannel equivalence, minimality, center, and deficiency. Section 9 does not perform that census. It merely states that none is selected by the frozen terminal tasks and gives abstract algebras for candidate-matched dephasing after a separating extension. This is an unmet mandatory control, though it does not refute Theorem 4.2.

## 9. Center lift and physical scope

The process minimum is a Karoubi pair \((X,e)\). Such a pair contains composition data and an idempotent coarse-graining, but no intrinsic multiplication of effects. Neither a center nor a central instrument follows from that datum.

The Choi example establishes only the narrower map-level warning, but the failure to earn the center rung does not depend on the overstated Proposition 6.1. The paper constructs no presentation-invariant multiplication, no process-level center functor, and no admitted central readout. The operator-system example independently shows why passing to a generated \(C^*\)-algebra does not supply an already admitted effect.

The minimum additional physical structure would be:

1. a presentation-covariant operator-system or algebra object attached to each relevant Karoubi retract;
2. admitted superchannels realizing its compression and recovery;
3. an admitted nondemolition instrument reading its central projections; and
4. covariance of that instrument under every admitted reversible presentation.

Without these data, the third rung cannot be earned.

## 10. Severity register

### Fatal

None.

### Major-but-bounded

1. The success/sink flag is discarded in the branch-memory minimal-sufficiency analysis, changing \(\mathbb C^4\) to \(\mathbb C^5\) and \(M_4\) to \(M_4\oplus\mathbb C\) at the stated parameterization.
2. Proposition 6.1’s family-level nonimplication is not proved by the Choi swap.
3. The mandatory branch-memory classification by equivalence, minimality, center, and deficiency is incomplete.

### Minor

1. Proposition 5.1 omits the step of minimizing the abelian center experiment before invoking uniqueness.
2. Theorem 7.1 uses imprecise “affine span of the self-adjoint state space” language.
3. Proposition 8.1 leaves the direction of deficiency implicit.

### Scope clarifications

1. Future task bundling requires a common \(\theta\)-independent flag profile and an admitted controlled or normalized flagged superchannel.
2. Theorem 4.2 is a Karoubi-process theorem, not an ordinary-comb splitting theorem.
3. Proposition 3.1 gives an operational decision witness only relative to the balanced tester-generated dual ball.
4. Minimum rank is invariant under admitted reversible object presentations, not arbitrary noninvertible embeddings.

## 11. Final registered disposition

`RQ0-L0-FUTURE-EXPERIMENT` is earned narrowly because the primary construction retains complete instruments, weights, flags, disturbances, and common process types once controlled-bundle admission and a common non-parameter flag profile are included in the declared compatibility conditions.

`RQ0-L0-MINIMAL-SUFFICIENT-BOUNDARY` is earned at finite-dimensional, compact-convex, tester-quotiented Karoubi scope. The minimum-rank proof, retract property, rigidity, presentation covariance, and uniqueness all survive hostile reconstruction.

`RQ0-L0-CANONICAL-CLASSICAL-CENTER` is not earned. A process retract has not been made into a canonical physical observable algebra, and no admitted central instrument has been constructed.

`RQ0-L0-W3-MARKOV-BOUNDARY` is not earned. Its one-step state-process control is valid, but the cumulative center prerequisite fails, and the branch-memory control is quantitatively misclassified.

Accordingly, the first registered blocked outcome is

\[
\boxed{\texttt{RQ0-L0-BLOCKED-AT-CENTER-LIFT}.}
\]

`RQ0-L0-BLOCKED-AT-TASK-SELECTION` remains a valid downstream warning, not the first obstruction. No locality, topology, causality, field, gravity, autonomous-boundary, or actual-outcome conclusion follows.
