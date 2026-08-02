# Hostile Review B — quantum combs, superchannels, and process decision theory

**Status:** `COMPLETE / INDEPENDENT / REPOSITORY-READ-ONLY`

**Date:** 2026-08-01

**Strict pin:** `93444340f86e6db260c6836b21d4c8d493ee3219`  
**Verified SHA-256:** `d073e3b3f9a7cfffd8cfcf0e1feb27a7e5bd0e48ed1810d2eadc15ca6baff41d`

**Immutable paper:** `7e81dce3ef5267892face7b9579047fae78ccc54`  
**Verified SHA-256:** `5cca95256f2100d10dafa80f9facf34dc3c88fa3e9bb9f3b9ee102232030d053`

I also read the binding complete-comb/tester antecedent and its hostile adjudication through antecedent HEAD `9436b0713f33ad0fa2db4435058efc08261d00bd`. No repository artifact was edited.

## Disposition

The paper’s first two registered rungs survive, but only at their explicitly restricted scopes. The center rung does not survive, and the W3 rung is not reached.

| Registered rung | Verdict |
|---|---|
| `RQ0-L0-FUTURE-EXPERIMENT` | **EARNED AT NARROW COMMON-PROFILE FINITE SCOPE** |
| `RQ0-L0-MINIMAL-SUFFICIENT-BOUNDARY` | **EARNED AT ABSTRACT FINITE KAROUBI SCOPE** |
| `RQ0-L0-CANONICAL-CLASSICAL-CENTER` | **NOT EARNED** |
| `RQ0-L0-W3-MARKOV-BOUNDARY` | **NOT EARNED / NOT REACHED** |

The first registered obstruction is therefore

\[
\boxed{\texttt{RQ0-L0-BLOCKED-AT-CENTER-LIFT}.}
\]

There is no stronger earlier registered block. The minimum-rank theorem is sound under its printed hypotheses. The paper does, however, contain two false subsidiary statements and one important common-type under-specification. These do not move the first registered obstruction, but they must remain visible in adjudication.

## Findings, most severe first

### F1 — MAJOR-BUT-BOUNDED: retaining the branch weight changes the branch-memory eraser minimum from \(\mathbb C^4\) to \(\mathbb C^5\)

Section 9 says each written branch has weight \(1/4\), retained using the common success/sink embedding

\[
\widehat x_j
=
\frac14 |1\rangle\langle1|\otimes|\psi_j\rangle\langle\psi_j|
+
\frac34 |0\rangle\langle0|\otimes\omega_{\rm sink}.
\]

After \(E=U^*\) and computational readout, and after grouping all nonzero sink outcomes into their one common likelihood class, the actual classical experiment is

\[
q_j
=
\frac34\,\delta_f+\frac14\,\delta_j,
\qquad j=0,1,2,3,
\]

on the five outcomes \(f,0,1,2,3\). It is not the deterministic four-point experiment \(\delta_j\).

The equal success probability carries no information by itself, but it is not statistically redundant: on failure, the parameter label has been erased. Conditioning on success would recover \(\delta_j\), but that is exactly the normalization-and-weight deletion forbidden by the pin.

The five likelihood vectors are

\[
(3/4,3/4,3/4,3/4),
\qquad
(1/4,0,0,0),\ldots,(0,0,0,1/4),
\]

and no two are proportional. Hence the ordinary minimal sufficient statistic has five classes.

The same conclusion follows directly from stabilizers. Let \(T\) be a stochastic endomorphism fixing every \(q_j\), with columns \(T_f,T_j\). Then

\[
\frac34T_f+\frac14T_j
=
\frac34e_f+\frac14e_j,
\]

so

\[
T_j=e_j+3(e_f-T_f).
\]

For every success coordinate \(k\neq j\), nonnegativity gives
\(-3(T_f)_k\ge0\), hence \((T_f)_k=0\). Therefore \(T_f=e_f\) and \(T_j=e_j\) for all \(j\). The experiment is rigid on all five outcomes.

Consequently:

- the preserving written experiment is still trivial, because all four complete flagged outputs are identical;
- the no-write preserving experiment is of erasure form \(q_j\) and is strictly more informative than the written preserving experiment;
- the eraser minimum is \(\mathbb C^5\), not \(\mathbb C^4\);
- the preserving-plus-eraser tagged bundle is also \(\mathbb C^5\), after all parameter-independent outcomes are grouped;
- retaining the four orthogonal written states with the same success/sink flag likewise gives a five-class experiment, not \(\mathbb C^4\).

