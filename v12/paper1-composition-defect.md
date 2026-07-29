# Interference as the Composition Defect of Stochastic Shadows: Records, Gauge, and the Loop Signature of Indivisible Stochastic Processes

## Abstract

Barandes' formulation of quantum theory replaces the state vector by an
*indivisible stochastic process*: a fixed configuration space carrying
definite configurations at all times, together with transition matrices
supplied only at a sparse set of *division events*, and an identity
$\Gamma = |\Theta|^{\circ 2}$ exhibiting each transition matrix as the
entrywise modulus square of a complex propagator [1,3]. Because the laws
are supplied only at division events, the question of what happens *between*
them — of how the stochastic representation composes across a cut — is
posed by the framework but not answered by it. This paper studies that
question.

We take as the subject the **composition defect**
$$
\Delta^{B}(U_2,U_1)\;:=\;B(U_2U_1)\;-\;B(U_2)\,B(U_1),
\qquad B(U)=|U|^{\circ 2},
$$
and prove: (i) a closed form identifying $\Delta^{B}_{ij}$ with the total
pairwise interference of the path amplitudes through the cut, an exact
separation of $\Delta^{B}$ from the residual of a declared stochastic law
and from existential divisibility, a coherence law valid at every
bracketing, a complete two-sided annihilator theory (the monomial group),
and an identification of the vanishing locus on a Fourier-sandwich family
with flatness of a discrete spectrum — the CAZAC condition, which is
classical and cited, not derived here; (ii) a **records theorem**: two
support hypotheses, stated with no reference to any defect, force the
defect to vanish termwise, with an $O(n^2)$ decision procedure for the
existential question "does *any* record structure work?", exact sharpness
on unitarily realizable supports at $n=3$, and an eraser control that
locates the boundary; (iii) a **gauge reduction**: the entrywise
Schur–Hadamard freedom of [3] is annihilating on a single arrow, and its
composition-compatible subgroup is *exactly* the boundary gauge — proved
twice, once from compatibility with the admissible class of composable
dynamics and once from preservation of unitarity, with the residual
stabilizer that "partial fixing of the gauge freedom" [3, p.19] leaves
computed exactly; (iv) a **loop signature** for the reduced gauge, whose
completeness for a composable pair holds *exactly when* the four-cycles
generate the cycle lattice of a tripartite path graph, with the failure
realized at every failing support class at $n=4$ by an uncompensated cut,
and whose completeness for the *composite* is refuted at one class by an
exact unitary witness; a cross-block completion closes every gap found at
$n\le 4$ exhaustively and at a declared $n=5$ sample; (v) a **record
descent** for the signature, together with its limit: a pair may carry a
record, have a fully diagonal cut-coherence tensor, and still have a
composite carrying a boundary-gauge phase invariant; (vi) an
**independence** result: four obstruction families — temporal, contextual,
lattice-gluing and frame-mappability — are pairwise independent on a
common finite carrier, with witnesses in both directions for all six pairs;
and (vii) a **law-of-total-probability lemma** proved against [3]'s own
equations (19)–(20), whose contrapositive forces the withdrawal of an
exactly declared, unmarginalized division event wherever the declared law
fails to compose on the model's own distribution — exhibited on a
36-configuration two-measurement model built here from scratch.

All results are finite-dimensional and are stated with their scopes. Every
number printed below is regenerated in exact arithmetic (rational
arithmetic, cyclotomic and totally real number fields, integer lattices)
by the accompanying code bundle; no floating-point number and no tolerance
occurs anywhere in the reproduction.

---

## 1. Introduction

### 1.1 The framework, and the question

Barandes [1,2,3] formulates quantum theory as follows. A system is given by
a **configuration space** $C$, a fixed ingredient of the model: *"one can
take the sample space to be the system's configuration space $C$, which is
a fixed ingredient of the model, meaning that it remains the same for every
physical run or instantiation of the model"* [3, p.5]. Over it there is a
contingent **standalone probability distribution** $p(i,t)$, which supplies
*"the model's informational or 'epistemic' content"* [3, p.5]. The
**dynamical law** consists of transition probabilities $p(i,t\mid j,t_0)$,
and — this is the characteristic move — they are supplied only for a sparse
set of conditioning times:

> "Note that **no assumption is made** here that the transition
> probabilities $p(i,t\mid j,t_0)$ exist as part of the laws for **all**
> real-valued choices of $t_0$. Allowed conditioning times $t_0$ are called
> **division events** for the given system, and, without any real loss of
> generality, are assumed to include an 'initial' time $0$." [3, p.9]

The target time, by contrast, is free: *"The target time $t$ … can be
treated as a free variable. In particular, no assumption is made that
$t>t_0$."* [3, p.10]. At a division event the law of total probability
holds exactly, $p(t)=\Gamma(t\leftarrow t_0)\,p(t_0)$ [3, p.9, eqs. 19–20],
and *"the law of total probability (19) is linear"* [3, p.9]. Away from
division events the process is **indivisible**: *"an indivisible stochastic
process, as befits its name, will not generally obey a divisibility
condition"* [3, p.10]. Attempting to manufacture an intermediate leg
$\tilde\Gamma(t\leftarrow t')=\Gamma(t\leftarrow t_0)\Gamma^{-1}(t'\leftarrow t_0)$ produces, in Barandes' own diagnosis, an object that *"will
generically fail to be a column stochastic matrix, and, indeed, will
typically have negative entries, and so will form a so-called
pseudo-stochastic matrix"* [3, p.10].

The bridge to Hilbert space is the identity
$$
\Gamma_{ij}(t\leftarrow 0)\;=\;\bigl|\Theta_{ij}(t\leftarrow 0)\bigr|^{2},
$$
of which Barandes writes: *"Note that this formula is **not a postulate,
but an identity**, and that the potential matrix $\Theta(t\leftarrow 0)$ …
is **not unique**"* [3, p.11, eq. 25]. The non-uniqueness is an entrywise
phase freedom: *"the Schur-Hadamard product (27) of the time-evolution
operator $\Theta(t\leftarrow 0)$ and a matrix of arbitrary, time-dependent
phases $\exp(i\theta_{ij}(t))$ is a transformation of $\Theta(t\leftarrow 0)$ with **no physical effects**, and therefore corresponds to a genuine
form of **gauge invariance**"* [3, p.12, eqs. 29–30]; the phases carry one
$U(1)$ per *ordered pair* of configurations, as [3]'s own dilated version
makes explicit — the internal unitaries are *"labeled by a specific pair
$(ij)$ of configuration labels"* [3, p.27, eq. 106]. Fixing a unitary
representative is therefore only a partial gauge fixing: *"a unitary
time-evolution operator $U(t\leftarrow 0)$ will **not generically remain
unitary** under arbitrary Schur-Hadamard gauge transformations (30). Hence,
writing a unistochastic transition matrix $\Gamma(t\leftarrow 0)$ in terms
of a unitary time-evolution operator $U(t\leftarrow 0)$ corresponds to
making a **gauge choice** — or, somewhat more precisely, to a **partial
fixing of the gauge freedom** (30)."* [3, p.19].

Two things are conspicuous in this presentation. First, the framework
*names* the phenomenon we study — *"indivisible stochastic processes
generically exhibit all the hallmark empirical features of quantum systems,
including **interference**, decoherence, entanglement, and noncommutative
observables"* [3, p.2] — but supplies no invariant that measures it.
Second, the entrywise gauge is declared for a *single* propagator, and
nothing in [3] says which part of it survives when propagators are asked to
compose. This paper supplies both: an invariant, and the exact residual
that the gauge leaves.

### 1.2 The subject

Write $B(U):=|U|^{\circ 2}$ for the entrywise Born projection and, for a
composable pair of propagators,
$$
\Delta^{B}(U_2,U_1)\;:=\;B(U_2U_1)\;-\;B(U_2)B(U_1).
$$
This is the failure of the Born shadow of the coherent composite to equal
the shadow one obtains by forgetting phases and restarting at the
intermediate cut. Everything below is organized around it: its algebra
(§2), its location relative to the correlation bodies of the CHSH
scenario (§3), the exact conditions on records that kill it (§4), the gauge
under which a *compositional* invariant may be built (§5), the phase-
retaining signature that the Born shadow cannot see (§6), the descent of
that signature under records and the limit of the descent (§7), its
independence from three other obstruction families (§8), and its relation
to Barandes' own equations (§9).

### 1.3 Contributions

The following are proved here, each with its scope tag.

1. **The closed form and the three-defect separation** (Theorems 2.1, 2.3).
   $\Delta^{B}_{ij}=|\sum_k w_k|^2-\sum_k|w_k|^2$ with $w_k$ the amplitude
   of the path through the cut; and an exact rational pair of $2\times 2$
   rotations with $\Delta^{B}\ne 0$ for which the shadow nevertheless admits
   a stochastic divisor. $\Delta^{B}$ is an amplitude-level coherence
   measure and is *not* a divisibility measure. *Scope: all finite
   dimensions for the identity; one exact rational pair for the
   separation.*

2. **The coherence law at every bracketing** (Theorem 2.5), together with
   the honest measurement that it is an identity of associativity: it
   survives replacing $B$ by six declared substitutes, including a map that
   ignores its argument. It constrains the family and selects nothing.

3. **The two-sided annihilator** (Theorem 2.8): the set of left factors
   annihilating the defect against *every* unitary is exactly the
   row-monomial unitaries, and dually. *Scope: hand proof with gated
   ingredients; the universal quantifier is carried by an explicit probe.*

4. **The flat-spectrum identification** (Theorem 2.10). On the
   Fourier-sandwich family the defect vanishes exactly when the
   interleaving diagonal has a flat discrete spectrum. That flatness is
   equivalent to vanishing periodic autocorrelation is the discrete
   Wiener–Khinchin theorem and the definition of a CAZAC sequence [16]:
   **the equivalence is classical and is cited, not proved here.** What is
   ours is the identification of the vanishing locus with that condition.

5. **The records theorem with a decision procedure** (Theorems 4.2, 4.6,
   4.8, 4.9). Two support hypotheses — perfect correlation and availability
   — stated without reference to any defect, force every cross term to
   vanish individually. The existential question *does any record structure
   exist?* is not a search: it is decided by one union-find pass, in
   $O(n^2)$. On unitarily realizable supports at $n=3$ the criterion is
   exactly sharp (318 of 318); on abstract $0/1$ patterns it is not (5 490
   of 94 746). *Scope: finite dimension; sufficiency, never necessity.*

6. **The gauge reduction, derived twice** (Theorems 5.4, 5.5). The
   composition-compatible subgroup of the entrywise gauge is exactly the
   boundary gauge, and so is the subgroup preserving unitarity — the exact
   residual stabilizer that [3, p.19]'s "partial fixing" leaves open. The
   load-bearing quantifier in the first route is named and *measured*: on a
   totally path-degenerate pair that route licenses nothing, and the second
   route alone carries the verdict there.

7. **The pair-orbit theorem and the completeness dichotomy** (Theorems 6.7,
   6.11). The reduced gauge acts as vertex switching on a tripartite path
   graph; a complete set of invariants at fixed moduli is a cycle basis.
   For the *pair*, the declared signature is complete **exactly when** the
   four-cycles generate; where they do not, the gap is realized by an
   uncompensated cut for every unitary pair with that support — established
   at all seven failing classes at $n=4$. For the *composite* the question
   is strictly stronger and is refuted at one class by an exact unitary
   witness whose two pairs share the entire signature *and* the entire
   defect family. *Scope: exhaustive for $n\le4$; a declared strided sample
   at $n=5$; general $n$ open.*

8. **The cross-block completion** (§6.6). A single uniformly definable
   octic invariant closes every gap at the declared scope, and its total
   over the block indices *equals* the composite's own four-cycle
   invariant — a derived identity, not an input. It is **sufficient and not
   claimed minimal**: every failing class has rank deficit exactly one, so
   a smaller completion is not excluded.

9. **A phase-retaining invariant the Born shadow does not determine**
   (Proposition 6.3). The relation-loop scalar $\beta$ separates all $N$
   Weyl classes at $N=2,\dots,6$ while their Born shadows are identical.
   The claim is **non-factorization, not refinement**: $\beta$ is *not a
   functional of* $B\circ\rho$, and it is *not* finer than it — a
   counterexample is exhibited.

10. **Record descent and its measured limit** (Theorems 7.1, 7.2, §7.4).
    Availability alone block-diagonalizes the cut-coherence tensor;
    correlation collapses it inside a block. Block-diagonalization is
    **not** phase triviality, and a pair may carry a record, have a fully
    diagonal tensor, and still have a phase-nontrivial composite.

11. **Independence of four obstruction families** (§8). All six pairs are
    independent on a common 48-process carrier, with witnesses in both
    directions found mechanically by a test declared before the models were
    built. *Scope: one measurement scenario, six empirical models, nine
    configurations.*

12. **The law-of-total-probability lemma and its forcing** (Lemma 9.1,
    §9.3). Against [3]'s own eqs. (19)–(20), the declared-law residual must
    annihilate every admissible distribution; the matrix form needs a
    spanning hypothesis which [3] does not state and which is shown here to
    be load-bearing. The contrapositive fires on an exactly declared,
    unmarginalized division event in a two-measurement model, at three of
    six setting pairs and in both time orderings. Barandes' own hedge —
    that division events *"may be generated to an extremely good
    approximation … after marginalizing over those other systems"*
    [3, p.10] — describes a different object and is **not tested here**.

### 1.4 What is not claimed

No claim is made about nature. Every result is a statement about declared
finite models, declared families and declared scopes. No derivation of the
Born rule is claimed; no interpretation is advanced; no ontological
conclusion is drawn from any invariant exhibited here. The relation to
Barandes in §9 is a delimited reading of published texts, with his hedges
quoted where they bear. §10 restates every scope.

---

## 2. The three defects and the coherence law

Throughout, $U$ ranges over $n\times n$ unitaries unless stated otherwise,
$B(U)_{ij}=|U_{ij}|^2$, and for a composable pair we write
$$
w_k \;=\; w_k^{ij} \;=\; (U_2)_{ik}(U_1)_{kj}
$$
for the amplitude of the path through the intermediate configuration $k$.

### 2.1 The closed form

**Theorem 2.1 (closed form).** *For every composable pair and all $i,j$,*
$$
\Delta^{B}_{ij}\;=\;\Bigl|\sum_k w_k\Bigr|^{2}-\sum_k|w_k|^{2}
\;=\;2\sum_{k<\ell}\operatorname{Re}\bigl(w_k\overline{w_\ell}\bigr).
$$

*Proof.* $B(U_2U_1)_{ij}=|(U_2U_1)_{ij}|^2=|\sum_k w_k|^2$ and
$(B(U_2)B(U_1))_{ij}=\sum_k |(U_2)_{ik}|^2|(U_1)_{kj}|^2=\sum_k|w_k|^2$.
Subtract. Writing $w_k=x_k+iy_k$, the difference
$(\sum x_k)^2+(\sum y_k)^2-\sum(x_k^2+y_k^2)$ equals
$2\sum_{k<\ell}(x_kx_\ell+y_ky_\ell)$, which is
$2\sum_{k<\ell}\operatorname{Re}(w_k\overline{w_\ell})$. $\square$

The second equality is a polynomial identity over $\mathbb{Q}$; it is
verified symbolically at $d=2,\dots,6$ and against the definition on all
$72\,585$ entries of the two reference families of §2.2, with $0$
mismatches. **The defect entry is the total pairwise interference of the
path amplitudes through the cut, and nothing else.** The identification of
these cross terms with interference is Barandes' [1]; the closed form is a
rewriting of it.

### 2.2 Two reference families

Two finite families are used as carriers throughout; both are declared here
and every member is verified unitary in exact arithmetic.

$$
\begin{aligned}
\mathcal{F}_2\subset U(2)\ \text{over}\ \mathbb{Q}(\zeta_8):&\quad
P\cdot\operatorname{diag}(\mu_4)\ \text{and}\
\operatorname{diag}(1,\mu_8)\,H\,\operatorname{diag}(1,\mu_8),\\
\mathcal{F}_3\subset U(3)\ \text{over}\ \mathbb{Q}(\zeta_{12}):&\quad
P\cdot\operatorname{diag}(1,\mu_3,\mu_3)\ \text{and}\
D(\mu_3)\,F_3\,D(\mu_3),
\end{aligned}
$$
with $H$ the $2\times2$ Hadamard, $F_3$ the $3$-point Fourier matrix,
$D(m)=\operatorname{diag}(1,\omega^m,1)$, and $P$ ranging over the
permutation matrices. Then $|\mathcal{F}_2|=96$ (32 monomial) and
$|\mathcal{F}_3|=63$ (54 monomial); $9216$ and $3969$ ordered pairs. Every
family entry has a rational non-negative modulus square; the modulus square
of an entry of a *product* need not be rational (for instance
$|1+\zeta_8|^2=2+\sqrt2$), so the Born projection is carried in the field
throughout and never coerced.

Calling a pair *conditioned* when $U_2$ has at most one nonzero per row or
$U_1$ has at most one nonzero per column, the vanishing census is exact:

| | conditioned, $\Delta^{B}=0$ | conditioned, $\Delta^{B}\ne0$ | free, $\Delta^{B}=0$ | free, $\Delta^{B}\ne0$ |
|---|---|---|---|---|
| $2\times2$ | 5120 | **0** | 1024 | 3072 |
| $3\times3$ | 3888 | **0** | 54 | 27 |

The conditioned column is empty of nonzero defects — the $k\ne\ell$ sum is
literally empty — and the free column shows the condition is far from
necessary. A named witness uses the Hadamard matrix $H$ and the unitary $V$,
$$
H=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
V=\frac{1}{\sqrt2}\begin{pmatrix}1&i\\i&1\end{pmatrix},
$$
both of which are fully unbiased. For these,
$$
\Delta^{B}(H,V)=0,
\qquad
\Delta^{B}(H,H)=\begin{pmatrix}\tfrac12&-\tfrac12\\[2pt]-\tfrac12&\tfrac12\end{pmatrix}.
$$

### 2.3 The three defects, separated

Three objects must never be conflated:
$$
\begin{array}{ll}
\Delta^{B}(U_2,U_1)=B(U_2U_1)-B(U_2)B(U_1) & \text{the Born-shadow defect;}\\[3pt]
D \;=\;\Gamma_{20}-\Gamma_{21}\Gamma_{10} & \text{the residual of a declared law;}\\[3pt]
d_{\mathrm{div}}\;=\;\inf_{K\in\mathrm{Stoch}}\|\Gamma_{20}-K\Gamma_{10}\| & \text{existential divisibility.}
\end{array}
$$
Under the Born declaration $\Gamma_{21}:=B(U_2)$ the first two coincide;
in general they do not, and $d_{\mathrm{div}}$ is a third object.

**Theorem 2.3 (separation).** *There is an exact rational pair of $2\times2$
unitaries with $\Delta^{B}\ne0$ whose Born shadow nevertheless factorizes
through a genuine stochastic matrix. Hence $\Delta^{B}\ne0$ does not imply
stochastic indivisibility.*

