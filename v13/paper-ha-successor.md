# HA — THE RECORD-NATIVE `H_a[N]`, CONSTRUCTED; AND THE DEFORMATION-CLOSURE TEST, RUN

**Status:** GREEN-UNREVIEWED, STRICT, 2026-08-08.
**Pin:** `v13/note-ha-successor-pin.md` (frozen; immutable base commit `024fcd7`).
**Binding:** `v13/note-gw1-metric-from-closure.md` — TERMINAL at v13 LOG #5 —
and in particular its §7.1 successor directive, quoted verbatim in §1;
`v13/note-gw1-metric-from-closure-pin.md`; v4 paper 7 Definitions 1.1–1.4 and
2.1–2.5; v4 paper 12 Definition 11.6M; `v13/relativistic-isp-v13-paper0-gravity.md`
(the charter, `[DRAFT]`).  Declared secondary:
`v13/paper-nt-nomological-transport.md` and `v13/paper-gen-generality-check.md`,
both receipts hash-pinned in §11.
**Verdict:** **`HA-RUNNABLE` + `HA-BRIDGE-NOT-POSABLE`.**
**Deliverables:** this note; `v13/code/ha_successor_exact.py`,
`v13/code/ha_successor_output.txt`, `v13/code/ha_successor_receipt.json`.

---

## Scope box

The pin's three-defect separation is engraved and is not relaxed anywhere below.
Quoting v13 paper 0 §2:

> $$\Delta^B \;\neq\; \Omega_{\mathrm{hypersurface}} \;\neq\;
> R^{\rho}{}_{\sigma\mu\nu}.$$
>
> They can be related, but identifying them would repeat the v1 $H^1$ mistake at
> a higher level.

Nothing below identifies any two of them.  **No Einstein-dynamics claim of any
kind is made**: no field equation, no backreaction, no stress response, no
constraint preservation, no continuum limit.  v13 paper 0 §5 remains out of
scope and the charter stays `[DRAFT]`.

The GW1 kill condition, quoted once, verbatim from v13 paper 0 §6:

> If the metric must already be inserted into $J[N]$, or if the same record law
> permits inequivalent recovered tensors, then the deformation algebra is
> representing geometry rather than explaining it.

**The kill fires, and it is measured rather than asserted.**  That is this
unit's contribution: GW1's conditional — "the corpus can either obtain
nontrivial closure by supplying geometry, or remain record-native and fail to
produce the required closure" — becomes a measurement on a constructed
substrate, with the sector where each alternative holds named and counted (§6).

Everything below is at ONE declared finite arena: $d = 2$ (primary) and $d = 3$
(extension) spatial directions, $L = 3$ sites per direction, the declared link
set, the declared record family, the declared lapse family, the declared
drag-rule family, the declared density-weight convention, the declared
tangential realisation, and three declared primes for the operator layer.  No
continuum limit, no refinement sequence, and no general-$d$, general-$L$,
general-record or general-lapse claim is made.

---

## 1. The order, and what it required

The terminal GW1 census closed with a directive, quoted verbatim:

> **First — construct a record-native `H_a[N]` to v4 paper 7 Definition 1.3, and
> measure `R_{HH,a}[N,M]` against
> `β_a^i = I_a(g)^{ij}(N∂_jM − M∂_jN)` with `I_a(g)^{ij}` supplied by the
> order+count extraction of `v6_task2b`.**

with co-requisites listed from GW1 §5: `∇_j` on the slice, `K_i` and its
inverse, a transported second step, an `ε` to pin, a fixed density-weight
convention, the `q_comp`/`q_order` gauge-and-scale identification, and a
lapse-pair family of full rank at each point.

The directive is executed with **one substitution**, declared here and carried
in the deviations (§12).  `v6_task2b` is **not** used as the metric readout.
GW1's own §2 grades it partial: its fit runs against embedding coordinate
separations `dx = P[b] − P[a]` and its constant `K` is calibrated against the
true interval.  Using it would insert held-out embedding data into `β` and would
fail GW1 §1.2 at the first line.  Instead the metric candidate is read where v4
paper 7 Definition 1.4 says it lives — **from the finite geometry record
itself** — by the corpus's own order+count relation, interval cardinality as
squared separation (§3.2).

The co-requisites are discharged or declared as follows.

- `∇_j` on the slice: the declared forward difference on the record adjacency.
- A transported second step: built in, and measured **necessary** (§6.4).
- `K_i`, its inverse, and `ε`: **eliminated, not supplied.**  The residual is
  posed in v4 paper 7 Definition 2.3's exact multiplicative form, which needs
  no division by $\epsilon^2$ and no decoder inverse — the tangential
  correction is included rather than fitted.  GW1 §5 items 2 and 4 are
  therefore not open here; they are not needed by this formulation, which is
  itself a declared narrowing of GW1's original STEP 4.
- The density-weight convention: declared, and flip-tested (§7.5).  It moves
  the verdict, and that is reported.
- The lapse-pair rank: measured full (§4.2).  This is the first time that
  co-requisite has been tested anywhere in the corpus.
- The `q_comp`/`q_order` identification: not required, because there is only
  one metric object here — the record-read $I_a(g)$.

---

## 2. What is new, in one paragraph

GW1's block had two faces: where the corpus's two-order machinery is metric-free
and nontrivial it carries no lapse profile, and where it is lapse-profiled
either the two-cell is trivial or undefined or the metric is inserted into the
construction.  The object built here has, simultaneously and in runnable form,
all five of GW1 §1.1's conditions: a lapse-profiled comparison family; a
construction that calls no metric estimator, no embedding coordinate, no
background normal and no planted frame; a defined, nontrivial, **transported**
two-cell; the residual posed in a form needing no decoder; and a metric read
from the same record on the same hypersurface.  It is invertible by construction
with a closed-form inverse, not by declaration.  Everything it uses is the
corpus's own division-event counts.

---

## 3. The construction

### 3.1 The arena, declared as data

