# Relativistic ISP V3 Paper 28: RN-MIXAMP Spectral Contraction Plus Tail Campaign

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Date: 2026-05-25

## Abstract

Paper 27 identified the most promising remaining Branch-A positive route:
same-law spectral contraction plus a Peter-Weyl tail estimate for the actual
RN-MIXAMP conditional kernel.  This paper executes that route through the
four promised steps:

1. define the actual same-law conditional transfer operator for RN-MIXAMP;
2. compute or sharply bound the finite low-mode Peter-Weyl block norm;
3. prove or sharply audit the same-law Peter-Weyl tail;
4. compare the resulting low-mode-plus-tail quantity against the Paper-25
   contraction margin.

The result is again negative for the current corpus, but now the obstruction
is sharper.  The universal Markov/oscillation estimate gives only the
trivial non-expansion \(\Theta_L\le1\), while the Paper-25 route requires a
strict spectral gap after path entropy and endpoint conversion costs.  The
current papers also do not prove finite-band support, Peter-Weyl decay, or any
cofinal numerical tail schedule for the actual adaptive residual RN-MIXAMP
Hamiltonian.  Therefore the spectral route is reduced to a precise new
same-law source:
\[
\boxed{
\Theta_L^{act}+\kappa_L^{act}
<
\theta_{\mathrm{crit}}
}
\]
for a declared cutoff schedule, where both terms are evaluated on the same
adaptive `SEL2` pushed-forward scalar law.

No off-law heat kernel, continuum Yang-Mills measure, clean-row tail, or
hidden Markov subprocess is used.

## 0. Imports And Boundary

### Import 0.1: Paper-25 Step Margin

Paper 25 defines the actual Peter-Weyl step source
\[
\mathrm{P25\text{-}RPF\text{-}ACTUAL\text{-}HKPW\text{-}STEP}
(\theta,B_{step},h_{path},C_{path})
\]
and proves that it closes adaptive Branch A if
\[
        -\log\theta-h_{path}
        >
        \log\!\left(1+{B_{step}C_{path}\over4}\right).
\]
Equivalently, define the critical contraction
\[
        \theta_{\mathrm{crit}}
        :=
        \exp\!\left(
        -h_{path}
        -
        \log\!\left(1+{B_{step}C_{path}\over4}\right)
        \right).
\]
The spectral route closes only if
\[
        \theta<\theta_{\mathrm{crit}}.
\]

Since \(h_{path}\ge0\), \(B_{step}>0\), and \(C_{path}>0\), one has
\[
        0<\theta_{\mathrm{crit}}<1.
\]

### Import 0.2: Paper-25 Tail Gate

Paper 25 defines the actual conditional tail
\[
        \kappa_{PW}^{N,j}(L)
        :=
        \sup_{x,y}
        \left\|
        (I-\Pi_{\le L}^{xy})C_0^{m,N,j}(x,y)
        \right\|_{edge}.
\]
It proves that a finite Peter-Weyl projection becomes honest only after one
of the following same-law sources is supplied:

1. exact finite band support `PWBAND(L0)`;
2. uniform Peter-Weyl decay `PWDECAY(A,t)`;
3. a direct cofinal tail table
   \(\kappa_{PW}^{N,j}(L(N,j))\to0\).

### Import 0.3: Paper-26 And Paper-27 RN-MIXAMP Endpoint

Paper 26 identifies the minimal mixed RN ratio with the true mixed
`CleanRPF`/bridge amplitude table.  Paper 27 freezes the weighted RN-MIXAMP
row
\[
        {\mathfrak D}_{mix}^{N,j}(a)
        =
        \sup_x\sum_{y\ne x}
        e^{a d_{RPF}(x,y)}
        \tanh\!\left({D_{RN,0}^{N,j}(x,y)\over4}\right)
\]
and proves that the current corpus does not prove direct smallness, signed
cancellation, spectral contraction, or the lower floor.

This paper refines only the spectral contraction branch of that verdict.

### Boundary 0.4: Same-Law Spectral Discipline

A spectral estimate in this paper is admissible only if its operator,
projection, norm, and tail are computed from the same adaptive `SEL2`
pushed-forward scalar law.  A clean heat-kernel transfer matrix or a
comparison-law Peter-Weyl coefficient estimate is not admissible unless a
same-law transfer theorem is printed.

## 1. Step 1: Actual RN-MIXAMP Conditional Transfer Operator

### Definition 1.1: Local RN-MIXAMP Conditional Kernel