*Proof.* Let $R(\theta)$ be the real rotation and let
$$
S(x)=\frac12\begin{pmatrix}1+x&1-x\\1-x&1+x\end{pmatrix}.
$$
Two polynomial identities over $\mathbb{Q}$, both verified symbolically:
$B(R(\theta))=S(\cos2\theta)$ modulo $c^2+s^2=1$, and $S(c)S(d)=S(cd)$.
Take $U_1=R(\theta_1)$ with $(\cos\theta_1,\sin\theta_1)=(24/25,7/25)$ and
$U_2=R(\theta_2)$ with $(4/5,3/5)$. Then
$$
c_1=\tfrac{527}{625},\qquad c_2=\tfrac{7}{25},\qquad
c_{\mathrm{tot}}=c_1c_2-s_1s_2=-\tfrac{7}{25},
$$
so $\Delta^{B}_{00}=\tfrac12(c_{\mathrm{tot}}-c_1c_2)=-\tfrac{4032}{15625}\ne0$;
with the Born declaration $D=\Delta^{B}$, so the declared residual is
nonzero too. Yet $K=S(-175/527)$ has entries $(1\pm x)/2\ge0$ and unit
column sums, and $K\,B(U_1)=S(-\tfrac{175}{527})S(\tfrac{527}{625}) =S(-\tfrac{175}{625})=S(-\tfrac{7}{25})=B(U_2U_1)$ exactly. Also
$K\ne B(U_2)$: the divisor exists but is not the Born shadow of the second
step. $\square$

The construction is general for rotations: whenever
$|c_{\mathrm{tot}}|\le|c_1|$, the matrix $S(c_{\mathrm{tot}}/c_1)$ is a
stochastic divisor. This is verified on $22\,062$ exact rational
$(c_1,c_{\mathrm{tot}})$ pairs, with $0$ failures.

**Engraved.** $\Delta^{B}$ is an amplitude-level coherence measure. It is
not a divisibility measure, not a witness of indivisibility, and not the
residual of any declared stochastic law unless that law is declared to be
$B(U_2)$.

### 2.4 The invariance group, and the one handle

**Proposition 2.4.** *With $D,D'$ diagonal unitary and $P$ a permutation:*

| | law | |
|---|---|---|
| (i) | $\Delta^{B}(I,U)=\Delta^{B}(U,I)=0$ | normalization |
| (ii) | $\Delta^{B}(DU_2,\,U_1D')=\Delta^{B}(U_2,U_1)$ | outer tori |
| (iii) | $\Delta^{B}(U_2D,\,D^{-1}U_1)=\Delta^{B}(U_2,U_1)$ | compensated cut |
| (iv) | $\Delta^{B}(PU_2,\,U_1P)=P\,\Delta^{B}(U_2,U_1)\,P$ | equivariance |
| (v) | $\Delta^{B}(U_2,U_1)^{\mathsf T}=\Delta^{B}(U_1^{\mathsf T},U_2^{\mathsf T})$ | reversal covariance |
| (vi) | $\Delta^{B}(U_2D,\,U_1)\ne\Delta^{B}(U_2,U_1)$ in general | the only handle |

*Proof.* Each follows from Theorem 2.1: (ii) and (iii) leave every $w_k$
unchanged up to a common unimodular factor per $(i,j)$, or unchanged
outright; (iv) permutes the index triples; (v) transposes the path
labelling. (i) is near-tautological, since $B(I)=I$ makes the two terms of
the definition coincide term by term. $\square$

Item (ii) contains the standing wall $B(\omega U)=B(U)$ and is strictly
stronger: what dies at each outer slot is the whole maximal torus, and by
(iii) the compensated torus at the cut dies too. Item (v) is a
*covariance*, not an evenness: transpose-invariant functionals of
$\Delta^{B}$ are reversal-even, but the antisymmetric part
$A=\tfrac12(\Delta^{B}-(\Delta^{B})^{\mathsf T})$ is reversal-odd and is
not identically zero. On both reference families $A\equiv0$ — $0$ of
$13\,185$ ordered pairs carry a nonzero $A$ — which at $2\times2$ is forced,
every multiple of the matrix
$$
J_-=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}
$$
being symmetric, and which at $3\times3$ is a **contingent property of that
family**. Off the families it is nonzero. Let $R_{k\ell}$ denote the exact
rational rotation in the $(k,\ell)$ plane, that is, the identity outside the
$(k,\ell)$ block and
$$
\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix}
$$
inside it. On the declared witness set
$\{R_{01},R_{12},R_{01}F_3,R_{12}F_3\}$ at $n=3$ — none of whose members
lies in $\mathcal{F}_3$ — one finds $A\ne0$ on $12$ of the $16$ ordered
pairs, with off-diagonal entries $\pm14/625$, and $A\mapsto-A$ under
reversal on all $16$.

Item (vi) — the *uncompensated* cut — is the only surviving handle, and it
is not a group action on the pair. On a declared stride of 24 members of
$\mathcal{F}_2$ it moves the defect on **192 of 576** ordered pairs. This
count returns in §5 and §6, where it is the same measurement read twice,
not two independent ones.

Finally, $\Delta^{B}$ has real entries — immediately from Theorem 2.1 —
so every real-polynomial functional of it is real, and a real number of
modulus one is $\pm1$. Both values occur: over the $9216$ pairs of
$\mathcal{F}_2$, $\operatorname{tr}\Delta^{B}=+1$ on exactly $512$ pairs and
$-1$ on exactly $512$.

### 2.5 The doubly-centred structure and the sharp bounds

$B(U)$ is doubly stochastic for unitary $U$, hence so are $B(U_2U_1)$ and
$B(U_2)B(U_1)$; therefore **all row sums and all column sums of
$\Delta^{B}$ vanish**, and the family lands in the $(n-1)^2$-dimensional
space of doubly-centred matrices. Writing $s_{ij}=(B(U_2)B(U_1))_{ij}$:

**Proposition 2.5 (sharp bounds, by certificate).**
$$
\Delta^{B}_{ij}+s_{ij}=\Bigl|\sum_k w_k\Bigr|^{2},
\qquad
n\,s_{ij}-\bigl(\Delta^{B}_{ij}+s_{ij}\bigr)=\sum_{k<\ell}|w_k-w_\ell|^{2},
$$
*so $-s_{ij}\le\Delta^{B}_{ij}\le(n-1)s_{ij}$.*

Both are exact identities — a modulus square and the Lagrange
sum-of-squares — so the bounds are obtained without any order comparison.
Both certificates hold on all $72\,585$ census entries, as does the
vanishing of all row and column sums.

At $n=2$ the family is one-dimensional: $\Delta^{B}$ is a multiple of the
matrix $J_-$ of §2.4, and its **exact range
over the census is $[-\tfrac12,\tfrac12]$**, read with an exact sign oracle
on $\mathbb{Q}(\sqrt2)$. Both ends are witnessed, and by *different* pairs:
$$
\Delta^{B}(H,H)_{00}=+\tfrac12,\qquad
\Delta^{B}\bigl(H,\ \operatorname{diag}(1,-1)H\bigr)_{00}=-\tfrac12 .
$$

### 2.6 The coherence law, and what it is worth

**Theorem 2.6 (coherence law).** *For any three composable factors,*
$$
\Delta^{B}(U_3U_2,\,U_1)+\Delta^{B}(U_3,U_2)B(U_1)
\;=\;
\Delta^{B}(U_3,\,U_2U_1)+B(U_3)\Delta^{B}(U_2,U_1),
$$
*both sides being $B(U_3U_2U_1)-B(U_3)B(U_2)B(U_1)$.*

*Proof.* Expand each $\Delta^{B}$ by its definition; both sides telescope
to the common form. $\square$

More generally, write $\Delta_n(L_1,\dots,L_n)=B(L_1\cdots L_n)-B(L_1)\cdots B(L_n)$, and for a binary bracketing $T$ define $\Phi(\text{leaf})=0$ and
$$
\Phi(T)=\Delta^{B}\bigl(U(T_L),U(T_R)\bigr)+\Phi(T_L)\,B\bigl(U(T_R)\bigr)
+\Bigl(\textstyle\prod_{L}B\Bigr)\Phi(T_R),
$$
where $\prod_L B$ is the product of $B$ over the *leaves* of $T_L$.

**Theorem 2.7 (tree law).** $\Phi(T)=\Delta_n$ *for every bracketing $T$.*

*Proof.* Induction. With $A=U(T_L)$, $B$-side $=U(T_R)$,
$\Phi(T_L)=B(A)-\prod_L$ and $\Phi(T_R)=B(\text{right})-\prod_R$,
$$
\Phi(T)=\bigl[B(AB)-B(A)B(B)\bigr]+\bigl[B(A)-\textstyle\prod_L\bigr]B(B)
+\textstyle\prod_L\bigl[B(B)-\prod_R\bigr]=B(AB)-\prod_L\prod_R .\ \square
$$

Both are verified as **formal-matrix identities**: independent polynomial
variables for every entry of $B$ of every contiguous sub-product — 24
variables at $d=2$, 54 at $d=3$ — with no property of $B$ assumed. The
bracketing counts at $n=2,\dots,5$ are $1,2,5,14$, the Catalan numbers, and
the identity holds at all of them.

**Honest measurement.** Because the gate assumes nothing about $B$, the law
holds for *any* map. This is made concrete: with $B$ replaced by six
declared substitutes — the identity, the transpose, $M\mapsto M+2M^{\mathsf T}+3I$, doubling, the zero map, and a **constant map that
ignores its argument entirely** — the identity holds in all six cases. The
telescope
$$
\bigl(f(ABC)-f(AB)f(C)\bigr)+\bigl(f(AB)-f(A)f(B)\bigr)f(C)
=\bigl(f(ABC)-f(A)f(BC)\bigr)+f(A)\bigl(f(BC)-f(B)f(C)\bigr)
$$
has both sides equal to $f(ABC)-f(A)f(B)f(C)$ for every $f$. **A law that
survives replacing its subject constrains the subject not at all**: the
coherence law is an identity of associativity. It organizes the family; it
selects nothing.

One consequence is not vacuous. From
$\Delta_3=\Delta^{B}(U_3,U_2U_1)+B(U_3)\Delta^{B}(U_2,U_1)$, a chain whose
every consecutive cut is flat can still be globally non-flat: an exact
witness is exhibited in $\mathcal{F}_2$ (family indices $32,0,32$).
**Flatness is not locally determined.**

### 2.7 The two-sided annihilator

**Theorem 2.8 (annihilator).** *Let*
$$
\mathcal{K}_L=\{U_2:\Delta^{B}(U_2,V)=0\ \text{for every unitary}\ V\},\qquad
\mathcal{K}_R=\{U_1:\Delta^{B}(V,U_1)=0\ \text{for every unitary}\ V\}.
$$
*Then $\mathcal{K}_L$ is exactly the row-monomial unitaries and
$\mathcal{K}_R$ exactly the column-monomial unitaries.*

*Proof.* Sufficiency is Theorem 2.1: if $U_2$ is row-monomial, at most one
$w_k$ is nonzero for each $(i,j)$ and the pairwise sum is empty; dually for
$U_1$. Necessity: suppose row $i$ of $U_2$ has nonzero entries $a,b$ at
columns $k\ne\ell$. Probe with $V=D^{(k)}_m R_{k\ell}$, where $R_{k\ell}$ is
the exact rational rotation of §2.4 in the $(k,\ell)$ plane and $D^{(k)}_m$
carries $i^m$ at position $k$. Then
$$
\Delta^{B}(U_2,V)_{ik}=\tfrac{24}{25}\operatorname{Re}\bigl(i^m\,a\,\overline b\bigr),
$$
and $\operatorname{Re}(z)=\operatorname{Re}(iz)=0$ forces $z=0$; so
$m\in\{0,1\}$ separates every non-monomial row. $\mathcal{K}_R$ follows by
the reversal covariance 2.4(v), whose effect is to transpose the probes.
$\square$

*Scope tag.* This is a hand proof with verified ingredients: the closed
form, the unitarity of the probes (entries in $\mathbb{Q}(i)$ only), and
the two-phase separation are all checked exactly; the quantifier over all
unitaries is carried by the argument. Corroboration: with $2$ probes at
$n=2$ and $6$ at $n=3$, all $64$ non-row-monomial members of
$\mathcal{F}_2$ and all $9$ of $\mathcal{F}_3$ are separated in the left
slot, and likewise in the right slot with the transposed probes — $0$
unseparated in either.

**Corollary.** $B$ restricted to the monomial group $\mathrm{Mon}(n)= \mathbb{T}^n\rtimes S_n$ is a group homomorphism onto $S_n$, with the whole
torus in its kernel.

### 2.8 The flat-spectrum identification

On the Fourier-sandwich family $U_2=D_aF_ND_b$, $U_1=D_cF_ND_e$ one has
$B(U_2)=B(U_1)=J/N$, so $\Delta^{B}=0$ iff $B(F_NEF_N)=J/N$ with
$E=D_bD_c$ the **interleaving** diagonal. Since
$(F_NEF_N)_{jk}=\tfrac1N\sum_m\varepsilon_m\omega^{m(j+k)}$, the entries are
the discrete Fourier transform of the unimodular sequence $\varepsilon$
read at $j+k$.

**Theorem 2.10 (identification).**
$$
\Delta^{B}=0
\;\Longleftrightarrow\;
\bigl|\widehat{\varepsilon}(s)\bigr|=\sqrt N\ \text{for every }s
\;\Longleftrightarrow\;
\varepsilon\ \text{has vanishing periodic autocorrelation at every nonzero lag.}
$$

**Attribution, and it is load-bearing.** The *second* equivalence is the
discrete Wiener–Khinchin theorem together with the *definition* of a CAZAC
(constant-amplitude zero-autocorrelation) sequence, a classical family with
explicit constructions at every $N$ [16]. **It is not proved here.** What
this paper claims is the *first* equivalence: the identification of the
vanishing of $\Delta^{B}$ on the Fourier-sandwich family with that known
condition on the interleaving diagonal. The second is re-verified here only
as an arithmetic check on the computation.

Verified with $\varepsilon_0=1$ fixed: $N=2$ over $\mu_8$ (8 diagonals, 2
flat), $N=3$ over $\mu_6$ (36, 6), $N=4$ over $\mu_8$ (512, 16), $N=5$ over
$\mu_5$ (625, 20) — with three-way agreement at every single diagonal. Two
closed forms follow and are checked exhaustively:
$$
\begin{aligned}
N=2:&\quad U_2=\operatorname{diag}(1,\zeta_8^{s})H\operatorname{diag}(1,\zeta_8^{t}),\
U_1=\operatorname{diag}(1,\zeta_8^{u})H\operatorname{diag}(1,\zeta_8^{v}):\quad
\Delta^{B}=0\iff t+u\equiv\pm2 \ (\mathrm{mod}\ 8);\\
N=3:&\quad U_2=D(a_2)F_3D(b_2),\ U_1=D(a_1)F_3D(b_1):\quad
\Delta^{B}=0\iff b_2+a_1\not\equiv0\ (\mathrm{mod}\ 3),
\end{aligned}
$$
on all $4096$ and all $81$ parameter quadruples respectively, $0$
mismatches. **The vanishing of $\Delta^{B}$ is a phase-alignment condition,
and the alignment condition is flatness of a Fourier spectrum.** The
support criterion of Theorem 2.8 is sufficient and strictly weaker.

---

## 3. The CHSH three-class skeleton

This section fixes the correlation geometry in which the amplitude
structure of $\Delta^{B}$ will be read. Everything in it is assembled from
cited antecedents; the contribution is the exact assembly, two class-level
statements, and the exhibit of §3.5.

### 3.1 Three convex bodies

On the CHSH correlator projection, with
$P(x,y\mid a,b)=\tfrac14(1+xy\,E_{ab})$, $x,y\in\{\pm1\}$, and
$S=E_{00}+E_{01}+E_{10}-E_{11}$, define
$$
\begin{aligned}
\mathcal{L}&=\operatorname{conv}\{E_{ab}=s_at_b:\ s_a,t_b\in\{\pm1\}\},\\
\mathcal{Q}&=\operatorname{conv}\{E_{ab}=\operatorname{Re}(z_a\overline{w_b}):\ z_a,w_b\in U(1)\},\\
\mathcal{N}&=[-1,1]^4 .
\end{aligned}
$$

**Theorem 3.1.** $\mathcal{L}\subsetneq\mathcal{Q}\subsetneq\mathcal{N}$,
*with*
$$
\max|S|\;=\;2,\qquad 2\sqrt2,\qquad 4
$$
*respectively.*

*Proof.* A linear functional attains its maximum over a compact convex set
at an extreme point, and $\max$ over $\operatorname{conv}(S)$ equals $\max$
over $S$; so each body's maximum is the maximum over its generating set.

*(i)* The 16 sign patterns give 8 distinct correlator vectors; over them
$\max S=2$ and $\min S=-2$ on all four CHSH functionals ($64$ exact
rational evaluations), and the bound propagates over the hull by linearity
(checked on $330$ exact rational hull points with weights in
$\tfrac14\mathbb{Z}$). This is Fine's characterization of the local set as
the hull of the deterministic assignments [4].

*(ii)* Four exact polynomial identities over $\mathbb{Q}$:
- **(C0)** the regrouping $S=\operatorname{Re}\bigl(\overline{z_0}(w_0+w_1)\bigr) +\operatorname{Re}\bigl(\overline{z_1}(w_0-w_1)\bigr)$;
- **(C1)** $(cx+sy)^2+(cy-sx)^2=(c^2+s^2)(x^2+y^2)$, whence for $|z|=1$,
  $\operatorname{Re}(\bar z u)^2\le|u|^2$, so $S\le|w_0+w_1|+|w_0-w_1|=:p+q$;
- **(C2)** the parallelogram identity $p^2+q^2=4$ for unit $w$'s;
- **(C3)** $8-(p+q)^2=(p-q)^2+2(4-p^2-q^2)$, which on $p^2+q^2=4$ reads
  $8-(p+q)^2=(p-q)^2\ge0$, i.e. $p+q\le2\sqrt2$ with equality iff $p=q=\sqrt2$.

Attainment is exact in $\mathbb{Q}(\zeta_8)$: $(z_0,z_1,w_0,w_1)= (\zeta_8,\zeta_8^7,1,\zeta_8^2)$ gives correlators
$(\tfrac{\sqrt2}{2},\tfrac{\sqrt2}{2},\tfrac{\sqrt2}{2},-\tfrac{\sqrt2}{2})$
and $S=2\sqrt2$. Corroboration: the exhaustive $\pi/4$ grid, $8^4=4096$
quadruples, exact comparison in $\mathbb{Q}(\sqrt2)$ — no point exceeds
$2\sqrt2$ and the grid maximum is exactly $2\sqrt2$.

*(iii)* $|E_{ab}|\le1$ gives $|S|\le4$ at once; the maximum $4$ is attained
on the cube only at $(+1,+1,+1,-1)$. The 24 no-signalling vertices of the
scenario [8] are enumerated exactly: 16 deterministic behaviours and 8
superquantum ones, all verified normalized, non-negative and no-signalling
on both wings. The 16 deterministic behaviours project to the 8 distinct
local correlator vectors, whose maximum is 2; every superquantum vertex
attains 4 on one of the 8 signed CHSH functionals, and no local vertex
attains 4 on any.

Strictness: $\mathcal{L}\subseteq\mathcal{Q}$ because each of the 16 local
generators is a $U(1)$-Gram generator (verified), and $2<2\sqrt2$ exactly;
$\mathcal{Q}\subseteq\mathcal{N}$ because every Gram correlator lies in
$[-1,1]$, and $2\sqrt2<4$ exactly. $\square$