| coordinate | value |
|---|---|
| sites | $X = (\mathbb Z_L)^d$, $L = 3$; $d = 2$ primary ($\lvert X\rvert = 9$), $d = 3$ extension ($\lvert X\rvert = 27$) |
| record adjacency | periodic, direction-labelled; links $\mathcal L$ = the $d$ axis links and the $\binom d2$ positive diagonals |
| geometry record | $s$: for each site $x$ and link $\ell$, the interval cardinality $n_\ell(x)\in\mathbb Z_{>0}$ |
| front | $n : X\to\mathbb Z$; $n(x)$ = the number of division events already committed at record site $x$ |
| matter record | $m : X\to\mathbb Q^d$, the address register: the recorded tangential address of the matter carrier at $x$ |
| total records | $C^{tot} = C^{matter}\times C^{geom}$, $V_a^{tot} = \mathbb R^{C^{tot}}$ (v4 p7 Def 1.1) |
| lapse family | the $\lvert X\rvert$ site deltas, the constant profile $1$, and the $d$ chart ramps — **12** members at $d=2$, **132** ordered pairs |
| declared finite difference | $\partial_j F(x) := F(x+e_j) - F(x)$ |
| density weight | $I_a(g) := q^{-1}\cdot(\det q)^w$; $w = 0$ primary, $w = 1$ flipped |
| operator-layer primes | $p \in \{5, 7, 13\}$ |

Every entry is a declaration recorded before any fixture value is evaluated.
The instrument measures its fixture-evaluation counter to be **zero** at the
freeze point (G01), and the `freeze-lax` mutant, which evaluates one datum
first, dies there.

### 3.2 The geometry record, and the metric candidate it carries

The geometry record is count data on the corpus's own division/record structure:
$n_\ell(x)$ is the number of division events in the record interval between $x$
and $x+\ell$.  GW1 §1.2 permits event counts and record adjacency explicitly.
The metric candidate is read from that record by the corpus's own order+count
relation — interval cardinality as squared separation — solved exactly:

$$q_{ij}(x)\,e_\ell^i e_\ell^j \;=\; n_\ell(x)\quad\text{for every }\ell\in\mathcal L,
\qquad I_a(g)^{ij}(x) \;:=\; (q^{-1})^{ij}(x)\cdot(\det q)^{w}(x).$$

At $d = 2$ the three links determine the three components of $q$ exactly; at
$d = 3$ the six links determine the six.  A record is **admissible** when $q$ is
nonsingular and positive definite at every site, by the exact Sylvester
criterion, and $q^{-1}$ exists at every site.

### 3.3 `H_a[N]`, and its inverse

$$H_a[N]\,(n, m) \;=\; \bigl(\,n + N,\;\; m + w[N,n]\,\bigr),\qquad
H_a[N]^{-1}(n, m) \;=\; \bigl(\,n - N,\;\; m - w[N,\,n-N]\,\bigr),$$

with the record-native drag field, in two declared architectures:

$$\text{(A)}\qquad w[N,n]^i(x) \;=\; N(x)\sum_{j} \Lambda^{ij}(x)\bigl(n(x+e_j)-n(x)\bigr),$$

$$\text{(B)}\qquad w[N,n]^i(x) \;=\; N(x)\sum_{\ell\in\mathcal L}\lambda_\ell(x)\,e_\ell^i\bigl(n(x+e_\ell)-n(x)\bigr).$$

The drag has exactly two ingredients: the **front tilt** $n(x+e)-n(x)$, a
difference of committed division-event counts, and the **eventwise lapse value**
$N(x)$.  Both are on GW1 §1.2's permitted list.  Nothing else enters.

The map is a bijection of the total configuration set, hence an invertible
algebraic map on $V_a^{tot}$ exactly as v4 paper 7 Definition 1.3 requires — and
here **constructed**, not declared: it is a skew product over the front, so the
front is recovered first and the drag is then determined.

**The second normal step is transported along the first.**  In $H_a[M]H_a[N]$
the $M$-step's drag is evaluated at the already-advanced front $n+N$.  That is
GW1 §1.1 condition 3, which the census found implemented on no record
substrate.

### 3.4 The drag-rule family, declared

| rule | arch | weight |
|---|---|---|
| `A-chart` | A | $\Lambda = \delta$, count-blind |
| `A-axis` | A | $\Lambda = \operatorname{diag}(1/n_{e_j})$ — **link-local** in the axis interval counts |
| `A-linkframe` | A | $\Lambda^{ij} = \sum_{\ell}e_\ell^ie_\ell^j/n_\ell$ over every declared link |
| `A-linkhalf` | A | $\tfrac12\sum_\ell e_\ell e_\ell^{\mathsf T}/n_\ell$ (declared normalisation variant) |
| `A-insert` | A | $\Lambda = I_a(g)$ — **positive control**, the metric inserted |
| `A-insert-x` | A | $I_a(g)$ with the cross term sign-flipped — **broken** |
| `A-insert-2x` | A | $2\,I_a(g)$ — **broken** |
| `A-notransport` | A | $I_a(g)$, but the drag reads a **frozen reference front** — **broken** |
| `B-axis`, `B-all`, `B-chart` | B | $\lambda_\ell = 1/n_\ell$ on the axis links, on every link, and $\lambda_\ell = 1$ on the axis links |

### 3.5 `D_a[v]`, and the bookkeeping split

$D_a[v]$ is v4 paper 7 Definition 1.2's tangential comparison map.  Two
realisations are declared, and both are measured (§7.6):

- **D-REG** (primary): $D_a[v]$ shifts the address register by $v$; the geometry
  front is not transported.
- **D-TOT** (flip-test): $D_a[v]$ shifts the register **and** drags the front
  along the site map $x\mapsto x+v(x)$, defined only where that map is a
  bijection.

### 3.6 The residual and the detector

$$R_{HH,a}[N,M] \;:=\; H_a[N]H_a[M]H_a[N]^{-1}H_a[M]^{-1}\,D_a\bigl[-\beta_a(g;N,M)\bigr],
\qquad \beta_a^i \;=\; I_a(g)^{ij}\bigl(N\partial_jM - M\partial_jN\bigr),$$

