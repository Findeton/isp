# Independent hostile review — quantum combs and tester discrimination

**Target:** paper commit `fa02148f96b12b1bca8b663d30c282c70fe61473`  
**Frozen pin:** `3c958da7c8b78e2fc5eafdd7101762101ec1b4df`  
**Pin SHA-256:** `ec1e1c5e6ba6e003daf1cb0ccb88f13a7cd709fb26b55614ec2a8465ff9ef1f9`  
**Paper SHA-256:** `c2c8a27df423b417bcc8e11b68288f7c7169fee0b0f4b8c18b5ca3f440f1b74a`  
**Preceding adjudication SHA-256:** `f2c5568e2a729e402b118768eb669e8455490587063f4c6ee22245be00dcf4cb`  
**Mode:** repository read-only; independent exact calculations used `/private/tmp` only.

## Executive verdict

\[
\boxed{\texttt{RQ0-L0-BLOCKED-AT-TESTER-DESCENT}}
\]

The first two registered rungs survive:

1. `RQ0-L0-COMB-COMPLETE-W3` — **EARNED**, at the paper’s finite, definite-order, law-relative scope, subject to bounded tensor-order and direct-sum typing corrections.
2. `RQ0-L0-TESTER-SEPARATED-W3` — **EARNED**.
3. `RQ0-L0-W3-TEST-SHEAF` — **NOT EARNED by the frozen construction**.

The decisive failure is at the third rung. The site is built from testers of one fixed process type \(\tau\), but its proposed evaluation fibers simultaneously apply the same tester index to \(W,N\), \(V\star W\), \(V\star\mathcal D_RW\), \(E\star W\), and \(E\star\mathcal D_RW\). These generally have different open-wire profiles. No common outer type, padding supermap, or multi-sorted tester context is constructed. Consequently \(X_{s,a,\Xi}\), hence \(\mathcal E_s(U)\), is not defined at the advertised general typed scope. Stackification cannot repair an undefined evaluation functor.

There is also a new exact counterexample to the paper’s asserted exhaustivity of the nine branch-memory candidates. The six \(2+1+1\) values \(5/4\), the three \(2+2\) values \(1\), and the claim that all nine inherited candidates remain W3 are correct. What fails is the stronger assertion that terminal operational preservation forces the coarse record PVM to be a partition of the \(v_i\) basis. The frozen source/tester law is nonseparating, and an additional complex two-sector W3 PVM can be written explicitly.

No comb/process result crosses the paper’s one-chart firewall. No atlas, locality, topology, causality, field, or gravity claim is earned.

## Registered rung dispositions

| Registered rung | Verdict | Exact reason |
|---|---|---|
| `RQ0-L0-COMB-COMPLETE-W3` | **EARNED, narrowly** | Complete source, write/no-write, continuation, record, and output CP branches are retained as fields; flagged instruments retain weights, outcomes, output states, and disturbance. The explicit controls are valid typed finite networks. General notation needs direct-sum and tensor-order corrections. |
| `RQ0-L0-TESTER-SEPARATED-W3` | **EARNED** | The admitted-tester seminorm is sound; zero is exactly equality of all admitted tester probabilities; preservation and recovery are respectively zero and positive tester distance. The imaginary and real controls independently return \(0\) and \(1/2\). |
| `RQ0-L0-W3-TEST-SHEAF` | **NOT EARNED** | The evaluation presheaf is not typed across its named comparisons. The coordinate-product sheaf theorem survives for a fixed common type, but the paper does not construct the required multi-typed W3 evaluation object. |
| `RQ0-L0-BLOCKED-AT-BRANCH-CLASSIFICATION` | **NOT selected** | The nine inherited candidates are correctly reclassified and their distances are correct. Only the paper’s stronger exhaustivity claim fails. |
| `RQ0-L0-BLOCKED-AT-TESTER-DESCENT` | **SELECTED** | First registered obstruction after the two surviving rungs. |

## Findings, most severe first

### F1 — FATAL to the third rung: the tester-evaluation sheaf is not typed

Section 10 fixes one category \(\mathsf{Tester}_D(\tau)\), chooses a master set \(A\) in that category, and makes contexts subsets \(U\subseteq A\). Section 11 then defines, for every \(a\in A\),

