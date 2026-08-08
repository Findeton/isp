# HA — THE RECORD-NATIVE `H_a[N]`, CONSTRUCTED; AND THE DEFORMATION-CLOSURE TEST, RUN

**Status:** GREEN-UNREVIEWED-REPAIRED, STRICT, 2026-08-08.
**Pin:** `v13/note-ha-successor-pin.md` (frozen; immutable base commit `024fcd7`).
**Binding:** `v13/note-gw1-metric-from-closure.md` — TERMINAL at v13 LOG #5 —
and in particular its §7.1 successor directive, quoted verbatim in §1;
`v13/note-gw1-metric-from-closure-pin.md`; v4 paper 7 Definitions 1.1–1.4 and
2.1–2.5; v4 paper 12 Definition 11.6M; `v13/relativistic-isp-v13-paper0-gravity.md`
(the charter, `[DRAFT]`).  Declared secondary:
`v13/paper-nt-nomological-transport.md` and `v13/paper-gen-generality-check.md`,
both receipts hash-pinned in §11.
**Verdict:** **`HA-RUNNABLE`.**  The declared secondary enters **no**
`HA-BRIDGE-…` outcome: §10 is a coordinate audit, the morphism question is
registered OPEN in §14, and the verdict string is derived inside a gate (G25)
with a falsifier that must die there.
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