exactly v4 paper 7 Definitions 2.3 and 1.4, with the declared finite bracket
covector

$$\omega_j(x) \;:=\; N(x)M(x+e_j) - M(x)N(x+e_j) \;=\; \bigl(N\partial_jM - M\partial_jN\bigr)(x).$$

The detector is v4 paper 12 Definition 11.6M verbatim,
$\mathsf W_{N|ML,a} := \mathsf C\bigl(H_a[N], D_a[B_{ML,a}]\bigr)\,H_a[\mathcal L_{B_{ML,a}}N]$
with $B_{ML,a} = \beta_a(g;M,L)$ and $\mathcal L_BN = B^j\partial_jN$ the
declared finite transported lapse derivative, and
$\mathsf{SW}_{HHH,a} = \mathsf W_{N|ML}\mathsf W_{M|LN}\mathsf W_{L|NM}$.

### 3.7 Two layers, three comparators

The residual is computed by routes that share no code.

- **The exact rational layer.**  Every object is an exact `Fraction`-valued
  field; the residual is the register displacement of the literal five-map
  composition.  No modulus, no truncation, no tolerance.
- **The closed form**, built from the drag rule and the record readout without
  touching the composition:
  $\rho^i(x) = \bigl(\Lambda^{ij}(x)-I^{ij}(x)\bigr)\omega_j(x)$ for
  architecture A, and $\sum_\ell\lambda_\ell e_\ell^i\omega_\ell - \beta^i$ for
  architecture B.
- **The finite operator layer.**  On a declared finite total-configuration
  carrier $C_{red} = \mathcal F\times\mathcal A$ — $\mathcal F$ the front sector
  $n_0 + \operatorname{span}_{\mathbb F_p}\{N,M\}$, $\mathcal A = (\mathbb F_p)^d$
  the address register at a declared detector site — every comparison map is an
  explicit permutation and $R_{HH}$ is formed as a genuine operator product.
  This is Definition 2.3 as an operator on $V_a^{tot}$, with Definition 2.4's
  norm on the declared test class of indicator effects:
  $\lVert R\rVert$ = configurations moved, over carrier size.

---

## 4. What is measured before anything else

### 4.1 The record family and its readout

Counts are listed as $(n_{e_1}, n_{e_2}, n_{e_1+e_2})$ and the symmetric
matrices by their components $(q_{11}, q_{12}, q_{22})$ and
$(I^{11}, I^{12}, I^{22})$, all at the site $(0,0)$.

| record | counts at $(0,0)$ | counts at $(1,1)$ | $q$ | $\det q$ | $I = q^{-1}$ | homog. | adm. |
|---|---|---|---|---|---|---|---|
| `G-FLAT` | $(1,1,2)$ | $(1,1,2)$ | $(1,0,1)$ | $1$ | $(1,0,1)$ | yes | yes |
| `G-DIAG2` | $(2,2,4)$ | $(2,2,4)$ | $(2,0,2)$ | $4$ | $(1/2,0,1/2)$ | yes | yes |
| `G-ANISO` | $(1,4,5)$ | $(1,4,5)$ | $(1,0,4)$ | $4$ | $(1,0,1/4)$ | yes | yes |
| `G-ANISO2` | $(4,9,13)$ | $(4,9,13)$ | $(4,0,9)$ | $36$ | $(1/4,0,1/9)$ | yes | yes |
| `G-CURVED` | $(1,1,2)$ | $(2,2,4)$ | $(1,0,1)$ | $1$ | $(1,0,1)$ | **no** | yes |
| `G-OFFDIAG` | $(2,2,6)$ | $(2,2,6)$ | $(2,1,2)$ | $3$ | $(2/3,-1/3,2/3)$ | yes | yes |
| `G-OFFDIAG2` | $(3,5,12)$ | $(3,5,12)$ | $(3,2,5)$ | $11$ | $(5/11,-2/11,3/11)$ | yes | yes |
| `G-OFFNEG` | $(3,5,4)$ | $(3,5,4)$ | $(3,-2,5)$ | $11$ | $(5/11,2/11,3/11)$ | yes | yes |
| `G-CURVOFF` | $(2,2,6)$ | $(3,3,10)$ | $(2,1,2)$ | $3$ | $(2/3,-1/3,2/3)$ | **no** | yes |
| `G-SINGULAR` | $(1,1,4)$ | $(1,1,4)$ | $(1,1,1)$ | $0$ | none | yes | **no** |
| `G-INDEF` | $(1,1,6)$ | $(1,1,6)$ | $(1,2,1)$ | $-3$ | $(-1/3,2/3,-1/3)$ | yes | **no** |

Nine records admissible; the two declared negative controls rejected, one in
each failure mode (G02).  The `posdef-lax` mutant, which blinds the Sylvester
criterion, dies on the indefinite one.

### 4.2 Identifiability: the lapse-pair rank

GW1 §5 item 7 names the rank test and records that "no committed run tests
rank".  It is tested here.  Over the declared lapse family the realised bracket
covectors $\omega(x) = (\omega_1(x),\omega_2(x))$ span a space of rank **2** —
full — at **every one of the 9 sites**.  The closure relation therefore
determines the structure function uniquely: two rules with different weights
cannot both close.  The `rank-lax` mutant, which degenerates the lapse family to
a proportional family, dies on this gate.

---

## 5. The construction runs

$H^{-1}H = HH^{-1} = \mathrm{id}$ is measured on **396** (rule, record, lapse)
triples, with **0** failures; and the declared non-injective falsifier — a
variant that collapses the address register — is measured **rejected** by the
same predicate (G04).  The `invert-lax` mutant, which blinds that predicate,
dies there; so does `transport-off`, because a drag read at the wrong front is
no longer inverted by the closed form.

The literal five-map composition and the independently built closed form agree
field by field at **1188** comparisons, **0** disagreements (G05).  The
comparator is not a copy of the audited object routed through it: `sign-flip`,
`order-swap`, `omega-asym` and `transport-off` each move one side and not the
other, and each dies at G05.