Thus Theorem 9.1(2) and (3), Section 9.4’s four-point statement, the branch-memory row of the control table, and the displayed sequence
\(\mathbb C\to\mathbb C^4\) are false under the paper’s own complete-weight convention.

The qualitative negative conclusion survives: neither \(\mathbb C^5\) nor the trivial preserving minimum selects any inherited coarse seam. This defect is fatal to the printed branch-memory classification but bounded downstream of the first two rungs.

### F2 — MAJOR-BUT-BOUNDED: the Choi swap proves that one state map does not lift, not Proposition 6.1 as worded

With the paper’s convention

\[
J(\Phi)\in B(H_A\otimes H_B),
\qquad
\operatorname{Tr}_B J(\Phi)=I_A,
\]

the swap calculation is correct. For a qubit replacer,

\[
J(\Phi_\rho)=I_A\otimes\rho_B,
\]

and conjugation by the factor swap gives

\[
WJ(\Phi_\rho)W=\rho_A\otimes I_B,
\qquad
\operatorname{Tr}_B(WJ(\Phi_\rho)W)=2\rho_A.
\]

This is channel-normalized only for \(\rho=I/2\). Therefore the unitary CPTP map \(J\mapsto WJW\) on normalized Choi states is not a deterministic superchannel on the full qubit-channel slice.

That proves the useful weaker statement:

> A particular CP equivalence witness between normalized Choi states need not itself be an admitted deterministic superchannel.

It does not prove Proposition 6.1 as written:

> Exact CP equivalence of a family of normalized Choi states does not imply exact process equivalence.

For the only explicit family mentioned, the identity-channel Choi state is fixed by swap; the identity superchannel is an alternative exact process simulator. Thus state equivalence and process equivalence both hold for that singleton family. If one instead includes a generic replacer, the swapped target is not a channel and hence not a second process experiment. To prove the existential non-implication, the paper needed two valid channel families related by state CP maps and a proof that no admitted superchannel relates them. It provides neither.

This invalidates Proposition 6.1 at its printed strength and the claim of two full experiment-level center-lift counterexamples. It does not earn the center rung: the weaker nonautomatic-lift statement is proved, and, independently, the Karoubi object lacks a supplied multiplication or central instrument.

### F3 — MAJOR-BUT-BOUNDED SCOPE GAP: Proposition 2.1 needs more explicit common typing than is printed

The complete-instrument flagging itself is valid:

\[
\widehat{\mathcal P}_{\theta}(\rho)
=
\sum_a |a\rangle\langle a|\otimes\mathcal P_{\theta,a}(\rho)
\]

is CPTP because the branch sum is trace preserving. It retains probabilities, outcomes, conditional outputs, and disturbances.

Three restrictions are nevertheless necessary.

First, the paper writes the flag space as \(A_\theta\). If different settings have different outcome profiles, their flagged channels do not automatically have one common cut type. One must either restrict \(\Theta_c\) to settings with a common physical outcome register or provide a single \(\theta\)-independent padded register. A direct sum with disjoint \(\theta\)-labelled sectors would give the future a forbidden copy of \(\theta\).

Second, the scalar sink formula is valid when

\[
x_\theta=p_\theta\bar x_\theta
\]

with \(\bar x_\theta\) itself a deterministic process. This covers the paper’s subnormalized source states. It does not cover an arbitrary probabilistic comb whose success probability depends on an input. Such a branch must be completed by its actual complementary CP branch, not by a scalar fixed sink.

Third, a literal unweighted direct sum of deterministic future tasks is not deterministic: its total normalization is multiplied by the number of summands. Heterogeneous tasks can be bundled validly in either of two ways:

- a classical task-choice input controls which \(L_t\) is applied; or
- fixed probabilities \(q_t>0\), independent of \(\theta\), produce
  \(\bigoplus_t q_t L_t(s_\theta)\) with an output task flag.

The paper says “deterministic controlled superchannel” but prints neither the control wire nor fixed randomization weights. Its claim is therefore not a construction for arbitrary heterogeneous families.

These restrictions do not force the first registered block earlier. The displayed qubit and branch-memory controls use compatible finite profiles, common binary success flags, and state branches for which the sink formula is valid. Proposition 2.1 is accepted only at that narrow common-profile scope, not at an unrestricted heterogeneous-instrument scope.

