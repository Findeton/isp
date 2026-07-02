# The Gibbs–Defect Route To Walsh Delta Global Optimality

Companion to `walsh-delta-global-optimality-problem.md` (cited below as
[WD]). This note records a third proof architecture for the Global Delta
Optimality Problem, independent of the DCT/RAC machinery ([WD] §7–46) and of
the projection route ([WD] §47). It contains:

*(Revision note, 2026-07-02, final: the Global Delta Optimality Theorem is
PROVED for all $n$ in §6d — Theorem E (deep-dip trichotomy) + Theorem F
(assembly), audited by four hostile independent verifiers with zero
fatal/gap findings; see §10 for the trust base. Sections 7 and parts of
§6c/§8b predate the final step and are kept as the historical record of
the route: §7's L0/effectivity framework and §8b's limit problem are
superseded as *requirements* — the limit problem remains open only as the
route to the sharp asymptotic constant $4\log4$. Earlier same-day
revision: §7/§10 corrected after the first audit; details in the solve
log.)*

1. a complete existence/uniqueness theorem for the seal (§2);
2. an exact identity package that rewrites the sealed law as the Gibbs
   measure of the *defect-mass function* and reduces the entropy gap to a
   one-dimensional functional of its law (§3);
3. the exact classification of flat-spectrum sealed laws by difference sets
   (§4);
4. the dip-model rigidity theorem: in the idealized dip model, positivity of
   the two weight families plus the exponential seal link force a single dip
   — i.e. force the delta — whenever the dip set does not affinely span
   (§5); this includes an explicit counterexample showing that the one-sided
   spectral floor alone is *not* sufficient (§5.4);
5. quantitative structure theorems for low-gap sealed laws (§6);
6. the precise statement of the remaining lemma (L0, with its L1/L2 proof
   decomposition) and the effectivity condition under which it closes the
   full theorem, plus the finite-`n` status (§7);
7. numerical receipts: exhaustive scans for `n ≤ 4` (delta uniquely minimal;
   the landscape has a hard gap; both halves of the [WD] §47.6 SPS lemma
   hold exhaustively), probes for `n = 5, 6`, and mpmath (dps = 50)
   re-verification of the extreme values and the thinnest margin (§8).

Throughout, $G=\{\pm1\}^n \simeq \mathbb F_2^n$, $N=2^n$, characters
$\chi_a$ for masks $a\ne0$, orientation $\sigma\in\{\pm1\}^{N-1}$, uniform
law $U$. A *sealed law* for $\sigma$ is a probability law $P$ with density
$X=NP>0$ satisfying the seal equations of [WD] §4:
$\mathbb E_P[\sigma_a\chi_a]=e^{-h_a}$ with
$\widehat{\log X}(a)=\sigma_ah_a$. We write $x_a=\widehat X(a)$,
$u_a=|x_a|=e^{-h_a}$, $D=D(P\|U)$, $\bar D=D(U\|P)$.

## 1. Summary Of What Is New

The problem ([WD] §4) is to show $D(\epsilon)\ge D(\epsilon_\star)$ for all
orientations, with equality only on the delta orbit. [WD] establishes that
the pointwise DCT is false (§46), that RAC cannot be a single Bregman square
(§45), and leaves RAC and SPS as open closure targets. The route below
replaces the relaxed-melt/path objects by *endpoint identities only*: no
melt, no path integrals, no line cells. The entire nonlinearity of the seal
is compressed into one scalar function on the group — the defect-mass
function — and the delta emerges as the unique sign pattern whose
defect-mass function can be constant except at a single point.

## 2. Existence And Uniqueness Of The Seal

**Theorem 1.** For every $n\ge2$ and every orientation
$\sigma\in\{\pm1\}^{N-1}$ there exists exactly one sealed law $P_\sigma$.
It is the Gibbs law $P_\ell\propto\exp(\sum_a\ell_a\chi_a)$ at the unique
global minimizer $\ell^\ast$ of the smooth, strictly convex, coercive
function

$$
\boxed{\;G_\sigma(\ell)=F(\ell)+\sum_{a\ne0}e^{-\sigma_a\ell_a},\qquad
F(\ell)=\log\mathbb E_U\exp\Big(\sum_{a\ne0}\ell_a\chi_a\Big).\;}
$$

*Proof.* $\nabla^2F(\ell)=\operatorname{Cov}_{P_\ell}(\chi)\succ0$ because
$P_\ell$ has full support and $\{\chi_a\}_{a\neq0}\cup\{1\}$ is linearly
independent; the barrier terms are convex, so $G_\sigma$ is strictly convex.
Along any ray $\ell=tv$, $v\ne0$: $\mu(v):=\max_s\sum_av_a\chi_a(s)>0$
(the function $s\mapsto\langle v,\chi(s)\rangle$ is nonzero with zero mean),
so $F(tv)\ge t\mu(v)-\log N\to\infty$; the barriers are nonnegative. A
finite convex function tending to $+\infty$ along every ray is coercive,
so a unique minimizer $\ell^\ast$ exists. The critical equations are
$x_a=\sigma_ae^{-\sigma_a\ell_a}$, i.e. exactly the seal with
$h_a=\sigma_a\ell_a$; conversely every sealed law solves them. Since
$|x_a|=|\mathbb E_P\chi_a|<1$ for a full-support law, $h_a>0$
automatically. $\square$

Two consequences used constantly below: (i) each $\sigma$ has *one* gap
value $D(\sigma)$; (ii) numerically the seal is an unconstrained convex
Newton solve (this is what makes the exhaustive scans in §8 trivial).

## 3. The Gibbs–Defect Identity Package

Define for each point $s$ the *defect set* and *defect mass*

$$
M(s)=\{a\ne0:\ \sigma_a=\chi_a(s)\},\qquad
m(s)=2\!\!\sum_{a\in M(s)}\!\!h_a .
$$

$M(s)$ is the defect set of $\sigma$ relative to the delta orientation
centered at $s$; $\sigma$ is the delta at $s_0$ iff $M(s_0)=\varnothing$.
Also set $w(s)=\log N-\log X(s)\ge0$,
$z(s)=1-\sum_a\sigma_a\chi_a(s)$, and $\varphi(h)=he^{-h}$.

**Theorem 2 (identity package).** For every sealed law:

(a) **Gibbs form.**
$\;\log X(s)=c-\sum_ah_a+m(s)$ and hence
$$
\boxed{\;X(s)=\frac{e^{m(s)}}{\mathbb E_U[e^{m}]}\;}
$$
— the sealed law is the Gibbs measure of its own defect-mass function.

(b) **Law reduction.** $D$ depends only on the law $\mu$ of $m$ under $U$:
$$
\boxed{\;D=\Phi(\mu):=\frac{\mathbb E_\mu[me^{m}]}{\mathbb E_\mu[e^{m}]}
-\log\mathbb E_\mu[e^{m}]\;\ge0,}
$$
with $\Phi(\mu)=0$ iff $\mu$ is a point mass.

(c) **Depth–defect budget.** For every $s$:
$w(s)+m(s)=B$ where $B=\sum_ah_a+\log N+\bar D=\mathbb E_U[wz]$.
Hence $\max_sw=B-\min_sm$, and the normalization $\mathbb E X=1$ reads
$\sum_se^{m(s)}=e^{B}$.

(d) **Jeffreys identity.** $D+\bar D=\sum_a\varphi(h_a)\le (N-1)/e$.