The finite operator layer builds **1056** reduced carriers over $p\in\{5,7,13\}$
with **0** non-bijective comparison maps and **0** operator-versus-field
mismatches (G10); **33** carriers are skipped because the exact-to-$\mathbb F_p$
reduction of a rational entry is undefined at that prime, and that count is
printed rather than hidden.  No cell with a nonzero exact residual is invisible
at every tested prime — counting an undefined reduction as not seeing it (G10B);
the `prime-single` mutant, which collapses the multi-prime control to one prime,
dies there on the cell `A-linkframe | G-OFFDIAG2`, whose exact residual at the
detector site is $(35/132,\;7/660)$: its reduction is **undefined** mod 5 (a
denominator divisible by 5) and exactly $(0,0)$ mod 7, so the operator layer is
blind to a nonzero residual at both, and only $p = 13$, where it reduces to
$(11,2)$, sees it.  A second,
differently routed comparator reads the operator's own register displacement off
the permutation and matches the reduced exact field at **76** of 76 tested cells
(G11).

---

## 6. The closure result

### 6.1 The table

Cells give the number of the **132** ordered lapse pairs at which
$R_{HH,a}[N,M]$ is **not** the identity; `CLOSES` means none of them, at every
one of the 9 sites.

| rule | `G-FLAT` | `G-DIAG2` | `G-ANISO` | `G-ANISO2` | `G-CURVED` | `G-OFFDIAG` | `G-OFFDIAG2` | `G-OFFNEG` | `G-CURVOFF` |
|---|---|---|---|---|---|---|---|---|---|
| `A-chart` | CLOSES | 96 | 70 | 96 | 84 | 96 | 96 | 96 | 96 |
| `A-axis` | **CLOSES** | **CLOSES** | **CLOSES** | **CLOSES** | **CLOSES** | 96 | 96 | 96 | 96 |
| `A-linkframe` | 96 | 96 | 96 | 96 | 96 | 96 | 96 | 96 | 96 |
| `A-linkhalf` | 96 | 96 | 96 | 96 | 96 | 96 | 96 | 96 | 96 |
| `A-insert` | CLOSES | CLOSES | CLOSES | CLOSES | CLOSES | CLOSES | CLOSES | CLOSES | CLOSES |
| `A-insert-x` | CLOSES | CLOSES | CLOSES | CLOSES | CLOSES | 96 | 96 | 96 | 96 |
| `A-insert-2x` | 96 | 96 | 96 | 96 | 96 | 96 | 96 | 96 | 96 |
| `A-notransport` | 96 | 96 | 96 | 96 | 96 | 96 | 96 | 96 | 96 |
| `B-axis` | CLOSES | CLOSES | CLOSES | CLOSES | CLOSES | 96 | 96 | 96 | 96 |
| `B-all` | 78 | 78 | 78 | 78 | 78 | 114 | 114 | 114 | 114 |
| `B-chart` | CLOSES | 96 | 70 | 96 | 84 | 96 | 96 | 96 | 96 |

**The result is two-sided.**

> **The GW1 deformation-closure test runs, and on the diagonal sector it
> CLOSES.**  The link-local record-native rule — whose weight is
> $\operatorname{diag}(1/n_{e_j})$, read from the axis interval counts alone,
> with no metric estimator anywhere in its construction — gives
> $R_{HH,a}[N,M] = \mathrm{id}$ exactly, at all 132 tested lapse pairs and all 9
> sites, on all **five** records whose order+count readout is diagonal:
> `G-FLAT`, the scaled-flat `G-DIAG2`, the two homogeneous anisotropic records
> `G-ANISO` and `G-ANISO2`, and the **inhomogeneous** diagonal record
> `G-CURVED`.

> **At the cross term it does not close, and the anomaly is exact.**  On all
> four records whose readout carries $q_{12}\neq0$ the residual is nonzero at 96
> of the 132 pairs.

The gap $\Lambda - I$ at the site $(0,0)$, by components
$\bigl((\Lambda-I)^{11}, (\Lambda-I)^{12}, (\Lambda-I)^{22}\bigr)$, for the
link-local rule `A-axis`:

| record | $q_{12}$ | $\Lambda - I$ at $(0,0)$ | $\max\lvert\rho\rvert$ |
|---|---|---|---|
| the five diagonal records | $0$ | $(0,0,0)$ | $0$ |
| `G-OFFDIAG` | $1$ | $(-1/6,\;1/3,\;-1/6)$ | $2$ |
| `G-OFFDIAG2` | $2$ | $(-4/33,\;2/11,\;-4/55)$ | $40/33$ |
| `G-OFFNEG` | $-2$ | $(-4/33,\;-2/11,\;-4/55)$ | $20/33$ |
| `G-CURVOFF` | $1$ | $(-1/6,\;1/3,\;-1/6)$ | $2/3$ |

### 6.2 Positive and negative controls

- **Positive control (G06):** the metric-inserted rule closes exactly at every
  admissible record and every tested pair — 9 of 9 records.
- **Negative control with teeth (G07):** every declared broken variant fails
  closure — `A-insert-x` on 4 records (exactly the four with a nonzero cross
  term, since flipping the sign of a zero is a no-op), `A-insert-2x` on 9,
  `A-notransport` on 9.  `closure-lax`, `control-lax` and `readout-local` each
  die here.

### 6.3 The sector law: closure IS insertion

Cells read *(sites where $\Lambda = I_a(g)$) / (sites where the residual
vanishes at all 132 pairs)*, out of 9.

| rule | `G-FLAT` | `G-DIAG2` | `G-ANISO` | `G-ANISO2` | `G-CURVED` | `G-OFFDIAG` | `G-OFFDIAG2` | `G-OFFNEG` | `G-CURVOFF` |
|---|---|---|---|---|---|---|---|---|---|
| `A-chart` | 9/9 | 0/0 | 0/0 | 0/0 | 1/1 | 0/0 | 0/0 | 0/0 | 0/0 |
| `A-axis` | 9/9 | 9/9 | 9/9 | 9/9 | 9/9 | 0/0 | 0/0 | 0/0 | 0/0 |
| `A-linkframe` | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 |
| `A-linkhalf` | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 |
| `A-insert` | 9/9 | 9/9 | 9/9 | 9/9 | 9/9 | 9/9 | 9/9 | 9/9 | 9/9 |
| `A-insert-x` | 9/9 | 9/9 | 9/9 | 9/9 | 9/9 | 0/0 | 0/0 | 0/0 | 0/0 |
| `A-insert-2x` | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 |
| `A-notransport` | 9/0 | 9/0 | 9/0 | 9/0 | 9/0 | 9/0 | 9/0 | 9/0 | 9/0 |