\[
X_{s,a,\Xi},
\qquad
\Xi\in
\{W,N,V\star W,V\star\mathcal D_RW,E\star W,E\star\mathcal D_RW\}.
\]

But the named processes are not generally all of type \(\tau\):

- \(W,N\) terminate at the cut system \(H_1\);
- \(V\star W\) and \(E\star W\) terminate at \(H_2\), with retained continuation flags;
- output instruments may terminate in outcome-dependent systems \(K_j\);
- a tester of the open pre-continuation comb type contains a continuation, whereas a tester of the already-linked process does not.

Equality of Hilbert-space dimensions in a benchmark does not identify these labeled process types. The paper supplies neither:

1. deterministic embeddings of all comparisons into one flagged outer comb type, nor
2. a multi-sorted context \(a=(a_\Xi)_\Xi\) with \(a_\Xi\in\mathsf{Test}_D(\tau_\Xi)\).

Thus the product

\[
\mathcal E_s(U)
=
\prod_{a\in U}\prod_\Xi X_{s,a,\Xi}
\]

is undefined at the stated typed scope. The later coordinate-gluing proof is correct only after this missing typing is supplied.

A valid replacement construction would start with finite master families \(A_\Xi\subseteq\mathsf{Test}_D(\tau_\Xi)\), define contexts \(U=(U_\Xi)_\Xi\), and set

\[
\mathcal E_s(U)
=
\prod_\Xi\prod_{a\in U_\Xi}X_{s,a,\Xi},
\]

with componentwise-union covers and explicitly typed groupoid actions. That construction is not in the frozen paper. Because the pin requires a **correctly typed** tester-context site, this is a registered-rung failure rather than a wording note.

### F2 — MAJOR: terminal preservation does not exhaust candidates by \(v\)-partitions

The paper correctly proves preservation for its nine inherited \(v\)-partition candidates by the sufficient direction of Theorem 6.1. It incorrectly states that operational preservation **requires** the coarse projectors to be spans of blocks of \(\{v_0,v_1,v_2,v_3\}\).

The source family consists of four orthogonal written states

\[
\psi_j=U|j\rangle,
\]

whose density matrices span only a four-dimensional diagonal subspace, not the sixteen-dimensional Hermitian operator space. The paper’s own Corollary 6.2 therefore applies: the terminal probability law need not force the operator block identity.

An exact additional W3 candidate is as follows. Work in the written basis \(\{\psi_j\}\) and define a Hermitian unitary \(S\) by

\[
\begin{aligned}
S\psi_0&=i\psi_1,&S\psi_1&=-i\psi_0,\\
S\psi_2&=i\psi_3,&S\psi_3&=-i\psi_2.
\end{aligned}
\]

Let

\[
P_\pm=\frac{I\pm S}{2}.
\]

These are nontrivial rank-two coarse record projectors. They are not \(v\)-partition projectors: every \(v_i\) satisfies

\[
\langle v_i,P_\pm v_i\rangle=\frac12.
\]

Choose the fine rays

\[
\begin{aligned}
f_{0,\pm}&=\frac{\psi_0\pm i\psi_1}{\sqrt2},\\
f_{1,\pm}&=\frac{\psi_2\pm i\psi_3}{\sqrt2},
\end{aligned}
\]

with \(f_{0,+},f_{1,+}\) inside \(P_+\) and \(f_{0,-},f_{1,-}\) inside \(P_-\).

Then:

- **Write correlation:** each \(\psi_j\) has exactly one live fine ray inside each coarse sector.
- **No-write failure:** every \(v_i\) has probability \(1/4\) on each of the four fine rays, hence two positive fine alternatives inside each coarse sector.
- **Preservation:** write \(h_{ij}=\langle v_i,\psi_j\rangle=\pm1/2\) and \(k_{ij}=\langle v_i,S\psi_j\rangle=\pm i/2\). Then

  \[
  \sum_{\epsilon=\pm}
  |\langle v_i,P_\epsilon\psi_j\rangle|^2
  =
  \frac{|h_{ij}|^2+|k_{ij}|^2}{2}
  =
  \frac14,
  \]

  exactly the undephased terminal probability.