Fix a minimal live RPF edge \(e=(x,y)\), a finite adaptive template
\({\mathfrak T}\), and a cofinal record index \((N,j)\).  Let
\[
        K_{e,\zeta}^{N,j}(u,dv)
\]
be the conditional transition kernel obtained by:

1. pushing the adaptive `SEL2` scalar law to the declared local template;
2. conditioning on the outside configuration \(\zeta\);
3. isolating the residual RPF/RN-MIXAMP response along \(e\);
4. normalizing to a probability kernel on the endpoint compact group
   coordinate.

This kernel is a whole-law conditional object.  It is not a separately
introduced Markov subprocess.

### Definition 1.2: Transfer Operator

For bounded endpoint test functions \(f\), define
\[
        (T_{e,\zeta}^{N,j}f)(u)
        :=
        \int f(v)\,K_{e,\zeta}^{N,j}(u,dv).
\]
Let \(P_0\) denote the constant-mode projection and let
\[
        T_{e,\zeta,\circ}^{N,j}
        :=
        (I-P_0)T_{e,\zeta}^{N,j}(I-P_0)
\]
be the centered nontrivial-mode transfer.

### Definition 1.3: Low-Mode Peter-Weyl Block

For a Peter-Weyl cutoff \(L\), set
\[
        T_{e,\zeta,L}^{N,j}
        :=
        \Pi_{\le L}^{xy}
        T_{e,\zeta,\circ}^{N,j}
        \Pi_{\le L}^{xy}.
\]
The actual low-mode norm is
\[
        \Theta_L^{N,j}
        :=
        \sup_{e,\zeta}
        \left\|
        T_{e,\zeta,L}^{N,j}
        \right\|_{edge}.
\]
The edge norm is the same norm used in Papers 23--25 for the minimal-edge
contraction budget.

### Lemma 1.4: Same-Law Operator Is Well-Defined

For each finite template, cutoff, and finite record index, the matrix of
\(T_{e,\zeta,L}^{N,j}\) is finite and computable from the actual conditional
probabilities of the pushed-forward scalar law.

Proof.

The template and cutoff leave finitely many endpoint Peter-Weyl modes and
finitely many local conditionals.  The kernel \(K_{e,\zeta}^{N,j}\) is a
conditional probability kernel of the same finite pushed-forward scalar law.
Matrix entries are therefore finite integrals of Peter-Weyl matrix
coefficients against that conditional kernel. `square`

### Corollary 1.5: Step 1 Is Complete

The actual same-law conditional transfer operator required by the spectral
route is now defined.  The problem is not its existence; it is bounding
\(\Theta_L^{N,j}\) and the omitted tail cofinally.

## 2. Step 2: Low-Mode Block Norm

### Definition 2.1: Cofinal Low-Mode Norm

For a cutoff schedule \(L=L(N,j)\), define
\[
        \Theta^{act}[L]
        :=
        \limsup_{(N,j)}
        \Theta_{L(N,j)}^{N,j}.
\]

### Lemma 2.2: Universal Oscillation Non-Expansion Bound

In the operational sup norm,
\[
        \left\|T_{e,\zeta}^{N,j}\right\|_{\infty\to\infty}\le1.
\]
In the edge oscillation seminorm
\[
        \|f\|_{\mathrm{osc}}:=\sup f-\inf f,
\]
the centered transfer is non-expansive:
\[
        \left\|T_{e,\zeta,\circ}^{N,j}\right\|_{\mathrm{osc}\to\mathrm{osc}}
        \le1.
\]

Proof.

\(T_{e,\zeta}^{N,j}\) is integration against a probability kernel, hence it
maps bounded functions to conditional averages and cannot increase the
supremum norm.  More importantly for Dobrushin, it cannot increase
oscillation:
\[
\operatorname{osc}(Tf)
\le
\operatorname{osc}(f),
\]
because every value of \(Tf\) lies in the interval
\([\inf f,\sup f]\).  The centered operator is the induced operator on
functions modulo constants, so inserting \(I-P_0\) before and after the
kernel leaves the oscillation seminorm non-expansive. `square`

### Lemma 2.3: The Universal Bound Does Not Close

The estimate \(\Theta^{act}[L]\le1\) is insufficient for the Paper-25 step
margin.

Proof.

The Paper-25 margin requires
\[
        \theta<\theta_{\mathrm{crit}},
        \qquad
        0<\theta_{\mathrm{crit}}<1.
\]
A non-expansion bound \(\theta\le1\) gives no strict contraction after path
entropy and endpoint conversion costs. `square`