**The kill fires — at its second disjunct, and measured rather than asserted.**
That is this unit's contribution: GW1's conditional — "the corpus can either
obtain nontrivial closure by supplying geometry, or remain record-native and
fail to produce the required closure" — becomes a measurement on a constructed
substrate, with the sector where each alternative holds named and counted (§6).
The disjunct that fires is *the same record law permits inequivalent recovered
tensors*, counted at §6.3; the first disjunct cannot be fired by GW1's original
route here, because this formulation eliminates the decoder that would extract a
second tensor to compare (§1, §12.2).

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
The reach outside order-and-count data is broader than GW1's own §2 recorded,
and it is enumerated here because the substitution rests on it: the sample
region is selected by embedding coordinates (`:40`), the fit runs against
embedding separations `dx = P[b] − P[a]` (`:48`, `:63–65`), the sample is
filtered by the **true** interval (`:49–50`), and the single scale `K` is
calibrated against the true interval (`:58`).  Exactly one ingredient,
`c = C[a,b]` (`:52`), is order-and-count data.  That fails GW1 §1.1
**condition 5** ("`q^{ij}_order` … from order and count data on the same
substrate") and GW1 §1.2's **second** bullet, which bans held-out embedding
coordinates; using it would insert held-out embedding data into `β`, i.e. into
the residual under test.

Two further reasons the directive's letter is unexecutable, independent of
smuggling.  **Type.** `v6_task2b` returns one constant `d × d` least-squares
matrix fitted over a whole sprinkling, while `β_a^i = I_a(g)^{ij}(x) ω_j(x)`
needs an exact, site-dependent rational field on a `3^d` lattice; there is no
route from the former to the latter.  **Validation.** That script's own closing
note (`:116–119`) lists the curved test as REMAINING, so the fit is validated on
flat space only.

Instead the metric candidate is read from the finite geometry record itself, by
a **declared** readout — interval cardinality as squared separation (§3.2) —
which is a legitimate instantiation of v4 paper 7 Definition 1.4's undetermined
"metric candidate", chosen because it inverts exactly.  Definition 1.4 supplies
no relation, and the only committed corpus implementation of cardinality →
metric uses the Myrheim–Meyer exponent, `τ̂² = (card/K)^{2/d}`, not a
cardinality-linear relation; the two agree only at spacetime `d = 2`, while this
unit applies its readout at spatial `d = 2` and `d = 3`.  The readout is
therefore this unit's declared choice and is not attributed to the corpus.

The co-requisites are discharged or declared as follows.

- `∇_j` on the slice: the declared forward difference on the record adjacency.
- A transported second step: built in, and measured **necessary** (§6.4).
- `K_i`, its inverse, and `ε`: **eliminated, not supplied.**  The residual is
  posed in v4 paper 7 Definition 2.3's exact multiplicative form, which needs
  no division by $\epsilon^2$ and no decoder inverse — the tangential
  correction is included rather than fitted.  GW1 §5 items 2 and 4 are
  therefore not open here; they are not needed by this formulation, which is
  itself a declared narrowing of GW1's original STEP 4.  **The price is stated
  once:** with no decoder there is no independently extracted tensor, so GW1's
  `q_comp`/`q_order` comparison is eliminated along with `K_i`, and the kill
  condition's first disjunct cannot be fired by GW1's original route.  What
  fires instead is its second disjunct, measured (§6.3).
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

**One of GW1 §1.2's four exclusions is vacuous here, and it is the fourth.**
That clause bans "algebraic data equivalent to the target metric"; at this arena
the site's link counts and the components of $q$ determine each other by an
invertible linear map (§3.2, G28), so *every* record-native rule has access to
data equivalent to the metric by construction and the clause cannot discriminate.
The first three exclusions are passed cleanly and are what §2's claim rests on.
What this unit measures is therefore not *what data a rule can see* but **which
function of the counts it computes** (§6.5).

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
The metric candidate is read from that record by the **declared** readout of §1
— interval cardinality as squared separation — solved exactly:

$$q_{ij}(x)\,e_\ell^i e_\ell^j \;=\; n_\ell(x)\quad\text{for every }\ell\in\mathcal L,
\qquad I_a(g)^{ij}(x) \;:=\; (q^{-1})^{ij}(x)\cdot(\det q)^{w}(x).$$

At $d = 2$ the three links determine the three components of $q$ exactly; at
$d = 3$ the six links determine the six.  A record is **admissible** when $q$ is
nonsingular and positive definite at every site, by the exact Sylvester
criterion, and $q^{-1}$ exists at every site.

> **The readout is an invertible linear re-encoding: in count coordinates, the
> record IS the metric.**  The map from the site's link counts to the components
> of $q$ is linear with an exact nonzero determinant (measured: $2$ at $d=2$),
> and $q$ reproduces every declared link count at every site of every record
> (81 of 81; G28).  At $d = 2$ this is $q_{11} = n_{e_1}$, $q_{22} = n_{e_2}$,
> $q_{12} = (n_{e_1+e_2} - n_{e_1} - n_{e_2})/2$; three links, three components.
> So "the geometry record" and "the metric candidate" are **one datum in two
> coordinate systems**, and reading one off the other is a change of
> coordinates, not a reconstruction.  Everything this unit measures about
> insertion and no-smuggling is therefore a statement about **which function of
> the counts a drag rule computes** — not about what data it could in principle
> see (§2, disclosure X05).  Nothing below weakens on that account, and §6.3
> says so at the point where it matters.

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

The residual is computed by routes that share no code, and every cell of the
headline table is computed by **both** (13 068 comparisons, 0 disagreements,
G05).

- **The exact rational layer.**  Every object is an exact `Fraction`-valued
  field; the residual is the register displacement of the literal five-map
  composition.  No modulus, no truncation, no tolerance.
- **The closed form**, built from the drag rule and the record readout without
  touching the composition:
  $\rho^i(x) = \bigl(\Lambda^{ij}(x)-I^{ij}(x)\bigr)\omega_j(x)$ for
  architecture A, and $\sum_\ell\lambda_\ell e_\ell^i\omega_\ell - \beta^i$ for
  architecture B.  One row is not of that form: the frozen-front variant
  `A-notransport` is evaluated in the closed route as $-\beta$ directly, which
  is what its frozen front makes it, and the literal composition confirms that
  independently at every one of its cells.
- **What the two routes do and do not share.**  They share `beta()`: a
  common-mode error in $\beta$ would be invisible to G05, and is policed
  instead by the positive control (G06), the sector law (G08), the flat/curved
  separation (G12) and the $d=3$ extension (G21), each of which a declared
  falsifier that perturbs $\beta$ must and does kill.
- **The finite operator layer.**  On a declared finite total-configuration
  carrier $C_{red} = \mathcal F\times\mathcal A$ — $\mathcal F$ the front sector
  $n_0 + \operatorname{span}_{\mathbb F_p}\{N,M\}$, $\mathcal A = (\mathbb F_p)^d$
  the address register at a declared detector site — every comparison map is an
  explicit permutation and $R_{HH}$ is formed as a genuine operator product.
  This is Definition 2.3 as an operator on $V_a^{tot}$, with Definition 2.4's
  norm on the declared test class of indicator effects:
  $\lVert R\rVert$ = configurations moved, over carrier size.  **That norm is a
  boolean in disguise on this carrier** and is read as one: a nonzero
  translation of $\mathcal F\times(\mathbb F_p)^d$ moves *every* configuration,
  so $\lVert R\rVert \in \{0, 1\}$ and each row of the printed table carries one
  bit — whether the residual reduces to zero at that prime — not a magnitude.

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

$H^{-1}H = HH^{-1} = \mathrm{id}$ is measured on **792** (rule, record, lapse,
register) instances — 396 at each of the two declared address registers,
$m \equiv 0$ and $m \equiv 1$ — with **0** failures at each (G04).  The declared
non-injective falsifier, a variant that collapses the address register, is run
at both registers too, and the report is two-sided: it is **rejected** at
$m \equiv 1$, and at $m \equiv 0$ it is **not** rejected and cannot be, because
collapsing an already-zero register is the identity there and no predicate could
separate them.  The gate's teeth are therefore at $m \equiv 1$, the H family is
measured invertible at both, and the coordinate at which each side is evaluated
is stated rather than left to be inferred.  The `invert-lax` mutant, which
blinds the predicate, dies there; so does `transport-off`, because a drag read
at the wrong front is no longer inverted by the closed form.

The literal five-map composition and the independently built closed form agree
field by field at **13 068** comparisons — **every** (rule, record, ordered
lapse pair) cell of the headline table — with **0** disagreements (G05).  The
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
> `G-CURVED`.  **Read this with §6.5:** on a diagonal readout
> $\Lambda_{\text{axis}} = \operatorname{diag}(1/q_{jj}) = q^{-1}$ *identically*,
> so what the diagonal sector exhibits is a rule that coincides with the metric
> by arithmetic rather than by design.  The finding is the sector boundary and
> its mechanism, not a derivation of geometry.

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
  admissible record and every tested pair — 9 of 9 records — **by both routes**.
  The closed-form clause is forced by X02's identity; the literal five-map clause
  is not, and it is the measurement: 0 nonzero cells of the 1188 literal
  evaluations of that rule.  `beta-flat` and `transport-off` each kill it.
- **Negative control with teeth (G07):** every declared broken variant fails
  closure — `A-insert-x` on 4 records (exactly the four with a nonzero cross
  term, since flipping the sign of a zero is a no-op), `A-insert-2x` on 9,
  `A-notransport` on 9.  `closure-lax`, `control-lax` and `readout-local` each
  die here.

### 6.3 The sector law: closure forces the count-matrix inverse — a joint, not link-local, function of the record

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
spanning covector family if and only if $\Lambda = I$.  The same identity forces
the closed-form clause of the positive control G06 and the `A-insert` clauses of
G12 and G21; in each case the **measurement** is the literal five-map route,
which the identity does not force, and G06 carries that route explicitly.  The
forcing is conditional on §4.2's rank, which a declared falsifier genuinely
breaks, so the pair is not vacuous.  It is recorded as a disclosure, not claimed
as an independent discovery.  The measured content is the rank that makes the
statement bite, the cell census above, the residual magnitudes of §6.1, and
§6.5's theorem.

**Which disjunct of the kill condition fires — measured.**  GW1's kill has two
disjuncts: *the metric must already be inserted into $J[N]$*, **or** *the same
record law permits inequivalent recovered tensors*.  The **second** is the one
that fires here, and it fires cleanly.  Under GW1's own STEP 4 reading the
commutator's displacement is $\Lambda^{ij}\omega_j$, so the tensor a rule
"recovers" **is its own weight field** $\Lambda$.  On one record — `G-OFFDIAG` —
the complete declared family realises **7 pairwise-distinct recovered tensors**
across its 8 architecture-A rules (`A-insert` and `A-notransport` carry the same
weight and differ only in transport), and **9 pairwise-distinct residual laws**
across all 11 declared rules (`B-axis` reproduces `A-axis` and `B-chart`
reproduces `A-chart`, exactly as the architecture split predicts).  One record,
many inequivalent recovered tensors: that is the second disjunct, measured, over
a family whose completeness is itself gated (G26, G27).

**And "insertion" means something specific here.**  Nothing external is
inserted: by §3.2 the record and the metric are one datum in two coordinate
systems, so what closure forces is not the arrival of foreign data but that the
drag weight be a **particular joint function of the record** — the count-matrix
inverse — rather than any link-local function of it (§6.5).  GW1's kill was
written for substrates where the metric arrived from outside; the boundary this
unit actually locates is between **link-local and joint functions of the
record**, which is a different and weaker boundary, and it is the honest one.

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

### 6.5 No link-local record-native weight closes — a theorem

A weight is **link-local** when each declared link contributes a weight that is
a function of **its own** interval count alone:

$$\Lambda(x) \;=\; \sum_{\ell\in\mathcal L} f_\ell\bigl(n_\ell(x)\bigr)\,
e_\ell e_\ell^{\mathsf T},\qquad\text{so at } d = 2:\quad
\Lambda^{11} = f_1(n_{e_1}) + f_3(n_{e_1+e_2}),\quad
\Lambda^{22} = f_2(n_{e_2}) + f_3(n_{e_1+e_2}),\quad
\Lambda^{12} = f_3(n_{e_1+e_2}).$$

> **Theorem.**  No link-local weight closes on the declared record family.
>
> *Proof.*  Closure at a site forces $\Lambda = I_a(g)$ there (§6.3, with §4.2's
> full rank).  For a link-local weight the cross component
> $\Lambda^{12} = f_3(n_{e_1+e_2})$ is a function of the diagonal link's own
> count alone, so closure demands $f_3(n_{e_1+e_2}) = I^{12}$ at **every**
> admissible record.  `G-DIAG2` $(2,2,4)$ and `G-OFFNEG` $(3,5,4)$ are both
> admissible and both carry $n_{e_1+e_2}(0,0) = 4$, while
> $I^{12} = -q_{12}/\det q$ is $0$ at the first and $2/11$ at the second.  So
> $f_3(4)$ would have to take two values.  $\blacksquare$

The witness is gated (G09), and the weaker statement is kept separate from the
stronger one: the pair `G-CURVOFF`/`G-DIAG2`, which share $n_{e_1}(0,0) = 2$
while demanding $I^{11} = 2/3$ and $1/2$, refutes only the diagonal-restricted
subfamily $\Lambda^{jj} = f(n_{e_j})$ — that is, exactly `A-axis` — and is
reported as such.  Neither witness is an accident of the declared nine: over the
declared count lattice ($1 \le n_{e_1}, n_{e_2} \le 6$, $1 \le n_{e_1+e_2} \le
12$, positive definite) there are **361** admissible count vectors, **5100**
pairs that share $n_{e_1+e_2}$ and demand different $I^{12}$, and **781** that
share $(n_{e_1}, n_{e_1+e_2})$ and demand different $I^{11}$ (G09B, recorded).

The mechanism: $I^{ij} = \operatorname{adj}(q)^{ij}/\det q$, and $\det q$ is a
**joint** function of every link count at the site.  A weight assembled from
per-link functions cannot see it.  Closure therefore requires a rule that
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
at every site, at **every** cell of the headline table: **13 068** (rule,
record, ordered pair) cells, **0** antisymmetry violations (G13).  The
`omega-asym` mutant, which replaces the bracket covector by a non-antisymmetric
difference, dies here.

### 7.4 Chart changes — and the RUNBOOK §14 symmetry self-test

The declared chart group is the $\lvert X\rvert = 9$ chart translations and the
$d! = 2$ direction relabellings — **18** elements — acting on sites, on the
record's link counts, on the lapse profiles and on every tensor index.
Equivariance of the residual field is measured over the **whole** group, at
every admissible record, every one of the 132 ordered lapse pairs and every
site, on freshly rebuilt records: **192 456** site comparisons (**384 912**
components), **0** violations (G14).  The `chart-shift` mutant, which moves the
record but not the field index, dies here.

**The memo, stated as it is coded.**  The self-test's comparands are served
*through* the weight memo — that is what gives G14 its teeth against a cache
that returns the wrong record's weight — and the memo's returns are themselves
measured: every weight the self-test uses is recomputed with the memo **bypassed**
and compared against what the memo returned, on the base record and on the
chart-transformed record alike.  Measured: **904 241** cache hits, **2349**
misses, **2916** fresh bypasses, **2916** fresh-versus-memo comparisons, **0**
disagreements (G15).  Two declared falsifiers die on this pair: `cache-lax`,
which routes the fresh path back through the memo, and `cache-alias`, which
serves a chart-transformed record the base record's cached weight — the latter
kills G14 and G15 together.  A zero-hit cache gate would have been vacuous; this
one measures that the cache is exercised **and** that what it returns is right.

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

**The displacement has an exact closed form, and it is measured.**  Writing
$A = \mathcal L_{B_{ML}}N$, $B = \mathcal L_{B_{LN}}M$,
$C = \mathcal L_{B_{NM}}L$ for the three transported lapse derivatives — whose
sum vanishes at all 108 cells, above — the degeneracy $\mathsf C(H,D) = I$ makes
$\mathsf{SW}_{HHH} = H_a[A]H_a[B]H_a[C]$, and its register displacement is

$$\Delta m^i \;=\; \Lambda^{ij}\bigl(B\,\partial_j C \;+\; A\,\partial_j B \;+\;
A\,\partial_j C\bigr),$$

compared against the literal composition of the three corrected switches at
**108 of 108** cells with **0** disagreements (G20B).  The `transport-off`
mutant, which reads the pre-advance front, moves the literal side only and dies
there.

> **What the nonzero $\mathsf{SW}_{HHH}$ is, and is not.**  The comparison is
> between a **corrected** pair object and an **uncorrected** triple: v4 paper 7
> defines no triple-level correction, so a nonzero $\mathsf{SW}_{HHH}$ is what
> the definitions predict rather than a failure of the inserted rule, and the
> section's content is the closed form above.  The metric-inserted rule closes
> the $HH$ pair residual exactly at every record and every pair (§6.2) and its
> three-normal object is nonzero at 27 of its 36 tested triples: that is the
> finite measurement of v4 paper 12's own reason for building the corrected
> switch — "the smallest switch object that can see the $HHH$ Jacobi obstruction
> is not the corrected $HH$ pair residual itself."

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

## 10. The declared secondary, as a coordinate audit

The pin asks, by measurement and not by analogy, whether $R_{HH}$ can be
expressed in the data of the measured transport/holonomy layer — NT's bigon
group and GEN's defect law $D = (\Sigma V^{\mathsf T}\Sigma V)\otimes I_9$.
**This section does not answer that question.**  It reports what is measured
about the two objects' coordinates, separates what is a property of $R_{HH}$
from what is a property of the declared arena, and hands the unanswered
question to a successor unit with its requirements stated (§14).  No posability
predicate is evaluated anywhere in the run, and no `HA-BRIDGE-…` outcome is
entered.

### 10.1 What $R_{HH}$ is on the reduced carrier, and what the prime decides

The instrument forms $R_{HH}$ as an explicit permutation product on the reduced
carrier and takes the group generated by that **one** permutation: it is the
**cyclic** group $\langle R_{HH}\rangle$, not a loop product of link transports
and not a multi-generator group.  Its structure is measured, not inferred:

> $R_{HH}$ acts on the reduced carrier as the **translation of the address
> register by $\rho(x^\ast) \bmod p$**, with the front sector returning to
> itself — verified configuration by configuration at every swept prime (G29).
> Hence $\langle R_{HH}\rangle \cong \mathbb Z/p$ whenever $\rho \not\equiv 0$.

Which makes the group's order an **arena coordinate**.  At the declared
symmetric configuration the exact rational residual at the detector site is
$\rho(0,0) = (1/6,\,1/6)$ — the same at every prime — while the group order
tracks the declared reduction prime exactly:

| $p$ | 5 | 7 | 11 | 13 | 17 | 19 | 23 |
|---|---|---|---|---|---|---|---|
| carrier $p^{k+d}$ | 625 | 2401 | 14 641 | 28 561 | 83 521 | 130 321 | 279 841 |
| $\rho \bmod p$ | $(1,1)$ | $(6,6)$ | $(2,2)$ | $(11,11)$ | $(3,3)$ | $(16,16)$ | $(4,4)$ |
| $\lvert\langle R_{HH}\rangle\rvert$ | **5** | **7** | **11** | **13** | **17** | **19** | **23** |

RUNBOOK §15 is explicit about what follows: a quantity not gated invariant
across the unit's admissible arenas may serve as an instrument reading and may
**never** enter as a conclusion.  The order of $\langle R_{HH}\rangle$ is such a
quantity (G30), and it is therefore excluded from every argument below.  The
`prime-single` mutant, which collapses the sweep to one prime, dies at that
gate; `factor-lax`, which perturbs the exact-to-$\mathbb F_p$ reduction, dies at
the translation-structure gate.

### 10.2 GEN's relations, and the spectrum a like-for-like comparison must use

GEN's defect law is rebuilt independently from the published prose (§2.3's
$\psi$, Householder and declared transposition; its §8.1's reduction of
$\Sigma V^{\mathsf T}\Sigma V$ to $\Sigma Q^{\mathsf T}\Sigma Q$ for an
exchange-invariant $\psi$), and reproduces the committed defect permutation
$[0,2,1,6,4,5,3,7,8]$ entry by entry, its order **2**, its **45** fixed
configurations of 81, the whole **40 320**-member family, its **96**
identity-defect members and **40 224** geometry-bearing ones, its order and
fixed-configuration spectra, and **0** members where the dihedral relation
fails.  Those are anchors A09–A17.