- **Recovery:** with \(E=U^*\),

  \[
  p_{\rm return}
  =
  \sum_{\epsilon=\pm}
  |\langle\psi_j,P_\epsilon\psi_j\rangle|^2
  =
  \frac12,
  \]

  so the terminal \(\ell^1\) recovery distance is \(2(1-1/2)=1>0\).

This candidate passes the same complete source and terminal tester law as the nine stated candidates. Varying the pairing phase gives further candidates. Therefore the secure sentence is:

> Within the inherited subfamily whose coarse record projectors are stipulated to be \(v\)-basis partition projectors, exactly six \(2+1+1\) and three \(2+2\) candidates pass, with distances \(5/4\) and \(1\). The nonseparating terminal law does not prove this subfamily exhaustive among all sharp record actions.

The nine benchmark results survive; “universal preservation requires” and any all-candidate finite census do not.

### F3 — MAJOR but bounded: several comb/instrument type formulas need correction

These defects do not overturn the explicit finite witnesses, but the general statements are not literally typed.

1. **Comb recursion order.** With the paper’s declared ascending tensor order

   \[
   H_0\otimes H_1\otimes\cdots\otimes H_{2n-1},
   \]

   tracing \(H_{2n-1}\) leaves the new input \(H_{2n-2}\) last. The displayed recursion should therefore be

   \[
   \operatorname{Tr}_{2n-1}C^{(n)}
   =
   C^{(n-1)}\otimes I_{2n-2},
   \]

   or the paper must declare the reversed CDP factor order under which \(I_{2n-2}\otimes C^{(n-1)}\) is literal. This is an ordering error, not a failure of comb normalization itself.

2. **Flagged Choi order.** With input-first Choi order, the flag belongs among the output factors. The expression

   \[
   \sum_i |i\rangle\langle i|_C\otimes J(\mathcal I_i)
   \]

   needs the appropriate canonical permutation of the labeled input and output factors.

3. **Outcome-dependent output systems.** Proposition 4.2 assumes all \(\mathcal I_i\) share one quantum output. Definition 4.1 allows \(\mathcal M_j:H_2\to K_j\). The correct common output is the tagged direct sum

   \[
   \widehat{\mathcal M}(\rho)
   =
   \bigoplus_j\mathcal M_j(\rho)
   \in
   \mathcal L\!\left(\bigoplus_jK_j\right).
   \]

   Under this correction, projection onto the \(j\)-summand recovers every CP branch, its probability, output system, and disturbance.

4. **Fine versus coarse instruments.** Although \(P_r=\sum_{k\in K_r}Q_k\) at effect level,

   \[
   P_r\rho P_r
   \ne
   \sum_{k\in K_r}Q_k\rho Q_k
   \]

   in general. Hence \(\mathbf R\subseteq\mathbf F\) is not an instrument coarse-graining. The paper’s subsequent formulas correctly use two distinct Lüders instruments, so the repair is to say explicitly that only their **effects** refine, while their disturbance maps are separately declared.