(e) **Deep-pair exclusion.** For all $s\ne s'$, with $t=s+s'$:
$$
m(s)+m(s')\;\ge\;2H_t,\qquad
H_t=\sum_{a:\chi_a(t)=-1}h_a\;\ge\;\tfrac N2\,h_{\min},
$$
since $M(s)\,\Delta\,M(s')=\{a:\chi_a(t)=-1\}$, a set of exactly $N/2$
masks. Consequently **at most one point of $G$ can have
$m(s)<\tfrac N2h_{\min}$**: a sealed law has at most one deep candidate
delta center.

(f) **$z$-bookkeeping.** $z$ is even-integer valued, $\sum_sz=N$,
$\sum_sz^2=N^2$, and $z=N\mathbf 1_{s_0}$ iff $\sigma$ is the delta at
$s_0$.

*Proof.* (a): $\sum_a\sigma_ah_a\chi_a(s)=m(s)-\sum_ah_a$ by splitting masks
into $M(s)$ and its complement; exponentiate and normalize. (b): insert (a)
into $D=\mathbb E_U[X\log X]$. (c): from (a) and the definitions; the
formula $B=\mathbb E[wz]$ follows from
$\sum_ah_a=\sum_a|\widehat w(a)|=\mathbb E[w\,(z-1)]$ because
$\widehat w(a)=-\sigma_ah_a$ so the sign pattern $-\sigma$ extracts the
$\ell^1$ norm. (d): Parseval on $\mathbb E[(X-1)\log X]$ plus the seal.
(e): defect masses over a symmetric difference. (f): Parseval and Fourier
inversion. All six were verified to machine precision on orientations of
$n=3,4,5$ (worst error $1.9\times10^{-12}$, zero DP violations; §8). $\square$

**Theorem 3 (exact delta comparison).** For every orientation $\epsilon$
and every delta center $s_\star$ (with delta data $u_\star,h_\star,
A_\star=1-(N-1)u_\star$):
$$
\boxed{\;D(\epsilon)-D(\epsilon_\star)
= D(P_\epsilon\|P_{\delta,s_\star})
- h_\star\big(X_\epsilon(s_\star)-A_\star\big).\;}
$$

*Proof.* $\mathbb E[X_\epsilon\log X_\epsilon]-\mathbb E[X_\delta\log
X_\delta]=D(P_\epsilon\|P_\delta)+\mathbb E[(X_\epsilon-X_\delta)\log
X_\delta]$ and $\log X_\delta=c_\star-h_\star(N\mathbf 1_{s_\star}-1)$.
$\square$

In particular if $\min_sX_\epsilon(s)\le A_\star$ the theorem is immediate
for that $\epsilon$; the hard regime is competitors bounded away from the
simplex boundary — matching [WD] §9's boundary analysis, but obtained here
in one line.

## 4. Flat-Spectrum Sealed Laws Are Classified By Difference Sets

**Theorem 4.** Suppose a sealed law has flat spectrum: $h_a=\bar h$ for all
$a\ne0$. Then $z$ takes at most two values, and $S=\{s:z(s)=z_1\}$
(upper value) satisfies $|N\widehat{\mathbf 1_S}(a)|=\mathrm{const}$ for all
$a\ne0$ — i.e. **$S$ is a difference set in $\mathbb F_2^n$**. The
admissible parameter families are:

* $k=|S|=1$: the **delta** ($z=N\mathbf 1_{s_0}$), gap
  $D_\delta<\log\frac N{N-1}$;
* $k=N-1$: the **anti-delta** (all-plus at a point), gap $D_+$ large
  ([WD] §13: $D_+>D_\delta$, and in fact $D_+\to\log N$);
* nontrivial difference sets ($\mu\ge2$, which forces
  $k(N-k)=\mu^2(N-1)\ge4(N-1)$): by the classical theory of difference sets
  in elementary abelian 2-groups these have Hadamard/Menon parameters
  $k=(N\pm\sqrt N)/2$ ($n$ even; equivalently bent functions), so the two
  Gibbs levels each carry $\approx N/2$ points and the sealed two-level
  system forces $D\ge\log2-o(1)$.

*Proof sketch (first two claims are complete).* Flat spectrum makes both
$X=1+\bar u(1-z)$ and $\log X=c'-\bar hz$ affine in $z$; a strictly concave
function ($\log$) agrees with an affine function in at most two points, so
$z$ is two-valued. Writing $z=z_2+(z_1-z_2)\mathbf 1_S$, the seal's
unit-modulus spectrum $|\widehat z(a)|=1$ gives
$|\widehat{\mathbf 1_S}(a)|=1/(z_1-z_2)$ for all $a\ne0$: a difference set.
The moment constraints (Theorem 2(f)) then fix
$z_{1,2}=1+d_1,\,1-d_2$ with $d_1=m_0/k$, $d_2=m_0/(N-k)$,
$m_0=\sqrt{(N-1)k(N-k)}$, and $\mu:=N/(z_1-z_2)$ obeys
$\mu^2=k(N-k)/(N-1)$; $\mu=1$ iff $k\in\{1,N-1\}$. For the balanced
families, exponential level separation (forced by
$\bar u=e^{-\bar h}$ with $\bar h$ solving the two-level seal) kills half
the mass, giving the $\log 2$ floor. $\square$

Two corrections this classification makes to naive expectations: "flat
$\Rightarrow$ delta" is false — the anti-delta and bent configurations are
genuinely flat sealed laws — but every non-delta flat law has gap
$\ge\log2-o(1)\gg D_\delta$. Numerically at $n=4$: the bent orientations
sit at defect distance $6$ (the covering-radius extremal class) and the scan
gives their gap as $0.978$–$1.020$, vs $D_\delta=0.0645$.

## 5. The Dip Model And The Positivity Kill

### 5.1 The dip model

The structure theorems of §6 say a low-gap sealed law is, quantitatively, a
*dip configuration*: $X=X_b$ on a bulk, $X_j=X_be^{-\beta_j}$ at $k$
exceptional points $s_1,\dots,s_k$ with log-depths $\beta_j>0$. In the
idealized (exactly flat-bulk) model, Fourier inversion gives, for all
$a\ne0$, with weights $\mu_j:=1-e^{-\beta_j}\in(0,1)$:

$$
\widehat X(a)=-\frac{X_b}N\,G(a),\quad
\widehat{\log X}(a)=-\frac1N\,F(a),\qquad
G(a)=\sum_j\mu_j\chi_a(s_j),\ \ F(a)=\sum_j\beta_j\chi_a(s_j).
$$

The seal becomes the **two-sided matching system**

$$
\boxed{\;\operatorname{sgn}F(a)=\operatorname{sgn}G(a)\ (=-\sigma_a\cdot(\pm)),
\qquad
\frac{X_b}N\,|G(a)|=\exp\Big(-\frac{|F(a)|}N\Big)\quad(a\ne0).\;}
$$

Both weight families are strictly positive, and the second equation links
the two transforms through a *decreasing* exponential.

### 5.2 The positivity kill

**Theorem 5 (single-dip rigidity).** In the dip model, suppose the dip
points do not affinely span $\mathbb F_2^n$ (in particular whenever
$k\le n$). Then $k=1$, and the sign pattern is the delta at $s_1$.

*Proof.* Let $t_j=s_1+s_j$ and pick $a^\ast\ne0$ orthogonal to
$\langle t_2,\dots,t_k\rangle$ (possible since the span is proper). Then
$\chi_{a^\ast}(s_j)$ has a common sign over $j$, so
$|F(a^\ast)|=\sum_j\beta_j=\max_a|F(a)|$ and simultaneously
$|G(a^\ast)|=\sum_j\mu_j=\max_a|G(a)|$ (positivity of both weight
families). But the matching equation sends maxima of $|F|$ to *minima* of
$|G|$ — the exponential link inverts peaking. Hence $|G|$ attains its
maximum and its minimum at $a^\ast$, so $|G(a)|$ is constant, and so is
$|F(a)|$. Constancy of $|G|$ with positive weights forces
$$
(N-1)\Big(\sum_j\mu_j\Big)^2=\sum_{a\ne0}G(a)^2
=N\sum_j\mu_j^2-\Big(\sum_j\mu_j\Big)^2
\iff \Big(\sum_j\mu_j\Big)^2=\sum_j\mu_j^2,
$$
i.e. $\sum_{i\ne j}\mu_i\mu_j=0$, impossible for $k\ge2$ positive weights.
So $k=1$; then $\widehat X(a)=-(X_b\mu_1/N)\chi_a(s_1)$, giving
$\sigma_a=\operatorname{sgn}x_a=-\chi_a(s_1)$: the delta. $\square$

This is the endpoint mechanism that DCT/RAC sought as a flow/cut statement:
*positivity of dip depths and dip masses, plus the exponential seal link,
is already inconsistent with more than one dip.* Note it subsumes $k=2$
unconditionally (two points never affinely span for $n\ge2$).

### 5.3 What the theorem does and does not cover

It covers the idealized model with $k\le n$ (and any non-spanning $k$). It
does not yet cover (i) the *quantitative* version, where the bulk is only
$\ell^2$-flat to $O(\sqrt D)$ and the dips only approximately point-like;
(ii) spanning configurations with $k\ge n+1$ (up to $O(DN)$ dips are
a priori allowed by the budget of §6). These are the two cases of
Lemma L0's intended proof (§7).

### 5.4 The one-sided floor is not enough (counterexample)

One might hope the spectral floor alone suffices: if all
$|\widehat{\log X}(a)|\ge\eta$ and the Gibbs gap is small, must the signs be
delta? **No.** Take three points of an affine plane
$\{s_1,s_2,s_3\}\subset\{s_1,s_2,s_3,s_4\}$ and
$f=-d\,N(\mathbf 1_{s_1}+\mathbf 1_{s_2}+\mathbf 1_{s_3})+\mathrm{const}$:
then $|\widehat f(a)|\in\{d,3d\}$ on the four sign classes — full spectrum
with $\eta=d$ — while the Gibbs gap of $f$ is $\approx3/N$. The
$x$-side of the seal is what kills this configuration: its density spectrum
has magnitudes $\{3/N,\,1/N\}$-scale on classes where the log-side demands
$\{e^{-3d},e^{-d}\}$, and the matching (Theorem 5's system) then forces a
negative depth. This identifies precisely why every one-sided route
(including the naive reading of the [WD] §9 sign cone) must fail, and why
the exhaustively observed $n=4$ runner-up — which has exactly this 3-dip
shape — sits at $D=0.328$ rather than $3/N$.

## 6. Quantitative Structure Of Low-Gap Sealed Laws

Fix a sealed law with $D\le c_0$. Elementary consequences, with explicit
constants:

(a) **Coefficient floor.** $u_a\le\mathbb E|X-1|\le\sqrt{2D}$ for every
$a$, hence $h_a\ge h_{\min}\ge\tfrac12\log\frac1{2c_0}$ for every $a$.

(b) **Level-set bound.** For $A=\{s:\ m_{\max}-m(s)\ge d\}$ with
$e^{-d}\le\tfrac12\bar A$ ($\bar A=\mathbb E_U e^{m-m_{\max}}$), binary data
processing gives $U(A)\le CD$ with an absolute constant ($C\le7$ suffices):
only $O(DN)$ points may dip.

(c) **Spike exclusion.** Points with $m$ above the bulk level get
exponentially boosted Gibbs mass; concentration of $P$ on $o(N)$ points
forces $D\ge\log(N/o(N))$. Hence low-gap laws have dips only. Any spike
tall enough to feed the spectral floor (a) forces $D$ of order $\log N$ —
this is the anti-delta branch, excluded by [WD] §13.

(d) **Unique deep center.** By Theorem 2(e), all dips except possibly one
have $m(s)\ge\tfrac N2h_{\min}$; the unique possible deep point $s_0$ is the
candidate delta center, and $M(s_0)$ is the candidate defect set.

(e) **Dip-transform approximation.** With $\lambda$ the bulk level of $m$
and $d_s=\lambda-m(s)$, every mask satisfies
$$
\Big|\,Nc_a+\sum_{s\in \mathrm{dip}}d_s\chi_a(s)\Big|
\le\sum_{s\in\mathrm{bulk}}|m(s)-\lambda|
\le N\sqrt{2c_0}\,(1+o(1)),
$$
so the spectrum of $m$ is the transform of the weighted dip configuration
up to an $\ell^\infty$ error $\sqrt{2c_0}$, small against
$h_{\min}\ge\tfrac12\log\frac1{2c_0}$. This is the bridge from the general
sealed law to the dip model of §5.

## 6b. Three Further Unconditional Theorems

*(Added in the full-proof campaign; proofs complete.)*

**Theorem A (universal abyss).** Every sealed law (any orientation, any
$n\ge2$, no smallness hypothesis) satisfies
$$
\min_s X(s)\;\le\;N\exp\!\big(-2\|h\|_2\big)
\;\le\;N\exp\!\big(-2h_{\min}\sqrt{N-1}\big),
$$
and more precisely $\min_sX\le e^{-\bar D}\exp\!\big(-\|h\|_2^2/(\log
N+\bar D)\big)$.

*Proof.* $w=\log N-\log X\ge0$ with $\mathbb E_Uw=\log N+\bar D=:\mu$ and
$\operatorname{Var}_Uw=\sum_ah_a^2=\|h\|_2^2$ (Parseval; the nonconstant
coefficients of $\log X$ are $\pm h_a$). Bhatia–Davis for a variable in
$[0,w_{\max}]$ — i.e. $\mathbb E[(w_{\max}-w)(w-0)]\ge0$ — gives
$\|h\|_2^2\le(w_{\max}-\mu)\mu$, so
$w_{\max}\ge\mu+\|h\|_2^2/\mu\ge2\|h\|_2$ by AM–GM, and
$\min X=Ne^{-w_{\max}}$. Since $|x_a|<1$ strictly (Theorem 1),
$h_{\min}>0$ always. $\square$

**Theorem B (defect-threshold / $\ell^1$-saturation reduction).** For every
sealed law:
$$
\sigma\ \text{is a delta orientation}
\iff
\min_s m(s)<2h_{\min}
\iff
w_{\max}>\sum_ah_a+\log N+\bar D-2h_{\min}.
$$

*Proof.* If $\sigma$ is the delta at $s_0$ then $m(s_0)=0$. Conversely if
$m(s_1)<2h_{\min}$ at the minimizer, then
$\sum_{a\in M(s_1)}h_a<h_{\min}$, and since every element of $M(s_1)$
contributes at least $h_{\min}$, $M(s_1)=\varnothing$, i.e.
$\sigma_a=-\chi_a(s_1)$ for all $a$. The $w$-form is the budget identity
$m=B-w$, $B=\sum h_a+\log N+\bar D$ (Theorem 2(c)). $\square$

So Lemma L0 is *equivalent* to: $D\le c_0$ forces the deepest point to
exhaust the $\ell^1$ spectral budget $B=\mathbb E_U[wz]$ to within
$2h_{\min}$.

**Theorem C (sign-rigidity dominance criterion).** Let $s_1$ be the
deepest point, $\varphi=w-\mathbb E_Uw$, $\varphi_1=\varphi(s_1)$, and let
$$
V_2=\sum_{s\ne s_1}\Big(\varphi(s)-\bar\varphi'\Big)^2,
\qquad
\bar\varphi'=-\frac{\varphi_1}{N-1}
$$
be the off-deep-point fluctuation (equivalently
$V_2=N\|h\|_2^2-\varphi_1^2\frac N{N-1}$). If
$$
\boxed{\;\varphi_1\cdot\frac N{N-1}\;>\;\sqrt{(N-1)V_2}\;}
\qquad\Big(\text{sufficient: }\varphi_1\ge\tfrac{N-1}{\sqrt N}\|h\|_2\Big)
$$
then $\sigma$ is the delta at $s_1$ — and hence, by Theorem 1 uniqueness,
$P$ *is* the delta sealed law.

*Proof.* $\sigma_a=\operatorname{sgn}\widehat{\log X}(a)$ and
$\widehat{\log X}(a)=-\widehat w(a)$ for $a\ne0$, so it suffices to show
$\widehat w(a)\chi_a(s_1)>0$ for every $a\ne0$. Write
$w=\mathbb Ew+\varphi$; the constant part drops, and splitting off $s_1$
with $\varphi=\bar\varphi'+\psi$ on $s\ne s_1$
($\sum_{s\ne s_1}\psi=0$, $\sum\psi^2=V_2$):
$$
N\widehat w(a)\chi_a(s_1)
=\varphi_1-\bar\varphi'+\chi_a(s_1)\!\!\sum_{s\ne s_1}\!\!\psi(s)\chi_a(s)
\;\ge\;\varphi_1\frac N{N-1}-\sqrt{(N-1)V_2}
$$
using $\sum_{s\ne s_1}\chi_a(s)=-\chi_a(s_1)$ and Cauchy–Schwarz. The
simplified sufficient form follows from
$V_2=N\|h\|_2^2-\varphi_1^2N/(N-1)$ and algebra (exact threshold
$\varphi_1^2>(N-1)^3\|h\|_2^2/(N^2-N+1)$). $\square$

*Calibration check (audit-sharpened).* At the delta,
$\varphi_1=(N-1)\alpha_\star$ exactly (from
$\log(1/A_\star)=N\alpha_\star-\log(1+u_\star)$ and
$c=-\alpha_\star+\log(1+u_\star)$), $\|h\|_2^2=(N-1)\alpha_\star^2$, and
$V_2=0$ *exactly* ($w$ is two-valued at the delta, so $\psi\equiv0$); the
criterion holds trivially strictly. The exact-threshold relative margin is
$(N^2-N+1)/(N-1)^2-1\sim1/N$, asymptotically exact. On the false side the
criterion is even sharper: 1-defect (non-delta) sealed laws approach the
dominance threshold from below with deficit $\to0$ (ratio
$0.99999974$ at $n=8$) — so C admits essentially NO relaxation in either
direction. Two further audit notes: Theorem B's threshold $2h_{\min}$ is
*attained* by every 1-defect orientation ($\min_sm=2h_{\min}$ exactly,
with $h$ minimized at the flipped mask), so B's strict inequality is
load-bearing with zero margin and the weakening to "$\le$" is false;
both facts pin B and C as exactly-calibrated instruments.

**What Theorems B and C leave open** is precisely L0: showing that
$D\le c_0$ *forces* one of the two triggers. The obstruction in both cases
is the same — configurations whose depth/fluctuation budget is spread over
several dips — and §5's matching mechanism is what must kill them. In this
sense the pair (B, C) is the endpoint-exact replacement for the melt-based
DCT: they are true, sharp, and unconditional, and they isolate the
multi-dip kill as the entire remaining difficulty.

## 6c. Rigorous Dip Reduction With Explicit Constants (Theorem D)

*(This section replaces the "idealized dip model" caveat of §5.3 for
everything except the balanced multi-dip core: the model hypotheses are now
THEOREMS with explicit, $N$-uniform constants.)*

Fix $c_0\le\frac1{200}$ and a sealed law with $D\le c_0$; set
$\varepsilon=\sqrt{2c_0}$, $h_{\min}\ge\frac12\log\frac1{2c_0}$. Define

* dips $\mathcal S=\{s:X(s)\le\tfrac12\}$, $k=|\mathcal S|$, depths
  $\beta_s=-\log X(s)\ge\log2$, masses $\mu_s=1-X(s)\in[\tfrac12,1)$;
* spikes $\mathcal S'=\{s:X(s)>2\}$, excesses $\nu_s=X(s)-1>1$,
  log-excesses $\gamma_s=\log X(s)$;
* bulk $\mathcal T'$ the rest, and the dip transform
  $F(a)=\sum_{s\in\mathcal S}\beta_s\chi_a(s)$.

**Bookkeeping bounds (each one line, from $D=\mathbb E[\psi(X)]$ with
$\psi(x)=x\log x-x+1$, and Pinsker).**
(i) $k\le D/\psi(\tfrac12)\cdot N\le6.6\,c_0N$ and
$|\mathcal S'|\le D/\psi(2)\cdot N\le2.6\,c_0N$.
(ii) $\sum\nu_s\le N\,\mathbb E(X-1)_+\le N\varepsilon/2$, hence
$\sum\gamma_s\le\sum\log(1+\nu_s)\le N\varepsilon/2$.
(iii) Bulk $\ell^1$: $\frac1N\sum_{\mathcal T'}|X-1|\le\varepsilon$ and
$\frac1N\sum_{\mathcal T'}|\log X|\le2\varepsilon$ (since $|\log x|\le
2|x-1|$ on $[\tfrac12,2]$).
(iv) Bulk $\ell^2$: $\psi(x)\ge(x-1)^2/4$ on $[\tfrac12,2]$, so
$\sum_a\tau_a^2\le\chi^2_{\rm bulk}\le4c_0$, where $\tau_a$ is the bulk
contribution to $\widehat X(a)$.

**Theorem D.** With $\varepsilon_G:=2\varepsilon+\varepsilon/2$
($=\,$bulk-log + spike-log per-mask bounds) and $c_0$ small enough that
$h_{\min}>2\varepsilon_G$ (true already at $c_0=1/200$: $h_{\min}\ge2.30$
vs $2\varepsilon_G=0.50$):

**(D0)** $k\ge1$, for every $N$: if $k=0$ then $F\equiv0$ and (D1)'s
error bound gives $h_a\le\varepsilon_G<h_{\min}$ for every $a$ —
impossible. (The earlier route via Theorem A needed $N\ge N_0(c_0)$; this
one is $N$-free — audit strengthening.)

**(D1) (full spectrum + sign readout).** For every $a\ne0$:
$$
\Big|\widehat{\log X}(a)+\tfrac1NF(a)\Big|\le\varepsilon_G,
\qquad
|F(a)|\ge N(h_{\min}-\varepsilon_G),
\qquad
\boxed{\;\sigma_a=-\operatorname{sgn}F(a).\;}
$$
*The orientation is read off the dip configuration.* (If some
$|F(a)|\le N\varepsilon_G$ then $h_a\le2\varepsilon_G<h_{\min}$,
impossible; the sign follows since the dip part dominates the error.)

**(D2) (dominant-dip kill).** If some dip dominates,
$\beta_{s_1}\ge\sum_{s\in\mathcal S\setminus\{s_1\}}\beta_s$, then
$\operatorname{sgn}F(a)=\chi_a(s_1)$ for every $a$, so by (D1)
$\sigma_a=-\chi_a(s_1)$: $\sigma$ is the delta at $s_1$, and by Theorem 1
uniqueness $P$ *is* the delta sealed law. In particular then $k=1$
(the delta law has $X=1+u_\star>\tfrac12$ off-center, and at the center
$A_\star=u_\star^N(1+u_\star)<(N-1)^{-N}\cdot\frac N{N-1}\le\tfrac12$, so
the center is a dip). Contrapositive:
**a non-delta sealed law with $D\le c_0$ has $k\ge3$ dips, none dominant.**
(For $k=2$: either $\beta_1\ne\beta_2$, which is dominance, or
$\beta_1=\beta_2$, which kills $|F|$ on the class
$\chi_a(s_1+s_2)=-1$, contradicting (D1). $k=1$ is dominance. $k=0$ is
(D0).)

**(D3) (depth scale).** $u_a=e^{-h_a}\ge e^{-\sum\beta/N-\varepsilon_G}$
for every $a$, while the dip+spike part of $\widehat X(a)$ is at most
$(k+\sum\nu)/N\le6.6c_0+\varepsilon/2$ in modulus; the bulk budget (iv)
then forces
$$
\sum_{s\in\mathcal S}\beta_s\;\ge\;\frac N2\,
\log\frac{1}{C\,c_0}
$$
with $C=9$ (audit-verified explicit constant), valid for all $N\ge4$,
$c_0\le1/200$: the total dip depth is of order $N$, always.

**Status of the remaining case (the honest frontier).** The single open
configuration class after Theorem D is: $k\ge3$ dips, no dominant depth,
$F$ full-spectrum with non-character sign pattern. We record explicitly
(from the failed refutation attempts, which is itself information): for
the balanced $3$-of-an-affine-plane configuration, ALL budget-level
accounting above is self-consistent at the parameter scales
$\beta\sim\frac N2\log\frac N{c_0}$, $\bar u_1\sim\sqrt{c_0/N}$ — the
configuration is *not* killed by $\ell^1/\ell^2$/counting/Jeffreys
budgets. Its death (numerically certain: the exhaustive $n\le4$ and
orbit-certified $n=5$ landscapes have no sealed law in
$(D_\delta,\,0.32)$) must come from the exact fixed-point coupling
between the bulk $x$-tilt $\tau$ and the bulk log-tilt $\eta$ (they are
transforms of the same bulk values, $\eta\approx\tau$ to leading order,
and the seal forces $|\eta_a|$ to track $e^{-|F(a)|/N}$ exactly). This is
Lemma L2′ below — the irreducible core of the problem on this route.

**Lemma L2′ — REFUTED as stated (same day).** The natural constant-$c_0$
form — "no sealed law with $D\le c_0$ has a balanced dip set of size
$k\ge3$" — is **false**: the balanced 3-dip plane family (§8b) is a
sealed, non-delta, balanced-$k{=}3$ law with $D=(4\log4+o(1))/N\le c_0$
for all large $N$. The same example refutes any constant-$c_0$ form of
L0. The correct open statement is the *ratio* version:

**Lemma L0-ratio (the true open core).** There exist $\kappa^\ast>1$ and
$n_0$ such that for all $n\ge n_0$, every non-delta orientation has
$N\!\cdot\!D\ge\kappa^\ast$. (Conjectured sharp constant: $4\log4$;
the limit problem of §8b yields $\kappa^\ast=3$ modulo the compactness
step.)

Theorem D remains true as stated (it is conditional on $D\le c_0$ and
never claimed balanced $k\ge3$ impossible); its role is now to reduce
L0-ratio to the classification of balanced multi-dip configurations,
which at the $1/N$ scale is exactly §8b's limit problem.

## 6d. Theorem E (Deep-Dip Trichotomy) And Theorem F (The Full Theorem)

*(Final campaign step. The insight unlocking it: the limit problem's
compactness step is NOT needed — only the count of nearly-dead dips
matters, and (D1)+(D2) control that count directly, at a moderate
threshold. All constants below are explicit and $N$-uniform; every step
was verified numerically in log-domain on the in-regime families at
$n=9,10,11$ before write-up.)*

**Standing constants.** Work with any sealed law with $D\le c_0:=1/60$.
Then, writing $\varepsilon_G(D)=2.5\sqrt{2D}$ and
$h'(D)=\tfrac12\log\tfrac1{2D}-\varepsilon_G(D)$ (both monotone
favorably in $D$, so it suffices to evaluate at $D=1/60$):
$$
h_{\min}\ge\tfrac12\log30>1.70059,\quad
\varepsilon_G\le0.45644,\quad
h'>1.24416,
$$
and Theorem D's hypothesis $h_{\min}>2\varepsilon_G$ holds
($1.70059>0.91288$), so (D1) and (D2) apply verbatim at $c_0=1/60$
(their proofs are parameterized only by that hypothesis; the "$1/200$"
in §6c was a sufficient instance, not a requirement — audit-verified,
with the hypothesis in fact persisting to $D\approx0.035$). Dip count:
$k\le DN/\psi(\tfrac12)\le N/(60\cdot0.1534264)<0.108630\,N$.
*(All decimals in this section are safe-rounded: lower bounds down,
upper bounds up — repaired after the audit caught four unsafe
roundings at the sixth decimal.)*

**Theorem E (deep-dip trichotomy).** Let $P$ be a sealed law for a
NON-delta orientation $\sigma$ with $D\le1/60$, any $n\ge2$. Then
$$
\boxed{\;N\cdot D\;\ge\;3\,\psi(e^{-5})\;=\;2.87871\ldots\;}
$$

*Proof.* Let $\mathcal S=\{X\le\frac12\}$ with depths
$\beta_s=-\log X(s)$, and split $\mathcal S$ at $\Theta=5$: deep
($\beta\ge5$, count $m$) and shallow ($\beta<5$). Shallow mass:
$$
\Sigma_{\rm sh}:=\sum_{\text{shallow}}\beta_s\;<\;\Theta k\;\le\;
\frac{5N}{60\,\psi(\tfrac12)}\;<\;0.543149\,N.
$$
By (D1), $|F(a)|\ge Nh'>1.24416\,N$ for every mask $a\ne0$, where
$F(a)=\sum_{s\in\mathcal S}\beta_s\chi_a(s)$. Trichotomy on $m$:

* **$m=0$:** for any $a\ne0$,
  $|F(a)|\le\sum\beta=\Sigma_{\rm sh}<0.543149\,N<1.24416\,N$ —
  contradicts (D1). (This includes $k=0$, where $F\equiv0$.)
* **$m=1$** (deep dip $s_1$): $|F(a)|\le\beta_1+\Sigma_{\rm sh}$ gives
  $\beta_1\ge Nh'-\Sigma_{\rm sh}>0.701014\,N>0.543149\,N>
  \sum_{s\ne s_1}\beta_s$: the dip $s_1$ dominates, so (D2) forces
  $\sigma$ to be the delta at $s_1$ — contradicting non-delta.
* **$m=2$** (deep $s_1,s_2$, wlog $\beta_1\ge\beta_2$): choose
  $a\ne0$ with $\chi_a(s_1+s_2)=-1$ (the set of such $a$ has size $N/2$
  and excludes $0$). There
  $|F(a)|\le|\beta_1-\beta_2|+\Sigma_{\rm sh}$, so
  $\beta_1-\beta_2\ge Nh'-\Sigma_{\rm sh}>0.701014\,N$. Dominance:
  $\beta_1-\big(\beta_2+\Sigma_{\rm sh}\big)\ge
  Nh'-2\Sigma_{\rm sh}>0.157865\,N>0$ — again (D2) forces delta,
  contradiction.
* **$m\ge3$:** since $\mathbb E_U[X-1]=0$,
  $D=\mathbb E_U[\psi(X)]$ with $\psi(x)=x\log x-x+1\ge0$, and $\psi$ is
  decreasing on $[0,1]$, so
  $D\ge\frac1N\sum_{\text{deep}}\psi(X_s)\ge\frac3N\psi(e^{-5})
  =\frac{3(1-6e^{-5})}N=\frac{2.87871\ldots}N$. $\square$

**Theorem F (Global Delta Optimality, all $n$).** For every $n\ge2$ and
every orientation $\epsilon$,
$$
\boxed{\;\widehat m(\epsilon)\ge\widehat m(\epsilon_\star),\;}
$$
with equality exactly on the spin-flip (translate) orbit of the delta
orientation.

*Proof.* For $n\le5$: the certified computations of §8/§8a (exhaustive
$n\le4$; complete 176-orbit transversal at $n=5$; worst certified margin
$0.1389$). For $n\ge6$ and $\sigma$ non-delta, two branches:

1. **$D(\sigma)>1/60$:** by the elementary delta bound (§7 recovery
   fact iii), $D_\delta<\frac1{N-1}\le\frac1{63}<\frac1{60}<D(\sigma)$.
2. **$D(\sigma)\le1/60$:** Theorem E gives
   $D(\sigma)\ge\frac{2.87871}N>\frac1{N-1}>D_\delta$
   (the middle inequality is $2.87871(N-1)>N$, true for all
   $N\ge2$).

Both branches are strict, so non-delta orientations lie strictly above
$D_\delta$; all $N$ delta orientations share the value $D_\delta$ by
translation covariance (§7 recovery fact ii). $\square$

**Trust base of Theorem F** (final form, per the second audit). (a)
Theorems 1, D(D1–D2) and the recovery facts — proved above; adversarially
audited twice (seven independent verifiers in total, zero falsifications;
the load-bearing hypothesis $h_{\min}>2\varepsilon_G$ re-proved end-to-end
at $c_0=1/60$; a ~55,000-solve counterexample campaign at $n=4..13$ found
zero violations and an $m$-census over 4,570+ non-delta laws found no
deep-count below 3). (b) Pinsker's inequality and the one-line
bookkeeping bounds of §6c. (c) The elementary delta bound
$D_\delta<1/(N-1)$ (independently certified at dps 100 for $n=6..14$).
(d) For $n\le5$ the proof is computer-assisted: exhaustive
per-orientation Newton–Kantorovich certificates ($n=2,3,4$: all
$2^{N-1}$ orientations, worst certified margins $0.193236/0.462239/
0.263509$) and a complete 176-orbit transversal of
$\langle\text{translations},GL(5,2)\rangle$ with certified dps-40 solves
($n=5$: worst certified margin $0.138873$, $D$-errors $\le10^{-33}$),
delta reference by dps-60 sign-bracketing; validity is modulo faithful
round-to-nearest mpmath arithmetic (directed-rounding interval
arithmetic is the remaining formality; margins exceed certified errors
by 8–30 orders), completeness of the orbit partition (BFS checksum
$=2^{31}$ plus independent Burnside count), and recovery fact (ii′).
Nothing else. In particular: no limit problem, no compactness step, no
melt, no cut families.

**Why the sharp constant is not needed.** Theorem E's constant
$3\psi(e^{-5})=2.879$ is far below the true asymptotic runner-up
$4\log4=5.545$ (§8b) — but the theorem only requires beating
$N\!\cdot\!D_\delta<N/(N-1)\le64/63\approx1.016$, and $2.879$ clears
that with a $2.8\times$ margin. The photo-finish that defeated
slack-based methods was an artifact of aiming at the sharp constant;
the win threshold is $1$, not $4\log4$.

## 7. Remaining Lemma And Conditional Theorem

*(Revised after the 2026-07-02 adversarial audit; see the solve log. The
original formulation split the open content into two lemmas L1/L2 keyed to
"the dip set" of a sealed law — but §6 admits several inequivalent dip-set
definitions, so that pair was a statement-schema, not a pair of theorems.
The definition-independent statement below is what the conditional theorem
actually consumes; L1/L2 survive as the intended two-case proof strategy,
relative to one fixed definition.)*

**Lemma L0 (the open lemma).** There are constants $c_0>0$ and $n_0$ such
that for every $n\ge n_0$, every sealed law with $D\le c_0$ is a delta
sealed law.

*Intended proof decomposition.* Fix once and for all the dip set
$\mathcal S=\{s:\ m_{\max}-m(s)\ge h_{\min}\}$. Case L1 ($\mathcal S$ does
not affinely span $\mathbb F_2^n$): the $\varepsilon$-version of Theorem 5
with the §6 error terms; natural endgame is integer rigidity ($z$ is
even-integer valued with $\sum z=N$, $\sum z^2=N^2$ exactly, so
"approximately delta" collapses to "exactly delta" once errors are below
the integer gap). Case L2 ($\mathcal S$ affinely spans, so
$k\ge n+1$, no common-sign mask): the matching system
$|G(a)|=Ne^{-|F(a)|/N}/X_b$ over the full mask space with $k$-dimensional
$F,G$ is overdetermined by a factor $\sim N/k$; expected statement is that
it has no positive solutions for $k\ge2$. Both cases must be proved for the
*same* $\mathcal S$, $c_0$, $n_0$.

*Update (full-proof campaign):* Theorem D (§6c) now proves the dip-model
reduction rigorously with explicit constants (using the $X$-based dip set
$\{X\le\frac12\}$) and kills every configuration except balanced $k\ge3$.
Hence **L0 $\iff$ L2′** (§6c), and the L1/L2 split above is superseded.

**Recovery facts (proved; used silently before, now explicit).** (i) A
sealed law determines its orientation: $|x_a|=e^{-h_a}>0$ for every $a$, so
$\sigma_a=\operatorname{sgn}(x_a)$; hence "is a delta sealed law" means
exactly "$\sigma$ is in the delta orbit". (ii) $G_\sigma$ is covariant
under $\ell_a\mapsto\ell_a\chi_a(t)$, so $D$ is constant on the size-$N$
translate (= spin-flip) orbit of the delta. (ii′) *(added after the
Theorem-F audit — load-bearing for the $n=5$ orbit reduction)* $D$ is
likewise invariant under $GL(n,2)$: for invertible $M$, $s\mapsto Ms$ is a
$U$-preserving bijection with $\chi_a(Ms)=\chi_{M^{\mathsf T}a}(s)$, so
$\ell\mapsto\ell'$ with $\ell'_{M^{\mathsf T}a}=\ell_a$ carries $G_\sigma$
to $G_{\sigma'}$ ($\sigma'_{M^{\mathsf T}a}=\sigma_a$) with equal values;
by Theorem 1 uniqueness the sealed laws correspond under the bijection and
have equal $D$. Hence $D$ is constant on
$\langle\text{translations},GL(n,2)\rangle$-orbits — exactly the group of
the §8 orbit enumeration. (Audit-verified numerically: agreement
$\le1.8\times10^{-15}$ on random $(t,M)$-images at $n=5$.) (iii) Elementary self-contained
delta bound: $A\log A\le0$ and $(1+u)\log(1+u)\le u(1+u)$ give
$D_\delta\le\frac{N-1}N u_\star(1+u_\star)<\frac1{N-1}$, using
$u_\star<\frac1{N-1}$ (the seal polynomial is negative at $0$ and positive
at $\frac1{N-1}$). So the chain below does not need [WD] §13's sharper
$D_\delta<\log\frac N{N-1}$.

**Theorem 6 (conditional, corrected form).** Assume L0 with constants
$(c_0,n_0)$ and let $n_c=\min\{n:\ c_0>D_\delta(2^n)\}
\le\lceil\log_2(1+1/c_0)\rceil$, $n^\ast=\max(n_0,n_c)$. Then the Global
Delta Optimality Theorem, with equality exactly on the spin-flip orbit,
holds for all $n\ge n^\ast$: a non-delta orientation has $D>c_0>D_\delta$
by L0 + recovery fact (i), and the delta orbit is a single equality class
by (ii). Together with the (certified) finite verification for $n\le4$,
the *full* problem is solved iff the window $5\le n<n^\ast$ is empty or
closed by finite verification.

**Effectivity requirement (essential; updated after §8b).** The
constant-$c_0$ framing of this requirement is obsolete — no constant
$c_0$ works at all (§8b) — but its logic survives at the ratio scale.
L0-ratio with bare existential $(\kappa^\ast,n_0)$ leaves the window
$6\le n<n_0$ (now that $n\le5$ is certified), closable by computation
only at $n=6$ (heroic: $\ge7.1\times10^6$ orbits over a $2^{63}$-point
space) and categorically impossible for $n\ge7$
($\ge8.1\times10^{21}$ orbits). Since
$N\!\cdot\!D_\delta<N/(N-1)\le64/63$ for $n\ge6$, the clean target is
$$
\boxed{\;\kappa^\ast\ge\tfrac{65}{64}\;(>\!\tfrac N{N-1}\ \forall n\ge6),
\qquad n_0\le6,\;}
$$
and the limit-problem route promises $\kappa^\ast=3$ with sharp value
$4\log4$ — ample margin, PROVIDED the compactness step is made
quantitative enough to pin $n_0\le6$ (or $\le7$ plus an $n{=}6$ orbit
computation). A non-effective compactness proof would leave an
uncloseable window at $n\ge7$.

Compared with [WD] §9.9's conditional endpoint, the RAC cut-family and the
smoothed vanishing exclusion are replaced by L0, a *finite, endpoint-only*
statement about sealed laws — no relaxed paths, no cut families, no line
cells.

## 8. Numerical Receipts

All code in `walsh-delta-code/` (`seal_scan.py`, `analyze_defects.py`,
`probe_n56.py`, `verify_identities.py`, `mp_verify.py`). Solver: damped
Newton on the strictly convex $G_\sigma$ (Theorem 1), residuals
$<10^{-13}$ (float64) resp. $<10^{-40}$ (mpmath dps 50).

**Exhaustive scans (all $2^{N-1}$ orientations).**

| $n$ | $D_\delta$ | min non-δ $D$ | attained at $|M|$ | landscape gap | χ² floor ratio |
|---|---|---|---|---|---|
| 2 | 0.266653365 | 0.459889495 | 1 | (0.267, 0.460) empty | 3.45 |
| 3 | 0.133530982 | 0.595770438 | 2 | (0.134, 0.596) empty | 7.87 |
| 4 | 0.064538521 | 0.328047800 | 4 | (0.065, 0.328) empty | 9.00 |

Delta orbit (size $N$) is the exact and unique minimizer in every case —
this independently replicates and extends [WD] §7.9. The runner-up defect
class is $|M|=2^{n-2}$ (not $|M|=1$, whose minima grow: 0.460, 0.677,
0.725); the $n=4$ runner-up is the 3-of-an-affine-plane dip configuration
of §5.4.

**SPS ([WD] §47.6) exhaustive check, $n\le4$:** zero violations of SPS-1
and zero of SPS-2 over all orientations. Thinnest margin found anywhere:
SPS-2 at $n=3$, margin $0.0024408010$ (mpmath: $R_2$(idx 7)
$=0.08420625495$, $R_2(\delta)=0.08176545391$). SPS-1 margins are wide
(ratio $\ge1.7$). This is the first exhaustive evidence for the Sealed
Projection-Stability Lemma.

**Certified $n=5$ (full-proof campaign).** Complete orbit enumeration of
all $2^{31}$ orientations under $\langle$translations,
$GL(5,2)\rangle$ by BFS in C with completeness checksum: exactly **176
orbits**, sizes summing to $2^{31}$ (cross-checks: 2, 4, 14 orbits at
$n=2,3,4$, matching independent Burnside counts). Certified Kantorovich
solves (mpmath dps 40) of all 176 representatives: **zero failures**;
delta orbit (size 32) uniquely minimal at $D=0.0317486983$; worst
certified non-delta margin $0.1388727$; certified $D$-errors
$\le10^{-33}$. Lowest orbits: delta $0.03175$; balanced 3-dip family
(rep 2040, size 4960) $0.17062$; $0.23471$; the $j{=}3$ family $0.24362$.
**The Global Delta Optimality Theorem is thereby established for all
$n\le5$** (modulo faithful mpmath arithmetic; see §8a).

**Warning on local-search probes.** The earlier $n=5,6$ probe values
($0.406$, $0.336$) were local-search artifacts, NOT landscape minima —
the certified $n=5$ minimum over non-delta orbits is $0.17062$. See §8b:
the true landscape scale is $\Theta(1/N)$.

## 8a. Certified $n\le4$ (Kantorovich pass)

Per-orientation a-posteriori certificates over ALL orientations
($n=2,3,4$): evaluate at the exact float64 Newton output $\tilde\ell$ in
mpmath (dps 30): residual $\rho=\|\nabla G_\sigma(\tilde\ell)\|_2$,
Hessian floor $\lambda=\min_ae^{-\sigma_a\tilde\ell_a}$ (valid since
$\operatorname{Hess}G\succeq\operatorname{diag}(e^{-\sigma\ell})$); if
$r_0=2e\rho/\lambda\le1$ then $\|\ell^\ast-\tilde\ell\|\le r_0$ (convex
monotonicity along the segment, barrier entries lose at most $e^{-1}$
within radius 1); transfer to $D$ by
$\nabla D(\ell)=H_F(\ell)\ell$, $\|H_F\|\le N-1$. Delta reference by
certified sign-bracketing of $u^{N+1}+u^N+(N-1)u-1$ at dps 60. Results:
zero failures; worst certified margins $0.19324$ ($n{=}2$), $0.46224$
($n{=}3$), $0.26351$ ($n{=}4$); max radius $2.3\times10^{-11}$, max
$D$-error $1.6\times10^{-9}$ against margins $\ge0.19$.

*Audit trust-base notes (all conclusions stand).* (i) The Kantorovich
bound and the Lipschitz transfer were independently reproved and
stress-tested (384 adversarial certificates, min slack ratio 5.4).
(ii) The delta reference uses round-to-nearest dps-60 (not directed
rounding): the returned upper value can sit below the true $D_\delta$ by
$\sim5\times10^{-62}$, so strictly the certificates prove
$D>D_\delta-10^{-60}$ — absorbed by 60 orders of margin; directed
rounding is the final polish. (iii) A theoretical NaN silent-pass channel
in the comparison logic was closed empirically: an exhaustive finiteness
sweep over all $n\le4$ solver outputs found zero nonfinite values;
hardening (`not (r0 <= 1/2)`) recommended. (iv) The $n=5$ orbit count 176
is doubly certified: BFS completeness checksum ($\sum$ sizes
$=2^{31}$ exactly, loud-abort stack design) *and* an independent exact
Burnside computation over all $9{,}999{,}360$ elements of $GL(5,2)$; the
Burnside match also proves the BFS generators generate the full
invariance group (a proper subgroup would give a finer partition —
which would still be sound for certification, only redundant).

## 8b. The True Landscape Is $\Theta(1/N)$: Exact Asymptotic Families

Solving the seal for the balanced 3-dip orientation family
($\sigma_a=+1$ iff $a\supseteq\{$bits $0,1\}$; this IS the runner-up
orbit at $n=3,4,5$) for $n=3..8$ gives $N\!\cdot\!D=$ 4.766, 5.249,
5.460, 5.523, 5.540, 5.544 — so
$$
\boxed{\;\min_{\text{non-}\delta}D\;\le\;\frac{4\log4+o(1)}N\;:}
$$
**there is no constant landscape floor; the delta wins by a constant
factor, not a constant gap.** The limit is exactly solvable: three dead
points on an affine plane (depths $\beta\approx N\log(N/4)$), one spike
at the fourth plane point with $X\to4$ exactly (forced: it annihilates
the $(+,+)$-class $x$-coefficients and balances the plane's mass), bulk
$\to1$, $u$-levels $\{4/N,\,64/N^3\}$; limit cost $N\!\cdot\!D\to
3\cdot\psi(0)+\psi(4)=3+4\log4-3=4\log4=5.545177$. The $j$-flat
generalization ($\sigma_a=+1$ iff $a\supseteq$ bits $0..j{-}1$) has
$N\!\cdot\!D\to2^j\log\frac{2^j}{2^{j-1}-1}$ (measured: $7.8458$ at
$n=8$, converging to $8\log\frac83=7.84663$), increasing in $j$; the
delta is the degenerate $j$ case with $\kappa=1$.

**The limit problem.** At scale $N\!\cdot\!D=O(1)$ the seal converges
(compactness to be made rigorous) to a finite object: dead points $K_0$
(depths $N(\log N-\log c_s)$, $c_s>0$), finite-value points
$(s_i,\xi_i)$, bulk $\to1$; with $m_a=\sum_{K_0}\chi_a(s)\in\mathbb Z$
and $\Phi(a)=\sum_i(\xi_i-1)\chi_a(s_i)-\sum_{K_0}\chi_a(s)$ the limit
seal reads: (i) $|m_a|\ge1$ for all $a\ne0$; (ii) $\Phi(0)=0$ and
$\Phi\equiv0$ on $\{|m_a|\ge2\}$; (iii) on $\{|m_a|=1\}$:
$\operatorname{sgn}\Phi(a)=-\operatorname{sgn}(m_a)$ and
$\log|\Phi(a)|$ equals a signed linear form in $\{\log c_s\}$; and the
cost is $N\!\cdot\!D\to\kappa=|K_0|+\sum_i\psi(\xi_i)$,
$\psi(x)=x\log x-x+1$. Solved within the limit problem: $|K_0|=1$ forces
the pure delta ($\kappa=1$); $|K_0|=2$ and $|K_0|=4$ are impossible
($m_a=0$ classes / Parseval counting $(2^r-1)\cdot4+k^2\le2^rk$ fails);
$|K_0|=3$ always spans a plane and is forced to the unique
$\xi=4$-completion, $\kappa=4\log4$; even $|K_0|=6$ needs dimension
$\ge4$ and $\kappa\ge6$. Since $\psi\ge0$, every admissible non-delta
configuration has $\kappa\ge|K_0|\ge3$. Hence, **modulo the compactness
step**, the asymptotic theorem holds with ratio constant
$\kappa^\ast=3$:
$$
\liminf_{n}\;\min_{\text{non-}\delta}\;N\!\cdot\!D\;\ge\;3\;>\;1
=\lim_n N\!\cdot\!D_\delta,
$$
with conjectured sharp value $4\log4$.

**mpmath receipts (dps 50).**
$D_\delta(n{=}3)=0.13353098207247197385$,
runner-up $=0.59577043845760836634$ (gap $0.46223945638513639249$);
$D_\delta(n{=}4)=0.06453852113757117122$,
runner-up $=0.32804779982701766312$ (gap $0.26350927868944649190$).
Identity package verified to $1.9\times10^{-12}$ (float64) on 17
orientations across $n=3,4,5$; deep-pair inequality: zero violations on all
$N^2$ pairs tested per orientation.

## 9. Relation To The [WD] Program

* Theorem 2(e) is the endpoint, path-free avatar of the boundary sign cone
  ([WD] §9.7): it excludes *all* multi-deep-center structures at once,
  without tropical limits.
* Theorem 5 is the endpoint statement that the DCT (killed in [WD] §46)
  tried to reach by monotone flow: here it is an algebraic consequence of
  two-family positivity plus the exponential link, with no flow.
* §5.4's counterexample explains structurally why RAC could not collapse to
  a single Bregman square ([WD] §45): the one-sided objects (log-side only)
  genuinely admit cheap non-delta configurations; only the two-sided
  matching kills them. Any successful RAC-type argument must consume both
  sides of the seal.
* The SPS route ([WD] §47) receives its first exhaustive verification
  ($n\le4$) but also a caution: the thinnest SPS-2 margin ($0.0024$ at
  $n=3$) is two orders below the main theorem's margin, so SPS-2 is a
  genuinely sharper statement than delta optimality itself.

## 10. Status

*(Corrected after the 2026-07-02 adversarial audit — four independent
hostile auditors; every numerical receipt was replicated on independent
code paths, Theorem 5's proof was verified step-by-step including machine
re-verification of its Parseval identity, and no circularity was found.)*

* **Proved here:** Theorems 1, 2, 3, 5; Theorem 4's first two claims
  ($z$ two-valued; $S$ a difference set) — its Hadamard-parameter
  classification is cited from the classical theory and its
  $\log2-o(1)$ floor for bent configurations is a sketch (neither is
  load-bearing for Theorem 6); §6(a),(b),(d) with constants; the §5.4
  no-go; the §7 recovery facts.
* **Hedged (proof obligations inside L0, not inputs to Theorem 6):**
  §6(c) spike exclusion (qualitative as stated) and §6(e)'s error constant
  (its naive one-sided accounting is false — solve log — and must be
  anchored at the Gibbs top).
* **Verified numerically, certification mechanical but not yet performed:**
  the $n\le4$ exhaustive verification (float64 residuals $<10^{-13}$,
  mpmath dps-50 for extremes and the thinnest margin, margins
  $0.19$–$0.46$; independently replicated during audit). A proof-grade
  certificate would run a Newton–Kantorovich pass over all orientations —
  Theorem 1 supplies the needed Hessian floor
  $\lambda_{\min}\ge\min_au_a$ for free, leaving $\sim8$ orders of error
  slack — and, for the delta reference values, the scalar closed form.
* **Proved in the full-proof campaign (2026-07-02, second pass):**
  Theorems A, B, C (§6b) and Theorem D (§6c) — the rigorous dip reduction:
  full-spectrum + sign-readout (D1), dominant-dip kill (D2, subsuming
  $k\le2$), depth scale (D3); certified verification of all orientations
  for $n\le4$ (§8a: Kantorovich certificates, zero failures, worst margins
  0.193 / 0.462 / 0.264); complete orbit partitions with checksum
  certificates (2, 4, 14, **176** orbits at $n=2..5$) and certified
  solves of all 176 representatives — **the theorem is established for
  all $n\le5$** (worst certified margin 0.13887), modulo faithful mpmath
  arithmetic.
* **Discovered and corrected (same day):** the constant-floor picture is
  FALSE — the balanced 3-dip family has $N\!\cdot\!D\to4\log4$ (§8b), so
  the constant-$c_0$ lemmas (L0, L2′) are refuted as stated; the earlier
  $n=5,6$ probe "floors" ($0.41,0.34$) were local-search artifacts. The
  problem is a sharp constant-factor race at scale $1/N$.
* **THE THEOREM IS PROVED (§6d, third pass, 2026-07-02):** Theorem E
  (deep-dip trichotomy: non-delta with $D\le1/60$ forces $\ge3$ dips of
  depth $\ge5$, hence $N\!\cdot\!D\ge3\psi(e^{-5})=2.87871$) and
  Theorem F (assembly: $n\le5$ certified; $n\ge6$ by the two-branch
  argument at threshold $1/60$). Audited by four maximally-hostile
  independent verifiers: verdicts proof-correct / correct-with-repairs,
  zero fatal findings, zero gaps; all repairs (safe rounding of four
  constants, recovery fact (ii′) $GL$-invariance, trust-base sentence,
  receipt script, NaN hardening) applied. A ~55,000-solve adversarial
  campaign at $n=4..13$ found zero violations; no sealed non-delta law
  with fewer than 3 deep dips exists anywhere in the data.
* **Key structural insight:** the win threshold is
  $N\!\cdot\!D_\delta<64/63\approx1.016$, not the sharp runner-up
  constant $4\log4=5.545$ — the "photo-finish" that defeated all prior
  slack-based routes was an artifact of aiming at the sharp constant.
  The §8b limit problem is no longer needed for the theorem; it remains
  the route to the *sharp* asymptotic constant (conjectured $4\log4$),
  now a refinement rather than a gap.
* **Remaining formality (does not affect the theorem's status as
  computer-assisted-proved):** directed-rounding interval arithmetic
  for the $n\le5$ certificates (§8/§8a; margins exceed certified errors
  by 8–30 orders; faithful mpmath + independent replication on separate
  code paths is the current trust base).
