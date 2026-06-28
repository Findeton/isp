# The Walsh Delta Global-Optimality Problem

This note isolates the real mathematical problem. The easy fact is that the
delta-shaped Walsh field is the unique maximally deep field. The novel problem
is to prove that this same field is globally optimal for the seal/chiral gap
among all Walsh fields with nonzero coefficients equal to $\pm 1$.

## 1. The Class Of Objects

Fix $n \ge 2$ and let

$$
G=\{-1,+1\}^n,
\qquad
N=|G|=2^n.
$$

For each nonzero mask $a \in \mathbb F_2^n\setminus\{0\}$, let

$$
\chi_a(s)=\prod_{i:a_i=1}s_i
$$

be the corresponding Walsh character. An orientation is a sign choice

$$
\epsilon_a \in \{-1,+1\}
\qquad
(a\ne 0).
$$

It defines the Walsh field

$$
T_\epsilon(s)=\sum_{a\ne 0}\epsilon_a\chi_a(s).
$$

Equivalently, $T_\epsilon$ is a real function on $G$ whose constant Walsh
coefficient is zero and whose every nonconstant Walsh coefficient has modulus
one.

## 2. The Delta Candidate

For a chosen point $s_{\star} \in G$, define

$$
T_{\star}(s)=1-N\mathbf{1}_{s=s_{\star}}.
$$

Thus

$$
T_{\star}(s_{\star})=-(N-1),
\qquad
T_{\star}(s)=1 \quad (s\ne s_{\star}).
$$

After normalization by $N-1$, this is the vector with one value $-1$ and all
other values equal to $1/(N-1)$:

$$
\frac{T_{\star}(s_{\star})}{N-1}=-1,
\qquad
\frac{T_{\star}(s)}{N-1}=\frac{1}{N-1}
\quad (s\ne s_{\star}).
$$

It has mean zero:

$$
-1+(N-1)\frac{1}{N-1}=0.
$$

The Walsh signs realizing this field are

$$
\epsilon_a=-\chi_a(s_{\star}).
$$

Indeed,

$$
\sum_{a\ne 0} -\chi_a(s_{\star})\chi_a(s)
=
1-N\mathbf{1}_{s=s_{\star}}.
$$

## 3. The Easy/Done Fact

The following fact is not the novel problem.

**Lemma.** If an orientation satisfies

$$
T_\epsilon(s_0)=-(N-1)
$$

at some point $s_0\in G$, then it is exactly the delta orientation centered at
$s_0$:

$$
\epsilon_a=-\chi_a(s_0)
\qquad
(a\ne 0).
$$

Consequently,

$$
T_\epsilon(s)=1-N\mathbf{1}_{s=s_0}.
$$

**Reason.** The number $T_\epsilon(s_0)$ is a sum of $N-1$ terms, each equal to
$\pm 1$:

$$
T_\epsilon(s_0)=\sum_{a\ne 0}\epsilon_a\chi_a(s_0).
$$

The only way this sum can equal its minimum possible value $-(N-1)$ is for
every summand to be $-1$. Hence

$$
\epsilon_a\chi_a(s_0)=-1
$$

for every $a\ne 0$, which gives $\epsilon_a=-\chi_a(s_0)$.

This proves uniqueness at maximal depth. It does not prove global optimality.

## 4. The Real Novel Problem

For an orientation $\epsilon$, define a sealed probability law

$$
P_\epsilon(s)
=
\frac{
\exp\left(\sum_{a\ne 0}h_a\epsilon_a\chi_a(s)\right)
}{
\sum_{r\in G}
\exp\left(\sum_{a\ne 0}h_a\epsilon_a\chi_a(r)\right)
},
$$

where the parameters $h_a$ are determined by the seal equations

$$
\mathbb E_{P_\epsilon}[\epsilon_a\chi_a]=e^{-h_a}
\qquad
(a\ne 0).
$$

Let $U$ be the uniform law on $G$. Define the gap

$$
\widehat m(\epsilon)=D(P_\epsilon\|U).
$$

The real problem is:

**Global Delta Optimality Problem.** Prove that for every $n\ge 2$ and every
orientation $\epsilon$,

$$
\widehat m(\epsilon)\ge \widehat m(\epsilon_{\star}),
$$

where $\epsilon_a^{\star}=-\chi_a(s_{\star})$ is any delta orientation.
Moreover, equality should occur only for the spin-flip orbit of the delta
orientation.

In words:

> Among all zero-mean Walsh fields whose nonconstant Walsh coefficients are
> all $\pm 1$, the one-spike delta field should be the unique global minimizer
> of the seal/chiral gap.

## 5. Why This Is Not The Easy Lemma

The easy lemma only says:

$$
\min_s T_\epsilon(s)=-(N-1)
\quad
\Longrightarrow
\quad
T_\epsilon=T_{\star}.
$$

The hard problem must rule out every other Walsh field, including fields whose
minimum value is not as deep as $-(N-1)$ but whose full value distribution and
seal tilt might still produce a smaller gap.

So the missing theorem is not:

> The delta field is the unique deepest field.

That is already elementary.

The missing theorem is:

> No shallower or multi-level Walsh field has a smaller sealed relative entropy
> than the delta field.

This is an extremal problem for $\pm 1$ Walsh spectra, not just a pointwise
minimum problem.

## 6. Equivalent Entropy Form

Since

$$
D(P_\epsilon\|U)=\log N-H(P_\epsilon),
$$

the global optimality problem can also be stated as an entropy maximization
problem:

$$
H(P_\epsilon)\le H(P_{\epsilon_{\star}})
$$

for every orientation $\epsilon$.

Thus the delta field is conjectured to make the sealed law as entropic as
possible, even though the unsealed Walsh field itself is the most negatively
concentrated at one point.

That tension is the core novelty of the problem.

## 7. Current Proof Architecture And Reductions

This section records the current state of the proof search. It is not yet a
complete proof of global optimality; rather, it isolates the exact continuous
problem and the remaining cone inequality that would complete the theorem.

### 7.1 Normalized Density And Exact Fourier-Log Seal

Let

$$
X(s)=N P_\epsilon(s)
$$

be the density of the sealed law relative to the uniform law. Thus

$$
\mathbb E_U[X]=1,
\qquad
\widehat m(\epsilon)=D(P_\epsilon\|U)
=\mathbb E_U[X\log X].
$$

Use normalized Walsh coefficients

$$
\widehat f(a)=\mathbb E_U[f\chi_a].
$$

Since

$$
\widehat X(a)=\mathbb E_U[X\chi_a]=\mathbb E_{P_\epsilon}[\chi_a],
$$

the seal equations imply

$$
\epsilon_a\widehat X(a)=e^{-h_a}.
$$

Hence, if

$$
x_a=\widehat X(a),
\qquad
u_a=|x_a|,
\qquad
\sigma_a=\operatorname{sgn}(x_a)=\epsilon_a,
$$

then

$$
x_a=\sigma_a u_a,
\qquad
u_a=e^{-h_a}.
$$

On the other hand,

$$
\log X(s)=
\sum_{a\ne0}h_a\epsilon_a\chi_a(s)
\;+\;\text{constant},
$$

so its nonconstant Fourier coefficients satisfy

$$
\widehat{\log X}(a)=h_a\epsilon_a.
$$

Since \(h_a=-\log u_a\), the seal is equivalently the nonlinear
Fourier-log fixed point

$$
\boxed{
\widehat{\log X}(a)
=
-\operatorname{sgn}(\widehat X(a))\log|\widehat X(a)|
}
\qquad(a\ne0).
$$

This is one exact boundary of the problem: the sealed laws are precisely the
positive densities \(X\) of mean one whose Fourier coefficients and
log-Fourier coefficients obey this relation.

### 7.2 Convex Dual Form

Let

$$
F(\ell)=
\log\mathbb E_U\exp\left(\sum_{a\ne0}\ell_a\chi_a\right).
$$

Its convex conjugate is the entropy functional

$$
F^*(x)=\mathbb E_U[X\log X],
\qquad
X=1+\sum_{a\ne0}x_a\chi_a,
$$

on the interior of the probability simplex. Moreover,

$$
\nabla F^*(x)_a=\widehat{\log X}(a),
$$

and

$$
\nabla^2 F^*(x)_{ab}
=
\mathbb E_U\left[\frac{\chi_a\chi_b}{X}\right]
=
\mathbb E_U\left[\frac{\chi_{a+b}}{X}\right].
$$

For a fixed orientation orthant \(\sigma\), write

$$
x=\sigma\odot u,
\qquad
u_a>0.
$$

Then the sealed point is the critical point of

$$
K_\sigma(u)
=
F^*(\sigma\odot u)
+
\sum_{a\ne0}(u_a\log u_a-u_a).
$$

Indeed,

$$
\frac{\partial K_\sigma}{\partial u_a}
=
\sigma_a\nabla F^*(\sigma\odot u)_a+\log u_a,
$$

so the critical equation is exactly

$$
\sigma_a\widehat{\log X}(a)+\log u_a=0.
$$

### 7.3 Delta Sealed Law

For the delta orientation centered at \(s_\star\),

$$
\sigma_a^\star=-\chi_a(s_\star).
$$

By symmetry all \(u_a\) are equal; write \(u_a=u\). Then

$$
X_\star(s_\star)=1-(N-1)u,
\qquad
X_\star(s)=1+u
\quad(s\ne s_\star).
$$

The log-ratio condition gives

$$
\frac{1-(N-1)u}{1+u}=u^N,
$$

or equivalently

$$
\boxed{
u^{N+1}+u^N+(N-1)u-1=0.
}
$$

The delta gap is therefore

$$
\widehat m(\epsilon_\star)
=
\frac1N(1-(N-1)u)\log(1-(N-1)u)
+
\frac{N-1}{N}(1+u)\log(1+u),
$$

where \(u\) is the root above. As \(N\) grows, \(u\sim 1/(N-1)\), so the
sealed delta law is almost uniform on \(N-1\) states and almost zero at the
deep state.

### 7.4 What Does Not Work

Two tempting routes fail.

First, the pointwise-depth lemma is insufficient: it only identifies the
unique field that attains value \(-(N-1)\), but global optimality is an
entropy statement about the self-consistent sealed law.

Second, ordinary majorization of the unsealed value vector cannot prove the
result. The delta value vector is

$$
(1,1,\dots,1,-(N-1)),
$$

while the all-plus orientation has value vector

$$
(N-1,-1,\dots,-1).
$$

Sorted decreasingly, these vectors are not ordered in the required
majorization direction. The seal map sees the full Fourier sign pattern, not
just the sorted multiset of field values.

Likewise, a fixed-\(h\) free-energy comparison is not enough. For equal
positive \(h\), the all-plus orientation has larger log-partition function
than the delta orientation. Delta wins only after the self-consistent seal
moves its equilibrium correlations \(u_a\) much closer to zero.

### 7.5 Cocycle Defects And The Correct Sign Convention

The Walsh characters multiply by

$$
\chi_a\chi_b=\chi_{a+b}.
$$

Expanding \(F^*(x)\) around the uniform density, with

$$
\delta(s)=\sum_{a\ne0}x_a\chi_a(s),
\qquad
X=1+\delta,
$$

gives

$$
(1+\delta)\log(1+\delta)
=
\delta+\frac12\delta^2-\frac16\delta^3+\frac1{12}\delta^4-\cdots .
$$

The quadratic term is blind to orientation:

$$
\frac12\mathbb E_U[\delta^2]
=
\frac12\sum_a x_a^2.
$$

The first sign-sensitive term is cubic:

$$
-\frac16
\sum_{\substack{a,b\ne0\\a\ne b}}
x_a x_b x_{a+b}.
$$

Writing \(x_a=\sigma_a u_a\), the natural delta-gauge line invariant is

$$
\kappa_{a,b}=-\sigma_a\sigma_b\sigma_{a+b}.
$$

For a delta orientation, \(\kappa_{a,b}=+1\) on every Walsh line
\(\{a,b,a+b\}\). In this convention,

$$
F^*(\sigma\odot u)
=
\frac12\sum_a u_a^2
+
\frac16
\sum_{\substack{a,b\ne0\\a\ne b}}
\kappa_{a,b}u_a u_b u_{a+b}
+
O(u^4).
$$

This perturbative expansion explains where the cocycle defects enter, but it
cannot by itself prove the theorem. Near the delta law, the density approaches
the boundary of the simplex at \(s_\star\), and higher derivatives of \(F^*\)
involve powers of \(1/X\). Thus the Taylor tail is not uniformly controlled.

### 7.6 Synchronous Relaxed Melt To Delta

Fix a delta orientation \(\sigma^\star\). For any orientation \(\sigma\),
write the relative sign pattern

$$
\tau_a=\frac{\sigma_a}{\sigma_a^\star}\in\{-1,+1\}.
$$

The defect set is

$$
M=\{a:\tau_a=-1\}.
$$

Instead of trying to flip individual Walsh lines, which is not compatible with
the global coboundary structure, relax all coefficient defects synchronously:

$$
\lambda_a(t)=(1-t)\tau_a+t,
\qquad
0\le t\le1.
$$

Then

$$
\lambda_a(0)=\tau_a,
\qquad
\lambda_a(1)=1,
$$

and

$$
\dot\lambda_a=1-\tau_a
=
\begin{cases}
0,&a\notin M,\\
2,&a\in M.
\end{cases}
$$

Let

$$
S(t)=\operatorname{diag}(\sigma^\star\odot\lambda(t)),
\qquad
x(t)=S(t)u(t),
\qquad
X(t)=1+\sum_{a\ne0}x_a(t)\chi_a.
$$

The relaxed sealed point is defined by the critical equation

$$
Sg+\log u=0,
\qquad
g=\nabla F^*(x)=\widehat{\log X}.
$$

Set

$$
H=\nabla^2F^*(x),
\qquad
H_{ab}=
\mathbb E_U\left[\frac{\chi_a\chi_b}{X}\right],
$$

and

$$
A=\operatorname{diag}(1/u)+S H S.
$$

The matrix \(H\) is a weighted Walsh Gram matrix:

$$
z^T H z
=
\mathbb E_U\left[
\frac{\left(\sum_a z_a\chi_a\right)^2}{X}
\right]
>0.
$$

It is positive definite, but it is not generally a graph Laplacian or an
M-matrix; no entrywise sign pattern of \(H^{-1}\) should be expected.

Differentiating the relaxed seal equation gives

$$
\boxed{
A\dot u
=
-\dot S\,g
-S H(\dot S\,u).
}
$$

The relative entropy along the path is

$$
D(t)=F^*(S(t)u(t)).
$$

Since \(Sg=-\log u\),

$$
D'(t)
=
g^T\dot S\,u
+
(Sg)^T\dot u.
$$

Let

$$
\alpha=Sg=-\log u,
\qquad
\eta=A^{-1}\alpha.
$$