Over the **63** transported-rule cells the two columns agree everywhere:
**0 mismatches** (G08).  Note the `A-chart` / `G-CURVED` cell, 1/1: on the
inhomogeneous diagonal record the chart-identity weight coincides with the
record-read inverse metric at exactly one site — the one where the counts happen
to be unity — and closure holds at exactly that site and nowhere else.  The
sector law is measured at site resolution, not only at record resolution.

**Disclosure (X02).** The equivalence in G08 is **analytically forced** once
§4.2's rank is full: $\rho^i = (\Lambda^{ij}-I^{ij})\omega_j$ vanishes on a
spanning covector family if and only if $\Lambda = I$.  It is recorded as a
disclosure, not claimed as an independent discovery.  The measured content is
the rank that makes the statement bite, the cell census above, the residual
magnitudes of §6.1, and §6.5's obstruction.

### 6.4 Insertion alone does not buy closure: transport is necessary

The `A-notransport` row is the sharpest single measurement in the unit.  That
variant is **fully metric-inserted** — its weight equals the record-read
$I_a(g)$ at 9 of 9 sites on every one of the 9 records — and its residual
vanishes at **0** of 9 sites on every one of them (G08B).  Its only defect is
that its drag reads a frozen reference front instead of the current one, so its
normal steps commute in the register and the group commutator contributes
nothing, leaving $\rho = -\beta$ uncancelled.

> **GW1 §1.1 condition 3 is not a bookkeeping nicety.**  Supplying the metric is
> insufficient; the second normal step must be transported along the first, and
> the price of dropping it is the whole tangential correction.

### 6.5 No link-local record-native weight can close

A weight is **link-local** when $\lambda_\ell$ is a function of $n_\ell$ alone.
The obstruction is exhibited, not argued: `G-CURVOFF` and `G-DIAG2` **agree** on
the interval count of the link $e_1$ — both carry $n_{e_1}(0,0) = 2$ — while
their full count vectors are $(2,2,6)$ and $(2,2,4)$ and the record-read inverse
metric demands $I^{11} = 2/3$ at the first and $1/2$ at the second (G09).

The mechanism: $I^{jj} = \operatorname{adj}(q)^{jj}/\det q$, and $\det q$ is a
**joint** function of every link count at the site.  A weight that reads only
its own link's count cannot see it.  Closure therefore requires a rule that
computes the record's count-matrix inverse — which is the metric.  The
`readout-local` mutant, which replaces the readout by a link-local surrogate,
dies here and at three further gates.

That is why `A-axis` closes exactly on the diagonal sector: there $\det q$
factorises, $\operatorname{adj}(q)^{jj}/\det q = 1/q_{jj} = 1/n_{e_j}$, and the
link-local rule coincides with the metric by arithmetic rather than by design.
Off the diagonal sector the factorisation fails and so does the closure.  This
is an independent recurrence, at a completely different construction, of v2
paper 10 Proposition 10.4's wall — the leading coefficient there sees $h^{11}$
and $h^{22}$ but not $h^{12}$.

### 6.6 The two architectures

Architecture B's link-sum form (`B-all`) never closes, on any record: it carries
diagonal-link differences $\omega_{e_1+e_2}$ for which the $\beta$ side has no
counterpart at finite lattice spacing.  `B-axis` reproduces `A-axis` exactly, as
it must, and `B-chart` reproduces `A-chart`.  The architecture split is a
declared bookkeeping choice and it is measured rather than assumed.

---

## 7. The controls, all of the GW1 pin's own list

### 7.1 Wrong deformation kernels

§6.2's negative control: three declared broken variants, all failing closure.

### 7.2 Flat and curved targets

`A-axis` closes on the flat record **and** on the inhomogeneous diagonal record,
and fails on both cross-term records, one homogeneous and one inhomogeneous
(G12).  Curvature in the sense of site-dependence is **not** what breaks the
closure; a cross term is.

### 7.3 Randomised update order

Exchanging the two normal labels sends the residual field to its exact negative
at every site: **360** pairs tested, **0** antisymmetry violations (G13).  The
`omega-asym` mutant, which replaces the bracket covector by a non-antisymmetric
difference, dies here.

### 7.4 Chart changes — and the RUNBOOK §14 symmetry self-test

The declared chart group is the $\lvert X\rvert$ chart translations and the $d!$
direction relabellings, acting on sites, on the record's link counts, on the
lapse profiles and on every tensor index.  Equivariance of the residual field is
measured component by component on freshly rebuilt records: **4860**
comparisons, **0** violations (G14).  The `chart-shift` mutant, which moves the
record but not the field index, dies here.

Per the RUNBOOK §14 addendum the self-test evaluates fresh, and the cache path is itself
gated: **283 133** cache hits, **1377** misses, **486** fresh bypasses (G15).
The `cache-lax` mutant, which routes the fresh path back through the memo, dies
there.  A zero-hit cache gate would have been vacuous; this one measures that
the cache is exercised and that the self-test does not read it.

### 7.5 The density-weight convention — and it moves the verdict

GW1 §5 item 5 warns that the extracted object is inverse metric data "or inverse
metric density data, according to the normalization convention".  Measured, over
the same 132 pairs, for `A-axis`:

| record | nonzero pairs at $w = 0$ | nonzero pairs at $w = 1$ |
|---|---|---|
| `G-FLAT` | 0 | 0 |
| `G-DIAG2` | 0 | 96 |
| `G-ANISO` | 0 | 96 |
| `G-ANISO2` | 0 | 96 |
| `G-CURVED` | 0 | 92 |
| `G-OFFDIAG` | 96 | 96 |
| `G-OFFDIAG2` | 96 | 96 |
| `G-OFFNEG` | 96 | 96 |
| `G-CURVOFF` | 96 | 96 |

