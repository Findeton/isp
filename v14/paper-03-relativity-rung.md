# R3 — THE RELATIVITY RUNG: the deformation algebra of the record layer

**Status:** `TERMINAL` — panel #39/#40/#45 (3× ACCEPT-WITH-FIXES),
adjudicated #46; repair R-R3-1…R-R3-10 delivered #71 and
adjudicator-verified (plain-run byte-identical; the full independent
selftest 124/124 mutants dead by named gates); v14 ledger #74,
2026-08-10.  Pin: `v14/note-r3-relativity-pin.md`, sha256-12
`a2ac89687a65`.**Pin:** `v14/note-r3-relativity-pin.md` (v14 ledger #23, `a2ac89687a65`).
**Instrument:** `v14/code/r3_relativity_exact.py` → `_output.txt`, `_receipt.json`.
**Base:** the R0 founding pin (row I7), the R2 joint adjudication's handoff
ruling, and nothing else.

---

## Scope box

This unit measures the deformation algebra of the record-native constraint
family $H_a[N]$ **at finite extent, at density weight $w=0$, on I7's own
declared lattice.** It claims nothing about a continuum limit (R1's terminal
closed that door until a non-copying refinement exists), nothing about
manifoldhood (R2's terminal holds those standards), and nothing about the
bridge walls (I1/I2 ride as anchors). Locality, the consistent chart-intrinsic
dimension and translation covariance of this lattice are **inherited facts**
from the R2 terminal, re-confirmed here as anchors and never re-derived.

Three further scopes are load-bearing and are carried at every claim rather
than in a box. The tangential family is restricted to **constant** fields in
the census, because $x\mapsto x+v(x)$ must be a bijection of the site set; two
declared non-constant bijective fields are run separately. The density weight
$w=1$ is declared by I7 and is **not swept**. And the arena's geometry record
is a **fixed background**: no declared generator moves it. Section 7 is the
measurement of that last fact, and it is this unit's central result.

---

## 1. The question, and the three relations it is asked against

Hypersurface-deformation structure is not one bracket but three:

$$\{H[N],H[M]\} = D\!\left[q^{ij}(N\partial_jM - M\partial_jN)\right],\qquad
\{D[v],H[N]\} = H[\mathcal L_vN],\qquad
\{D[v],D[w]\} = D[[v,w]].$$

Four properties make that system relativity-shaped rather than merely
algebraic, and each is a separate thing to look for:

1. the coefficient $q^{ij}$ in the first relation is a **canonical variable** —
   a function on phase space, not a fixed field — which is what makes the
   algebra open rather than a Lie algebra;
2. the third relation is **nonabelian**: $[v,w]$ is the Lie bracket of vector
   fields, so the tangential generators represent $\mathrm{vect}(\Sigma)$;
3. the second relation holds because $H$ is a scalar density of weight one;
4. the three are **one structure**, realised on one family, with their Jacobi
   identities linking them.

This unit asks the deformation question on I7's own sites, censuses all three
brackets, and reports each of the four properties as a separate measured
verdict. Two outcomes are gated as first-class from the pin: a closure, with
its coefficient class named, and a defect, characterised exactly.

---

## 2. The arena, as data

Everything below is read from the pinned I7 receipt (`542b8735daf0`) through
anchored (path, value) pairs; nothing about the arena is typed.

| coordinate | value |
|---|---|
| sites | $X = (\mathbb Z_L)^d$, periodic |
| links | the $d$ axis links and the $\binom d2$ positive diagonals |
| geometry record | $n_\ell(x)$, the interval cardinality on each link |
| readout | $q_{ij}(x)e_\ell^ie_\ell^j = n_\ell(x)$; $I_a(g) = q^{-1}$ at $w=0$ |
| constraint family | $H_a[N](n,m) = (n+N,\;m+w[N,n])$ |
| drag (arch A) | $w[N,n]^i(x) = N(x)\sum_j\Lambda^{ij}(x)\bigl(n(x+e_j)-n(x)\bigr)$ |
| tangential family | $D_a[v]$, at all 27 realisations built from its two declared atoms (§6) |
| lapse family | the $\lvert X\rvert$ site deltas, the constant profile $1$, the $d$ chart ramps |
| density weight | $w=0$ throughout; $w=1$ declared and not swept |
| censused arenas | $(d,L) \in \{(2,4),(2,5),(3,4),(3,5)\}$ |

**The lapse family is a named verdict coordinate**, censused at two declared
values: the family as I7 declares it (BASE), and that family closed under the
lattice's own chart translations (TRANSLATES). The second is an enlargement and
is printed as arena data — the deltas and the constant profile are already
translate-closed, while each chart ramp acquires $L$ translates, because a
ramp's wrap-around is not a constant shift.

The two inhomogeneous records `G-CURVED` and `G-CURVOFF` are built at $d=3$ as
well as $d=2$, by I7's own site-dependent recipes. This is a declared extension
of I7's $d=3$ list and is printed as such — without an inhomogeneous record a
structure function cannot be distinguished from a structure constant at all.

Of the 11 rules declared at d = 2, 9 are distinct as weight fields in the
first bracket and 8 in the register sector. `A-axis` and `B-axis` are the same
weight field at every site of every record, as are `A-chart` and `B-chart`; and
`A-insert` and `A-notransport` coincide in the drag that the register action
uses. Every count over "rules" below is a count over the **declared** list, and
this is the structure that makes some of those counts smaller than they look.

### The L gate

The excluded extent is excluded for a measured reason: at
d = 2, L = 3 the record lattice's overlap graph is complete at 36 of 36
pairs on 9 sites. A complete overlap graph fails the inherited criterion — some
component not complete — which is why R2 gated $L \ge 4$.

Of the six extents censused for the criterion, 5 meet it; d = 3, L = 3 is
among them and is excluded only because the inherited ruling gates L >= 4
uniformly.

That criterion arrives as a **(path, value) read out of the R2 terminal
receipt**, and this unit's implementation of it is controlled against a
declared pair of graphs: the three-vertex path, whose single component is not
complete, must be reported as bearing locality, and the complete graph on three
vertices must not. The R2 ruling's own sentences — the handoff, the gating
requirement, the two link profiles — arrive as verbatim-text anchors binding
context windows, each bound to the gate that consumes it. An attempted census
run below the gated extent dies at `G-L-GATE`.

---

## 3. The machinery-recovery control

Nothing new is allowed to count until the reimplementation reproduces I7's own
numbers at I7's own declared scope — which is precisely the extent the census
gate excludes.

The reimplementation reproduces 99 of 99 cells of the pinned closure table and
72 of 72 cells of its site-resolved sector law, with 0 mismatches.
The identifiability rank, the record-IS-metric readout determinant with its
site count, the general-$d$ row and the declared count lattice's link-locality
census all reproduce their pinned values as well. I7's diagonal sector is
recovered exactly: the link-local record-native rule closes on the five records
whose readout is diagonal, and on no others.

**Record-IS-metric** is re-encoded by two routes that share no code — the exact
linear solve and the closed form $q_{jj}=n_{e_j}$,
$q_{ij}=(n_{e_i+e_j}-n_{e_i}-n_{e_j})/2$ — agreeing at every site of every
admissible record and reproducing every declared link count.

---

## 4. The first bracket: what is measured, and what is a theorem

### 4.1 The structure theorem

Because $w[N,\cdot]$ is linear in the front, $H[N]H[M]$ and $H[M]H[N]$ differ
by the configuration-independent field $w[N,M]-w[M,N]$. The group commutator is
therefore a **pure tangential generator**, with an empty normal channel, and
its register displacement is $\Delta = W\Omega$, where $W$ is the rule's
declared drag matrix and

$$\Omega_\ell(x) = N(x)M(x+\ell)-M(x)N(x+\ell)$$

is the finite bracket covector on link $\ell$. Writing $B$ for the
record's inverse-metric matrix — the coefficient the first relation calls for —
the census residual is

$$\rho \;=\; \Delta - B\Omega \;=\; (W - B)\,\Omega .$$

Three consequences follow with no commutator in them at all.

- **The residual vanishes identically iff $W \equiv B$ pointwise.** Whether a
  cell's coefficient matches the record metric is a comparison of two declared
  fields at each site.
- **The coefficient system is consistent iff $W$'s diagonal-link columns
  vanish**, because a diagonal-link bracket cannot be reproduced by any
  $d\times d$ coefficient acting on the $d$ axis covectors.
- **The coefficient class is a pure function of $(W, B)$** — of the rule's
  declared weight field composed with the record's readout. Neither $L$ nor the
  lapse family appears in it.

A predictor built from the declared weight field and the record's readout
alone, carrying no commutator, reproduces the metric-match status and the
coefficient class at 476 of 476 cells, with 0 mispredictions. The whole
closure-and-coefficient census is therefore **forced** by the declarations, and
every clause of it is carried at that label (disclosure X01). The
$L$-constancy of the structural columns and the inertness of the lapse
coordinate are corollaries, not independent measurements.

### 4.2 What is genuinely measured: hypothesis (S)

The theorem determines the coefficient only if the realised bracket covectors
determine it — that is, only if they span. They do:

The realised bracket covectors span the full declared link space at 460 of 460
sites, over all 8 arena-and-lapse-scope combinations.

$\Omega$ is a function of the lapse pair and the lattice alone, never of the
record or the rule, and that independence is measured too. **This is the
load-bearing measurement of the entire first-bracket half.** It is what makes
the extracted coefficient a *determination* rather than a reading: no other
coefficient reproduces the commutators at any site. Every uniqueness statement
below, and the whole of §8's lapse-scope inertness, is a corollary of it.

The census is cell-complete at 476 cells over 4 arenas and 2 lapse scopes; the
commutator lands in the tangential generator family at every one of them. The
dense route cross-checks 198 of the 476 census cells, the third route -- which
shares no component with the other two, and which reaches every censused arena
-- 238, and the literal four-map composition 21420, with 0 disagreements in
total. The three routes are genuinely three: the
support-restricted and dense routes both build the residual from the gap matrix
$W-B$, so a corruption of that shared component would move them together; the
third reads the register displacement off the literal four-map composition and
subtracts the record-metric generator, touching the gap matrix nowhere.

### 4.3 Closure, defined against the declared basis

"Closes" here means one thing and one thing only: **the commutator lies in the
declared generator basis**. Which coefficient it closes with is a second,
independent question. Separating the two is what makes the pin's third outcome
— a rigid algebra, closing with a constant coefficient that is demonstrably not
a metric — a reachable verdict rather than an empty branch.

Measured against the declared generator basis, the commutator lies in the basis
at 440 of 476 cells. Of those, 216 close with a constant non-metric coefficient
-- the rigid form -- and 140 close with a coefficient equal to the record's
inverse metric.

So the rigid outcome is not a hypothetical: it is the census's most populous
form. The 36 cells that do not lie in the basis are treated in §4.5.

### 4.4 The structure coefficient, extracted and typed

The coefficient is not taken from the rule. It is **solved for** from the
commutators themselves: over every ordered lapse pair the system
$\Delta^i[N,M](x) = \sum_j c^{ij}(x)\,\omega_j[N,M](x)$ is assembled at each
site and reduced exactly, and the solution is then typed against an
independently re-encoded record metric.

The extracted coefficient is a reading of the record metric at 56 of 56 cells
of the metric-inserted rule, and it is site-varying -- a structure function,
not a constant -- at 32 of the 120 inhomogeneous-record cells, realised at
exactly 4 of the declared rules: A-axis, A-insert, A-insert-x, B-axis.

Two scopes belong at that sentence. At the metric-inserted rule both the
coefficient's *value* and its *site-variation class* are forced by declaration
(X03): the weight is the record-read inverse metric by construction, and
constant-versus-site-varying then asks only whether the record's count field is
constant, which is a property of the arena. And of the four rules realising the
class, three reduce to two distinct weight matrices. The honest reading of the
32-of-120 is therefore: it is the count of (rule, record) pairs at which the
declared weight happens to coincide with $q^{-1}$ on an inhomogeneous record.

### 4.5 The residual channel

The residual against the metric-inserted generator is nonzero at 336 of 476
census cells, and the coefficient system is inconsistent -- the commutator is
not in the declared basis at all -- at 36, which are exactly the cells of
B-all, 36 of the 108 architecture-B cells.

The mechanism is the diagonal-link column, and it belongs to one declared rule,
not to an architecture. `B-all` is the only rule that weights **every** link, so
its commutator carries diagonal-link brackets; `B-axis` and `B-chart` weight
only the axis links and are extractable at every one of their cells — indeed
four `B-axis` cells are themselves site-varying metric readings. The instrument
gates the iff over the whole census: the non-extractable set equals the set of
cells whose weight matrix has a nonzero diagonal-link column, computed, not
asserted.

### 4.6 What the first bracket actually is

The two-cocycle identity holds at 4284 of 4284 cells, and the commutator field
is configuration-independent at 3570 of 3570 ordered lapse pairs.

That is, $H[N]H[M] = T_{w[N,M]}\circ H[N+M]$ exactly: the constraint family
generates a two-step nilpotent group — a **central extension** of the abelian
group of lapse profiles by the register fields, with $w$ as its two-cocycle —
and the "structure coefficient" the extraction returns is that cocycle's
antisymmetrisation. The commutator field does not move when the dynamical
configuration moves. Property 1 of §1 — the coefficient as a canonical variable
— is therefore **measured absent**. The object here is exact in form and
analogical in status.

---

## 5. The second bracket: $\{D,H\}$

The second relation requires $\{D[v],H[N]\} = H[\mathcal L_vN]$. Over 21012
normal-tangential brackets the tally is D-REG/IDENTITY 10506; D-TOT/IDENTITY
120; D-TOT/OUTSIDE 10386, and the bracket lies in the constraint family at 0 of
them. That denominator is not balanced across dimension: 18612 of it at d2,
2400 of it at d3.

**At D-REG** — the realisation in which $D_a[v]$ shifts the address register
and does not transport the front — the bracket is the identity, and this is
forced (X02): the register shift and the front shift are independent summands
of the total configuration. The entire deformation content of this bracket is
absent there.

**At D-TOT** — in which $D_a[v]$ also drags the front along $x\mapsto x+v(x)$ —
the bracket is nontrivial and its closed form is exact:

$$\text{front} \;=\; S_vN - N,\qquad
\text{register} \;=\; w\bigl[N,\;(S_{-v}-1)(n-N)\bigr],\qquad
(S_vn)(x) := n(x-v).$$

Both closed forms are verified against the literal four-map composition.

### The convention sweep

The front sector's apparent mismatch with $\mathcal L_vN$ under the declared
forward difference is a *convention*, and the instrument decides that by
measurement, sweeping both factor orders against both finite-difference
directions.

Exactly 1 of the 4 declared convention combinations makes the bracket's front
sector equal the transported lapse derivative everywhere:
H-D-Hinv-Dinv/BACKWARD. The sweep evaluates 685 distinct front-sector probes.

685 is the number of front-sector computations actually performed. The front
closed form is a function of the lapse and the translation alone — measured, at
every declared record and at two declared rules per arena — so the sweep is
evaluated once per (lapse, translation) probe. The record and rule
multiplicity is disclosed beside that count and never folded into it (X12): a
number obtained by multiplying a measured sample by an unvaried axis is an
argument, not a census.

So the front sector reproduces the deformation content exactly, at one declared
convention and at constant $v$. What survives the sweep is the register sector.

---

## 6. The realisation census

I7 declares exactly two ingredients for $D_a[v]$: the site map $x\mapsto x+v(x)$
and the address register. A realisation is therefore a triple
$(a,b,c)\in\{-1,0,1\}^3$ —

$$D_{(a,b,c)}[v]\;:\;(n,m)\;\longmapsto\;\bigl(S_{av}\,n,\;S_{cv}\,m + bv\bigr),$$

$a$ dragging the front, $b$ shifting the register, $c$ transporting the
register field along the *same declared site map*. I7's two named realisations
are two of these: D-REG $=(0,1,0)$ and D-TOT $=(1,1,0)$. No new ingredient
enters at $(1,1,1)$; it is the realisation in which the register's labelling is
carried along by the very map that already carries the front.

All 27 are censused.

Across all 27 realisations built from the two declared atoms, over 73872
classifications, the bracket lies in the constraint family at 0 of them. At the
6 realisations that transport the register along the same declared site map it
lies in the extended basis at every one of the 12384 homogeneous-record
classifications, resisting at exactly 24 cells.

Three results, of quite different strength.

- **The defect head is realisation-independent, and absolutely so.** No
  declared-expressible realisation whatsoever realises
  $\{D[v],H[N]\}=H[\mathcal L_vN]$ — 0 of 73872, across every triple and every
  arena censused. This is the strongest statement in the unit.
- **The *outside-the-basis* characterisation is realisation-relative.** At the
  realisations with $a=c\neq 0$ the bracket lies inside the declared basis
  extended by a fixed tangential factor, on the entire homogeneous sector.
- **The residue is curvature-supported.** The 24 resisting cells are exactly
  the inhomogeneous records paired with the rules whose weight reads the
  record's counts; the two count-blind rules never resist, and no homogeneous
  record resists at all. Where the register is transported, what is left of the
  obstruction sits precisely where the geometry is inhomogeneous.

The register shift $b$ is inert: it cancels from the bracket identically, and
the census reports that rather than three copies of the same row.

---

## 7. The covariance theorem, and the background it detects

Conjugation by full transport carries the constraint of the record to the
constraint of the transported record at 2064 of 2064 cells; at the realisation
that transports the front but not the register it holds at 0 of 2064.

That is, exactly and at every cell of the declared probe,

$$D_{\mathrm{full}}[v]\;\circ\;H_g[N]\;\circ\;D_{\mathrm{full}}[v]^{-1}
\;=\; H_{S_vg}\bigl[S_vN\bigr].$$

The negative side is what makes the positive one a measurement: at D-TOT, which
transports the front but leaves the register's labelling behind, the same
identity fails at every cell.

**This is the unit's central result, and it is a statement about the arena.**
The constraint family is exactly covariant under full transport — the moment
every declared field moves, the algebra moves with it. What does not move is
$g$: the conjugated constraint is the constraint *of the transported record*,
and $H_{S_vg}\neq H_g$ whenever the record is inhomogeneous and the rule reads
it. No declared generator transports the geometry record. In the continuum
relation, $D[v]$ moves $q_{ij}$; here nothing does.

So the honest positive claim of this unit is **fixed-background covariance with
GR's bracket form**, and the surviving obstruction is not that matter fails to
follow geometry's deformations. It is that **this arena carries a fixed
background metric, and this bracket is the exact functional that detects it.**

The unit's own symmetry self-test is the same fact from the other side: it
transports the record and the lapses together and finds the residual field
exactly covariant. The control's success and the bracket's failure are one
statement seen twice.

---

## 8. The defect, characterised

$$\text{defect}\;=\;w\bigl[N,(S_{-v}-1)(n-N)\bigr]\;-\;w\bigl[S_vN-N,\;n\bigr].$$

The defect is nonzero at 3096 of 3096 probes, its lattice sum is nonzero at
3096 of them, and it vanishes at 0 of the 2280 homogeneous-record probes.

Read that as four measurements, each carried at the realisation D-TOT.

- **It never vanishes.** No rule, no record, no lapse, no translation direction
  in the declared probe set kills it.
- **It is not a boundary term.** On a periodic lattice a total finite
  difference sums to zero; this one does not, at any probe. The degenerate
  probe is built and measured: the zero lapse profile gives a defect field that
  vanishes identically and whose lattice sum is zero at 60 of its 60 probes,
  while the unit constant profile vanishes at 12 of its 60. The boundary test
  can therefore produce a zero, and does, on a field declared for the purpose.
- **It does not switch off on the homogeneous records** at the field level.
  At the membership level this reverses under transport: §6's absorbing
  realisations put the whole homogeneous sector inside the extended basis, and
  the residue that survives is exactly the inhomogeneous one. The defect field
  is about transport; the residue that survives a full-transport realisation is
  about curvature.
- **It is $L$- and $d$-independent**, and the mechanism explains why: it is a
  per-site comparison of two weight fields, and extent does not enter.

The defect is nonzero at 3096 of 3096 probes under the other declared bracket
order, and the bracket lies outside the declared basis at 1188 of 1188 probes
at the declared non-constant tangential fields. Neither the choice of factor
order nor the restriction to lattice translations is load-bearing for it.

Under the declared-arena discipline the defect is therefore an **instrument**,
and an excellent one: exact closed form, cheap, extent-free, and precise about
which declared fields a declared generator transports. It is not by itself a
conclusion, because its basis-membership status is not invariant across the
arena's admissible realisations. What is invariant, and what §7 states, is the
background.

---

## 9. The third bracket, and the controls

The lattice's own translation generators close exactly: 644 of 644 tangential
brackets are the identity, of which 192 pair two distinct nonzero generators.

Since the bracket of two constant vector fields vanishes, this is exactly what
the third relation demands of them — so the closure is **forced** (X04) and is
used as a positive control for the commutator machinery, with a declared
corruption of the tangential comparison map flipping it. The 192 is the
informative count; the remaining brackets (derived in text: 644 − 192 = 452)
pair a generator with itself or with zero.

The relation's discriminating content is **absent, not merely forced**. The
censused family contains only constant fields, where $[v,w]\equiv 0$
identically, so the nonabelian core is untested by construction (X08). This
restriction has a second cost: the generator the first bracket produces is
generally not a member of the family the second bracket uses, so the three
relations are not simultaneously realisable on one declared tangential family
at this arena.

The declared chart group closes at 4 of 4 censused arenas. Its order is derived
by explicit closure of the generated permutation group of the site set, and
equals $\lvert X\rvert\cdot d!$ at every one.

The record lattice is translation-equivariant at 120969 of 120969 cells; the
scrambled lattice violates equivariance at 58572 of 120969, and breaks the
residual field's covariance at 128 cells. The equivariance of the record
lattice is **forced by modular arithmetic** — $(x+u)+\ell = (x+\ell)+u$ — and
is carried at that label (X11); the measurement is the scrambled lattice's
violation count, and the residual-covariance probe ships its non-vacuity as the
number of *distinct* nonzero base cells, not that number multiplied by the
translations it was recomputed under.

---

## 10. The L-sweep

| $d$ | $L$ | scope | cells | in basis | rigid | metric match | max $\lvert\rho\rvert$ | metric-reading | site-varying |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 4 | BASE | 99 | 90 | 46 | 26 | 9 | 26 | 5 |
| 2 | 4 | TRANSLATES | 99 | 90 | 46 | 26 | 9 | 26 | 5 |
| 2 | 5 | BASE | 99 | 90 | 46 | 26 | 16 | 26 | 5 |
| 2 | 5 | TRANSLATES | 99 | 90 | 46 | 26 | 16 | 26 | 5 |
| 3 | 4 | BASE | 20 | 20 | 8 | 9 | 8 | 9 | 3 |
| 3 | 4 | TRANSLATES | 20 | 20 | 8 | 9 | 27 | 9 | 3 |
| 3 | 5 | BASE | 20 | 20 | 8 | 9 | 128/9 | 9 | 3 |
| 3 | 5 | TRANSLATES | 20 | 20 | 8 | 9 | 48 | 9 | 3 |

At fixed $d$ every structural column is constant in $L$ and in the lapse
scope — and per §4.1 that constancy is **forced**: the per-cell class is a
function of (rule, record) alone, in which neither $L$ nor the lapse family
appears. The sweep's honest headline is the other column. The structure is
extent-free by construction; the anomaly's size is not, and it moves along both
coordinates.

Enlarging the lapse family to its lattice translates moves the residual
MAGNITUDE at 62 of the 238 (arena, rule, record) cells compared across the two
scopes -- always upward, at 62 of 62 -- and moves no cell's closure status and
no cell's coefficient class (0 moved). The second half of that sentence is a
corollary of hypothesis (S): with full spanning already at BASE, enlarging the
family cannot change a coefficient the commutators already determine.

---

## 11. The correspondence, relation by relation

| object | this arena's object | verdict |
|---|---|---|
| Poisson bracket on phase-space functionals | group commutator of bijections of a configuration set | ABSENT — no symplectic form, no phase space |
| constraint ($H\approx 0$, first class) | an invertible map; nothing vanishes, no surface | ABSENT — "constraint family" is a name here |
| $N\partial_jM - M\partial_jN$ | $\Omega_j(x)=N(x)M(x+e_j)-M(x)N(x+e_j)$ | EXACT — the finite transcription |
| $q^{ij}$ as a value | $\Lambda^{ij}(x)$, matched against an independently re-encoded $q^{-1}$ | EXACT where the rule declares it (X03) |
| $q^{ij}$ as a **structure function** | read from a fixed background record; the commutator field is configuration-independent | ABSENT — measured, §4.6 |
| relation (I)'s landing | $D_a[\Lambda^{ij}\Omega_j]$, empty normal channel | EXACT IN FORM, FORCED (X01) |
| relation (II), front sector | $S_vN-N$ against $\mathcal L_vN$ | EXACT at one convention, at constant $v$ |
| relation (II), register sector | the defect | DEFECTS at D-TOT; absorbed at the transporting realisations on the homogeneous sector |
| relation (III) | only constant fields, where $[v,w]\equiv 0$ | ABSENT in discriminating content (X08) |
| $q$ transported by $D[v]$ | no declared generator moves the record | ABSENT — §7 |
| signature $\varepsilon$ | not measured | ABSENT |
| density weight of $H$ | $w=0$ only; $w=1$ declared, not swept | ABSENT (X09) |
| the representation leg | not attempted | ABSENT — and not claimed |

**Relation (I) — exact in form, analogical in status.** The finite bracket
covector is the exact lattice transcription and the coefficient equals $q^{-1}$
where declared; but the bracket is a group commutator, the coefficient is a
background field, and the algebra realised is a central extension, not an open
algebra.

**Relation (II) — partial.** Front sector exact at one convention and at
constant $v$; register sector defective at D-TOT, absorbed at the transporting
realisations on the homogeneous sector, entirely absent at D-REG.

**Relation (III) — contentless here.** Only the abelian constant-field
subfamily is testable, by the bijection requirement.

The name this unit uses for what it found is therefore **fixed-background
covariance with GR's bracket form**. The paper does not use the unqualified
name for the continuum algebra, because three of its four defining properties
are measured absent and the fourth is realised on a background.

---

## 12. The verdict

```
R3-DEFORMATION-DEFECT-AT<ARENA=…|L-GATE=…|RECOVERY=…|SPANNING=…|
HH-BRACKET=…|COEFFICIENT=…|HH-CLOSURE=…|HH-RESIDUAL=…|DH-BRACKET=…|
REALISATION-CENSUS=…|COVARIANCE=…|DEFECT=…|CONVENTION=…|DD-BRACKET=…|
CORRESPONDENCE=…|LAPSE=…|REALISATION=…|LSWEEP=…|CONTROLS=…|SCOPE=…>
```

The full string, with every segment's computed value, is emitted by the
instrument and carried in the receipt; it is compared character for character
against an independent reconstruction built from the receipt's own raw measured
rows, by a comparator that shares no code and no input with the builder and
reads deep copies of every table.

**In words.** The record layer carries a deformation algebra whose first
bracket has GR's exact bracket form on a fixed background, whose second bracket
does not close at any expressible realisation, and whose third bracket is
untestable here.

1. $\{H,H\}$ lands in the declared tangential family at every census cell, with
   an empty normal channel — and both facts are forced by the linearity of the
   drag. The census's closure-and-coefficient content is a corollary of the
   structure theorem $\rho=(W-B)\Omega$; what is measured is hypothesis (S),
   the residual magnitudes, and the sector arithmetic. Against the declared
   basis the commutator closes at 440 of 476 cells, most populously in the
   **rigid** form, and at the metric-inserted rule with a coefficient equal to
   the record metric, site-varying on the inhomogeneous records.
2. $\{D,D\}$ closes exactly on the lattice's own translation generators, and
   carries no discriminating content: $[v,w]$ vanishes identically on the
   censused family.
3. $\{D,H\}$ **does not close, at any of the 27 declared-expressible
   realisations, over 73872 classifications.** Its front sector reproduces the
   transported lapse derivative exactly at one declared convention; its
   register sector lies outside the declared basis at D-TOT, is absorbed on the
   whole homogeneous sector at the realisations that transport the register,
   and leaves a curvature-supported residue.
4. Conjugation by full transport is **exactly covariant**, at 2064 of 2064
   cells. The obstruction that survives every realisation is that the geometry
   record does not transport: **the arena carries a fixed background.**

The head is the defect head, and the deliverable is the pair of exact objects
behind it — the covariance law, and the functional that measures its failure.

---

## 13. Forced clauses, disclosed

| id | forced clause | what is measured instead |
|---|---|---|
| X01 | the whole $\{H,H\}$ closure-and-class census, via $\rho=(W-B)\Omega$ | hypothesis (S); the residual magnitudes; the literal-composition agreements |
| X02 | the D-REG normal-tangential identity | the D-TOT classification and the realisation census |
| X03 | the positive control's coefficient value **and** its site-variation class | uniqueness; the class census away from the positive control |
| X04 | the $\{D,D\}$ closure at constant fields | the control's sensitivity; the informative count |
| X05 | non-extractability where the weight has a diagonal-link column | which declared rules those are |
| X06 | the $d=3$ inhomogeneous records are a declared extension | printed as arena data |
| X07 | the bracket census's $d=3$ lapse scope is I7's own probe convention | printed and gated |
| X08 | the constant-field restriction and its two costs | the non-constant bijective probes |
| X09 | the whole unit runs at $w=0$; $w=1$ declared, not swept | — |
| X10 | the declared rule list contains exact duplicates | the distinct-rule counts, per sector |
| X11 | the translation control's every-cell agreement is forced by modular arithmetic | the scrambled lattice's violations |
| X12 | the convention sweep's denominator is its distinct probe count | the front sector's record- and rule-independence |

---

## 14. What this does not claim

The site-varying coefficient is realised at four declared rules, three of which
reduce to two distinct weight matrices, and on off-diagonal inhomogeneous
records only the rule that already contains the metric produces it. Nothing
here derives the metric from the record; I7's record-IS-metric result already
says the two are one datum in two coordinate systems.

The defect is a finite-extent statement. Whether it survives a refinement
direction is not asked, because R1's terminal leaves no legitimate refinement
to ask it in.

The tangential realisation is a **named verdict coordinate** with 27 declared
values, and the unit reports all of them. Neither the choice of D-REG nor of
D-TOT is a bookkeeping choice, and neither is a conclusion.

The signature is not measured. The density weight is not swept. The
representation leg — algebra plus canonical embedding variables implying field
equations — is not attempted, and this unit makes no claim on it.

---

## 15. The successor's requirements

These are the conditions a successor must meet to earn the claim this unit
declines. They are stated as requirements, not as findings, and this unit's own
numbers are the null results several of them are written against. **They are
recorded verbatim as received.** Any figure appearing inside a requirement —
FR5's percentages, FR11's constant — belongs to the requirement as stated and
is not a measurement of this unit; every number this unit asserts is rendered
from its receipt and appears in §§2–10 and §17.

- **FR1 — A BRACKET, NOT A GROUP COMMUTATOR.** Declare a phase space (or a Lie
  algebroid with a named anchor) and compute the relations as brackets on it.
  Gate antisymmetry and the **Jacobi identity**, measured, with a mutant that
  breaks it. Until then the object is a group, and group commutators of
  bijections are not the HDA.
- **FR2 — THE COEFFICIENT MUST MOVE WITH THE STATE.** Gate: vary the dynamical
  configuration at fixed declarations and measure that the {H,H} coefficient
  changes. R3's configuration-independence is the null result this requirement
  is written against. Operationally this requires the **record counts to enter
  the configuration space**.
- **FR3 — THE RECORD MUST TRANSPORT.** A tangential generator must act on *all*
  declared fields — front, register **and record**. R3's covariance theorem
  (`D_full H_g[N] D_full⁻¹ = H_{S_v g}[S_v N]`, 2064/2064) shows the algebra is
  exactly covariant the moment it does; the successor either makes the record
  dynamical or states that its arena carries a **fixed background metric**, in
  which case the HDA is the wrong target and must not be named.
- **FR4 — NONABELIAN TANGENTIAL GENERATORS.** Declare a tangential family closed
  under a nonvanishing bracket — e.g. lattice vector fields realized by partial
  bijections / a groupoid action rather than by `x ↦ x+v(x)` — and measure
  `{D[v],D[w]} = D[[v,w]]` with `[v,w] ≠ 0` at a stated fraction of the census.
  Report that fraction; if it is 0, relation (III) is not tested.
- **FR5 — ONE ALGEBRA, ONE REALIZATION.** Gate that the generator produced by (I)
  **is an element of the family used in (II) and (III)**. R3 fails this at
  99.29% (d=2,L=4) and 99.75% (d=3,L=4) of its own nonzero generators, and the
  failure is invisible in the delivery. A three-relation claim requires a single
  realization in which all three brackets are defined.
- **FR6 — THE SAME `q` IN BOTH PLACES.** Gate that the metric read off the {H,H}
  coefficient is the *same datum* as the metric appearing in `H`'s own definition,
  as a measured identity rather than a declaration (X03 currently installs it).
- **FR7 — SIGNATURE.** Measure `ε` in `{H,H} = ε D[q⁻¹(N dM − M dN)]` and its
  stability across records. A relativity-shaped claim that does not know its own
  signature is incomplete.
- **FR8 — DENSITY WEIGHT SWEPT, NOT ANCHORED.** Sweep `w ∈ {0,1}` (both are
  declared) and gate the weight at which (II)'s front sector holds.
- **FR9 — A RIGID OUTCOME THAT CAN WIN.** Define the residual against the
  **declared generator basis**, so that "closes with a constant non-metric
  coefficient" is a reachable verdict. Ship the injection that returns it.
- **FR10 — SCALE, OR SILENCE ABOUT SCALE.** "At scale" requires the relations to
  survive a refinement direction. R1's terminal closes that door; until it
  reopens, the requirement is to carry the finite-extent scope **at the claim**,
  not only in a scope box.
- **FR11 — THE REPRESENTATION LEG, NAMED.** The HDA's force is HKT: algebra +
  canonical embedding variables ⟹ Einstein up to two constants, and the corpus's
  own paper 57 already proves `G` un-fixable here (`κ·σ_A = G·Λ² = const`). A
  successor must state which leg it attempts and which it concedes.

**FR3 is this unit's own conclusion, not a request.** The arena measured here
is a declared fixed background: §7 is the exact statement of it, and that is
why this paper does not use the unqualified name for the continuum algebra
anywhere.

FR9 is met in this delivery: §4.3 defines closure against the declared basis,
the rigid form is the census's most populous outcome, and the verdict machinery
is shown to return the rigid head on a synthetic payload built to exhibit it.

---

## 16. The handoff to R4

R4 inherits the arena — I7's lattice with R2's locality and dimension facts and
this unit's covariance machinery, the full-transport conjugation law — and
three instruments.

**The seed is not the register defect.** It fails the realisation census: a
realisation built from the same declared ingredients absorbs it on the entire
homogeneous sector, and its signature property inverts there — "a statement
about transport" becomes "a statement about curvature" one realisation over. A
seed for an interaction law must be invariant across the arena's admissible
realisations, and this one is not. What survives is a background, not an
interaction, and building interactions on the obstruction would encode a fixed
background into the interaction law. The seed R4 takes is $\Delta^{\mathrm B}$,
the composition defect: a defect of a *composition*, which is what an
interaction is, and one that has already survived a realisation and relabelling
hunt at its own scope.

**The gate is the realisation census.** Every R4 interaction generator declares
which of the arena's fields it transports, and is run through an enumeration of
the realisations built from its own declared atoms. No defect enters an R4
verdict head without that census, and a defect's status is read only at the
maximal declared transport. This unit's numbers ship as the gate's controls:
D-TOT gives 10386 OUTSIDE; the transporting realisations give 0 OUTSIDE on the
homogeneous sector; and the covariance theorem, 2064 of 2064, is the closed
form the gate checks against.

**The third layer is the background detector.** The register defect's
functional is exact, cheap, and independent of extent and dimension. If an R4
arena is meant to carry no background, this functional must vanish on it. If it
does not, the arena has one, and the functional says where.

---

## 17. The instrument

99 gates, all passed; 44 anchors; 124 mutants, all dead.
Every count is computed, never typed. The arena arrives through 4 verbatim-text
anchors, 7 file-byte anchors and 32 (path, value) anchors, plus one anchor
whose expected hash is read out of the pinned receipt itself. Two plain runs
are byte-identical. The falsification selftest re-invokes the instrument once
per mutant and requires exit 1, a named gate, an unchanged artifact pair and no
traceback.

Every file this instrument reads at run time is either a hash-pinned artifact
carrying both a byte anchor and a value anchor — (path, value) for JSON,
verbatim-text context windows bound to their consumer gate for prose — or this
unit's own owned paper, read by the gate that renders its numbers. No ledger,
no status board and no other unit's working file is read anywhere, and the
declared read list is itself gated.

The payload written to disk is sealed: a digest of the whole gated subtree is
taken after the last measurement gate and re-verified immediately before the
write, together with a fresh render check and a fresh independent rebuild of
the verdict, so that no mutation of a measured row between the gates and the
write can ship. Every anchor row of every kind carries its own declared
falsifier; every waiver's counts are computed from the falsifier map and
audited; and the falsifier map is rebuilt in the final pass so it cannot go
stale against the census printed beside it.