Then \(D'(t)\le0\) is equivalent to the nonnegativity of the certificate

$$
\operatorname{Cert}
=
\alpha^T A^{-1}
\left(\dot S\,g+S H(\dot S\,u)\right)
-g^T\dot S\,u.
$$

Using the state-space representation of \(H\), this becomes

$$
\operatorname{Cert}
=
\sum_a\dot S_a g_a(\eta_a-u_a)
+
\mathbb E_U\left[
\frac{(CS\eta)(C\dot S\,u)}{X}
\right],
$$

where \(C\) is the nonconstant Walsh matrix.

### 7.7 Collapse To A Local Defect-Cone Certificate

The mixed state-space term can be eliminated algebraically. Away from
coordinates where \(S_a=0\), set

$$
v=S^{-1}\dot S\,u.
$$

Since \(A\eta=\alpha=Sg\),

$$
v^T A\eta=v^T\alpha.
$$

Expanding the left-hand side gives

$$
v^T A\eta
=
\sum_a\frac{\dot S_a}{S_a}\eta_a
+
\mathbb E_U\left[
\frac{(C\dot S\,u)(CS\eta)}{X}
\right],
$$

while the right-hand side is

$$
v^T\alpha
=
\sum_a\dot S_a u_a g_a.
$$

Therefore

$$
\mathbb E_U\left[
\frac{(C\dot S\,u)(CS\eta)}{X}
\right]
=
\sum_a\dot S_a u_a g_a
-
\sum_a\frac{\dot S_a}{S_a}\eta_a.
$$

Substituting this identity into the certificate cancels the \(u\)-terms and
leaves the local expression

$$
\operatorname{Cert}
=
\sum_a\dot S_a\eta_a
\left(g_a-\frac1{S_a}\right).
$$

Equivalently, write

$$
\eta=S\beta.
$$

Then

$$
\boxed{
\operatorname{Cert}
=
\sum_a\dot S_a\beta_a(\alpha_a-1).
}
$$

The apparent singularity at \(S_a=0\) is removable. Instead of defining
\(\beta=\eta/S\) by division, define \(\beta\) as the solution of the regular
equation

$$
\boxed{
\operatorname{diag}(1/u)\beta
+
H S^2\beta
=
g.
}
$$

This equation remains meaningful through the zero-crossing of the relaxed
sign multiplier.

At this stage it is natural to ask for the pointwise monotonicity inequality

$$
\boxed{
\sum_a\dot S_a\beta_a(\alpha_a-1)\ge0.
}
$$

Since \(\dot S\) is supported exactly on the defect set \(M\), this is a
localized condition. In the common gauge where the delta target has
\(\dot S_a=-2\) on \(M\), it becomes

$$
\boxed{
\sum_{a\in M}\beta_a(1-\alpha_a)\ge0.
}
$$

Proving this inequality for every orientation, every \(t\in[0,1]\), and the
corresponding relaxed sealed solution would imply

$$
D(0)\ge D(1),
$$

that is,

$$
\widehat m(\epsilon)\ge \widehat m(\epsilon_\star).
$$

Strictness should follow unless \(M=\varnothing\), i.e. unless the orientation
is already in the delta orbit.

Section 46 records the correction: this pointwise defect-cone theorem is
false. The scalar all-active relaxed branch passes through the uniform law,
whose entropy gap is below the delta endpoint. Thus the relaxed melt need not
be monotone toward delta. The formula above remains the correct local
certificate for a monotonicity attempt, but it is not a valid global theorem.

### 7.8 The Remaining Theorem

The original monotonicity route would have reduced the problem to a weighted
Walsh cone-preservation theorem.

Partition the coefficient set into the active defect coordinates \(M\) and
the passive coordinates \(R\). The passive coordinates are not discarded; they
are optimally enslaved through the weighted Walsh metric. For example, in the
\(\eta\)-coordinates the relevant Schur complement is defined by

$$
z_M^T A_{\rm eff} z_M
=
\inf_{z_R}
\left[
\sum_a\frac{z_a^2}{u_a}
+
\mathbb E_U
\frac{(CSz)^2}{X}
\right].
$$

This is not an ordinary Walsh projection: the projection is weighted by both
the diagonal seal penalty \(1/u_a\) and the state-space barrier \(1/X(s)\).

The candidate theorem was:

**Candidate Defect-Cone Theorem.** Along the synchronous relaxed melt from any
orientation to any delta orientation, let \(u,X,H,\alpha,\beta\) be defined by
the relaxed sealed equations above. Then

$$
\sum_a\dot S_a\beta_a(\alpha_a-1)\ge0,
$$

with equality only when no coefficient is melting.

This candidate cannot follow from generic positive-definiteness of \(A\), and
it cannot follow from a simple M-matrix or graph-Laplacian argument. Section
46 shows something stronger: the candidate itself is false as a pointwise
statement. Hence the proof cannot proceed by integrating a monotone relaxed
flow. The weighted Walsh Gram representation

$$
H=\frac1N C^T\operatorname{diag}(1/X)C
$$

together with the synchronous support structure of \(\dot S\) remains useful
for endpoint identities, but not as a pointwise DCT theorem.

### 7.9 Numerical Sanity Checks

Direct numerical solution of the seal equations gives:

$$
\begin{array}{c|c|c}
n & \widehat m(\epsilon_\star) & \text{next observed gap}\\
\hline
2 & 0.266653365 & 0.459889495\\
3 & 0.133530982 & 0.595770419\\
4 & 0.064538522 & 0.328047800
\end{array}
$$

For \(n=2,3,4\), exhaustive enumeration of all orientations shows the delta
orbit is the unique minimizer up to the expected spin-flip orbit. Exhaustive
checks for some relaxed synchronous paths in \(n=3,4\) showed monotone
decrease of \(D(t)\) toward delta, but Section 46 shows that such monotonicity
cannot hold as a pointwise theorem on all relaxed branches. The exhaustive
orientation computations remain evidence for endpoint delta optimality, not
for DCT.

## 8. Schur Complement Reduction Of The Defect Cone

The defect-cone certificate can be localized further by eliminating the
passive coordinates in the regular \(\beta\)-equation. This gives a sharper
finite-dimensional target, but it also shows why naive entrywise sign
arguments are not enough.

### 8.1 Block Form Of The Regularized Equation

Recall the regular equation

$$
\operatorname{diag}(1/u)\beta+H S^2\beta=g.
$$

Let \(M=\{a:\tau_a=-1\}\) be the active defect set and let \(R\) be its
complement. Along the synchronous melt,

$$
\lambda_a(t)=1\quad(a\in R),
\qquad
\lambda_a(t)=q(t)=2t-1\quad(a\in M).
$$

Therefore

$$
S_R^2=I_R,
\qquad
S_M^2=q^2 I_M.
$$

This statement uses only \(S^2\), so it is independent of the signs of the
chosen delta orientation \(\sigma^\star\).

Write

$$
U_M=\operatorname{diag}(u_a:a\in M),
\qquad
U_R=\operatorname{diag}(u_a:a\in R).
$$

In block form the regular equation is

$$
\begin{pmatrix}
U_M^{-1}+q^2H_{MM} & H_{MR}\\
q^2H_{RM} & U_R^{-1}+H_{RR}
\end{pmatrix}
\begin{pmatrix}
\beta_M\\
\beta_R
\end{pmatrix}
=
\begin{pmatrix}
g_M\\
g_R
\end{pmatrix}.
$$

Set

$$
B_R=U_R^{-1}+H_{RR}.
$$

Since \(U_R^{-1}>0\) and \(H_{RR}\ge0\), the matrix \(B_R\) is strictly
positive definite. The passive coordinates are therefore determined by

$$
\beta_R
=
B_R^{-1}\left(g_R-q^2H_{RM}\beta_M\right).
$$

Substituting this into the active block gives the exact effective equation

$$
\boxed{
\left(U_M^{-1}+q^2\widetilde H_{MM}\right)\beta_M
=
\widetilde g_M,
}
$$

where

$$
\boxed{
\widetilde H_{MM}
=
H_{MM}-H_{MR}B_R^{-1}H_{RM},
}
$$

and

$$
\boxed{
\widetilde g_M
=
g_M-H_{MR}B_R^{-1}g_R.
}
$$

The matrix \(\widetilde H_{MM}\) is the weighted Walsh Schur complement seen
by the defect set after the passive coordinates have been optimally enslaved.
It is positive semidefinite: since \(B_R=U_R^{-1}+H_{RR}\ge H_{RR}\), one has
\(B_R^{-1}\le H_{RR}^{-1}\) when \(H_{RR}\) is invertible, and the usual Schur
complement of \(H\) is nonnegative. The singular case follows by the standard
regularization \(H_{RR}\mapsto H_{RR}+\varepsilon I\) and
\(\varepsilon\downarrow0\).

Thus the active operator

$$
U_M^{-1}+q^2\widetilde H_{MM}
$$

is strictly positive definite for every \(q\), including \(q=0\).

### 8.2 Effective Defect-Cone Target

The certificate from Section 7 is

$$
\operatorname{Cert}
=
\sum_a\dot S_a\beta_a(\alpha_a-1),
\qquad
\alpha=-\log u.
$$

Since \(\dot S\) is supported on \(M\), the Schur complement rewrites the
candidate pointwise monotonicity theorem as

$$
\boxed{
\left\langle
\dot S_M\odot(\alpha_M-1),
\left(U_M^{-1}+q^2\widetilde H_{MM}\right)^{-1}
\widetilde g_M
\right\rangle
\ge0.
}
$$

Equivalently, in any gauge where \(\dot S_a=-2\) on \(M\), this is

$$
\boxed{
\left\langle
\beta_M,
1-\alpha_M
\right\rangle
\ge0,
\qquad
\beta_M=
\left(U_M^{-1}+q^2\widetilde H_{MM}\right)^{-1}
\widetilde g_M.
}
$$

This is the localized defect-cone theorem in effective coordinates.

### 8.3 Why The Obvious Sign Proof Still Fails

The Schur complement is a genuine reduction, but it does not by itself prove
the sign of the cone pairing. Several tempting shortcuts fail.

First, the entries of \(1-\alpha_M\) do not have a fixed sign along the whole
path. At the delta endpoint and for \(N\ge4\), the delta value has
\(\alpha=\log(N-1)>1\). But along a general relaxed path the active
coordinates can have \(\alpha_a<1\). In particular, at the zero crossing
\(q=0\), the critical equation

$$
Sg+\log u=0
$$

forces \(u_a=1\) for \(a\in M\), hence

$$
\alpha_a=0
\qquad(a\in M).
$$

So no proof can rely on a permanent entrywise inequality
\(1-\alpha_a<0\).

Second, the effective source

$$
\widetilde g_M=g_M-H_{MR}B_R^{-1}g_R
$$

has no guaranteed entrywise sign. The matrix \(H\) is a weighted Walsh Gram
matrix, not an M-matrix. Thus \(H_{MR}B_R^{-1}\) is not a positive
transmission operator in the entrywise sense, and the subtraction above need
not push \(\widetilde g_M\) into a fixed orthant.

Third, the resolvent expansion

$$
\left(I+q^2 U_M\widetilde H_{MM}\right)^{-1}
=
\sum_{k\ge0}(-q^2 U_M\widetilde H_{MM})^k
$$

is not a uniform proof of sign preservation. It requires a norm bound
\(\|q^2U_M\widetilde H_{MM}\|<1\), and even when such a bound holds locally,
the matrix \(U_M\widetilde H_{MM}\) need not have an entrywise sign pattern
that preserves orthants. Moreover, near the boundary of the probability
simplex the entries of \(H\) can become large because they contain the weight
\(1/X(s)\), so the diagonal penalty \(U_M^{-1}\) does not uniformly dominate
the weighted Walsh term.

Finally, the zero crossing \(q=0\) is regular, but not because \(g_M\)
diverges. Rather, \(x_M=S_Mu_M=0\), the entropy penalty forces
\(u_M\to1\), and \(g_M=\widehat{\log X}_M\) remains finite as long as the
relaxed density \(X\) remains in the interior. The effective equation simply
collapses to

$$
\beta_M=U_M\widetilde g_M
\qquad(q=0).
$$

### 8.4 The Sharpened Remaining Problem

After the Schur complement, the pointwise monotonicity route would be reduced
to the following weighted Walsh cone statement.

**Candidate Effective Defect-Cone Theorem.** Along the synchronous relaxed
melt from any orientation to a delta orientation, the solution

$$
\beta_M=
\left(U_M^{-1}+q^2\widetilde H_{MM}\right)^{-1}
\widetilde g_M
$$

satisfies

$$
\left\langle
\dot S_M\odot(\alpha_M-1),
\beta_M
\right\rangle
\ge0
$$

for every \(t\in[0,1]\), with equality only when \(M=\varnothing\).

This is stronger and more localized than the original entropy extremization
problem, but Section 46 shows that it is false as a pointwise theorem. The
Schur complement remains an exact representation of the monotonicity
certificate, and it explains why ordinary positive definiteness is
insufficient. It is not the remaining endpoint theorem. The surviving closure
target is RAC/GERAB, which is an endpoint cut-family inequality rather than a
pointwise relaxed-flow inequality.

The exact operator still uses the special representation

$$
H=\frac1N C^T\operatorname{diag}(1/X)C
$$

and the synchronous structure \(S_M^2=q^2I_M\), together with the sealed
critical equation \(Sg+\log u=0\).

## 9. Quotient-Fiber Architecture And Boundary Sign Cone

This section records the next reduction. The goal is not to claim that the
global theorem is finished. Rather, it isolates the remaining obstruction at
the correct logarithmic scale and shows how boundary collapses are constrained
by a rigid Walsh sign cone.

### 9.1 Structured Core And Quotient Density

Let \(L\subseteq M\cup\{0\}\) be a structured active core, assumed here to be
a linear subspace containing \(0\). Set

$$
H=L^\perp.
$$

The quotient \(G/H\) has dual group \(L\). For a coset \(y+H\), define the
coarse density

$$
\bar X(y)=\mathbb E_{h\in H}X(y+h).
$$

The density Gram matrix restricted to \(L\) diagonalizes on the quotient. Its
eigenvalues are exactly the coset averages \(\bar X(y)\). Thus, in the
structured-core regime, controlling \(K_{LL}^{-1}\) is equivalent to proving
that the relevant coset densities do not collapse, except possibly along the
delta-aligned boundary channel.

### 9.2 Exact Fiber Decomposition

Let

$$
c=\mathbb E_U[\log X].
$$

Decompose the log-density into quotient and fiber pieces:

$$
\log X(y+h)=c+W_L(y)+V_y(h),
$$

where

$$
W_L(y)=\sum_{\ell\in L\setminus\{0\}}g_\ell\chi_\ell(y).
$$

Frequencies outside \(L\) are grouped into cosets of the dual group modulo
\(L\). If \(\rho\) denotes a nonzero class in \(\widehat G/L\), then all
frequencies \(\rho+\ell\), \(\ell\in L\), restrict to the same fiber
character on \(H\). Write this character as \(\psi_\rho\). Then

$$
V_y(h)=\sum_{\rho\ne0}A_\rho(y)\psi_\rho(h),
$$

with aliased fiber amplitudes

$$
A_\rho(y)=
\sum_{\ell\in L}
g_{\rho+\ell}\chi_{\rho+\ell}(y).
$$

The exact fiber free energy is

$$
\Lambda_H(A(y))
=
\log Z_H(y)
=
\log\mathbb E_{h\in H}
\exp\left(\sum_{\rho\ne0}A_\rho(y)\psi_\rho(h)\right).
$$

Consequently,

$$
\boxed{
\log \bar X(y)
=
c+W_L(y)+\Lambda_H(A(y)).
}
$$

It is useful to define the total quotient potential

$$
\Phi_L(y)=W_L(y)+\Lambda_H(A(y)).
$$

Then

$$
\bar X(y)=e^{c+\Phi_L(y)}.
$$

### 9.3 Reverse-KL Jensen Buffer

Jensen's inequality gives

$$
\log \bar X(y)
\ge
\mathbb E_{h\in H}[\log X(y+h)].
$$

In fact the gap is exact. If \(U_{y+H}\) is uniform on the coset and
\(P(\cdot\mid y+H)\) is the conditional sealed law on that coset, then

$$
\boxed{
\log \bar X(y)
=
\mathbb E_{h\in H}[\log X(y+h)]
+
D(U_{y+H}\|P(\cdot\mid y+H)).
}
$$

The divergence is the reverse conditional KL, not the forward KL. Since the
projection of \(\log X\) onto the quotient keeps precisely the \(L\)-modes,

$$
\mathbb E_{h\in H}[\log X(y+h)]
=
c+W_L(y).
$$

Thus the fiber free energy is exactly the reverse-KL/Jensen buffer:

$$
\Lambda_H(A(y))
=
D(U_{y+H}\|P(\cdot\mid y+H)).
$$

This identity is exact but, by itself, tautological. It identifies the
correct scale of the problem; it does not yet prove a lower bound.

### 9.4 Projected Sealed Equations

The quotient-fiber decomposition gives the exact projected seal system.
For \(\ell\in L\),

$$
\boxed{
x_\ell
=
e^c\mathbb E_{y\in G/H}
\left[
e^{\Phi_L(y)}\chi_\ell(y)
\right].
}
$$

For an off-quotient class \(\rho\ne0\), define the physical fiber moment

$$
m_\rho(y)
=
\partial_{A_\rho}\Lambda_H(A(y))
=
\mathbb E_{\nu_y}[\psi_\rho],
$$

where

$$
d\nu_y(h)
=
\frac{e^{V_y(h)}}{Z_H(y)}\,dU_H(h).
$$

Then for every \(\ell\in L\),

$$
\boxed{
x_{\rho+\ell}
=
e^c\mathbb E_{y\in G/H}
\left[
e^{\Phi_L(y)}
m_\rho(y)
\chi_{\rho+\ell}(y)
\right].
}
$$

These equations must be used together with the scalar seal

$$
\boxed{
x_a=S_a e^{-S_ag_a}.
}
$$

The remaining structured-core problem is therefore a maximum-principle or
observability statement for the quotient potential \(\Phi_L\) under this
projected sealed system:

$$
\boxed{
\min_y\Phi_L(y)\ge -C_L
}
$$

away from the delta-aligned boundary channel. Proving this gives a coset
floor for \(\bar X\) and hence controls the structured block of the density
Gram matrix without using the pointwise bound \(\min_s X(s)\).

### 9.5 Positive Poisson Sieve

Direct Fourier inversion of \(\Phi_L\) is the wrong scale, since
\(\Phi_L\) contains the nonlinear free energy \(\Lambda_H(A)\). Instead use
positive quotient kernels.

Let \(d=\dim L\), \(Q=2^d=|G/H|\), and choose a quotient basis. For
\(0<r<1\), define the Boolean Poisson kernel

$$
P_r(y,y_0)
=
\sum_{\ell\in L}r^{|\ell|}\chi_\ell(y)\chi_\ell(y_0)
=
\prod_{i=1}^d(1+r\,\eta_i(y)\eta_i(y_0)).
$$

Here \(|\ell|\) is Hamming weight in the chosen quotient basis. The kernel is
strictly positive and has mean one under the uniform quotient measure.

Define the smoothed quotient density

$$
D_r(y_0)
=
\mathbb E_y[\bar X(y)P_r(y,y_0)]
=
1+\sum_{\ell\in L\setminus\{0\}}
r^{|\ell|}\chi_\ell(y_0)x_\ell.
$$

After fixing quotient representatives, the corresponding vector probes have
the form

$$
V_{r,\rho}(y_0)
=
\sum_{\ell\in L}
r^{|\ell|}\chi_\ell(y_0)x_{\rho+\ell},
$$

up to the harmless fixed section character for the class \(\rho\). Since
\(|m_\rho(y)|\le1\), the projected off-quotient equations imply the
confinement estimate

$$
\boxed{
|V_{r,\rho}(y_0)|\le D_r(y_0)
\qquad(\rho\ne0).
}
$$

Thus any collapse of the smoothed scalar mass forces all smoothed
off-quotient packets to collapse simultaneously.

### 9.6 Smoothed Vanishing Exclusion And Pointwise Bridge

The needed non-tautological theorem is a smoothed vanishing exclusion:

$$
\boxed{
D_r(y_0)\ge\delta_{L,r}>0
}
$$

for every non-delta-aligned coset \(y_0+H\), with constants strong enough as
\(r\to1\). The trivial positivity of the Poisson kernel only gives
\(\delta_{L,r}\ge(1-r)^d\), which decays too quickly to imply a pointwise
floor. The seal must supply a stronger exclusion of synchronized vanishing.

Once such a bound is known, the passage from smoothed mass to pointwise mass
does not require a Harnack inequality. Let

$$
p_0=\frac{P_r(y_0,y_0)}{Q}
=
\left(\frac{1+r}{2}\right)^d.
$$

Since \(\bar X\ge0\) and \(\mathbb E_y\bar X(y)=1\), one has

$$
0\le \bar X(y)\le Q.
$$

Therefore

$$
D_r(y_0)
\le
p_0\bar X(y_0)+(1-p_0)Q.
$$

If \(r\) is chosen so that

$$
(1-p_0)Q\le\frac12\delta_{L,r},
$$

then

$$
\boxed{
\bar X(y_0)\ge\frac{\delta_{L,r}}{2p_0}.
}
$$

This gives the desired pointwise coset floor without differentiating the
possibly singular log-potential.

### 9.7 Tropical Boundary Sign Cone

The natural way to attack the smoothed vanishing exclusion is to classify
possible boundary limits of sealed densities.

Suppose \(X_j\to X_\infty\ge0\) and let \(Z=\{s:X_\infty(s)=0\}\). Let
\(M_j\to\infty\) be a scale on which \(-\log X_j\) diverges on \(Z\).
After passing to a subsequence,

$$
-\frac{\log X_j}{M_j}\to w,
$$

where \(w\ge0\) is supported on \(Z\). Hence the diverging part of the
log-force is

$$
g_a^{\rm div}
\sim
-M_j\widehat w(a).
$$

Since

$$
x_a=S_a e^{-S_ag_a}
$$

must remain bounded, it is impossible for \(S_ag_a\to-\infty\). Therefore
every diverging Fourier direction must satisfy the boundary sign-cone
condition

$$
\boxed{
S_a\widehat w(a)\le0.
}
$$

For a pure coset collapse \(Z=y_0+H\), take \(w=\mathbf 1_Z\). Then

$$
\widehat{\mathbf 1_Z}(\ell)
=
\frac1Q\chi_\ell(y_0)
\qquad(\ell\in L),
$$

and the transform vanishes off \(L\).

On the delta side of the melt, where \(q=2t-1>0\) and

$$
S_\ell=q\sigma_\ell^\star
=
-q\chi_\ell(s_\star)
\qquad(\ell\in L\setminus\{0\}),
$$

the sign cone becomes

$$
\left(-q\chi_\ell(s_\star)\right)
\left(\frac1Q\chi_\ell(y_0)\right)\le0.
$$

Equivalently,

$$
\chi_\ell(y_0+s_\star)=1
\qquad(\ell\in L\setminus\{0\}).
$$

Thus

$$
y_0+s_\star\in L^\perp=H,
$$

or

$$
\boxed{
y_0+H=s_\star+H.
}
$$

In words: on the delta side of the synchronous melt, the boundary sign cone
forbids the collapse of any structured quotient coset except the coset
containing the target delta spike.

This is the main boundary classification. It converts the analytic threat of
macroscopic coset collapse into a finite Walsh sign-cone obstruction.

### 9.8 The Allowed Delta Channel

The target coset \(s_\star+H\) is not buoyed by the preceding argument. It is
the allowed boundary channel. This is not a defect of the proof: in the full
delta endpoint, the density really does approach zero at the delta spike.

Thus the structured-core proof must split into two cases.

First, every spurious coset collapse is excluded by the sign-cone boundary
classification, giving the needed smoothed vanishing exclusion and hence the
coset floor.

Second, the delta-aligned channel must be handled by an explicit reduced
delta comparison. Along this channel the limiting degeneration is in the
delta orbit, and the sealed law is governed by the scalar delta equation

$$
\frac{1-(N-1)u}{1+u}=u^N.
$$

The remaining task is to verify that motion into this allowed channel has gap
bounded below by the delta endpoint, not below it.

### 9.9 Current Conditional Endpoint

The present reduction can be summarized as follows.

**Conditional Endpoint.** Global delta optimality follows if:

1. the endpoint residual closure cut RAC/GERAB holds once all structured and
   pseudorandom components are combined;
2. the smoothed vanishing exclusion \(D_r(y_0)\ge\delta_{L,r}\) is proved for
   every non-delta-aligned structured core coset, with constants compatible
   with the pointwise bridge;
3. the only remaining boundary channel is the delta-aligned channel, and its
   reduced comparison gives no gap below the explicit delta value.

The strongest new structural fact is the tropical sign-cone classification:
near the simplex boundary, the seal permits only zero sets whose Walsh
spectra lie in the sign cone \(S_a\widehat w(a)\le0\). For structured coset
collapse on the delta side of the melt, this sign cone allows exactly the
delta-aligned coset and excludes every spurious coset.

## 10. Interior Density-Side Schur Complement

This section records the current endpoint of the interior proof search. The
boundary architecture above removes the macroscopic vanishing threat, so the
remaining problem can be stated as a finite-dimensional matrix inequality in
the interior. The point of the reduction is to keep the exact Walsh group law
visible and to avoid Taylor expanding the singular weight \(1/X\).

### 10.1 Target Gauge And Symmetric Response

Translate the target spike to the identity, so that

$$
\chi_a(s_\star)=1
\qquad(a\ne0),
$$

and therefore the delta orientation has \(\sigma_a^\star=-1\). On the
delta side of the synchronous melt write

$$
q=2t-1>0.
$$

In this gauge the sealed Fourier coefficients have the two-tier form

$$
x_c=
\begin{cases}
1,&c=0,\\
-u_c,&c\in R,\\
-q u_c,&c\in M.
\end{cases}
$$

The signs have now been isolated, and the symmetric quadratic response uses
only

$$
\widetilde S=\operatorname{diag}(q I_M,I_R).
$$

All response variables in this section are written in these delta-signed
symmetric coordinates; the fixed delta signs are carried by the density
coefficients \(x_c\), while the quadratic response sees \(\widetilde S\).

In \(\eta\)-coordinates, with

$$
z=\eta_M=q\beta_M,
$$

the global mobility matrix is

$$
A
=
\operatorname{diag}(1/u)+\widetilde S H\widetilde S
=
\begin{pmatrix}
U_M^{-1}+q^2H_{MM} & qH_{MR}\\
qH_{RM} & B_R
\end{pmatrix},
$$

where

$$
B_R=U_R^{-1}+H_{RR}.
$$

The true relaxed response satisfies the symmetric equation

$$
A\eta=\alpha.
$$

Equivalently, for a prescribed active vector \(z\), the passive harmonic
completion is

$$
\boxed{
\eta_R=B_R^{-1}\left(\alpha_R-qH_{RM}z\right).
}
$$

This is the affine lift that absorbs the passive Schur transmission into a
global energy identity.

### 10.2 Exact State-Space Residual

Define the active, passive, and total response fields

$$
Z(s)=\sum_{a\in M}z_a\chi_a(s),
\qquad
P(s)=\sum_{b\in R}\eta_b\chi_b(s),
$$

and

$$
Y(s)=qZ(s)+P(s).
$$

Since \(s_\star\) is the identity in this gauge,

$$
Z(s_\star)=\sum_{a\in M}z_a.
$$

The active block of \(A\eta=\alpha\) gives, for \(a\in M\),

$$
\alpha_a
=
\frac{z_a}{u_a}
+q\mathbb E_U\left[\frac{\chi_aY}{X}\right].
$$

Pairing this equation with \(z\) gives the exact identity

$$
q\left\langle\beta_M,1-\alpha_M\right\rangle
=
Z(s_\star)
-z^TU_M^{-1}z
-q\mathbb E_U\left[\frac{ZY}{X}\right].
$$

Splitting \(Y=qZ+P\) and then using the passive equation gives the equivalent
residual form

$$
\boxed{
Z(s_\star)
-z^TU_M^{-1}z
-q^2\mathbb E_U\left[\frac{Z^2}{X}\right]
+\eta_R^TB_R\eta_R
-\eta_R^T\alpha_R
\ge0.
}
$$

This is exactly the original defect-cone inequality, but expressed on the
global harmonic response. The passive term should not be treated as
unconditionally positive. In fact the passive block equation gives

$$
\boxed{
\eta_R^TB_R\eta_R-\eta_R^T\alpha_R
=
-q\,\eta_R^TH_{RM}z.
}
$$

Thus the passive modes are a coupled transmission channel, not a free
stabilizing reservoir.

### 10.3 Inverting The Density Gram Matrix

The state-space penalty can be rewritten without expanding \(1/X\). Include
the zero frequency, set

$$
w_c=\widehat{1/X}(c),
$$

and define the full convolution matrices

$$
K_X=(x_{a+b})_{a,b\in\mathbb F_2^n},
\qquad
W=(w_{a+b})_{a,b\in\mathbb F_2^n}.
$$

Since \(X\cdot(1/X)=1\), the Fourier coefficients obey

$$
\sum_{d\in\mathbb F_2^n}x_dw_{c+d}
=
\mathbf 1_{c=0}.
$$

Equivalently,

$$
\boxed{
K_XW=I.
}
$$

This is the exact replacement for any conjugate-density or Taylor-series
heuristic: the inverse-density Walsh matrix is the inverse of the true
density Walsh matrix.

Partition the full frequency space as

$$
\mathbb F_2^n=M\sqcup\bar R,
\qquad
\bar R=R\cup\{0\}.
$$

Since \(X>0\) in the interior, \(K_X\) is strictly positive definite. Its
active Schur complement is

$$
\boxed{
\mathcal K_M
=
K_{MM}-K_{M\bar R}K_{\bar R\bar R}^{-1}K_{\bar RM}.
}
$$

The active block of \(W=K_X^{-1}\) is therefore

$$
\boxed{
W_{MM}=\mathcal K_M^{-1}.
}
$$

Consequently,

$$
\boxed{
\mathbb E_U\left[\frac{Z^2}{X}\right]
=
z^T\mathcal K_M^{-1}z.
}
$$

Every entry of \(K_X\) is now controlled by the sealed coefficients

$$
x_c=
\begin{cases}
1,&c=0,\\
-u_c,&c\in R,\\
-q u_c,&c\in M.
\end{cases}
$$

Thus the singular-looking \(1/X\) term has been transferred to a
finite-dimensional Schur complement built directly from the density.

### 10.4 Density-Side Cone Target

Combining the state-space residual with the density-side Schur complement
gives an exact density-side form of the pointwise monotonicity candidate.

**Candidate Density-Side Schur Complement Cone Theorem.** Along the delta side
of the synchronous relaxed melt, for the true response \(z=q\beta_M\) and its
passive harmonic completion \(\eta_R\),

$$
\boxed{
\sum_{a\in M}z_a
-z^TU_M^{-1}z
-q^2z^T\mathcal K_M^{-1}z
+\eta_R^TB_R\eta_R
-\eta_R^T\alpha_R
\ge0.
}
$$

This candidate is equivalent to the effective defect-cone inequality

$$
\left\langle\beta_M,1-\alpha_M\right\rangle\ge0
$$

for \(q>0\), and the zero crossing \(q=0\) is handled by the regular limiting
equation already isolated in Section 8. Section 46 shows that this pointwise
sign statement is false on the scalar all-active branch. The identity remains
useful as an exact residual formula, not as a global monotonicity theorem.

Substituting the active response equation directly into the trace
\(\sum_{a\in M}z_a\) merely returns the original cone pairing
\(\langle z,1-\alpha_M\rangle\). It is therefore a useful consistency check,
but not by itself a sign proof.

The next structural input should be the subgroup-face decomposition of
\(\mathcal K_M\). In the target gauge the all-ones vector is the exact
point-evaluation eigenvector:

$$
K_X\mathbf 1=X(s_\star)\mathbf 1.
$$

After the split \(M\sqcup\bar R\), this identity relates the active trace
\(Z(s_\star)\) to the Schur complement geometry. The boundary sign-cone and
coset-floor analysis from Section 9 then identifies which subgroup faces can
produce small eigenvalues and which are excluded. The remaining
finite-dimensional route must be endpoint/cut based, not a proof of
pointwise DCT.

## 11. Delta-Side Stieltjes Route

The density-side reduction suggests a sharper proof strategy: on the delta
side, the central object should be the full density convolution matrix
\(K_X\), not the weighted Hessian \(H=\widehat{1/X}\) by itself. The reason is
that \(K_X\) has an order structure that \(H\) does not visibly have in the
original coordinates.

### 11.1 Stieltjes Structure Of \(K_X\)

In the target gauge from Section 10, on the delta side \(q>0\),

$$
x_c=
\begin{cases}
1,&c=0,\\
-u_c,&c\in R,\\
-q u_c,&c\in M.
\end{cases}
$$

Thus every nonzero Fourier coefficient of the density is nonpositive:

$$
x_c\le0
\qquad(c\ne0).
$$

The full density convolution matrix is

$$
K_X=(x_{a+b})_{a,b\in\mathbb F_2^n}.
$$

It is positive definite because, for every real vector \(v\),

$$
v^TK_Xv
=
\mathbb E_U\left[
X\left(\sum_a v_a\chi_a\right)^2
\right]>0.
$$

It also has nonpositive off-diagonal entries, since \(a\ne b\) implies
\(a+b\ne0\). Therefore \(K_X\) is a symmetric positive definite
\(Z\)-matrix, hence a Stieltjes matrix. Consequently,

$$
\boxed{
K_X^{-1}\ge0
\quad\text{entrywise}.
}
$$

Since \(W=K_X^{-1}\) and

$$
W=(\widehat{1/X}(a+b))_{a,b\in\mathbb F_2^n},
$$

this gives

$$
\boxed{
\widehat{1/X}(c)\ge0
\qquad(c\in\mathbb F_2^n).
}
$$

In particular, the original Hessian block

$$
H_{ab}=\widehat{1/X}(a+b)
$$

has nonnegative entries on the delta side. This does not make \(H\) an
\(M\)-matrix; rather, it explains why the \(K_X\)-side is the correct place to
look for cone preservation.

The same order structure passes to the active density Schur complement. With
\(\bar R=R\cup\{0\}\),

$$
\mathcal K_M
=
K_{MM}-K_{M\bar R}K_{\bar R\bar R}^{-1}K_{\bar RM}.
$$

Since \(K_{\bar R\bar R}\) is Stieltjes, \(K_{\bar R\bar R}^{-1}\ge0\).
Moreover \(K_{M\bar R}\le0\) entrywise. Hence
\(K_{M\bar R}K_{\bar R\bar R}^{-1}K_{\bar RM}\ge0\) entrywise, and
\(\mathcal K_M\) is again a Stieltjes matrix. Therefore

$$
\boxed{
\mathcal K_M^{-1}\ge0.
}
$$

This is the first concrete order-preservation result available on the
density side.

### 11.2 Logarithmic Sign Preservation

The matrix \(K_X\) is the multiplication operator by \(X\) in the Walsh basis.
Therefore functional calculus gives

$$
\log K_X=K_{\log X},
$$

where

$$
(K_{\log X})_{ab}=\widehat{\log X}(a+b).
$$

For a Stieltjes matrix \(K\), the integral representation

$$
\log K
=
\int_0^\infty
\left(
\frac{1}{1+t}I-(K+tI)^{-1}
\right)\,dt
$$

shows that the off-diagonal entries of \(\log K\) are nonpositive, because
\((K+tI)^{-1}\ge0\) entrywise for every \(t\ge0\). Applying this to \(K_X\)
gives

$$
\boxed{
g_c=\widehat{\log X}(c)\le0
\qquad(c\ne0).
}
$$

Write

$$
a_c=-g_c\ge0.
$$

For active coordinates \(c\in M\), the seal gives

$$
u_c=e^{qg_c}=e^{-qa_c},
\qquad
\alpha_c=-\log u_c=qa_c.
$$

Thus the factor \(1-\alpha_c\) appearing in the cone certificate has a scalar
origin:

$$
\frac{\partial}{\partial q}
\left(qe^{-qa_c}\right)
=
e^{-qa_c}(1-qa_c)
=
u_c(1-\alpha_c),
$$

when \(a_c\) is held fixed. The full sealed path also differentiates
\(a_c(q)\), so this identity is not yet a monotonicity proof. It identifies
the correct tangent-cone mechanism that must be controlled.

### 11.3 Stieltjes Tangent-Cone Target

The entropy can be written directly in density-matrix form:

$$
D(q)
=
\mathbb E_U[X\log X]
=
\frac1N\operatorname{Tr}(K_X\log K_X).
$$

Along the sealed synchronous melt, proving

$$
\frac{d}{dq}D(q)\le0
$$

on the delta side is equivalent to the defect-cone inequality

$$
\left\langle\beta_M,1-\alpha_M\right\rangle\ge0.
$$

This was the natural strengthened monotonicity target:

**Candidate Stieltjes Tangent-Cone Theorem.** Let \(K_X(q)\) be the delta-side
sealed Stieltjes solution. Along the active deformation \(s_c=q\) for
\(c\in M\),

$$
\boxed{
\frac{d}{dq}
\frac1N\operatorname{Tr}(K_X\log K_X)
\le0.
}
$$

The relevant derivative is the Frechet derivative

$$
D(\log)_K[\dot K]
=
\int_0^\infty
(K+tI)^{-1}\dot K(K+tI)^{-1}\,dt.
$$

Because \((K+tI)^{-1}\ge0\) entrywise, this derivative has an
order-preserving structure inside the Stieltjes cone. The remaining issue is
not generic positivity of the derivative; it is to prove that the sealed
self-consistency equation forces \(\dot K_X\) to lie in the correct tangent
cone.

Section 46 shows that this candidate is false as a pointwise theorem. On the
scalar all-active branch the relaxed path runs from the uniform law at
\(q=0\) to the delta law at \(q=1\), so \(D(q)\) increases near \(q=0\).
Thus the density-side route, if useful, must be endpoint/cut based rather
than a global pointwise tangent-cone monotonicity theorem.

### 11.4 Point-Evaluation Schur Identity

The target spike creates the only obvious small-eigenvalue channel. In the
target gauge the all-ones vector \(e\) is the point-evaluation eigenvector:

$$
K_Xe=X(s_\star)e.
$$

Split

$$
e=(e_M,e_{\bar R}),
\qquad
\mathbb F_2^n=M\sqcup\bar R.
$$

The block equations are

$$
K_{MM}e_M+K_{M\bar R}e_{\bar R}
=
X(s_\star)e_M,
$$

and

$$
K_{\bar RM}e_M+K_{\bar R\bar R}e_{\bar R}
=
X(s_\star)e_{\bar R}.
$$

Eliminating the passive block gives the exact Schur identity

$$
\boxed{
\mathcal K_Me_M
=
X(s_\star)\rho_M,
}
$$

where

$$
\boxed{
\rho_M
=
e_M-K_{M\bar R}K_{\bar R\bar R}^{-1}e_{\bar R}.
}
$$

Since \(K_{M\bar R}\le0\) and
\(K_{\bar R\bar R}^{-1}\ge0\), one has

$$
K_{M\bar R}K_{\bar R\bar R}^{-1}e_{\bar R}\le0,
$$

and therefore

$$
\boxed{
\rho_M\ge e_M>0.
}
$$

Thus \(e_M\) becomes an approximate active kernel only when
\(X(s_\star)\) is small. This is precisely the allowed delta channel. The
proof should decompose the active response into

$$
z=z_{\rm delta}+z_\perp,
$$

where \(z_{\rm delta}\) is the point-evaluation channel and \(z_\perp\) is
controlled by the transverse Stieltjes gap.

### 11.5 Delsarte Boundary Cone

The boundary sign-cone argument in Section 9 was stated for pure coset
collapse. The density-side Stieltjes picture suggests the correct quotient
limit cone.

After translating \(s_\star\) to the identity, the delta-side sign condition
on a quotient \(G/H\) becomes

$$
\widehat{\bar w}(\ell)\ge0
\qquad(\ell\in L).
$$

Together with \(\bar w\ge0\), this places every quotient-scale tropical
collapse in the Boolean Delsarte cone

$$
\boxed{
\bar w\ge0,
\qquad
\widehat{\bar w}\ge0.
}
$$

This cone is larger than the cone generated by subgroup indicators, so the
right statement is not that every Delsarte face is a subgroup face. The
needed strengthened theorem is more precise:

**Seal-Compatible Delsarte Face Theorem.** Any quotient-scale boundary
collapse compatible with the projected seal equations and the simultaneous
Poisson-packet vanishing lies in a Delsarte face generated by subgroup
channels through the target coset. Non-target faces are excluded by the sign
cone; target faces reduce to lower-dimensional delta channels.

This formulation keeps the pure Delsarte geometry separate from the
additional rigidity supplied by the seal.

### 11.6 Compactness And Delta-Channel Comparison

The smoothed vanishing exclusion can now be attacked by compactness. If, for
a non-delta-aligned coset, one had

$$
D_r(y_0)\to0,
$$

then the confinement estimate

$$
|V_{r,\rho}(y_0)|\le D_r(y_0)
$$

would force all smoothed off-quotient packets to vanish simultaneously. A
tropical limit would produce a nonzero quotient profile \(\bar w\) in the
Delsarte sign cone. The seal-compatible face theorem should then rule out
every non-delta-aligned face, giving the desired coset floor.

The only remaining boundary channel is delta-aligned. On such a face the
problem reduces to a lower-dimensional delta comparison governed by the
scalar equation

$$
\frac{1-(N-1)u}{1+u}=u^N.
$$

The remaining boundary theorem is:

**Reduced Delta-Channel Comparison.** On every subgroup face through
\(s_\star\), the restricted sealed problem has its minimum at the
lower-dimensional delta endpoint. Motion into a delta-aligned face cannot
produce entropy below the explicit full delta value.

Together, the Stieltjes tangent-cone theorem, the seal-compatible Delsarte
face theorem, and the reduced delta-channel comparison give the current
proposed route:

$$
\text{defect cone}
\Longrightarrow
\text{density-side Stieltjes flow}
\Longrightarrow
\text{point-evaluation channel plus transverse gap}
$$

$$
\Longrightarrow
\text{boundary sign cone excludes non-delta faces}
\Longrightarrow
\text{delta-aligned faces reduce to scalar delta comparison}.
$$

This promotes \(K_X\) from a bookkeeping device to the main object: on the
delta side it is a Walsh-circulant Stieltjes matrix, and its inverse
positivity, logarithmic sign preservation, and point-evaluation Schur
identity expose the likely mechanism behind the defect-cone inequality.

## 12. Proof Advances After The Stieltjes Reduction

The reductions above framed the remaining obstruction as a boundary-sensitive
Schur/combinatorial cone problem. The later proof search changes the picture
substantially.

The main advances are:

1. the scalar opposite-vs-delta endpoint comparison is closed;
2. finite-\(n\) relaxed sealed branches cannot collapse to the simplex
   boundary;
3. the transverse Schur floor follows exactly from a density floor;
4. passive coordinates can be eliminated into two active functionals;
5. the endpoint excess is an active horizontal cumulant identity in a
   Poisson-killed Walsh exponential family;
6. pointwise cubic positivity is not the right target;
7. the remaining obstruction is a delta-anchored curvature-centroid
   inequality, with a rank-one killed base case and a higher-rank domination
   problem.

These advances do not yet complete global delta optimality. They replace the
earlier boundary-oriented obstruction by an interior transfer problem.

## 13. Closed Scalar Endpoint Comparison

Let \(Q=2^d\). The scalar delta endpoint has density

$$
X_\delta(s_\star)=1-(Q-1)u,
\qquad
X_\delta(s)=1+u
\quad(s\ne s_\star),
$$

where

$$
\frac{1-(Q-1)u}{1+u}=u^Q.
$$

The opposite scalar endpoint has density

$$
X_+(s_\star)=1+(Q-1)v,
\qquad
X_+(s)=1-v
\quad(s\ne s_\star),
$$

where

$$
\frac{1-v}{1+(Q-1)v}=v^Q.
$$

Define

$$
D_\delta(u)
=
\frac1Q
\left[
(1-(Q-1)u)\log(1-(Q-1)u)
+
(Q-1)(1+u)\log(1+u)
\right],
$$

and

$$
D_+(v)
=
\frac1Q
\left[
(1+(Q-1)v)\log(1+(Q-1)v)
+
(Q-1)(1-v)\log(1-v)
\right].
$$

**Scalar Endpoint Theorem.** For every \(Q\ge4\),

$$
\boxed{
D_+(v_Q)>D_\delta(u_Q),
}
$$

with equality only in the degenerate Boolean quotient \(Q=2\).

**Proof.** First,

$$
D_\delta'(u)
=
\frac{Q-1}{Q}
\log\frac{1+u}{1-(Q-1)u}
>0.
$$

Since \(0<u_Q<1/(Q-1)\),

$$
D_\delta(u_Q)
<
D_\delta\left(\frac1{Q-1}\right)
=
\log\frac{Q}{Q-1}.
$$

For the opposite scalar equation, set

$$
f_Q(v)=\frac{1-v}{1+(Q-1)v}-v^Q.
$$

This function is strictly decreasing, and

$$
f_Q\left(\frac12\right)
=
\frac1{Q+1}-2^{-Q}>0
\qquad(Q\ge4).
$$

Thus \(v_Q>1/2\). Since

$$
D_+'(v)
=
\frac{Q-1}{Q}
\log\frac{1+(Q-1)v}{1-v}
>0,
$$

we get

$$
D_+(v_Q)>D_+\left(\frac12\right),
$$

where

$$
D_+\left(\frac12\right)
=
\frac{Q+1}{2Q}\log(Q+1)-\log2.
$$

Define

$$
h(Q)
=
\frac{Q+1}{2Q}\log(Q+1)
-\log2
-\log\frac{Q}{Q-1}.
$$

Then

$$
h'(Q)
=
\frac{
Q^2+Q-(Q-1)\log(Q+1)
}{
2Q^2(Q-1)
}
>0
\qquad(Q\ge4),
$$

and \(h(4)>0\). Hence

$$
D_+\left(\frac12\right)>
\log\frac{Q}{Q-1}.
$$

Combining the estimates gives

$$
D_+(v_Q)
>
\log\frac{Q}{Q-1}
>
D_\delta(u_Q).
$$

This closes the scalar quotient endpoint channel.

The comparison also gives a useful scale separation. For \(Q\ge4\),

$$
\frac1Q<D_\delta(Q)<\log\frac{Q}{Q-1}<\frac1{Q-1}.
$$

Thus if \(Q<N\) are powers of two, then \(N\ge2Q\), and

$$
D_\delta(Q)>\frac1Q>\frac1{N-1}>D_\delta(N).
$$

So a proper quotient delta channel has too much gap to beat the full
\(N\)-point delta endpoint.

## 14. Finite-\(n\) No-Collapse

The earlier boundary architecture is useful conceptually, but for fixed
\(n\) the relaxed sealed branches are uniformly interior.

For the minus branch in the target gauge, write

$$
S_a(r)=
\begin{cases}
-r,&a\in M,\\
-1,&a\in R,
\end{cases}
\qquad
0\le r\le1.
$$

The seal gives

$$
x_a(r)=
\begin{cases}
-r e^{r g_a(r)},&a\in M,\\
-e^{g_a(r)},&a\in R.
\end{cases}
$$

Hence \(x_a(r)\le0\) for every \(a\ne0\).

**Minus-Branch No-Collapse Theorem.** For fixed \(n\) and fixed defect set
\(M\), there is a number \(\delta_->0\) such that

$$
\boxed{
X_-(r,s)\ge\delta_-
\qquad(0\le r\le1,\ s\in G).
}
$$

**Proof sketch.** Suppose a collapsing sequence exists. After passing to a
subsequence,

$$
X_j\to X_\infty\ge0,
\qquad
\mathbb E_U X_\infty=1,
$$

with nonempty zero set. Let \(L_j\to\infty\) be a logarithmic scale such that

$$
-\frac{\log X_j}{L_j}\to w,
$$

where

$$
w\ge0,\qquad w\not\equiv0,\qquad
\operatorname{supp}w\subseteq\{X_\infty=0\}.
$$

Then

$$
g_{j,a}=\widehat{\log X_j}(a)
\sim
-L_j\widehat w(a).
$$

For passive coordinates, \(S_{j,a}=-1\) is bounded away from zero. If
\(\widehat w(a)>0\), the exponential kills the coefficient and
\(x_{\infty,a}=0\). If \(\widehat w(a)<0\), then \(x_{\infty,a}\le0\), so

$$
x_{\infty,a}\widehat w(a)\ge0.
$$

For active coordinates with \(r_j\to0\), the prefactor \(r_j\) either kills
the limiting coefficient or allows only a finite limiting contribution whose
product with \(\widehat w(a)\) is nonnegative. Thus every nonconstant term in

$$
0=\mathbb E_U[X_\infty w]
=
\sum_a\widehat X_\infty(a)\widehat w(a)
$$

is nonnegative or zero, while the constant term is

$$
\widehat X_\infty(0)\widehat w(0)
=
\widehat w(0)>0.
$$

This contradiction proves no-collapse.

The same compactness mechanism applies to any fixed finite-\(n\) relaxed
signed branch on compact parameter sets, provided each multiplier either
stays away from zero or tends to zero through the controlled seal prefactor.
Thus the boundary problem disappears at fixed \(n\). The minus branch remains
special only because \(x_a\le0\) for all nonzero coefficients, which gives the
Stieltjes order structure.

### 14.1 Uniform Minus-Branch Ellipticity

Using the spectral representation

$$
K_X
=
\frac1N\sum_{s\in G}X(s)e_se_s^T,
$$

and

$$
\frac1N\sum_s e_se_s^T=I,
$$

the no-collapse floor implies

$$
\boxed{
K_{X_-}(r)\succeq\delta_- I
\qquad(0\le r\le1).
}
$$

For the active Schur complement,

$$
z^T\mathcal K_M^-z
=
\min_{y_M=z}y^TK_{X_-}y
\ge
\delta_-\min_{y_M=z}|y|^2
=
\delta_-|z|^2.
$$

Hence

$$
\boxed{
\mathcal K_M^-(r)\succeq\delta_- I,
\qquad
(\mathcal K_M^-)^{-1}\preceq\delta_-^{-1}I.
}
$$

On the minus branch,

$$
K_{X_-}=I-\mathcal C,
\qquad
\mathcal C\ge0,
\qquad
\rho(\mathcal C)\le1-\delta_-<1.
$$

Therefore

$$
\boxed{
K_{X_-}^{-1}
=
\sum_{m\ge0}\mathcal C^m,
}
$$

and

$$
\boxed{
\log K_{X_-}
=
-\sum_{m\ge1}\frac{\mathcal C^m}{m}
}
$$

converge uniformly. Consequently,

$$
\widehat{1/X_-}(c)\ge0,
\qquad
\widehat{\log X_-}(c)\le0
\quad(c\ne0),
$$

with uniform operator bounds controlled by \(\delta_-\).

## 15. Spectral-Floor Schur Gap

Let \(V=\mathbb F_2^n\), including the zero frequency, and split

$$
V=M\sqcup\bar R,
\qquad
\bar R=R\cup\{0\}.
$$

For \(s\in G\), define

$$
e_s=(\chi_a(s))_{a\in V},
\qquad
p_s=(\chi_a(s))_{a\in M},
\qquad
r_s=(\chi_b(s))_{b\in\bar R}.
$$

Since

$$
K_Xe_s=X(s)e_s,
$$

the active Schur complement satisfies the exact point-evaluation identity

$$
\boxed{
\mathcal K_Mp_s=X(s)\rho_s,
}
$$

where

$$
\boxed{
\rho_s
=
p_s-K_{M\bar R}K_{\bar R\bar R}^{-1}r_s.
}
$$

**Spectral-Floor Schur Gap Lemma.** Let \(Z\subseteq G\), and suppose

$$
X(s)\ge\delta_Z>0
\qquad(s\notin Z).
$$

Then

$$
\boxed{
z^T\mathcal K_Mz\ge\delta_Z|z|^2
}
$$

for every \(z\) satisfying

$$
\boxed{
\langle z,\rho_s\rangle=0
\qquad(s\in Z).
}
$$

**Proof.** Let \(y=(z,y_{\bar R})\) be the \(K_X\)-harmonic lift:

$$
y_{\bar R}
=
-K_{\bar R\bar R}^{-1}K_{\bar RM}z.
$$

Then

$$
(K_Xy)_{\bar R}=0,
\qquad
(K_Xy)_M=\mathcal K_Mz,
$$

and

$$
z^T\mathcal K_Mz=y^TK_Xy.
$$

Moreover,

$$
e_s^Ty=\rho_s^Tz.
$$

Thus \(e_s^Ty=0\) on \(Z\). Using

$$
K_X=\frac1N\sum_sX(s)e_se_s^T,
$$

we get

$$
y^TK_Xy
=
\frac1N\sum_{s\notin Z}X(s)(e_s^Ty)^2
\ge
\delta_Z\frac1N\sum_{s\notin Z}(e_s^Ty)^2.
$$

Since \(e_s^Ty=0\) on \(Z\),

$$
\frac1N\sum_{s\notin Z}(e_s^Ty)^2
=
|y|^2
\ge
|z|^2.
$$

This proves the lemma.

For \(Z=\{s_\star\}\), the complement condition is
\(\langle z,\rho_M\rangle=0\), not \(\langle z,e_M\rangle=0\). This is the
exact condition that the harmonic lift has no target point-evaluation
component.

If \(Z=s_\star+H\) is a target-aligned face, the finite-rank dangerous space
is

$$
\boxed{
\mathscr P_Z=\operatorname{span}\{p_s:s\in Z\},
}
$$

and the transverse complement is

$$
\boxed{
\langle z,\rho_s\rangle=0
\qquad(s\in Z).
}
$$

At fixed finite \(n\), no-collapse says such faces are not actual interior
degeneracies. They remain useful as blow-up models and as the finite-rank
geometry behind quotient reductions.

## 16. Passive Elimination: Two Active Functionals

The passive coordinates can be eliminated exactly, but one must distinguish
the reduced critical functional from the reduced entropy value.

Let \(y=x_M\) and write passive coefficients as \(x_R=-v_R\), with
\(v_R>0\). Set

$$
\phi(u)=u\log u-u.
$$

Define

$$
\boxed{
\mathscr R(y)
=
\inf_{v_R>0}
\left[
F^*(y,-v_R)+\sum_{b\in R}\phi(v_b)
\right].
}
$$

Let \(v(y)\) be the passive minimizer. Its Euler equation is

$$
-g_R+\log v_R=0,
$$

so

$$
g_R=\log v_R.
$$

The envelope theorem gives

$$
\boxed{
\nabla\mathscr R(y)=g_M(y).
}
$$

Differentiating the passive equation gives

$$
dv_R
=
B_R^{-1}H_{RM}\,dy,
\qquad
B_R=U_R^{-1}+H_{RR}.
$$

Thus

$$
\boxed{
\nabla^2\mathscr R(y)
=
H_{MM}-H_{MR}B_R^{-1}H_{RM}.
}
$$

This is the Schur-reduced Hessian from Section 8.

However, the entropy value after passive elimination is

$$
\boxed{
\mathscr D(y)
:=
F^*(y,-v(y)).
}
$$

Since

$$
\mathscr R(y)=\mathscr D(y)+\Pi(y),
\qquad
\Pi(y)=\sum_{b\in R}\phi(v_b(y)),
$$

we have

$$
\mathscr D(y)=\mathscr R(y)-\Pi(y).
$$

Furthermore,

$$
d\Pi=g_R^Tdv_R,
$$

so

$$
\boxed{
\nabla\Pi(y)=H_{MR}B_R^{-1}g_R.
}
$$

Therefore

$$
\boxed{
\nabla\mathscr D(y)
=
g_M-H_{MR}B_R^{-1}g_R
=
\widetilde g_M.
}
$$

Thus:

$$
\boxed{
\nabla\mathscr R
\text{ determines the sealed critical endpoints,}
\qquad
\nabla\mathscr D
\text{ determines entropy change.}
}
$$

### 16.1 Reduced Endpoint Equations

For a signed active multiplier \(s\in[-1,1]\), write

$$
y(s)=su(s).
$$

The reduced active critical equation is

$$
s\nabla\mathscr R(su)+\log u=0.
$$

Equivalently,

$$
\boxed{
\alpha(s)=s\nabla\mathscr R(y(s)),
\qquad
y(s)=s e^{-\alpha(s)}.
}
$$

At the endpoints,

$$
y_+=u^+>0,
\qquad
y_-=-u^-<0,
$$

and

$$
\boxed{
\nabla\mathscr R(y_+)=\alpha^+,
\qquad
\nabla\mathscr R(y_-)=-\alpha^-.
}
$$

The endpoint theorem is

$$
\boxed{
\Omega(1)
=
\mathscr D(y_+)-\mathscr D(y_-)
\ge0.
}
$$

## 17. Dual Active Normal Form

Define the passive-eliminated active dual potential

$$
\boxed{
\Lambda(G)
=
\inf_{g_R}
\left[
F(G,g_R)+\sum_{b\in R}e^{g_b}
\right].
}
$$

Then

$$
\boxed{
\mathscr R=\Lambda^*.
}
$$

Let \(h(G)\) be the passive minimizing vector and set

$$
v_b(G)=e^{h_b(G)}.
$$

Define the passive entropy envelope

$$
\boxed{
\mathcal A(G)
=
\sum_{b\in R}v_b(G)(1-h_b(G)).
}
$$

Since \(\Pi(y)=\sum_R(v_bh_b-v_b)\), one has

$$
\mathcal A(G)=-\Pi(y),
\qquad
G=\nabla\mathscr R(y).
$$

Thus the reduced entropy in dual variables is

$$
\boxed{
\Theta(G)
:=
\mathscr D(\nabla\Lambda(G))
=
G\cdot\nabla\Lambda(G)-\Lambda(G)+\mathcal A(G).
}
$$

The endpoint equations are

$$
G_+=\alpha^+\ge0,
\qquad
G_-=-\alpha^-\le0,
$$

with

$$
\boxed{
\nabla\Lambda(G_+)=e^{-G_+}=u^+,
}
$$

and

$$
\boxed{
\nabla\Lambda(G_-)=-e^{G_-}=-u^-.
}
$$

Equivalently, \(G_+\) minimizes

$$
J_+(G)=\Lambda(G)+\sum_{a\in M}e^{-G_a},
$$

and \(G_-\) minimizes

$$
J_-(G)=\Lambda(G)+\sum_{a\in M}e^{G_a}.
$$

The endpoint theorem is

$$
\boxed{
\Theta(G_+)-\Theta(G_-)\ge0.
}
$$

### 17.1 Bregman And Curvature-Centroid Forms

Let

$$
d=G_+-G_-=\alpha^++\alpha^-\ge0,
\qquad
G(t)=G_-+td,
\quad 0\le t\le1.
$$

Set

$$
V(t)=d^T\nabla^2\Lambda(G(t))d.
$$

The endpoint excess has the equivalent forms

$$
\boxed{
\Omega
=
\Delta\mathcal A
-\langle\alpha^-,u^++u^-\rangle
+
\int_0^1 tV(t)\,dt,
}
$$

and

$$
\boxed{
\Omega
=
\Delta\mathcal A
+
\frac12\langle u^++u^-,\alpha^+-\alpha^-\rangle
+
\frac12
\left[
B_\Lambda(G_-,G_+)-B_\Lambda(G_+,G_-)
\right].
}
$$

Here

$$
\Delta\mathcal A=\mathcal A(G_+)-\mathcal A(G_-).
$$

Moreover,

$$
B_\Lambda(G_-,G_+)-B_\Lambda(G_+,G_-)
=
\int_0^1(2t-1)V(t)\,dt.
$$

Since

$$
\int_0^1V(t)\,dt
=
\langle d,u^++u^-\rangle,
$$

the theorem is equivalent to the curvature-centroid inequality

$$
\boxed{
\frac{\int_0^1tV(t)\,dt}{\int_0^1V(t)\,dt}
\ge
\frac{
\langle \alpha^-,u^++u^-\rangle-\Delta\mathcal A
}{
\langle d,u^++u^-\rangle
}.
}
$$

Thus the horizontal curvature measure \(V(t)\,dt\) must not concentrate too
close to the negative endpoint.

## 18. Full-Field Work And Horizontal Cumulants

Let

$$
\ell(t)=(G(t),h(t)),
$$

where \(h(t)\) is the passive minimizer in \(\Lambda(G(t))\). The passive
constraint is

$$
F_R(G,h)+e^h=0.
$$

Define

$$
\mathcal F(G,h)=F(G,h)+\sum_{b\in R}e^{h_b}.
$$

Then

$$
\mathcal F_R(G,h)=0.
$$

Differentiating gives

$$
h'
=
-(F_{RR}+U_R)^{-1}F_{RM}d,
\qquad
U_R=\operatorname{diag}(e^h).
$$

Writing \(q=(d,k)\), with

$$
k=-(F_{RR}+U_R)^{-1}F_{RM}d,
$$

we have the horizontal condition

$$
\Gamma_{R,*}q=0,
$$

where

$$
\Gamma=\nabla^2\mathcal F
=
\begin{pmatrix}
F_{MM}&F_{MR}\\
F_{RM}&F_{RR}+U_R
\end{pmatrix}.
$$

The endpoint excess is the full-field line integral

$$
\boxed{
\Omega=\Theta(G_+)-\Theta(G_-)
=
\int_0^1 \ell(t)\cdot x'(t)\,dt,
}
$$

where \(x(t)=\nabla F(\ell(t))\). Equivalently,

$$
\Omega=\int_0^1\mathcal W(t)\,dt,
$$

with reduced Walsh work density

$$
\boxed{
\mathcal W(t)
=
G^T\nabla^2\Lambda(G)d
+
h^TU_R(F_{RR}+U_R)^{-1}F_{RM}d.
}
$$

### 18.1 Poisson-Killed Extension

Introduce independent random variables

$$
N_b\sim\operatorname{Pois}(e^{h_b})
\qquad(b\in R),
$$

independent of \(s\sim P_{G,h}\), and define extended coordinates

$$
\xi_a=\chi_a
\qquad(a\in M),
$$

and

$$
\xi_b=\chi_b+N_b
\qquad(b\in R).
$$

Then

$$
\Gamma_{ij}=\operatorname{Cov}(\xi_i,\xi_j),
$$

and the passive equation gives

$$
\mathbb E[\xi_b]=0
\qquad(b\in R).
$$

The horizontal lift \(q=(d,k)\) satisfies

$$
\operatorname{Cov}(\xi_b,\Psi)=0
\qquad(b\in R),
$$

where

$$
\Psi=\sum_{a\in M}d_a\xi_a+\sum_{b\in R}k_b\xi_b.
$$

Equivalently,

$$
\Psi
=
\psi(s)+\sum_{b\in R}k_b\bigl(N_b-e^{h_b}\bigr),
$$

with

$$
\psi(s)=\sum_{a\in M}d_a\chi_a(s)+\sum_{b\in R}k_b\chi_b(s).
$$

The passive killing is exactly the Poisson extension:

$$
\boxed{
\operatorname{Var}(\Psi)
=
\operatorname{Var}_{P_{G,h}}(\psi)
+
\sum_{b\in R}e^{h_b}k_b^2
=
d^T\nabla^2\Lambda(G)d.
}
$$

and

$$
\boxed{
\kappa_3(\Psi)
=
\kappa_{P_{G,h}}(\psi^3)
+
\sum_{b\in R}e^{h_b}k_b^3
=
D^3\Lambda(G)[d,d,d].
}
$$

Thus the passive killing skew is not an error term. It is exactly the third
cumulant of the Poisson-killed horizontal tangent.

### 18.2 Horizontal Residuals

Define the residualized active coordinates

$$
\boxed{
\varphi_a
=
\xi_a
-
\sum_{b\in R}
\left[(F_{RR}+U_R)^{-1}F_{RM}\right]_{ba}\xi_b.
}
$$

Then

$$
\operatorname{Cov}(\xi_b,\varphi_a)=0
\qquad(b\in R),
$$

and

$$
\Psi=\sum_{a\in M}d_a\varphi_a.
$$

Therefore

$$
\boxed{
\nabla^2\Lambda(G)_{ab}
=
\operatorname{Cov}(\varphi_a,\varphi_b),
}
$$

and

$$
\boxed{
D^3\Lambda(G)[d,d,d]
=
\kappa_3\left(\sum_{a\in M}d_a\varphi_a\right).
}
$$

This is the exact replacement for the earlier Walsh-line cubic picture.
At the uniform density the third cumulant is line-supported. Away from
uniform it is a density-transported cumulant with sidebands. Horizontalization
absorbs the sidebands into the residuals \(\varphi_a\).

The endpoint excess becomes

$$
\boxed{
\Omega
=
\Delta\mathcal A
+
\frac12
\langle u^++u^-,\alpha^+-\alpha^-\rangle
+
\frac12
\int_0^1t(1-t)
\kappa_3\left(\sum_{a\in M}d_a\varphi_a(t)\right)\,dt.
}
$$

Pointwise positivity of the horizontal cubic is not the correct theorem and
is generally too strong. The correct statement is integrated:

$$
\boxed{
\Delta\mathcal A
+
\frac12
\langle u^++u^-,\alpha^+-\alpha^-\rangle
+
\frac12
\int_0^1t(1-t)
\kappa_3(\Psi_t)\,dt
\ge0.
}
$$

## 19. Delta-Anchored Curvature Threshold

The negative endpoint is not arbitrary. It is the fully symmetric delta
endpoint. In the target gauge,

$$
G_-=h_-=\log u_\star
$$

on every nonzero Walsh coordinate, where \(u_\star\) solves

$$
\frac{1-(N-1)u_\star}{1+u_\star}=u_\star^N.
$$

Set

$$
\alpha_\star=-\log u_\star.
$$

Then

$$
\alpha^-=\alpha_\star\mathbf1_M,
\qquad
u_a^-=u_\star
\quad(a\in M).
$$

Consequently,

$$
d_a=G_{+,a}-G_{-,a}
=
\alpha_a^++\alpha_\star,
$$

and

$$
u_a^++u_a^-
=
e^{-\alpha_a^+}+u_\star
=
\frac{e^{-d_a}}{u_\star}+u_\star.
$$

The centroid threshold becomes explicit:

$$
\boxed{
\Omega\ge0
\iff
\frac{\int_0^1tV(t)\,dt}{\int_0^1V(t)\,dt}
\ge
\frac{
\alpha_\star
\sum_{a\in M}
\left(
u_\star+\frac{e^{-d_a}}{u_\star}
\right)
-\Delta\mathcal A
}{
\sum_{a\in M}
d_a
\left(
u_\star+\frac{e^{-d_a}}{u_\star}
\right)
}.
}
$$

Thus the remaining theorem says that the delta-anchored horizontal curvature
measure cannot have barycenter before this explicit threshold.

### 19.1 Passive Envelope Sign Target

The passive envelope is

$$
\mathcal A(G)=\sum_{b\in R}e^{h_b(G)}(1-h_b(G)).
$$

The passive equation gives

$$
e^{h_b}=-\mathbb E_{P_{G,h}}\chi_b,
$$

so on the relevant negative passive orthant,

$$
0<e^{h_b}\le1,
\qquad
h_b\le0.
$$

The scalar function

$$
A(v)=v(1-\log v)
\qquad(0<v\le1)
$$

has

$$
A'(v)=-\log v\ge0.
$$

Therefore the following would be a useful independent lemma:

**Passive Coefficient Floor Lemma.**

$$
\boxed{
e^{h_b(G_+)}\ge u_\star
\qquad(b\in R).
}
$$

If true, it implies

$$
\Delta\mathcal A\ge0,
$$

which lowers the required curvature-centroid threshold. Even an explicit
averaged lower bound for \(\Delta\mathcal A\) would be useful.

### 19.2 Stieltjes Initial Condition

At the negative endpoint,

$$
x_c=-u_\star
\qquad(c\ne0).
$$

Thus the density convolution matrix has the killed-walk form

$$
K_X=I-\mathcal C,
\qquad
\mathcal C\ge0.
$$

In horizontal dual language, the extended Hessian

$$
\Gamma(G_-)=\nabla^2\mathcal F(G_-,h_-)
$$

is Stieltjes. Indeed, for \(i\ne j\),

$$
\Gamma_{ij}=x_{i+j}-x_ix_j\le0,
$$

and adding Poisson killing only increases the passive diagonal. Hence the
active Schur complement

$$
\nabla^2\Lambda(G_-)
$$

is also Stieltjes. Therefore

$$
\boxed{
\nabla^2\Lambda(G_-)
\text{ has nonpositive off-diagonal entries and inverse-positive order.}
}
$$

This does not prove the endpoint theorem, but it gives a rigid initial
condition for the curvature measure \(V(t)\,dt\).

## 20. Rank-One Killed Base Case

The scalar quotient theorem closes the pure one-dimensional quotient channel.
The next base case is stronger:

$$
\boxed{
|M|=1
\quad
\text{with all passive coordinates eliminated exactly.}
}
$$

Let \(M=\{m\}\), and write the plus endpoint coefficients as

$$
x_m=u>0,
\qquad
x_b=-v\quad(b\in R).
$$

By symmetry, \(v=e^h\) is common over \(R\). The density has three levels:

$$
A=1+u-(N-2)v,
\qquad
B=1+u+2v,
\qquad
C=1-u,
$$

with counts

$$
1,\qquad \frac N2-1,\qquad \frac N2.
$$

The seal equations reduce to

$$
\boxed{
\frac AB=v^N,
\qquad
\frac CB=u^2v^2.
}
$$

Since \(A>0\),

$$
v<\frac{1+u}{N-2}.
$$

For \(N\ge8\),

$$
\frac{1-u}{1+u}
=
u^2v^2
\left(1+\frac{2v}{1+u}\right)
<u^2.
$$

Hence \(u>\rho\), where \(\rho\) is the binary opposite root

$$
\frac{1-\rho}{1+\rho}=\rho^2.
$$

By data processing onto the active character,

$$
D_+\ge
B_2(u),
$$

where

$$
B_2(u)
=
\frac12
\left[
(1+u)\log(1+u)
+
(1-u)\log(1-u)
\right].
$$

Thus

$$
D_+>B_2(\rho).
$$

A direct scalar check gives

$$
B_2(\rho)>\log\frac87.
$$

Meanwhile,

$$
D_\delta(N)<\log\frac{N}{N-1}\le\log\frac87
\qquad(N\ge8).
$$

Therefore the rank-one killed theorem is closed for every \(N\ge8\):

$$
\boxed{
D_+>D_\delta(N)
\qquad(N\ge8,\ |M|=1).
}
$$

For \(N=4\), the active binary marginal bound is too weak, but the remaining
case is finite. The passive characters are one-bit marginals, so subadditivity
gives

$$
D_+\ge2B_2(v).
$$

Eliminating \(u\) from \(A/B=v^4\) gives

$$
1+u=\frac{2v(1+v^4)}{1-v^4}.
$$

The remaining equation is

$$
(1-v^4)^2(1-v-v^4-v^5)
=
2v^3(2v+2v^5-1+v^4)^2.
$$

Move the right-hand side to the left and factor:

$$
(1-v^4)^2(1-v-v^4-v^5)
-
2v^3(2v+2v^5-1+v^4)^2
$$

$$
=
-
\left(3v^5+v^4+v-1\right)
\left(3v^8+2v^7+4v^4-2v^3+1\right).
$$

The second factor is positive on \(0<v<1\). The first factor is strictly
increasing there, because

$$
15v^4+4v^3+1>0.
$$

Moreover,

$$
3\left(\frac35\right)^5
\left(\frac35\right)^4
\frac35-1<0,
$$

while

$$
3\left(\frac{31}{50}\right)^5
\left(\frac{31}{50}\right)^4
\frac{31}{50}-1>0.
$$

Thus the admissible root lies in

$$
\frac35<v<\frac{31}{50}.
$$

Therefore

$$
D_+\ge2B_2(v)>2B_2(3/5)>\log\frac43>D_\delta(4).
$$

Thus the rank-one killed theorem is closed for every \(N\ge4\):

$$
\boxed{
|M|=1
\quad\Longrightarrow\quad
D_+>D_\delta(N).
}
$$

## 21. Final Current Obstruction

The proof has been reduced to two sharp remaining statements.

### 21.1 Horizontal Copositive Centroid Lemma

For general \(M\), \(d\ge0\), and

$$
H(t)=\nabla^2\Lambda(G_-+td),
$$

define

$$
K_1=\int_0^1tH(t)\,dt.
$$

The endpoint theorem is exactly

$$
\boxed{
d^TK_1d
+
\Delta\mathcal A
\ge
\alpha_\star
\sum_{a\in M}
\left(
u_\star+\frac{e^{-d_a}}{u_\star}
\right).
}
$$

This is the final active interior inequality. It is a copositive
curvature-centroid statement on the cone \(d\ge0\).

### 21.2 Horizontal Rank-One Domination

Rank-one killed comparison proves the desired endpoint excess along each
coordinate ray. The remaining higher-rank task is to show that mixed
horizontal curvature cannot move the curvature centroid earlier than the
coordinate-ray bound.

One possible proof-ready formulation is:

**Horizontal Rank-One Domination Lemma.** For every \(d\ge0\), the horizontal
curvature measure

$$
V_d(t)\,dt
=
d^T\nabla^2\Lambda(G_-+td)d\,dt
$$

dominates, in the centroid sense relevant to the endpoint inequality, a
positive mixture of the coordinate-ray measures

$$
V_{e_a}(t)\,dt.
$$

The domination must include the passive envelope correction
\(\Delta\mathcal A\). If true, then

$$
\text{rank-one killed theorem}
\quad+\quad
\text{rank-one domination}
\quad\Longrightarrow\quad
\Omega\ge0.
$$

This is cleaner than a direct Walsh-line cubic decomposition. Direct cubic
expansion creates density sidebands. Horizontal residualization absorbs those
sidebands, and the centroid formulation asks where the curvature mass lies,
not whether the cubic is pointwise positive.

The current sharp state is therefore:

$$
\boxed{
\text{Boundary is gone. Passive variables are horizontally eliminated.}
}
$$

$$
\boxed{
\text{Pointwise cubic positivity is false as a target.}
}
$$

$$
\boxed{
\text{Remaining route: rank-one killed comparison plus horizontal
rank-one domination.}
}
$$

## 22. Coboundary-Null Correction

The rank-one domination formulation in Section 21.2 is too strong as a final
statement. The reason is that the global equality set is not only the chosen
target delta representative. It contains the full translated delta orbit.

Let

$$
\tau_a=
\begin{cases}
-1,&a\in M,\\
+1,&a\notin M.
\end{cases}
$$

A translated delta centered at \(t_0\) has relative signs

$$
\tau_a=\chi_a(t_0).
$$

Equivalently, its defect set is

$$
M_{t_0}
=
\{a\ne0:\chi_a(t_0)=-1\},
$$

with

$$
|M_{t_0}|=\frac N2.
$$

For this translated delta endpoint,

$$
u_a^+=u_\star,
\qquad
G_{+,a}=\alpha_\star,
\qquad
G_{-,a}=-\alpha_\star
\qquad(a\in M_{t_0}),
$$

and therefore

$$
d_a=2\alpha_\star
\qquad(a\in M_{t_0}).
$$

Both endpoints are delta laws, merely centered at different points, so

$$
\Theta(G_+)-\Theta(G_-)=0.
$$

Thus the final copositive endpoint excess must have the translated-delta
nullspace:

$$
\boxed{
\mathcal E_{M_{t_0}}(2\alpha_\star\mathbf1)=0.
}
$$

The mixed terms cannot merely be dominated by a positive mixture of rank-one
excesses. In translated-delta directions, they must cancel exactly enough to
turn many strict coordinate-ray costs into zero total excess.

The corrected final theorem is therefore:

**Coboundary-Null Horizontal Copositive Theorem.** For every defect set \(M\)
and endpoint displacement \(d\ge0\),

$$
\boxed{
\mathcal E_M(d)\ge0.
}
$$

Moreover,

$$
\boxed{
\mathcal E_M(d)=0
}
$$

if and only if either \(M=\varnothing\), or there exists \(t_0\ne s_\star\)
such that

$$
M=\{a\ne0:\chi_a(t_0)=-1\},
\qquad
d=2\alpha_\star\mathbf1_M.
$$

In words:

$$
\boxed{
\text{the only positive-orthant zero directions are Walsh coboundaries with
translated-delta amplitude.}
}
$$

This supersedes the literal rank-one domination lemma. Rank-one killed
comparison is still a strict face of the theorem, but not the whole
higher-rank mechanism.

## 23. Two-Layer Cocycle-Amplitude Nullspace

The sign cocycle detects whether the orientation is a coboundary, but it does
not enforce the endpoint amplitude \(d=2\alpha_\star\mathbf1_M\). A second
amplitude layer is needed.

Extend the active displacement by zero:

$$
D_a=
\begin{cases}
d_a,&a\in M,\\
0,&a\notin M,
\end{cases}
\qquad
a\ne0.
$$

Normalize it by

$$
\boxed{
Y_a=1-\frac{D_a}{\alpha_\star}.
}
$$

For a translated delta,

$$
D_a=\alpha_\star(1-\tau_a),
\qquad
Y_a=\tau_a.
$$

The two line defects are

$$
\boxed{
C^\tau_{a,b}
=
\tau_{a+b}-\tau_a\tau_b,
}
$$

and

$$
\boxed{
C^Y_{a,b}
=
Y_{a+b}-Y_aY_b.
}
$$

The sign defect has the exact square form

$$
\frac{1-\tau_a\tau_b\tau_{a+b}}2
=
\frac14
\left(\tau_{a+b}-\tau_a\tau_b\right)^2.
$$

The amplitude condition can also be written directly in \(D\). Since

$$
Y_{a+b}-Y_aY_b
=
-
\frac1{\alpha_\star}
\left(
D_{a+b}-D_a-D_b+\frac{D_aD_b}{\alpha_\star}
\right),
$$

the vanishing of \(C^Y\) is equivalent to the nonlinear Cauchy rule

$$
\boxed{
D_{a+b}
=
D_a+D_b-\frac{D_aD_b}{\alpha_\star}.
}
$$

If \(r_a=D_a/(2\alpha_\star)\), then in the translated-delta case
\(r_a\in\{0,1\}\) and this rule is exactly

$$
r_{a+b}=r_a\oplus r_b.
$$

The nullspace is exact:

1. If \(C^\tau_{a,b}=0\) for all Walsh lines, then
   \(\tau_{a+b}=\tau_a\tau_b\), so after setting \(\tau_0=1\) the map
   \(a\mapsto\tau_a\) is a character:

$$
\tau_a=\chi_a(t_0).
$$

2. If also \(C^Y_{a,b}=0\) for all Walsh lines, then \(Y\) is multiplicative.
   Since \(Y_a=1\) on \(M^c\) and \(Y_a\le0\) on \(M\), multiplicativity
   forces

$$
Y_a=\tau_a.
$$

Hence

$$
D_a=\alpha_\star(1-\tau_a),
$$

and therefore

$$
d_a=2\alpha_\star
\qquad(a\in M).
$$

Thus the two-layer defects have exactly the desired global zero set:

$$
\boxed{
C^\tau\equiv0,\quad C^Y\equiv0
\quad\Longleftrightarrow\quad
\text{target delta or translated delta.}
}
$$

The desired endpoint certificate should therefore have the schematic form

$$
\boxed{
\mathcal E_M(d)
=
\mathcal Q_{\rm amp}(d,\tau)
+
\sum_{\{a,b,a+b\}}
W_{a,b}(d)
\left(\tau_{a+b}-\tau_a\tau_b\right)^2
+
\mathcal R_{\rm hor},
}
$$

with

$$
\mathcal Q_{\rm amp}\ge0,
\qquad
W_{a,b}\ge0,
\qquad
\mathcal R_{\rm hor}\ge0,
$$

and

$$
\mathcal Q_{\rm amp}
\sim
\sum_{\{a,b,a+b\}}
Q_{a,b}(d)
\left(
D_{a+b}-D_a-D_b+\frac{D_aD_b}{\alpha_\star}
\right)^2.
$$

## 24. Twisted \(N=4\) Delta Cells

The local line object should not be ordinary conditional mutual information.
For a Walsh line

$$
L=\{a,b,a+b\},
$$

the quotient \(G/L^\perp\) is a four-point system. Ordinary conditional
mutual information vanishes on product laws, but a translated delta on this
four-point quotient is generally not a product law. It must nevertheless have
zero endpoint excess.

The correct local object is a twisted \(N=4\) delta-cell Bregman energy. For
each line \(L\), freeze the admissible horizontal/passive background generated
by the global enslaved path and let \(\Theta_L\) be the line-restricted mirror
functional. Let \(\mathcal Z_L\) be the local four-point delta orbit. Define

$$
\boxed{
\mathfrak B_L
=
\inf_{z\in\mathcal Z_L}
B_{\Theta_L}(\ell_L,z).
}
$$

The local orbit is characterized by

$$
\tau_{a+b}=\tau_a\tau_b,
\qquad
Y_{a+b}=Y_aY_b,
$$

together with the four-point delta amplitude normalization. The Bregman
energy has the right zero set:

$$
\mathfrak B_L=0
\quad\Longrightarrow\quad
C^\tau_{a,b}=0,
\qquad
C^Y_{a,b}=0.
$$

For fixed finite \(n\), the no-collapse arguments keep all admissible line
branches in a compact interior set. Hence the Hessian of \(\Theta_L\) is
uniformly positive transverse to \(\mathcal Z_L\), and there are positive
local weights such that

$$
\boxed{
\mathfrak B_L
\ge
W_L(C^\tau_{a,b})^2
+
Q_L(C^Y_{a,b})^2.
}
$$

This is the nonperturbative replacement for the uniform Walsh-line cubic
term. The cubic line invariant remains the leading perturbative trace, but
the full line theorem is a twisted four-point delta-cell Bregman coercivity
statement.

## 25. Exact Raw Line-Incidence Decomposition

The global endpoint excess has an exact raw decomposition over Walsh lines.
Let

$$
V^\times=\mathbb F_2^n\setminus\{0\},
$$

and let \(\mathcal L\) be the set of unordered Walsh lines

$$
L=\{a,b,a+b\}\subset V^\times.
$$

Each nonzero frequency belongs to exactly

$$
\rho=\frac{N-2}{2}=\frac N2-1
$$

Walsh lines, and each unordered pair \(\{a,b\}\), \(a\ne b\), belongs to
exactly one line.

Let

$$
H(t)=\nabla^2\Lambda(G_-+td),
$$

and extend \(d_i=0\) outside \(M\). For a line \(L\), define

$$
\boxed{
\mathsf K_L(t)
=
\frac1\rho
\sum_{i\in L}d_i^2H_{ii}(t)
+
2
\sum_{\{i,j\}\subset L}
d_id_jH_{ij}(t).
}
$$

Then the incidence counts give the exact identity

$$
\boxed{
d^TH(t)d
=
\sum_{L\in\mathcal L}\mathsf K_L(t).
}
$$

The passive envelope correction also splits by incidence. Along the
horizontal path,

$$
\Delta\mathcal A
=
\int_0^1
h(t)^TU(t)B(t)^{-1}F_{RM}(t)d\,dt.
$$

Write

$$
p_a(t)
=
h(t)^TU(t)B(t)^{-1}F_{R,a}(t).
$$

Then

$$
\Delta\mathcal A
=
\sum_a d_a\int_0^1p_a(t)\,dt.
$$

Distribute each coordinate over the \(\rho\) lines containing it:

$$
\boxed{
\Delta\mathcal A_L
=
\frac1\rho
\sum_{a\in L}d_a\int_0^1p_a(t)\,dt.
}
$$

Similarly define the distributed endpoint barrier

$$
\boxed{
\mathsf B_L
=
\frac1\rho
\sum_{a\in L\cap M}
\alpha_\star
\left(
u_\star+\frac{e^{-d_a}}{u_\star}
\right).
}
$$

Thus

$$
\boxed{
\mathcal E_M(d)
=
\sum_{L\in\mathcal L}
\mathcal E_L^{\rm raw},
}
$$

where

$$
\boxed{
\mathcal E_L^{\rm raw}
=
\int_0^1t\,\mathsf K_L(t)\,dt
+
\Delta\mathcal A_L
-
\mathsf B_L.
}
$$

These raw cells are not expected to be nonnegative. The diagonal budgets have
been divided by \(\rho\), while off-diagonal pairs live on a unique line and
appear fully. Therefore the raw cells are incidence-normalized pieces, not
ordinary four-point cells.

The remaining Stokes problem is to gauge-transform these raw pieces into
positive allocated line cells.

## 26. Incidence-Transport Bregman-Stokes Form

A full unscaled \(N=4\) cell on every line would immediately overcount the
rank-one case. If \(M=\{i\}\), the active coordinate \(i\) lies on \(\rho\)
lines, but the global excess contains only one one-body budget. Thus the
local cells must be allocated or tethered.

Define the off-diagonal line contribution

$$
\boxed{
O_L
=
2\int_0^1t
\sum_{\{i,j\}\subset L}
d_id_jH_{ij}(t)\,dt.
}
$$

For each frequency \(i\), define the one-body terms

$$
A_i
=
\int_0^1t\,d_i^2H_{ii}(t)\,dt,
$$

$$
P_i=\int_0^1p_i(t)\,dt,
\qquad
\Pi_i=d_iP_i,
$$

and

$$
B_i
=
\mathbf1_{i\in M}
\alpha_\star
\left(
u_\star+\frac{e^{-d_i}}{u_\star}
\right).
$$

Set the net one-body supply

$$
\boxed{
S_i=A_i+\Pi_i-B_i.
}
$$

Then the exact global excess is

$$
\boxed{
\mathcal E_M(d)
=
\sum_iS_i+\sum_{L\in\mathcal L}O_L.
}
$$

The immediate strengthening of the rank-one killed theorem is the
fiberwise one-body supply lemma:

$$
\boxed{
S_i\ge0
\qquad(i\in M).
}
$$

If this holds, the Stokes gauge becomes a transport problem. Choose
incidence weights

$$
\lambda_{iL}\ge0,
\qquad
\sum_{L\ni i}\lambda_{iL}=1.
$$

The allocated line energy is

$$
\boxed{
\mathcal E_L^\lambda
=
O_L+\sum_{i\in L}\lambda_{iL}S_i,
}
$$

and

$$
\boxed{
\sum_L\mathcal E_L^\lambda=\mathcal E_M(d).
}
$$

Let the desired local line demand be

$$
T_L
=
W_L(C_L^\tau)^2+Q_L(C_L^Y)^2.
$$

The allocated Stokes inequality is

$$
\boxed{
O_L+\sum_{i\in L}\lambda_{iL}S_i
\ge
T_L
\qquad(L\in\mathcal L).
}
$$

Equivalently, with

$$
\Delta_L=(T_L-O_L)^+,
$$

the transport exists if and only if the Hall inequalities hold:

$$
\boxed{
\sum_{L\in\mathcal S}\Delta_L
\le
\sum_{i\in N(\mathcal S)}S_i
\qquad
\text{for every family of lines }\mathcal S,
}
$$

where

$$
N(\mathcal S)=\{i:\exists L\in\mathcal S,\ i\in L\}.
$$

Thus the positive Bregman-Stokes gauge has become a concrete incidence
transport theorem on the point-line geometry of \(\mathbb F_2^n\).

If the sign of \(\Pi_i\) cannot be controlled, the safer version keeps the
three resources \(A_i\), \(\Pi_i\), and \(B_i\) separate. For every
nonnegative test weight \(\mu_L\), the dual feasibility condition is

$$
\boxed{
\sum_L\mu_L(T_L-O_L)
\le
\sum_i A_i\max_{L\ni i}\mu_L
+
\sum_i \Pi_i^+\max_{L\ni i}\mu_L
-
\sum_i \Pi_i^-\min_{L\ni i}\mu_L
-
\sum_i B_i\min_{L\ni i}\mu_L.
}
$$

This is the explicit three-resource form of the same Stokes-gauge problem.

## 27. Flat Stokes Cuts And The Remaining Hall Filling

The quotient/fiber entropy chain rule naturally produces flat cuts. For a
line family \(\mathcal S\), let

$$
U(\mathcal S)
=
\operatorname{span}\bigcup_{L\in\mathcal S}L.
$$

Quotienting by \(U(\mathcal S)^\perp\) gives an entropy decomposition

$$
D(P\|U_G)
=
D(\bar P_U\|U_{G/U^\perp})
+
\mathbb E_{\bar P_U}
D(P(\cdot\mid y+U^\perp)\|U_{U^\perp}).
$$

The second term is nonnegative. In the present endpoint language, this should
produce the flat Stokes inequality

$$
\boxed{
\sum_{L\subset U}
\left(T_L-O_L\right)
\le
\sum_{i\in U^\times}S_i
-
R_U,
\qquad
R_U\ge0.
}
$$

This is exactly the quotient/fiber mechanism already isolated earlier: the
quotient potential includes a nonlinear fiber free-energy/Jensen buffer, so
the line quotient is not just a linear Fourier projection.

However, Hall transport needs inequalities for arbitrary line families:

$$
\sum_{L\in\mathcal S}\Delta_L
\le
\sum_{i\in N(\mathcal S)}S_i.
$$

Since

$$
N(\mathcal S)\subseteq U(\mathcal S)^\times,
$$

flat cuts alone are weaker. The final combinatorial step is a geometric
filling or uncrossing theorem that converts flat cuts into arbitrary Hall
cuts. One possible form is:

$$
\boxed{
\sum_{\substack{L\subset U(\mathcal S)\\ L\notin\mathcal S}}
\Delta_L
\ge
\sum_{i\in U(\mathcal S)^\times\setminus N(\mathcal S)}S_i.
}
$$

Equivalently, the unused lines inside the generated flat must carry enough
positive demand to pay for the unused point supplies. This is the precise
place where Walsh incidence geometry enters after the analytic quotient
decomposition.

The current final proof route is therefore:

1. Prove the fiberwise rank-one supply lemma:

$$
\boxed{
S_i\ge0.
}
$$

2. Prove flat quotient/fiber Stokes inequalities from KL chain rules:

$$
\boxed{
\sum_{L\subset U}(T_L-O_L)
\le
\sum_{i\in U^\times}S_i-R_U,
\qquad R_U\ge0.
}
$$

3. Prove the geometric Hall filling/uncrossing lemma that upgrades flat cuts
to arbitrary Hall cuts.

Together these give allocations \(\lambda_{iL}\) with

$$
O_L+\sum_{i\in L}\lambda_{iL}S_i
\ge
W_L(C_L^\tau)^2+Q_L(C_L^Y)^2.
$$

Summing over lines yields

$$
\boxed{
\mathcal E_M(d)
\ge
\sum_L
\left[
W_L(C_L^\tau)^2+Q_L(C_L^Y)^2
\right].
}
$$

Equality forces

$$
C_L^\tau=0,
\qquad
C_L^Y=0
\qquad
\forall L,
$$

hence

$$
\tau_a=\chi_a(t_0),
\qquad
Y_a=\tau_a,
$$

and therefore

$$
D_a=\alpha_\star(1-\tau_a).
$$

Thus the endpoint is exactly a translated delta. The remaining obstruction is
now sharply:

$$
\boxed{
\text{fiberwise rank-one supply}
+
\text{flat KL-Stokes}
+
\text{geometric Hall filling}
\Longrightarrow
\text{global delta optimality.}
}
$$

## 28. Cut-Functional Collapse Of The Stokes Wall

The three subwalls in Section 27 can be collapsed into one max-flow cut
theorem. The fiberwise rank-one supply lemma is not a separate statement; it
is the singleton cut of the same theorem.

For each Walsh line \(L\), let the local target be the twisted \(N=4\)
Bregman cell

$$
\mathfrak B_L
$$

or, after applying local compact coercivity, the quadratic lower bound

$$
T_L
=
W_L(C_L^\tau)^2+Q_L(C_L^Y)^2.
$$

It is cleaner to formulate the transport first with \(\mathfrak B_L\) and
then use

$$
\mathfrak B_L\ge T_L.
$$

Define the actual line demand

$$
\boxed{
\Delta_L
=
(\mathfrak B_L-O_L)_+.
}
$$

If one works directly with the quadratic defect lower bound, replace
\(\mathfrak B_L\) by \(T_L\).

Recall the exact decomposition

$$
\mathcal E_M(d)
=
\sum_iS_i+\sum_LO_L.
$$

The allocation problem is to find nonnegative incidence weights
\(\lambda_{iL}\) such that

$$
\sum_{L\ni i}\lambda_{iL}\le1
\qquad(i\in V^\times),
$$

and

$$
\sum_{i\in L}\lambda_{iL}S_i\ge\Delta_L
\qquad(L\in\mathcal L).
$$

Then

$$
O_L+\sum_{i\in L}\lambda_{iL}S_i
\ge
\mathfrak B_L,
$$

and summing over lines gives

$$
\mathcal E_M(d)
\ge
\sum_L\mathfrak B_L
\ge
\sum_L
\left[
W_L(C_L^\tau)^2+Q_L(C_L^Y)^2
\right].
$$

The corresponding network has source-to-line capacities \(\Delta_L\),
infinite line-to-point capacities for incidences \(i\in L\), and point-to-sink
capacities \(S_i\). By max-flow/min-cut, the allocation exists if and only if

$$
\sum_{L\in\mathcal S}\Delta_L
\le
\sum_{i\in N(\mathcal S)}S_i
\qquad
\text{for every line family }\mathcal S.
$$

Since \(\Delta_L\ge0\), these Hall cuts are equivalent to point-set cuts:

$$
\boxed{
\sum_{L\subset P}\Delta_L
\le
\sum_{i\in P}S_i
\qquad
\forall P\subseteq V^\times.
}
$$

Indeed, for a line family \(\mathcal S\), put

$$
P=N(\mathcal S).
$$

Then

$$
\mathcal S\subseteq\{L:L\subset P\},
$$

so the point-set cut implies the Hall cut. Conversely, taking

$$
\mathcal S=\{L:L\subset P\}
$$

recovers the point-set cut.

Thus define the cut functional

$$
\boxed{
\Phi(P)
=
\sum_{i\in P}S_i
-
\sum_{L\subset P}\Delta_L.
}
$$

The final transport theorem is simply

$$
\boxed{
\Phi(P)\ge0
\qquad
\forall P\subseteq V^\times.
}
$$

The singleton cut \(P=\{i\}\) gives \(S_i\ge0\), because no Walsh line is
contained in a singleton. Thus the fiberwise rank-one supply lemma is
included automatically.

## 29. Translated-Delta Calibration Cut

The point-set cut theorem is exactly calibrated on every translated-delta
equality face.

On such a face,

$$
\tau_a=\chi_a(t_0),
\qquad
D_a=\alpha_\star(1-\tau_a),
\qquad
Y_a=\tau_a.
$$

The active set

$$
M=\{a:\tau_a=-1\}
$$

is an affine hyperplane of \(V^\times\), so

$$
|M|=\frac N2.
$$

Every Walsh line has either zero active points or two active points. Hence

$$
C_L^\tau=0,
\qquad
C_L^Y=0,
\qquad
\mathfrak B_L=T_L=0
\qquad
(L\in\mathcal L).
$$

Therefore

$$
\Delta_L=(-O_L)_+.
$$

By symmetry, all active supplies are equal:

$$
S_i=s_\star^{\rm line}
\qquad(i\in M),
$$

and every two-active line has the same off-diagonal value

$$
O_L=o_\star<0.
$$

Lines with no active points have \(O_L=0\). Let

$$
\rho=\frac N2-1
$$

be the number of Walsh lines through a fixed point inside the affine
hyperplane. Each active point is incident to exactly \(\rho\) two-active
lines, and each two-active line has two active endpoints. Thus the number of
two-active lines is

$$
\frac{|M|\rho}{2}.
$$

Since translated deltas are equality cases,

$$
0
=
\mathcal E_M(d)
=
|M|s_\star^{\rm line}
+
\frac{|M|\rho}{2}o_\star.
$$

Hence

$$
-o_\star
=
\frac{2s_\star^{\rm line}}{\rho}.
$$

The canonical equality flow is

$$
\boxed{
\lambda^\delta_{iL}
=
\begin{cases}
1/\rho,&i\in M,\ L\ni i,\ |L\cap M|=2,\\
0,&\text{otherwise.}
\end{cases}
}
$$

Equivalently, each two-active line demand

$$
\Delta_L=-O_L=\frac{2s_\star^{\rm line}}{\rho}
$$

is split equally between its two active endpoints. Each active endpoint pays

$$
\frac{\Delta_L}{2}
=
\frac{s_\star^{\rm line}}{\rho}
$$

on each of its \(\rho\) two-active lines, for total charge

$$
s_\star^{\rm line}.
$$

Therefore every point-set cut holds on the translated-delta calibration:

$$
\boxed{
\Phi(P)\ge0
\qquad(P\subseteq V^\times).
}
$$

More explicitly,

$$
\Phi_\delta(P)
=
s_\star^{\rm line}|P\cap M|
-
\frac{2s_\star^{\rm line}}{\rho}
\#\{L\subset P:|L\cap M|=2\}.
$$

If \(\deg_P(i)\) denotes the number of two-active lines through \(i\) that
are contained in \(P\), then

$$
\Phi_\delta(P)
=
\frac{s_\star^{\rm line}}{\rho}
\sum_{i\in P\cap M}
\left(\rho-\deg_P(i)\right)
\ge0.
$$

Thus the cut theorem is not merely compatible with the equality orbit; it is
calibrated by the translated-delta equality flow.

## 30. Flat Deficit Stokes And Closure Filling

For a point set \(P\), let

$$
U=\operatorname{span}(P).
$$

The cut functional satisfies the exact identity

$$
\boxed{
\Phi(P)-\Phi(U)
=
\sum_{\substack{L\subset U\\L\not\subset P}}\Delta_L
-
\sum_{i\in U^\times\setminus P}S_i.
}
$$

Therefore the point-set theorem follows from two statements.

First, a flat deficit Stokes inequality:

$$
\boxed{
\Phi(U)
=
\sum_{i\in U^\times}S_i
-
\sum_{L\subset U}\Delta_L
\ge
R_U,
\qquad
R_U\ge0.
}
$$

This is where the quotient/fiber entropy chain rule should enter. Flats are
closed under Walsh addition, so every line interaction inside \(U\) remains
inside \(U\). Quotienting by \(U^\perp\) turns the raw line decomposition into
a quotient-level endpoint excess, and the conditional fiber KL supplies the
nonnegative surplus \(R_U\).

Second, a closure-filling inequality:

$$
\boxed{
\Phi(P)\ge\Phi(U)-R_U.
}
$$

Equivalently,

$$
\boxed{
\sum_{i\in U^\times\setminus P}S_i
\le
\sum_{\substack{L\subset U\\L\not\subset P}}\Delta_L
+
R_U.
}
$$

Combining the two gives

$$
\Phi(P)\ge0.
$$

Thus flat cuts alone are not the theorem. They must be paired with closure
filling. This filling step is not purely combinatorial: arbitrary point-set
Hall cuts are not implied by flat cuts in finite projective geometries. It
must use the analytic relation among the demands \(\Delta_L\), supplies
\(S_i\), horizontal Walsh geometry, and the quotient/fiber surplus.

## 31. Weighted Closure Stability

The closure-filling theorem should be proved as a stability theorem around
the translated-delta calibration flow.

For a flat \(U\), let \(\mathcal Z_\delta(U)\) be the translated-delta
calibration orbit restricted to \(U^\times\). Choose the best calibration
\((\tau^U,Y^U)\in\mathcal Z_\delta(U)\), for example by minimizing

$$
\sum_{i\in U^\times}
\left[
(\tau_i-\tau_i^U)^2+(Y_i-Y_i^U)^2
\right].
$$

The algebraic BLR/cohomology stability principle says that distance to this
orbit is controlled by line defects:

$$
\operatorname{dist}_U((\tau,Y),\mathcal Z_\delta(U))^2
\lesssim_U
\sum_{L\subset U}
\left[
(C_L^\tau)^2+(C_L^Y)^2
\right].
$$

For closure filling one needs the localized extension version:

$$
\boxed{
\operatorname{dist}_{U\setminus P}
((\tau,Y),\mathcal Z_\delta(U))^2
\lesssim_U
\sum_{\substack{L\subset U\\L\not\subset P}}
\left[
(C_L^\tau)^2+(C_L^Y)^2
\right].
}
$$

In words: if the crossing lines have small sign and amplitude defects, then
multiplicativity propagates from \(P\) into its span.

The analytic companion is calibrated supply stability. Near a translated
delta calibration, missing supplies are controlled by missing calibrated line
demands plus defect energy:

$$
\boxed{
\sum_{i\in U^\times\setminus P}S_i
\le
\sum_{\substack{L\subset U\\L\not\subset P}}
(-O_L)_+
+
C_U
\sum_{\substack{L\subset U\\L\not\subset P}}
\left[
(C_L^\tau)^2+(C_L^Y)^2
\right]
+
R_U.
}
$$

Because

$$
\Delta_L=(\mathfrak B_L-O_L)_+
$$

and

$$
\mathfrak B_L
\ge
W_L(C_L^\tau)^2+Q_L(C_L^Y)^2,
$$

choosing the local weights to dominate the compact stability constants gives
the closure-filling inequality

$$
\sum_{i\in U^\times\setminus P}S_i
\le
\sum_{\substack{L\subset U\\L\not\subset P}}\Delta_L
+
R_U.
$$

Equivalently,

$$
\Phi(P)\ge\Phi(U)-R_U.
$$

A one-point version makes the mechanism explicit. If \(q\notin P\), then

$$
\Phi(P\cup\{q\})-\Phi(P)
=
S_q
-
\sum_{\substack{L\ni q\\L\setminus\{q\}\subset P}}
\Delta_L.
$$

In the translated-delta calibration, these increments are paid exactly along
closure chains by the canonical equality flow. Away from calibration, the
failure of exact payment is measured by the local Bregman cell, hence by
\(C_L^\tau\) and \(C_L^Y\).

The sharp current endpoint is therefore:

$$
\boxed{
\text{global delta optimality follows from the point-set cut theorem}
}
$$

where the point-set cut theorem follows from

$$
\boxed{
\text{flat deficit Stokes}
+
\text{weighted closure stability around translated-delta calibration}.
}
$$

The algebraic zero set, the translated-delta equality flow, and the max-flow
equivalence are now fixed. What remains is the compact stability estimate
that turns deviations from the calibrated flow into twisted \(N=4\) line-cell
energy.

## 32. Audited Weighted Closure Stability

The preceding closure-stability formulation needs one normalization audit.
The row one-form is supplied by

$$
\mathcal J_U=\mathcal A_U-\Lambda_U,
$$

but \(\mathcal J_U\) is not necessarily a positive buffer. For example, if
there are no passive or fiber variables, then \(\mathcal A_U=0\) and

$$
\mathcal J_U=-\Lambda_U,
$$

which is concave. Thus positivity must not be assigned to
\(\nabla^2\mathcal J_U\). The positive object is an augmented flat buffer

$$
\boxed{
\mathcal B_U
=
\mathcal J_U+\mathcal P_U+\mathcal F_U,
}
$$

where \(\mathcal P_U\) is the Poisson-killing buffer from passive elimination
and \(\mathcal F_U\) is the quotient/fiber Jensen or reverse-KL buffer from
the flat chain rule.

The flat surplus \(R_U\) is henceforth normalized as the full augmented
flat KL/Jensen/Poisson chain-rule surplus, namely the endpoint Bregman
surplus of \(\mathcal B_U\) plus any remaining orthogonal quotient/fiber
nonnegative terms. With this convention, closure filling is reduced to local
line-cell coercivity and the augmented buffer audit below.

Let \(P\subset U^\times\) span \(U\), and set

$$
Q=U^\times\setminus P,
\qquad
\partial P=\{L\subset U^\times:L\not\subset P\}.
$$

Define

$$
F_P
=
\sum_{i\in Q}S_i
-
\sum_{L\in\partial P}(-O_L)_+
-
R_U.
$$

The audited weighted closure statement is:

$$
\boxed{
F_P^+
\le
C_U\sum_{L\in\partial P}\mathfrak B_L.
}
$$

The provisional absorption step would be to rescale the line cells and use

$$
O_L^+\lesssim\mathfrak B_L,
$$

to obtain closure filling:

$$
\boxed{
\sum_{i\in Q}S_i
\le
\sum_{L\in\partial P}\Delta_L+R_U,
\qquad
\Delta_L=(\mathfrak B_L-O_L)_+.
}
$$

Section 41 records the correction: this rescaling is not free, because
\(\mathfrak B_L\) also defines the max-flow demands and flat cuts. The final
closure theorem must therefore be proved at the original, unit scale.

## 33. Boundary-Zero Calibrated Fiber

Assume the boundary-cell energy vanishes:

$$
B_{\partial P}
:=
\sum_{L\in\partial P}\mathfrak B_L
=0.
$$

Let

$$
M=\{i\in U^\times:\tau_i=-1\},
\qquad
B=Q\cap M.
$$

Every boundary line is then a twisted \(N=4\) delta cell. Extend

$$
\tau_0=Y_0=1.
$$

For any additive relation in \(B\),

$$
q_1+\cdots+q_m=0,
\qquad
q_j\in B,
$$

let \(r_k=q_1+\cdots+q_k\). At each step, the line

$$
\{r_{k-1},q_k,r_k\}
$$

contains \(q_k\in Q\), hence is a boundary line whenever it is
nondegenerate. In degenerate cases the same identity follows from
\(\tau_0=1\) and \(\tau_q^2=1\). Boundary-line multiplicativity gives

$$
\tau_{r_k}=\tau_{r_{k-1}}\tau_{q_k}.
$$

Therefore

$$
1=\tau_0=\tau_{r_m}=\prod_{j=1}^m\tau_{q_j}.
$$

Since each \(q_j\in B\) is active, \(\tau_{q_j}=-1\), so \(m\) is even. Thus
the assignment

$$
q\mapsto-1
\qquad(q\in B)
$$

is compatible with all additive relations among elements of \(B\). It
extends to a character

$$
\omega:W:=\operatorname{span}(B)\to\{\pm1\}.
$$

Boundary zero therefore gives a calibrated \(W\)-fiber:

$$
\boxed{
\tau_{x+w}=\omega(w)\tau_x,
\qquad
Y_{x+w}=\omega(w)Y_x
\qquad(x\in U,\ w\in W).
}
$$

This is the correct replacement for the false global statement that boundary
zero calibrates all of \(U\).

In particular, for \(q\in B\),

$$
\tau_{a+q}=-\tau_a.
$$

Thus exactly one of \(a\) and \(a+q\) is active, and

$$
\boxed{
d_ad_{a+q}=0.
}
$$

This cancellation is the algebraic reason the row formula below is exact.

## 34. Boundary-Zero Row One-Form Lemma

For \(q\in B\), define

$$
\Gamma_q
=
S_q+\frac12\sum_{\substack{L\subset U\\q\in L}}O_L.
$$

Then

$$
\boxed{
\Gamma_q
=
\int_0^1d_q(p_q(t)-x_q(t))\,dt.
}
$$

Indeed, for a line \(L=\{q,a,q+a\}\),

$$
O_L
=
2\int_0^1t
\left[
d_qd_aH_{qa}
+
d_qd_{q+a}H_{q,q+a}
+
d_ad_{q+a}H_{a,q+a}
\right]dt.
$$

By the calibrated fiber cancellation,

$$
d_ad_{a+q}=0,
$$

so the non-row term vanishes. Therefore

$$
\frac12\sum_{L\ni q}O_L
=
\int_0^1t\,d_q
\sum_{j\ne q}d_jH_{qj}(t)\,dt.
$$

Adding

$$
A_q=\int_0^1t\,d_q^2H_{qq}(t)\,dt
$$

gives

$$
A_q+\frac12\sum_{L\ni q}O_L
=
\int_0^1t\,d_q(H_U(t)d_U)_q\,dt.
$$

Since

$$
x_q'(t)=(H_U(t)d_U)_q,
$$

we have

$$
\Gamma_q
=
\int_0^1t\,d_qx_q'(t)\,dt+\Pi_q-B_q.
$$

For \(q\in B\),

$$
d_q=2\alpha_\star,
\qquad
x_q(0)=-u_\star,
\qquad
x_q(1)=u_\star.
$$

Integration by parts gives

$$
\int_0^1t\,d_qx_q'(t)\,dt
=
d_qu_\star
-
\int_0^1d_qx_q(t)\,dt.
$$

Also,

$$
B_q
=
\alpha_\star
\left(u_\star+\frac{e^{-d_q}}{u_\star}\right)
=
2\alpha_\star u_\star
=
d_qu_\star.
$$

The endpoint barrier cancels, leaving

$$
\Gamma_q
=
\Pi_q-\int_0^1d_qx_q(t)\,dt.
$$

Since

$$
\Pi_q=d_q\int_0^1p_q(t)\,dt,
$$

we obtain the row identity.

Because

$$
\nabla\mathcal J_U=p-x,
$$

summing over \(q\in B\) gives

$$
\boxed{
\sum_{q\in B}\Gamma_q
=
\int_0^1
\left\langle
d_B,\nabla_B\mathcal J_U(G(t))
\right\rangle dt.
}
$$

This lemma is a statement about the row one-form \(\mathcal J_U\), not about
positive curvature.

## 35. Augmented Buffer Audit

The augmented flat buffer is

$$
\mathcal B_U=\mathcal J_U+\mathcal P_U+\mathcal F_U.
$$

The audit has three parts. The first was initially stated as the pointwise
condition

$$
\partial_q(\mathcal P_U+\mathcal F_U)=0
\qquad(q\in B),
$$

or equivalently \(\nabla_B\mathcal B_U=\nabla_B\mathcal J_U\) along the
boundary-zero path. This is a sufficient condition, but Section 40 records
the safer formulation: what is actually needed is the row-decomposed surplus
identity for \(R_U\). Convexity or fiber symmetry alone should not be used to
infer this pointwise derivative identity.

Second, the Hessian of the augmented buffer is positive:

$$
\boxed{
\mathsf G_U(t)
:=
\nabla^2\mathcal B_U(G(t))
\succeq0.
}
$$

Its quadratic form is the horizontal residual covariance plus the
Poisson-killing square and the quotient/fiber Jensen square. No positivity is
claimed for \(\nabla^2\mathcal J_U\).

Third, the flat chain-rule surplus is normalized as

$$
\boxed{
R_U
=
\sum_{q\in B}\Gamma_q
+
B_{\mathcal B_U}(G_-,G_+)
+
\mathcal R_{\rm quot}^{\perp},
}
$$

where \(\mathcal R_{\rm quot}^{\perp}\ge0\) and

$$
B_{\mathcal B_U}(G_-,G_+)
=
\mathcal B_U(G_-)-\mathcal B_U(G_+)
-
\langle\nabla\mathcal B_U(G_+),G_--G_+\rangle.
$$

Along \(G(t)=G_-+td_U\),

$$
\boxed{
B_{\mathcal B_U}(G_-,G_+)
=
\int_0^1t\,d_U^T\mathsf G_U(t)d_U\,dt.
}
$$

The factor \(t\) comes from

$$
j(0)-j(1)+j'(1)=\int_0^1t\,j''(t)\,dt,
\qquad
j(t)=\mathcal B_U(G_-+td_U).
$$

Therefore

$$
\boxed{
R_U-\sum_{q\in B}\Gamma_q
=
\int_0^1t\,d_U^T\mathsf G_U(t)d_U\,dt
+
\mathcal R_{\rm quot}^{\perp}
\ge0.
}
$$

This is the Star-Row Surplus Lemma in its normalized form.

## 36. \(W\)-Fiber Pythagorean Form

Split

$$
U^\times=B\sqcup C.
$$

For each \(t\), write

$$
\mathsf G(t)
=
\begin{pmatrix}
\mathsf G_{BB}(t)&\mathsf G_{BC}(t)\\
\mathsf G_{CB}(t)&\mathsf G_{CC}(t)
\end{pmatrix}.
$$

Since \(\mathsf G(t)\succeq0\), the Hilbert-space projection identity gives

$$
d_U^T\mathsf G(t)d_U
=
\operatorname{Schur}_{B|C}^{\mathsf G(t)}(d_B)
+
\|d_C-d_C^{\rm har}(t)\|_{\mathsf G_{CC}(t)}^2,
$$

where

$$
d_C^{\rm har}(t)
=
-
\mathsf G_{CC}(t)^\dagger\mathsf G_{CB}(t)d_B,
$$

and

$$
\operatorname{Schur}_{B|C}^{\mathsf G(t)}(d_B)
=
d_B^T
\left[
\mathsf G_{BB}(t)
-
\mathsf G_{BC}(t)\mathsf G_{CC}(t)^\dagger\mathsf G_{CB}(t)
\right]
d_B.
$$

Equivalently, if the norm is the one induced by \(\mathsf G(t)\), then

$$
\operatorname{Schur}_{B|C}^{\mathsf G(t)}(d_B)
=
\inf_{z_C}
\left\|
\sum_{q\in B}d_q\varphi_q(t)
+
\sum_{c\in C}z_c\varphi_c(t)
\right\|_{\mathsf G(t)}^2
\ge0.
$$

Thus the audited Pythagorean identity is

$$
\boxed{
R_U-\sum_{q\in B}\Gamma_q
=
\int_0^1t\,
\operatorname{Schur}_{B|C}^{\mathsf G(t)}(d_B)\,dt
+
\int_0^1t\,
\|d_C-d_C^{\rm har}(t)\|_{\mathsf G_{CC}(t)}^2\,dt
+
\mathcal R_{\rm quot}^{\perp}.
}
$$

All terms on the right are nonnegative. The dangerous concavity issue is
avoided by separating the two roles:

$$
\boxed{
\mathcal J_U\text{ supplies the row one-form }p-x,
}
$$

while

$$
\boxed{
\mathcal B_U\text{ supplies the positive KL/Jensen/Pythagorean curvature.}
}
$$

## 37. Boundary-Zero Payment

At boundary zero, inactive missing points have zero supply. Hence

$$
\sum_{i\in Q}S_i=\sum_{q\in B}S_q.
$$

Let

$$
\mathcal A_\partial
=
\{L\in\partial P:|L\cap M|=2\}.
$$

On two-active boundary zero cells,

$$
O_L\le0,
$$

and on zero-active boundary zero cells,

$$
O_L=0.
$$

Therefore

$$
F_P
=
\sum_{q\in B}S_q
+
\sum_{L\in\mathcal A_\partial}O_L
-
R_U.
$$

For \(L\in\mathcal A_\partial\), define

$$
m_L=|L\cap B|.
$$

The row sum gives

$$
\sum_{q\in B}\Gamma_q
=
\sum_{q\in B}S_q
+
\sum_{L\in\mathcal A_\partial}
\frac{m_L}{2}O_L.
$$

Hence

$$
\sum_{q\in B}\Gamma_q-R_U-F_P
=
\sum_{L\in\mathcal A_\partial}
\left(\frac{m_L}{2}-1\right)O_L.
$$

Since

$$
O_L\le0,
\qquad
\frac{m_L}{2}-1\le0,
$$

every summand is nonnegative, so

$$
F_P
\le
\sum_{q\in B}\Gamma_q-R_U.
$$

The augmented Pythagorean identity gives

$$
R_U\ge\sum_{q\in B}\Gamma_q.
$$

Therefore

$$
\boxed{
B_{\partial P}=0
\quad\Longrightarrow\quad
F_P\le0.
}
$$

This proves Boundary-Zero Payment.

## 38. Compactness And Absorption

Once Boundary-Zero Payment is known, the stability estimate follows from
finite-dimensional compactness and local twisted \(N=4\) coercivity.

Let

$$
B_{\partial P}=\sum_{L\in\partial P}\mathfrak B_L.
$$

The local cell coercivity gives

$$
B_{\partial P}
\gtrsim
\operatorname{dist}^2((\tau,Y),Z_{\partial P}),
\qquad
Z_{\partial P}=\{B_{\partial P}=0\}.
$$

On active-missing zero components, incidence slack gives strict negativity
of \(F_P\). Indeed, if \(B\ne\varnothing\), not every active boundary line
can have both active endpoints missing; otherwise \(B\) would be invariant
under translation by \(P\), and since \(P\) spans \(U\), \(B\) would be
invariant under all of \(U\), forcing \(0\in B\), impossible. Hence some
active boundary line has \(m_L\le1\), giving strict negative slack because on
a two-active zero cell

$$
-O_L\ge\omega_U>0.
$$

On inactive tight zero components, \(B=\varnothing\), so every missing
displacement vanishes. Then the missing supplies and boundary off-diagonal
leakage begin quadratically, and the local line cells control that quadratic
distance.

Away from \(Z_{\partial P}\), compactness gives a positive lower bound for
\(B_{\partial P}\), while \(F_P^+\) is bounded. Thus, for each fixed
spanning \(P\subset U^\times\),

$$
F_P^+
\le
C_{U,P}\sum_{L\in\partial P}\mathfrak B_L.
$$

Taking the maximum over the finitely many spanning subsets of \(U^\times\)
gives

$$
\boxed{
F_P^+
\le
C_U\sum_{L\in\partial P}\mathfrak B_L.
}
$$

This gives the compactness estimate

$$
\boxed{
F_P^+
\le
C_U\sum_{L\in\partial P}\mathfrak B_L.
}
$$

There is also a useful line-level addendum

$$
\boxed{
O_L^+\le C_L^O\mathfrak B_L.
}
$$

At two-active zero cells \(O_L<0\), so \(O_L^+=0\) nearby. At zero-active
zero cells, all local displacements vanish, so \(O_L\) is quadratic and is
controlled by the local Bregman distance. Away from the zero set, compactness
gives the same bound.

However, this compactness estimate does not by itself imply closure filling
at the scale required by the max-flow cut theorem. The tempting move is to
rescale

$$
\widetilde{\mathfrak B}_L=K\mathfrak B_L
$$

with \(K\) large enough,

$$
(\widetilde{\mathfrak B}_L-O_L)_+
\ge
(-O_L)_+
+
C_U\mathfrak B_L.
$$

This algebraic inequality is true for \(K\) large enough, but the rescaling
is not free. The same line cell \(\mathfrak B_L\) defines the demand

$$
\Delta_L=(\mathfrak B_L-O_L)_+.
$$

Replacing it by \(K\mathfrak B_L\) changes the demands and makes the flat
cuts harder. Thus the preceding compactness-and-rescaling argument should not
be treated as a proof of closure filling.

The closure theorem must instead be proved at unit scale:

$$
\boxed{
\sum_{i\in U^\times\setminus P}S_i
\le
\sum_{\substack{L\subset U\\L\not\subset P}}
(\mathfrak B_L-O_L)_+
+
R_U.
}
$$

Section 41 records this as the remaining narrow gap.

## 39. Revised Closure Status

The augmented row-buffer audit has now been isolated sharply enough to close
the star-row surplus, provided \(R_U\) is normalized as the full flat
KL/Jensen/Poisson chain-rule surplus. The roles are:

$$
\boxed{
\mathcal J_U\text{ supplies the row one-form }p-x,
}
$$

and

$$
\boxed{
\mathcal B_U
=
\mathcal J_U+\mathcal P_U+\mathcal F_U
\text{ supplies the positive augmented curvature.}
}
$$

With this convention,

$$
\boxed{
R_U\ge\sum_{q\in B}\Gamma_q.
}
$$

Consequently,

$$
\boxed{
B_{\partial P}=0
\quad\Longrightarrow\quad
F_P\le0.
}
$$

Thus the row-decomposed audit closes the boundary-zero payment layer.

The remaining gap is not the row audit. It is the scale of the final
closure absorption. Compactness gives only

$$
\boxed{
F_P^+
\le
C_U\sum_{L\in\partial P}\mathfrak B_L.
}
$$

The previous rescaling step

$$
\mathfrak B_L\mapsto K\mathfrak B_L
$$

cannot be used freely, because \(\mathfrak B_L\) also defines the line
demands

$$
\Delta_L=(\mathfrak B_L-O_L)_+
$$

in the max-flow cut theorem. Increasing \(\mathfrak B_L\) changes the flat
cuts and can destroy the deficit inequality. The final closure theorem must
therefore be proved at unit scale.

## 40. Row-Decomposed Augmented Buffer Audit

The previous section should be read with one additional safety correction.
The closure argument does not need a global pointwise identity

$$
\nabla_B\mathcal B_U=\nabla_B\mathcal J_U.
$$

Nor should it rely on a slogan such as "the added buffers are even under the
fiber symmetry." The exact object needed by closure is the row-decomposed
flat surplus identity below.

Recall

$$
\mathcal J_U=\mathcal A_U-\Lambda_U,
\qquad
\nabla\mathcal J_U=p-x.
$$

This is the row one-form potential. It is not the positive curvature object.
The positive object is the augmented flat buffer

$$
\boxed{
\mathcal B_U
=
\mathcal J_U+\mathcal P_U+\mathcal F_U,
}
$$

where \(\mathcal P_U\) is the Poisson-killing buffer and \(\mathcal F_U\) is
the quotient/fiber Jensen or reverse-KL buffer. Its Hessian is denoted

$$
\mathsf G_U(t)
=
\nabla^2\mathcal B_U(G(t)).
$$

The required audit is the following.

**Row-Decomposed Augmented Buffer Identity.** Along a boundary-zero
configuration, with \(B=Q\cap M\),

$$
\boxed{
R_U
=
\int_0^1
\left\langle d_B,\nabla_B\mathcal J_U(G(t))\right\rangle dt
+
B_{\mathcal B_U}(G_-,G_+)
+
\mathcal R_{U,B}^{\perp},
}
$$

where

$$
\mathcal R_{U,B}^{\perp}\ge0
$$

and

$$
B_{\mathcal B_U}(G_-,G_+)
=
\int_0^1
t\,d_U^T\mathsf G_U(t)d_U\,dt
\ge0.
$$

Using the boundary-zero row one-form lemma,

$$
\sum_{q\in B}\Gamma_q
=
\int_0^1
\left\langle d_B,\nabla_B\mathcal J_U(G(t))\right\rangle dt,
$$

the audit immediately gives the star-row surplus

$$
\boxed{
R_U\ge\sum_{q\in B}\Gamma_q.
}
$$

This is exactly the input needed for Boundary-Zero Payment.

Equivalently, if one starts from a decomposition written with
\(\mathcal B_U\) in the row term,

$$
R_U
=
\int_0^1
\left\langle d_B,\nabla_B\mathcal B_U(G(t))\right\rangle dt
+
B_{\mathcal B_U}(G_-,G_+)
+
\mathcal R^\perp,
$$

then the missing compatibility condition is the integrated inequality

$$
\boxed{
\int_0^1
\left\langle
d_B,\nabla_B(\mathcal B_U-\mathcal J_U)(G(t))
\right\rangle dt
\ge0.
}
$$

This condition is not automatic from convexity or symmetry. For example, the
convex even function

$$
C(x,y)=(x-y)^2
$$

is invariant under simultaneous sign flip, but along

$$
x(t)=-1+2t,
\qquad
y(t)=10,
$$

one has

$$
\int_0^1
2\,\partial_x C(x(t),y(t))\,dt
=
-40.
$$

Thus the row compatibility must come from the actual flat KL chain-rule
definitions of \(\mathcal P_U\), \(\mathcal F_U\), and \(R_U\), not from
formal convexity alone.

With the row-decomposed audit in hand, the boundary-zero part of closure is
mechanical:

$$
\text{row-decomposed augmented audit}
\Longrightarrow
R_U\ge\sum_{q\in B}\Gamma_q
\Longrightarrow
\text{Boundary-Zero Payment}
$$

Together with compactness this gives

$$
\boxed{
F_P^+
\le
C_U\sum_{L\in\partial P}\mathfrak B_L.
}
$$

But this is not yet the point-set closure theorem, because absorbing the
constant by rescaling \(\mathfrak B_L\) changes the demands
\((\mathfrak B_L-O_L)_+\). The honest current status is:

$$
\boxed{
\text{the row audit is closed; the remaining gap is unit-scale closure.}
}
$$

The next theorem must compare \(F_P^+\) directly with the actual demand
increment

$$
(\mathfrak B_L-O_L)_+-(-O_L)_+
$$

at the original scale.

## 41. Unit-Scale Closure Gap

The row-decomposed augmented-buffer audit closes the star-row surplus:

$$
\boxed{
R_U\ge\sum_{q\in B}\Gamma_q.
}
$$

Together with the boundary-zero row identity, this proves

$$
\boxed{
B_{\partial P}=0
\quad\Longrightarrow\quad
F_P\le0.
}
$$

Thus the remaining obstruction is not the flat buffer audit. It is the final
absorption from the compactness estimate to the actual max-flow demands.

The correct unit-scale increment carried by a boundary line is

$$
\boxed{
A_L
:=
(\mathfrak B_L-O_L)_+
-
(-O_L)_+.
}
$$

The theorem needed for closure filling is therefore:

**Unit-Scale Closure Theorem.** For every flat \(U\le V\), every spanning set
\(P\subset U^\times\), and every endpoint displacement \(d\ge0\) produced by
the sealed horizontal branch,

$$
\boxed{
F_P^+
\le
\sum_{L\in\partial P}
\left[
(\mathfrak B_L-O_L)_+
-
(-O_L)_+
\right].
}
$$

Equivalently,

$$
\boxed{
\sum_{i\in U^\times\setminus P}S_i
\le
\sum_{\substack{L\subset U\\L\not\subset P}}
(\mathfrak B_L-O_L)_+
+
R_U.
}
$$

This is stronger than the compactness estimate

$$
F_P^+
\le
C_U\sum_{L\in\partial P}\mathfrak B_L,
$$

and it cannot be obtained by replacing \(\mathfrak B_L\) with
\(K\mathfrak B_L\). Such a replacement changes the demand

$$
\Delta_L=(\mathfrak B_L-O_L)_+
$$

and therefore changes the flat cut functional.

The obstruction is already visible on a full flat \(P=U^\times\). With
rescaled demands

$$
\Delta_L^{(K)}=(K\mathfrak B_L-O_L)_+,
$$

one gets

$$
\Phi_K(U)
=
\sum_{i\in U^\times}S_i
-
\sum_{L\subset U}\Delta_L^{(K)}.
$$

If \(O_L\le0\) on the relevant lines, then

$$
\Phi_K(U)
=
\sum_iS_i+\sum_LO_L
-
K\sum_L\mathfrak B_L
=
\mathcal E_U
-
K\sum_L\mathfrak B_L.
$$

For large \(K\), this can be negative unless the flat endpoint excess already
dominates \(K\sum_L\mathfrak B_L\). That domination is another theorem, not a
free consequence of compactness.

Thus the final closure proof must be unit-scale. The correct next step is
not a free compactness absorption, and not merely a local second-variation
check near the boundary-zero set. At unit scale there is no adjustable
constant left. Section 42 records the sharper endpoint identity and the
remaining anchored/component payment theorem.

If the Unit-Scale Closure Theorem holds, the rest of the proof chain closes
formally. Let \(U=\operatorname{span}(P)\). Since

$$
\Phi(P)-\Phi(U)
=
\sum_{\substack{L\subset U\\L\not\subset P}}\Delta_L
-
\sum_{i\in U^\times\setminus P}S_i,
$$

flat deficit Stokes gives

$$
\Phi(U)\ge R_U,
$$

and unit-scale closure gives

$$
\sum_{i\in U^\times\setminus P}S_i
\le
\sum_{\substack{L\subset U\\L\not\subset P}}\Delta_L
+
R_U.
$$

Therefore

$$
\Phi(P)\ge\Phi(U)-R_U\ge0.
$$

The point-set cuts follow:

$$
\boxed{
\Phi(P)\ge0
\qquad(P\subseteq V^\times).
}
$$

By max-flow/min-cut, there are incidence weights \(\lambda_{iL}\ge0\) such
that

$$
O_L+\sum_{i\in L}\lambda_{iL}S_i
\ge
\mathfrak B_L.
$$

Summing over lines gives

$$
\boxed{
\mathcal E_M(d)
=
\sum_iS_i+\sum_LO_L
\ge
\sum_L\mathfrak B_L.
}
$$

Local twisted-\(N=4\) coercivity then yields

$$
\mathcal E_M(d)
\ge
\sum_L
\left[
W_L(C_L^\tau)^2
+
Q_L(C_L^Y)^2
\right].
$$

The two-layer nullspace forces equality only when

$$
\tau_a=\chi_a(t_0),
\qquad
D_a=\alpha_\star(1-\tau_a),
$$

that is, at the target delta or a translated delta.

The current final status is therefore:

$$
\boxed{
\text{row audit closed; boundary-zero payment closed; unit-scale closure
remains open.}
}
$$

This is a much narrower gap than the original weighted Walsh cone problem,
but it is still a real lemma. The proof cannot honestly be marked complete
until the unit-scale closure theorem is established.

## 42. Anchored Component Payment Status

This section records the sharpened endpoint form of the unit-scale closure
gap. It also corrects a false line-local payment statement: the amplitude
residual cannot be distributed uniformly over all boundary lines.

Keep

$$
A_L=(\mathfrak B_L-O_L)_+-(-O_L)_+,
$$

and define

$$
H_P=F_P-\sum_{L\in\partial P}A_L.
$$

Since

$$
F_P
=
\sum_{i\in Q}S_i
-
\sum_{L\in\partial P}(-O_L)_+
-
R_U,
$$

we have the exact simplification

$$
\boxed{
H_P
=
\sum_{i\in Q}S_i
-
R_U
-
\sum_{L\in\partial P}(\mathfrak B_L-O_L)_+.
}
$$

Inactive missing points have zero supply, so

$$
\sum_{i\in Q}S_i=\sum_{q\in B}S_q,
\qquad
B=Q\cap M.
$$

For

$$
\Gamma_q
=
S_q+\frac12\sum_{\substack{L\subset U\\q\in L}}O_L,
$$

one has

$$
S_q
=
\Gamma_q
-
\frac12\sum_{\substack{L\subset U\\q\in L}}O_L.
$$

Every line through \(q\in Q\) is a boundary line. Therefore

$$
\sum_{q\in B}S_q
=
\sum_{q\in B}\Gamma_q
-
\sum_{L\in\partial P}\frac{m_L}{2}O_L,
\qquad
m_L=|L\cap B|.
$$

The defective row identity has the form

$$
\sum_{q\in B}\Gamma_q-R_U
=
\sum_{q\in B}E_q^{\rm amp}
+
\sum_{L\in\partial P}N_L
-
P_U,
$$

where

$$
P_U=B_{\mathcal B_U}(G_-,G_+)+\mathcal R_{U,B}^{\perp}\ge0.
$$

Consequently the exact endpoint identity is

$$
\boxed{
H_P
=
-P_U
+
\sum_{q\in B}E_q^{\rm amp}
+
\sum_{L\in\partial P}
\left[
N_L-\frac{m_L}{2}O_L
-
(\mathfrak B_L-O_L)_+
\right].
}
\tag{42.1}
$$

Here, for a boundary line \(L=\{i,j,k\}\), set

$$
T_{ij}^L
=
\int_0^1 t\,d_id_jH_{ij}(t)\,dt,
\qquad
O_L=2(T_{ij}^L+T_{ik}^L+T_{jk}^L),
$$

and, with \(J_L=L\cap B\),

$$
N_L=\sum_{q\in J_L}T_{L\setminus\{q\}}^L,
$$

where \(T_{L\setminus\{q\}}^L\) denotes the cross term on the pair opposite
\(q\).

### 42.1 Why Uniform Line Payment Fails

A tempting localization is to distribute each \(E_q^{\rm amp}\) equally among
all boundary lines through \(q\). This is false at unit scale.

Let

$$
L=\{i,j,k\},
\qquad
J_L=\{i,j\},
\qquad
d_k=0.
$$

Then

$$
N_L=0,
\qquad
O_L=2T_{ij}^L.
$$

The uniform localization would force, near the translated-delta calibration,

$$
\frac{E_i^{\rm amp}+E_j^{\rm amp}}{\rho_U}
\le
\mathfrak B_L.
$$

But if

$$
d_i=d_j=2\alpha_\star-\varepsilon,
\qquad
\varepsilon>0,
$$

then

$$
E_q^{\rm amp}
=
u_\star(\alpha_\star-1)\varepsilon
+O(\varepsilon^2),
$$

while the smooth twisted line Bregman distance satisfies

$$
\mathfrak B_L=O(\varepsilon^2).
$$

For \(N\ge4\), \(\alpha_\star>1\). Hence the uniform line-local payment
inequality fails. The linear amplitude drift must not be assigned to
two-missing-active lines.

### 42.2 Anchored Amplitude Routing

The amplitude residual must instead be routed through anchored boundary
lines. Define the active anchor set

$$
A_P=P\cap M.
$$

For \(q\in B\), the anchored boundary lines are

$$
\mathcal A(q)
=
\{L(q,a)=\{q,a,q+a\}:a\in A_P\}.
$$

At boundary zero, if \(B\ne\varnothing\), then \(A_P\ne\varnothing\). If
\(A_P\) were empty, every point of \(P\) would be inactive; boundary-line
multiplicativity would propagate activity from \(q\in B\) through the span of
\(P\), eventually forcing \(0\in M\), impossible.

Choose weights

$$
\omega_{qL}\ge0,
\qquad
\sum_{L\in\mathcal A(q)}\omega_{qL}=1,
\qquad
\omega_{qL}=0\quad(L\notin\mathcal A(q)).
$$

Set

$$
E_q^+=(E_q^{\rm amp})_+.
$$

Since \(E_q^{\rm amp}\le E_q^+\), (42.1) gives the upper bound

$$
\boxed{
H_P
\le
-P_U
+
\sum_{L\in\partial P}
\left[
\mathcal D_L^\omega
-
(\mathfrak B_L-O_L)_+
\right],
}
\tag{42.2}
$$

where

$$
\boxed{
\mathcal D_L^\omega
=
N_L-\frac{m_L}{2}O_L
+
\sum_{q\in L\cap B}\omega_{qL}E_q^+.
}
\tag{42.3}
$$

This removes the false linear-vs-quadratic demand on two-missing-active
lines. Positive amplitude residuals are routed only through one-missing-active
anchored lines, where the calibrated rank-one killed slack is available.

### 42.3 Remaining Component Payment Theorem

The proof is now reduced to the following static endpoint theorem.

**Anchored Component Payment Theorem.** For every flat \(U\), every spanning
set \(P\subset U^\times\), and every admissible endpoint branch,

$$
\boxed{
\sum_{q\in B}E_q^{\rm amp}
+
\sum_{L\in\partial P}
\left(
N_L-\frac{m_L}{2}O_L
\right)
-
\sum_{L\in\partial P}
(\mathfrak B_L-O_L)_+
\le
P_U.
}
\tag{CPT}
$$

Equivalently,

$$
\boxed{
H_P\le0.
}
$$

The anchored routing gives a plausible route to (CPT), but it is not yet an
unconditional proof. Two unit-scale ingredients remain to be checked with
the actual, unrescaled line cell \(\mathfrak B_L\).

First, one needs an amplitude-routing lemma: every positive amplitude
residual \(E_q^+\) must be payable through anchored one-missing-active lines,
not through two-missing-active lines where the local cell is only quadratic
in the under-amplitude perturbation.

Second, one needs the exact line-face payment inequalities with the
normalization of the manuscript's twisted \(N=4\) cell. The closed rank-one
killed theorem is strong evidence for the anchored face, but it does not by
itself identify the exact local inequality

$$
E_q^+
+
N_L-\frac12O_L
\le
(\mathfrak B_L-O_L)_+
$$

for every anchored line in the global horizontal background. This
identification is an additional lemma.

The pure non-row part also has to be verified at unit scale:

$$
N_L-\frac{m_L}{2}O_L
\le
(\mathfrak B_L-O_L)_+
$$

after the amplitude residual has been removed from unanchored lines.

### 42.4 Consequence If The Component Theorem Holds

If (CPT) holds, then \(H_P\le0\), hence

$$
F_P
\le
\sum_{L\in\partial P}
\left[
(\mathfrak B_L-O_L)_+
-
(-O_L)_+
\right].
$$

The right-hand side is nonnegative, so

$$
\boxed{
F_P^+
\le
\sum_{L\in\partial P}
\left[
(\mathfrak B_L-O_L)_+
-
(-O_L)_+
\right].
}
$$

Equivalently,

$$
\boxed{
\sum_{i\in U^\times\setminus P}S_i
\le
\sum_{\substack{L\subset U\\L\not\subset P}}
(\mathfrak B_L-O_L)_+
+
R_U.
}
$$

This is exactly unit-scale closure. Combining it with flat deficit Stokes
gives all point-set cuts, hence the max-flow allocation. Summing the
allocated line inequalities gives

$$
\mathcal E_M(d)\ge\sum_L\mathfrak B_L.
$$

The local twisted \(N=4\) coercivity and the two-layer nullspace then force

$$
C^\tau\equiv0,
\qquad
C^Y\equiv0,
$$

and therefore

$$
\tau_a=\chi_a(t_0),
\qquad
D_a=\alpha_\star(1-\tau_a).
$$

Thus equality occurs only at the target delta or a translated delta.

The honest current status is therefore:

$$
\boxed{
\text{global delta optimality is reduced to the Anchored Component Payment
Theorem (CPT).}
}
$$

The remaining gap is no longer the original weighted Walsh cone theorem, the
flat Stokes theorem, compactness, rescaling, or the row audit. It is the
anchored/component endpoint payment theorem above.

## 43. Hard Checks On Component Capacities

The anchored/component formulation above is still not a proof. Two hard
checks sharpen the remaining obstruction. One boundary-zero component
obstruction disappears, but full line-capacity nonnegativity is reduced to
two explicit twisted \(N=4\) bad cones.

### 43.1 Line Capacity Audit

For a boundary line

$$
L=\{i,j,k\},
$$

write

$$
T_{ij}^L
=
\int_0^1 t\,d_id_jH_{ij}(t)\,dt,
$$

and set

$$
S_L=T_{ij}^L+T_{ik}^L+T_{jk}^L.
$$

Then

$$
O_L=2S_L.
$$

Let

$$
J=L\cap B,
\qquad
m=|J|.
$$

The non-row residual is

$$
N_L=\sum_{q\in J}T_{L\setminus\{q\}}^L,
$$

where \(T_{L\setminus\{q\}}^L\) denotes the pair term opposite \(q\).
Define the actual line capacity

$$
\boxed{
C_L
=
(\mathfrak B_L-O_L)_+
-
\left(
N_L-\frac m2O_L
\right).
}
$$

Equivalently,

$$
\boxed{
C_L
=
(\mathfrak B_L-2S_L)_+
-
\left(
N_L-mS_L
\right).
}
\tag{43.1}
$$

This is the quantity that must pay positive amplitude residuals in the
component Hall theorem. The audit by the number \(m=|L\cap B|\) is as
follows.

If \(m=0\), then \(N_L=0\), so

$$
C_L=(\mathfrak B_L-2S_L)_+\ge0.
$$

Thus zero-missing-active boundary lines are safe.

If \(m=3\), then

$$
N_L=S_L.
$$

Hence

$$
N_L-mS_L=-2S_L,
$$

and therefore

$$
C_L=(\mathfrak B_L-2S_L)_+ +2S_L.
$$

If \(\mathfrak B_L\ge2S_L\), then \(C_L=\mathfrak B_L\ge0\). If
\(\mathfrak B_L<2S_L\), then \(2S_L>\mathfrak B_L\ge0\), so \(C_L=2S_L>0\).
Thus

$$
\boxed{
m=3\Longrightarrow C_L\ge0.
}
$$

The all-missing-active case is also safe.

If \(m=2\), write

$$
J=\{i,j\},
\qquad
k\notin B,
$$

and set

$$
N=N_L=T_{ik}^L+T_{jk}^L.
$$

Then

$$
S_L=T_{ij}^L+N,
$$

and

$$
C_L
=
(\mathfrak B_L-2S_L)_+
-
(N-2S_L).
$$

Therefore

$$
\boxed{
C_L\ge0
\Longleftrightarrow
\mathfrak B_L\ge N
\ \text{or}\
2S_L\ge N.
}
\tag{43.2}
$$

This proves that the old two-missing-active counterexample is harmless. In
that obstruction one has

$$
d_k=0,
\qquad
T_{ik}^L=T_{jk}^L=0,
\qquad
N=0,
$$

so (43.2) is automatic. The line receives no linear amplitude charge, and
its own capacity is nonnegative.

If \(m=1\), write

$$
J=\{i\},
$$

and set

$$
N=T_{jk}^L,
\qquad
R=T_{ij}^L+T_{ik}^L.
$$

Then

$$
S_L=N+R,
$$

and

$$
N_L-mS_L=N-(N+R)=-R.
$$

Thus

$$
C_L
=
(\mathfrak B_L-2N-2R)_+
+R.
$$

Consequently,

$$
\boxed{
C_L\ge0
\Longleftrightarrow
R\ge0
\ \text{or}\
\mathfrak B_L\ge2N+R.
}
\tag{43.3}
$$

On an anchored calibrated line, \(N=0\) and \(R<0\). Then the threshold
\(2N+R=R<0\) lies below \(\mathfrak B_L\ge0\), and the calibrated zero face
has positive slack

$$
C_L=-R>0.
$$

This is the rank-one killed slack mechanism. Away from the calibrated face,
however, the \(m=1\) case has a genuine bad cone:

$$
R<0,
\qquad
\mathfrak B_L<2N+R.
$$

This bad cone is not excluded by positive semidefiniteness of the ambient
Hessian. For example, the off-diagonal data

$$
T_{jk}^L=1,
\qquad
T_{ij}^L=T_{ik}^L=-0.4
$$

give

$$
N=1,
\qquad
R=-0.8,
\qquad
S_L=0.2,
\qquad
O_L=0.4.
$$

If \(\mathfrak B_L=0.1\), then

$$
C_L=(0.1-0.4)_+-0.8=-0.8<0.
$$

The symmetric matrix

$$
\begin{pmatrix}
2&-0.4&-0.4\\
-0.4&2&1\\
-0.4&1&2
\end{pmatrix}
$$

is positive definite, so this failure is not ruled out by Hessian positivity.

Thus full line-capacity nonnegativity cannot be proved from
\(\mathfrak B_L\ge0\) and positive curvature alone. It is reduced to the
following two local twisted \(N=4\) inequalities:

$$
\boxed{
m=1:
\quad
R=T_{ij}^L+T_{ik}^L<0
\Longrightarrow
\mathfrak B_L\ge 2T_{jk}^L+T_{ij}^L+T_{ik}^L,
}
\tag{43.4}
$$

and

$$
\boxed{
m=2:
\quad
2S_L<N_L
\Longrightarrow
\mathfrak B_L\ge N_L.
}
\tag{43.5}
$$

Every other case in the line-capacity audit is already safe.

### 43.2 No-Anchor Components At Boundary Zero

The most dangerous component-level scenario was a missing-active component
with no direct active anchor. At boundary zero this scenario cannot occur.

Assume

$$
\mathfrak B_L=0
\qquad(L\in\partial P).
$$

Then every boundary line satisfies

$$
\tau_{a+b}=\tau_a\tau_b.
$$

Let

$$
B=Q\cap M,
\qquad
Q=U^\times\setminus P.
$$

Suppose, toward contradiction, that

$$
B\ne\varnothing,
\qquad
P\cap M=\varnothing.
$$

Then

$$
\tau_p=+1
\qquad(p\in P).
$$

Set \(\tau_0=1\). Since \(P\) spans \(U\), every \(x\in U\) can be written
as

$$
x=p_1+\cdots+p_r,
\qquad
p_\ell\in P.
$$

Let

$$
r_k=p_1+\cdots+p_k.
$$

We prove by induction that

$$
\tau_{r_k}=1
\qquad(k=0,\dots,r).
$$

This is true for \(r_0=0\). If it is true for \(r_{k-1}\), then either
\(r_k\in P\), in which case \(\tau_{r_k}=1\), or the line

$$
\{r_{k-1},p_k,r_k\}
$$

is a boundary line whenever it is nondegenerate. Boundary-zero
multiplicativity then gives

$$
\tau_{r_k}
=
\tau_{r_{k-1}}\tau_{p_k}
=
1.
$$

In the degenerate case \(r_k=0\), the same conclusion follows from
\(\tau_0=1\). Therefore

$$
\tau_x=1
\qquad(x\in U).
$$

Thus

$$
M\cap U^\times=\varnothing,
$$

and in particular

$$
B=Q\cap M=\varnothing,
$$

contradicting \(B\ne\varnothing\). Hence

$$
\boxed{
B\ne\varnothing
\quad\text{and boundary zero}
\quad\Longrightarrow\quad
P\cap M\ne\varnothing.
}
\tag{43.6}
$$

Moreover, once \(P\cap M\ne\varnothing\), every missing active point has a
direct active anchor. For any

$$
q\in B,
\qquad
a\in P\cap M,
$$

the line

$$
L=\{q,a,q+a\}
$$

is a boundary line because \(q\notin P\). Since

$$
\tau_q=\tau_a=-1,
$$

boundary-zero multiplicativity gives

$$
\tau_{q+a}=+1.
$$

Thus \(L\) is a one-missing-active anchored line:

$$
q\in B,
\qquad
a\in P\cap M,
\qquad
q+a\notin M.
$$

So a boundary-zero missing-active component with no direct active anchor does
not exist. Equivalently, any no-anchor missing-active component away from
boundary zero must carry a nonzero boundary sign defect. Since the sign
defect is discrete,

$$
C_L^\tau\in\{0,\pm2\},
$$

the local coercivity

$$
\mathfrak B_L
\ge
W_L(C_L^\tau)^2+Q_L(C_L^Y)^2
$$

then supplies a fixed sign-cell reserve near that pattern. The no-anchor
component is therefore not a linear-vs-quadratic obstruction at the
boundary-zero face.

### 43.3 Remaining Hall Theorem

The component Hall payment theorem is now sharper but still open. In terms
of the capacities \(C_L\), the endpoint identity can be written as

$$
\boxed{
H_P
=
-P_U
+\sum_{q\in B}E_q^{\rm amp}
-\sum_{L\in\partial P}C_L.
}
\tag{43.7}
$$

Since negative amplitude residuals help, it is enough to pay

$$
E_q^+=(E_q^{\rm amp})_+.
$$

The remaining capacity theorem is the subset Hall family

$$
\boxed{
\sum_{q\in X}E_q^+
\le
P_U
+
\sum_{\substack{L\in\partial P\\L\cap X\ne\varnothing}}C_L
\qquad(X\subseteq B).
}
\tag{43.8}
$$

Taking \(X=B\) gives \(H_P\le0\), hence unit-scale closure. The downstream
chain from Sections 28-30 then gives point-set cuts, max-flow allocation,
the global endpoint lower bound, and the two-layer nullspace conclusion.

The hard-check status is therefore:

$$
\boxed{
\text{no-anchor component obstruction is dissolved at boundary zero;}
}
$$

$$
\boxed{
\text{the old two-missing-active linear obstruction is dissolved;}
}
$$

$$
\boxed{
C_L\ge0
\text{ in full generality is reduced to the two bad cones (43.4) and
(43.5);}
}
$$

and

$$
\boxed{
\text{the subset Hall inequalities (43.8) remain the final component
payment theorem.}
}
$$

Thus the proof is not complete. The next genuinely local task is the full
twisted \(N=4\) normal-form verification of (43.4) and (43.5), with the
actual unrescaled \(\mathfrak B_L\). The next genuinely global task is the
Hall routing inequality (43.8), using those capacities together with the
augmented flat surplus \(P_U\).

## 44. Signed Soft Closure Cut

The component Hall formulation above is no longer the shortest closure route.
Keeping the amplitude residual signed gives a sharper invariant target.

For a flat \(U\), a spanning set \(P\subset U^\times\), and

$$
Q=U^\times\setminus P,
\qquad
B=Q\cap M,
$$

write

$$
h_\varepsilon(y)=\varepsilon\log(1+e^{y/\varepsilon}),
\qquad
w_L^\varepsilon
=
h_\varepsilon(\mathfrak B_L-O_L).
$$

The exact endpoint identity from Section 42 gives

$$
H_P
=
\sum_{q\in B}S_q
-R_U
-
\sum_{L\in\partial P}(\mathfrak B_L-O_L)_+.
$$

Therefore define the smoothed closure functional

$$
\boxed{
\mathscr C_\varepsilon(P)
:=
R_U-\sum_{q\in B}S_q
+
\sum_{L\in\partial P}w_L^\varepsilon .
}
\tag{44.1}
$$

Then

$$
\boxed{
\mathscr C_\varepsilon(P)
=
-H_P
+
\sum_{L\in\partial P}
\left[
h_\varepsilon(\mathfrak B_L-O_L)
-
(\mathfrak B_L-O_L)_+
\right].
}
\tag{44.2}
$$

Since

$$
0\le h_\varepsilon(y)-y_+\le \varepsilon\log2,
$$

the limit \(\varepsilon\downarrow0\) is exactly

$$
\mathscr C_0(P)=-H_P.
$$

Thus the unit-scale closure theorem is equivalent to the smoothed scalar cut

$$
\boxed{
\mathscr C_\varepsilon(P)\ge0
\qquad(\varepsilon>0),
}
\tag{SC_\varepsilon}
$$

uniformly as \(\varepsilon\downarrow0\). In hard form this is

$$
\boxed{
\sum_{q\in B}S_q
\le
R_U+
\sum_{L\in\partial P}(\mathfrak B_L-O_L)_+ .
}
\tag{44.3}
$$

This is precisely the closure-filling inequality needed in Section 30.
Combining it with flat deficit Stokes gives

$$
\Phi(P)\ge\Phi(U)-R_U\ge0,
$$

and the max-flow allocation from Section 28 then supplies the global
line-cell lower bound. In this minimal route the BSA/PAR split and the
subset Hall payment theorem are proof devices, not logical necessities.

### 44.1 Signed Direct Form

The same cut can be written in the row-defect variables. From Section 42,

$$
\sum_{q\in B}\Gamma_q-R_U
=
\sum_{q\in B}E_q^{\rm amp}
+
\sum_{L\in\partial P}N_L
-
P_U,
$$

and

$$
\sum_{q\in B}S_q
=
\sum_{q\in B}\Gamma_q
-
\sum_{L\in\partial P}\frac{m_L}{2}O_L.
$$

Consequently

$$
\boxed{
\mathscr C_\varepsilon(P)
=
P_U
-
\sum_{q\in B}E_q^{\rm amp}
+
\sum_{L\in\partial P}
\left[
h_\varepsilon(\mathfrak B_L-O_L)
-
\left(
N_L-\frac{m_L}{2}O_L
\right)
\right].
}
\tag{44.4}
$$

This is the invariant signed-direct gauge. Negative amplitude residuals help
the closure inequality and should not be replaced by a positive-part routing
unless one wants the stronger internal Hall theorem.

Equivalently, if

$$
\nu_L=h_\varepsilon'(\mathfrak B_L-O_L),
$$

then

$$
h_\varepsilon(y)
=
\nu_Ly+\varepsilon H(\nu_L),
\qquad
H(\nu)=-\nu\log\nu-(1-\nu)\log(1-\nu),
$$

so (44.4) becomes

$$
P_U
-
\sum_{q\in B}E_q^{\rm amp}
+
\sum_{L\in\partial P}
\left[
\nu_L\mathfrak B_L-\nu_LO_L
-
\left(
N_L-\frac{m_L}{2}O_L
\right)
+
\varepsilon H(\nu_L)
\right]
\ge0.
\tag{44.5}
$$

The hinge curvature term is nonnegative and appears only from the actual
soft demand \((\mathfrak B_L-O_L)_+\). This is the smooth Bregman identity
that must be derived from the augmented flat KL/Poisson/Jensen chain rule.

### 44.2 Reverse Banking Has No Ordering Obstruction

The failed forward rank-one closure chain is replaced by a reverse banked
certificate. Let

$$
U^\times=A_0\supset A_1\supset\cdots\supset A_m=P
$$

remove the points \(x_r\in Q\). If \(Q'\subseteq Q\) is the set of points not
yet removed, define the remaining future credit

$$
W_{\rm rem}(Q')
=
\sum_{\substack{L\in\partial P\\\varnothing\ne L\cap Q\subseteq Q'}}
w_L^\varepsilon
$$

and the remaining supply

$$
S(Q')=\sum_{x\in Q'}S_x.
$$

Removing \(x\in Q'\) releases

$$
D_x(Q')
=
W_{\rm rem}(Q')-W_{\rm rem}(Q'\setminus\{x\})
=
\sum_{\substack{L\in\partial P\\x\in L\\L\cap Q\subseteq Q'}}
w_L^\varepsilon .
$$

If the current bank is \(b\), the quantity

$$
b+W_{\rm rem}(Q')-S(Q')
$$

is invariant under the update

$$
b^+=b+D_x(Q')-S_x.
$$

Hence a nonnegative-bank reverse ordering exists if and only if

$$
R_U+W_{\rm rem}(Q)-S(Q)\ge0,
$$

which is exactly \((SC_\varepsilon)\). Indeed, suppose at some stage

$$
b+W_{\rm rem}(Q')-S(Q')\ge0,
\qquad
b\ge0.
$$

If every \(x\in Q'\) failed the next-step bank condition, then

$$
S_x>b+D_x(Q')
\qquad(x\in Q').
$$

Summing over \(x\in Q'\) gives

$$
S(Q')>|Q'|b+\sum_{x\in Q'}D_x(Q').
$$

Every remaining future-credit line is counted at least once in
\(\sum_xD_x(Q')\), hence

$$
\sum_{x\in Q'}D_x(Q')\ge W_{\rm rem}(Q').
$$

Therefore

$$
S(Q')>|Q'|b+W_{\rm rem}(Q')\ge b+W_{\rm rem}(Q'),
$$

contradicting the invariant inequality. Thus some \(x\) can be removed while
keeping the bank nonnegative, and induction gives the reverse ordering.

The ordering problem is therefore solved: reverse banking is calibrated,
including on translated-delta equality faces. But it does not prove the
analytic inequality; it is equivalent to the scalar smoothed closure cut.

### 44.3 Fractional Cut Form

The family of smoothed closure cuts also has a useful coarea dual. For
\(0\le\theta_x\le1\), put

$$
\Theta_L=\max_{x\in L\cap Q}\theta_x.
$$

The set-cut family

$$
S(Q_*)\le R_U+
\sum_{\substack{L\in\partial P\\L\cap Q_*\ne\varnothing}}
w_L^\varepsilon
\qquad(Q_*\subseteq Q)
$$

is equivalent, by layer cake, to

$$
\boxed{
\sum_{x\in Q}\theta_xS_x
\le
R_U+
\sum_{L\in\partial P}w_L^\varepsilon\Theta_L
\qquad(0\le\theta\le1).
}
\tag{44.6}
$$

Indeed, with \(Q_t=\{x:\theta_x\ge t\}\),

$$
\sum_x\theta_xS_x
-
\sum_Lw_L^\varepsilon\Theta_L
=
\int_0^1
\left[
S(Q_t)
-
\sum_{\substack{L\in\partial P\\L\cap Q_t\ne\varnothing}}
w_L^\varepsilon
\right]dt.
$$

This is another exact formulation of the same analytic wall. A proof may try
to produce nonnegative augmented square terms for the left side of (44.6).

### 44.4 Extremal Obstruction Profile

If the smoothed closure cut fails, choose \(Q_*\subseteq Q\) maximizing

$$
\mathcal D(Q_*)
=
S(Q_*)
-
\sum_{\substack{L\in\partial P\\L\cap Q_*\ne\varnothing}}
w_L^\varepsilon .
$$

Then \(\mathcal D(Q_*)>R_U\), and the maximizer obeys the local Euler
conditions

$$
\boxed{
S_x
\ge
\sum_{\substack{L\in\partial P\\L\cap Q_*=\{x\}}}
w_L^\varepsilon
\qquad(x\in Q_*),
}
\tag{44.7}
$$

and

$$
\boxed{
S_x
\le
\sum_{\substack{L\in\partial P\\x\in L\\L\cap Q_*=\varnothing}}
w_L^\varepsilon
\qquad(x\in Q\setminus Q_*).
}
\tag{44.8}
$$

Thus any counterexample is a self-supporting soft closure component. If

$$
U_x(Q_*)
=
\sum_{\substack{L\in\partial P\\L\cap Q_*=\{x\}}}
w_L^\varepsilon,
\qquad
W_{\ge2}(Q_*)
=
\sum_{\substack{L\in\partial P\\|L\cap Q_*|\ge2}}
w_L^\varepsilon,
$$

then

$$
\mathcal D(Q_*)
=
\sum_{x\in Q_*}\bigl(S_x-U_x(Q_*)\bigr)
-
W_{\ge2}(Q_*).
$$

At a maximizing obstruction the summands
\(S_x-U_x(Q_*)\) are nonnegative by (44.7), so failure is exactly the
component inequality

$$
\boxed{
\sum_{x\in Q_*}\bigl(S_x-U_x(Q_*)\bigr)
>
R_U+W_{\ge2}(Q_*).
}
\tag{44.9}
$$

The remaining proof obligation is therefore no longer a line-local capacity
theorem, a forward rank-one monotonicity theorem, or a separate BSA/PAR Hall
routing theorem. It is the scalar augmented-buffer cut:

$$
\boxed{
R_U-\sum_{q\in B}S_q
+
\sum_{L\in\partial P}h_\varepsilon(\mathfrak B_L-O_L)
\ge0,
}
$$

or equivalently the exclusion of the self-supporting obstruction
(44.9), directly from the augmented flat KL/Poisson/Jensen chain rule.

### 44.5 Residual Augmented-Buffer Inequality

The preceding obstruction profile can be made exact. For every
\(Q_*\subseteq Q\), the set

$$
P_*:=U^\times\setminus Q_*
$$

contains \(P\), hence is spanning. The smoothed closure cut for \(P_*\) is

$$
\boxed{
\mathfrak R_\varepsilon(Q_*)
:=
R_U+
\sum_{\substack{L\subset U\\L\cap Q_*\ne\varnothing}}
h_\varepsilon(\mathfrak B_L-O_L)
-
\sum_{x\in Q_*}S_x
\ge0.
}
\tag{44.10}
$$

Thus the closure theorem for all spanning supersets of \(P\) is equivalent
to

$$
\mathfrak R_\varepsilon(Q_*)\ge0
\qquad(Q_*\subseteq Q).
$$

Keep

$$
w_L^\varepsilon=h_\varepsilon(\mathfrak B_L-O_L),
$$

and define

$$
W(Q_*)=
\sum_{\substack{L\subset U\\L\cap Q_*\ne\varnothing}}
w_L^\varepsilon,
\qquad
S(Q_*)=\sum_{x\in Q_*}S_x.
$$

For \(x\in Q_*\), set

$$
U_x(Q_*)
=
\sum_{\substack{L\subset U\\L\cap Q_*=\{x\}}}
w_L^\varepsilon,
$$

and

$$
W_{\ge2}(Q_*)
=
\sum_{\substack{L\subset U\\|L\cap Q_*|\ge2}}
w_L^\varepsilon.
$$

Then exactly

$$
W(Q_*)=\sum_{x\in Q_*}U_x(Q_*)+W_{\ge2}(Q_*),
$$

and therefore

$$
\boxed{
S(Q_*)-W(Q_*)
=
\sum_{x\in Q_*}\bigl(S_x-U_x(Q_*)\bigr)
-
W_{\ge2}(Q_*).
}
\tag{44.11}
$$

So the closure cut for \(Q_*\) is equivalent to

$$
\boxed{
\sum_{x\in Q_*}\bigl(S_x-U_x(Q_*)\bigr)
\le
R_U+W_{\ge2}(Q_*).
}
\tag{44.12}
$$

This is the residual component form: one-touch lines pay their unique exposed
endpoint first; the leftover exposed supply must be absorbed by the flat
reservoir and the multi-touch soft line cells.

If

$$
a_x(Q_*):=S_x-U_x(Q_*)\le0,
$$

then deleting \(x\) cannot decrease the deficit \(S(Q_*)-W(Q_*)\). Indeed,
with \(Q'=Q_*\setminus\{x\}\),

$$
W(Q')=W(Q_*)-U_x(Q_*),
\qquad
S(Q')=S(Q_*)-S_x,
$$

so

$$
S(Q')-W(Q')
=
S(Q_*)-W(Q_*)-a_x(Q_*).
$$

Thus every counterexample can be stripped until it is self-supporting:

$$
\boxed{
S_x>U_x(Q_*)
\qquad(x\in Q_*).
}
\tag{44.13}
$$

Inactive missing points automatically disappear in this stripping process,
because \(S_x=0\) and \(U_x(Q_*)\ge0\). Hence every minimal residual
obstruction lies inside \(B=Q\cap M\).

The exact residual component theorem is therefore:

$$
\boxed{
\sum_{x\in Q_*}
\left[
S_x-
\sum_{\substack{L\subset U\\L\cap Q_*=\{x\}}}
h_\varepsilon(\mathfrak B_L-O_L)
\right]
\le
R_U+
\sum_{\substack{L\subset U\\|L\cap Q_*|\ge2}}
h_\varepsilon(\mathfrak B_L-O_L)
}
\tag{RC}
$$

for every self-supporting \(Q_*\subseteq B\). The previous paragraphs prove

$$
\boxed{
(SC_\varepsilon)
\Longleftrightarrow
(RC).
}
\tag{44.14}
$$

Thus the combinatorial reduction is closed.

There is also a stronger extremal normal form. Since \(W\) is a coverage
function, it is submodular, and

$$
\mathcal D(Q')=S(Q')-W(Q')
$$

is supermodular. If closure fails and \(Q_*\) maximizes \(\mathcal D\), then
for every \(Y\subseteq Q_*\),

$$
\boxed{
\sum_{x\in Y}S_x
\ge
\sum_{\substack{L\subset U\\\varnothing\ne L\cap Q_*\subseteq Y}}
w_L^\varepsilon.
}
\tag{44.15}
$$

This is deletion stability. Likewise, for every \(Z\subseteq Q\setminus Q_*\),

$$
\boxed{
\sum_{z\in Z}S_z
\le
\sum_{\substack{L\subset U\\L\cap Q_*=\varnothing\\L\cap Z\ne\varnothing}}
w_L^\varepsilon.
}
\tag{44.16}
$$

This is addition stability. The singleton case of (44.15) is the
self-supporting condition (44.13), after stripping zero-slack points.

In the signed-direct gauge, define

$$
m_L(Q_*)=|L\cap Q_*|,
$$

and

$$
N_L^{Q_*}
=
\sum_{q\in L\cap Q_*}T_{L\setminus\{q\}}^L.
$$

The same residual can be written as

$$
\boxed{
\mathfrak R_\varepsilon(Q_*)
=
P_U
-
\sum_{x\in Q_*}E_x^{\rm amp}
+
\sum_{\substack{L\subset U\\L\cap Q_*\ne\varnothing}}
\left[
h_\varepsilon(\mathfrak B_L-O_L)
-
\left(
N_L^{Q_*}-\frac{m_L(Q_*)}{2}O_L
\right)
\right].
}
\tag{44.17}
$$

This is the form that the augmented chain rule must make nonnegative. The
recorded row-decomposed audit supplies the boundary-zero layer, but it does
not yet imply (44.17) off that face: the signed amplitude defects
\(E_x^{\rm amp}\) and non-row leakages \(N_L^{Q_*}\) are precisely the
terms that must be absorbed by the actual sealed horizontal branch and the
actual augmented KL/Poisson/Jensen chain rule.

A tempting analytic bridge would be a branch-specific square identity of the
form

$$
\boxed{
\begin{aligned}
\mathfrak R_\varepsilon(Q_*)
&=
R_U+W_{\ge2}(Q_*)
-
\sum_{x\in Q_*}\bigl(S_x-U_x(Q_*)\bigr)
\\
&=
\int_0^1 t\,|\mathcal Z_{Q_*,\varepsilon}(t)|^2\,dt
+
\mathcal R_{Q_*,\varepsilon}^{\perp}
+
\sum_L\mathcal R_{L,Q_*,\varepsilon}^{\rm hinge}
\ge0.
\end{aligned}
}
\tag{44.18}
$$

Equivalently, in signed-direct form one needs

$$
\boxed{
\begin{aligned}
&P_U
-
\sum_{x\in Q_*}E_x^{\rm amp}
+
\sum_{\substack{L\subset U\\L\cap Q_*\ne\varnothing}}
\left[
h_\varepsilon(\mathfrak B_L-O_L)
-
\left(
N_L^{Q_*}-\frac{m_L(Q_*)}{2}O_L
\right)
\right]
\\
&\qquad =
\int_0^1 t\,|\mathcal Z_{Q_*,\varepsilon}(t)|^2\,dt
+
\mathcal R_{Q_*,\varepsilon}^{\perp}
+
\sum_L\mathcal R_{L,Q_*,\varepsilon}^{\rm hinge}
\ge0.
\end{aligned}
}
\tag{44.19}
$$

This identity is not a generic Schur or PSD consequence. Section 45 records
the correction: the common scalar augmented-Bregman version of this square
bridge is false. Thus (44.18), if it is to be rescued at all, must be a
genuinely non-Bregman signed Stokes or tangent-cone identity, not a single
KL/Poisson/Jensen Bregman square. Once a valid replacement for (44.18), or
equivalently (44.19), is proved, the remaining chain is formal:

$$
(RC)
\Longrightarrow
(SC_\varepsilon)
\Longrightarrow
(SC)
\Longrightarrow
\text{unit-scale closure}
\Longrightarrow
\text{point-set cuts}
\Longrightarrow
\text{max-flow allocation}
\Longrightarrow
\mathcal E_M(d)\ge\sum_L\mathfrak B_L.
$$

The twisted \(N=4\) coercivity and the two-layer nullspace then leave only
the target delta or a translated delta.

## 45. RAC/GERAB No-Go Audit

This section records the correction to the square-bridge route in Section
44.5. The residual augmented closure target remains the same:

$$
\boxed{
\mathfrak R_\varepsilon(Q_*)
=
R_U+
\sum_{L\cap Q_*\ne\varnothing}
h_\varepsilon(\mathfrak B_L-O_L)
-
\sum_{x\in Q_*}S_x
\ge0.
}
\tag{RAC}
$$

Equivalently, after the exposed-row rewrite and after discarding the harmless
\(m_L=3\) lines, the target is

$$
\boxed{
P_U-\sum_{x\in Q_*}E_x^{\rm amp}
+
\sum_{L:m_L=1,2}
\left[
\nu_L\mathfrak B_L+\varepsilon H(\nu_L)
+
\sum_{\{a,b\}\subset L}
(\theta_a+\theta_b-2\nu_L)T_{ab}^L
\right]
\ge0,
}
\tag{GERAB}
$$

where

$$
\theta_x=\mathbf 1_{x\in Q_*},
\qquad
\nu_L=h_\varepsilon'(\mathfrak B_L-O_L).
$$

The point of the audit is not to disprove RAC/GERAB. It disproves a stronger
compatibility theorem: RAC/GERAB cannot be obtained by making \(P_U\) and the
line cells \(\mathfrak B_L\) into pieces of one common scalar augmented
Bregman-square identity.

### 45.1 Exposed-Row Coefficients On One Line

Let

$$
L=\{a,b,c\},
\qquad
c=a+b.
$$

For this line, the exposed-row pair coefficients are

$$
c_{ab}=\theta_a+\theta_b-2\nu_L,
\qquad
c_{ac}=\theta_a+\theta_c-2\nu_L,
\qquad
c_{bc}=\theta_b+\theta_c-2\nu_L.
$$

The line-pair part of GERAB is

$$
c_{ab}T_{ab}^L+c_{ac}T_{ac}^L+c_{bc}T_{bc}^L.
$$

If this term came from the Hessian of a scalar Bregman potential \(\Psi\),
then, up to the harmless factor relating off-diagonal Hessian entries to
quadratic-form cross terms, one would need

$$
\Psi_{ab}\sim c_{ab}H_{ab},
\qquad
\Psi_{ac}\sim c_{ac}H_{ac},
\qquad
\Psi_{bc}\sim c_{bc}H_{bc}.
$$

### 45.2 Hessian-Curl Obstruction

Work in the four-point quotient \(U\simeq\mathbb F_2^2\). For

$$
F^*(x)=\mathbb E_U[X\log X],
\qquad
X=1+\sum_{r\ne0}x_r\chi_r,
$$

the entropy Hessian is

$$
H_{ij}(x)
=
\partial_i\partial_jF^*(x)
=
\mathbb E_U\left[\frac{\chi_i\chi_j}{X}\right]
=
\mathbb E_U\left[\frac{\chi_{i+j}}{X}\right].
$$

At the uniform point \(x=0\), so \(X=1\),

$$
H_{ij}(0)=\delta_{ij}.
$$

For the three distinct indices \(a,b,c\) on the line,

$$
\partial_cH_{ab}(0)
=
-\mathbb E_U[\chi_{a+b}\chi_c]
=
-1,
$$

and cyclically

$$
\partial_bH_{ac}(0)=-1,
\qquad
\partial_aH_{bc}(0)=-1.
$$

Therefore a scalar \(C^3\) potential must satisfy the Schwarz conditions

$$
\partial_c\Psi_{ab}
=
\partial_b\Psi_{ac}
=
\partial_a\Psi_{bc}.
$$

At the uniform point this forces

$$
\boxed{
c_{ab}=c_{ac}=c_{bc}.
}
$$

But for \(m_L=1\), say

$$
\theta_a=1,
\qquad
\theta_b=\theta_c=0,
$$

the coefficient triple is

$$
(c_{ab},c_{ac},c_{bc})
=
(1-2\nu_L,\,1-2\nu_L,\,-2\nu_L),
$$

which is never constant. For \(m_L=2\), say

$$
\theta_a=\theta_b=1,
\qquad
\theta_c=0,
$$

the coefficient triple is

$$
(c_{ab},c_{ac},c_{bc})
=
(2-2\nu_L,\,1-2\nu_L,\,1-2\nu_L),
$$

which is also never constant. Hence

$$
\boxed{
m_L=1,2
\quad\Longrightarrow\quad
\text{the exposed-row pair field is not Hessian-integrable.}
}
$$

No choice of the soft-hinge multiplier \(\nu_L\) repairs this, because the
term \(-2\nu_L\) shifts all three pairs equally.

### 45.3 Exact Curl Formula

The obstruction can be written as an exact line curl. At \(x=0\),

$$
\partial_c(c_{ab}H_{ab})
-
\partial_b(c_{ac}H_{ac})
=
-c_{ab}+c_{ac}
=
\theta_c-\theta_b.
$$

Cyclically,

$$
\partial_b(c_{ac}H_{ac})
-
\partial_a(c_{bc}H_{bc})
=
\theta_b-\theta_a,
$$

and

$$
\partial_a(c_{bc}H_{bc})
-
\partial_c(c_{ab}H_{ab})
=
\theta_a-\theta_c.
$$

Thus the exposed-row curl is exactly the discrete boundary of the exposed
indicator \(\theta\) around the Walsh line. It vanishes only in the harmless
cases \(m_L=0\) and \(m_L=3\). In the live cases \(m_L=1,2\), the curl is
nonzero and independent of the hinge parameter.

This is the sharper form of the no-go:

$$
\boxed{
\text{GERAB has nonzero Hessian curl on exposed-row lines.}
}
$$

### 45.4 Consequence For The Proof Architecture

The flat reservoir \(P_U\) is already a genuine Bregman/Pythagorean surplus,

$$
P_U
=
B_{\mathcal B_U}(G_-,G_+)+\mathcal R^\perp,
\qquad
B_{\mathcal B_U}
=
\int_0^1 t\,d_U^T\mathsf G_U(t)d_U\,dt,
\qquad
\mathsf G_U\succeq0.
$$

Likewise, on each smooth branch, the twisted line cell
\(\mathfrak B_L\), the endpoint amplitude terms, and the soft-hinge entropy
term are scalar objects and obey the usual third-derivative symmetries. If a
common scalar augmented KL/Poisson/Jensen Bregman-square identity existed,
subtracting these already-integrable pieces would leave another
Hessian-integrable object. The live exposed-row pair field is not
Hessian-integrable, so such a common-square identity cannot exist.

Therefore the following theorem is false:

$$
\boxed{
\begin{gathered}
\text{RAC/GERAB follows from one common scalar augmented Bregman square}\\
\text{built from }P_U\text{ and }\mathfrak B_L.
\end{gathered}
}
$$

What remains possible is narrower:

$$
\boxed{
\begin{gathered}
\text{RAC/GERAB may still be true, but it must be proved by a genuinely}\\
\text{non-Bregman signed endpoint cut/Stokes argument.}
\end{gathered}
}
$$

Section 46 adds a second no-go: the pointwise sealed tangent-cone theorem
itself is false. Thus the surviving proof target is the endpoint cut

$$
\boxed{
\mathfrak R_\varepsilon(Q_*)\ge0
}
$$

The new information is that the proof cannot collapse RAC into a single
scalar KL/Poisson/Jensen Bregman square. The live \(m_L=1,2\)
exposed-row terms carry a nonzero line curl, so any successful proof must
allow nonintegrable exposed-row cancellations rather than trying to hide them
inside one scalar potential.

## 46. Pointwise DCT Is False

Section 45 killed the common scalar Bregman-square route to RAC/GERAB. This
section records a second correction: the pointwise defect-cone theorem (DCT)
itself is false. RAC remains viable, but it must be proved as an endpoint cut
theorem, not by integrating monotonicity along the relaxed melt.

### 46.1 The Scalar All-Active Branch

Translate the target spike to the identity and take

$$
M=V^\times,
\qquad
R=\varnothing.
$$

Thus every nonzero Walsh coefficient is melting. On the delta side write

$$
S_a=-q,
\qquad
0\le q\le1,
\qquad
a\ne0.
$$

By symmetry,

$$
u_a=u(q),
\qquad
x_a=-q\,u(q)
\qquad(a\ne0).
$$

Set

$$
r(q)=q\,u(q).
$$

The density has two levels:

$$
X_q(s_\star)=A(q)=1-(N-1)r(q),
$$

and

$$
X_q(s)=B(q)=1+r(q)
\qquad(s\ne s_\star).
$$

For every nonzero \(a\),

$$
g_a=g(q)=\widehat{\log X_q}(a)
=
\frac1N\log\frac{A(q)}{B(q)}.
$$

On the delta side, \(0<r(q)<1/(N-1)\), so \(A(q)<B(q)\). Hence

$$
\boxed{
g(q)<0.
}
$$

The seal equation is

$$
S_ag_a+\log u_a=0.
$$

Since \(S_a=-q\), this gives

$$
\log u(q)=qg(q),
\qquad
\alpha(q):=-\log u(q)=-qg(q)>0.
$$

At \(q=0\), the implicit scalar equation has the uniform solution

$$
u(0)=1,
\qquad
\alpha(0)=0.
$$

By continuity,

$$
\boxed{
0<q\ll1
\quad\Longrightarrow\quad
\alpha(q)<1.
}
$$

### 46.2 The DCT Certificate Has The Wrong Sign

The regular \(\beta\)-equation is

$$
\operatorname{diag}(1/u)\beta+HS^2\beta=g.
$$

On the scalar branch, \(\beta_a=\beta(q)\) for all \(a\ne0\). The all-ones
vector is an eigenvector of \(H(q)\), say

$$
H(q)\mathbf 1=\lambda(q)\mathbf 1.
$$

Since \(H(q)\succ0\),

$$
\lambda(q)>0.
$$

Therefore the regular equation reduces to

$$
\left(u(q)^{-1}+q^2\lambda(q)\right)\beta(q)=g(q).
$$

The denominator is positive and \(g(q)<0\), so

$$
\boxed{
\beta(q)<0.
}
$$

Combining this with \(\alpha(q)<1\) for small positive \(q\), one obtains

$$
\beta(q)(1-\alpha(q))<0.
$$

In fact the local expansion at the zero multiplier is

$$
g(q)=-q+O(q^2),
\qquad
\alpha(q)=q^2+O(q^3),
\qquad
\beta(q)=-q+O(q^2),
$$

so the sign failure is immediate.

Since there are \(N-1\) active coordinates,

$$
\boxed{
\sum_{a\in M}\beta_a(1-\alpha_a)
=
(N-1)\beta(q)(1-\alpha(q))<0
}
$$

for all sufficiently small positive \(q\). This contradicts the pointwise
DCT inequality in the delta-side gauge,

$$
\sum_{a\in M}\beta_a(1-\alpha_a)\ge0.
$$

There is no fixed-sign repair. At \(q=1\), the branch is the delta endpoint
and

$$
\alpha(1)=\alpha_\star.
$$

For \(N\ge4\), \(\alpha_\star>1\), while still \(\beta(1)<0\). Hence

$$
\beta(1)(1-\alpha_\star)>0.
$$

Thus the reversed inequality would fail near the delta endpoint. The
pointwise defect-cone certificate changes sign on the scalar all-active
branch:

$$
\boxed{
\text{DCT is false as a pointwise monotonicity theorem.}
}
$$

### 46.3 Why This Does Not Disprove Endpoint Optimality

The scalar all-active relaxed branch passes through

$$
q=0,
\qquad
S_a=0,
\qquad
x_a=0,
\qquad
X\equiv1.
$$

Thus

$$
D(P\|U)=0
$$

at the zero multiplier, while the delta endpoint has

$$
D_\delta>0.
$$

So the relaxed path necessarily dips below the delta gap. This is allowed:
\(q=0\) is not a genuine orientation. The global theorem compares only
\(\pm1\) orientations, and the scalar endpoint theorem in Section 13 compares
the opposite endpoint with the delta endpoint without requiring monotonicity
through the relaxed zero multiplier.

The correct conclusion is therefore

$$
\boxed{
\text{the relaxed melt need not be monotone; endpoint comparison remains
viable.}
}
$$

### 46.4 Consequence For RAC

RAC is an endpoint cut theorem. It does not assert monotonicity along the
relaxed melt, so the scalar all-active counterexample to DCT does not touch
RAC. It only rules out the implication

$$
\boxed{
\text{pointwise DCT}
\Longrightarrow
\text{RAC}.
}
$$

The live theorem is now the endpoint residual closure cut

$$
\boxed{
R_U+
\sum_{L\cap Q_*\ne\varnothing}
h_\varepsilon(\mathfrak B_L-O_L)
\ge
\sum_{x\in Q_*}S_x.
}
$$

Equivalently, in the signed-direct exposed-row gauge, after the harmless
\(m_L=3\) sector has been separated,

$$
\boxed{
P_U-\sum_{x\in Q_*}E_x^{\rm amp}
+
\sum_{L:m_L=1,2}\mathcal L_L^\theta
\ge0,
}
\tag{RAC'}
$$

where

$$
\mathcal L_L^\theta
=
h_\varepsilon(\mathfrak B_L-O_L)
+
\sum_{\{a,b\}\subset L}
(\theta_a+\theta_b)T_{ab}^L.
$$

For \(m_L=3\),

$$
h_\varepsilon(\mathfrak B_L-O_L)+O_L
\ge
\mathfrak B_L
\ge0,
$$

so all-three-exposed lines cannot drive failure.

### 46.5 Exact RAC Obstruction

Split the live \(m_L=1,2\) line contributions into positive and negative
parts:

$$
L_+(Q_*)=
\sum_{L:m_L=1,2}(\mathcal L_L^\theta)_+,
$$

and

$$
L_-(Q_*)=
\sum_{L:m_L=1,2}(-\mathcal L_L^\theta)_+.
$$

Also split the amplitude residual:

$$
A_+(Q_*)=
\sum_{x\in Q_*}(E_x^{\rm amp})_+,
$$

and

$$
A_-(Q_*)=
\sum_{x\in Q_*}(-E_x^{\rm amp})_+.
$$

Let \(M_3(Q_*)\ge0\) denote the total contribution of the all-three-exposed
lines. Then

$$
\mathfrak R_\varepsilon(Q_*)
=
P_U
+
A_-(Q_*)
-
A_+(Q_*)
+
L_+(Q_*)
-
L_-(Q_*)
+
M_3(Q_*).
$$

Thus RAC can fail only if

$$
\boxed{
A_+(Q_*)+L_-(Q_*)
>
P_U+A_-(Q_*)+L_+(Q_*)+M_3(Q_*).
}
$$

Every genuine RAC counterexample must therefore contain either positive
amplitude residual, negative \(m_L=1,2\) exposed-row line deficit, or both.
The all-three-exposed sector cannot be the source of failure.

### 46.6 Corrected Route

The proof architecture is now:

$$
\boxed{
\text{do not use pointwise DCT monotonicity;}
}
$$

$$
\boxed{
\text{prove RAC directly as an endpoint residual cut;}
}
$$

$$
\boxed{
\text{use RAC to obtain point-set cuts and the max-flow allocation;}
}
$$

$$
\boxed{
\mathcal E_M(d)\ge\sum_L\mathfrak B_L;
}
$$

and then use the two-layer nullspace to force equality only at the target
delta or a translated delta.

In particular, RAC is stronger than a scalar endpoint inequality
\(\mathcal E_M(d)\ge0\). It is a full cut-family theorem. A scalar endpoint
inequality can hold while a subset cut fails; RAC is precisely the missing
closure mechanism that prevents such hidden local deficits.

## 47. Projection-Redundancy Conditional Route

This section records a second endpoint architecture. It does not replace RAC
and it does not revive DCT. It gives a different conditional certificate:
global delta optimality follows from a sealed-only stability theorem for
two-dimensional Walsh projections. In this route, the projection
decomposition and the universal Shearer inequality are proved; the remaining
input is isolated as the Sealed Projection-Stability Lemma.

### 47.1 Four-Point Walsh Line Quotients

Let

$$
L=\{a,b,a+b\}
$$

be a Walsh line. For a mean-one density

$$
X=1+\sum_{c\ne0}x_c\chi_c,
$$

define the quotient density on \(G/L^\perp\) by

$$
\boxed{
X_L(\eta_a,\eta_b)
=
1+x_a\eta_a+x_b\eta_b+x_{a+b}\eta_a\eta_b,
}
$$

where \(\eta_a,\eta_b\in\{\pm1\}\). This is the conditional expectation of
\(X\) onto the four-point quotient generated by \(L\).

Define the quotient entropy gap

$$
\boxed{
D_L(X)
=
\frac14\sum_{\eta_a,\eta_b=\pm1}
X_L(\eta_a,\eta_b)\log X_L(\eta_a,\eta_b).
}
$$

In the target gauge \(s_\star=1\), the full \(N\)-point delta density has

$$
x_c^\star=-u_\star
\qquad(c\ne0),
$$

so every line quotient is

$$
X_{L,\star}(\eta_a,\eta_b)
=
1-u_\star(\eta_a+\eta_b+\eta_a\eta_b).
$$

It has one value \(1-3u_\star\) and three values \(1+u_\star\). Set

$$
\boxed{
D_{L,\star}
=
\frac14
\left[
(1-3u_\star)\log(1-3u_\star)
+
3(1+u_\star)\log(1+u_\star)
\right].
}
$$

This number is independent of \(L\).

The number of Walsh lines is

$$
|\mathcal L|=\frac{(N-1)(N-2)}6.
$$

Set

$$
\boxed{
\gamma_n
=
\frac{n}{2|\mathcal L|}
=
\frac{3n}{(N-1)(N-2)}.
}
$$

### 47.2 Exact Projection Decomposition

Write

$$
H(X)=\log N-D(X),
\qquad
H(X_L)=\log4-D_L(X).
$$

Define the two-dimensional projection redundancy

$$
\boxed{
\mathcal R_2(X)
=
\gamma_n\sum_{L\in\mathcal L}H(X_L)-H(X).
}
$$

Also define the aggregate line quotient excess

$$
\boxed{
A_{\rm line}(X)
=
\sum_{L\in\mathcal L}
\left[D_L(X)-D_{L,\star}\right].
}
$$

Then, for every mean-one density \(X\),

$$
\boxed{
D(X)-D(X_\delta)
=
\gamma_nA_{\rm line}(X)
+
\mathcal R_2(X)-\mathcal R_2(X_\delta).
}
\tag{47.1}
$$

Indeed,

$$
\mathcal R_2(X)
=
\gamma_n\sum_L(\log4-D_L(X))-(\log N-D(X)).
$$

The constants cancel because

$$
\gamma_n|\mathcal L|\log4
=
\frac n{2|\mathcal L|}|\mathcal L|\cdot2\log2
=
\log N.
$$

Thus

$$
\mathcal R_2(X)=D(X)-\gamma_n\sum_LD_L(X).
$$

Subtract the same identity for \(X_\delta\), and use
\(D_L(X_\delta)=D_{L,\star}\) for every line. This proves (47.1).

Consequently, global delta optimality would follow if one could prove

$$
A_{\rm line}(X_\epsilon)\ge0
$$

and

$$
\mathcal R_2(X_\epsilon)\ge\mathcal R_2(X_\delta)
$$

for every sealed orientation density \(X_\epsilon\).

### 47.3 Universal Shearer Redundancy

The unshifted redundancy is universally nonnegative:

$$
\boxed{
\mathcal R_2(X)\ge0
}
$$

for every probability density \(X\) on \(G\). Equivalently,

$$
\boxed{
D(X)\ge\gamma_n\sum_{L\in\mathcal L}D_L(X).
}
$$

To prove this, sample \(Y\in G\) with density \(X\) relative to uniform.
Choose an ordered basis \(B=(b_1,\dots,b_n)\) of \(V=\mathbb F_2^n\), and
write

$$
Y_i=\chi_{b_i}(Y).
$$

The \(n\) signs \(Y_1,\dots,Y_n\) determine \(Y\). Shearer's inequality for
all coordinate pairs gives

$$
H(Y_1,\dots,Y_n)
\le
\frac1{n-1}\sum_{1\le i<j\le n}H(Y_i,Y_j).
$$

Average over ordered bases. By \(\operatorname{GL}(n,2)\)-symmetry, each
two-dimensional subspace occurs equally often as
\(\operatorname{span}\{b_i,b_j\}\). Hence

$$
H(X)
\le
\frac1{n-1}\binom n2
\frac1{|\mathcal L|}\sum_LH(X_L)
=
\gamma_n\sum_LH(X_L).
$$

This is exactly \(\mathcal R_2(X)\ge0\).

This universal fact is not enough for delta optimality, because

$$
\mathcal R_2(X_{\rm unif})=0
$$

whereas

$$
\mathcal R_2(X_\delta)>0.
$$

The shifted bound \(\mathcal R_2(X_\epsilon)\ge\mathcal R_2(X_\delta)\) must
therefore use the seal.

### 47.4 Defective-Line Counting

Fix the target delta sign pattern \(\sigma^\star\), and write

$$
\tau_a=\frac{\sigma_a}{\sigma_a^\star}\in\{\pm1\}.
$$

In target gauge, \(\sigma_a^\star=-1\), so \(\tau_a=-\sigma_a\). A translated
delta has

$$
\tau_a=\chi_a(t_0),
$$

hence \(\tau\) is a character. A line \(L=\{a,b,a+b\}\) is sign-defective
when

$$
\boxed{
\tau_{a+b}\ne\tau_a\tau_b.
}
$$

Let

$$
\rho=\frac N2-1,
$$

the number of Walsh lines through a fixed nonzero point.

If \(\tau\) is not a character, then at least \(\rho\) Walsh lines are
sign-defective. To see this, multiply \(\tau\) by a closest character and
reduce to the case where the closest character is \(1\). Let

$$
E=\{a:\tau_a=-1\}.
$$

A random character disagrees with \(\tau\) on \((N-1)/2\) nonzero points on
average, so the closest character gives

$$
1\le |E|\le \rho.
$$

Fix \(e\in E\). Of the \(\rho\) lines through \(e\), at most \(|E|-1\) contain
another point of \(E\). Hence at least \(\rho-|E|+1\) lines through \(e\)
contain exactly one error. Such lines are defective. Summing over
\(e\in E\) counts each one-error line once, giving at least

$$
|E|(\rho-|E|+1)\ge\rho
$$

defective lines.

This is a genuine global coboundary fact, but it is still not an entropy
floor: defective lines need not individually carry enough quotient entropy.
The useful lower bound has to be aggregate.

### 47.5 Projection Nullspace

The intended equality set is the translated-delta orbit. The projection
certificate has the right nullspace.

Suppose every line quotient is locally a translated-delta quotient. Then for
each \(L=\{a,b,a+b\}\),

$$
\tau_{a+b}=\tau_a\tau_b.
$$

Extending \(\tau_0=1\), \(\tau\) is multiplicative on \(V\), hence

$$
\tau_a=\chi_a(t_0)
$$

for some \(t_0\in G\). The local delta quotient condition also forces the
common amplitude

$$
|x_a|=u_\star
\qquad(a\ne0).
$$

Thus, in target gauge,

$$
x_a=-u_\star\chi_a(t_0),
$$

and therefore

$$
X(s)=1-u_\star\sum_{a\ne0}\chi_a(t_0)\chi_a(s).
$$

Using the Walsh identity

$$
\sum_{a\ne0}\chi_a(t_0)\chi_a(s)
=
\begin{cases}
N-1,&s=t_0,\\
-1,&s\ne t_0,
\end{cases}
$$

we get

$$
X(t_0)=1-(N-1)u_\star,
\qquad
X(s)=1+u_\star\quad(s\ne t_0).
$$

So \(X\) is exactly a translated sealed delta.

### 47.6 Sealed Projection-Stability Lemma

The missing input for this route is:

**Sealed Projection-Stability Lemma.** For every sealed orientation density
\(X_\epsilon\),

$$
\boxed{
\sum_{L\in\mathcal L}
\left[D_L(X_\epsilon)-D_{L,\star}\right]\ge0,
}
\tag{SPS-1}
$$

and

$$
\boxed{
\mathcal R_2(X_\epsilon)\ge\mathcal R_2(X_\delta).
}
\tag{SPS-2}
$$

Moreover, equality in both should occur only for translated sealed deltas.

The combined inequality

$$
\boxed{
\gamma_n
\sum_L
\left[D_L(X_\epsilon)-D_{L,\star}\right]
+
\mathcal R_2(X_\epsilon)-\mathcal R_2(X_\delta)
\ge0
}
\tag{SPS}
$$

with the same equality statement would also suffice.

Assuming SPS, global delta optimality follows immediately from (47.1):

$$
D(X_\epsilon)-D(X_\delta)
=
\gamma_nA_{\rm line}(X_\epsilon)
+
\mathcal R_2(X_\epsilon)-\mathcal R_2(X_\delta)
\ge0.
$$

The equality clause then forces \(X_\epsilon\) to be a translated sealed
delta.

### 47.7 Why SPS Is The Real Obstruction

Neither part of SPS is an ordinary entropy inequality. The uniform density
has

$$
D_L(X_{\rm unif})=0
\qquad(L\in\mathcal L),
$$

and

$$
\mathcal R_2(X_{\rm unif})=0,
$$

while \(D_{L,\star}>0\) and \(\mathcal R_2(X_\delta)>0\). Thus both shifted
floors fail for arbitrary densities. They must use the Fourier-log seal.

The projected seal shows where the difficulty sits. Since \(X_L\) is the
conditional expectation of \(X\) on the quotient \(G/L^\perp\), Jensen gives

$$
\log X_L(\eta)
=
\mathbb E[\log X\mid L=\eta]+J_L(\eta),
$$

where

$$
\boxed{
J_L(\eta)
=
D(U_{\rm fiber}\|P(\cdot\mid L=\eta))\ge0.
}
$$

Taking line Fourier coefficients gives, for \(i\in L\),

$$
\widehat{\log X_L}(i)
=
\widehat{\log X}(i)+\widehat J_L(i).
$$

The full seal gives

$$
\widehat{\log X}(i)
=
-\sigma_i\log u_i.
$$

Therefore the four-point quotient obeys the perturbed local seal

$$
\boxed{
\widehat{\log X_L}(i)
=
-\sigma_i\log u_i+\widehat J_L(i).
}
$$

The buffer \(J_L\) is pointwise nonnegative, but its line Fourier
coefficients \(\widehat J_L(i)\) have no fixed sign. Hence a linewise proof
cannot simply import the four-point problem. SPS must show that these
projected Jensen-buffer errors become favorable only after averaging over
all Walsh lines and using the global Fourier-log seal.

This is the exact current state of the projection route:

$$
\boxed{
\text{projection decomposition + Shearer + nullspace are proved;}
}
$$

$$
\boxed{
\text{Sealed Projection-Stability is the remaining sealed-only lemma.}
}
$$