### F4 — MINOR: the W3 deficiency shorthand reverses the paper’s declared deficiency direction

Section 3 defines

\[
\delta_D(\mathsf E\Vert\mathsf G)
=
\min_{\Gamma:X_E\to X_G}
\max_\theta\|\Gamma x_\theta-y_\theta\|.
\]

If a classical center is sufficient for a future experiment, the recovery runs from the center to the future process. The relevant quantity is therefore

\[
\delta_D(R_c\Vert\mathsf E_c),
\]

not \(\delta_D(\mathsf E_c\Vert R_c)\). The verbal argument in Section 8 uses the correct direction—“from the preserving center to the enlarged experiment”—but Proposition 8.1 suppresses the arguments, and the governing pin’s shorthand writes them in the reverse order.

The zero-versus-positive control remains meaningful when read in the recovery direction. The displayed shorthand should not be used as evidence of center sufficiency.

## Independent reconstruction of the process theorem

### Operational quotient and contraction

For each type, quotienting the real comb span by the tester-seminorm kernel produces a finite-dimensional normed space. A superchannel descends exactly when it maps the upstream kernel into the downstream kernel.

This is not automatic for an arbitrary law-relative tester subset. It follows from the inherited tester-pullback condition

\[
T\in\mathsf{Test}_D(Y)
\Longrightarrow
\Gamma^*T\in\mathsf{Test}_D(X),
\]

which gives

\[
\|\Gamma z\|_{\mathsf{Test}_D,Y}
\le
\|z\|_{\mathsf{Test}_D,X}.
\]

Section 3.1 includes contraction as an explicit hypothesis, so every morphism used in Theorem 4.2 preserves the quotient. For unrestricted comb testers, deterministic superchannels satisfy this by ordinary tester pullback. For a restricted laboratory category, closedness and convexity alone are insufficient; pullback closure or direct kernel preservation is additionally required.

### Compactness, convexity, and attainment

For fixed finite ordinary comb profiles, deterministic superchannels form a closed, bounded affine slice of a finite-dimensional positive Choi cone. Their hom-sets are compact and convex, classical randomization is again deterministic, and composition is continuous and bilinear on linear representatives. Passing to induced quotient maps preserves compactness.

Accordingly,

\[
\Gamma\longmapsto
\max_\theta\|\Gamma x_\theta-y_\theta\|
\]

is continuous on a compact hom-set. The deficiency minimum is attained, and zero deficiency is equivalent to an exact parameter-independent simulator.

### Proposition 3.1

For

\[
z_\theta=y_\theta-\Gamma x_\theta,
\]

the product-space norm is

\[
\max_\theta\|z_\theta\|
=
\max_{\sum_\theta\|g_\theta\|_*\le1}
\sum_\theta g_\theta(z_\theta).
\]

This is precisely the duality between a finite \(\ell^\infty\)-sum and its
\(\ell^1\)-sum dual. Both the hom-set and dual ball are compact and convex, and the pairing is continuous and affine in each argument. Finite-dimensional minimax therefore gives

\[
\delta_D(\mathsf E\Vert\mathsf G)
=
\max_{(g_\theta)\in\mathcal B_1}
\left[
\sum_\theta g_\theta(y_\theta)
-
\max_\Gamma\sum_\theta g_\theta(\Gamma x_\theta)
\right].
\]

The sign and inner maximum are correct. The interpretation of arbitrary \(g_\theta\) as a physical decision problem requires the balanced-convex tester generation caveat printed after the proposition; the norm identity itself does not require it.

### Minimum-rank idempotent and mean ergodic projection

Let \(e\) be a minimum-rank idempotent in the stabilizer. Such an idempotent exists because the identity is one, and linear ranks range over finitely many integers.

For a stabilizing endomorphism \(f:(X,e)\to(X,e)\),

\[
f=efe.
\]

All powers \(f^n\) are admitted and lie in a compact hom-set, hence are uniformly bounded. In finite dimension, power boundedness implies:

- every eigenvalue has modulus at most one;
- eigenvalues on the unit circle have no nontrivial Jordan blocks.

Therefore

\[
A_N=\frac1N\sum_{n=1}^Nf^n
\]

converges to the spectral projection \(p\) onto the fixed space of \(f\) in \(\operatorname{ran}e\), extended by zero on \(\ker e\). Convexity admits every \(A_N\), and closedness admits \(p\). Moreover,

