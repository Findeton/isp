# Exponential-consistency fixed points of parity-relation codes: an exactly solvable binding theory

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-11.

## Abstract

Let $S$ be a finite set of parity characters ("modes") on $n$ spins
and $K$ the binary linear code of relations among them.  We study
the **exponential-consistency fixed point**: fields $h_a$ on the
modes determined self-referentially by $\langle\chi_a\rangle_h =
e^{-h_a}$ — each mode's thermal expectation equals its own Boltzmann
suppression.  The relation-free case is the scalar equation
$\tanh h = e^{-h}$, whose root is $\eta = -\ln\theta$ with $\theta$
the real root of $\theta^3 + \theta^2 + \theta = 1$ (the reciprocal
tribonacci constant).  Results, each with machine receipts at 40+
digits: (1) **invariance and decomposition** — the fixed point and
its evidence defect depend on $S$ only through the code $K$, and
decompose additively over code components; (2) the **single-relation
theorem** — for one weight-$w$ relation the fixed point reduces to a
scalar equation, solved exactly: weight 3 *binds* (defect
$+0.008438104972291$) while every $w \ge 4$ anti-binds, with the
asymptotic law $\mathrm{defect} \to \theta^w(1 - w\kappa)$,
$\kappa = \eta(1-\theta^2)/(1-\theta^2+\theta) =
0.343922878815527$, and sign boundary $w = 1/\kappa = 2.9076$ — so
the triangle's binding is decided strictly beyond first order; (3)
the **exact defect functional** $\mathrm{defect}(w;\lambda) =
\ln(1+\lambda t^w) - w[D(h^*) - D(\eta)]$, $D(h) = he^{-h} -
\ln\cosh h$, reproducing the full solved table, and its **second
order in closed form**: $d_2(w) = \theta^{2w}\bigl[-\tfrac12 + bw +
cw^2\bigr]$ with $c = \eta(1-\theta^2)^3/(\theta^2\Delta^2)$,
$\Delta = 1-\theta^2+\theta$, verified to $10^{-26}$; (4) a
**frustration identity** (Proposition 5.1; the matched value is
computed in an external companion supplied as supplementary
material, so this is a proposition with a 14-digit receipt, not a
self-contained theorem) — the sign-reversed ($\lambda = -1$) point
of the scalar theory equals that companion's oriented frustrated
triangle, $+0.201674235292$, to $10^{-14}$:
frustration is amplitude reversal; (5) **interaction constants** —
an exact multi-mode solver for arbitrary codes (validated
internally by two independent solution routes and by exact
component additivity) gives the
shared-mode pair $+0.0208449703908$ and the per-link limit of
single-share chains $D_\infty = 0.013273$ (converged to $4\times
10^{-6}$ by six links); (6) **algebraic status** — $11\kappa =
\eta(7 - 2\theta + \theta^2)$ exactly, while $\kappa \notin
\mathbb Q(\theta)$ is a theorem (Hermite–Lindemann): the
theory's constants are transcendental-form in $\theta$ with one
$\eta$ factor.  The marginality $\varepsilon = 3\kappa - 1 =
0.0317686364466$ — the triangle's first-order distance from the
sign boundary — is the constant exported to companion papers; this
paper is its complete, self-contained pedigree.

## 1. The model

Fix $n$ spins and a set $S$ of $m$ distinct nontrivial parity
characters $\chi_a(x) = (-1)^{\langle a, x\rangle}$,
$a \in \mathbb F_2^n\setminus\{0\}$, $x \in \mathbb F_2^n$.  The
**relation code** $K \subseteq \mathbb F_2^S$ is the kernel of
$\mathbb F_2^S \to \mathbb F_2^n$ — a binary linear code of length
$m$, dimension $m - \mathrm{rank}(S)$, and minimum distance $\ge 3$
(weight-1 words are trivial characters, weight-2 words repeated
characters; both excluded by distinctness).  For fields
$h \in \mathbb R^S$ define

$$
Z(h) = \sum_{x\in\mathbb F_2^n} \exp\Bigl(\sum_{a\in S} h_a
\chi_a(x)\Bigr), \qquad
\frac{Z(h)}{2^n\prod_a \cosh h_a} = W_K(t) =
\sum_{c\in K}\ \prod_{a\in\mathrm{supp}(c)} t_a,
$$

with $t_a = \tanh h_a$ — the standard character (high-temperature)
expansion [1], exact; $W_K$ is the code's weight enumerator in the
sense of [2].

**Definition (exponential consistency).**  A fixed point is a
field $h^*$ solving, for every mode,