### Definition 2.4: Low-Mode Spectral Gap Source

`P28-RN-MIXAMP-LOWGAP(L,theta)` asserts that cofinally,
\[
        \Theta_L^{N,j}\le\theta<\theta_{\mathrm{crit}}.
\]

More generally, for a cutoff schedule \(L(N,j)\),
`P28-RN-MIXAMP-LOWGAP-SCH(theta)` asserts
\[
        \Theta^{act}[L]\le\theta<\theta_{\mathrm{crit}}.
\]

### Proposition 2.5: Current-Corpus Low-Mode Verdict

The current Papers 20--27 do not prove
`P28-RN-MIXAMP-LOWGAP(L,theta)` or
`P28-RN-MIXAMP-LOWGAP-SCH(theta)` for any closing \(\theta\).

Proof.

Lemma 1.4 shows that the finite low-mode matrices are well-defined if their
same-law conditional entries are supplied.  Paper 26 proves that these
actual RN-MIXAMP conditional/RN entries are not populated by the current
corpus.  Paper 27 proves that signed, direct, and spectral value estimates
are not currently available.  The only source-independent estimate is the
non-expansion of Lemma 2.2, and Lemma 2.3 shows it cannot meet the strict
Paper-25 margin. `square`

We record:
\[
\boxed{\mathrm{P28\text{-}RN\text{-}MIXAMP\text{-}LOWGAP\text{-}GAP}.}
\]

## 3. Step 3: Same-Law Peter-Weyl Tail

### Definition 3.1: RN-MIXAMP Tail Profile

For the actual RN-MIXAMP residual Hamiltonian \(C_{RN}^{N,j}\), define
\[
        \kappa_L^{N,j}
        :=
        \sup_{e,\zeta}
        \left\|
        (I-\Pi_{\le L}^{xy})C_{RN}^{N,j}(e,\zeta)
        \right\|_{edge}.
\]
For a cutoff schedule \(L(N,j)\), write
\[
        \kappa^{act}[L]
        :=
        \limsup_{(N,j)}\kappa_{L(N,j)}^{N,j}.
\]

### Definition 3.2: RN-MIXAMP Tail Sources

The following are admissible same-law tail sources:

1. `P28-RN-MIXAMP-PWBAND(L0)`:
   \[
   (I-\Pi_{\le L_0}^{xy})C_{RN}^{N,j}=0
   \]
   cofinally;
2. `P28-RN-MIXAMP-PWDECAY(A,t)`:
   \[
   \kappa_L^{N,j}
   \le
   A\exp(-t\lambda_{L+1}^{xy})
   \]
   cofinally for all sufficiently large \(L\);
3. `P28-RN-MIXAMP-KTAIL(kappa)`:
   \[
   \kappa^{act}[L]\le\kappa
   \]
   for a declared cutoff schedule.

### Lemma 3.3: Tail Source Is Necessary For Projection Honesty

A projected low-mode estimate alone does not bound the full RN-MIXAMP
conditional transfer unless one of the tail sources in Definition 3.2 is
supplied.

Proof.

The full conditional Hamiltonian splits into its projected part and
\((I-\Pi_{\le L})\)-tail.  A finite matrix norm controls only the projected
part.  The omitted complement may carry conditional oscillation unless the
same adaptive law bounds it.  This is exactly the Paper-23/Paper-25
projection-tail gate in RN-MIXAMP notation. `square`

### Proposition 3.4: Current-Corpus Tail Verdict

The current Papers 20--27 do not prove `P28-RN-MIXAMP-PWBAND(L0)`,
`P28-RN-MIXAMP-PWDECAY(A,t)`, or `P28-RN-MIXAMP-KTAIL(kappa)` for any useful
\(\kappa\).

Proof.

Paper 23 Section 55 proves that finite record support does not imply finite
Peter-Weyl band support after conditioning, central-entry division,
normalization, anchoring, and logarithms.  Paper 25 Section 13 imports this
verdict for the actual adaptive law.  Paper 26 identifies the RN-MIXAMP
object as a true residual RN/bridge amplitude table, but it does not supply
tail coefficients or a cofinal cutoff schedule.  Paper 27 confirms that no
same-law spectral value theorem has been supplied.

The heat-kernel/Casimir estimates in earlier papers are not enough: their
declared objects are clean or comparison-law rows unless a same-law transfer
theorem is printed.  No such transfer theorem exists in Papers 20--27.
`square`