\[
p^2=p,\qquad p=epe,\qquad px_\theta=x_\theta.
\]

If \(f\neq e\), its restriction to \(\operatorname{ran}e\) cannot be the identity; otherwise \(f=efe=e\). Its fixed space is then proper, so

\[
\operatorname{rank}p<\operatorname{rank}e,
\]

contradicting minimality. Lemma 4.1 is correct.

No admitted finite superchannel category satisfying all the stated hypotheses can defeat this argument. Counterexamples require dropping at least one load-bearing condition: closedness, convexity, composition stability, finite dimensionality/power boundedness, or quotient congruence.

### Retract minimality, uniqueness, and presentation covariance

Given a sufficient coarse-graining \(\Gamma:X\to Y\) and recovery \(R:Y\to X\), set

\[
a=\Gamma e,\qquad b=eR.
\]

Then \(ba=eR\Gamma e\) is a stabilizing endomorphism of \((X,e)\), hence \(ba=e\). Thus \((X,e)\) is a retract of every sufficient representative.

If two rigid representatives simulate one another through \(u,v\), then \(vu\) and \(uv\) stabilize their respective experiments. Rigidity makes both identities, so \(u,v\) are inverse admitted arrows. Uniqueness is therefore correctly proved.

A reversible presentation map conjugates the stabilizer semigroup and preserves linear rank, so the minimal isomorphism class is presentation covariant. A Choi-convention change is more properly a coordinate/category isomorphism than a physical superchannel, but the rank and categorical argument remain invariant.

The result belongs to

\[
\operatorname{Kar}(\mathsf{Proc}_D),
\]

not generally to the ordinary comb category. The paper does not prove that an idempotent superchannel’s range is an ordinary wire profile. The registered pin explicitly allows a formal idempotent split, provided it is interpreted only as a repeatable coarse-graining. The paper observes that ceiling.

## Center-lift audit

The operator-system calculation is correct. For

\[
S=\operatorname{span}\{(I,I),(Z,Z),(X,2X+Z)\}
\subset M_2\oplus M_2,
\]

one has

\[
(X,2X+Z)^2=(I,5I),
\]

so the generated algebra contains both block identities and hence all of
\(M_2\oplus M_2\). Neither block identity belongs to \(S\). The two scalar norm witnesses exclude each nonzero proper block ideal as a boundary ideal, so

\[
C_e^*(S)=M_2\oplus M_2.
\]

Thus the center of an envelope need not be an effect in the original operator system.

This example is not itself realized as the range of a displayed comb superchannel, so it is not a process-retract counterexample. It nevertheless correctly disproves the claim that passing to a generated envelope automatically supplies an already admitted central effect.

More fundamentally, the abstract Karoubi data \((X,e)\) contain no declared bilinear multiplication. A Choi–Effros product would require additional concrete operator-system and completely positive projection hypotheses that are not part of the tester quotient or abstract process category; even then, an admitted nondemolition central instrument would still have to be constructed. No omitted ordinary-comb theorem automatically supplies presentation-invariant physical readout from the stated data.

No CP state map is otherwise silently promoted to a superchannel. The Koashi–Imoto and dephasing examples are explicitly state-level or order-zero state-process controls. The paper correctly refuses to infer a general process center from them.

The center rung is therefore not earned independently of the overstatement in Proposition 6.1.

## Task-smuggling theorem

Theorem 7.1 is correct as a no-selection result. Starting from a chosen PVM \(P\), one may choose finitely many faithful block-diagonal states affinely spanning the trace-one self-adjoint hyperplane of

\[
A_P=\bigoplus_rP_rB(H)P_r.
\]

A CP endomorphism fixing that family fixes its affine hull and therefore the linear span \(A_P\). The output experiment is minimal on \(A_P\), whose center is generated by the chosen block identities.

The theorem deliberately assumes the desired PVM in order to show that a matched dephasing task can plant its center. It does not silently derive the center it assumes. Its conclusion is exactly that such a construction cannot count as independent record selection.

This is a real downstream `TASK-SELECTION` obstruction, but center lift fails first in the registered ladder.

## Exact qubit W3 control

The qubit arithmetic is correct:

\[
p_0=(3/4,1/4),\qquad p_1=(1/4,3/4),
\]

while the no-write reset gives \((1/2,1/2)\) for both parameters. The preserving classical experiment is nontrivial and minimal.