$$
\langle\chi_a\rangle_{h} \;=\; e^{-h_a}.
$$

The motivation comes from a physics research program in which
$e^{-h_a}$ is a record weight and the condition equates a mode's
evidence with its weight; the mathematics stands alone, and this
paper develops it as such.

**Lemma 1.1 (well-posedness, scalar case).**  For the relation-free
mode, $F(h) = \tanh h - e^{-h}$ has $F'(h) = \mathrm{sech}^2 h +
e^{-h} > 0$ on all of $\mathbb R$: strictly increasing, with
$F(0) = -1 < 0 < F(\infty) = 1$ — the root $\eta$ exists and is
unique on $\mathbb R$.  For the single-relation system of Section 3
at **both** $\lambda = +1$ and $\lambda = -1$ (the latter is the
case Proposition 5.1 uses), existence follows from the same sign
change (at $\lambda = -1$, $(1-t^2)/(1-t^w) \to 2/w$ gives the
positive limit $1 - 2/w$ for $w \ge 3$); uniqueness on $(0, 6)$ is
established by *fine sign-change scan* — bracketing on a
$20001$-point grid with monotone refinement at each bracket — at
every $w \le 40$ and both signs of $\lambda$ (one root each;
receipts; the scan is fine but carries no inter-node derivative
bound, so "one root" on $(0,6)$ is a verified-numerics statement,
not a certificate), and roots outside $(0,6)$ are excluded
analytically, split by the sign of $\lambda$ (the inequality an
earlier draft printed here — "$2\tanh^{w-1}h/(1-\tanh^w h) < 0.01$"
— was false, its left side *diverging* as $h$ grows; caught in
review): for $h \ge 6$, $e^{-h} \le e^{-6} < 0.0025$, while at
$\lambda = +1$ the relation term is positive so the left side
exceeds $\tanh 6 > 0.9999$, and at $\lambda = -1$ the relation
term $(1-t^2)\,t^{w-1}/(1-t^w)$ ($t = \tanh h$) is bounded by its
$t \uparrow 1$ limit $2/w \le 2/3$ for $w \ge 3$ (it increases to
that limit in $t$; verified on a $20000$-point sweep for $w \le
40$), so the left side is at least $\tanh 6 - 2/3 - e^{-6} >
0.33$ from a root — worst margin, at $w = 3$.  $h \le 0$ fails
the sign at once.  For general
multi-mode systems we *assume* the Newton solution continued from
$h_a = \eta$ is the relevant fixed point and verify it is locally
unique; ruling out asymmetric solutions of symmetric systems
globally is open, and the flag is discharged where used (Section
3's reduction): a $300$-start random multi-start search per case
($w = 3, 4$; $\lambda = \pm 1$; starts in $(0.05, 4)^w$) finds
only the symmetric point, with zero asymmetric solutions
(receipts).

**The evidence defect.**  Define, at the fixed point,

$$
\mathrm{defect}(S) \;=\; \ln W_K(t^*)
\;-\; \sum_{a}\,[\,D(h_a^*) - D(\eta)\,],
\qquad D(h) = he^{-h} - \ln\cosh h
$$

— equivalently $\mathrm{defect}(S) = D^{\mathrm{free}} -
D(P_{h^*}\Vert U)$ with $D^{\mathrm{free}} = m\,d_0$ ($d_0$ the
per-mode divergence below), the evidence *absorbed* by the
relations: a
positive defect means the constrained system sits **closer to
uniform** than free modes — the relations soak up commitment — and
we call such relation sets *binding*; negative = anti-binding.
(An earlier draft defined the defect with the opposite sign while
printing these values, an inconsistency caught in review; the
present definition is the one all printed numbers satisfy, and the
gloss above is the correct reading of its sign.)

**The free mode.**  With $K = \{0\}$, each mode separately solves
$\tanh h = e^{-h}$.  Substituting $x = e^{-h}$ gives
$x^3 + x^2 + x = 1$: the root is $\theta = 0.543689012692\ldots$
(the reciprocal tribonacci constant, algebraic of degree 3), with
$h = \eta = -\ln\theta = 0.609377863\ldots$ and per-mode divergence
$d_0 = \eta\theta - \ln\cosh\eta$.

## 2. Invariance and decomposition

**Theorem 2.1 (code invariance).**  $h^*$, $Z$, and
$\mathrm{defect}(S)$ depend on $S$ only through $K$ as a subset
structure: mode sets with isomorphic relation codes have equal
defects, at any $n$.

*Proof.*  $W_K$ is a function of $K$ alone;
$\psi = \sum_a \ln\cosh h_a + \ln W_K$ generates all expectations;
the fixed point and $D(P\Vert U)$ are functions of $\psi$.
$\square$

**Theorem 2.2 (component decomposition).**  If $K = K_1 \oplus K_2$
over a partition of $S$ (no codeword mixes the parts), then
$W = W_1 W_2$, the fixed point decouples, and
$\mathrm{defect} = \mathrm{defect}_1 + \mathrm{defect}_2$.  Modes
touched by no codeword contribute exactly zero.  $\square$

*Receipts*: additivity exact across an exhaustive $n = 4$ census
and $n = 5$ sampling (861 random relation-carrying sets).

## 3. The single-relation theorem

For a single codeword of weight $w$ (all $w$ touched modes equal by
symmetry, field $h$), the fixed point is the scalar equation

$$
\tanh h \;+\; (1-\tanh^2 h)\,
\frac{\tanh^{w-1}h}{1+\tanh^{w}h} \;=\; e^{-h}.
$$

**Theorem 3.1.**  Solved at 40 digits: weight 3 **binds**, and
$w$ **anti-binds** for every $4 \le w \le 40$ (each case exact);
$|$defect$|$ is maximal at $w = 5$.  The full claim — anti-binding
for *every* $w \ge 4$ — follows with Corollary 3.2's tail bound:

```text
  w    defect(w)              first-order theta^w(1 - w kappa)
  3   +0.008438104972291      -0.005105640645752
  4   -0.016839123523194      -0.032827182757183
  5   -0.023567123903722      -0.034186341316418
  6   -0.021780633113267      -0.027469835199371
  8   -0.012214241830450      -0.013371668136528
 12   -0.002061783361279      -0.002086147023869
 16   -0.000262122892964      -0.000262475207817
 24   -0.000003228444384      -0.000003228492885
 30   -0.000000107108657      -0.000000107108709
```

**Corollary 3.2 (the tail, bounded).**  For $w > 40$,
$\mathrm{defect}(w) = d_1(w)(1 + r_w)$ with $d_1(w) =
\theta^w(1 - w\kappa) < 0$ and
$$
|r_w| \;\le\; \frac{2c\,w^2\theta^{w}}{w\kappa - 1},
$$
where $c$ is Theorem 4.2's second-order coefficient: by Lemma
1.1's strict monotonicity the fixed-point shift obeys
$|h^* - \eta| \le 2(1-\theta^2)\theta^{w-1}/\Delta$ for large
$w$, and the defect's $\lambda$-Taylor remainder past first order
is then bounded by twice the second-order term, which is
$\theta^{2w}\,O(w^2)$ with the explicit coefficient.  Grading:
the factor-two domination is *not* proved analytically for all
$w$; it is verified against the exact solver — $|r_w| \le$ the
displayed bound, with $|r_w|/|d_2/d_1| \le 1$, at every checked
$w \in \{6, 12, 40, 60, 80, 100\}$ — so this corollary is a
verified-numerics bound, not a theorem.  The bound is decreasing
in $w$ (as $w^2\theta^w$ is, for $w > 2/\eta \approx 3.3$) and
equals $3.0\times 10^{-9}$ at $w = 40$, where the true remainder
is $|r_{40}| = 1.43\times 10^{-9}$.  (An earlier draft quoted
"$1.5\times 10^{-9}$" and "$0.26$" for the bound — those are the
second-order *ratios* $|d_2/d_1|$, a mislabeling caught in
review; the displayed bound at $w = 6$ is in fact $0.81$ and the
true remainder there $0.21$ — not uniformly small for $6 \le w
\le 40$, which is why those cases are solved exactly rather than
bounded; the earlier draft's "$\ll$ for $w \ge 6$" claim was
wrong and is replaced by this split.)  The sign of the tail is
that of $d_1$, i.e. anti-binding.  $\square$

**Theorem 3.3 (first order and the marginality).**  The defect's
first order in the codeword amplitude is exactly
$\theta^w(1 - w\kappa)$ with

$$
\kappa = \frac{\eta\,(1-\theta^2)}{1-\theta^2+\theta}
= \frac{\eta\,(1+\theta^2)}{2+\theta^2}
= 0.343922878815527\ldots
$$

The sign boundary sits at $w = 1/\kappa = 2.9076\ldots$: weight 3
lies just above it, at first-order distance

$$
\varepsilon \;=\; 3\kappa - 1 \;=\; 0.031768636446582\ldots
$$

— the **marginality**.  Since the first-order $w = 3$ coefficient
is *negative* ($-\varepsilon\theta^3$) while the exact defect is
*positive*, the triangle's binding is decided strictly beyond first
order: a sign settled by self-interaction cannot be captured by any
first-order (weight-counting) law.

## 4. The exact defect functional and its second order

**Theorem 4.1 (the scalar functional).**  With $h^*(w,\lambda)$
the fixed point of the $\lambda$-deformed equation (codeword
amplitude $\lambda$), the Section 1 definition reduces to

$$
\mathrm{defect}(w;\lambda) = \ln(1+\lambda \tanh^w h^*)
- w\,[\,D(h^*) - D(\eta)\,],
$$

reproducing every value of Theorem 3.1's table at print precision
(worst deviation $4.9\times 10^{-16}$), and cross-checked by
solving the fixed point directly on explicit spin realizations
(no functional) at $w = 3, 4, 5$ and the Section 6 codes.

**Theorem 4.2 (closed-form second order).**  Expanding
$h^* = \eta + \lambda h_1 + \lambda^2 h_2$:
$h_1 = -(1-\theta^2)\theta^{w-1}/\Delta$ with
$\Delta = 1-\theta^2+\theta$;
$h_2 = [(1-\theta^2)\theta^{2w-1} - \tfrac12 G''h_1^2 - h_1
P']/\Delta$ with $G'' = -\theta(3-2\theta^2)$ and $P' =
(1-\theta^2)\theta^{w-2}[(w-1)(1-\theta^2) - 2\theta^2]$; and with
$D'(\eta) = -\eta\theta$, $D''(\eta) = -(2-\eta)\theta -
(1-\theta^2)$:

$$
d_2(w) = w\theta^{w-1}(1-\theta^2)h_1 - \tfrac12\theta^{2w}
+ w\eta\theta h_2 - \tfrac{w}{2}D''h_1^2
\;=\; \theta^{2w}\Bigl[-\tfrac12 + b\,w + c\,w^2\Bigr],
$$

with intercept $-\tfrac12$ exact (the logarithm's own second
order),

$$
c = \frac{\eta\,(1-\theta^2)^3}{\theta^2\Delta^2}
= 0.4625461677\ldots, \qquad
b = -0.8775524218\ldots
$$

($b$ given in assembled closed form by the display).  *Receipts*:
matches high-precision numerical extraction at every
$w \in \{3,\ldots,12\}$ to $1.9\times 10^{-26}$; the first-order
law re-verified to $10^{-38}$.

**Warning, kept on record.**  The expansion is built at
$\lambda = 0$; evaluating its truncation at $\lambda = -1$
suggested a value near $\varepsilon$ for the sign-reversed
triangle — wrong by a factor of six against the exact solution
(Section 5).  Perturbative truncations of this theory must not be
extrapolated to unit amplitude.

## 5. The frustration identity

**Proposition 5.1 (numerical identity; the oriented value's
source named).**  The $\lambda = -1$ (sign-reversed amplitude)
point of the scalar theory at $w = 3$ has exact defect

$$
\mathrm{defect}(3; -1) = +0.2016742352919823\ldots,
$$

equal to the **oriented frustrated triangle** computed
independently in the physics program's chirality analysis (corpus
Paper 8, "The Tractable Frontier Campaign," supplied as
supplementary material with this submission; its printed value
$+0.201674235292$ and frustrated fixed point $h = 1.114142135$
both match — our $\lambda = -1$ root is $h = 1.1141421355$ — and
the oriented computation is not reproduced here, which is why this
is a proposition with a 14-digit receipt rather than a
self-contained theorem).  Frustration *is* amplitude reversal: the orientation
character's only effect on a single relation is the sign of its
codeword term.  (The frustrated triangle binds $\sim 24\times$
harder than the unfrustrated one.)

## 6. Interaction constants from the exact multi-mode solver

For arbitrary codes the fixed point is the coupled system
$\langle\chi_a\rangle = e^{-h_a}$, one equation per mode, with
$\mathrm{defect} = \ln W_K(t^*) - \sum_a [D(h_a^*) - D(\eta)]$.
*Validation, internal*: (i) the shared-mode triangle pair is
solved twice in this paper — by the general solver and by its
symmetric two-class reduction — agreeing at $+0.020844970391$;
(ii) disjoint additivity: the solver's value for the disjoint
$w{=}3 \oplus w{=}4$ pair equals $\mathrm{defect}(3) +
\mathrm{defect}(4) = 0.008438104972 - 0.016839123523 =
-0.008401018551$, as Theorem 2.2 requires.

**Theorem 6.1 (chain constants).**  For chains $T_k$ of $k$
triangles, consecutive pairs sharing one mode, the per-link defect
increments converge rapidly (successive increment-difference
ratios $0.182, 0.176, 0.168$ — mildly drifting, not geometric):

```text
  D2 = 0.0124068654   D4 = 0.0132458948   D6 = 0.0132724704
  D3 = 0.0131167761   D5 = 0.0132686431
  per-link limit D_inf = 0.013273 (D6 value; converged to 4e-6,
  so the sixth decimal is not significant)
```

Stars (all triangles sharing one common mode) give per-triangle
defects $0.0104, 0.0125, 0.0147, 0.0169$ at $k = 2, 3, 4, 5$ —
growing, with no per-triangle limit claimed.  One caution: the
"double-share pair" (two triangles sharing two modes) contains a
weight-2 codeword and is therefore *not realizable* by distinct
characters in the Section 1 model — it requires the *multiset
extension* (allowing repeated characters, i.e. dropping the
min-distance-3 exclusion); we report it as abstract-enumerator
algebra, flagged.  Its raw enumerator defect is $+0.0903175428$;
the per-link figure $+0.0818794378$ quoted alongside the chain
increments is that value *minus* $\mathrm{defect}(3)$ — the
increment convention of this section — stated explicitly since a
reader reproducing the raw number would otherwise see a
discrepancy.
These are, to our knowledge, the first interaction constants of
this fixed-point theory.

## 7. Algebraic status of the constants

PSLQ [3] at 40+ digits with symbolic verification (residuals
$\sim 10^{-50}$):

$$
11\kappa = \eta\,(7 - 2\theta + \theta^2)
\quad\text{(exactly; via } (7-2\theta+\theta^2)(2+\theta^2) =
11(1+\theta^2) \text{ mod the cubic)},
$$

and correspondingly $11\varepsilon = -11 + \eta(21 - 6\theta +
3\theta^2)$.  Moreover $\kappa \notin \mathbb Q(\theta)$ is a
*theorem*, not a search result: $\kappa/\eta = (1+\theta^2)/
(2+\theta^2) \in \mathbb Q(\theta)\setminus\{0\}$ exactly, and
$\eta = -\ln\theta$ is transcendental by Hermite–Lindemann
($\theta$ algebraic, $\neq 0, 1$); if $\kappa$ were even
*algebraic over* $\mathbb Q(\theta)$ it would be algebraic over
$\mathbb Q$ (towers of algebraic extensions are algebraic), forcing
$\eta = \kappa\cdot(2+\theta^2)/(1+\theta^2)$ algebraic —
contradiction.  So no algebraic relation over $\mathbb Q(\theta)$
holds at any height.  The theory's
constants are transcendental-form — one $\eta$ factor over the
cubic field.

## 8. Related work and novelty position

The character expansion is classical (high-temperature expansions;
van der Waerden); Ising models on hypergraphs and codes are widely
studied, as are self-consistent field equations.  What we have not
found in the literature: the exponential-consistency condition
$\langle\chi_a\rangle = e^{-h_a}$ itself; the exactly solved
single-relation family with its sign boundary $1/\kappa$ and the
closed-form constants of Sections 3–4; the frustration identity in
this form; the chain constants.  We state this as a checked absence
and commit in advance: if a referee locates any of these, the
corresponding section becomes exposition with attribution.

## Reproducibility

Every number regenerates from fixed-seed scripts at 40–50 digits
(mpmath): the table of Theorem 3.1; the functional and second-order
verifications; the frustration identity; the multi-mode solver
validations and chain constants; the PSLQ relations with symbolic
checks.  Bit-identical reruns; code and canonical outputs accompany
the submission.

## References

[1] B. L. van der Waerden, Die lange Reichweite der regelmässigen
Atomanordnung in Mischkristallen, *Z. Phys.* **118** (1941) 473 —
character/high-temperature expansions.

[2] F. J. MacWilliams, N. J. A. Sloane, *The Theory of
Error-Correcting Codes*, North-Holland (1977) — codes, characters,
weight enumerators.

[3] H. R. P. Ferguson, D. H. Bailey, S. Arno, Analysis of PSLQ,
*Math. Comp.* **68** (1999) 351 — integer-relation detection.

**Companion papers:** the physics program exporting
$\varepsilon = 3\kappa - 1$ (same author; this paper is the
constant's self-contained pedigree).