> **The closure verdict is convention-relative.**  At the declared weight
> $w = 0$ the diagonal sector closes; at $w = 1$ it closes only at `G-FLAT`,
> where $\det q = 1$.  Four cells move (G17).  Every closure statement in this
> note is at $w = 0$, and the sector on which it holds is the sector on which
> the record's own determinant is trivial or the convention is the inverse
> metric proper.  This is not a caveat added afterwards: it is the declared
> convention's measured cost.

### 7.6 Matter-free versus matter-conditioned, and the tangential split

On the matter-free carrier the $HH$ commutator is the identity for every rule
and record, so the deformation-closure test has **no content without matter
records** (G16).  This is recorded rather than must-pass: it is forced by the
additivity of the front advance (disclosure X04).

The D-TOT flip-test measures what the other realisation costs.  Over **1188**
(record, lapse pair) cells, $\beta$ is nonzero at **864**; the site map
$x\mapsto x+\beta(x)$ is a bijection at **332** cells and undefined at **856**;
and the cells with $\beta$ nonzero **and** a defined site map number **8**
(G18).

> **Named obstruction for D-TOT.**  Of the brackets this arena realises, almost
> none admits a site-permutation realisation of $D_a[\beta]$: $\beta$ is
> generically non-integral, and where it is integral it is supported at too few
> sites to be a bijection.  The additive address-register realisation is
> therefore not a convenience — it is the only one of the two declared
> realisations on which the residual can be posed at all at this arena.  The
> price is stated in §13.

---

## 8. The three-normal detector

The normal-tangential group commutator $\mathsf C(H_a[N], D_a[B])$ is measured
**trivial** at 108 of 108 tested cells (G19), so the corrected switch degenerates
to $\mathsf W = H_a[\mathcal L_BN]$ on this substrate.  This construction
therefore does **not** reproduce v4 paper 13 Proposition 3.6's nonzero
$\mathsf W$; it is forced by the address register's passivity under the front
(disclosure X04) and is recorded, not claimed.

$\mathsf{SW}_{HHH,a}$ is nevertheless nontrivial, and that is the section's
result.  Over **108** tested (rule, record, lapse-triple) cells — three rules,
nine records, four declared triples — evaluated by **literal composition of the
three corrected switches**:

- the cyclic Jacobi **lapse** sum
  $\mathcal L_{B_{ML}}N + \mathcal L_{B_{LN}}M + \mathcal L_{B_{NM}}L$ vanishes
  at **all 108** cells;
- $\mathsf{SW}_{HHH,a}$ is **not** the identity at **81** of them — 27 of 36 for
  each of `A-insert`, `A-axis` and `A-chart` — with the obstruction carried
  entirely by the register displacement, e.g.
  $\max\lvert\text{reg}\rvert = 2$ at `A-insert | G-ANISO | (9,10,0)` and
  $1/64$ at `A-insert | G-ANISO2 | (0,3,9)` (G20).

> **Pair closure does not buy $HHH$ closure.**  The metric-inserted rule closes
> the $HH$ pair residual exactly at every record and every pair (§6.2) and its
> three-normal detector is nonzero at 27 of its 36 tested triples.  That is the
> finite measurement of v4 paper 12's own reason for building the corrected
> switch: "the smallest switch object that can see the $HHH$ Jacobi obstruction
> is not the corrected $HH$ pair residual itself."  The obstruction survives
> insertion.

---

## 9. The general-`d` extension

v4 paper 7's definitions are general-$d$, so the unit runs at $d = 3$:
$\lvert X\rvert = 27$ sites, 6 links, 3 records, 7 lapses, 42 ordered pairs.
Cells give nonzero pairs of 42.

| rule | `G3-FLAT` $(1,1,1,2,2,2)$ | `G3-ANISO` $(1,4,9,5,10,13)$ | `G3-OFF` $(2,2,2,6,4,4)$ |
|---|---|---|---|
| `A-chart` | CLOSES | 30 | 30 |
| `A-axis` | **CLOSES** | **CLOSES** | 18 |
| `A-linkframe` | 30 | 30 | 30 |
| `A-insert` | CLOSES | CLOSES | CLOSES |

The same separation, at the same scope tags (G21): the inserted rule closes
everywhere, the link-local record-native rule closes on the diagonal records and
fails on the cross-term record.

---

## 10. The declared secondary: the stitching geometry

The pin asks, by measurement and not by analogy, whether $R_{HH}$ can be
expressed in the data of the measured transport/holonomy layer — NT's bigon
group and GEN's defect law $D = (\Sigma V^{\mathsf T}\Sigma V)\otimes I_9$.

### 10.1 The HA residual as a holonomy, in NT's and GEN's own coordinate

At the declared symmetric configuration (a swap-invariant base front and two
swap-invariant lapses, so that the chart involution preserves the front sector —
measured, not assumed), the based closed-loop product of the link transports is
computed on the reduced carrier of **625** total records.  The HA residual
generates a group of order **5**, abelian, with element orders $\{1,5\}$: an
elementary abelian group of exponent $p$.

### 10.2 GEN's own relations, tested — with GEN's own defect as the control

GEN's defect law is rebuilt independently from the published prose (§2.3's
$\psi$, Householder and declared transposition; its §8.1's reduction of
$\Sigma V^{\mathsf T}\Sigma V$ to $\Sigma Q^{\mathsf T}\Sigma Q$ for an
exchange-invariant $\psi$), and reproduces the committed defect permutation
$[0,2,1,6,4,5,3,7,8]$ entry by entry, its order **2**, its **45** fixed
configurations of 81, the whole **40 320**-member family, its **96**
identity-defect members and **40 224** geometry-bearing ones, its order and
fixed-configuration spectra, and **0** members where the dihedral relation
fails.  Those are anchors A09–A16.