We record:
\[
\boxed{\mathrm{P28\text{-}RN\text{-}MIXAMP\text{-}KTAIL\text{-}GAP}.}
\]

## 4. Step 4: Low-Mode Plus Tail Margin Test

### Definition 4.1: Spectral-Tail Closure Source

For a cutoff schedule \(L(N,j)\), define
\[
        \Xi^{act}[L]
        :=
        \Theta^{act}[L]+\kappa^{act}[L].
\]

`P28-RN-MIXAMP-SPECTAIL(theta)` asserts that
\[
        \Xi^{act}[L]\le\theta<\theta_{\mathrm{crit}}
\]
for some declared cutoff schedule \(L(N,j)\).

### Theorem 4.2: Spectral-Tail Source Closes Adaptive Branch A

If `P28-RN-MIXAMP-SPECTAIL(theta)` holds, then adaptive Branch A closes.

Proof.

The low-mode bound controls the projected actual RN-MIXAMP conditional
transfer.  The tail term pays the omitted Peter-Weyl complement on the same
law.  Their sum is therefore an admissible value of the Paper-25
step-contraction parameter \(\theta\).  Since
\(\theta<\theta_{\mathrm{crit}}\), the Paper-25 step theorem closes adaptive
Branch A. `square`

### Proposition 4.3: Current-Corpus Margin Test Fails To Prove Closure

The current Papers 20--27 do not prove `P28-RN-MIXAMP-SPECTAIL(theta)` for
any closing \(\theta\).

Proof.

By Proposition 2.5, the current corpus supplies no closing strict low-mode
gap; only the trivial non-expansion \(\Theta\le1\) is source-free.  By
Proposition 3.4, the current corpus supplies no useful same-law tail bound.
Since \(\theta_{\mathrm{crit}}<1\), the available bound cannot imply
\[
        \Theta^{act}[L]+\kappa^{act}[L]<\theta_{\mathrm{crit}}.
\]
`square`

We record:
\[
\boxed{\mathrm{P28\text{-}RN\text{-}MIXAMP\text{-}SPECTAIL\text{-}GAP}.}
\]

### Corollary 4.4: Exact Remaining Spectral Theorem

The spectral route is now reduced to one exact same-law theorem:
\[
\boxed{
\exists L(N,j)\quad
\Theta^{act}[L]+\kappa^{act}[L]
<
\theta_{\mathrm{crit}}.
}
\]

Equivalently, one must print:

1. the actual low-mode matrix values or a same-law strict spectral gap; and
2. finite-band support, Peter-Weyl decay, or a direct cofinal tail table.

No clean heat-kernel estimate, finite label count, or off-law comparison
operator can replace these two same-law value sources.

## 5. Final Paper-28 Verdict

### Theorem 5.1: Paper-28 Completion

Paper 28 completes the requested four-step spectral-tail investigation:

1. the actual RN-MIXAMP conditional transfer operator is well-defined;
2. the finite low-mode block is computable from actual same-law conditional
   entries, but the current corpus gives only non-expansion and no strict
   closing gap;
3. the same-law Peter-Weyl tail is explicitly defined, but the current
   corpus proves no finite-band, decay, or direct cofinal tail source;
4. the combined margin test therefore fails to prove adaptive Branch A from
   Papers 20--27.

The completed current-corpus gaps are
\[
\mathrm{P28\text{-}RN\text{-}MIXAMP\text{-}LOWGAP\text{-}GAP},
\qquad
\mathrm{P28\text{-}RN\text{-}MIXAMP\text{-}KTAIL\text{-}GAP},
\qquad
\mathrm{P28\text{-}RN\text{-}MIXAMP\text{-}SPECTAIL\text{-}GAP}.
\]

Proof.

The four items are Corollary 1.5, Proposition 2.5, Proposition 3.4, and
Proposition 4.3. `square`

### Corollary 5.2: What This Changes

Paper 28 does not close Branch A, but it narrows the spectral obstruction.
The problem is no longer `define a finite operator`.  The operator exists.
The problem is to prove, on the same adaptive law,
\[
        \Theta^{act}[L]<1
\]
with enough margin and simultaneously pay
\[
        \kappa^{act}[L].
\]

The next positive spectral attempt must therefore be numerical/analytic
value extraction for the actual pushed-forward scalar law, not more
structural bookkeeping.

This completes Paper 28.
