# R3 — THE RELATIVITY RUNG: hypersurface deformation on the record lattice

**Status:** GREEN-UNREVIEWED.
**Pin:** `v14/note-r3-relativity-pin.md` (v14 ledger #23, `a2ac89687a65`).
**Instrument:** `v14/code/r3_relativity_exact.py` → `_output.txt`, `_receipt.json`.
**Base:** the R0 founding pin (row I7), the R2 joint adjudication's handoff
ruling, and nothing else.

---

## Scope box

This unit measures the deformation algebra of the record-native constraint
family $H_a[N]$ **at finite extent on I7's own declared lattice**. It claims
nothing about a continuum limit (R1's terminal closed that door until a
non-copying refinement exists), nothing about manifoldhood (R2's terminal holds
those standards), and nothing about the bridge walls (I1/I2 ride as anchors).
Locality, the consistent chart-intrinsic dimension and translation covariance of
this lattice are **inherited facts** from the R2 terminal; they are re-confirmed
here as anchors, never re-derived as results.

---

## 1. The question

Hypersurface-deformation structure is not one bracket but three:

$$\{H[N],H[M]\} = D\!\left[q^{ij}(N\partial_jM - M\partial_jN)\right],\qquad
\{D[v],H[N]\} = H[\mathcal L_vN],\qquad
\{D[v],D[w]\} = D[[v,w]].$$

What makes the first of these *relativity-shaped* rather than merely algebraic
is the coefficient $q^{ij}$: a **reading of the metric**, varying from point to
point — a structure *function*, not a structure *constant*. An algebra that
closes with constant coefficients is a rigid algebra, a strictly weaker
geometry.

The R2 handoff established that the record layer's own lattice — I7's sites,
links, chart group and lapse family — satisfies the inherited locality
criterion, is translation-covariant, and carries a consistent chart-intrinsic
dimension. This unit asks the deformation question there, on I7's own sites,
with all three brackets censused and both first-class outcomes gated:

- `R3-DEFORMATION-CLOSES<…>`, naming the coefficient class;
- `R3-DEFORMATION-DEFECT-AT<…>`, in which the defect is a **measured object**
  — its generator decomposition, its $L$- and $d$-dependence, its boundary-term
  status and its sector behaviour all measured, exactly as the v12 precedent
  requires.

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
| tangential family | $D_a[v]$, at the two declared realisations D-REG and D-TOT |
| lapse family | the $\lvert X\rvert$ site deltas, the constant profile $1$, the $d$ chart ramps |
| censused arenas | $(d,L) \in \{(2,4),(2,5),(3,4),(3,5)\}$ |

**The lapse family is a named verdict coordinate**, and it is censused at two
declared values: the family as I7 declares it (BASE), and that family closed
under the lattice's own chart translations (TRANSLATES). The second is an
enlargement and is printed as arena data: the deltas and the constant profile
are already translate-closed, while each chart ramp acquires $L$ translates,
because a ramp's wrap-around is not a constant shift.

The two inhomogeneous records `G-CURVED` and `G-CURVOFF` are built at $d=3$ as
well as $d=2$, by I7's own site-dependent recipes. This is a declared extension
of I7's $d=3$ list and is printed as such — without an inhomogeneous record a
structure function cannot be distinguished from a structure constant at all.

### The L gate

The excluded extent is excluded for a measured reason: at d = 2, L = 3 the
record lattice's overlap graph is complete at 36 of 36 pairs on 9 sites.
A complete overlap graph fails the inherited criterion (some component not
complete), which is why R2 gated $L \ge 4$. The instrument recomputes the
locality fractions the R2 record states for this lattice and finds them in its
text; an attempted census run below the gated extent dies at `G-L-GATE`.

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

## 4. The first bracket: $\{H,H\}$

Because $w[N,\cdot]$ is linear in the front, $H[N]H[M]$ and $H[M]H[N]$ differ by
the configuration-independent field $w[N,M]-w[M,N]$. The group commutator is
therefore a **pure tangential generator**, with an empty normal channel:

$$[H[N],H[M]] = D_a\bigl[\Lambda^{ij}\,\omega_j\bigr],\qquad
\omega_j(x) = N(x)M(x+e_j)-M(x)N(x+e_j).$$

**This landing is FORCED, and is carried at that label** (disclosure X01): it
follows from the linearity of the drag in the front, not from a census. The
census is cell-complete at 476 cells over 4 arenas and 2 lapse scopes; the
commutator lands in the tangential generator family at every one of them.
The verdict segment says so at its forced label. What the census *measures* is
the coefficient and the residual channel. The literal four-map composition
$H[N]H[M]H[N]^{-1}H[M]^{-1}$, applied to three declared front configurations,
leaves the front unmoved and reproduces the closed-form register displacement
exactly.

The dense route cross-checks 198 cells and the literal four-map composition
21420, with 0 disagreements in total.

### The structure coefficient, extracted rather than read off

The coefficient is not taken from the rule. It is **solved for** from the
commutators themselves: over every ordered lapse pair the system

$$\Delta^i[N,M](x) \;=\; \sum_j c^{ij}(x)\,\omega_j[N,M](x)$$

is assembled at each site and reduced exactly. The system is heavily
over-determined, so existence is a real test. The extracted coefficient is then
**typed by measurement** against an independently re-encoded record metric.

That the positive control's coefficient *value* is a metric reading is forced by
its own declaration (disclosure X03) — its weight is the record-read inverse
metric by construction. What the extraction adds, and what is measured, is
**uniqueness** (the realised bracket covectors span fully at every site, so no
other coefficient reproduces the commutators) and the **site-variation class**,
which the rule's declaration does not state.

The extracted coefficient is a reading of the record metric at 56 of 56 cells of
the metric-inserted rule, and it is site-varying -- a structure function, not a
constant -- at 32 of the 120 inhomogeneous-record cells.

This is the unit's positive finding, and it is exactly the
hypersurface-deformation signature in the first bracket: on the inhomogeneous
records the commutator's coefficient is the record-read inverse metric,
**different at different sites**. On the homogeneous records the same
coefficient is a metric reading that happens to be constant — the two classes
are indistinguishable there, which is why the inhomogeneous records carry the
discrimination.

### The residual channel

The residual channel is nonzero at 336 of 476 census cells, and the coefficient
system is inconsistent -- no structure coefficient exists -- at 36.
The inconsistent cells are exactly the architecture-B rules: their commutator
carries diagonal-link brackets, so its displacement is not of the axis-covector
form at all, and no $d\times d$ coefficient can reproduce it. That the arch-B
cells fail is forced by that observation (disclosure X05); what is measured is
that the same solve *succeeds* at every architecture-A cell, so the failure is a
property of the rule and not of the instrument.

---

## 5. The second bracket: $\{D,H\}$

Hypersurface deformation requires $\{D[v],H[N]\} = H[\mathcal L_vN]$. Both
declared tangential realisations are censused, at the lattice's own translation
generators, against every declared configuration.

Over 21012 normal-tangential brackets the tally is D-REG/IDENTITY 10506;
D-TOT/IDENTITY 120; D-TOT/OUTSIDE 10386, and the bracket lies in the constraint
family at 0 of them.

The two realisations fail in two different measured ways.

**At D-REG** — the primary realisation, in which $D_a[v]$ shifts the address
register and does not transport the front — the bracket is the **identity**,
and this is forced (disclosure X02): the register shift and the front shift are
independent summands of the total configuration.
The tangential generator does not see the front at all, so the entire
hypersurface-deformation content of this bracket is absent. (I7's own detector
row records the same fact locally, as `C_trivial`; here it is censused in full.)

**At D-TOT** — in which $D_a[v]$ also drags the front along $x\mapsto x+v(x)$ —
the bracket is nontrivial, and its closed form is exact:

$$\text{front} \;=\; S_vN - N,\qquad
\text{register} \;=\; w\bigl[N,\;(S_{-v}-1)(n-N)\bigr],\qquad
(S_vn)(x) := n(x-v).$$

Both closed forms are verified against the literal four-map composition. The
front sector is the good news; the register sector is the defect.

### The convention sweep

The front sector's apparent mismatch with $\mathcal L_vN$ under the declared
forward difference is a *convention*, and the instrument decides that by
measurement rather than argument, sweeping both factor orders against both
finite-difference directions.

Exactly 1 of the 4 declared convention combinations makes the bracket's front
sector equal the transported lapse derivative everywhere:
H-D-Hinv-Dinv/BACKWARD.

So the normal-tangential bracket's **front sector reproduces the
hypersurface-deformation content exactly**, at one declared convention, at every
bracket in the census. What survives the sweep is the register sector.

---

## 6. The defect, characterised

$$\text{defect}\;=\;w\bigl[N,(S_{-v}-1)(n-N)\bigr]\;-\;w\bigl[S_vN-N,\;n\bigr].$$

It is not $H[P]$ for the $P$ its own front names, and it is not $H[P]\circ D[u]$
for any configuration-independent $u$: the deviation is a *different linear
functional of the front* from the one any constraint generator computes, and
tested at three declared configurations it moves with the configuration. The
defect therefore lies **outside the declared generator basis**, which is the
precise sense in which the algebra does not close.

The defect is nonzero at 3096 of 3096 probes, its lattice sum is nonzero at 3096
of them, and it vanishes at 0 of the 2280 homogeneous-record probes.

Read that as four separate measurements:

- **It never vanishes.** No rule, no record, no lapse, no translation direction
  in the declared probe set kills it.
- **It is not a boundary term.** On a periodic lattice a total finite difference
  sums to zero; this one does not, at any probe. The degenerate probe — the zero
  field, which does sum to zero — is carried alongside as the test's own death
  certificate, so the boundary test is not vacuous.
- **It has no vanishing sector.** In particular it does not switch off on the
  homogeneous records, where the metric is constant and the first bracket's
  coefficient becomes indistinguishable from a constant. The defect is a
  statement about *transport*, not about curvature.
- **It is $L$- and $d$-independent.** It is present with the same character at
  every censused arena.

The mechanism is legible in the closed form. A constraint generator's drag reads
the front difference at $x$; the bracket's drag reads the front difference
*between two lattice points a translation apart*. At finite extent those are
different functionals, and no member of the declared basis computes the second.
This is a finite-lattice statement, and the unit claims it only at finite
extent.

---

## 7. The third bracket: $\{D,D\}$, and the controls

The lattice's own translation generators close exactly: 644 of 644 tangential
brackets are the identity. Since the bracket of two constant fields vanishes,
this is exactly what hypersurface deformation demands of them — so the closure
is **forced** (disclosure X04) and is used as a **positive control** for the
commutator machinery rather than reported as a discovery. Its non-vacuity is
shown, not asserted: the declared corruption of the tangential comparison map
flips it.

The declared chart group closes at 4 of 4 censused arenas. Its order is derived
by explicit closure of the generated permutation group of the site set, and
equals $\lvert X\rvert\cdot d!$ at every one.

The record lattice is translation-equivariant at 120969 of 120969 cells; the
scrambled lattice violates equivariance at 58572 of 120969, and breaks the
residual field's covariance at 128 cells. The scrambled lattice is the negative
control with teeth: it shows that the positive control is a measurement about
this lattice and not a tautology of the test. The covariance probe is run at a
rule-and-record pair whose residual is *not* identically zero, and the
non-vacuity count ships with every row.

---

## 8. The L-sweep

| $d$ | $L$ | scope | cells | closing | max $\lvert\rho\rvert$ | metric-reading | site-varying |
|---|---|---|---|---|---|---|---|
| 2 | 4 | BASE | 99 | 26 | 9 | 26 | 5 |
| 2 | 4 | TRANSLATES | 99 | 26 | 9 | 26 | 5 |
| 2 | 5 | BASE | 99 | 26 | 16 | 26 | 5 |
| 2 | 5 | TRANSLATES | 99 | 26 | 16 | 26 | 5 |
| 3 | 4 | BASE | 20 | 9 | 8 | 9 | 3 |
| 3 | 4 | TRANSLATES | 20 | 9 | 27 | 9 | 3 |
| 3 | 5 | BASE | 20 | 9 | 128/9 | 9 | 3 |
| 3 | 5 | TRANSLATES | 20 | 9 | 48 | 9 | 3 |

At fixed $d$ the closing-cell count and the coefficient-class census are
constant in $L$: the finding is not an artefact of one extent. What does move
along the sweep is the residual's *magnitude*, and the lapse coordinate moves it
too.

Enlarging the lapse family to its lattice translates moves the residual
MAGNITUDE at 62 of 476 census cells, and moves no cell's closure status and no
cell's coefficient class (0 moved). So the lapse family is a live coordinate for
the size of the anomaly and an inert one for its structure — measured on both
counts, which is why it is carried as a named verdict coordinate rather than a
convention.

---

## 9. The verdict

```
R3-DEFORMATION-DEFECT-AT<ARENA=…|L-GATE=…|RECOVERY=…|HH-BRACKET=…|
COEFFICIENT=…|HH-RESIDUAL=…|DH-BRACKET=…|DEFECT=…|CONVENTION=…|
DD-BRACKET=…|LAPSE=…|REALISATION=…|LSWEEP=…|CONTROLS=…>
```

The full string, with every segment's computed value, is emitted by the
instrument and carried in the receipt; it is compared character for character
against an independent reconstruction built from the receipt's own measured
rows, by a comparator that shares no code and no input with the builder.

**In words.** Two of the three hypersurface-deformation brackets are reproduced
on the record layer and one is not.

1. $\{H,H\}$ **closes**, into the tangential generator family, at every census
   cell, with an empty normal channel — and at the metric-inserted rule the
   coefficient extracted from the commutators *is* the record metric, and is
   **site-varying on the inhomogeneous records**. That is a structure function,
   and it is the programme's first relativity-shaped statement about the record
   layer.
2. $\{D,D\}$ **closes** exactly on the lattice's own translation generators.
3. $\{D,H\}$ **does not close.** Its front sector reproduces the transported
   lapse derivative exactly at one declared convention; its register sector lies
   outside the declared generator basis at every bracket, never vanishes, is not
   a boundary term, has no vanishing sector, and is independent of $L$ and $d$.

The honest head is therefore the defect head, and the defect is the deliverable:
a single, exactly characterised obstruction sitting in the register sector of
the normal-tangential bracket, with the other two brackets and the first
bracket's structure functions standing behind it.

---

## 10. Forced clauses, disclosed

Seven clauses of this unit follow from its own declarations without being
measured, and each ships as a disclosure carried at that label, with the
matching verdict segments saying `FORCED` in the emitted string:

| id | forced clause | what is measured instead |
|---|---|---|
| X01 | the $\{H,H\}$ landing and the empty normal channel | the coefficient; the residual channel |
| X02 | the D-REG normal-tangential identity | the D-TOT classification and the defect |
| X03 | the positive control's coefficient *value* | its uniqueness and its site-variation class |
| X04 | the $\{D,D\}$ closure at constant fields | the control's sensitivity — a mutant flips it |
| X05 | the arch-B cells' non-extractability | that the same solve succeeds at every arch-A cell |
| X06 | the $d=3$ inhomogeneous records are a declared extension | printed as arena data |
| X07 | the bracket census's $d=3$ lapse scope is I7's own probe convention | printed and gated, not a silent cap |

---

## 11. What this does not claim

The site-varying coefficient is measured **at the metric-inserted rule**, whose
weight is the record-read inverse metric by construction; what the extraction
adds is that the commutators themselves determine that coefficient uniquely
(the realised bracket covectors span fully at every site) and that it is a
metric reading rather than a constant — a distinction only the inhomogeneous
records can make, and only 32 of 120 inhomogeneous-record cells realise it.
Nothing here derives the metric from the record; I7's record-IS-metric result
already says the two are one datum in two coordinate systems.

The defect is a finite-extent statement. Whether it survives a refinement
direction is not asked, because R1's terminal leaves no legitimate refinement to
ask it in.

The tangential realisation is a **named verdict coordinate**: at D-REG the
bracket is trivial, at D-TOT it is nontrivial and outside the basis. Neither is
a bookkeeping choice, and the unit reports both.

---

## 12. The instrument

81 gates, all passed; 40 anchors; 60 mutants, all dead.
Every count is computed, never typed. The arena arrives through 7 file-byte
anchors and 32 (path, value) anchors, plus one anchor whose expected hash is
read out of the pinned receipt itself rather than written down. Two plain runs
are byte-identical. The falsification selftest re-invokes the instrument once
per mutant and requires exit 1, a named gate, an unchanged artifact pair and no
traceback.

The five R1 verdict-injection classes each ship as a mutant against this unit's
verdict gate, together with path-drift, L-gate violation, commutator-machinery
corruption (which flips the translation control), decomposition-basis drop,
coefficient-typing conflation, diagonal-anchor drift, lapse-family drop,
convention-sweep truncation, render-cell corruption, prose drift, and a
compliance claim with no gate behind it. Every compliance claim in the sweep
cites gates this run registered and that passed.