| relation | GEN's own defect (positive control) | the HA residual |
|---|---|---|
| $\Sigma D\Sigma = D^{-1}$ | **holds** | **fails** at the declared loop |
| order | 2 | 5 |
| in GEN's measured order spectrum $\{1,2,3,4,5,6,7,15\}$ for the defect, holonomy $\{1,4,6,8,10,12,14,30\}$ | yes | **no** (order 5) |
| Klein four-group (NT's group) | — | **no** |

The dihedral relation is measured over 24 further declared lapse pairs and holds
at **17** of them — so it is a coordinate coincidence at this arena, not a
structural property of $R_{HH}$.

### 10.3 The coordinate table

| coordinate | NT / GEN | HA |
|---|---|---|
| carrier | 36 configurations $(q_A,q_B,p_A,p_B)$ / 81 $(s_A,s_B,p_A,p_B)$ | 625 total records = front sector $\times$ address register |
| family | 6 settings $\times$ 2 frames / 6 settings | 11 drag rules $\times$ 9 geometry records |
| law | the declared legs $U_{\text{prep}}, U_A(a), U_B(b)$ | $H_a[N] : (n,m)\mapsto(n+N,\,m+w[N,n])$ at a lapse profile |
| state | $p(0) = \delta_{j_0}$ | the base total record $(n_{\text{sym}}, 0)$ |
| arena | (frame, read time) nodes, co-reference identifications | (record site, front sector), normal and tangential comparison maps |
| structure group | Klein four $\{1,W,X,WX\}$ / dihedral of order $2n$ | elementary abelian of exponent 5, order 5 here |
| defect construction | $D = P_WU_{\text{prep}}^{-1}P_WU_{\text{prep}} = (\Sigma V^{\mathsf T}\Sigma V)\otimes I_9$ | $R_{HH} = \mathsf C(H[N],H[M])\,D[-\beta_a(g;N,M)]$ |

### 10.4 Verdict

> **`HA-BRIDGE-NOT-POSABLE`.  Named obstruction: NO COMMITTED CARRIER
> MORPHISM.**  The stitching geometry's defect law is a statement about a fixed
> 81-element (or 36-element) process carrier factorised as a system pair times a
> pointer pair, with $\Sigma$ the pair-label exchange and the defect the failure
> of a declared completion to intertwine that exchange.  $R_{HH}$ lives on total
> matter-geometry records with no such factorisation, no exchange-typed
> completion, and no committed map to that carrier.  The measured consequences:
> the HA holonomy group has order 5 and exponent 5, which is not in GEN's
> measured order spectrum; and GEN's defining relation
> $\Sigma D\Sigma = D^{-1}$ is measured **not** to hold for $R_{HH}$ at the
> declared loop, while the same relation is measured **to** hold for GEN's own
> defect.  The `bridge-lax` mutant, which drops the coordinate test from the
> posability predicate, dies at G22.

The stitching geometry therefore does **not** supply the interface object GW1
lacked.  What GW1 lacked was a lapse-profiled record-native comparison family;
NT and GEN measure path-dependence of lawful data on a co-reference base with no
lapse argument, no front, and no geometry record.  The shape is shared — both
are holonomies of a bigon corrected by a third transport — and shape-sharing is
analogy, which the pin excludes.

---

## 11. The receipt

`v13/code/ha_successor_exact.py` emits `ha_successor_output.txt` and
`ha_successor_receipt.json`.  Interpreter `/opt/homebrew/bin/python3.13`
(3.13.2).  Exact arithmetic throughout: `fractions.Fraction`, integers, and
exact $\mathbb F_p$; no float or complex literal appears in the source, the
scanner is validated by a synthetic injection it must flag, and every value of
every residual field is measured to be an exact type (G24).

| item | value |
|---|---|
| anchors (exit-1-only) | **16**, all reproduced |
| gates | **26** (21 must-pass, 5 recorded), **0** must-pass failures |
| disclosures | **4** (X01–X04) |
| mutants | **25**, **0** survivors, `never_falsified` **empty** |
| runs | two full runs, byte-identical output and receipt |

**Hash pins.**
`v13/code/nt_transport_receipt.json` sha256
`d256891b479a8636fe88df5e9b0f553998140f1553fdfc167662220b44eeb03e`;
`v13/code/gen_generality_receipt.json` sha256
`e0b2f444f6a9b82861024f7733c7230583742dfd477d9ed6037a241e7b48d292`.
Instrument sha256 `19dad19b01ee09f333c9780769dd3b887cc7699b2132813b7d24b03dcb83d772`.

**The anchor set.**  A01–A04 recompute the terminal GW1 census's own repository
facts: the `.py` counts of its ten frozen runnable trees — 353, 273, 137, 101,
84, 9, 8, 7, 3 and 1 — the 3 at the repository root, the **12** files in `code/`
carrying the token `lapse`, and **0** in every other frozen tree.  A05–A08 pin
the NT and GEN receipt hashes and recompute NT's **34 024** reduced paths and its
per-setting holonomy orders $(1,1,1,1,4,4)$.  A09–A16 rebuild GEN's completion
census independently from the paper's prose (§10.2).

**Disclosure X01.**  `v12/code/` now carries 7 `.py` against the GW1 census's 5,
and `v13/code/` is the live tree of four concurrent cycles.  Both are declared
LIVE and excluded from A01 **by declaration, not by outcome**; their current
counts are printed.

**The mutant table.**  Every declared mutant exits 1 with its named kills:
`anchor-gen-defect` → A12; `anchor-gen-family` → A09; `anchor-gw1-lapse` → A03;
`anchor-gw1-trees` → A01; `anchor-nt-paths` → A07; `anchor-nt-sha` → A05;
`beta-flat` → G06, G08, G12, G21; `bridge-lax` → G22; `cache-lax` → G15;
`chart-shift` → G14; `closure-lax` → G07, G08, G08B, G12, G21;
`control-lax` → G07; `exempt-lax` → G23; `factor-lax` → G10, G11;
`float-lax` → G24; `freeze-lax` → G01; `invert-lax` → G04;
`omega-asym` → G05, G13; `order-swap` → G05; `posdef-lax` → G02;
`prime-single` → G10B; `rank-lax` → G03, G07, G08, G08B, G10, G12;
`readout-local` → G07, G09, G12, G21; `sign-flip` → G05, G10, G11;
`transport-off` → G04, G05, G19.

**Mutant discipline.**  Every mutation is a mutation of an instrument helper; no
gate predicate and no gate-registering function references mutant identity —
neither `MUTANT`, nor a per-mutant switch, nor a mutant-name literal — and the
AST guard that measures this is validated by a synthetic injection it must flag
(G23).  The single exception is disclosed: one run-mode boolean, identical for
every mutant, decides only whether the delivery artifacts are written; no gate
reads it (X03).  `--falsification-selftest` reproduces the whole run and the
whole mutant harness without writing artifacts.

---

## 12. Deviations and declared choices

Everything here is a choice the directive underdetermined, declared rather than
made silently.

1. **`v6_task2b` is not the metric readout** (§1).  The successor directive
   names it; GW1's own §2 grades its fit as reaching outside order and count
   data, and using it would fail GW1 §1.2.  The readout is instead the
   record-internal interval-cardinality relation of §3.2.  This is a deviation
   from the directive's letter in service of the directive's own no-smuggling
   predicate, and it is the largest single deviation in the unit.
2. **`K_i` and `ε` are eliminated, not built** (§1).  The residual is posed in v4
   paper 7's multiplicative form, which needs neither.  GW1 §5 items 2 and 4
   remain open for the divided form $(\Omega-I)/\epsilon^2$; this unit does not
   discharge them, it declines to need them.
3. **The direction-labelled record adjacency is declared, not derived.**  The
   site set $(\mathbb Z_3)^d$ with $d$ direction-labelled periodic links is
   declared data.  Deriving a direction labelling from a record order is exactly
   the open problem GW1 §2 records as unsolved (the spectral frame is
   unoriented).  The mitigation is measurement: the residual field is gated
   equivariant under the whole declared chart group (§7.4), so the verdict is a
   chart-invariant, but the arena's existence is a declaration.
4. **The address-register realisation of the tangential sector.**  $D_a[v]$ acts
   additively on a matter-record address register.  Consequences, all measured
   or disclosed: the tangential maps form an **abelian** group, so the declared
   finite Lie bracket $[v,w]_a$ is zero on that class and $R_{DD}$ closure is
   vacuous; $H_a[N]$ and $D_a[B]$ commute identically, so the tangential-normal
   residual is not the identity and the corrected switch degenerates (§8).  **No diffeomorphism
   action on geometry records is claimed, and $R_{DD}$ and $R_{DH}$ are outside
   the tested scope.**  The alternative realisation D-TOT is measured and found
   almost never defined at this arena (§7.6).
5. **The density weight $w = 0$.**  Declared, flip-tested, and it moves the
   verdict at four cells (§7.5).  Every closure claim is at $w = 0$.
6. **The declared lapse family** is 12 profiles, not all profiles; the rank it
   realises is measured full, which is what the identifiability argument needs,
   but no all-lapse claim is made.
7. **The geometry sector is frozen under $H_a[N]$.**  The interval-cardinality
   record $s$ is a configuration variable that $H_a[N]$ does not move; only the
   front does.  This is v4 paper 7 Hypothesis 5.1 item 2's frozen reduction, and
   it is why $\beta_a(g;N,M)$ is well defined sectorwise as Definition 2.3
   requires.  **No geometry-update law is constructed**, so nothing here bears
   on v4 paper 7 Theorem 6.1.
8. **The operator layer's carrier is reduced** to the front sector and the
   address register at one declared detector site, swept over all 9 sites at
   $p = 5$ and at the origin for $p \in \{7,13\}$.  Two comparators tie it to
   the exact rational field (G10, G11) and the multi-prime gate bounds the
   modular risk (G10B), with 33 undefined reductions printed.
9. **G16 and G19 are analytically forced** and are recorded rather than
   must-pass (X04).
10. **The G08 sector-law grid excludes the frozen-front variant by
    declaration**, and that variant is measured separately at G08B, where it
    carries the unit's sharpest result.
11. **Three anchors could not be taken as the census recorded them.**
    `v12/code/` and `v13/code/` have moved since 2026-07-28; both are declared
    LIVE and excluded, with their current counts printed (X01).

---

## 13. Non-claims

- No Einstein-dynamics claim in any form: no field equation, no backreaction, no
  stress response, no constraint preservation, no continuum limit, no refinement
  sequence.
- $\Delta^B$, $\Omega_{\text{hypersurface}}$ and $R^\rho{}_{\sigma\mu\nu}$ remain
  three distinct objects; no two are identified.
- **No metric is recovered.**  The metric candidate is read from the geometry
  record by a declared readout and the closure test measures whether a drag
  rule's structure function equals it.  Nothing is reconstructed from the
  closure law; §6.3 measures the opposite.
- No claim that the closure that holds on the diagonal sector is a derivation of
  geometry: §6.5 measures that it holds precisely where the link-local weight
  coincides with the metric by arithmetic.
- No claim about general $d$, general $L$, general records, general lapses,
  general weights, or general primes.  The verdict is at the declared arena.
- No diffeomorphism-group content: the tangential sector is abelian by
  declaration, $R_{DD}$ and $R_{DH}$ are untested, and v4 paper 7 Definition 2.5's
  `V4P7-FIN-ALG-CLOSE` is **not** claimed — only its $HH$ component is measured,
  at one regulator, without any limit.
- No claim that v4 paper 13 Proposition 3.6's nonzero detector is reproduced; it
  is measured **not** to be, on this substrate, for a disclosed structural
  reason.
- No claim about the stitching geometry beyond the measured coordinate mismatch
  of §10; NT and GEN are not criticised, they are measured to be a different
  arena.
- The negative in §10.4 is scoped to the committed coordinates enumerated there;
  no nonexistence theorem about bridges is claimed.
- Nothing here is citable before an external hostile round confers TERMINAL.