5. **Tester normalization.** The operational condition

   \[
   \sum_t\operatorname{Tr}(T_tC)=1
   \quad
   \text{for every deterministic }C
   \]

   is a sound finite-dimensional definition, but the promised dual recursion is asserted rather than printed. The standard network/tester characterization is indeed the one developed in the cited [Chiribella–D’Ariano–Perinotti paper](https://arxiv.org/abs/0904.4483).

### F4 — MINOR scope corrections

- “The continuation outcome remains available” means the **complete flagged object** is retained. It does not imply algebraic equality of every CP branch unless the admitted tester family separates the flag and conditional quantum outputs. Zero seminorm means equality under the admitted tests, exactly as the paper’s nonfaithful-family control recognizes.
- In Theorem 6.1, binary readouts exist for effects \(a\in\mathcal E\cap[0,I]\), not for every arbitrary element of the operator system. Equality then extends to the linear span.
- Under the no-\(1/2\) convention, the unrestricted norm is the standard strategy/comb norm. Multiplying by \(1/2\) gives total variation and \(2p_{\rm succ}-1\); the advantage \(p_{\rm succ}-1/2\) is one quarter of the paper’s raw \(\ell^1\) norm. “Bias” should specify which convention is intended. The cited strategy-norm source is correctly relevant: [Gutoski, *On a measure of distance for quantum strategies*](https://arxiv.org/abs/1008.4636).

## Independent tester-seminorm rebuild

For fixed \(\mathbf T=(T_t)\),

\[
q_{\mathbf T}(X)=\sum_t|\operatorname{Tr}(T_tX)|
\]

is a seminorm on the real Hermitian process space. Therefore its supremum over admitted testers is a seminorm. Finite-dimensional tester normalization makes the family bounded, so the supremum is finite even if the admitted subset is not closed.

Moreover,

\[
\|X\|_{\mathsf{Test}_D}=0
\iff
\operatorname{Tr}(T_tX)=0
\quad\text{for every admitted }(\mathbf T,t).
\]

Thus for deterministic combs \(C,C'\), zero is exactly equality of every admitted complete-tester probability. No hidden coefficient survives unless it lies in the operational kernel.

For an admitted deterministic supermap \(S\),

\[
\operatorname{Tr}(T_tS(X))
=
\operatorname{Tr}((S^*T_t)X).
\]

If tester pullbacks are admitted, taking the supremum gives

\[
\|S(X)\|_{\mathsf{Test}_D}
\le
\|X\|_{\mathsf{Test}_D}.
\]

This proves contraction and congruence for the linked deterministic/flagged-complete continuations used by W3.

Basis changes, valid Choi-presentation changes, and handle permutations act simultaneously on processes and dual testers and preserve every closed probability. Presentation invariance therefore survives, although “corresponding partial transposes” should be understood as the induced dual representation change, not an arbitrary partial transpose of a positive operator.

At unrestricted scope, a multi-outcome tester can be coarse-grained according to the sign of \(\operatorname{Tr}(T_tX)\). The resulting binary measuring co-strategy attains the same sum of absolute values. Hence the paper’s unrestricted \(\ell^1\) norm agrees with the standard strategy norm, with no missing factor in its declared convention. The standard strategy representation and measuring-co-strategy pairing are also supported by [Gutoski–Watrous](https://arxiv.org/abs/quant-ph/0611234).

## Independent W3 predicate audit

The operational definitions are sound:

\[
\|\boldsymbol{\mathcal V}\star W-
\boldsymbol{\mathcal V}\star\mathcal D_R\star W\|=0
\]

is precisely equality under every admitted downstream closed experiment, and

\[
\|\boldsymbol{\mathcal E}\star W-
\boldsymbol{\mathcal E}\star\mathcal D_R\star W\|>0
\]

is precisely existence of an admitted outcome-probability contrast.

For normalized deterministic or flagged-complete processes,

\[
0\le \mathcal C_R(W;E)\le2.
\]

Restriction of the tester family can only decrease the supremum. An admitted downstream supermap contracts it by tester pullback. These statements, presentation invariance, and the distinction from the Born and multiplicativity defects all survive.

Write and no-write are complete probability statements on subnormalized source branches. The explicit four-level and branch-memory fine instruments are Lüders instruments, so zero fine probability removes the relevant positive support block. No branch weight is discarded.

## Effect-versus-instrument audit

Theorem 6.1 is correct after replacing “all \(a\in\mathcal E\)” by the admitted effect interval and then extending linearly. For a separating source family,

\[
\operatorname{Tr}\rho\,
\bigl(V^*(a)-\mathcal D_RV^*(a)\bigr)=0
\quad\forall\rho
\]

forces

\[
V^*(a)=\mathcal D_RV^*(a),
\]

equivalently \(P_rV^*(a)P_s=0\) for \(r\ne s\). Without source separation, the block condition remains sufficient but is not necessary. The new branch-memory counterexample above is an exact instance of that caveat.

The Lüders/reprepare example correctly proves that effect equality does not imply complete-instrument equality. On input \(q_1\),

\[
\mathcal L_A(q_1)=q_1,\qquad
\mathcal J_A(q_1)=q_0,
\]

while both instruments have effect \(P_A\). A retained outcome followed by computational readout gives disjoint distributions and distance \(2\).

The multiplicative-domain proposition is also correct: for UCP \(F\), equality \(F(P_r)=F(P_r)^2\) puts each record projection in \(\operatorname{MD}(F)\); the multiplicative domain is a C*-subalgebra, so the entire finite record algebra is transported homomorphically. The paper correctly refuses to promote this to equality of complete Schrödinger instruments.

## Exact-control rebuild

| Control | Claimed | Independent result | Verdict |
|---|---:|---:|---|
| Imaginary cross term | \(-i/4\), tester distance \(0\) | \(\langle\psi|q_0a_iq_2|\psi\rangle=-i/4\); conjugate cancels; every admitted binary probability agrees | **PASS** |
| Real-phase eraser | \(1/2\) | Branches \(0,2\) each contribute weight \(1/4\) times binary \(\ell^1\) distance \(1\); total \(1/2\) | **PASS** |
| Unequal source weights | at least \(\sum_\alpha|p_\alpha-q_\alpha|\) | Exact when later conditional processes coincide | **PASS** |
| Same POVM/different disturbance | \(2\) | Lüders output \(q_1\), reprepare output \(q_0\); perfect tail separation | **PASS** |
| Interactive tail | separates where label-only test cannot | Outcome \(A\) followed by computational readout separates perfectly | **PASS** |
| Inaccessible spectator | identical probability functors | \(\operatorname{Tr}[(T\otimes I)(C\otimes\sigma)]=\operatorname{Tr}(TC)\) under the stated tester-image premise | **PASS** |
| Nonfaithful tester family | distinct processes at zero distance | Imaginary restricted law identifies coherent/dephased states; adding the real tester separates them | **PASS** |
| Context variance | witness lost under restriction | \(T_+\) witnesses recovery, \(T_i\) does not; preservation can also appear falsely under a nonseparating singleton | **PASS** |

No factor-of-two error occurs in these values because the paper consistently omits the conventional \(1/2\).

## Independent nine-candidate rebuild

Let \(H=A/2\), where the displayed Hadamard matrix satisfies \(A^*A=4I\), and set

\[
\psi_j=U|j\rangle
=
\frac12\sum_iA_{ij}v_i.
\]

For an inherited partition \(\pi\) of the \(v_i\):

- a singleton block \(\{a\}\) has fine ray \(v_a\);
- a double block \(\{a,b\}\) has fine rays
  \((v_a+v_b)/\sqrt2\) and \((v_a-v_b)/\sqrt2\).

Every restricted Hadamard column in a double block lies on exactly one of these rays, so write correlation holds. The no-write states are the \(v_i\); inside a double block, \(v_a\) and \(v_b\) each have probability \(1/2\) on both fine rays, so no-write failure holds whenever a double block is present. Triple blocks contain four distinct restricted Hadamard rays that cannot be embedded in a three-ray orthogonal fine PVM, while the all-singleton partition has no possible within-sector no-write failure.

Hence the inherited partition census is exactly

\[
6\text{ of type }2+1+1
\quad\sqcup\quad
3\text{ of type }2+2.
\]

For these candidates, the pulled-back terminal effects under \(V\) are the \(v_i\) projectors and are block diagonal, so preservation distance is zero.

After coarse dephasing and \(E=U^*\),

\[
p(k|j)
=
\sum_{B\in\pi}
\left|
\frac14\sum_{i\in B}A_{ik}A_{ij}
\right|^2.
\]

In particular,

\[
p(j|j)
=
\frac1{16}\sum_{B\in\pi}|B|^2.
\]

Because the coherent distribution is deterministic,

\[
\mathcal C_{R_\pi}
=
2\left(
1-\frac1{16}\sum_B|B|^2
\right).
\]

Thus:

\[
\begin{array}{c|c|c}
\text{type}&\sum_B|B|^2&\mathcal C_R\\ \hline
2+1+1&6&5/4\\
2+2&8&1
\end{array}
\]

for every retained source branch and hence for the equally weighted flagged source instrument.

Therefore all nine inherited candidates remain W3 and the reported values are exact. The failure is only the claim that these nine exhaust all sharp W3 actions under the nonseparating terminal law.

## One-chart and ontology audit

The paper consistently confines \(\mathsf{Test}_D\), \(A_D\), the operational quotient, and “global sections” to one finite chart. No atlas-wide tester, cross-chart event set, or global state is used. The definite laboratory wire order is not promoted to causal order.

The following claims therefore survive unchanged:

\[
\text{W3 seam}
\ne
\text{actual outcome}
\ne
\text{fact co-reference}
\ne
\text{event-token identity}.
\]

No spatial localization, topology, influence, causality, Lorentzian structure, field, or gravity conclusion is present.

## Exact surviving and failed claims

**Survive:**

- the complete-process replacement of state/effect shadows;
- the common-output/direct-sum flagged-instrument equivalence;
- the tester seminorm, operational kernel, contraction, and unrestricted-norm relation;
- operational preservation and positive-probability recovery;
- the \(0\le\mathcal C_R\le2\) bound and monotonicity;
- the terminal effect theorem with its separating-source hypothesis;
- the nonseparating-source caveat;
- the multiplicative-domain comparison;
- every listed exact control and the values \(0,\frac12,2\);
- all nine inherited branch-memory candidates;
- the six values \(5/4\) and three values \(1\);
- the coordinate-product sheaf lemma for a genuinely fixed common process type;
- the universal/existential variance diagnosis;
- singleton evidence not being chart-complete evidence;
- the one-chart and ontology firewalls.

**Fail or require withdrawal:**

- `RQ0-L0-W3-TEST-SHEAF` as a typed construction;
- the use of one tester \(a\) across differently typed named comparisons;
- the finite all-candidate groupoid if it is meant to exhaust the declared sharp actions;
- “universal preservation requires a \(v\)-partition” under the frozen nonseparating source/tester law;
- any claim that the nine inherited candidates are the complete sharp-candidate census;
- the literal ascending-order comb recursion as printed;
- the literal flagged formula for outcome-dependent \(K_j\);
- \(\mathbf R\subseteq\mathbf F\) as a CP-instrument coarse-graining;
- the assertion that retained flags automatically imply branchwise algebraic separation by an arbitrary admitted tester family.

## Required replacement sentences

For the branch-memory section:

> Within the inherited candidate subfamily whose coarse record projectors are spans of blocks of \(\{v_0,v_1,v_2,v_3\}\), exactly six \(2+1+1\) and three \(2+2\) candidates pass, with recovered coherences \(5/4\) and \(1\). The frozen source and terminal tester family is not tomographically separating, so this calculation does not exhaust all sharp record actions.

For the outcome section:

> `RQ0-L0-COMB-COMPLETE-W3` and `RQ0-L0-TESTER-SEPARATED-W3` are supported at the stated finite law-relative scope. `RQ0-L0-W3-TEST-SHEAF` is not earned because the displayed evaluation presheaf applies one fixed-type tester index to named process comparisons with different wire profiles. The selected registered disposition is `RQ0-L0-BLOCKED-AT-TESTER-DESCENT`.

For the flag-separation sentence:

> Retaining the classical continuation flag preserves every CP branch as part of the process object. Equality at zero tester seminorm is equality under all admitted tests; it becomes branchwise algebraic equality only when the admitted tester family separates the flag-conditioned outputs.

## Final disposition

The comb/tester successor repairs the preceding operational-Morita failure at the first two registered levels: full CP branches are retained, algebraic false erasure is replaced by closed-experiment probability contrast, and the exact controls survive independent reconstruction.

The frozen paper does not yet supply a typed W3 tester sheaf, and its terminal benchmark does not exhaust sharp record actions. The highest secure new rung is therefore

\[
\boxed{\texttt{RQ0-L0-TESTER-SEPARATED-W3}},
\]

with cycle disposition

\[
\boxed{\texttt{RQ0-L0-BLOCKED-AT-TESTER-DESCENT}}.
\]

The antecedent terminal `RQ0-L0-ADDRESSABLE-W3-OPERATOR-SYSTEM` result is not reopened or weakened.