### 3.2 Planar sufficiency

By Tsirelson's theorem [7] — cited, not proved here — the quantum
correlator set at this scenario is
$\mathcal{Q}^{\mathrm{qm}}=\{E_{ab}=\langle u_a,v_b\rangle: u_a,v_b\ \text{unit vectors in a real Hilbert space}\}$, of unbounded dimension.
That the *planar* configurations already generate it is likewise standard
(it is normally quoted as part of Tsirelson's theorem); the contribution
here is the exact assembly of its three ingredients, each verified
symbolically in $\mathbb{R}^n$ for $n=2,\dots,6$ and holding for every $n$
by the same expansion:

1. For any $\lambda\in\mathbb{R}^4$ and fixed $v_0,v_1$,
   $\sum_{ab}\lambda_{ab}\langle u_a,v_b\rangle =\langle u_0,\lambda_{00}v_0+\lambda_{01}v_1\rangle +\langle u_1,\lambda_{10}v_0+\lambda_{11}v_1\rangle$ — an identity with
   *symbolic* $\lambda$. Lagrange's identity
   $\|u\|^2\|r\|^2-\langle u,r\rangle^2=\sum_{i<j}(u_ir_j-u_jr_i)^2$ gives
   $\langle u,r\rangle\le\|r\|$ with maximizer $r/\|r\|$. Hence **some**
   optimizer $u_a$ lies in $\operatorname{span}\{v_0,v_1\}$, of dimension at
   most 2. (Not *all* optimizers: for degenerate $\lambda$ with $r_a=0$
   every unit vector is optimal; planar *attainment* is all the
   support-function argument needs.)
2. $\|xv_0+yv_1\|^2=x^2\|v_0\|^2+y^2\|v_1\|^2+2xy\langle v_0,v_1\rangle$:
   on unit $v$'s the optimum depends on $(v_0,v_1)$ only through
   $t=\langle v_0,v_1\rangle$.
3. Every $t\in[-1,1]$ is realized by unit vectors in $\mathbb{R}^2$: the
   rational parametrization $t=(1-m^2)/(1+m^2)$, $s=2m/(1+m^2)$ is exact on
   $1830$ declared rational slopes ($t^2+s^2=1$ exactly, $t\in[-1,1]$), and
   surjectivity onto $[-1,1]$ is continuity.

Hence the support function of $\mathcal{Q}^{\mathrm{qm}}$ equals that of the
planar family for every $\lambda$; both sets are compact convex, so
$\mathcal{Q}=\mathcal{Q}^{\mathrm{qm}}$.

An independent corroboration presses the ceiling with a **declared
deterministic stride**: from the full enumeration of rational unit vectors
(246 in $\mathbb{R}^3$ at entries $|k|\le9$; 808 in $\mathbb{R}^4$ at
$|k|\le5$) take every 9th, respectively every 31st, keeping 26 in each
case, and sweep all $26^4=456\,976$ four-vector configurations. No
configuration exceeds $2\sqrt2$; the maxima reached are $14/5=2.8$ in
$\mathbb{R}^3$ and $19/7\approx2.714$ in $\mathbb{R}^4$, against the ceiling
$2\sqrt2\approx2.8284$.

**Scope tag, engraved with the theorem.** This is the CHSH $(2,2,2)$
correlator projection, after convexification. It says nothing about full
behaviours including marginals, nothing about scenarios with more settings,
parties or outcomes, and it does not claim that the un-convexified
$U(1)$-Gram *generating class* is the quantum set — §3.3 proves that class
is not even convex.

### 3.3 The generating class is not convex, and the sharp exclusion

The point $E=(1,0,0,0)$ is the mean of four deterministic vertices, hence
lies in $\mathcal{L}\subseteq\mathcal{Q}$. It is **not** a $U(1)$-Gram
generator: $E_{00}=1$ forces $w_0=z_0$ (equality in (C1)); $E_{01}=0$ forces
$w_1=\mu\,i\,z_0$; $E_{10}=0$ forces $z_1=\varepsilon\,i\,z_0$; and then
$E_{11}=\varepsilon\mu\in\{\pm1\}$, never $0$. All four sign branches are
checked in $\mathbb{Q}(\zeta_8)$. So the generating class is not convex,
and the convexification in Theorem 3.1 is load-bearing rather than
cosmetic.

At the class level the exclusion is sharper.

**Proposition 3.3.** *Every $\{\pm1\}$-valued $U(1)$-Gram point satisfies*
$$
E_{00}E_{01}E_{10}E_{11}=+1. \tag{$*$}
$$

*Proof.* By (C1) with $|z|=|w|=1$, $\operatorname{Re}(z\bar w)= \varepsilon\in\{\pm1\}$ forces $\operatorname{Im}(z\bar w)=0$, hence
$z=\varepsilon w$. Reading $z_a=E_{ab}w_b$ at $b=0$ and $b=1$ gives
$w_1=E_{a0}E_{a1}w_0$ for both $a$, hence $E_{00}E_{01}=E_{10}E_{11}$,
hence $(*)$. $\square$

Of the 16 sign vectors, exactly the 8 with product $+1$ are the
$\{\pm1\}$-factorizable ones — verified exhaustively. The superquantum
correlators $(1,1,1,-1)$ have product $-1$, so **the superquantum vertex
admits no $U(1)$-Gram representation at all** — not merely a point outside
a convex body.

$(*)$ is the **four-cycle holonomy of the edge-phase pattern**: with
$g_{ab}=z_a\overline{w_b}$,
$$
g_{00}\,g_{10}^{-1}\,g_{11}\,g_{01}^{-1}
=(z_0\bar z_0)(z_1\bar z_1)(w_0\bar w_0)(w_1\bar w_1)=1
$$
identically — every factorized edge phase is a coboundary. The invariant
excluding the superquantum vertex from the Gram class is exactly a
four-cycle holonomy, and the same invariant returns as the organizing
object of §5 and §6.

### 3.4 Constructive no-signalling

$P(x,y\mid a,b)=\tfrac14(1+xy\,E_{ab})$ is normalized, has both marginals
$\equiv\tfrac12$, and reproduces $E$ — three polynomial identities in $E$,
verified symbolically — so no-signalling holds for *every* correlator
vector; non-negativity is the only inequality, and $|E_{ab}|\le1$ is
verified with the exact sign oracle on all $4096$ grid points.

### 3.5 The anti-correlation exhibit

Two named models, with opposite pairings of holonomy and CHSH value.

**The singlet amplitude model.** $\psi_{xy}(a,b)=(z_a-xy\,w_b)/(2\sqrt2)$
with $z_a=e^{ia}$, $w_b=e^{ib}$. The Born identity
$$
P(x,y\mid a,b)=|\psi_{xy}(a,b)|^2=\tfrac14\bigl(1-xy\cos(a-b)\bigr)
$$
follows from the polynomial identity
$|z-\varepsilon w|^2=|z|^2+\varepsilon^2|w|^2-2\varepsilon\operatorname{Re}(z\bar w)$,
verified symbolically and instantiated at two declared algebraic angle
families: the $\pi/4$ family in $\mathbb{Q}(\zeta_8)$ (all 8 angles, 256
exact identities) and the $\pi/8$ family in $\mathbb{Q}(\zeta_{16})$ (all 16
angles, 1024). At the settings $(a_0,a_1)=(0,\pi/2)$,
$(b_0,b_1)=(\pi/4,-\pi/4)$ the correlators are $E_{ab}=-\cos(a-b)$ and
$$
S=-2\sqrt2 \quad\text{exactly},\qquad |S|=2\sqrt2=\max_{\mathcal{Q}}|S| .
$$
The sign belongs to the functional, not the model: $w_b\mapsto-w_b$ stays in
the class and carries the instance to $+2\sqrt2$ (verified). The four-cycle
holonomy of the factorized edge phase is **identically 1**, on all 4096
quadruples of the $\pi/4$ family and all 4096 of the $\pi/8$ family (the
latter with $a_0=0$ fixed; the holonomy is invariant under $z_a\mapsto \lambda z_a$ and $w_b\mapsto\mu w_b$ separately). These are two different
sweeps over two different families and are cited separately.

**The superquantum edge-phase pattern** $(\gamma_{00},\gamma_{01}, \gamma_{10},\gamma_{11})=(1,1,1,-1)$ gives a valid no-signalling table with
uniform marginals, correlators $(1,1,1,-1)$, $S=4$ exactly, and four-cycle
holonomy $-1$: not a coboundary.

| model | four-cycle holonomy | $|$CHSH$|$ |
|---|---|---|
| singlet Gram model (Tsirelson-saturating) | **trivial** ($=1$) | $2\sqrt2$ |
| superquantum edge-phase pattern | **nontrivial** ($=-1$) | $4$ |

**This is an exhibit, not a theorem about all models.** Two named models
pair holonomy triviality with quantumness in *opposite* senses; the exhibit
establishes no replacement correlation between class and CHSH value. It is
the concrete form of the caution of [6] that a cohomological class is a
sufficient witness of contextuality, not an equivalence — a caution that
returns quantitatively in §8.

---

## 4. Records

### 4.1 The record, defined first

A **record** of a family of alternatives at a cut is a variable whose values
label mutually exclusive sectors, correlated with those alternatives, and
available under the declared future dynamics. At finite dimension, with
configuration space $C$, propagators $U_1$ (initial $\to$ cut) and $U_2$
(cut $\to$ final), and the declared laws
$$
\Gamma_{10}=B(U_1),\qquad \Gamma_{21}=B(U_2),\qquad \Gamma_{20}=B(U_2U_1),
$$
a **record structure** is a partition of $C$ into sectors $\{C_r\}$,
equivalently an orthogonal resolution $P_r=\sum_{k\in C_r}|k\rangle\langle k|$, and the three clauses become three conditions **on supports**:

- **(H-orth)** the sectors are mutually exclusive — definitional;
- **(H-corr) perfect correlation.** For every initial configuration $j$,
  the *live* alternatives at the cut — the $k$ with $(U_1)_{kj}\ne0$ — lie
  in pairwise **distinct** sectors;
- **(H-avail) availability.** For every later configuration $i$, all cut
  configurations $k$ with $(U_2)_{ik}\ne0$ lie in **one** sector.

**Neither hypothesis mentions $\Delta^{B}$, $D$, $d_{\mathrm{div}}$ or
divisibility.** The theorem below is therefore falsifiable rather than
definitional: a stable record with a surviving residual on its own algebra,
under record-preserving dynamics, would refute it. Every census, sweep and
model in this section evaluates the hypotheses *before* any defect is
computed, and no such counterexample is found.

### 4.2 The theorem

**Theorem 4.2 (records kill the defect).** *Let a record structure at the
cut satisfy (H-corr) and (H-avail). Then every summand of the closed form
vanishes individually, hence*
$$
\Delta^{B}(U_2,U_1)=0,\qquad D=0\ \text{on the cut algebra with the
canonical divisor}\ \Gamma_{21}=B(U_2).
$$

*Proof.* Fix $i,j$ and $k<\ell$. If the summand
$w_k\overline{w_\ell}=(U_2)_{ik}(U_1)_{kj}\overline{(U_2)_{i\ell}(U_1)_{\ell j}}$
is nonzero then all four factors are nonzero. From $(U_2)_{ik}\ne0$ and
$(U_2)_{i\ell}\ne0$ and **(H-avail)**, $k$ and $\ell$ lie in the same
sector. From $(U_1)_{kj}\ne0$ and $(U_1)_{\ell j}\ne0$ and **(H-corr)**,
$k$ and $\ell$ lie in distinct sectors unless $k=\ell$. But $k<\ell$.
Contradiction; the summand is zero. Summing, $\Delta^{B}=0$. $\square$

The proof is a **support argument**: it uses no property of the amplitudes.
This is what makes the conclusion robust in a way that phase cancellation is
not (§4.7).

*Worked exhibit, with nothing decohered.* On four configurations
$(\text{branch},\text{record})$, take $U_1=\mathrm{CNOT}\circ(H\otimes I)$
— which writes the branch into the record — and $U_2=H\otimes I$, which acts
on the branch alone; the record structure is the second bit,
$\{\,\{0,2\},\{1,3\}\,\}$. Both hypotheses hold; **all 96 cross terms are
individually zero**; $\Delta^{B}=0$; and the composite shadow's first column
is $(\tfrac14,\tfrac14,\tfrac14,\tfrac14)$. No decoherence is applied
anywhere. Removing the CNOT — the only change — breaks (H-corr) and the
defect returns with $\Delta^{B}_{00}=\tfrac12$.

**Theorem 4.3 (the reading route).** *If the record is physically read at
the cut — the channel is $U_2\circ\mathcal{D}\circ U_1$ with the pinching
$\mathcal{D}(\rho)=\sum_r P_r\rho P_r$ onto the record sectors — and the
sectors satisfy (H-corr), then for **any** later dynamics whatever*
$$
\mathrm{shadow}\bigl(U_2\circ\mathcal{D}\circ U_1\bigr)=B(U_2)B(U_1),
\qquad\text{so } D=0 .
$$

*Proof.* Under (H-corr) each sector contains at most one live alternative
of column $j$, so $P_rU_1|j\rangle\langle j|U_1^\dagger P_r$ is either zero
or a single diagonal term: the sector pinching already equals the full
configuration pinching on that state, giving
$\mathcal{D}(U_1|j\rangle\langle j|U_1^\dagger)=\sum_k|(U_1)_{kj}|^2\, |k\rangle\langle k|$. Conjugating by $U_2$ and reading the diagonal gives
$\sum_k|(U_2)_{ik}|^2|(U_1)_{kj}|^2=(B(U_2)B(U_1))_{ij}$. $\square$

The two routes are genuinely different: Theorem 4.2 needs **no decoherence
at all** — the record keeps the branches apart by itself — while Theorem 4.3
needs no hypothesis on the future. **The reading route still needs
(H-corr):** reading a *coarse*, non-separating record leaves the
intra-sector coherences alive. Both are verified: the fine reading equals
$B(U_2)B(U_1)$ and is a genuine stochastic matrix (rational, non-negative,
unit column sums); a genuinely coarse but *separating* record — two sectors
of size two, not singletons — also divides; and the one-sector reading
returns the *unread* shadow exactly.

**Theorem 4.4 (channel form).** *Let $\mathcal{H}$ be finite-dimensional,
$\{\rho_j\}$ declared initial states, $\Phi_1,\Phi_2$ CPTP maps, $\{P_r\}$
an orthogonal resolution at the cut, $\{F_i\}$ a POVM at the final time.
Put $\Gamma_{10}(r\mid j)=\operatorname{Tr}[P_r\Phi_1(\rho_j)]$,
$\Gamma_{20}(i\mid j)=\operatorname{Tr}[F_i\Phi_2\Phi_1(\rho_j)]$ and
$\sigma_{r\mid j}=P_r\Phi_1(\rho_j)P_r/\Gamma_{10}(r\mid j)$. Assume*

- **(R1) no recoherence:** $\operatorname{Tr}[F_i\Phi_2(X)]= \operatorname{Tr}[F_i\Phi_2(\mathcal{D}(X))]$ for every $X=\Phi_1(\rho_j)$;
- **(R2) sufficiency:** there are states $\sigma_r$ with
  $\operatorname{Tr}[F_i\Phi_2(\sigma_{r\mid j})]= \operatorname{Tr}[F_i\Phi_2(\sigma_r)]=:\Gamma_{21}(i\mid r)$ for every
  $j$ with $\Gamma_{10}(r\mid j)>0$.

*Then $\Gamma_{20}=\Gamma_{21}\Gamma_{10}$ exactly.*

*Proof.* $\Gamma_{20}(i\mid j)=\operatorname{Tr}[F_i\Phi_2\Phi_1(\rho_j)] \overset{(R1)}{=}\operatorname{Tr}[F_i\Phi_2(\sum_rP_r\Phi_1(\rho_j)P_r)] =\sum_r\Gamma_{10}(r\mid j)\operatorname{Tr}[F_i\Phi_2(\sigma_{r\mid j})] \overset{(R2)}{=}\sum_r\Gamma_{21}(i\mid r)\Gamma_{10}(r\mid j)$. $\square$

(R1) holds when the reading is applied physically, and when $\Phi_2$'s Kraus
operators are sector-graded and the $F_i$ commute with the $P_r$ — which is
(H-avail) at the support level. (R2) holds when the sectors are rank one —
(H-corr)'s strongest form. Theorem 4.2 does **not** need (R2), because under
(H-avail) the later configuration already determines the record value. Both
are the same one-line mechanism: *interference between record sectors is
unobservable, and inside a sector there is at most one live alternative.*
**Declared limit:** Theorem 4.4 is proved here and exercised only through
its instances; no separate CPTP census is run.

**Theorem 4.5 (approximate correlation).** *Under (R1), with the declared
divisor $\widehat\Gamma_{21}(i\mid r)=\operatorname{Tr}[F_i\Phi_2(\sigma_r)]$,*
$$
\sum_i\bigl|D(i\mid j)\bigr|\;\le\;\sum_r\Gamma_{10}(r\mid j)\,
\bigl\|\sigma_{r\mid j}-\sigma_r\bigr\|_1 .
$$

*Proof.* $D(i\mid j)=\sum_r\Gamma_{10}(r\mid j) \operatorname{Tr}[F_i\Phi_2(\sigma_{r\mid j}-\sigma_r)]$; for a POVM,
$\sum_i|\operatorname{Tr}[F_iX]|\le\sum_i\operatorname{Tr}[F_i|X|]=\|X\|_1$,
and $\Phi_2$ is trace-norm contractive. $\square$

On a declared exact rational family at six deviation values and **both**
columns, with the right-hand side recomputed from $\sigma_{r\mid j}$,
$\sigma_r$ and $\Gamma_{10}$ at every point, the bound is not merely
satisfied but **tight: equality at all 12 points**. The tightness is
disclosed at its true strength: 7 of the 12 are degenerate (both sides
exactly zero — one column carries no unrecorded residue at any deviation,
and the zero-deviation point is the exact-record point) and the remaining
**5** have both sides equal and strictly positive.

### 4.3 The decision procedure

Theorem 4.2 is a sufficient condition *at a given* record structure. The
question that matters downstream — *does **any** record structure work?* —
is not a search problem at all.

**Theorem 4.6 (decision criterion).** *Let $M(U_2)$ be the transitive
closure of the co-merge relation "$k\sim\ell$ iff some later configuration
receives amplitude from both", and call $k,\ell$ **co-live** for $U_1$ if
some initial configuration makes both live. Then*
$$
\exists\pi\ \bigl[(\text{H-corr})(U_1,\pi)\wedge(\text{H-avail})(U_2,\pi)\bigr]
\iff
M(U_2)\ \text{separates every co-live pair of}\ U_1 .
$$

*Proof.* (H-avail)$(U_2,\pi)$ says every row support of $U_2$ lies in one
$\pi$-sector, i.e. $\pi$ is **coarser** than $M(U_2)$; and $M(U_2)$ is
itself admissible, so it is the *finest* admissible partition. (H-corr) is
inherited by every **refinement** of a partition satisfying it. Hence if any
admissible $\pi$ satisfies (H-corr), so does $M(U_2)$; and conversely
$M(U_2)$ is admissible. $\square$

One union-find pass over the row supports and one duplicate-label scan over
the column supports: **$O(n^2)$, with no enumeration of partitions.** The
criterion is checked against every search performed here: over all
$512\times512=262\,144$ support pairs at $n=3$, against the exhaustive
5-partition table, there are **0 disagreements**.

### 4.4 The exhaustive support sweep, and sharpness

At $n=3$ the hypotheses are checked exhaustively over *all* $2^9=512$
support patterns for $U_1$, all 512 for $U_2$, and all 5 set partitions:
**146 536 admissible triples, 0 cross-term violations.** Because both
hypotheses are monotone under shrinking a support, this covers **every**
pair of $3\times3$ matrices with any amplitudes whatever: at $n=3$ no
counterexample exists at all.

*Scope of these sweeps, stated once and carried.* They range over abstract
$0/1$ patterns. Call a pattern **admissible** if it has no empty row or
column and any two rows — and any two columns — have supports that are
disjoint or overlap in at least two places; this is a necessary condition
for carrying a unitary, since an overlap of exactly one would make an inner
product a single nonzero term. Exactly **25 of the 512** patterns are
admissible at $n=3$, and **exact witnesses are exhibited for all 25**: the
6 permutation patterns (permutation matrices), the full pattern ($F_3$), the
9 patterns with a singleton row and column plus a full $2\times2$ block
($1\oplus H$ in the appropriate positions), and the 9 patterns with exactly
one zero entry, realized by the exact rational orthogonal matrix
$$
\begin{pmatrix}
12/25 & -9/25 & 4/5\\
16/25 & -12/25 & -3/5\\
3/5 & 4/5 & 0
\end{pmatrix}
$$
and its row/column permutations, whose orthogonality is verified exactly.
On the other 487 patterns no unistochastic law exists, so every
canonical-divisor statement is *vacuous* there.

Call a support pair a **$Q$-pair** if every cross-term slot is
support-forced empty, so $\Delta^{B}=0$ for *any* amplitudes on it.

**Sharpness, both sides reported.** Over all $262\,144$ abstract support
pairs there are **94 746** $Q$-pairs, of which **5 490 admit no record
structure at all**: on abstract patterns the hypotheses are strictly
sufficient and the criterion is *not* sharp. Restrict to the 25 realizable
supports and the picture inverts: of the 625 ordered pairs, **318 are
$Q$-pairs and all 318 admit a record structure — 0 exceptions**. At $n=3$
the abstract non-sharpness is entirely an artefact of patterns that carry no
unitary. Neither number is claimed beyond $n=3$.

**Proposition 4.7 (the two monomial endpoints).** *Over all 512 supports at
$n=3$, with no exceptions,*
$$
(\text{H-avail})\ \text{at the finest record}\iff U_2\ \text{row-monomial},
\qquad
(\text{H-corr})\ \text{at the trivial record}\iff U_1\ \text{column-monomial},
$$
*with the other hypothesis automatic in each case.* The two structural
sufficiency conditions of §2.2 are therefore the two endpoints of one
record-indexed family, and the **intermediate** structures are strictly
stronger than both.

**Corollary 4.8 (multi-cut).** *Let $U_1,\dots,U_{m+1}$ be the legs of a
chain and let each cut $t$ carry a record structure $\pi_t$ satisfying
(H-corr) for the composite prefix $U_t\cdots U_1$ and (H-avail) for the next
leg $U_{t+1}$. Then*
$$
B(U_{m+1}\cdots U_1)=B(U_{m+1})\cdots B(U_1),
$$
*i.e. the residual vanishes at every cut simultaneously and the chain is
Chapman–Kolmogorov.*

*Proof.* Apply Theorem 4.2 at the last cut to the pair
$(U_{m+1},U_m\cdots U_1)$, then recurse on the shorter chain. $\square$

Verified on exact chains with a **growing** record: three legs on 8
configurations with records at both cuts, and four legs on 16 configurations
with records at three cuts, both Chapman–Kolmogorov exactly.

*A dimension-four census over all 15 partitions.* With 8 declared unitary
operators on 4 configurations and all 15 partitions — 960 (partition,
$U_2$, $U_1$) triples — **259 satisfy both hypotheses and all 259 have a
vanishing defect**; of the 64 ordered pairs, 49 have a vanishing defect and
the decision criterion finds a record structure in **all 49**.

### 4.5 The composite two-measurement model

The same theorem is now exhibited on a model of a bipartite two-measurement
experiment, built here from scratch and reused in §8 and §9.

**Definition 4.9 (the composite model).** The configuration space is
$C=\{(q_A,q_B,p_A,p_B)\}$ with $q_X\in\{0,1\}$ and $p_X\in\{r,+,-\}$, so
$|C|=36$, indexed by $i=((q_A\cdot2+q_B)\cdot3+p_A)\cdot3+p_B$, with initial
configuration $j_0=0$, i.e. $(0,0,r,r)$. The propagators are

- **preparation** $U_{\mathrm{prep}}=V\otimes I_9$, with $V$ real orthogonal
  carrying $e_0$ to the singlet vector $(0,\tfrac1{\sqrt2},-\tfrac1{\sqrt2},0)$
  on $(q_Aq_B)=(00,01,10,11)$;
- **local measurement** $U_X(\theta)=\sum_s\Pi^\theta_s\otimes \mathrm{Sh}^{n(s)}$, acting on $(q_X,p_X)$ and trivially on the other pair,
  where $\Pi^\theta_\pm$ are the rank-one projectors onto
  $(\cos\tfrac\theta2,\sin\tfrac\theta2)$ and
  $(-\sin\tfrac\theta2,\cos\tfrac\theta2)$, $\mathrm{Sh}$ is the 3-cycle
  $r\to+\to-\to r$, and $n(+)=1$, $n(-)=2$.

Two **frames** order the same two local events: $F_1=(\mathrm{prep},A,B)$ and
$F_2=(\mathrm{prep},B,A)$, on one configuration space. The declared
intermediate time is $t'=2$ and the target $t=3$. Six setting pairs are
declared: $(0^\circ,45^\circ)$, $(0^\circ,135^\circ)$,
$(90^\circ,45^\circ)$, $(90^\circ,135^\circ)$, $(0^\circ,0^\circ)$,
$(45^\circ,45^\circ)$.

Every entry lies in the totally real quartic field
$\mathbb{Q}(\cos\pi/8)=\mathbb{Q}[x]/(8x^4-8x^2+1)$, so all arithmetic is
exact. Verified: $U_{\mathrm{prep}}$ is exactly orthogonal, with $j_0$
column $\tfrac1{\sqrt2}$ at index 9 and $-\tfrac1{\sqrt2}$ at index 18; all
8 local operators are exactly orthogonal; the two local operators **commute
at all 9 setting pairs**; and the outcome law is exactly
$$
P(\alpha,\beta)=\tfrac14\bigl(1-\alpha\beta\cos(a-b)\bigr),
$$
with both marginals $\tfrac12$ — 60 exact identities across the twelve
(setting, frame) cells.

**The division-event biconditional.** Declare, *before any defect of this
model is computed and depending only on the configuration indexing*, the
family of **16 record structures** that read a subset of the four
configuration coordinates, from the one-sector trivial structure to the
36-sector finest one. Then, at all twelve cells:

| setting pair | $F_1$ | winning structures | $F_2$ | winning structures |
|---|---|---|---|---|
| $(0^\circ,45^\circ)$ | divides | $\{q_A\},\{p_A\},\{q_A,p_A\}$ | divides | $\{q_A,q_B,p_B\}$, finest |
| $(0^\circ,135^\circ)$ | divides | $\{q_A\},\{p_A\},\{q_A,p_A\}$ | divides | $\{q_A,q_B,p_B\}$, finest |
| $(90^\circ,45^\circ)$ | indivisible | — | indivisible | — |
| $(90^\circ,135^\circ)$ | indivisible | — | indivisible | — |
| $(0^\circ,0^\circ)$ | divides | 14 of the 16 | divides | 14 of the 16 |
| $(45^\circ,45^\circ)$ | indivisible | — | indivisible | — |

The indivisible cells differ from $\Gamma(3\!\leftarrow\!2)\Gamma(2\!\leftarrow\!0)$
in **288 entries** each; the divisible ones in 0.

**The biconditional is decided over the full class, not measured over 16.**
Theorem 4.6 answers the existential question over *every* set partition of
the 36 configurations — a class of size $B(36)\approx10^{31}$, which no
search could enumerate — by testing the single canonical partition
$M(U_2)$. The answer agrees with divisibility at **12 of 12 cells**, and
agrees with the declared-family search everywhere: where a declared
structure wins, the criterion says yes; where none wins, **no record
structure exists at all**. The scope of the statement is therefore *decided
over the full class of record structures on this model*, not *measured over
a declared family*.

**The mechanism, exact.** In $F_1$ at $a=0^\circ$ Alice's measurement is a
configuration *permutation*, so the two branches leave the cut in
**different pointer-$A$ sectors**, and Bob — who never touches pointer $A$ —
cannot bring them back to one configuration: both hypotheses hold and the
law divides. At $a=45^\circ$ or $90^\circ$ the pointer still records
Alice's *outcome*, but two live alternatives share a pointer sector:
(H-corr) fails, the cross terms survive, and the law does not divide. In
$F_2$ at $a=0^\circ$ the divisibility comes from the *finest* record
instead, because the second-leg operator is monomial — the same theorem at
its other endpoint (Proposition 4.7).

**A legitimate division event is a record event**, on this model, in both
frames, at every setting pair. This is a statement about *this model*; the
general converse is false (§4.7).

Finally, the exact ranks of $\Gamma(2\!\leftarrow\!0)$ over the twelve cells
are $27$ or $18$ — **never 36**. This will matter in §9.

### 4.6 The eraser control

Same record, same initial configurations, same first leg
$U_1=\mathrm{CNOT}\circ(H\otimes I)$. **Only the later operation changes:**
$$
\text{preserving: } U_2=H\otimes I,
\qquad
\text{erasing: } U_2'=(H\otimes I)\circ\mathrm{CNOT}.
$$
Exactly: (H-corr) still holds — the record is still *made*; only its
availability changes — while **(H-avail) fails**. The erased composite law
is the **identity**: coherent erasure recovers the initial configuration
exactly. The residual returns maximally, with every entry $0$ or
$\pm\tfrac12$. And no record structure exists at the erasing cut under *any*
partition (the criterion says so).

**The floor, computed rather than asserted.** $\Gamma_{10}$ has column 0 =
column 2 $=(\tfrac12,0,0,\tfrac12)$ and column 1 = column 3
$=(0,\tfrac12,\tfrac12,0)$. Writing $p=K\Gamma_{10}e_0=K\Gamma_{10}e_2$ and
$q=K\Gamma_{10}e_1=K\Gamma_{10}e_3$, both probability vectors, against
$\Gamma_{20}=I$ the entrywise $\ell^1$ objective is
$$
\|\Gamma_{20}-K\Gamma_{10}\|=8-2(p_0+p_2)-2(q_1+q_3)\;\ge\;4,
$$
since $p_0+p_2\le1$ and $q_1+q_3\le1$. The objective is **affine** in $K$,
so its minimum over the column-stochastic polytope is attained at a vertex
and the 256 deterministic matrices exhaust the search: the minimum is
**exactly 4**. Under the **induced** 1-norm (maximum over columns) the floor
is **1**. Both are computed; the norm is named at each.

*An eraser inside the composite model.* Taking the second leg to be the
exact reverse of the first, the composite law becomes the identity, the law
differs in 36 entries at a cut that divided, **all 16 declared record
structures are destroyed**, and by the criterion **no record structure
exists there at all**. The boundary of every claim in this section is
therefore not a disclaimer but a measured location.

### 4.7 The converse, scoped

The implication ladder, with the divisor named at every link:
$$
\text{records}
\;\Rightarrow\;\text{medium decoherence at the cut}
\;\Rightarrow\;\Delta^{B}=0\;(=D\ \text{at the canonical divisor})
\;\Rightarrow\;d_{\mathrm{div}}=0 .
$$
At the canonical divisor $\Gamma_{21}=B(U_2)$ the middle equality is an
identity — $D=\Gamma_{20}-B(U_2)B(U_1)=\Delta^{B}$ — so the ladder has
**three strict links, not four**. Two of the three reverse implications are
refuted here; one is explicitly **not tested**.

- **$d_{\mathrm{div}}=0\;\not\Rightarrow$ a record.** At the rotation cut of
  Theorem 2.3, the *existential* divisibility holds — witnessed by the
  non-canonical divisor $K=S(-175/527)$ — while of the two partitions of a
  two-configuration space the finest fails (H-avail), because $U_2$ is not
  monomial, and the trivial fails (H-corr), because both alternatives are
  live. The criterion agrees. Note that with the *canonical* divisor
  $D=\Delta^{B}=-4032/15625\ne0$ here; the refuted link is the existential
  one.

- **$\Delta^{B}=0\;\not\Rightarrow$ medium decoherence, and this is the
  converse's first genuine failure.** The pair
  $(U_2,U_1)=(H,\operatorname{diag}(1,i)H)$ has $\Delta^{B}=0$ while the
  branch overlaps are nonzero, and it carries **no record structure at
  either partition** — exhaustive at $n=2$, with no third partition to hide
  in. Its vanishing is *phase alignment*, and it is **unstable**: of 7
  declared diagonal phase insertions, **6 break it**, whereas the same
  insertions leave the record-killed vanishing at exactly zero — **0 of 7**.
  Stability under phase kicks is the operational signature of a support
  kill, and it is the sharp difference between the two ways of killing the
  defect.

- **Not tested here:** *medium decoherence $\Rightarrow$ records* in this
  paper's sense — a configuration-space partition satisfying (H-corr) and
  (H-avail). For a different and coarser notion of record — later-time
  projections in *any* basis, existentially quantified over operators and
  required only to be perfectly correlated with the history branches — the
  corresponding biconditional for a pure initial state is a known theorem of
  decoherent histories [14,15]. It is **cited, never re-derived, and never
  claimed here.** The two record notions are different objects: theirs are
  projections at a later time in any basis; this paper's are partitions of
  the configuration space at the cut, constrained by the *supports* of the
  declared propagators — a strictly narrower object. Every reverse
  implication refuted above is refuted for *this* notion; [14]'s
  biconditional stands untouched, and the witnesses above all live where
  medium decoherence *fails*.

---

## 5. The gauge of a compositional law

Barandes' entrywise gauge is declared for a single propagator. This section
determines what survives when propagators are asked to compose.

### 5.1 On a single arrow the gauge annihilates everything

Call the transformation $U_{ij}\mapsto e^{i\theta_{ij}}U_{ij}$, with
$\theta$ independent per **ordered pair**, the *entrywise gauge* [3, p.12,
eqs. 29–30]. Call a phase matrix $\Theta$ of **boundary form** if
$\Theta_{ij}=d_i\overline{e_j}$ for unimodular $d,e$.

**Proposition 5.1.** *For any $U$ the entrywise-gauge orbit is exactly
$\{V:|V_{ij}|=|U_{ij}|\ \forall i,j\}$. Hence **every** entrywise-gauge
invariant is a function of $B(U)$ alone — moduli and support, no phase.*

*Proof.* One inclusion is immediate. For the other, given $V$ with matching
moduli set $\Theta_{ij}=V_{ij}/U_{ij}$ on the support — unimodular, since
the moduli agree — and $1$ off it. $\square$

Constructively verified: of the ordered pairs of $\mathcal{F}_2$, **1152**
share their moduli, and the connecting unimodular matrix is built in all
1152; the family has 3 Born-shadow classes, all 3 with more than one member,
whose members differ only in phase.

**Triple products are the wrong invariant here.** The Bargmann-type triple
product $u_{ij}u_{jk}u_{ki}$ is an invariant of the *one-index ray gauge*
$g_{ij}\mapsto\overline{\lambda_i}\lambda_jg_{ij}$ on a single space, where
the phases telescope around **any** cycle, odd ones included; that is the
setting of [13]. It is **not** an invariant of the matrix gauge, for two
separate reasons, both verified on all 9 full-support members of
$\mathcal{F}_3$: it is moved by a declared unimodular $\Theta$ (9 of 9), and
it is moved by a declared boundary gauge with
$d_0d_1d_2\ne1$ (9 of 9) — **odd cycles do not close in a bipartite support
graph, where rows and columns carry independent phases.** Under the ray
gauge it *is* invariant, 9 of 9: the correct typing of the object.

The even four-cycle survives. The Haagerup-type invariant
$$
H_{ii';jj'}(U)\;=\;U_{ij}\,U_{i'j'}\,\overline{U_{ij'}}\,\overline{U_{i'j}}
$$
has boundary-gauge factors
$(d_ie_j)(d_{i'}e_{j'})(d_ie_{j'})^{-1}(d_{i'}e_j)^{-1}=1$; verified over 9
matrices $\times$ 9 index quadruples.

### 5.2 The composition-compatibility theorem

Objects are configuration spaces; an arrow $U:V_a\to V_b$ is a matrix. A
gauge family $\{\Theta^{(b,a)}\}$ is **composition-compatible** if for every
composable pair
$$
\bigl(\Theta^{(2,1)}\!\circ U_2\bigr)\bigl(\Theta^{(1,0)}\!\circ U_1\bigr)
=\Theta^{(2,0)}\!\circ(U_2U_1),
$$
i.e. the transformed factors compose to the transformed composite: the gauge
is an endofunctor fixing objects.

**Theorem 5.4.** *Over unitary arrows in dimension $\ge2$, a gauge family is
composition-compatible **iff***
$$
\Theta^{(b,a)}_{ij}=d^{(b)}_i\,\overline{d^{(a)}_j}
$$
*for object-indexed unimodular functions $d^{(a)}$. The
composition-compatible subgroup of the entrywise gauge is **exactly** the
boundary gauge.*

*Proof.* $(\Leftarrow)$ $\Theta^{(b,a)}\!\circ U=D_bUD_a^{-1}$, and
$(D_2U_2D_1^{-1})(D_1U_1D_0^{-1})=D_2U_2U_1D_0^{-1}$.

$(\Rightarrow)$ Entrywise the requirement reads, for each $(i,j)$,
$$
\sum_k\Theta^{(2,1)}_{ik}\Theta^{(1,0)}_{kj}\,w_k
=\Theta^{(2,0)}_{ij}\sum_kw_k,\qquad w_k=(U_2)_{ik}(U_1)_{kj}.
$$
Take $U_2=VD_c$ and $U_1=D_{c'}V'$ with $V,V'$ Fourier-sandwich carriers
(all entries nonzero) and $c,c'$ free unimodular diagonals. Then
$w_k=r_ku_k$ with $r_k\ne0$ fixed and $u$ an arbitrary unimodular vector.
Subtracting the requirement at $u$ and at $u$ with slot $k$ negated gives
$2\bigl(\Theta^{(2,1)}_{ik}\Theta^{(1,0)}_{kj}-\Theta^{(2,0)}_{ij}\bigr)r_k=0$,
hence the pointwise functional equation
$$
\Theta^{(2,1)}_{ik}\,\Theta^{(1,0)}_{kj}=\Theta^{(2,0)}_{ij}
\qquad\text{for all }i,j,k. \tag{$\star$}
$$
Fix $k_0$ and set $a_i:=\Theta^{(2,1)}_{ik_0}$, $b_j:=\Theta^{(1,0)}_{k_0j}$.
Then $\Theta^{(2,0)}_{ij}=a_ib_j$, and $(\star)$ forces
$\Theta^{(1,0)}_{kj}/b_j$ to be independent of $j$, say $c_k$; so
$\Theta^{(1,0)}_{kj}=c_kb_j$ and $\Theta^{(2,1)}_{ik}=a_i\overline{c_k}$.
Taking $d^{(2)}=a$, $d^{(1)}=c$, $d^{(0)}=\bar b$ gives the boundary form.
$\square$

Both halves are verified **exhaustively over declared finite phase groups**.
At $n=2$ over $\mu_4$: of $65\,536$ ordered $\Theta$-pairs, **1024 satisfy
$(\star)$, and exactly the same 1024 admit an object-indexed family** — 65
536 agreements. At $n=3$ over $\mu_2$: **256 of 262 144**, again exactly
matching, 262 144 agreements. The coupling is visible in the surplus: of the
$64^2=4096$ pairs at $n=2$ whose two factors are **separately** of boundary
form, only 1024 are compatible; the surplus **3072** is precisely the set
whose middle phase functions disagree — an **uncompensated cut**. Separate
boundary form is necessary and not sufficient; the compensated cut is
exactly the coupling condition.

**The load-bearing quantifier, named and measured.** The theorem quantifies
over the admissible *class* of composable unitary arrows, not over one
realized pair, and the difference is measured. On a **totally
path-degenerate** pair — one live path per endpoint pair, e.g. a monomial
second leg — the requirement is an identity: with the declared pair $(H,X)$,
**all $65\,536$** ordered $\Theta$-pairs are compatible, and this route
licenses **nothing at all**. A single **non-degenerate** pair, by contrast,
already goes the whole way: with $(H,H)$ exactly **1024** are compatible —
the boundary answer, the same 1024 as $(\star)$, with 65 536 agreements.
Where the first route is vacuous, the second route carries the verdict.

### 5.3 The unitarity-preservation theorem

**Theorem 5.5.** *$\Theta\circ U$ is unitary for **every** unitary $U$ iff
every Haagerup invariant of $\Theta$ equals 1 iff $\Theta$ is of boundary
form.*

*Proof.* $(\Leftarrow)$ $\Theta\circ U=DUE^\dagger$ is unitary.

$(\Rightarrow)$ For $i\ne j$, orthogonality of rows $i,j$ of $\Theta\circ U$
reads $\sum_k\lambda_kv_k=0$ whenever $\sum_kv_k=0$, with
$\lambda_k=\Theta_{ik}\overline{\Theta_{jk}}$ and
$v_k=U_{ik}\overline{U_{jk}}$. The unitary realizing the needed $v$ must be
**placed at the rows the constraint is about**: for the given $(i,j)$ and
the given $(k,l)$, let $U$ carry the two columns $\{k,l\}$ into the two
**rows** $\{i,j\}$,
$$
U_{ik}=U_{jl}=\cos\theta,\qquad U_{il}=-\sin\theta,\qquad U_{jk}=\sin\theta,
$$
matching the remaining columns to the remaining rows by any fixed bijection
(entries 1). Then $U$ is unitary and
$$
v=U_{ik}\overline{U_{jk}}\,e_k+U_{il}\overline{U_{jl}}\,e_l
=\cos\theta\sin\theta\,(e_k-e_l),
$$
with every other $v_m=0$; it is nonzero for $\theta$ not a multiple of
$\pi/2$, and $\sum_mv_m=0$, so the hypothesis applies and forces
$\lambda_k=\lambda_l$, i.e. $H_{ij;kl}(\Theta)=1$. The construction exists
for **every** $(i,j)$ and **every** $(k,l)$, so every Haagerup quadruple of
$\Theta$ is trivial. For the last step: $\Theta$ is a gauge matrix, so every
entry is unimodular *by definition of the gauge* — $\Theta$ has full
support, its bipartite graph is complete and therefore connected, and by
Theorem 5.6 its cycle lattice is generated by the four-cycles. Trivial
Haagerup on every four-cycle is then precisely the boundary form, by the
switching reconstruction of Theorem 5.6. $\square$

**The placement is load-bearing, and the gap it closes is measured.** A
rotation in the $(k,l)$ *coordinate* plane moves columns $\{k,l\}$ back into
rows $\{k,l\}$ and so reaches only the diagonal quadruples $(i,j)=(k,l)$. At
$n=3$ over $\mu_2$ that literal family leaves **64** phase matrices
standing; the placed family leaves **32** — exactly the Haagerup-trivial
count and exactly the boundary-form count. The measured gap is 32.

Verified: at $n=2$ over $\mu_8$, **512 of 4096** phase matrices preserve
unitarity on the declared family, exactly 512 are Haagerup-trivial, and
exactly 512 are of boundary form; at $n=3$ over $\mu_2$, **32 of 512** in
all three counts, with 0 disagreements.

**This is the precise content of "a partial fixing of the gauge freedom"
[3, p.19].** Fixing a unitary representative does not exhaust the entrywise
freedom; the residual stabilizer is *exactly* the boundary group. The
phrase is Barandes'; the exact residual is this paper's.

### 5.4 The verdict, and its scope

Two further checks corroborate. The full entrywise gauge **moves the
composite's Born shadow**. Take the phase matrix
$$
\Theta=\begin{pmatrix}1&1\\1&-1\end{pmatrix}
$$
on the pair $(H,H)$: then
$B((\Theta\circ H)(\Theta\circ H))\ne B(H\cdot H)$; since $B(U_2U_1)$ *is*
the two-step transition law, a
transformation that moves it is not a gauge of a composable system. The same
$\Theta$ destroys unitarity, which is Barandes' own observation. And the
boundary group contains the three named sub-gauges — projective scalar,
compensated cut, same-space rephasing — while the **uncompensated** cut is
verified *not* to be a gauge: it moves the defect on 192 of 576 declared
stride pairs (§2.4). That is this paper's one measurement of the
uncompensated cut; §6.4 identifies its own no-descent predicate with it
rather than counting again.

> **The reduction is derived, not chosen.** The composition-compatible
> subgroup and the unitarity-preserving subgroup of the entrywise gauge both
> equal the boundary gauge. Neither route is a new postulate: composability
> makes the pair the subject, and double stochasticity of the Born shadow
> requires unitary arrows. **The load-bearing quantifier is named:** the
> first route asks the gauge to be compatible with the *admissible class* of
> composable dynamics, and on a totally path-degenerate support that
> requirement is an identity and the route licenses nothing; there the
> second route, whose quantifier ranges over all unitary $U$ and is
> untouched by path degeneracy, carries the verdict alone. The two routes
> are independent and are not interchangeable everywhere.

**Scope, engraved.** What is reduced is the gauge of a *composable, unitary*
system. For a single arrow considered in isolation, with neither composition
nor unitarity asked of it, Proposition 5.1 stands and **no phase invariant
exists at all**. The two facts are consistent, and both are stated.

### 5.5 The single-arrow orbit theorem

For a matrix $U$ let $G(U)$ be the **bipartite support graph**: vertices
$\mathrm{Rows}\sqcup\mathrm{Cols}$, an edge $(i,j)$ carrying $U_{ij}$ for
each nonzero entry. The boundary gauge acts as **vertex switching** on
$G(U)$. Traversing an edge rows$\to$cols contributes $U_{ij}$ and
cols$\to$rows contributes $\overline{U_{ij}}$; around any cycle each vertex
is entered once and left once, so its phase cancels and the **cycle holonomy
is switching-invariant**. All cycles of a bipartite graph are even, and the
elementary four-cycles are exactly the Haagerup invariants.

**Antecedent, and it is not this paper's theorem.** The gain-graph /
switching classification — phases on a cycle basis classify edge-phase
assignments up to vertex switching, componentwise, with cycle rank
$\mu=|E|-|V|+c$ — is Zaslavsky's [11,12]. What is this paper's is the exact
adaptation to the declared matrix families, to support changes, and (in §6)
to the composable-pair graph.

**Theorem 5.6 (orbit classification).** *Two matrices with the same support
and the same moduli are boundary-gauge equivalent **iff** their cycle-basis
holonomies agree.*

*Proof (the construction).* Fix a spanning forest of the support graph, set
the switching to 1 at each component root and propagate it along tree edges
— forced, one choice per vertex, since $V_{ij}=d_i\overline{d_j}U_{ij}$
determines the far endpoint from the near one. Every non-tree edge then
agrees iff its fundamental-cycle holonomy agrees. $\square$

Verified by **building** the switching in every positive case and checking
it entrywise: **4608 of 9216** ordered pairs of $\mathcal{F}_2$ and
**567 of 3969** of $\mathcal{F}_3$ are equivalent, with **0 disagreements**
against the four-cycle test.

Two structural facts close the section. The moduli determine the support and
the boundary gauge can neither create nor destroy an entry, so **support
strata never mix**: 0 of the $9216+3969$ ordered pairs are equivalent across
different supports. And on a monomial support the cycle set is **empty** —
$\mu=0$ for all 86 monomial members of the two families. **A vanished
amplitude does not have a trivial phase; it has no phase.** The invariant is
not 1; it does not exist. This bookkeeping is carried through §6 and §7,
where it becomes load-bearing.

---

## 6. The loop signature and its incompleteness

### 6.1 Why a phase-retaining invariant is needed at all

The Born shadow cannot see a projective class. This is not a remark about
one example; it is two theorems.

**Theorem 6.1 (the multiplier cancels).** *Let $\tilde\rho:G\to U(N)$ be any
projective representation with multiplier $\omega$, and put
$\beta_B:=B\circ\tilde\rho$. Then $\beta_B$ is independent of the lift, and*
$$
\Delta^{B}\bigl(\tilde\rho(g),\tilde\rho(h)\bigr)
=B\bigl(\omega(g,h)\,\tilde\rho(gh)\bigr)-B(\tilde\rho(g))B(\tilde\rho(h))
=\beta_B(gh)-\beta_B(g)\beta_B(h).
$$
*The multiplier does not appear.*

*Proof.* $B(\omega U)=B(U)$ for unimodular $\omega$; substitute. $\square$

The whole defect family of a projective representation is thus the deviation
of $\beta_B$ from being a homomorphism, and $\beta_B$ is a function of the
$PU(N)$-valued map alone. **This does not by itself close the question**:
the class $[\omega]$ is a *lift-independent* invariant of the projective map,
so "absent from the formula" and "invisible to every functional" are
different statements. Were $B$ injective on $PU(N)$, the theorem would hold
verbatim and a functional would exist. What closes it is the collapse.

**Theorem 6.2 (the collapse).** *Let $X_N$ be the shift and $Z_N$ the clock
on $\mathbb{C}^N$, and take the pair $(X_N,Z_N^{\,k})$ for $k=0,\dots,N-1$.
Then $B(Z_N^{\,k})=I$ for every $k$, so $\beta_B(a,b)=B(X^aZ^{kb})=P^a$ with
$P$ the shift permutation, **independent of $k$**; and the whole defect
family is identically zero.*

Verified at $N=2,\dots,6$: for every $N$ and every $k$, all $N^2$ words
$U^aV^b$ and all $N^4$ ordered word pairs — $12\,200$ exact defect
computations in total across the five dimensions and all classes — are
identically zero, and **the $N$ classes share exactly one Born shadow** (the
distinct-shadow count is 1 at every $N$). At $N=6$ the six values
$k=0,\dots,5$ give **six distinct classes of four distinct orders**
$1,2,3,6$, the trivial one among them, carried by realizations with
literally identical Born data.

**A functional cannot separate arguments it is not given.** Theorem 6.1
removes the multiplier from the formula; Theorem 6.2 shows the family cannot
separate the classes: any functional whatsoever, of any shape, takes the same
value on all of them. Neither alone suffices. Hence a phase-retaining
invariant, if one is to exist, must be an invariant of the projective map
that is **not a functional of its Born shadow**.

### 6.2 The relation-loop scalar

For a projective family $\rho$ with lifts $\tilde\rho$, the relation loop
retains
$$
\tilde\rho(g)\,\tilde\rho(h)\,\tilde\rho(g)^{-1}\tilde\rho(h)^{-1}
=\beta(g,h)\cdot I,
$$
the antisymmetrization of the multiplier and the complete invariant of the
class in $H^2(\mathbb{Z}^2,U(1))$, which for $\mathbb{Z}^2$ with trivial
action is determined by that alternating bicharacter.

**Proposition 6.3.** *On the Weyl families, $\beta=\zeta_N^{-k}$ separates
all $N$ classes at every $N=2,\dots,6$, with
$\operatorname{ord}\beta=N/\gcd(N,k)$; $\beta$ is independent of the lift
(scalars cancel in a group commutator) and invariant under
configuration-basis rephasing (the commutator conjugates and a scalar is
central). Hence $\beta$ is **not a functional of $B\circ\rho$**: the Born
shadow is identical across all $N$ classes while $\beta$ takes $N$ distinct
values.*

Verified: $\beta$ separates 2, 3, 4, 5, 6 classes at $N=2,\dots,6$; the
orders at $N=6$ are $\{1,2,3,6\}$; and $\beta$ is unchanged by every
declared rescaling of the two lifts and by a declared basis rephasing —
222 of 222 checks at $N=6$. By the finite Stone–von Neumann theorem [10] —
cited, not proved here — an irreducible realization at a primitive $q$-th
root multiplier has dimension exactly $q$, which is a structural consequence
the Born shadow cannot state.

**The claim is non-factorization, not a refinement ordering, and the
difference matters.** $\beta$ is *not* finer than $B\circ\rho$:
$$
\beta(N=4,k=2)=\beta(N=2,k=1)=-1,
$$
the same value, while their Born shadows differ (a $4\times4$ doubly
stochastic matrix against a $2\times2$ one). So $\beta$ does not separate
everything the Born shadow separates. **The two are incomparable
invariants.** What is supplied is a phase-retaining invariant of the
projective map that the Born shadow cannot determine — not one that refines
it.

Consistency with §5: $\beta$ is **not** an entrywise-gauge invariant — the
entrywise gauge does not even map a group element to a group element — so
its invariance is a statement about the *reduced* gauge, which is exactly
what §5 licensed.

### 6.3 The pair graph and the cut-coherence tensor

**Theorem 6.7 (pair-orbit theorem).** *The declared gauge on a composable
pair — outer boundary, compensated cut, projective scalar — acts **exactly
as vertex switching** on the tripartite path graph*
$$
\mathsf{G}(U_2,U_1):\quad
\text{vertices } R\sqcup K\sqcup C,\quad
\text{an edge }(i,k)\ \text{valued }(U_2)_{ik}\ \text{for each nonzero entry
of } U_2,\quad
\text{an edge }(k,j)\ \text{valued }(U_1)_{kj}.
$$
*$\mathsf{G}$ is bipartite with parts $K$ and $R\sqcup C$ — every edge has
exactly one endpoint in $K$ — so all its cycles are even. The switching at an
$R$-vertex is the outer output rephasing, at a $C$-vertex the outer input
rephasing, and **at a $K$-vertex it is exactly the compensated cut**:
$\overline{d_k}$ on $U_2$ and $d_k$ on $U_1$. Hence, at fixed moduli, a
complete set of invariants of the pair is a cycle basis of $\mathsf{G}$, of
size $\mu(\mathsf{G})=|E|-|V|+c$.*

*Proof.* The three declared moves are exactly the three vertex classes'
switchings, by inspection of the edge values; cycle holonomies are
switching-invariant by the argument of §5.5; and Theorem 5.6's construction,
applied to $\mathsf{G}$, reconstructs the switching from agreeing
cycle-basis holonomies. $\square$

**The shared boundary phase frame is the $K$-vertex switching.** It is
required: the gauge orbits of $U_2$ and $U_1$ *separately* do not determine
the orbit of $U_2U_1$, because $U_2\mapsto U_2D$ is a boundary gauge on
$U_2$ alone and leaves its isolated orbit data unchanged while moving the
composite. Since $B(U_2D)=B(U_2)$, one has
$$
\Delta^{B}(U_2D,U_1)-\Delta^{B}(U_2,U_1)=B(U_2DU_1)-B(U_2U_1),
$$
and "$U_2$ and $U_2D$ lie in the same boundary orbit" is *identically* true.
**The no-descent predicate and the uncompensated-cut predicate of §5.4 are
therefore the same predicate**, and the count is 192 of 576 read twice, not
two independent measurements. No independent corroboration is claimed.

Define the **cut-coherence tensor**
$$
w^{ij}_k=(U_2)_{ik}(U_1)_{kj},
\qquad
\mathcal{C}^{ij}_{k\ell}=w^{ij}_k\,\overline{w^{ij}_\ell}.
$$

**Proposition 6.8.** *On 64 declared stride pairs:* $\mathcal{C}$ is
invariant under the compensated cut (the $w$'s themselves are: 256 checks);
outer boundary rephasings cancel ($w_k\mapsto d_ie_jw_k$, so
$\mathcal{C}\mapsto|d_ie_j|^2\mathcal{C}$); projective scalars of both
factors cancel; the diagonal is the classical path weight
$\mathcal{C}^{ij}_{kk}=B(U_2)_{ik}B(U_1)_{kj}$; $\mathcal{C}^{ij}=w(w)^\dagger$
is Hermitian with every $2\times2$ minor identically zero (rank one, with a
non-negative diagonal, and no order comparison used); and the **readout**
$$
\Delta^{B}_{ij}=2\sum_{k<\ell}\operatorname{Re}\mathcal{C}^{ij}_{k\ell}
$$
holds — all 64 of 64 in each case. The readout is a **restatement of
Theorem 2.1, not a new theorem.**

$\mathcal{C}$ is blind to the projective class exactly where that class
lives: every Weyl pair has **at most one live path per endpoint pair** (20
classes at $N=2,\dots,6$), so the tensor cannot see the multiplier. That is
what forces the relation-loop layer to be part of the signature at all.

**What $\mathcal{C}$ sees, exactly.** $\arg\mathcal{C}^{ij}_{k\ell}= \arg w^{ij}_k-\arg w^{ij}_\ell$ is the holonomy of the **seam four-cycle**
$i\!-\!k\!-\!j\!-\!\ell\!-\!i$ in $\mathsf{G}$. So the signature decomposes:
the factor cycle holonomies are the cycles of the pure-$U_2$ and pure-$U_1$
subgraphs; $\mathcal{C}$ is the seam four-cycles. The **declared signature**
therefore contains the four-cycle sublattice $L_4$ of the cycle lattice
$Z(\mathsf{G})$, and one has the chain
$$
L_4\ \subseteq\ L_{\mathrm{declared}}\ \subseteq\ Z(\mathsf{G}).
$$
Whether either inclusion is strict is the question of §6.5. **Measured: at
the declared scope it makes no difference** — re-running the entire sweep of
§6.5 with the two *full* factor cycle lattices adjoined to the seam
four-cycles returns the same failure counts, $0$, $0$ and $7$ at
$n=2,3,4$. The gap below is not an artefact of reading the declared datum as
four-cycles only.

### 6.4 Completeness at full path support

**Theorem 6.9.** *If every path amplitude $w^{ij}_k$ is nonzero, then
$\mathcal{C}$ is a **complete** invariant of the pair up to the declared
gauge, and a fortiori determines the composite's boundary orbit.*

*Proof.* $\mathcal{C}^{ij}=w^{ij}(w^{ij})^\dagger$ determines $w^{ij}$ up to
one phase $\varphi_{ij}$. Suppose $\mathcal{C}(U_2',U_1')=\mathcal{C}(U_2,U_1)$.
The diagonal forces $|w'|=|w|$ entrywise; the off-diagonal forces
$w'_k/w_k$ independent of $k$, $=\varphi_{ij}$. Writing
$a_{ik}=(U_2')_{ik}/(U_2)_{ik}$ and $b_{kj}=(U_1')_{kj}/(U_1)_{kj}$ we get
$a_{ik}b_{kj}=\varphi_{ij}$ for all $k$ — **the same functional equation as
$(\star)$** — hence $a_{ik}=\alpha_i/c_k$ and $b_{kj}=c_k\beta_j$.

*The moduli step, and it is unitarity that supplies it.* The diagonal alone
gives only $|a_{ik}||b_{kj}|=1$, which does not make the three diagonals
unimodular: it leaves a free positive rescaling, and a positive rescaling is
not a gauge. Write the diagonal identity as
$B(U_2')_{ik}B(U_1')_{kj}=B(U_2)_{ik}B(U_1)_{kj}$ for all $i,j,k$; at full
path support every factor is positive, so
$B(U_2')_{ik}/B(U_2)_{ik}=r_k$ is independent of $i$. Both $U_2$ and $U_2'$
are unitary, so both Born shadows are **doubly stochastic** (§2.5), and
summing the $k$-th column gives $1=r_k\cdot1$, i.e. $r_k=1$. Hence
$|a_{ik}|=|b_{kj}|=1$, $|c_k|$ is constant, and absorbing that constant into
$\alpha$ and $\beta$ makes the three diagonals unimodular. So
$(U_2',U_1')=(D_\alpha U_2D_c^{-1},\,D_cU_1D_\beta)$: outer boundary plus
compensated cut, exactly the declared gauge. $\square$

*Scope tag.* This is a hand proof with verified ingredients: the quantifier
over pairs is carried by the functional equation and the moduli step by
double stochasticity. The lattice reading is the same statement — at full
support $\mathsf{G}$ contains the complete bipartite structure and
$L_4=Z(\mathsf{G})$ — and it is verified directly.

### 6.5 The exhaustive support-class sweep

A support pattern carries a unitary only if it satisfies the necessary
condition of §4.4 (no empty row or column; any two rows, and any two
columns, disjoint or overlapping in at least two places). That condition is
the **declared scope**, and it is a *superset* of the realizable patterns, so
a clean sweep on it is a clean sweep on them. Relabelling $R$ and $C$ are
graph isomorphisms of $\mathsf{G}$, so $U_2$'s support is reduced modulo
row-and-column permutations and $U_1$'s modulo column permutations; the
reduction is exhaustive.

| $n$ | admissible patterns | $\mathsf{G}$-classes | max $\mu$ | four-cycle failures |
|---|---|---|---|---|
| 2 | 3 | $2\times2=4$ | 3 | **0** |
| 3 | 25 | $4\times8=32$ | 10 | **0** |
| 4 | 783 | $16\times79=1264$ | 21 | **7** |

At $n=2$ and $n=3$ the four-cycles generate. **At $n=4$ seven
$\mathsf{G}$-classes have a four-cycle sublattice of rank exactly $\mu-1$**
— the deficit is 1 in every one of them.

**The superset is measured, not merely disclosed.** Birkhoff–von Neumann
sharpens the condition: $B(U)$ is doubly stochastic with exactly the same
support, so every entry of a realizable pattern must lie on a permutation
contained in it — *total support*. At $n=4$ that test proves **36 of the 783**
admissible patterns non-realizable. **All 7 failing classes have total
support on both legs**, so not one of them is a superset artefact.

**A lattice gap is not yet an invariant of unitaries. The $\varphi$-criterion
makes it one.** The only non-gauge diagonal move on a composable pair is the
uncompensated cut $U_2\mapsto U_2D$. It preserves unitarity, support and
moduli for *every* unitary pair with the given support; it fixes every $L_4$
holonomy; and it multiplies the holonomy of a cycle $z$ by
$\prod_kd_k^{\varphi(z)_k}$, where
$$
\varphi(z)_k=\sum_i z_{e_2(i,k)}
$$
sums the $U_2$-edge coefficients of $z$ at the intermediate vertex $k$. So
the gap is **realized — by an actual unitary pair, and for every unitary pair
with that support — iff $\varphi(Z(\mathsf{G}))\not\subseteq\varphi(L_4)$.**
It is: in **7 of 7** failing classes, with witness $\varphi$-images
$$
[0,0,1,-1],\ [-1,1,1,-1],\ [1,-1,1,-1],\ [0,0,1,-1],\ [1,-1,0,0],\
[0,0,1,-1],\ [0,0,1,-1].
$$
The forward direction is therefore established at **every** failing class of
the declared scope, not witnessed at one of them.

### 6.6 The composite-level witness, and the completion

§6.5 settles the **pair**. Whether the signature determines the
**composite's** gauge orbit is a strictly stronger question, and does not
follow: two pairs may differ and still have gauge-equivalent composites.
That question is answered negatively, at one class, in exact unitary
arithmetic.

**The witness.** Write, on four configurations,
$$
U_2:\ \text{rows }01\to\text{cols }23\ \text{by }A,\quad
\text{rows }23\to\text{cols }01\ \text{by }B;
\qquad
U_1:\ \text{rows }02\to\text{cols }23,\quad \text{rows }13\to\text{cols }01,
$$
with the $2\times2$ blocks drawn from $\{H\operatorname{diag}(1,\zeta_8^t)\} \cup\{I,X\}$. The witness triple is
$$
U_2=\mathrm{emb}(H,H),\qquad
U_2'=\mathrm{emb}\bigl(H,\ H\operatorname{diag}(1,\zeta_8)\bigr),\qquad
U_1=\mathrm{emb}(H,H).
$$
Exactly, and all verified:

- all three are unitary and **neither factor is monomial**;
- **every endpoint pair has exactly one live path** — total path degeneracy
  *without* monomial factors, so the annihilator theorem 2.8 does not cover
  it;
- $U_2$ and $U_2'$ lie in the **same** boundary orbit (they have identical
  moduli, and $U_2'=U_2\operatorname{diag}(1,\zeta_8,1,1)$);
- the two pairs have the **same** cut-coherence tensor, block by block,
  entry by entry — $\mathcal{C}$ is blind because there is one live path per
  endpoint pair;
- the relation-loop sector is **empty** here — checked, not assumed: $\beta$
  exists only when the group commutator is a scalar multiple of the
  identity, and for both pairs $U_2U_1U_2^\dagger U_1^\dagger$ is computed
  exactly and is **not** scalar, so no relation-loop phase is defined for
  either;
- the composites have the **same moduli**, $B(U_2U_1)=B(U_2'U_1)$, so the
  Born shadow cannot see it either;
- **both pairs are defect-flat**: one live path per endpoint pair kills every
  cross term, so the entire $\Delta^{B}$-family is silent;
- **but the composites lie in different gauge orbits.** Both absolute values
  are computed, not only their ratio:
  $$
  H_{02;02}(U_2U_1)=\tfrac1{16},\qquad
  H_{02;02}(U_2'U_1)=-\tfrac{\zeta_8^{3}}{16},
  $$
  a ratio of $-\zeta_8^{3}=\zeta_8^{7}$, a primitive eighth root, and no
  switching exists between them.

> **Theorem 6.11 (main theorem; two levels, kept apart).**
>
> **(i) For the pair.** The signature (factor cycle holonomies +
> relation-loop phases + $\mathcal{C}$) determines the pair $(U_2,U_1)$ up to
> the declared gauge **exactly when $L_4=Z(\mathsf{G})$.** $(\Leftarrow)$ is
> the switching reconstruction (Theorems 5.6, 6.7), holding unconditionally
> at full support (Theorem 6.9) and at every admissible support class for
> $n=2,3$. $(\Rightarrow)$ is the $\varphi$-criterion: where
> $L_4\ne Z(\mathsf{G})$ the gap is realized by an uncompensated cut, for
> *every* unitary pair with that support — established at **all seven**
> failing $n=4$ classes, not witnessed at one.
>
> **(ii) For the composite.** Whether the signature determines the
> *composite's* gauge orbit is **strictly stronger**, and does not follow
> from (i). It is **refuted at one class** by the exact unitary witness
> above, whose two pairs share the entire signature and the entire
> $\Delta^{B}$-family while their composites lie in different boundary
> orbits.

**The missing datum, named.** $\mathcal{C}$ is the $(i,j)$-block-diagonal
restriction of the full **path-amplitude Gram form**
$$
\mathcal{G}_{(ijk),(i'j'k')}=w^{ij}_k\,\overline{w^{i'j'}_{k'}},
$$
a rank-one positive semidefinite form on the live paths. What $\mathcal{C}$
discards is exactly $\mathcal{G}$'s **cross-block** entries — the coherences
between different endpoint pairs. Those are not individually gauge-invariant
(they carry $d_ie_j\overline{d_{i'}}\overline{e_{j'}}$), and the
**lowest-degree** gauge-invariant combination of them is the quadruple
$$
\mathcal{K}^{(ii';jj')}_{k\ell;k'\ell'}
=w^{ij}_k\,\overline{w^{i'j}_\ell}\;w^{i'j'}_{k'}\,\overline{w^{ij'}_{\ell'}},
$$
whose gauge factors telescope around the eight-cycle
$i\!-\!k\!-\!j\!-\!\ell\!-\!i'\!-\!k'\!-\!j'\!-\!\ell'\!-\!i$ of $\mathsf{G}$.

**No minimality is claimed.** Each failing class has rank deficit *exactly*
1, so **one further cycle per class would already suffice**. What
$\mathcal{K}$ is, is a **sufficient and uniformly definable** choice — one
formula, for every support, with no case analysis — not a minimal one. It is
not claimed that no smaller completion exists.

Four properties, each verified:

1. **Precise referent.** $\mathcal{K}$ is defined from the path amplitudes
   $w^{ij}_k$ of the composable pair and nothing else, and is exhibited in
   exact cyclotomic arithmetic at every index tuple used. It is boundary-
   and compensated-cut invariant at every declared switching moving all
   three vertex classes simultaneously.
2. **Necessity.** Something beyond the declared signature *is* needed, and
   that is measured, not assumed: the seven classes have rank deficit 1,
   realized by an actual uncompensated cut at every one of them by the
   $\varphi$-criterion, and the witness above exhibits an exact unitary pair
   whose composite the declared signature cannot separate.
3. **No smuggling.** Summing $\mathcal{K}$ over $k,\ell,k',\ell'$ gives
   $$
   \sum \mathcal{K}^{(ii';jj')}_{k\ell;k'\ell'}
   =H_{ii';jj'}(U_2U_1),
   $$
   the composite's own four-cycle invariant — which is exactly why adjoining
   $\mathcal{K}$ can restore what the composite carries, and exactly where a
   reader should suspect the answer of having been put in by hand. It was
   not: $\mathcal{K}$ is built from **factor** path amplitudes alone and
   never reads the composite, so the identity is something the definition
   *implies*. It is a derivation target, not an input, and it is verified as
   one.
4. **Discriminator.** $\mathcal{K}$ separates the witness that $\mathcal{C}$
   could not, and adjoining its eight-cycles closes **all seven** $n=4$
   gaps: $L_4+\mathcal{K}=Z(\mathsf{G})$ on every $\mathsf{G}$-class at
   $n=2,3,4$ — 4, 32 and 1264 classes, 0 remaining gaps.

**A declared $n=5$ sample.** Exhaustive enumeration is infeasible at $n=5$,
so a sample is declared: the 120 permutations of five elements in
lexicographic order, **stride 3** (40 of them), every union of 2, 3 and 4 of
those, filtered by the same necessary condition and reduced modulo the same
relabellings — **653 patterns, 2100 $\mathsf{G}$-classes, max $\mu=26$**. On
it $L_4=Z(\mathsf{G})$ **fails 101 times and $\mathcal{K}$ closes every one
of them**. So the $n=4$ phenomenon is not an $n=4$ accident at the sampled
scope; **neither the exhaustive $n=5$ statement nor the general-$n$
statement is settled here.** The natural conjecture, untested, is that
$L_4+\mathcal{K}=Z(\mathsf{G})$ for every admissible $\mathsf{G}$.

---

## 7. Record descent and its limit

### 7.1 The two hypotheses, and what each one buys

The record structure of §4 is a label map $k\mapsto\mathrm{part}(k)$ whose
fibres are the sectors, and its two hypotheses are pure support conditions:
(H-avail) says each row support of $U_2$ lies in one sector; (H-corr) says
$k\mapsto\mathrm{part}(k)$ is injective on each column support of $U_1$.

**Theorem 7.1.** *(H-avail) **alone** implies $\mathcal{C}$ is
block-diagonal by record sector: $\mathcal{C}^{ij}_{k\ell}=0$ whenever
$r(k)\ne r(\ell)$.*

*Proof.* If $r(k)\ne r(\ell)$ then for every $i$ at most one of $(U_2)_{ik}$,
$(U_2)_{i\ell}$ is nonzero, so $w^{ij}_k\overline{w^{ij}_\ell}=0$. $\square$

**Theorem 7.2.** *(H-avail) **and** (H-corr) imply $\mathcal{C}$ is fully
diagonal, hence $\Delta^{B}=0$ by the readout identity.*

*Proof.* Block-diagonality by Theorem 7.1; within a sector, (H-corr) leaves
at most one live $k$ per column $j$, so the surviving off-diagonal entries
are empty too. $\square$

This recovers Theorem 4.2 as a corollary and **separates the two
hypotheses' roles**: (H-avail) buys the *block structure*, (H-corr) buys the
*collapse inside a block*. Verified over 8 declared dimension-four operators
$\times$ 15 partitions $\times$ 8 second factors: **432 triples satisfy
(H-avail) and all 432 give a block-diagonal tensor**, 0 violations;
**259 satisfy both and the tensor is fully diagonal in all 259**, with 0
counterexamples to the vanishing of the defect there.

### 7.2 Block-diagonality is not phase triviality

Within an **unresolved** sector the off-diagonal entries survive:
block-diagonalization is a statement about *cross-sector* coherence only.
At the declared coarse structure $[0,0,1,1]$ with $U_2=U_1=I\otimes H$,
(H-avail) holds and (H-corr) fails; $\mathcal{C}$ is block-diagonal — **0
cross-sector entries** — yet carries **16 nonzero off-diagonal entries
inside the blocks**, and $\Delta^{B}\ne0$ there. The theorem's content is
block structure, not phase triviality.

### 7.3 The eraser control

The same record-writing first leg $U_1=\mathrm{CNOT}\circ(H\otimes I)$; only
the later operation changes. With the preserving leg $H\otimes I$,
$\mathcal{C}$ is block-diagonal *and* fully diagonal: 0 cross-sector and 0
off-diagonal entries. With the eraser $(H\otimes I)\circ\mathrm{CNOT}$,
**16 nonzero cross-sector entries return** — coherent recombination puts
back exactly what the record removed — the residual returns with entries
$0,\pm\tfrac12$, and the cause is exactly Theorem 7.1's hypothesis:
(H-avail) fails while (H-corr) still holds.

### 7.4 A measured negative, and the limit

*On the declared unitary families, a fully diagonal tensor always carries a
record.* Of the 64 ordered pairs of the dimension-four operator set, **49
have a fully diagonal tensor and the decision criterion finds a record
structure in all 49**. This agrees with the sharpness result of §4.4 (318 of
318 on realizable supports at $n=3$) and disagrees with the abstract support
count (5490 of 94 746). **Unitarity is doing the work.**

**Disclosure: how much of that negative is structure, and how much is one
degeneracy repeated.** A second census of 10 000 block-structured pairs also
returns a fully diagonal tensor and a record in all 10 000 — but **all
10 000 carry at most one live path per endpoint pair by the block pattern
alone** (4096 of them exactly one), so their diagonality is forced before any
record question is asked. That census is one degeneracy repeated 10 000
times, not 10 000 independent instances, and it is not evidence of anything
on its own. **The informative instances are the 49 of 64**, where the
diagonality is not built in. The numbers stand as measured; what changes is
what they are allowed to support.

And then the limit, which is the sharpest statement in this section.

> **The limit of record descent.** The composite-level witness of §6.6
> *carries* a record structure — its merge classes are
> $\{\{0,1\},\{2,3\}\}$, and the decision criterion returns yes — and its
> cut-coherence tensor is **fully diagonal**, so the record account is
> complete at the level of $\mathcal{C}$. Yet its composite still carries a
> boundary-gauge phase invariant that $\mathcal{C}$ cannot see.
> **Block-diagonalization of $\mathcal{C}$ under records is not phase
> triviality of the composite.**

This is the honest boundary of §4 read at the level of §6: records kill the
interference cross terms, and they do not kill the phase.

---

## 8. Independence of the obstruction families

Four obstruction families arise naturally around a composition defect: the
**temporal** one studied above; the **contextual** one of the CHSH scenario;
a **lattice-gluing** one, asking whether division-event assignments restrict
compatibly from a composite to its parts; and a **frame** one, asking
whether two orderings of the same two local events carry the same specified
content. This section asks whether they are one obstruction seen four times.

**They are not.** Each of the six pairs is *independent*: neither member is
a function of the other. The test is declared before any model is built, and
the witnesses are found mechanically.

**Every witness model is constructed here, from scratch, in exact
arithmetic.** Nothing in this section relies on any measurement made
elsewhere.

### 8.1 Six empirical models

On the CHSH cover — measurements $\{A_0,A_1,B_0,B_1\}$, contexts
$\{A_0,B_0\}$, $\{A_0,B_1\}$, $\{A_1,B_1\}$, $\{A_1,B_0\}$, outcomes
$\pm1$ — six models are declared. Each is verified normalized, non-negative
and no-signalling in exact arithmetic.

- **DET**: the deterministic assignment $A_0=A_1=B_0=B_1=+1$.
- **UNIF**: $P\equiv\tfrac14$.
- **LCORR**: an equal mixture of "everything $+1$" and "everything $-1$".
- **SINGLET**: $E_{ab}=-\cos(a-b)$ at the Tsirelson settings, over
  $\mathbb{Q}(\sqrt2)$.
- **HARDY**: the explicit no-signalling model with the Hardy support pattern
  $(4,3,3,3)$, given in full by
  $$
  \begin{array}{c|cccc}
   & (+,+) & (+,-) & (-,+) & (-,-)\\\hline
  (A_0,B_0) & 1/5 & 1/20 & 1/20 & 7/10\\
  (A_0,B_1) & 1/4 & 0 & 3/20 & 3/5\\
  (A_1,B_0) & 1/4 & 3/20 & 0 & 3/5\\
  (A_1,B_1) & 0 & 2/5 & 2/5 & 1/5
  \end{array}
  $$
- **PR**: the superquantum box, $P=\tfrac12$ when $xy=(-1)^{ab}$.

Their maximal CHSH values are, exactly,
$$
2,\qquad 0,\qquad 2,\qquad 2\sqrt2,\qquad \tfrac{14}{5},\qquad 4 .
$$

### 8.2 The contextual invariant

Let $X$ be the pair (hierarchy level, cohomological witness fires). The
level is decided by **certificates in both directions**.

*Positive certificate.* For the three local models an explicit distribution
on the sixteen deterministic global assignments is exhibited and verified to
reproduce the model entrywise: a point mass for DET, the uniform
distribution for UNIF, and a half-half mixture of the two constant
assignments for LCORR.

*Negative certificate.* The maximum of every signed CHSH functional over the
sixteen deterministic global assignments is **computed here, and is 2**;
a model whose own value exceeds it has no global distribution. This is
Fine's characterization [4], used as the cross-check it is.

The four levels are then: **NC** (a global distribution exists), **PC**
(contextual but every local section in the support extends to a global
assignment in the support), **LC** (some section does not extend), **SC** (no
global assignment is consistent with the support at all).

| model | level | consistent global assignments | non-extendable local sections | $\gamma\ne0$ |
|---|---|---|---|---|
| DET | NC | 1 | 0 | 0 of 4 |
| UNIF | NC | 16 | 0 | 0 of 16 |
| LCORR | NC | 2 | 0 | 0 of 8 |
| SINGLET | **PC** | 16 | 0 | **0 of 16** |
| HARDY | **LC** | 5 | 1 | **0 of 13** |
| PR | **SC** | 0 | 8 | **8 of 8** |

The **cohomological witness** $\gamma$ is computed for the criterion of [6]:
with $S$ the support presheaf and $F$ the free abelian presheaf it
generates, $\gamma(s_0)=0$ iff there are $r_i\in F(C_i)$ with
$r|_{C_0}=s_0$ agreeing on every overlap, the empty ones included. That is
an integer linear feasibility problem, decided here by exact integer
elimination.

**Attribution, before the numbers: both vanishing results are [6]'s own.**
They are reproduced independently here and are **not** findings of this
paper. The Hardy model is [6]'s own opening example of a *false positive* —
their terminology — exhibiting the same support pattern up to outcome
relabelling together with the mechanism by which a negative coefficient
defeats the support restriction; and the singlet verdict is an immediate
corollary of their proposition that possibilistic extendability implies the
obstruction vanishes on the whole support, since the singlet's support is
full. What this paper contributes here is the exact integer certificate and
the placement of these known facts inside the relation table.

With that in place: $\gamma$ vanishes identically on the singlet at the CHSH
settings — a model with **no global distribution at all** — and on HARDY,
which has a genuinely non-extendable local section. On this zoo the witness
fires on the strongly contextual box and on nothing else. **It is therefore
a separate object, strictly weaker than contextuality itself**, which is
[6]'s own stated status for it.

### 8.3 The carrier

Configurations are $C=\{(p_A,p_B)\}$ with $p_X\in\{r,+,-\}$: two
measurement-outcome pointers, $|C|=9$, initial configuration $(r,r)$. A
measurement step overwrites its own pointer, conditioning on the other
pointer whenever that pointer already carries an outcome and using its own
marginal otherwise. Two **frames** order the two steps: $F_1=(A,B)$ and
$F_2=(B,A)$. A **prefix** is either NONE or SWAPBACK — two pointer-exchange
steps first, so that the composite returns to the identity at the second
grid time, changing no final statistic. The **declared second leg** is
either the true conditional (**REC**) or the bare marginal (**COH**); the
*actual* dynamics always records, and only the declared leg changes. Two
**contexts** of the empirical model are realized. This gives
$$
6\ \text{tables}\times2\ \text{variants}\times2\ \text{prefixes}
\times2\ \text{contexts}=48\ \text{processes}.
$$

**Naming discipline.** There are no amplitudes anywhere in this carrier: the
tables are stochastic and no amplitude realization is built for any of them.
What the COH leg discards is a *classical record*, not a phase. What is
measured at the wing cut is therefore the **declared-law residual $D$ and
nothing else**; it is not $\Delta^{B}$, which is undefined on these tables,
and the two are never conflated.

**The temporal invariant $\mathsf{T}$** is the pair (the declared residual
at the wing cut is nonzero, existential divisibility fails there). Recording
kills the declared residual at every cut and every context — verified on all
24 recording processes. The non-recording residual at the wing cut is
$\text{joint}-\text{product}$, hence nonzero exactly on the correlated
tables.

**Divisibility, decided by certificates.** The question "is there a
column-stochastic $X$ with $X\,\text{src}=\text{tgt}$?" is decided first by
two exact certificates — equal source columns must carry equal targets, and
if the distinct source columns have pairwise disjoint supports a divisor is
**constructed** and verified entrywise — and otherwise by an exact Phase-I
simplex with Bland's rule over $\mathbb{Q}(\sqrt2)$. The simplex fallback is
invoked **64 times** across the sweep, and every invocation returns an exact
verdict; nothing is left undecided.

### 8.4 The lattice invariant

On the subsystem lattice $\{A,B,AB\}$, define for a subsystem $S$ with
complement $\bar S$ and declared reference configuration $c^\*=r$ the
reduced description
$$
\Gamma_S(t\!\leftarrow\!0)[u'\mid u]
=\Pr\bigl[\,\mathrm{cfg}_S(t)=u'\ \big|\ \mathrm{cfg}_S(0)=u,\
\mathrm{cfg}_{\bar S}(0)=c^\*\,\bigr],
$$
and say $\mathrm{DIV}_S(t)$ holds iff for **every** later grid time
$t_b\ge t$ there is a column-stochastic $X$ with
$X\,\Gamma_S(t\!\leftarrow\!0)=\Gamma_S(t_b\!\leftarrow\!0)$. Write $D(S)$
for the set of such $t$. The invariant $\mathsf{L}$ is the triple
$(D(A),D(B),D(AB))$ together with two gluing conditions:

- **restriction**: $t\in D(AB)\Rightarrow t\in D(A)$ and $t\in D(B)$;
- **gluing**: $t\in D(A)$ and $t\in D(B)\Rightarrow t\in D(AB)$.

Computed exactly:

| prefix | $D(A)$ | $D(B)$ | $D(AB)$ | restriction | gluing |
|---|---|---|---|---|---|
| NONE | $\{0,1,2\}$ | $\{0,1,2\}$ | $\{0,1,2\}$ | true | true |
| SWAPBACK | $\{0,2,3,4\}$ | $\{0,2,3,4\}$ | $\{0,1,2,3,4\}$ | **false** | true |

**This is the division-event non-gluing model.** The mechanism is exact and
elementary: at the first swap the *composite* description is a permutation,
hence invertible, so a divisor exists for every later target; but the
*atom's* reduced matrix there has constant columns — the wing's own pointer
has been replaced by the other wing's, which is still in its reference
configuration — and a matrix with constant columns cannot reach the identity
that the composite reaches two steps later. So the composite divides at a
step where neither atom can, and restriction-compatibility fails.
$\mathsf{L}$ is verified to depend only on the prefix.

### 8.5 The frame invariant

The **specified content** of a frame at grid time $t$ is the pair
$\bigl(p(t),\Gamma(t\!\leftarrow\!0)\bigr)$. Say the frames are
**mappable at grain $g$** iff there is a permutation $\pi$ of the nine
configurations with
$$
g\bigl(p_{F_1}(t)\circ\pi\bigr)=g\bigl(p_{F_2}(t)\bigr)
\quad\text{and}\quad
g\bigl(\pi\,\Gamma_{F_1}(t\!\leftarrow\!0)\,\pi^{-1}\bigr)
=g\bigl(\Gamma_{F_2}(t\!\leftarrow\!0)\bigr)
$$
for every $t$, where $g$ is the identity (full grain) or passage to supports
(support grain). The invariant $\mathsf{F}$ is that pair of booleans,
decided by an exhaustive depth-first search with pruning over the
permutation class, so a **negative is a proof of non-existence inside that
class**.

**This is the two-frame composite model.** The final law is frame-invariant
by construction — both orderings produce the same joint, by the chain rule —
while the intermediate slice content is not: in $F_1$ the $A$-outcome is
written and $B$'s pointer is still ready; in $F_2$ the reverse. Computed:
$\mathsf{F}=(\text{true},\text{true})$ for every model at the first declared
context and for DET, UNIF, LCORR, SINGLET and PR at the second, while
$$
\mathsf{F}(\text{HARDY, second context})=(\text{false},\ \text{true}).
$$
The full grain fails there because the two wings' marginals at that context
are $(\tfrac14,\tfrac34)$ and $(\tfrac25,\tfrac35)$, which no relabelling
identifies; at the support grain the two are still matched. $\mathsf{F}$ is
verified to depend only on the table and the context — not on the variant or
the prefix.

### 8.6 The relation table

**The test, declared before the models were built.** For an ordered pair of
invariants $(P,Q)$: *$Q$ is not a function of $P$* iff two processes exist
with equal $P$ and different $Q$. Witnesses both ways ⇒ **INDEPENDENT**.
Witness pairs are chosen mechanically, preferring the pair differing in the
fewest process coordinates, ties broken lexicographically, so the choice is
deterministic.

| pair | verdict | witness: $Q$ not a function of $P$ | witness: $P$ not a function of $Q$ |
|---|---|---|---|
| $\mathsf{T}$ vs $\mathsf{X}$ | **INDEPENDENT** | DET/REC vs HARDY/REC: $\mathsf{T}$ equal, level NC vs LC | DET/COH vs LCORR/COH: $\mathsf{X}$ equal (NC, $\gamma=0$), residual absent vs present |
| $\mathsf{T}$ vs $\mathsf{L}$ | **INDEPENDENT** | DET/COH/NONE vs DET/COH/SWAPBACK: $\mathsf{T}$ equal, restriction flips | DET/COH vs HARDY/COH: $\mathsf{L}$ equal, residual absent vs present |
| $\mathsf{T}$ vs $\mathsf{F}$ | **INDEPENDENT** | DET/REC vs HARDY/REC at the second context: $\mathsf{T}$ equal, $\mathsf{F}$ differs | DET/COH vs HARDY/COH: $\mathsf{F}$ equal, residual differs |
| $\mathsf{X}$ vs $\mathsf{L}$ | **INDEPENDENT** | DET/COH/NONE vs DET/COH/SWAPBACK: $\mathsf{X}$ is literally the same model, restriction flips | DET/COH vs HARDY/COH: $\mathsf{L}$ equal, level NC vs LC |
| $\mathsf{X}$ vs $\mathsf{F}$ | **INDEPENDENT** | HARDY at the two contexts: $\mathsf{X}$ unchanged, $\mathsf{F}$ differs | DET/COH vs HARDY/COH: $\mathsf{F}$ equal, level NC vs LC |
| $\mathsf{L}$ vs $\mathsf{F}$ | **INDEPENDENT** | DET/COH vs HARDY/COH at the second context: $\mathsf{L}$ equal, $\mathsf{F}$ differs | DET/COH/NONE vs DET/COH/SWAPBACK: $\mathsf{F}$ equal, restriction flips |

**Six of six INDEPENDENT. Zero equivalences constructed.**

Two of the twelve witness cells deserve comment. The $\mathsf{X}$-vs-$\mathsf{L}$
cell is carried by two processes sharing the same table, so they induce
*literally the same empirical model* while the lattice invariant flips — the
strongest available form of that separation. And the $\mathsf{X}$-vs-$\mathsf{F}$
cell is carried by one table realized at two contexts: the contextual
invariant is a property of the whole empirical model and does not move, while
the frame invariant, which sees only the realized context, does.

### 8.7 The count, and what it decides

Counting the separately decided invariants: the three temporal objects
($\Delta^{B}$, the declared residual, existential divisibility), the three
nested levels of the contextual hierarchy, the cohomological witness, the
lattice invariant and the frame invariant — **nine**. Under the collapsed
convention, counting the contextual hierarchy once, the number is **seven**.
Nothing in the relation table turns on the choice: every entry uses the
contextual invariant as the pair (level, witness fires), and all six
verdicts are identical either way.

Strict implications found: $\Delta^{B}=0\Rightarrow d_{\mathrm{div}}=0$ for
the Born-declared pair, strict by Theorem 2.3; SC $\Rightarrow$ LC
$\Rightarrow$ contextual, both strict on this zoo; and $\gamma\ne0 \Rightarrow$ contextual, strict with **two** witnesses (the singlet *and*
Hardy are contextual with $\gamma=0$ at every section). **Constructed
equivalences: none.**

**A finding worth stating plainly.** Both natural candidates for a "master"
invariant have false zeros, and they do not vanish together: $\Delta^{B}$
vanishes on a fully unbiased pair by phase alignment (§2.2), and $\gamma$
vanishes on the Tsirelson-saturating singlet by full support (§8.2 — [6]'s
own result). A single master invariant would need a zero-locus that both
agree with, and no such locus exists in this zoo.

**Caps and scope.** One measurement scenario (the CHSH four-cycle), binary
outcomes, six empirical models, 48 processes, $|C|=9$, three or five grid
times. INDEPENDENT means what the test says: neither invariant is a function
of the other *on this zoo*. It is a negative result about determination, not
a claim that no relation of any kind exists. The lattice and frame
instruments are declared reduced constructions on this carrier, not
reproductions of any other apparatus. And since no amplitude realization is
built for any table here, **$\Delta^{B}$ is undefined on all six** and every
finding of this section is about the declared residual or about existential
divisibility.

---

## 9. Relation to Barandes

This section states what is taken from [1,2,3], what is proved *about* the
framework, where this paper extends it, and where its texts resist. It makes
no claim about nature and draws no ontological conclusion; it is a delimited
reading of published texts, with the relevant hedges quoted.

### 9.1 What is taken

The configuration space, the epistemic/nomological/dynamical split, division
events and the free target time, the law of total probability at a division
event, the identity $\Gamma=|\Theta|^{\circ2}$, the entrywise
Schur–Hadamard gauge with one $U(1)$ per ordered pair, unitarity-fixing as a
*partial* gauge fixing, unistochasticity and the stochastic-quantum theorem,
the dilation that enlarges the internal space without touching the
configuration space, and the diagnosis of the pseudo-stochastic
interpolant — all are Barandes' and are cited at the point of use in §1.1
and below. The stochastic-quantum theorem itself is proven mathematics and
is not under test here.

The identification of the Born-projection cross terms with interference is
[1]'s; Theorem 2.1 is a rewriting of it in closed form.

### 9.2 The law-of-total-probability lemma

**Lemma 9.1 (forcing).** *Let $M$ be a model satisfying [3]'s three axioms
[3, p.29] with finite configuration space $C$, $|C|=N$. Let $0$ and $t'$ be
two **division events** of $M$ ([3, p.9]; $0$ is one by [3]'s own
convention), and let $t$ be any target time ([3, p.10]: the target time is a
free variable). The dynamical axiom supplies $M$ with the fixed
column-stochastic matrices $\Gamma(t'\!\leftarrow\!0)$,
$\Gamma(t\!\leftarrow\!0)$ and $\Gamma(t\!\leftarrow\!t')$, and [3]'s law of
total probability (eqs. 19–20, p.9) holds at **both** conditioning times.
Write*
$$
D\;:=\;\Gamma(t\!\leftarrow\!0)\;-\;\Gamma(t\!\leftarrow\!t')\,\Gamma(t'\!\leftarrow\!0)
$$
*for the declared-law residual. Call a distribution over $C$ at time $0$
**admissible** iff the model actually runs on it — i.e. iff the epistemic
axiom permits it: $p$ is "**contingent**, meaning that it can vary between
runs of the model", and it "is **connected between different times by the
model's transition probabilities**" [3, p.29]. Nothing else is meant by
"admissible" anywhere below. Then:*

**(a) Vector form, no extra hypothesis.** *For every admissible $p(0)$,
$D\,p(0)=0$.*

*Proof.* The epistemic axiom's connecting clause is what licenses reading
the model's **declared** transition matrices as the matrices connecting
$p(0)$ to later times, so eq. (20) applies at each declared conditioning
time. Hence $p(t')=\Gamma(t'\!\leftarrow\!0)p(0)$ and
$p(t)=\Gamma(t\!\leftarrow\!0)p(0)$ by eq. (20) at the division event $0$;
and $p(t)=\Gamma(t\!\leftarrow\!t')p(t')$ by eq. (20) at the division event
$t'$. Substituting the first into the third and subtracting the second gives
$D\,p(0)=0$, using only associativity of the matrix action. $\square$

**(b) Matrix form, under a spanning hypothesis.** *If the admissible
distributions span $\mathbb{R}^N$ then $D=0$ exactly, as matrices.*

**(c) The forcing (contrapositive of (a)).** *If the model exhibits a target
time $t$ and an admissible $p(0)$ with $D\,p(0)\ne0$, then $t'$ is **not** a
division event of that model. No hypothesis beyond [3]'s own eqs. (19)–(20)
is used; the spanning hypothesis is **not** needed for (c).*

Three things are verified. First, the one non-trivial step of (a) — the
associativity of the matrix action — is checked as a formal identity with
all $21$ entries indeterminate over $\mathbb{Q}$ at $N=3$: no property of
stochasticity is assumed. Second, **the spanning hypothesis is
load-bearing**, by an exact separating instance: the matrix $J_-$ of §2.4 is
nonzero yet annihilates $(\tfrac12,\tfrac12)$, so the vector form is
strictly weaker than the matrix form; and spanning restores it, since the
same matrix fails to annihilate a point mass, so admitting the $N$ point
masses across runs already forces $D=0$. Third, a control: a difference of
two column-stochastic matrices has identically zero column sums, so
$D\,p(0)$ always sums to zero — **the violation is cancelling mass, and
detection must count entries, never totals.**

**The spanning hypothesis is this paper's strengthening and is not stated by
[3].** What [3] states is only that $p$ is "contingent, meaning that it
**can vary between runs**" against dynamical laws that "are **fixed
features**" [3, p.29], which does not by itself supply a spanning family.
Clause (b) is flagged accordingly wherever it is used, and clause (c) — the
one that does the work below — does not need it.

### 9.3 The forcing, exhibited

The composite model of Definition 4.9 declares $t'=2$ (the first
measurement) a division event on the strength of [3, p.29]'s "division
events are generated during a measurement process". Evaluated on the
model's own declared initial distribution — a point mass, hence admissible
in the sense above — with $t=3$:

| setting pair | frame | nonzero residual entries of 36 | differing matrix entries |
|---|---|---|---|
| $(0^\circ,45^\circ)$ | $F_1$ / $F_2$ | 0 / 0 | 0 / 0 |
| $(0^\circ,135^\circ)$ | $F_1$ / $F_2$ | 0 / 0 | 0 / 0 |
| $(90^\circ,45^\circ)$ | $F_1$ / $F_2$ | **16 / 16** | **288 / 288** |
| $(90^\circ,135^\circ)$ | $F_1$ / $F_2$ | **16 / 16** | **288 / 288** |
| $(0^\circ,0^\circ)$ | $F_1$ / $F_2$ | 0 / 0 | 0 / 0 |
| $(45^\circ,45^\circ)$ | $F_1$ / $F_2$ | **16 / 16** | **288 / 288** |

The residual sums to zero at every cell, as the control requires. The value
censuses are computed and are **not the same at the three violated
settings**, and this is stated rather than glossed:

- at $(90^\circ,45^\circ)$ and $(90^\circ,135^\circ)$ the sixteen nonzero
  entries take exactly **four** values, $\pm\tfrac1{32}\pm\tfrac{\sqrt2}{32}$,
  four times each, with **zero rational entries**;
- at $(45^\circ,45^\circ)$ they take **six** values, of which **eight of the
  sixteen entries are the plain rationals $\pm\tfrac1{64}$**.

So at the first two settings the violation is irrational and cannot be an
artefact of rational truncation; **that extra argument does not apply at the
third**, and is not asserted there. The violation is exact all the same —
the arithmetic is exact everywhere, with no float and no tolerance — so
exactness never depended on irrationality. Why the two censuses differ is
**not explained here**; nothing rests on the explanation, only on the
censuses, which are computed.

> **The forcing fires.** At three of the six setting pairs, in both frames,
> [3]'s own eqs. (19)–(20) at the declared division events $0$ and $t'=2$
> are contradicted by the model's own declared law on the model's own
> declared distribution. By clause (c), $t'=2$ **is not a division event of
> that model as declared** — that is, not an *exact* division event of the
> *unmarginalized* composite. **The denial is forced by the framework's own
> equations, not imposed from outside.**

**Scoped, by Barandes' own hedge.** All of the above concerns **exact,
unmarginalized** division events. [3, p.10] allows that in practice division
events *"may be generated to an extremely good approximation through
interactions with other systems, after marginalizing over those other
systems"*. A model that declares only *that* — an approximate division event
for a *marginalized* description — is untouched here: there is no exact
eq.-(20) identity for the lemma to contradict, this paper runs no
approximation theory, and no claim is made about how large the residual is
relative to anything. The lemma bites exactly one reading, and it is the
reading the model above declares.

It does **not** show [3] inconsistent. [3] states no model. What it shows is
that a natural model of a two-measurement experiment, built to [3]'s own
prescriptions and declaring an **exact** division event for the
**unmarginalized** composite, cannot keep both that declaration and the law
of total probability of p.9 — and that the framework itself decides which
one goes.

Two further exact facts about the same model bear on [3]'s text.
The would-be interpolant $\tilde\Gamma(t\!\leftarrow\!t')= \Gamma(t\!\leftarrow\!0)\Gamma^{-1}(t'\!\leftarrow\!0)$ is offered by [3,
p.10] *"at least if $\Gamma(t'\!\leftarrow\!t_0)$ is invertible"*; here the
exact ranks of the first leg over the twelve cells are $27$ or $18$, **never
36**, so the hypothesis fails outright and the pseudo-stochastic diagnosis
is not even reached. And the amplitude propagators compose exactly at all
twelve cells, so on *this* model the declared-law residual and the
Born-shadow defect are the same object — which is why the two names may be
used interchangeably here and nowhere else.

### 9.4 Faithful, extension, tension

**Faithful.** The following are Barandes' own, and this paper uses them as
stated: the configuration space as a fixed feature; the separability of the
epistemic layer; the dynamical axiom as sparse in the conditioning slot and
free in the target slot; the system-centricity of division events; the Born
identity as an *identity, not a postulate*; unistochasticity as the
shadow-of-lift statement; the entrywise gauge, **sharpened here only in its
indexing** — the phases are indexed $(i,j)$, one $U(1)$ per *ordered pair of
configurations per time*, not one per configuration, which [3] itself makes
explicit in the dilated version [3, p.27, eq. 106]; unitarity-fixing as a
partial gauge fixing; dilation as enlargement of the internal space over
each configuration pair, with the configuration space untouched; and the
pseudo-stochastic interpolant as the diagnosis of restarting where the law
does not serve.

**Extension.** Three moves are this paper's and are marked as such wherever
they appear.

1. **The composition defect as the subject.** [3] names no such invariant.
   What it does assert is the phenomenon — *"indivisible stochastic
   processes generically exhibit all the hallmark empirical features of
   quantum systems, including interference, decoherence, entanglement, and
   noncommutative observables"* [3, p.2]. The identification of interference
   with the failure of the shadow to compose, and the organization of the
   results above around it, is this paper's naming, not a result imported
   from him.
2. **The gauge licensing.** [3] declares the entrywise gauge for a single
   propagator and says that fixing a unitary representative is a *partial*
   fixing. Theorems 5.4 and 5.5 determine exactly what the composability and
   unitarity requirements leave — the boundary subgroup — and Proposition
   5.1 shows that without them nothing phase-sensitive survives at all.
   Neither theorem is in [3].
3. **The spanning hypothesis** of Lemma 9.1(b), which [3] does not state,
   and which is shown here to be load-bearing.

**Tension, with both sides quoted.** Two places where a natural reading of
the results above runs against [3]'s text, and where this paper takes the
weaker option.

*Matrix-form divisibility across division events.* [3] writes that *"an
indivisible stochastic process, as befits its name, will **not generally
obey a divisibility condition** like (7) or (14)"* [3, p.10]. Lemma 9.1(b)
appears to say the opposite across a *pair* of division events. The two are
compatible, and the reconciliation is informative: [3]'s indivisibility is a
statement about times that are **not** division events — the eq.-(22)
discussion is explicitly about manufacturing a leg for a $t'$ the law does
not serve. Across a pair of *declared* division events the framework's own
law of total probability leaves no room. **Indivisibility lives between
division events, never across them.** The matrix form nevertheless needs the
spanning hypothesis, which [3] does not supply; on the model of §9.3 it is
not needed, because the model's own declared distribution already witnesses
the violation.

*Whether a phase-retaining structure may be treated as more than
bookkeeping.* §6 exhibits an invariant of the projective map that the Born
shadow cannot determine. Nothing in this paper concludes anything about its
status, and [3]'s own caution runs the other way: *"the Hilbert-space
formulation of an indivisible stochastic process is ultimately a collection
of **gauge-dependent quantities, or gauge variables**. In any physical
theory, one does not typically try to assign gauge variables an ontological
meaning."* [3, p.20]. The results of §5 are precisely a determination of
*which* part of that freedom is gauge once composition and unitarity are
required, and which part is not; whether the non-gauge remainder is anything
more than surplus representation is **not decided here and is not claimed**.

Finally, a remark of [3] that this paper's §5 and §6 make sharp rather than
contradict: [3] observes that the only fibre bundle in that paper — copies
of the system's Hilbert space fibred over a one-dimensional time base — *"has
vanishing curvature"* [3, p.21, fn. 16], which is anyway forced by the base
being one-dimensional. **No holonomy content lives in that bundle.** The
holonomies of §5 and §6 live on a different object entirely — the bipartite
support graph of a matrix, and the tripartite path graph of a composable
pair — and nothing above is in tension with that footnote.

---

## 10. Open problems, and non-claims

### 10.1 Open problems

1. **General $n$ for the completeness dichotomy.** Theorem 6.11(i) is proved
   for every admissible support class at $n\le4$ and sampled at $n=5$.
   Whether $L_4+\mathcal{K}=Z(\mathsf{G})$ for **every** admissible pair
   graph is open; it is the natural conjecture and it is untested.
2. **Exhaustive $n=5$.** The $n=5$ statement here rests on a declared
   strided sample (653 patterns, 2100 graph classes). An exhaustive $n=5$
   sweep is not attempted.
3. **Minimality of the completion.** Every failing class has rank deficit
   exactly one, so one further cycle per class would suffice.
   $\mathcal{K}$ is sufficient and uniformly definable; whether a smaller
   uniformly definable completion exists is open.
4. **Converse record notions.** The reverse implication *medium decoherence
   $\Rightarrow$ records* is refuted here only for this paper's notion — a
   configuration-space partition constrained by supports. For the coarser
   decoherent-histories notion the corresponding biconditional is a known
   theorem [14] and is untouched; whether an intermediate notion closes the
   gap is open.
5. **Beyond CHSH.** §3 and §8 are confined to the CHSH $(2,2,2)$ scenario.
   Whether the independence of §8 persists at more settings, parties or
   outcomes — where real-versus-complex separates and the planar argument of
   §3.2 does not apply — is untested.
6. **Sharpness of the decision criterion beyond $n=3$.** The exact sharpness
   of Theorem 4.6 on realizable supports is established at $n=3$ only.
7. **The relation-loop layer off the Weyl families.** $\beta$ is defined
   only where the group commutator is scalar; the composite-level witness of
   §6.6 has an empty relation-loop sector. A phase-retaining invariant
   defined without that hypothesis is not supplied here.

### 10.2 Non-claims, restated

- **No claim about nature.** Every result is a statement about declared
  finite models, declared families and declared scopes.
- **No Born-rule derivation** and no derivation of quantum theory is
  claimed. §3's chain is assembled from cited antecedents [4,7,8]; the
  contribution there is the exact assembly and the two class-level
  statements of §3.3.
- **$\Delta^{B}$ is not a divisibility measure** (Theorem 2.3), and it is
  never equated with indivisibility anywhere above.
- **The coherence law is an identity of associativity** (§2.6). It
  constrains the family and selects nothing.
- **The flat-spectrum equivalence is classical** [16] and is cited, not
  proved. Only the identification of the vanishing locus with it is claimed.
- **The record hypotheses are sufficient, never necessary** (§4.7), and no
  claim survives coherent erasure or any operation recombining the record
  sectors (§4.6).
- **The gauge reduction is scoped to composable unitary systems**; for an
  isolated non-unitary arrow the full entrywise gauge stands and no phase
  invariant exists (Proposition 5.1).
- **$\beta$ is not finer than the Born shadow** — the two are incomparable
  (§6.2), and the claim is non-factorization only.
- **The completion is gated, not proved, and is not claimed minimal**
  (§6.6).
- **Record descent has a measured limit**: a record can be present, the
  cut-coherence tensor fully diagonal, and the composite still
  phase-nontrivial (§7.4).
- **The independence result is a negative result about determination** on a
  declared zoo (§8.7), not a claim that no relation of any kind exists; and
  $\Delta^{B}$ is undefined on that zoo's tables.
- **The forcing of §9.3 tests one reading only** — exactly declared,
  unmarginalized division events. Barandes' hedged, approximate,
  marginalized reading [3, p.10] is a different object and is not tested.
- **No ontological conclusion is drawn** from any invariant exhibited here.
  §9.4 states where [3]'s own text resists such a reading, and takes the
  weaker option.

---

## Appendix: reproduction

Every number printed in this paper is regenerated in exact arithmetic by the
accompanying bundle. There is no floating-point number and no tolerance in
any substantive path: rational arithmetic uses `fractions.Fraction`; complex
algebraic quantities live in the cyclotomic fields $\mathbb{Q}(\zeta_n)$ for
$n=2,3,4,5,6,8,12,16$ in a canonical representation modulo $\Phi_n$, so tuple
equality *is* field equality; the composite model of Definition 4.9 lives in
the totally real quartic field $\mathbb{Q}(\cos\pi/8)=\mathbb{Q}[x]/(8x^4-8x^2+1)$;
order comparisons are made only in $\mathbb{Q}(\sqrt2)$ with an exact sign
oracle; symbolic identities are checked in a multivariate polynomial ring
over $\mathbb{Q}$; and lattice statements use integer Hermite normal form.

### Inventory

The bundle is `v12/paper1_code/`. Each section script is independently
runnable and imports only the shared exact-arithmetic module.

| file | regenerates |
|---|---|
| `exact.py` | the shared arithmetic layer: cyclotomic and general number fields, $\mathbb{Q}(\sqrt2)$ with an exact sign oracle, matrices and the Born projection, a multivariate polynomial ring, integer Hermite normal form, graph cycle ranks, and the anchor harness |
| `model_composite.py` | the composite two-measurement model of Definition 4.9, shared by §4, §8 and §9 |
| `sec2_defect_algebra.py` | §2 entire: the closed form, the two reference families and the vanishing census, the three-defect separation, the coherence and tree laws, the six substitutes, the invariance group, the bounds and the $n=2$ range, the annihilator, the flat-spectrum identification, reality and the odd channel |
| `sec3_chsh_bodies.py` | §3 entire: the three maxima, the four certificates and the saturating instance, the 24 no-signalling vertices, the three planar-sufficiency ingredients and the strided rational sweep, the non-convexity and the sharp exclusion, the four-cycle product identity, the anti-correlation exhibit |
| `sec4_records.py` | §4 entire: the termwise vanishing, the exhaustive $n=3$ sweep, the 25 realizable supports with exact witnesses, sharpness, the monomial endpoints, the reading route, the approximate bound, the multi-cut corollary, the dimension-four census, the composite model's biconditional, the eraser control and floor, the converse witnesses |
| `sec5_gauge.py` | §5 entire: the modulus-class orbit, the typing of triple products, the composition-compatibility theorem with the degeneracy measurement, the unitarity-preservation theorem with the placed-rotation gap, the shadow-moving check, the orbit theorem and support stratification |
| `sec6_signature.py` | §6 entire: the cancellation and collapse, $\beta$ and its invariances and the non-refinement counterexample, the tensor's seven properties, full-support completeness, the $n\le4$ sweep with the total-support screen and the $\varphi$-criterion, the composite-level witness, the completion and its four properties, the declared $n=5$ sample |
| `sec7_descent.py` | §7 entire: the two descent theorems, the coarse-record control, the eraser, the diagonal-tensor census with its declared degeneracy, the limit witness |
| `sec8_independence.py` | §8 entire: the six models, the hierarchy with certificates in both directions, the cohomological witness over $\mathbb{Z}$, the carrier and its 48 processes, the three instruments, the relation table |
| `sec9_ltp.py` | §9 entire: the associativity identity, the spanning separation, the column-sum control, the twelve-cell forcing table with both value censuses, the interpolant ranks |
| `paper1_run_all.py` | runs every section in order, prints the receipts table, and exits 0 iff every self-anchor passes |
| `RUN.txt` | the output of one full run |

### Anchors

Anchors are **self-anchors**: each compares a computed value against the
value *printed in this paper*. Exit 1 happens only on such a mismatch.
**Substantive negatives exit 0** — the seven failing support classes, the
composite-level witness, the refuted converse implications, the
recorded-but-phased limit and the forcing of §9.3 are results, not failures.

### Receipts

One full run of `paper1_run_all.py`:

| section | script | anchors | pass | fail | seconds |
|---|---|---|---|---|---|
| 2 | `sec2_defect_algebra.py` | 76 | 76 | 0 | 65.9 |
| 3 | `sec3_chsh_bodies.py` | 58 | 58 | 0 | 18.6 |
| 4 | `sec4_records.py` | 62 | 62 | 0 | 3.0 |
| 5 | `sec5_gauge.py` | 50 | 50 | 0 | 42.1 |
| 6 | `sec6_signature.py` | 66 | 66 | 0 | 30.9 |
| 7 | `sec7_descent.py` | 27 | 27 | 0 | 11.6 |
| 8 | `sec8_independence.py` | 14 | 14 | 0 | 11.2 |
| 9 | `sec9_ltp.py` | 16 | 16 | 0 | 0.8 |
| **all** | | **369** | **369** | **0** | **184.0** |

Anchor counts are reproducible exactly; the seconds column is wall-clock and
machine-dependent.

### Declared strides and samples

Three places use a declared deterministic stride or sample rather than an
exhaustive enumeration, and each is named in the text where its number
appears:

- §2.4 and §2.6: strides of 24 members of $\mathcal{F}_2$ and 21 of
  $\mathcal{F}_3$ for the invariance-group and corroboration sweeps.
- §3.2: from the full enumerations of rational unit vectors (246 in
  $\mathbb{R}^3$ at entries $|k|\le9$; 808 in $\mathbb{R}^4$ at $|k|\le5$),
  every 9th respectively every 31st, keeping 26 in each case, then all
  $26^4$ configurations.
- §6.6: at $n=5$, the 120 permutations in lexicographic order with stride 3
  (40 of them), all unions of 2, 3 and 4 of those, filtered by the necessary
  condition and reduced modulo the same relabellings.

Everything else in the paper is exhaustive at its declared scope: the
$n=3$ support sweep, the $n\le4$ graph-class sweep, the record gates, the
$\beta$ table, the three convex bodies, the coherence law, the composite
model and every reconstructed independence witness.

---

## References

- **[1]** J. A. Barandes, *The Stochastic-Quantum Correspondence*,
  arXiv:2302.10778.
- **[2]** J. A. Barandes, *The Stochastic-Quantum Theorem*,
  arXiv:2309.03085.
- **[3]** J. A. Barandes, *Quantum Systems as Indivisible Stochastic
  Processes*, arXiv:2507.21192. Page numbers in quotations are that
  document's own.
- **[4]** A. Fine, *Hidden Variables, Joint Probability, and the Bell
  Inequalities*, Phys. Rev. Lett. **48**, 291 (1982).
- **[5]** S. Abramsky, A. Brandenburger, *The Sheaf-Theoretic Structure of
  Non-Locality and Contextuality*, New J. Phys. **13**, 113036 (2011).
- **[6]** S. Abramsky, S. Mansfield, R. S. Barbosa, *The Cohomology of
  Non-Locality and Contextuality*, arXiv:1111.3620.
- **[7]** B. S. Tsirelson, *Quantum generalizations of Bell's inequality*,
  Lett. Math. Phys. **4**, 93 (1980); and the real-unit-vector
  characterization of the $(2,2,2)$ quantum correlator set with its
  dimension-free bound.
- **[8]** S. Popescu, D. Rohrlich, *Quantum nonlocality as an axiom*, Found.
  Phys. **24**, 379 (1994); J. Barrett, N. Linden, S. Massar, S. Pironio,
  S. Popescu, D. Roberts, *Nonlocal correlations as an information-theoretic
  resource*, Phys. Rev. A **71**, 022101 (2005).
- **[9]** Weyl relations and the noncommutative torus: projective
  multipliers on $\mathbb{Z}^2$ realized by the clock/shift pair; see e.g.
  arXiv:1606.01829.
- **[10]** The Stone–von Neumann theorem, finite form: on $\mathbb{C}^N$ the
  irreducible projective representations of $\mathbb{Z}^2$ with a primitive
  $q$-th root multiplier have dimension exactly $q$ and are the Weyl pair up
  to unitary equivalence and scalars. **Cited, not proved here.**
- **[11]** T. Zaslavsky, *Signed graphs*, Discrete Appl. Math. **4** (1982)
  47–74, and the gain-graph switching classification developed there and in
  its sequels. **The classification statement of §5.5 is this theorem, cited
  and not claimed.**
- **[12]** *On cospectrality of gain graphs*, DOI 10.1515/spma-2022-0169
  (secondary).
- **[13]** N. Mukunda et al., *Bargmann invariants and off-diagonal geometric
  phases for multi-level quantum systems*, arXiv:quant-ph/0107006. The
  ray/Gram setting: Bargmann triple products are invariants of a
  **one-index** ray gauge on a single Hilbert space, not of the bipartite
  matrix gauge of §5.
- **[14]** M. Gell-Mann, J. B. Hartle, *Classical equations for quantum
  systems*, Phys. Rev. D **47**, 3345 (1993): for a pure initial state, a
  set of histories medium-decoheres iff generalized records exist. **Cited,
  never re-derived, never claimed here.**
- **[15]** J. J. Halliwell, *Somewhere in the universe: Where is the
  information stored when histories decohere?*, Phys. Rev. D **60**, 105031
  (1999).
- **[16]** The discrete Wiener–Khinchin theorem — the periodic
  autocorrelation of a sequence and the squared modulus of its discrete
  Fourier transform are a transform pair — and the classical theory of
  CAZAC / perfect sequences, for which flatness of $|\widehat\varepsilon|$
  *is* the defining property, with explicit constructions at every $N$:
  G. Björck; D. C. Chu; R. L. Frank; R. J. Turyn; S. W. Golomb and G. Gong,
  *Signal Design for Good Correlation* (CUP, 2005). **§2.8 originates
  neither.**
- **[17]** G. Birkhoff; J. von Neumann: a doubly stochastic matrix is a
  convex combination of permutation matrices — used in §6.5 as the
  total-support screen.