**Disclosure (X06): $\Sigma D\Sigma = D^{-1}$ is analytically forced.**  With
$D = \Sigma Q^{-1}\Sigma Q$ and $\Sigma^2 = \mathrm{id}$,
$\Sigma D\Sigma = (\Sigma Q^{-1}\Sigma Q)^{-1} = D^{-1}$ for **every**
completion $Q$ — which is why A16 counts 0 failures over all 40 320 members.
It is a disclosure, not a discriminating control, and the sentence "the same
relation is measured *to* hold for GEN's own defect" is withdrawn as a
measurement.  The relation is not vacuous for arbitrary permutations: a declared
3-cycle outside the sandwich form does **not** satisfy it, measured.

**Both GEN spectra are computed in this run, from the completion census, and
neither is typed.**  The defect order spectrum is
$\{1,2,3,4,5,6,7,15\}$ with multiplicities
$\{1{:}96,\,2{:}1440,\,3{:}4224,\,4{:}4608,\,5{:}4608,\,6{:}6912,\,7{:}9216,\,
15{:}9216\}$ (A14); the holonomy order spectrum $\{1,4,6,8,10,12,14,30\}$ is
derived from it as $2n$ with the flat class at 1 (A17).  The coordinate table
below pairs $R_{HH}$ with GEN's **defect** $D$, so the **defect** spectrum is the
like-for-like comparator; reading HA against one spectrum and GEN against the
other would be a class-versus-class verdict taken at two different coordinates,
which RUNBOOK §15's addendum forbids.  Against the correct comparator:

| relation | GEN's own defect | $R_{HH}$ |
|---|---|---|
| $\Sigma D\Sigma = D^{-1}$ | holds — **analytically forced** (X06) | **fails** at the declared loop |
| order | 2 | $p$, the declared prime (§10.1) |
| in GEN's computed **defect** order spectrum | yes | **yes at $p = 5$** (multiplicity 4608 of 40 320) and at $p = 7$ (9216); no at $p = 11,13,17,19,23$ |
| Klein four-group (NT's group) | — | no — $\langle R_{HH}\rangle$ is cyclic on one generator |

The third row is the decisive one, and it reads **yes** at the arena's own first
prime: order 5 lies in GEN's defect order spectrum, at 4608 of its 40 320
members.  It reads no at four of the seven swept primes.  A criterion whose
answer is a function of the reduction prime decides nothing about $R_{HH}$, and
that prime-dependence is itself gated (G31); the `bridge-spectrum` mutant, which
reads the holonomy spectrum where the defect spectrum belongs, dies there.

### 10.3 The $\Sigma$-relation census, decomposed

$\Sigma$ is the declared chart involution.  On the reduced carrier it exists
only where the front sector is swap-closed, so the relation
$\Sigma R\Sigma = R^{-1}$ is **posable** only there.  Three readings are
reported rather than one, over two declared sets of ordered lapse pairs, with
the vacuous cells separated out (G32, recorded):

| reading | first 24 pairs | all 132 pairs |
|---|---|---|
| single-site surrogate $\rho_1 + \rho_2 = 0$ | 17 | 114 |
| …of which $R_{HH}$ is the identity at the detector site | **17 of 17** | **114 of 114** |
| the same statement over the whole field, all 9 sites | 8 | 36 |
| carrier-level relation **posable** ($\Sigma$ exists) | 4 | 20 |
| carrier-level relation **holds** | 3 | 18 |
| …of which $R_{HH}$ is the identity | 3 of 3 | 18 of 18 |

The single-site surrogate is not the relation, and its 17 are not coincidences:
every one of them is a cell where $R_{HH}$ is the identity and the relation holds
trivially.  What the census establishes is sharper than any single count:
**the relation holds at no tested cell where $R_{HH}$ is nontrivial** — at the
single-site reading, at the whole-field reading, and at the carrier level alike.
Where it is genuinely posable it holds 3 of 4, and those 3 are exactly the
identity cells.

### 10.4 The coordinate table

Sizes are reported as sizes.  Equal cardinality is neither necessary nor
sufficient for a carrier morphism to exist, and no cardinality test is used as a
criterion anywhere.

| coordinate | NT / GEN | HA |
|---|---|---|
| carrier | 36 configurations $(q_A,q_B,p_A,p_B)$ / 81 $(s_A,s_B,p_A,p_B)$ | $p^{k+d}$ total records = front sector $\times$ address register (625 at $p = 5$) |
| family | 6 settings $\times$ 2 frames / 6 settings | 11 drag rules $\times$ 9 geometry records |
| law | the declared legs $U_{\text{prep}}, U_A(a), U_B(b)$ | $H_a[N] : (n,m)\mapsto(n+N,\,m+w[N,n])$ at a lapse profile |
| state | $p(0) = \delta_{j_0}$ | the base total record $(n_{\text{sym}}, 0)$ |
| arena | (frame, read time) nodes, co-reference identifications | (record site, front sector), normal and tangential comparison maps |
| structure group | Klein four $\{1,W,X,WX\}$ / dihedral of order $2n$ | cyclic on one generator, of order $p$ — the **declared prime** (§10.1) |
| defect construction | $D = P_WU_{\text{prep}}^{-1}P_WU_{\text{prep}} = (\Sigma V^{\mathsf T}\Sigma V)\otimes I_9$ | $R_{HH} = \mathsf C(H[N],H[M])\,D[-\beta_a(g;N,M)]$ |

### 10.5 What is measured, and what is not

> **Measured.**  The carriers are different sizes with different factorisations.
> $\langle R_{HH}\rangle$ is cyclic on one generator, while NT's group is Klein
> four and GEN's is dihedral, both genuinely multi-generator.  GEN's relation
> $\Sigma D\Sigma = D^{-1}$ fails for $R_{HH}$ at every tested cell where
> $R_{HH}$ is nontrivial (§10.3).  No map between the carriers is committed
> anywhere in the corpus.
>
> **Not measured.**  Any census of candidate carrier morphisms.  None was run.
> Nothing here is a nonexistence statement, and no obstruction theorem is
> claimed or implied.  The group's order and its membership in GEN's spectrum
> are arena coordinates (§10.1, §10.2) and are excluded from the argument.
>
> **Therefore no `HA-BRIDGE-…` outcome is entered.**  The morphism question is
> registered OPEN in §14, with the requirements a successor unit must meet.

What GW1 lacked was a lapse-profiled record-native comparison family; NT and GEN
measure path-dependence of lawful data on a co-reference base with no lapse
argument, no front, and no geometry record.  The shape is shared — both are
holonomies of a bigon corrected by a third transport — and shape-sharing is
analogy, which the pin excludes.  Whether that shared shape is carried by an
actual morphism is exactly the open question, and it is not settled here in
either direction.

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
| anchors (exit-1-only) | **17**, all reproduced |
| gates | **36** (27 must-pass, 9 recorded), **0** must-pass failures |
| disclosures | **6** (X01–X06) |
| mutants | **29**, **0** survivors, `never_falsified` **empty** |
| runs | two full runs, byte-identical output and receipt |

**Hash pins.**
`v13/code/nt_transport_receipt.json` sha256
`d256891b479a8636fe88df5e9b0f553998140f1553fdfc167662220b44eeb03e`;
`v13/code/gen_generality_receipt.json` sha256
`e0b2f444f6a9b82861024f7733c7230583742dfd477d9ed6037a241e7b48d292`.
Instrument sha256 `d44cb72f8ee9f2d212f4c9a881247411bc3245c9453e3745b5f4ff673ff6c439`.

**The anchor set.**  A01–A04 recompute the terminal GW1 census's own repository
facts: the `.py` counts of its ten frozen runnable trees — 353, 273, 137, 101,
84, 9, 8, 7, 3 and 1 — the 3 at the repository root, the **12** files in `code/`
carrying the token `lapse`, and **0** in every other frozen tree.  A05–A08 pin
the NT and GEN receipt hashes and recompute NT's **34 024** reduced paths and its
per-setting holonomy orders $(1,1,1,1,4,4)$.  A09–A17 rebuild GEN's completion
census independently from the paper's prose, including both order spectra
(§10.2).

**Disclosure X01.**  `v12/code/` and `v13/code/` are LIVE trees written by
concurrent cycles, and are excluded from A01 **by declaration, not by outcome**.
**No live count of either is taken**: a count of a tree this unit does not own is
not reproducible by construction, and the delivery's byte-identity would
otherwise depend on directories outside the unit.  The GW1 census's own
committed value for `v12/code/` is 5; `v13/code/` is not in that census at all.

**The mutant table.**  Every declared mutant exits 1 with its named kills:
`anchor-gen-defect` → A12; `anchor-gen-family` → A09; `anchor-gen-spectrum` →
A14; `anchor-gw1-lapse` → A03; `anchor-gw1-trees` → A01; `anchor-nt-paths` →
A07; `anchor-nt-sha` → A05; `beta-flat` → G06, G08, G12, G21;
`bridge-spectrum` → G31; `cache-alias` → G14, G15; `cache-lax` → G15;
`census-drop` → G26, G27; `chart-shift` → G14;
`closure-lax` → G07, G08, G08B, G12, G21; `control-lax` → G07;
`exempt-lax` → G23; `factor-lax` → G10, G11, G29; `float-lax` → G24;
`freeze-lax` → G01; `invert-lax` → G04; `omega-asym` → G05, G06, G13, G20B;
`order-swap` → G05, G06; `posdef-lax` → G02; `prime-single` → G10B, G30, G31;
`rank-lax` → G03, G07, G08, G08B, G10, G12, G27;
`readout-local` → G07, G09, G12, G21, G30, G31;
`sign-flip` → G05, G06, G10, G11, G29, G30;
`transport-off` → G04, G05, G06, G19, G20B; `verdict-flip` → G25.

**Mutant discipline.**  Every mutation is a mutation of an instrument helper; no
gate predicate and no gate-registering function references **run-mode** identity
— neither `MUTANT`, nor a per-mutant switch, nor a mutant-name literal, nor a
run-mode boolean (`DELIVERY_RUN` is mutant identity under another name), nor
`sys.argv` — and the AST guard that measures this is validated by four synthetic
injections, one per channel, every one of which it must flag (G23).  That the
run-mode boolean touches no gate is now **measured, not asserted**: the whole
measurement lives in a function that registers every gate and reads no run-mode
name, and the run-mode branch lives in a function that registers none (X03).
`--falsification-selftest` reproduces the whole run and the whole mutant harness
without writing artifacts.

**The verdict is derived inside a gate.**  G25 recomputes the verdict string
from the measured gate outcomes and the must-pass failure count and compares it,
string by string, against what the run printed; the `verdict-flip` falsifier,
which hand-types a verdict, dies there.  The closing prose is gated on the same
boolean, so a blocked run cannot print a construction claim.  **Census
completeness is gated too** (G26): the closure table, the sector-law grid, the
$d = 3$ grid and the count of residual fields computed each match exactly what
their declarations require — 99, 72, 12 and 13 068 — so a silently dropped rule
cannot shrink a census, and `census-drop` dies there.

---

## 12. Deviations and declared choices

Everything here is a choice the directive underdetermined, declared rather than
made silently.

1. **`v6_task2b` is not the metric readout** (§1).  The successor directive
   names it; its fit reaches outside order and count data at five enumerated
   sites, and using it would fail GW1 §1.1 condition 5 and §1.2's second bullet.
   It is also of the wrong type (one constant least-squares matrix against an
   exact site-dependent rational field) and is validated on flat space only, by
   its own closing note.  The readout is instead the declared interval-cardinality
   relation of §3.2 — a legitimate instantiation of v4 paper 7 Definition 1.4's
   undetermined "metric candidate", **chosen because it inverts exactly**, and
   not the corpus's relation: Definition 1.4 supplies no relation, and the only
   committed corpus implementation uses the exponent $2/d$, not a
   cardinality-linear law.  This is a deviation from the directive's letter in
   service of the directive's own no-smuggling predicate, and it is the largest
   single deviation in the unit.
2. **`K_i` and `ε` are eliminated, not built** (§1).  The residual is posed in v4
   paper 7's multiplicative form, which needs neither.  GW1 §5 items 2 and 4
   remain open for the divided form $(\Omega-I)/\epsilon^2$; this unit does not
   discharge them, it declines to need them.  The price is declared in §1:
   eliminating $K_i$ eliminates the `q_comp`/`q_order` comparison itself, so the
   kill condition's first disjunct cannot be fired by GW1's original route here.
3. **The direction-labelled record adjacency is declared, not derived.**  The
   site set $(\mathbb Z_3)^d$ with $d$ direction-labelled periodic links is
   declared data, and this touches GW1 §1.2's ban on planted frames.  Deriving a
   direction labelling from a record order is exactly the open problem GW1 §2
   records as unsolved (the spectral frame is unoriented).  The mitigation is
   measurement — the residual field is gated equivariant under the whole declared
   chart group (§7.4) — and the mitigation is **priced honestly**: that group is
   a subgroup of the automorphisms of the planted structure itself, so it
   certifies chart-invariance of the verdict and cannot certify the frame.  The
   sector split rests on $q_{12} = 0 \Leftrightarrow n_{e_1+e_2} = n_{e_1} +
   n_{e_2}$, a statement about counts **and** about which link is called the
   diagonal; the second half is declared, not record-derived.
4. **The address-register realisation of the tangential sector.**  $D_a[v]$ acts
   additively on a matter-record address register.  Consequences, all measured
   or disclosed: the tangential maps form an **abelian** group, so the declared
   finite Lie bracket $[v,w]_a$ is zero on that class and $R_{DD}$ closure is
   vacuous; $H_a[N]$ and $D_a[B]$ commute identically, so the tangential-normal
   residual is not the identity and the corrected switch degenerates (§8).  **No diffeomorphism
   action on geometry records is claimed, and $R_{DD}$ and $R_{DH}$ are outside
   the tested scope.**  This is a **realisation choice**, not a derived fact, and
   its only tested alternative — D-TOT — is measured almost nowhere defined at
   this arena (§7.6), so GW1's diffeomorphism content is untouched by this unit
   in either direction.
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
   must-pass (X04).  So are the closed-form clause of G06 and the `A-insert`
   clauses of G12 and G21, and X02 now names them; in each case the measurement
   is the literal five-map route, which the identity does not force.  GEN's
   dihedral relation is likewise forced for every completion (X06), so it is a
   disclosure and not a control.
10. **The G08 sector-law grid excludes the frozen-front variant by
    declaration**, and that variant is measured separately at G08B, where it
    carries the unit's sharpest result.  The receipt reports both counts — the
    72 cells in the grid and the 63 the gate adjudicates — rather than one.
11. **Two trees could not be taken as the census recorded them.**
    `v12/code/` and `v13/code/` are LIVE, written by concurrent cycles; both are
    declared excluded and **no live count is taken** of either, because a count
    of a tree this unit does not own is not reproducible by construction (X01).
12. **The declared secondary enters no verdict, and the `NOT-POSABLE` reading is
    withdrawn.**  A posability predicate built from the coordinates available
    here cannot return its other value anywhere in the declared arena, so it
    measures nothing; and two of the quantities such a predicate would cite —
    the holonomy group's order, and that order's membership in a GEN spectrum —
    are measured to be arena coordinates (§10.1, §10.2).  §10 is therefore a
    coordinate audit, every sentence of it either a measurement or an explicit
    non-measurement, and the morphism question is registered OPEN in §14
    (v13 LOG #246).
13. **Nine of seventeen anchors carry a declared falsifier.**  A01, A03, A05,
    A07, A09, A12 and A14 are covered by named anchor mutants; A02, A04, A06,
    A08, A10, A11, A13, A15, A16 and A17 are not, and every one of the seventeen
    is recomputed on every run.  Stated rather than left to be counted.
14. **G03's falsifier is a wholesale replacement.**  The lapse family is
    degenerated to a proportional family, which drives $\omega \equiv 0$ and
    collaterally kills five further gates.  Per RUNBOOK §14 a wholesale
    replacement does not establish that the *right* invariant is computed; the
    rank measurement is reported at that scope.
15. **The RUNBOOK addenda bind at delivery time, not at pin time.**  The §13
    addendum requiring a gate-derived verdict with a verdict-flip falsifier, and
    a cell-completeness gate, post-dates this unit's pin and precedes its
    delivery.  It binds.  Both are carried here (G25, G26), with the falsifiers
    that must die at each.

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
- **No bridge verdict of any kind.**  §10 measures coordinates; it runs no
  morphism census, decides no posability question, and claims no obstruction —
  neither that a carrier morphism exists nor that none does.  NT and GEN are not
  criticised; they are measured to sit at different coordinates.
- No claim that the group order of $\langle R_{HH}\rangle$, its exponent, or its
  membership in either GEN spectrum carries physical content: all three are
  measured to move with the declared reduction prime.
- No claim that the closure result is a derivation of geometry from something
  else: by §3.2 the record and the metric candidate are one datum in two
  coordinate systems, and the closure result is a statement about which function
  of the counts a drag rule computes.
- Nothing here is citable before an external hostile round confers TERMINAL.

---

## 14. Opens

**THE MORPHISM QUESTION — OPEN.**  Is there a carrier morphism relating
$R_{HH}$'s arena to the stitching geometry's, and does one carry the shared
bigon-plus-correction shape?  This unit does not answer it in either direction
(§10.5).  A successor bridge unit is what would, and it must carry, at minimum:

1. **A carrier functor**, defined between the two arenas as objects with their
   own typed data — not a comparison of two tables of coordinates — with the
   direction of the map declared and its domain stated.
2. **A morphism census**, not a single candidate expression: the admissible maps
   enumerated over a declared class, each tested, with the count of candidates
   and the count that survive both printed against honest denominators.  No
   cardinality criterion may stand in for a morphism test; equal carrier size is
   neither necessary nor sufficient.
3. **Two-way gates, both reachable.**  `BRIDGE-MORPHISM-FOUND` and
   `BRIDGE-EMPTY-AT-CARRIER` must each be reachable by measurement, and the
   reachability of **each** must be demonstrated by a declared falsifier that
   forces it — a synthetic arena at which the census returns a morphism, and one
   at which it returns none.  A predicate that cannot return its other value
   anywhere in the declared arena is not a measurement, and no verdict may rest
   on one.
4. **Arena-invariance gated at every quantity that enters the argument**, per
   RUNBOOK §15: any quantity that moves with a declared reduction prime, a
   declared basis, or a declared labelling may appear as an instrument reading
   and may not appear as a premise.

Also open, and untouched here: the divided form $(\Omega-I)/\epsilon^2$ with its
decoder $K_i$ (GW1 §5 items 2 and 4); a record-derived direction labelling (GW1
§2); a geometry-update law, and hence anything bearing on v4 paper 7 Theorem
6.1; $R_{DD}$, $R_{DH}$, and `V4P7-FIN-ALG-CLOSE`; general $d$, general $L$,
general records, general lapses, general weights.