For a classical-to-quantum recovery with output states \(\sigma_0,\sigma_1\), exact recovery would require

\[
\frac34\sigma_0+\frac14\sigma_1=\rho_0,
\qquad
\frac14\sigma_0+\frac34\sigma_1=\rho_1.
\]

Because both coefficients are strictly positive and each \(\rho_i\) is pure, the first equality forces every contributing state to equal \(\rho_0\), while the second forces them to equal the distinct \(\rho_1\). This is impossible. Compactness of the channel set therefore gives strictly positive deficiency in the center-to-full direction.

The coherence calculation is also correct:

\[
\left\|\rho_i-\mathcal D_Z(\rho_i)\right\|_1
=
\frac{\sqrt3}{2}.
\]

That number is a dephasing contrast, not the optimized deficiency value. The paper only needs exact zero versus strict positivity, which is established.

This is a valid order-zero positive control. It does not establish a generic process-center lift.

## Branch-memory arithmetic and interpretation

The transition matrix is correct. Every overlap has magnitude \(1/2\), so the written preserving terminal distribution is uniform. The no-write states are the \(v_i\) and give distinct terminal delta distributions on success. The eraser satisfies \(E\psi_j=|j\rangle\).

The interpretation must nevertheless retain the sink contribution, as in Finding F1. The corrected task sequence for the original \(1/4\)-weighted branch parameters is

\[
\mathbb C
\longrightarrow
\mathbb C^5,
\]

not

\[
\mathbb C
\longrightarrow
\mathbb C^4.
\]

This correction still leaves every inherited \(2+1+1\), \(2+2\), and complex rank-two coarse seam unselected. Candidate-matched dephasing tasks can manufacture corresponding block structures only by using the candidate in the task definition. The paper also does not provide the pin’s requested individual four-axis census of all ten inherited/hostile candidates by superchannel equivalence, minimality, center, and deficiency; it only establishes their collective nonselection under the frozen tasks.

## One-chart firewall

The paper consistently treats comb order as laboratory composition typing. It does not infer spacetime causal order, localization, topology, overlap, fields, or gravity. Its Karoubi object is explicitly not called an autonomous subsystem or spatial boundary. The task-indexed family is not promoted to a sheaf. This firewall passes.

## Final rung audit

### `RQ0-L0-FUTURE-EXPERIMENT`

**Earned at narrow finite common-profile scope.** Complete flagged instruments and the explicit state-branch sink embeddings retain weights, outcomes, disturbances, and common outputs without a free copy of \(\theta\). The general heterogeneous-family wording requires the restrictions in Finding F3.

### `RQ0-L0-MINIMAL-SUFFICIENT-BOUNDARY`

**Earned at finite compact-convex Karoubi scope.** Exact simulation uses one parameter-independent admitted superchannel. Deficiency is attained, Proposition 3.1 is correct, the minimum-rank mean-ergodic argument is sound, every sufficient representative retracts onto the minimum, and rigid minima are uniquely isomorphic. No ordinary-comb splitting or autonomous boundary is proved.

### `RQ0-L0-CANONICAL-CLASSICAL-CENTER`

**Not earned.** The process retract has no supplied multiplication or central instrument. The operator-system example correctly blocks automatic readout from an envelope. The Choi swap supports only the weaker nonautomatic-lift claim, but no positive center-lift construction exists even after that overclaim is removed.

### `RQ0-L0-W3-MARKOV-BOUNDARY`

**Not earned and not reached.** The qubit order-zero control is valid, but no generic physical center exists. The branch-memory model has a trivial preserving minimum and a five-class erasure minimum once weights are honestly retained; it does not select any proposed coarse record.

## Final disposition

The paper establishes a genuine abstract process result:

\[
\boxed{
\text{finite compact-convex process experiments admit rigid minimal
sufficient retracts in the Karoubi completion.}
}
\]

It does not establish that such a retract is an ordinary comb boundary, an autonomous subsystem, an observable algebra, or a readable classical record.

The correct first registered stopping point remains

\[
\boxed{\texttt{RQ0-L0-BLOCKED-AT-CENTER-LIFT}.}
\]

`RQ0-L0-BLOCKED-AT-TASK-SELECTION` remains a genuine later obstruction. The false \(\mathbb C^4\) branch-memory classification and the overstrong Choi-swap proposition are major but bounded defects; neither moves the registered block earlier than center lift.
