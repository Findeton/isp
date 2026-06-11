# Relativistic ISP V3 Paper 22: Continuum Yang-Mills Confinement Continuation After The SEL2 Source Audit

Preprint, not peer reviewed, version 2026-05-28.

Author: Felix Robles Elvira

Status: completed continuation/source-audit ledger after Paper 21; handoff to
Paper 23.

Paper 22 is not a synthesis or summary paper.  It starts with the honest
status of the continuum Yang-Mills confinement program only to fix the import
contract.  Its job is to continue the work left by Paper 21: the common
finite inverse/admissibility ledger, the comparison source rows, the licensed
pass graph, and, if that finite-table route fails, a direct reduced-tail source
theorem.

## 0. Barandes-Aligned Boundary

The primitive object is the whole-process law of finite scalar records.  Gauge
fields, sheets, collars, root templates, Schwinger-Dyson rows, and polymers are
auxiliary representations used to compute scalar record inequalities.  Paper
22 does not import:

1. a Wilson-loop area law;
2. a mass gap;
3. an already-existing continuum Yang-Mills measure;
4. unrecorded gauge-fixed subprocesses;
5. off-record local Markov kernels;
6. an ontic flux-tube picture.

Every pass row, inverse slot, and tail estimate must be stated on the same
pushed-forward finite scalar law inherited from Papers 20 and 21.

### 0.1 Target Convention For Paper 22

Unless a later section explicitly declares a fixed low-rank target, Paper 22's
continuum Yang-Mills confinement target is:

```math
\text{one declared actual four-dimensional }SU(N)\text{ branch}
```

with \(N\) fixed before the final source and prefactor inequalities are
evaluated.  The target is **not** fixed to \(SU(4)\) by default.

The fundamental \(SU(4)\) channel \(F_4\) was introduced as the first active
low-rank test row because \(SU(2)\) and \(SU(3)\) fail the active tree-time
window, while \(SU(4)\) is the smallest fundamental row that passes the time
half.  Its later escape failure therefore falsifies the strict \(F_4\) route,
not the whole `4D SU(N)` continuation.

Consequently, switching from \(F_4\) to a declared \(F_N\) channel is a
legitimate alternate-channel branch for the `SU(N)` program, provided the
branch is frozen before the estimates are evaluated and all records are read
from the corresponding pushed-forward finite scalar law.  If a future target
is declared to be fixed low-rank \(SU(4)\), then that target declaration
overrides this convention and Branch A is disallowed.

## 1. Current Status Toward Continuum Yang-Mills Confinement

### 1.1 Closed Or Frozen Inputs

The following items are closed at the level needed for this continuation.

1. **Finite/projective gauge scaffolding.**  Papers 9 and 10 give finite
   non-Abelian gauge-sector records and projective gauge-continuum scaffolding.
   They do not prove a continuum Yang-Mills measure or confinement.

2. **RG and loop-readout scaffolding.**  Papers 11 and 12 export finite-battery
   RG residual, trajectory, covariance/readout, and renormalized loop-control
   ledgers.  They do not export the `SEL2` tree-time or escape source.

3. **Conditional confinement architecture.**  Papers 13--19 build the
   finite-block, surface-polymer, continuum-closure, mass-gap, confinement,
   and actual-source-constant architecture.  The architecture is conditional:
   it identifies the source constants and debits that must pass, without
   importing the conclusion.

4. **Paper-20 strict scalar reduction.**  On the strict exact reduced `SEL2`
   branch, Paper 20 closes the coefficient-normalization audit, the
   one-plaquette/surface dimension-cancellation identity, the interior
   `GENMATCH` root cancellation, the boundary/collar scalar census, and the
   strict five-term scalar coefficient comparison:

   ```math
   \mathrm{P20\text{-}SEL2\text{-}4DCOEFF\text{-}CLOSE}
   (\epsilon_{\rho,j}),
   \qquad
   \epsilon_{\rho,j}\to0.
   ```

   Paper 20 still parks the source gate

   ```math
   \mathrm{P20\text{-}SEL2\text{-}TREE\text{-}RATE\text{-}GATE}
   =
   \mathrm{P20\text{-}SEL2\text{-}TREE\text{-}TIME}(\rho)
   +
   \mathrm{P20\text{-}SEL2\text{-}ESC\text{-}MASS}
   (V_\rho,\gamma_\rho,q_\rho).
   ```

5. **Paper-21 finite source audit.**  Paper 21 prints the structural row maps

   ```math
   R_{fus}^{99,+},\qquad
   R_{act}^{99,+},\qquad
   R_{SD}^{99,+},\qquad
   R_{cmp}^{99,+},
   ```

   and proves that, on the current corpus, the licensed pass graph is empty:

   ```math
   \mathcal E_{pass}^{108,current}=\varnothing.
   ```

6. **`SDSRC+` and `ACTSRC+` are settled for the present corpus.**  Paper 21
   reduces `SDSRC+` to a projected multiplier envelope and same-shell inverse
   problem, with projected envelope \(A_{SD,proj}\le8\) under the minimal
   retained-word convention.  It reduces `ACTSRC+` to a closed finite envelope
   plus inverse/admissibility data:

   ```math
   \log A_{act,pass}
   \le
   \log^+(B_{act}^{110}C_v^{YM2,min})+36.31
   ```

   after `ACTINV` and admissibility/zero-carry tags are supplied.

### 1.2 Still Open At The Start Of Paper 22

The open gates are now precise.

1. **Common inverse/admissibility.**

   ```math
   \mathrm{PARK\text{-}COMMON\text{-}INV/ADM}^{+}
   ```

   The same-shell inverse and admissibility rows needed by `ACTSRC+`,
   `SDSRC+`, and `CMPSRC+` are not printed by the current papers.

2. **Comparison source rows.**

   ```math
   \mathrm{PARK\text{-}CMPSRC}^{+}
   ```

   Paper 21 prints the structural comparison row map but not its values,
   inverse slots, or zero/carry tags.

3. **Licensed pass graph.**  The carried graph is known, but no actual
   support-growing pass rows are licensed on the present corpus.  The SCC,
   coverage, and one-step KP computations must be rerun only after the source
   rows are supplied.

4. **Reduced-tail exponent.**  The program still lacks a same-record theorem
   proving either

   ```math
   \mathrm{P21\text{-}RED\text{-}DPT}_{prim}(m_{red}^{act})
   ```

   with a positive usable exponent, or the shell version

   ```math
   \mathrm{P21\text{-}RED\text{-}DPT}_{shell}(\delta),
   \qquad \delta>0.
   ```

5. **Tree-rate/pass inequality.**  Even after a reduced pass graph is printed,
   the final confinement branch needs the strict rate/source inequality
   inherited from Paper 20.  Without it, continuum Yang-Mills confinement is
   not proved.

6. **Unconditional continuum YM confinement and mass gap.**  These remain open.
   Papers 17--21 give conditional reductions and source audits, not an
   unconditional Clay-level theorem.

## 2. Paper-22 Main Problem

Paper 22 targets the next source theorem:

```math
\mathrm{P22\text{-}RED\text{-}PASSGRAPH\text{-}CLOSE}.
```

This theorem holds when the strict `SEL2` scalar branch admits a nonempty
licensed reduced pass graph with computable coefficients, inverse slots,
zero/carry tags, and SCC/coverage data strong enough to test reduced decay.

If the pass graph cannot be licensed, Paper 22 must instead prove the
negative continuation theorem:

```math
\mathrm{P22\text{-}FINITE\text{-}TABLE\text{-}ROUTE\text{-}PARK}.
```

That theorem says the current finite-table route is parked at explicit missing
source tables and must be replaced by a direct reduced-tail theorem.

## 3. Import Contract From Paper 21

Paper 22 imports exactly:

```math
\mathcal U_{99}^{vert},\quad
R_{fus}^{99,+},\quad
R_{act}^{99,+},\quad
R_{SD}^{99,+},\quad
R_{cmp}^{99,+},
```

the carried finite table of Section 108, and the final export ledger of Paper
21 Section 130.  It does not reopen the scalar identities already settled in
Papers 20 and 21 unless it changes the branch conventions.  If it changes the
branch conventions, it must re-run:

```math
\mathrm{P20\text{-}SEL2\text{-}4DCOEFF\text{-}CLOSE},
\qquad
\mathrm{P21\text{-}ACTSRC}^{+},
\qquad
\mathrm{P21\text{-}SDSRC}^{+}.
```

## 4. Work Package I: Common Inverse And Admissibility

Define a common finite certificate

```math
\mathrm{P22\text{-}COMMON\text{-}INVADM}^{+}
```

consisting of:

```math
\mathcal O_{act}^{99,+},\qquad
\mathcal O_{SD}^{99,+},\qquad
\mathcal O_{cmp}^{99,+},
```

and tags

```math
\mathrm{Adm}_{act},\qquad
\mathrm{Adm}_{SD},\qquad
\mathrm{Adm}_{cmp},
\qquad
\mathrm{ZC}_{act},\qquad
\mathrm{ZC}_{SD},\qquad
\mathrm{ZC}_{cmp}.
```

The certificate must satisfy three nonnegotiable rules.

1. **Same-record rule.**  Each inverse is evaluated under the same scalar
   pushed-forward law used by the corresponding row value.

2. **No-double-charge rule.**  A row assigned to `CMSSI`, `BTQ`, representation
   tail, product tail, readout/covariance transport, or a carried finite
   ledger is not also counted as a reduced escaping pass row.

3. **Finite-shell rule.**  Same-shell inverse slots may use only the finite
   row battery and the printed vertex cover.  They may not import continuum
   compactness or an unrecorded infinite-volume inverse.

### Theorem Target 4.1: Common Inverse Closure

If `P22-COMMON-INVADM+` is printed, then the Paper-21 conditional pass gates
for `ACTSRC+` and `SDSRC+` become executable finite row sets.  If it is not
printed, Paper 22 must keep both packages parked no matter how sharp their
coefficient envelopes are.

## 5. Work Package II: `CMPSRC+`

The comparison source is the main unfinished source bucket:

```math
\mathrm{PARK\text{-}CMPSRC}^{+}.
```

Paper 22 must split it as

```math
\mathrm{CMPSRC}^{+}
=
\mathrm{CMPVAL}^{+}
+\mathrm{CMPINV}^{+}
+\mathrm{CMPADM/ZC}^{+}
+\mathrm{CMP\text{-}NODC}^{+}.
```

The last term is the no-double-charge audit: comparison rows cannot repay a
defect already assigned to Paper-16 projective/covariance tails, Paper-12
readout/de-smearing, Paper-20 scalar correction terms, `CMSSI`, or `BTQ`.

### Theorem Target 5.1: Comparison Source Closure

Either prove

```math
\mathrm{P22\text{-}CMPSRC\text{-}CLOSE}^{+}
```

by printing all four components above, or prove the honest parked status

```math
\mathrm{P22\text{-}CMPSRC\text{-}PARK}^{+}
```

with the exact missing finite tables named.

## 6. Work Package III: Rebuild The Licensed Pass Graph

After Work Packages I and II, define the licensed pass set

```math
\mathcal E_{pass}^{22}
=
\mathcal E_{fus,pass}^{22}
\cup
\mathcal E_{act,pass}^{22}
\cup
\mathcal E_{SD,pass}^{22}
\cup
\mathcal E_{cmp,pass}^{22},
```

where a row is included only if its value, inverse, admissibility, and
zero/carry tags are supplied and it is not assigned to a non-decay ledger.

Then rerun:

1. zero-growth SCC classification;
2. reduced coverage;
3. degree-tail surcharge;
4. battery-growth surcharge;
5. one-step KP constant extraction;
6. reduced primitive or shell-tail inequality.

The first numerical inequality to test is the Paper-21 reduced gate

```math
m_{red}^{act}
>
\log A_{esc}^{BTQ}
+\log C_{geom}^{red}
+g_q^{red}.
```

If the pass graph is empty, the inequality is not false; it is unevaluable.

## 7. Work Package IV: Direct Reduced-Tail Source

If the finite pass graph remains empty or too expensive, Paper 22 should stop
trying to buy decay row by row and prove a direct theorem:

```math
\mathrm{P22\text{-}RED\text{-}TAIL\text{-}DIRECT}.
```

Allowed routes:

1. a Paper-16-to-Paper-21 transfer proving `P21-RED-1KP` on the same scalar
   law;
2. a shell-tail theorem proving `P21-RED-DPT_shell(delta)` with \(\delta>0\);
3. a finite-battery BLU theorem proving that all carried comparison/action/SD
   source defects are dominated by a single scalar contraction;
4. a selector theorem removing the unbounded support-growing family before the
   KP fit is attempted.

Forbidden routes:

1. assuming a Wilson-loop area law;
2. assuming confinement or a mass gap;
3. importing continuum Yang-Mills existence as a measure-theoretic premise;
4. replacing finite scalar records by unrecorded field configurations.

Section 14 below shows that Work Package IV is not needed on the strict
row-complete envelope branch: the licensed graph has finite maximum depth.  It
remains the correct fallback only if a later branch rejects the strict envelope
or row-complete finite-battery conventions.

## 8. Decision Outcomes

Paper 22 has four honest outcomes.

1. **Finite-table pass.**  `COMMON-INVADM`, `CMPSRC+`, and the licensed pass
   graph close; the reduced inequality passes.  Then Paper 22 exports a
   genuine source theorem back to the Paper-20/Paper-21 tree-rate chain.

2. **Finite-table failure.**  The licensed graph closes and the reduced
   inequality fails.  This falsifies the strict finite-table branch, not every
   possible confinement strategy.

3. **Finite-table park.**  The licensed graph or reduced tail theorem remains
   unprinted.  Before Section 13 this also included comparison values; after
   Work Package II, comparison values are closed by a same-record envelope and
   no longer form an independent park condition.

4. **Direct-tail continuation.**  The finite-table route is bypassed by
   `P22-RED-TAIL-DIRECT`.  Then the source work moves from row enumeration to
   analytic reduced decay.

Section 14 realizes the first outcome on the strict row-complete envelope
branch, with finite-depth reduced-tail closure rather than an all-depth
one-step KP inequality.

## 9. Immediate Execution Order

At the start of Paper 22, the execution order is:

1. freeze the Paper-21 Section-130 import ledger as the only Paper-22 input;
2. print `P22-COMMON-INVADM+` or prove exactly why the current papers cannot
   supply it;
3. close or park `CMPSRC+` with row values, inverse slots, admissibility, and
   no-double-charge tags;
4. rebuild the licensed pass graph and rerun SCC/coverage on that graph;
5. compute the reduced constants only after the graph is licensed;
6. if the graph is empty or the inequality cannot survive, switch to
   `P22-RED-TAIL-DIRECT`.

Section 11 completes item 2 by a row-complete finite scalar-record quotient
construction.  Section 13 completes item 3 by a same-record comparison-envelope
source package.  Section 14 completes items 4 and 5: the licensed pass graph is
rebuilt and the support-cardinality rank gives finite-depth reduced-tail
closure.  Thus item 6 is not needed on the strict row-complete envelope branch.

## 10. Current Bottom Line

The continuum Yang-Mills confinement task is not closed.  What is closed is a
large amount of the reduction machinery: finite/projective gauge records,
loop-readout scaffolding, scalar coefficient normalization, strict local
source cancellations, structural row maps, and finite envelopes for `SDSRC+`
and `ACTSRC+`, plus the same-record comparison envelope closing `CMPSRC+`.

After Work Packages I--III, the Paper-22 finite-table obstruction is closed on
the strict row-complete envelope branch.  The remaining live problem is now
upstream of Paper 22:

```math
\boxed{
\mathrm{P20\text{-}SEL2\text{-}TREE\text{-}RATE\text{-}GATE}
\quad\text{and the surface prefactor comparison.}
}
```

Section 15 freezes this upstream problem as a scalar worksheet: `TREE-TIME` is
the selector-time trichotomy, and `ESC-MASS` is a near-maximal fixed-set
anti-concentration demand at the current rooted tree threshold.

That is the next continuation after the Paper-22 source/pass-graph closure.

## 11. Work Package I Closure: Common Finite Inverse/Admissibility

This section closes Work Package I.  The previous papers did not print the
Section-99/104/106/107 inverse slots, but Paper 22 can define and certify them
directly on the finite row universe that Paper 21 already printed.  The
construction is a finite scalar-record quotient construction.  It is not a
continuum inverse, not a gauge-coordinate inverse, and not a hidden
conditioning kernel.

The goal is to replace the symbolic obstruction

```math
\mathrm{PARK\text{-}COMMON\text{-}INV/ADM}^{+}
```

by a closed finite certificate

```math
\mathrm{P22\text{-}COMMON\text{-}INVADM}^{+}.
```

### Definition 11.1: The Common Finite Row Universe

Let

```math
\mathcal U_{22}^{row}
:=
\mathcal U_{99}^{vert}
\times
\left(
\Xi_{act}^{99,+}
\sqcup
\Xi_{SD}^{99,+}
\sqcup
\Xi_{cmp}^{99,+}
\right)
```

restricted to rows on which the corresponding structural row map is defined:

```math
R_{act}^{99,+},\qquad
R_{SD}^{99,+},\qquad
R_{cmp}^{99,+}.
```

The fusion rows are not included in the inverse-source problem because Paper
21 assigns the retained fusion rows to the finite channel/`CMSSI` ledger on
the strict branch.  A later branch may add them, but then it must enlarge
\(\mathcal U_{22}^{row}\) explicitly.

Each row \(e\in\mathcal U_{22}^{row}\) has:

```math
s(e),\quad t(e),\quad c(e)\in\{act,SD,cmp\},\quad
\Delta_X(e),\quad \Delta_C(e),\quad \Delta_h(e),\quad \Delta_p(e),
```

all inherited from Paper 21.  Rows already assigned by Paper 21 to product
tail, representation tail, lower-shell retraction, internal `BTQ`, internal
comparison battery, or exact structural zero remain outside the inverse-pass
candidate set.

### Definition 11.2: Finite Scalar Quotient Space

For the active strict `SEL2` law at row scale \(j\), let
\(\mathcal R_{22,j}\) be the finite real vector space spanned by the scalar
record functions appearing in the source and target vertices of
\(\mathcal U_{22}^{row}\).  The span includes the character, trace-word,
frontier, retained-channel, and finite comparison-battery records printed in
Paper 21.

Define the finite same-record Gram form

```math
G_{22,j}(F,H)
:=
\mathbb E_{\mu_j^{SEL2}}\!\left[
(F-\mathbb E_{\mu_j^{SEL2}}F)
(H-\mathbb E_{\mu_j^{SEL2}}H)
\right].
```

Let

```math
\mathcal N_{22,j}
:=
\{F\in\mathcal R_{22,j}:G_{22,j}(F,F)=0\}
```

and define the finite quotient Hilbert space

```math
\mathcal H_{22,j}:=
\mathcal R_{22,j}/\mathcal N_{22,j}.
```

All exact trace identities, cyclic symmetries, inverse-pairing identities,
determinant-one reductions, Cayley-Hamilton reductions, and covariance-null
relations are absorbed into \(\mathcal N_{22,j}\).  Thus a null vector is not
a small error.  It is the same scalar record.

### Definition 11.3: Shell Blocks And Response Matrices

For each class \(c\in\{act,SD,cmp\}\) and each finite shell label
\(\sigma\), let \(\mathcal U_{22}^{c,\sigma}\subset\mathcal U_{22}^{row}\)
be the rows of class \(c\) whose source and target records lie in the same
declared finite shell block after removing rows already assigned to a tail,
internal `BTQ`, internal comparison battery, lower-shell retraction, or exact
zero ledger.

Let \(\mathcal K_{22}^{c,\sigma}\) be the finite coordinate space with basis
\([e]\) for \(e\in\mathcal U_{22}^{c,\sigma}\).  Define the finite response
map

```math
M_{22,j}^{c,\sigma}:\mathcal K_{22}^{c,\sigma}\to\mathcal H_{22,j}
```

by

```math
M_{22,j}^{c,\sigma}[e]
:=
\pi_{22,j}\bigl(T_e-S_e\bigr),
```

where \(S_e\) and \(T_e\) are the source and target scalar record functions
of the row and \(\pi_{22,j}:\mathcal R_{22,j}\to\mathcal H_{22,j}\) is the
quotient map.

This is the canonical finite response matrix for the printed row universe.
It is allowed because every entry is an expectation of finite scalar records
under the same pushed-forward law \(\mu_j^{SEL2}\).

The convention for Work Package I is the **row-complete finite battery**: once
a row survives the Paper-21 deletions and the no-double-charge filters, its own
finite scalar difference column is available as a same-shell battery generator.
This does not prove a source coefficient.  It only says that the inverse slot is
finite and same-record.  If a later branch insists on a smaller generator
battery, it must replace \(\mathcal K_{22}^{c,\sigma}\) by that subspace and
rerun the range test below.

### Definition 11.4: Canonical Same-Shell Right Inverse

Let

```math
Q_{22,j}^{c,\sigma}
:=
\left(M_{22,j}^{c,\sigma}\right)^\dagger
```

be the Moore-Penrose pseudoinverse on
\(\mathrm{Ran}(M_{22,j}^{c,\sigma})\), computed in the finite quotient
\(\mathcal H_{22,j}\).  Equivalently, after choosing any orthonormal basis of
\(\mathcal H_{22,j}\), \(Q_{22,j}^{c,\sigma}\) is the ordinary finite
pseudoinverse of the matrix of \(M_{22,j}^{c,\sigma}\).

For \(e\in\mathcal U_{22}^{c,\sigma}\), define

```math
b_{22,j}(e):=M_{22,j}^{c,\sigma}[e].
```

The row is inverse-admissible when

```math
b_{22,j}(e)\in\mathrm{Ran}(M_{22,j}^{c,\sigma})
```

and the no-double-charge filters of Definition 11.6 below pass.  In that case
define

```math
\mathcal O_{22,j}^{c}(e)
:=
\inf\left\{
\|x\|_{\ell^1(\mathcal K_{22}^{c,\sigma})}:
M_{22,j}^{c,\sigma}x=b_{22,j}(e)
\right\}.
```

If \(b_{22,j}(e)=0\), set \(\mathcal O_{22,j}^{c}(e)=0\) and mark the row
`zero` in the inverse ledger.  If \(b_{22,j}(e)\notin
\mathrm{Ran}(M_{22,j}^{c,\sigma})\), the row is not pass-admissible and is
sent to the carried inverse ledger.  Under the row-complete finite battery this
range failure cannot occur for a surviving row, because the coordinate vector
\([e]\) is already a witness:

```math
M_{22,j}^{c,\sigma}[e]=b_{22,j}(e).
```

Hence every nonzero surviving row has the sharp finite inverse bound

```math
\mathcal O_{22,j}^{c}(e)\le1.
```

### Lemma 11.5: Finite Pseudoinverse Legality

For every fixed row scale \(j\), class \(c\), and shell block \(\sigma\),
\(Q_{22,j}^{c,\sigma}\) exists as a finite matrix.  Moreover every
inverse-admissible row has finite \(\mathcal O_{22,j}^{c}(e)\), and under the
row-complete finite battery every nonzero surviving row satisfies
\(\mathcal O_{22,j}^{c}(e)\le1\).

Proof.  The row universe is finite by Paper 21 Sections 99--108 and the fixed
over-refined vertex cover.  Hence \(\mathcal K_{22}^{c,\sigma}\) is finite
dimensional.  The record span \(\mathcal R_{22,j}\) is finite dimensional, and
quotienting by \(\mathcal N_{22,j}\) gives a finite Hilbert space.  Therefore
\(M_{22,j}^{c,\sigma}\) is a finite matrix.  Every finite matrix has a
Moore-Penrose pseudoinverse on its range.  The infimum defining
\(\mathcal O_{22,j}^{c}(e)\) is over a nonempty finite-dimensional affine set
for every admissible row, so it is finite.  Under the row-complete convention
the single-coordinate vector \([e]\) is an admissible solution, giving
\(\mathcal O_{22,j}^{c}(e)\le\|[e]\|_1=1\). `square`

### Definition 11.6: Common Admissibility And Zero/Carry Tags

For every row \(e\in\mathcal U_{22}^{row}\), define

```math
\mathrm{Adm}_{22}(e)\in\{0,1\},
\qquad
\mathrm{ZC}_{22}(e)\in
\{\mathrm{zero},\mathrm{pass\text{-}eligible},
\mathrm{CMSSI},\mathrm{BTQ},\mathrm{cmpbat},
\mathrm{tail},\mathrm{carry}\}.
```

The tag is assigned by the following finite decision tree.

1. If Paper 21 already assigns \(e\) to representation tail, product tail,
   degree tail, lower-shell retraction, or an off-record comparison, then
   \(\mathrm{Adm}_{22}(e)=0\) and \(\mathrm{ZC}_{22}(e)=\mathrm{tail}\).

2. If Paper 21 assigns \(e\) to internal `BTQ`, then
   \(\mathrm{Adm}_{22}(e)=0\) and \(\mathrm{ZC}_{22}(e)=\mathrm{BTQ}\).

3. If Paper 21 assigns \(e\) to the internal common comparison battery, then
   \(\mathrm{Adm}_{22}(e)=0\) and \(\mathrm{ZC}_{22}(e)=\mathrm{cmpbat}\).

4. If \(b_{22,j}(e)=0\) in \(\mathcal H_{22,j}\), then
   \(\mathrm{Adm}_{22}(e)=0\) and \(\mathrm{ZC}_{22}(e)=\mathrm{zero}\).

5. If a later narrower battery is used and
   \(b_{22,j}(e)\notin\mathrm{Ran}(M_{22,j}^{c,\sigma})\), then
   \(\mathrm{Adm}_{22}(e)=0\) and \(\mathrm{ZC}_{22}(e)=\mathrm{carry}\).

6. If the row duplicates a debit already assigned to `ACTSRC`, `SDSRC`,
   `CMPSRC`, `CMSSI`, `BTQ`, representation tail, product tail, Paper-12
   readout/de-smearing, Paper-16 RP/Cov transport, Paper-20 scalar
   coefficient correction, `RPF`, `KPdec`, or `WP`, then
   \(\mathrm{Adm}_{22}(e)=0\) and \(\mathrm{ZC}_{22}(e)=\mathrm{carry}\).

7. If \(\Delta_X(e)=0\), the row is same-shell bookkeeping:
   \(\mathrm{Adm}_{22}(e)=0\) and
   \(\mathrm{ZC}_{22}(e)=\mathrm{CMSSI}\), with inverse contribution
   \(\mathcal O_{22,j}^{c}(e)\) assigned to the same-shell inverse ledger.

8. Otherwise \(\mathrm{Adm}_{22}(e)=1\) and
   \(\mathrm{ZC}_{22}(e)=\mathrm{pass\text{-}eligible}\).

This decision tree is part of the certificate.  It does not provide missing
source coefficients.  It only decides whether a row has a legitimate
same-record inverse/admissibility slot.

### Lemma 11.7: The Decision Tree Partitions The Row Universe

Every row \(e\in\mathcal U_{22}^{row}\) receives exactly one
\(\mathrm{ZC}_{22}\) tag.

Proof.  The tests are ordered.  Paper-21 structural deletions are checked
first, then quotient-zero, range failure, no-double-charge failure,
same-shell bookkeeping, and finally pass eligibility.  Each test is a
finite predicate on \(e\), and once one predicate succeeds the decision tree
stops.  Hence every row receives at least one tag and no row receives two.
`square`

### Definition 11.8: The Common Inverse Certificate

The common inverse/admissibility certificate is

```math
\mathfrak I_{22}^{common}
:=
\left(
\mathcal U_{22}^{row},
\{Q_{22,j}^{c,\sigma}\}_{c,\sigma},
\mathcal O_{22,j}^{c},
\mathrm{Adm}_{22},
\mathrm{ZC}_{22}
\right).
```

It induces the classwise certificates

```math
\mathrm{ACTINV}_{22}
:=
\left\{
\mathcal O_{22,j}^{act}(e),\mathrm{Adm}_{22}(e),\mathrm{ZC}_{22}(e):
c(e)=act
\right\},
```

```math
\mathrm{SDINV}_{22}
:=
\left\{
\mathcal O_{22,j}^{SD}(e),\mathrm{Adm}_{22}(e),\mathrm{ZC}_{22}(e):
c(e)=SD
\right\},
```

and

```math
\mathrm{CMPINV}_{22}
:=
\left\{
\mathcal O_{22,j}^{cmp}(e),\mathrm{Adm}_{22}(e),\mathrm{ZC}_{22}(e):
c(e)=cmp
\right\}.
```

### Theorem 11.9: `P22-COMMON-INVADM+` Is Closed

On the strict Paper-21 import branch, the common finite inverse/admissibility
certificate exists and is finite:

```math
\boxed{
\mathrm{P22\text{-}COMMON\text{-}INVADM}^{+}.
}
```

In particular, the previous inverse placeholders are discharged by the
canonical finite quotient construction:

```math
\boxed{
\mathrm{ACTINV}_{128}\leadsto\mathrm{ACTINV}_{22},
\qquad
\mathrm{SDINV}_{124}\leadsto\mathrm{SDINV}_{22},
\qquad
\mathrm{CMPINV}\leadsto\mathrm{CMPINV}_{22}.
}
```

Rows failing the finite quotient range test, the no-double-charge test, or
the same-shell/support-growth test are not made into pass rows.  They are
zero, `CMSSI`, `BTQ`, `cmpbat`, tail, or carry rows according to
Definition 11.6.

With the row-complete finite battery, the inverse surcharge of every surviving
nonzero row is bounded by one:

```math
\boxed{
\mathcal O_{22,j}^{c}(e)\le1.
}
```

Thus `COMMON-INVADM+` is no longer a large-constant obstruction.  It is a
finite mask plus a unit-normalized inverse slot.  The remaining obstruction is
whether the surviving rows have usable source values and produce a reduced
decay graph.

Proof.  Definition 11.1 gives a finite row universe from the printed Paper-21
row maps.  Definition 11.2 constructs the finite same-record scalar quotient.
Definition 11.3 constructs finite response matrices, and Definition 11.4
constructs their finite pseudoinverses.  Lemma 11.5 proves finiteness of every
admissible inverse slot.  Definition 11.6 supplies the common admissibility
and zero/carry tags, and Lemma 11.7 proves the decision tree is exhaustive and
exclusive.  Thus the certificate of Definition 11.8 is a finite same-record
object. `square`

### Corollary 11.10: No Remaining Literal Inverse Table

There is no further mathematical inverse/admissibility table to source for
Work Package I.  The literal table is the finite evaluation of Definition 11.6
on the printed Paper-21 row universe:

```math
e\longmapsto
\left(
\mathcal O_{22,j}^{c(e)}(e),
\mathrm{Adm}_{22}(e),
\mathrm{ZC}_{22}(e)
\right).
```

Rows tagged `zero`, `CMSSI`, `BTQ`, `cmpbat`, `tail`, or `carry` are not
support-growing pass rows.  Rows tagged `pass-eligible` have
\(\mathcal O_{22,j}^{c(e)}(e)\le1\).  Expanding this map row by row would be a
typographical expansion of the already printed Paper-21 finite cover, not a new
source theorem.  Work Package I is therefore closed on the row-complete
finite-battery branch.

## 12. Consequences For The Source Ledgers

The closure of Work Package I removes one obstruction but not all of them.
This section states exactly what changes.

### Corollary 12.1: Updated `ACTSRC+` Status

On the strict envelope route of Paper 21 Theorem 129.1, the action source no
longer parks at a missing inverse/admissibility package.  Its support-growing
pass-eligible rows are

```math
\mathcal E_{act,\Delta}^{22,elig}
:=
\left\{
e\in\mathcal U_{22}^{row}:
c(e)=act,\ \Delta_X(e)\ge1,\ \mathrm{Adm}_{22}(e)=1
\right\}.
```

Their coefficient base is still bounded by the Paper-21 envelope:

```math
A_{act,elig}^{22}
\le
\max\left(
1,\,
B_{act}^{110}\Pi_{act}^{113,mon}C_v^{YM2,min}
\right),
```

and with \(n_A^{113}\le408\),

```math
\log A_{act,elig}^{22}
\le
\log^+\!\left(B_{act}^{110}C_v^{YM2,min}\right)+36.31.
```

The literal signed route remains optional and still requires
`DTENS/COVPAIR/ROWVAL-LIT` if one wants exact row values instead of the
envelope.

### Corollary 12.2: Updated `SDSRC+` Status

Under the minimal retained-word projection convention of Paper 21 Section
123, the support-growing `SDdiv/loop` survivors now have both:

1. the projected coefficient envelope

   ```math
   A_{SD,proj}^{22}\le8;
   ```

2. the finite inverse/admissibility tags from
   \(\mathrm{SDINV}_{22}\).

Thus the remaining `SDSRC+` obstruction is not inverse/admissibility.  It is
only whether the strict branch adopts the minimal retained-word projection
convention.  If it does, the `SD` pass-eligible set is

```math
\mathcal E_{SD,\Delta}^{22,elig}
:=
\left\{
e\in\mathcal U_{22}^{row}:
c(e)=SD,\ \Delta_X(e)\ge1,\ \mathrm{Adm}_{22}(e)=1
\right\}.
```

If that projection convention is rejected, restore the finite projected
multiplier table as the named obstruction.

### Corollary 12.3: Updated `CMPSRC+` Status

The comparison inverse and admissibility part is closed:

```math
\mathrm{CMPINV}^{+}+\mathrm{CMPADM/ZC}^{+}
\quad\text{is supplied by}\quad
\mathrm{CMPINV}_{22}.
```

The comparison source is now reduced to the coefficient/value and
no-double-charge audit

```math
\boxed{
\mathrm{CMPSRC}^{+}
=
\mathrm{CMPVAL}^{+}
+\mathrm{CMP\text{-}NODC}^{+}.
}
```

The no-double-charge half is already encoded as a finite admissibility mask in
Definition 11.6.  What remains for Work Package II is therefore the literal or
envelope comparison coefficient table:

```math
\mathrm{CMPVAL}^{+}.
```

### Corollary 12.4: Updated Paper-22 Live Obstruction

After Work Package I, the live Paper-22 obstruction is

```math
\boxed{
\mathrm{PARK\text{-}CMPVAL}^{+}
\quad+\quad
\mathrm{PARK\text{-}RED\text{-}TAIL}^{+}.
}
```

If the strict branch adopts the minimal `SD` projection convention and the
action envelope route, `ACTSRC+` and `SDSRC+` are no longer blocked by
inverse/admissibility.  The next finite-table task is `CMPVAL+`; after that,
the licensed pass graph can be rebuilt and the reduced-tail inequality can be
tested.

Section 13 below closes this Work-I comparison-value obstruction by a finite
same-record envelope.  Thus this paragraph is the Work-I handoff, not the final
Paper-22 live obstruction.

This closes Work Package I.

## 13. Work Package II Closure: `CMPSRC+`

This section closes Work Package II on the strict row-complete, same-record
envelope branch.  Paper 21 printed the structural comparison row map
\(R_{cmp}^{99,+}\), but parked the comparison source package because it did not
print finite row values, inverse slots, or zero/carry tags.  Section 11 has now
supplied the inverse/admissibility and zero/carry part.  The only remaining
piece is therefore

```math
\mathrm{CMPVAL}^{+}.
```

The closure below is deliberately an **envelope closure**, not a signed
coefficient-table closure.  It supplies the finite nonnegative majorants needed
to rebuild the licensed pass graph.  It does not claim cancellation, decay, a
Wilson-loop area law, a mass gap, or an existing continuum Yang-Mills measure.

### Definition 13.1: Comparison Survivor Set

Let the Work-I admissibility mask be the one from Definition 11.6.  The
support-growing comparison rows eligible for the pass graph are

```math
\mathcal E_{cmp,\Delta}^{22,elig}
:=
\left\{
e\in\mathcal U_{22}^{row}:
c(e)=cmp,\ \Delta_X(e)\ge1,\ \mathrm{Adm}_{22}(e)=1
\right\}.
```

The non-pass comparison rows are partitioned by the same finite mask:

```math
\mathcal E_{cmp}^{22,zero},\quad
\mathcal E_{cmp}^{22,CMSSI},\quad
\mathcal E_{cmp}^{22,cmpbat},\quad
\mathcal E_{cmp}^{22,tail},\quad
\mathcal E_{cmp}^{22,carry}.
```

These are not new source rows.  They are exactly the comparison rows already
classified by Paper 21 Table 107.5 and the Work-I no-double-charge decision
tree.

### Definition 13.2: Same-Record Comparison Value Envelope

For a comparison row \(e\), let \(S_e,T_e\in\mathcal R_{22,j}\) be its source
and target scalar record functions as in Definition 11.3.  Define the raw
same-record comparison majorant

```math
a_{cmp,raw}^{22}(e)
:=
\|T_e-S_e\|_{L^\infty(\mu_j^{SEL2})}.
```

Equivalently, since the row functions are continuous finite scalar records on a
compact finite gauge battery, this is the supremum of \(|T_e-S_e|\) over the
declared finite endpoint record space.  It is independent of any unobserved
subprocess.

Define

```math
B_{cmp,rec}^{22}
:=
\max_{e\in\mathcal U_{22}^{row},\,c(e)=cmp}
\max\left(\|S_e\|_\infty,\|T_e\|_\infty\right).
```

If the comparison row set is empty, set \(B_{cmp,rec}^{22}=1\); then all
comparison pass maxima below are empty-set conventions.

Then

```math
a_{cmp,raw}^{22}(e)\le2B_{cmp,rec}^{22}.
```

On the strict unit-normalized scalar-record convention, where every retained
character/trace/product coordinate has been normalized to have sup norm at most
one,

```math
B_{cmp,rec}^{22}\le1,
\qquad
a_{cmp,raw}^{22}(e)\le2.
```

If source or target normal forms are inserted, set

```math
a_{cmp}^{22}(e)
:=
B_{cmp,s}^{22}(e)B_{cmp,t}^{22}(e)a_{cmp,raw}^{22}(e).
```

For the finite comparison row set, define the global normal-form envelopes

```math
B_{cmp,s}^{22}
:=
\max_{e\in\mathcal U_{22}^{row},\,c(e)=cmp}B_{cmp,s}^{22}(e),
\qquad
B_{cmp,t}^{22}
:=
\max_{e\in\mathcal U_{22}^{row},\,c(e)=cmp}B_{cmp,t}^{22}(e).
```

If there are no comparison rows, both global normal-form envelopes are set to
one by convention.

On the strict no-extra-normal-form branch,
\(B_{cmp,s}^{22}=B_{cmp,t}^{22}=1\).

### Lemma 13.3: The Comparison Envelope Is Same-Record And Finite

For every comparison row \(e\), \(a_{cmp}^{22}(e)\) is finite.  On the strict
unit-normalized no-extra-normal-form branch,

```math
A_{cmp,pass}^{22}
:=
\max_{e\in\mathcal E_{cmp,\Delta}^{22,elig}}
\max(1,a_{cmp}^{22}(e))
\le2,
```

with the convention \(A_{cmp,pass}^{22}=1\) if
\(\mathcal E_{cmp,\Delta}^{22,elig}=\varnothing\).

Proof.  Paper 21 Definition 107.1 makes the comparison atom set finite, and
Section 11 restricts to a finite row universe.  Each \(S_e,T_e\) is a finite
scalar gauge record on the same pushed-forward `SEL2` law.  The finite endpoint
spaces are compact and the retained scalar records are bounded continuous
functions, so \(B_{cmp,rec}^{22}<\infty\) and
\(\|T_e-S_e\|_\infty\le2B_{cmp,rec}^{22}\).  The strict unit-normalized
convention gives \(B_{cmp,rec}^{22}\le1\).  Taking the maximum over the finite
eligible set gives the displayed \(A_{cmp,pass}^{22}\) bound. `square`

### Definition 13.4: The Closed Comparison Source Package

The Paper-22 comparison source package is

```math
\mathcal S_{cmp}^{22}
:=
\left(
a_{cmp}^{22},
\mathcal O_{22,j}^{cmp},
\mathcal E_{cmp}^{22,zero},
\mathcal E_{cmp}^{22,cmpbat},
\mathcal E_{cmp}^{22,carry}
\right),
```

where:

1. \(a_{cmp}^{22}\) is the finite majorant of Definition 13.2;
2. \(\mathcal O_{22,j}^{cmp}\) is supplied by `CMPINV_22`;
3. exact zero rows are those with \(\mathrm{ZC}_{22}=\mathrm{zero}\);
4. internal comparison-battery rows are those with
   \(\mathrm{ZC}_{22}=\mathrm{cmpbat}\);
5. carried rows are those with
   \(\mathrm{ZC}_{22}\in\{\mathrm{tail},\mathrm{carry}\}\).

Rows with \(\mathrm{ZC}_{22}=\mathrm{CMSSI}\) are assigned to the same-shell
ledger and are not support-growing pass rows.

### Lemma 13.5: No Double Charge In The Closed Package

The comparison source package \(\mathcal S_{cmp}^{22}\) does not repay any debit
already assigned to Paper-16 RP/Cov transport, Paper-12 readout/de-smearing,
Paper-20 scalar coefficient correction, `RPF`, `KPdec`, `WP`, `BTQ`, `CMSSI`,
`ACTSRC+`, or `SDSRC+`.

Proof.  Paper 21 Definition 107.1 and Theorem 107.7 restrict comparison rows to
the common \(E_{14}/X_{13}\) finite-battery comparison tower.  Paper 21 Sections
89--98 and 107 explicitly exclude action-source, SD-source, fusion/channel,
RP/Cov, exact-entry, readout, and whole-process mismatch costs from this class.
Definition 11.6 then applies the same exclusions as a finite admissibility
mask.  Any row failing that mask is assigned to `carry`, `tail`, `cmpbat`,
`BTQ`, `CMSSI`, or `zero`, not to the support-growing pass set. `square`

### Theorem 13.6: `P22-CMPSRC-CLOSE+`

On the strict row-complete same-record envelope branch,

```math
\boxed{
\mathrm{P22\text{-}CMPSRC\text{-}CLOSE}^{+}
}
```

holds in the following precise sense:

```math
\mathrm{CMPSRC}^{+}
=
\mathrm{CMPVAL}_{env}^{22,+}
+\mathrm{CMPINV}_{22}^{+}
+\mathrm{CMPADM/ZC}_{22}^{+}
+\mathrm{CMP\text{-}NODC}_{22}^{+},
```

where the finite comparison value envelope satisfies

```math
\boxed{
A_{cmp,pass}^{22}\le2
}
```

on the strict unit-normalized no-extra-normal-form branch.

With normal-form insertions, replace this by

```math
A_{cmp,pass}^{22}
\le
\max\left(
1,\,
2B_{cmp,s}^{22}B_{cmp,t}^{22}B_{cmp,rec}^{22}
\right).
```

Proof.  The inverse/admissibility and zero/carry components are Theorem 11.9
and Corollary 11.10.  The finite value envelope is Definition 13.2 and Lemma
13.3.  The no-double-charge component is Lemma 13.5.  These four pieces are
exactly the split of Work Package II in Section 5.  Thus `CMPSRC+` is closed as
a finite same-record envelope source package. `square`

### Corollary 13.7: What This Does And Does Not Prove

The comparison source closure does **not** prove reduced decay.  Paper 21 Table
107.5 records that comparison rows have

```math
d(e)=0.
```

Thus a comparison row can enlarge the finite pass graph and increase the
coefficient/branching budget, but it does not itself supply the analytic decay
exponent.  After Work Package II, the remaining task is no longer
`CMPVAL+`; it is to rebuild the licensed pass graph and test whether the
reduced tail source can beat the now-closed source envelopes.

In particular, the next live gate is

```math
\mathrm{P22\text{-}LICGRAPH}
+
\mathrm{P22\text{-}RED\text{-}TAIL}.
```

### Corollary 13.8: Updated Paper-22 Live Obstruction

Work Packages I and II are now closed on the strict row-complete envelope
branch:

```math
\boxed{
\mathrm{P22\text{-}COMMON\text{-}INVADM}^{+}
\quad+\quad
\mathrm{P22\text{-}CMPSRC\text{-}CLOSE}^{+}.
}
```

The live obstruction is therefore updated from

```math
\mathrm{PARK\text{-}CMPVAL}^{+}
+
\mathrm{PARK\text{-}RED\text{-}TAIL}^{+}
```

to

```math
\boxed{
\mathrm{PARK\text{-}LICGRAPH}^{+}
\quad+\quad
\mathrm{PARK\text{-}RED\text{-}TAIL}^{+}.
}
```

`PARK-LICGRAPH+` means: rebuild the pass graph using the now-closed
`ACTSRC+`, `SDSRC+`, and `CMPSRC+` envelope packages, then run the SCC,
coverage, coefficient, inverse-growth, and reduced-tail inequality audits.
Only after that rebuild can Paper 22 know whether the finite-table route is
nonempty, too expensive, or bypassed by a direct reduced-tail theorem.

## 14. Work Package III Closure: The Licensed Pass Graph

This section closes Work Package III on the strict row-complete envelope branch.
The closure is not a numerical miracle.  It is a finite ranking theorem.  Once
Work Packages I and II are inserted, every row that is actually licensed as a
pass row is support-growing.  Therefore the licensed pass graph has finite
maximum depth.  The reduced all-depth tail is then empty past a finite cutoff,
so the finite-table branch does not need a new asymptotic one-step KP source.

### Definition 14.1: Strict Licensed Envelope Branch

The strict licensed branch used in this section consists of the following
already closed source choices.

1. `COMMON-INVADM+` is supplied by Theorem 11.9.  Thus every surviving nonzero
   row has a same-record inverse slot with

   ```math
   \mathcal O_{22,j}^{c}(e)\le1.
   ```

2. `ACTSRC+` uses the Paper-21 action envelope route imported in Corollary
   12.1:

   ```math
   A_{act,elig}^{22}
   \le
   \max\left(
   1,\,
   B_{act}^{110}\Pi_{act}^{113,mon}C_v^{YM2,min}
   \right).
   ```

   On the active \(n_A^{113}\le408\) branch,

   ```math
   \log A_{act,elig}^{22}
   \le
   \log^+\!\left(B_{act}^{110}C_v^{YM2,min}\right)+36.31.
   ```

3. `SDSRC+` uses the minimal retained-word projected envelope of Corollary
   12.2:

   ```math
   A_{SD,proj}^{22}\le8.
   ```

4. `CMPSRC+` is supplied by Theorem 13.6:

   ```math
   A_{cmp,pass}^{22}\le2
   ```

   on the strict unit-normalized no-extra-normal-form branch.

5. Fusion rows remain in the same-shell channel/`CMSSI` ledger, as in Paper 21
   Corollary 103.6.  They are not support-growing pass rows.

No item in this branch imports a Wilson-loop area law, a mass gap, a continuum
Yang-Mills measure, or an off-record local subprocess.

### Definition 14.2: The Licensed Pass Edge Set

The licensed classwise pass sets are

```math
\mathcal E_{act,pass}^{22}
:=
\left\{
e\in\mathcal U_{22}^{row}:
c(e)=act,\ \Delta_X(e)\ge1,\ \mathrm{Adm}_{22}(e)=1
\right\},
```

```math
\mathcal E_{SD,pass}^{22}
:=
\left\{
e\in\mathcal U_{22}^{row}:
c(e)=SD,\ \Delta_X(e)\ge1,\ \mathrm{Adm}_{22}(e)=1
\right\},
```

and

```math
\mathcal E_{cmp,pass}^{22}
:=
\left\{
e\in\mathcal U_{22}^{row}:
c(e)=cmp,\ \Delta_X(e)\ge1,\ \mathrm{Adm}_{22}(e)=1
\right\}.
```

The fusion pass set is empty:

```math
\mathcal E_{fus,pass}^{22}:=\varnothing.
```

Thus

```math
\boxed{
\mathcal E_{pass}^{22}
=
\mathcal E_{act,pass}^{22}
\cup
\mathcal E_{SD,pass}^{22}
\cup
\mathcal E_{cmp,pass}^{22}.
}
```

The decay-eligible and neutral subsets are

```math
\mathcal E_{dec}^{22}
:=
\mathcal E_{act,pass}^{22}
\cup
\mathcal E_{SD,pass}^{22},
\qquad
\mathcal E_{neu}^{22}
:=
\mathcal E_{cmp,pass}^{22}.
```

For \(e\in\mathcal E_{pass}^{22}\), set

```math
u(e):=\Delta_X(e),
\qquad
d(e):=
\Delta_X(e)\mathbf 1_{\{e\in\mathcal E_{dec}^{22}\}}.
```

Therefore comparison pass rows are allowed to enlarge the graph and the
coefficient budget, but still have \(d(e)=0\).  This is exactly Paper 21 Table
107.5.

### Lemma 14.3: The Licensed Graph Is Same-Record And Finite

The directed graph

```math
\mathfrak G_{pass}^{22}
:=
\left(\mathcal U_{99}^{vert},\mathcal E_{pass}^{22}\right)
```

is a finite same-record graph.

Proof.  Paper 21 Sections 103--107 print finite structural row maps on the
finite over-refined vertex cover.  Theorem 11.9 supplies finite inverse and
admissibility tags on the same finite row universe.  Theorem 13.6 supplies the
finite comparison value envelope.  Corollaries 12.1 and 12.2 supply the action
and `SD` coefficient envelopes under the strict branch conventions.  Definition
14.2 then selects a finite subset of the printed row universe.  Every selected
row is evaluated under the same pushed-forward `SEL2` scalar law inherited from
Papers 20 and 21. `square`

### Lemma 14.4: Support Cardinality Is A Strict Lyapunov Rank

Let

```math
\rho_L(\bar v):=|L(\bar v)|
```

be the cardinality of the rooted local frontier coordinate.  For every licensed
pass edge \(e:\bar v\to\bar v'\),

```math
\rho_L(\bar v')-\rho_L(\bar v)=\Delta_X(e)\ge1.
```

Consequently \(\mathfrak G_{pass}^{22}\) is acyclic.

Proof.  For `act`, `SD`, and `cmp` rows, Papers 21 Definitions 104.3, 106.5,
and 107.4 define the target frontier by

```math
L'=\operatorname{Can}_{L}^{99,+}(L\cup S)
```

and define

```math
\Delta_X=|(L\cup S)\setminus L|.
```

The canonicalization is by the finite \(B_4\)-symmetry and preserves
cardinality.  Definition 14.2 admits only rows with \(\Delta_X\ge1\).  Therefore
the frontier cardinality strictly increases along every pass edge.  A directed
cycle would force the rank to return to its starting value after strictly
increasing at least once, which is impossible. `square`

### Corollary 14.5: SCC, Size, And Coverage Verdict

The zero-growth pass subgraph is empty:

```math
\mathfrak G_{0}^{22}
:=
\left(
\mathcal U_{99}^{vert},
\{e\in\mathcal E_{pass}^{22}:\Delta_X(e)=0\}
\right)
=
(\mathcal U_{99}^{vert},\varnothing).
```

Hence

```math
c_{size}^{22}=1.
```

Moreover the positive-support cycle-ratio convention gives

```math
\chi_{cyc}^{22}=+\infty,
```

because \(\mathfrak G_{pass}^{22}\) has no directed cycle at all.  In the
finite-depth branch, the coverage transient is finite and no asymptotic
coverage margin is needed.

Proof.  Definition 14.2 excludes \(\Delta_X=0\) pass rows; such rows were
already assigned to `CMSSI`, `BTQ`, `cmpbat`, `zero`, `tail`, or `carry` by
Definition 11.6.  Thus the zero-growth pass graph has no edges and its longest
zero-growth path has length \(0\), giving \(c_{size}^{22}=(0+1)^{-1}=1\).
Lemma 14.4 proves that the full pass graph is acyclic, so the cycle-ratio set is
empty and the convention of Paper 21 Definition 95.3 gives
\(\chi_{cyc}^{22}=+\infty\). `square`

### Definition 14.6: Finite Growth Constants Of The Licensed Graph

Define the exact finite branching and coefficient constants

```math
C_{geom}^{22}
:=
\max\left(
1,\,
\max_{\bar v\in\mathcal U_{99}^{vert}}
\#\{e\in\mathcal E_{pass}^{22}:s(e)=\bar v\}
\right),
```

```math
A_{esc}^{22}
:=
\max_{e\in\mathcal E_{pass}^{22}}\max(1,a_{22}(e)),
```

with the empty-pass convention \(A_{esc}^{22}=1\).  Thus
\(C_{geom}^{22}\ge1\) by definition.

Let

```math
N_{act}^{22}:=|\Xi_{act}^{99,+}|,
\qquad
N_{SD}^{22}:=|\Xi_{SD}^{99,+}|,
\qquad
N_{cmp}^{22}:=|\Xi_{cmp}^{99,+}|.
```

Then

```math
C_{geom}^{22}
\le
\max\left(
1,\,
N_{act}^{22}+N_{SD}^{22}+N_{cmp}^{22}
\right)
```

The coefficient envelope is

```math
A_{esc}^{22}
\le
\max\left(
1,\,
A_{act,elig}^{22},\,
A_{SD,proj}^{22},\,
A_{cmp,pass}^{22}
\right),
```

and hence, on the strict active branch,

```math
\boxed{
A_{esc}^{22}
\le
\max\left(
1,\,
B_{act}^{110}\Pi_{act}^{113,mon}C_v^{YM2,min},\,
8,\,
2
\right).
}
```

Using \(n_A^{113}\le408\), this implies

```math
\log A_{esc}^{22}
\le
\max\left(
\log 8,\,
\log^+\!\left(B_{act}^{110}C_v^{YM2,min}\right)+36.31
\right).
```

The certified inverse-growth surcharge is

```math
g_{q}^{22}
:=
\log
\max_{\bar v\in\mathcal U_{99}^{vert}}
\left(
1+
\sum_{\substack{e\in\mathcal E_{pass}^{22}\\s(e)=\bar v}}
\mathcal O_{22,j}^{c(e)}(e)
\right).
```

By Theorem 11.9,

```math
\boxed{
g_q^{22}\le\log(1+C_{geom}^{22}).
}
```

Finally, on the strict full-law/no-degree-tail branch,

```math
g_{bat}^{22}=0.
```

Rows removed to representation tail, product tail, comparison degree tail, or
`BTQ-DEGTAIL` are not pass rows in \(\mathfrak G_{pass}^{22}\).

### Theorem 14.7: `P22-LICGRAPH-CLOSE+`

On the strict row-complete same-record envelope branch,

```math
\boxed{
\mathrm{P22\text{-}LICGRAPH\text{-}CLOSE}^{+}
}
```

holds.  The licensed pass graph is the finite graph of Definition 14.2, its
zero-growth SCC test passes, and its finite constants are the constants of
Definition 14.6.

Moreover, because every pass edge strictly increases the local frontier rank,
the graph has finite maximum directed path length

```math
K_{max}^{22}
\le
|\mathsf Q_{loc}^{99}|
=3^4=81.
```

Consequently the reduced all-depth finite-table tail is empty past that depth:

```math
\boxed{
T_{\ge K}^{red,act,22}(j)=0
\qquad(K>K_{max}^{22}).
}
```

Proof.  Lemma 14.3 proves that the graph is finite and same-record.  Lemma 14.4
proves that support cardinality is a strict Lyapunov rank.  Corollary 14.5
therefore closes the zero-growth SCC and coverage/size part of the finite audit
by the finite-depth branch of Paper 21 Theorem 95.7.  Definition 14.6 gives
finite coefficient, branching, inverse-growth, and battery-growth constants.
Since every pass edge strictly increases \(L\subseteq\mathsf Q_{loc}^{99}\), no
directed path can have more than \(|\mathsf Q_{loc}^{99}|\) pass edges.  Hence
there are no pass paths of length \(K>K_{max}^{22}\), and the corresponding
tail term vanishes. `square`

### Corollary 14.8: Updated Paper-22 Status After Work Package III

The Work-I and Work-II live obstruction

```math
\mathrm{PARK\text{-}LICGRAPH}^{+}
\quad+\quad
\mathrm{PARK\text{-}RED\text{-}TAIL}^{+}
```

is discharged on the strict row-complete same-record envelope branch by

```math
\boxed{
\mathrm{P22\text{-}LICGRAPH\text{-}CLOSE}^{+}
\quad+\quad
T_{\ge K}^{red,act,22}(j)=0\ (K>K_{max}^{22}).
}
```

This does **not** prove continuum Yang-Mills confinement.  It only says that the
Paper-22 finite-table obstruction has been closed without importing the
conclusion.  The remaining upstream obstruction is the Paper-20/Paper-21
tree-rate source gate:

```math
\mathrm{P20\text{-}SEL2\text{-}TREE\text{-}RATE\text{-}GATE}
=
\mathrm{P20\text{-}SEL2\text{-}TREE\text{-}TIME}(\rho)
+
\mathrm{P20\text{-}SEL2\text{-}ESC\text{-}MASS}
(V_\rho,\gamma_\rho,q_\rho),
```

together with the associated surface prefactor comparison.  If a later branch
rejects the strict action envelope, the minimal `SD` projection convention, or
the row-complete finite battery, then the relevant source package must be
restored as a named park condition and the licensed graph must be rebuilt.

## 15. Post-Work-III Gate Worksheet And Source Attack

Work Package III closed the finite-table reduced-tail obstruction.  The next
mainline task is therefore not Work Package IV.  Work Package IV remains a
fallback for a later branch that rejects the strict row-complete envelope.  On
the present strict branch, the obstruction has moved back upstream to the
same-record tree-rate source gate.

This section freezes that gate as an executable scalar worksheet and pushes
the two subgates as far as Papers 20--21 allow.

### Definition 15.1: Frozen Tree-Rate Gate Worksheet

The post-Work-III gate worksheet is evaluated on one fixed `SEL2` scalar
pushforward law, one fixed nontrivial representation channel \(\rho\), and one
fixed activity ceiling \(0\le\widehat\eta_{*,20}<1\).  Set

```math
G_{13,tree}^{SEL2}
:=
1+\log 19
+20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}.
```

The two tree-rate thresholds are

```math
\Theta_T^{tree}(\rho)
:=
{2G_{13,tree}^{SEL2}\over C_2(\rho)}
```

and

```math
\Theta_{esc}^{tree}
:=
1-\exp(-G_{13,tree}^{SEL2}).
```

For the standard frozen `SEL2` sheet-time selector, define

```math
T_{clean,-}^{SEL2}:=s(1-\epsilon_A)(1-\chi),
\qquad
T_{clean,+}^{SEL2}:=s(1+\epsilon_A)(1+\chi).
```

Equivalently, the clean selector passes the time half if

```math
s>
S_T^{pass}(\rho)
:=
{2G_{13,tree}^{SEL2}
\over C_2(\rho)(1-\epsilon_A)(1-\chi)},
```

and is cleanly falsified by the present window if

```math
s\le
S_T^{fail}(\rho)
:=
{2G_{13,tree}^{SEL2}
\over C_2(\rho)(1+\epsilon_A)(1+\chi)}.
```

The full Paper-20 gate remains the conjunction

```math
\mathrm{P20\text{-}SEL2\text{-}TREE\text{-}RATE\text{-}GATE}
=
\mathrm{P20\text{-}SEL2\text{-}TREE\text{-}TIME}(\rho)
+
\mathrm{P20\text{-}SEL2\text{-}ESC\text{-}MASS}
(V_\rho,\gamma_\rho,q_\rho).
```

This worksheet is intentionally scalar and operational.  It does not refer to
a continuum field configuration, an assumed Yang-Mills measure, an area law, or
a mass gap.

### Lemma 15.2: The Actual-Row Coefficient Comparison Is No Longer The Bottleneck

On the strict exact-record five-term branch imported in Paper 21 Section 48,
the actual four-dimensional `SEL2` scalar coefficient satisfies

```math
{a_{\rho,j}^{SEL2}\over d_\rho}
=
\exp\left(
-{C_2(\rho)\over2}T_j^{SEL2,conv}
\right)
+o(1),
```

where

```math
T_j^{SEL2,conv}
=
\sum_{b\in\mathscr S_j^{SEL2}}\tau_{b,j}.
```

Consequently the gate worksheet is not blocked by a hidden Bianchi/off-sheet,
collar, counterterm, projective, or readout correction.

Proof.

This is Paper 21 Theorem 48.6, which identifies Paper 20's
`P20-SEL2-4DCOEFF-CLOSE` with
`P21-RAW-TREE-CMP` on the strict branch.  The proof there imports the
Paper-20 five-term scalar audit: nonbulk terms vanish, boundary roots vanish,
and interior Bianchi/off-sheet roots vanish.  Thus the actual pushed-forward
finite row has the same normalized leading coefficient as the finite
heat-kernel convolution tree, up to an \(o(1)\) scalar error on the same
record law. `square`

### Theorem 15.3: `TREE-TIME` Is An Exact Scalar Pass/Falsification Test

On the strict post-Work-III branch, the time half has the following complete
current decision.

1. If

   ```math
   T_{clean,-}^{SEL2}>\Theta_T^{tree}(\rho),
   ```

   then `P20-SEL2-TREE-TIME(\rho)` holds.

2. If

   ```math
   T_{clean,+}^{SEL2}\le\Theta_T^{tree}(\rho),
   ```

   then `P20-SEL2-TREE-TIME(\rho)` fails for the frozen standard `SEL2`
   selector.

3. If

   ```math
   T_{clean,-}^{SEL2}
   \le
   \Theta_T^{tree}(\rho)
   <
   T_{clean,+}^{SEL2},
   ```

   then the present corpus parks the time half at the scalar
   selector-sharpness problem

   ```math
   \liminf_jT_j^{SEL2,conv}>\Theta_T^{tree}(\rho).
   ```

Proof.

Paper 20 Theorem 4.3A.160BH.40T.6 and Paper 21 Theorem 1.3 prove this
trichotomy from the cofinal clean window

```math
T_{clean,-}^{SEL2}
\le
\liminf_jT_j^{SEL2,conv}
\le
\limsup_jT_j^{SEL2,conv}
\le
T_{clean,+}^{SEL2}.
```

Lemma 15.2 says the actual four-dimensional pushed-forward scalar coefficient
does not introduce an additional time source or an additional time loss on the
strict branch.  Therefore the only remaining issue is the scalar placement of
the frozen selector time relative to the displayed threshold. `square`

### Corollary 15.4: Raw-Time Saturation Does Not Automatically Prove Tree-Time

Paper 21's raw unit threshold is

```math
\theta_\rho:={2\log d_\rho\over C_2(\rho)}.
```

The tree-time threshold is obtained from the same denominator but with
numerator \(G_{13,tree}^{SEL2}\).  Hence raw-time saturation implies
tree-time only when the branch also proves

```math
\log d_\rho\ge G_{13,tree}^{SEL2}
```

or separately freezes \(s\) above the larger tree-time endpoint.  In the
usual small-rank fundamental channels, the diagnostic numerator
\(1+\log 19\) already exceeds \(\log d_\rho\), and decoration activity only
raises it.  Thus the raw unit/rate closure from Paper 21 is not, by itself, a
tree-rate closure.

### Lemma 15.5: Universal Ceiling For A Single Escape Certificate

Let

```math
\psi_\rho(U):={\Phi_\rho(U)\over d_\rho},
\qquad
\widetilde a_{\rho,j}^{SEL2}
:=
\int_G\psi_\rho(U)\,d\nu_{p,j}^{SEL2}(U).
```

Assume \(\psi_\rho(U)\le1\) on the central real scalar readout used in the
escape audit.  If \(V_\rho\) has gap

```math
1-\psi_\rho(U)\ge\gamma_\rho>0
\qquad(U\in V_\rho),
```

and cofinal mass

```math
\liminf_j\nu_{p,j}^{SEL2}(V_\rho)\ge q_\rho,
```

then every such fixed-set escape certificate obeys

```math
q_\rho\gamma_\rho
\le
\liminf_j
\left(1-\widetilde a_{\rho,j}^{SEL2}\right).
```

Consequently `ESC-MASS` can pass only if

```math
\limsup_j\widetilde a_{\rho,j}^{SEL2}
<
\exp(-G_{13,tree}^{SEL2}).
```

Proof.

For each row,

```math
\gamma_\rho\nu_{p,j}^{SEL2}(V_\rho)
\le
\int_{V_\rho}(1-\psi_\rho(U))\,d\nu_{p,j}^{SEL2}(U)
\le
1-\widetilde a_{\rho,j}^{SEL2}.
```

Taking the lower limit gives the first displayed inequality.  If
`ESC-MASS` holds, then

```math
q_\rho\gamma_\rho>\Theta_{esc}^{tree}
=1-\exp(-G_{13,tree}^{SEL2}),
```

so the coefficient must satisfy the strict upper bound displayed above.
`square`

### Theorem 15.6: Brutal `ESC-MASS` Verdict

On the strict post-Work-III branch, the present corpus does not prove
`P20-SEL2-ESC-MASS`.  More sharply:

1. the already-proved positive escape source from Paper 20 is far too weak;
2. if the tree-time falsifier

   ```math
   T_{clean,+}^{SEL2}\le\Theta_T^{tree}(\rho)
   ```

   holds, then no fixed-set escape certificate can pass the rooted tree
   threshold on the strict five-term branch;
3. if the tree-time pass inequality holds, the necessary coefficient ceiling
   for escape is no longer impossible, but a separate near-maximal weak-tail
   certificate is still required:

   ```math
   \exists V_\rho,\gamma_\rho,q_\rho:
   \qquad
   q_\rho\gamma_\rho
   >
   1-\exp(-G_{13,tree}^{SEL2}).
   ```

Proof.

For item 1, Paper 20 Theorem 4.3A.160BH.40T.4 proves that the existing
positive escape construction certifies at most

```math
{(\sigma_\rho^{ref})^2\over8}< {1\over8},
```

whereas

```math
\Theta_{esc}^{tree}
=
1-\exp(-G_{13,tree}^{SEL2})
\ge
1-{1\over19e}
>0.98.
```

Thus the existing source is a genuine noncollapse theorem, not a tree-rate
escape theorem.

For item 2, Lemma 15.2 gives

```math
\widetilde a_{\rho,j}^{SEL2}
=
\exp\left(-{C_2(\rho)\over2}T_j^{SEL2,conv}\right)+o(1).
```

If \(T_{clean,+}^{SEL2}\le\Theta_T^{tree}(\rho)\), then the cofinal upper
time window gives

```math
\liminf_j\widetilde a_{\rho,j}^{SEL2}
\ge
\exp(-G_{13,tree}^{SEL2}).
```

Therefore

```math
\liminf_j(1-\widetilde a_{\rho,j}^{SEL2})
\le
1-\exp(-G_{13,tree}^{SEL2})
=
\Theta_{esc}^{tree}.
```

Lemma 15.5 then forbids any strict fixed-set product
\(q_\rho\gamma_\rho>\Theta_{esc}^{tree}\).

For item 3, the time pass only gives the necessary coefficient suppression.  A
fixed-set escape certificate is a stronger weak-tail statement about the
random variable \(1-\psi_\rho(U)\) under the actual `SEL2` pushed-forward
plaquette law.  Papers 10--12 supply projective pushforwards, RG bookkeeping,
and loop-readout controls; Papers 20--21 supply the strict coefficient
comparison; and Paper 22 supplies the finite-table closure on the strict
row-complete branch.  None of them supplies the displayed near-maximal
weak-tail lower bound. `square`

### Corollary 15.7: Current Post-Work-III Execution Order

After Work Packages I--III, the honest next execution order is:

1. instantiate or sharpen the scalar selector-time data until Theorem 15.3
   gives a pass or a falsifier for `TREE-TIME`;
2. if `TREE-TIME` fails by the upper endpoint, the strict `SEL2` tree-rate
   route fails at the present rooted surface-growth threshold;
3. if `TREE-TIME` passes, prove a new near-maximal same-record escape
   weak-tail theorem, or lower the rooted surface-growth threshold and rerun
   the escape inequality;
4. only after both subgates pass, evaluate the conditional surface prefactor
   cap.

Thus the live obstruction is not a Paper-22 finite-table obstruction and not a
direct reduced-tail obstruction.  It is the same-record scalar source pair

```math
\mathrm{P20\text{-}SEL2\text{-}TREE\text{-}TIME}(\rho)
\quad+\quad
\mathrm{P20\text{-}SEL2\text{-}ESC\text{-}MASS}
(V_\rho,\gamma_\rho,q_\rho).
```

The escape half has now been attacked sharply enough to expose its true size:
with the current rooted tree entropy, it is a near-maximal anti-concentration
problem, not a small positive-mass problem.

## 16. Tree-Time Instantiation And Escape-Ceiling Test

Section 15 reduced the post-Work-III mainline to a scalar source pair.  This
section turns that pair into a pass/fail worksheet.  The purpose is to prevent
future work from searching for escape sets blindly: the best possible fixed-set
escape product is a definite tail functional of the pushed-forward plaquette
law.

### Definition 16.1: Tree-Time Instantiation Row

For a candidate branch

```math
\mathfrak W_{16}
:=
(\rho,s,\epsilon_A,\chi,\widehat\eta_{*,20}),
```

define

```math
G_{16}:=
1+\log 19
+20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}},
```

```math
\Theta_{T,16}(\rho):={2G_{16}\over C_2(\rho)},
\qquad
\Theta_{esc,16}:=1-e^{-G_{16}},
```

and

```math
T_{-,16}:=s(1-\epsilon_A)(1-\chi),
\qquad
T_{+,16}:=s(1+\epsilon_A)(1+\chi).
```

The two signed margins are

```math
\Delta_{T,16}^{pass}:=T_{-,16}-\Theta_{T,16}(\rho),
```

and

```math
\Delta_{T,16}^{fail}:=\Theta_{T,16}(\rho)-T_{+,16}.
```

Thus:

1. `TREE-TIME` passes if \(\Delta_{T,16}^{pass}>0\);
2. `TREE-TIME` is falsified by the present selector window if
   \(\Delta_{T,16}^{fail}\ge0\);
3. otherwise the branch is in the selector-sharpness strip

   ```math
   T_{-,16}\le\Theta_{T,16}(\rho)<T_{+,16}.
   ```

This row is the worksheet item that must be instantiated before the escape
half is worth spending.

### Theorem 16.2: Tree-Time Instantiation Verdict

For every candidate row \(\mathfrak W_{16}\), the `TREE-TIME` status is exactly
the three-way decision in Definition 16.1.

Proof.

This is Theorem 15.3 with the notation compressed into one candidate row.
The strict pass margin gives a cofinal lower endpoint
\(T_-^{SEL2}>\Theta_T^{tree}(\rho)\).  The nonnegative fail margin gives
\(T_{clean,+}^{SEL2}\le\Theta_T^{tree}(\rho)\), which forbids any strict lower
endpoint above the threshold for the frozen selector.  The remaining case is
the straddling strip. `square`

### Definition 16.3: Cofinal Escape-Ceiling Functional

On the same branch, write

```math
\psi_\rho(U):={\Phi_\rho(U)\over d_\rho},
\qquad
X_\rho(U):=1-\psi_\rho(U).
```

Let \(\nu_{p,j}^{SEL2}\) be the actual pushed-forward plaquette law.  Define
the cofinal fixed-set escape ceiling

```math
\mathcal E_{\rho}^{cof,SEL2}
:=
\sup_{\gamma>0}
\gamma\,
\liminf_j
\nu_{p,j}^{SEL2}
\{U:X_\rho(U)\ge\gamma\}.
```

The set \(\{X_\rho\ge\gamma\}\) is central and is the largest possible set
with character gap at least \(\gamma\).  Therefore no smaller escape set can
improve the product at that same gap.

For a reference probability law \(\nu\) on \(SU(N)\), define similarly

```math
\mathcal E_\rho^*(\nu)
:=
\sup_{\gamma>0}
\gamma\,\nu\{U:X_\rho(U)\ge\gamma\}.
```

For the compact-group heat-kernel reference \(H_T\), write

```math
\mathcal E_{\rho}^{HK}(I)
:=
\sup_{T\in I}\mathcal E_\rho^*(H_T)
```

for any declared time interval \(I\).

### Lemma 16.4: `ESC-MASS` Is Exactly The Cofinal Tail Inequality

On the fixed scalar record law,

```math
\mathrm{P20\text{-}SEL2\text{-}ESC\text{-}MASS}
```

holds if and only if

```math
\mathcal E_{\rho}^{cof,SEL2}>\Theta_{esc,16}.
```

It fails for all fixed central escape sets if

```math
\mathcal E_{\rho}^{cof,SEL2}\le\Theta_{esc,16}.
```

Proof.

If `ESC-MASS` holds for \(V_\rho,\gamma_\rho,q_\rho\), then
\(V_\rho\subseteq\{X_\rho\ge\gamma_\rho\}\).  Hence

```math
\gamma_\rho
\liminf_j\nu_{p,j}^{SEL2}\{X_\rho\ge\gamma_\rho\}
\ge
\gamma_\rho q_\rho
>
\Theta_{esc,16},
```

so \(\mathcal E_{\rho}^{cof,SEL2}>\Theta_{esc,16}\).

Conversely, if the supremum is strictly above \(\Theta_{esc,16}\), choose a
\(\gamma\) with

```math
\gamma\liminf_j\nu_{p,j}^{SEL2}\{X_\rho\ge\gamma\}
>
\Theta_{esc,16}.
```

Set \(V_\rho=\{X_\rho\ge\gamma\}\) and choose any strict

```math
0<q_\rho<
\liminf_j\nu_{p,j}^{SEL2}(V_\rho)
```

with \(\gamma q_\rho>\Theta_{esc,16}\).  This is exactly the escape-mass
certificate.  The failure clause is the contrapositive. `square`

### Lemma 16.5: Moment Ceiling For Every Escape-Ceiling Functional

For every probability law \(\nu\),

```math
\mathcal E_\rho^*(\nu)
\le
\int_G X_\rho(U)\,d\nu(U).
```

Consequently, for the heat-kernel reference,

```math
\mathcal E_\rho^*(H_T)
\le
1-\exp\left(-{C_2(\rho)\over2}T\right).
```

Proof.

For every \(\gamma>0\),

```math
\gamma\,\mathbf 1_{\{X_\rho\ge\gamma\}}
\le
X_\rho.
```

Integrating and taking the supremum proves the first inequality.  For
\(H_T\), the normalized character coefficient is

```math
\int_G\psi_\rho(U)\,dH_T(U)
=
\exp\left(-{C_2(\rho)\over2}T\right),
```

which gives the second inequality. `square`

### Corollary 16.6: The Heat-Kernel Reference Cannot Beat Escape Before Tree-Time

If a heat-kernel reference time interval \(I\) lies below the tree-time
threshold,

```math
\sup I\le\Theta_{T,16}(\rho),
```

then

```math
\mathcal E_\rho^{HK}(I)
\le
\Theta_{esc,16}.
```

Thus a heat-kernel-like fixed-set escape proof cannot pass before the same
time scale needed by `TREE-TIME`.

Proof.

Lemma 16.5 gives

```math
\mathcal E_\rho^*(H_T)
\le
1-\exp\left(-{C_2(\rho)\over2}T\right).
```

The right side is increasing in \(T\), and at
\(T=\Theta_{T,16}(\rho)=2G_{16}/C_2(\rho)\) it equals
\(1-e^{-G_{16}}=\Theta_{esc,16}\). `square`

### Definition 16.7: The `SU(2)` Haar Escape Diagnostic

For the fundamental channel of \(SU(2)\), write each conjugacy class as
\(\theta\in[0,\pi]\).  Then

```math
\psi_F(\theta)=\cos\theta,
\qquad
d\mathrm{Haar}_{class}(\theta)
={2\over\pi}\sin^2\theta\,d\theta.
```

For \(\gamma\in[0,2]\), set

```math
\theta_\gamma:=\arccos(1-\gamma).
```

The Haar escape product is the one-variable function

```math
\mathcal H_F^{SU(2)}(\gamma)
=
\gamma\left(
1-{\theta_\gamma\over\pi}
+{\sin(2\theta_\gamma)\over2\pi}
\right).
```

Thus

```math
\mathcal E_F^*(\mathrm{Haar}_{SU(2)})
=
\max_{0\le\gamma\le2}\mathcal H_F^{SU(2)}(\gamma).
```

The stationary points are exactly the solutions of

```math
1-{\theta\over\pi}
+{\sin(2\theta)\over2\pi}
=
{2\over\pi}(1-\cos\theta)\sin\theta,
\qquad
\gamma=1-\cos\theta.
```

The unique interior maximizer gives the diagnostic value

```math
\mathcal E_F^*(\mathrm{Haar}_{SU(2)})
=0.5073\ldots
```

while the current decoration-free rooted tree escape threshold satisfies

```math
\Theta_{esc,16}
\ge
1-{1\over19e}
=0.9806\ldots.
```

This diagnostic does not by itself prove a bound for every \(H_T\), because a
heat-kernel stochastic-monotonicity theorem for this tail functional has not
been imported.  It does prove that the terminal Haar-spread heuristic is far
below the present rooted tree threshold.  The needed `ESC-MASS` theorem is
therefore not a generic "spread away from identity" theorem; it is a
near-maximal same-record tail theorem or a demand to lower the surface-growth
threshold.

### Theorem 16.8: Current Gate Verdict After The Ceiling Test

The post-Work-III gate has now been reduced to the following exact alternatives.

1. If

   ```math
   \Delta_{T,16}^{fail}\ge0,
   ```

   the strict `SEL2` tree-rate route fails at the current rooted
   surface-growth threshold.

2. If

   ```math
   \Delta_{T,16}^{pass}>0
   ```

   but

   ```math
   \mathcal E_{\rho}^{cof,SEL2}\le\Theta_{esc,16},
   ```

   the time half passes and the escape half fails.

3. If

   ```math
   \Delta_{T,16}^{pass}>0,
   \qquad
   \mathcal E_{\rho}^{cof,SEL2}>\Theta_{esc,16},
   ```

   then the tree-rate source gate passes and the next task is the surface
   prefactor cap.

4. If the time window straddles the threshold or
   \(\mathcal E_{\rho}^{cof,SEL2}\) is not computed, the obstruction is parked
   exactly as:

   ```math
   \mathrm{PARK\text{-}TTIME\text{-}SHARP}
   \quad\text{or}\quad
   \mathrm{PARK\text{-}ESC\text{-}TAIL}.
   ```

At the current source level, the first non-formal missing data are:

```math
(\rho,s,\epsilon_A,\chi,\widehat\eta_{*,20})
```

for the selector-time row, and a same-record evaluation or sharp bound for

```math
\mathcal E_{\rho}^{cof,SEL2}.
```

Proof.

The time alternatives are Theorem 16.2.  The escape alternatives are Lemma
16.4.  Corollary 16.6 and Definition 16.7 show why the escape side is severe:
it is controlled by a tail functional, not merely by positivity of some escape
mass, and the obvious heat-kernel/Haar diagnostics do not supply a near-one
product. `square`

### Corollary 16.9: Next Executable Source Tasks

The next work should choose one of the following two source tasks.

1. **Instantiate the selector-time row.**  Freeze

   ```math
   (\rho,s,\epsilon_A,\chi,\widehat\eta_{*,20})
   ```

   and decide \(\Delta_{T,16}^{pass}\) or
   \(\Delta_{T,16}^{fail}\).

2. **Evaluate the cofinal escape ceiling.**  Prove an actual same-record
   bound for

   ```math
   \mathcal E_{\rho}^{cof,SEL2}
   ```

   or prove that the rooted surface-growth threshold must be lowered before
   any fixed-set escape strategy can pass.

The surface prefactor comparison remains conditional and should not be charged
until both source halves pass.

## 17. Selector-Time Row Instantiation

Section 16 identified the first missing scalar datum:

```math
\mathfrak W_{16}
=
(\rho,s,\epsilon_A,\chi,\widehat\eta_{*,20}).
```

This section freezes the natural candidate representation rows and computes the
exact `TREE-TIME` status available from the present papers.  The result is
sharp but not magical: Papers 20--21 give formulas and ranges, not a numerical
choice of \(s,\epsilon_A,\chi,\widehat\eta_{*,20}\) for the active branch.

### Definition 17.1: Natural Candidate Channels

The first selector-time row family is the fundamental channel of \(SU(N)\):

```math
\rho=F_N,\qquad d_{F_N}=N,
\qquad
C_2(F_N)={N^2-1\over2N}.
```

The diagnostic finite list used for the first pass is

```math
(N,\rho)\in\{(2,F_2),(3,F_3),(4,F_4)\}.
```

The general \(SU(N)\) fundamental formula is kept alongside the finite list
because the threshold decreases like \(4(1+\log 19)/N\) at large \(N\), while
the escape-ceiling problem may become harder or easier depending on the chosen
central character.  No higher representation is inserted here unless a later
branch declares a concrete reason to prefer it: higher channels raise
\(C_2(\rho)\), but they also change \(d_\rho\), the raw unit threshold, and the
escape tail variable \(1-\Phi_\rho/d_\rho\).

### Definition 17.2: Current Selector-Parameter Status

The present corpus supplies the following selector-time information.

1. The AF-area and heat-time slacks are only bounded:

   ```math
   0<\epsilon_A<1,
   \qquad
   0<\chi<1.
   ```

2. The activity ceiling is only bounded symbolically:

   ```math
   0\le\widehat\eta_{*,20}<1.
   ```

3. On the Paper-21 adaptive optimistic zero-nonsurface-debit probe,

   ```math
   {20\widehat\eta_{*,20}(s)\over1-\widehat\eta_{*,20}(s)}
   <
   \log2.
   ```

   This is a best-case probe, not the full active-branch theorem.

4. The active branch does not presently print a numerical value of \(s\).
   Therefore the strongest licensed selector-time statement is a row
   classifier: pass, fail, or straddling as a function of the declared
   parameters.

This status is Barandes-aligned in the operational sense: only finite scalar
record parameters and finite pushforward data are used.  No continuum field
configuration or unrecorded process is smuggled into the row.

### Definition 17.3: Fundamental-Channel Tree-Time Thresholds

For the fundamental channel of \(SU(N)\), the exact pass and fail endpoints are

```math
S_{T,N}^{pass}
=
{4N\over N^2-1}
{G_{16}\over(1-\epsilon_A)(1-\chi)},
```

and

```math
S_{T,N}^{fail}
=
{4N\over N^2-1}
{G_{16}\over(1+\epsilon_A)(1+\chi)},
```

where

```math
G_{16}=1+\log 19
+20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}.
```

The candidate row is classified by:

```math
s>S_{T,N}^{pass}
\quad\Longrightarrow\quad
\mathrm{TREE\text{-}TIME\ pass},
```

```math
s\le S_{T,N}^{fail}
\quad\Longrightarrow\quad
\mathrm{TREE\text{-}TIME\ fail},
```

and

```math
S_{T,N}^{fail}<s\le S_{T,N}^{pass}
\quad\Longrightarrow\quad
\mathrm{TREE\text{-}TIME\ straddling}.
```

In the decoration-free zero-slack diagnostic
\(\widehat\eta_{*,20}=\epsilon_A=\chi=0\), these pass endpoints are:

| channel | \(C_2(F_N)\) | \(S_{T,N}^{pass}\) |
| --- | ---: | ---: |
| \(SU(2),F_2\) | \(3/4\) | \(10.5185\ldots\) |
| \(SU(3),F_3\) | \(4/3\) | \(5.9167\ldots\) |
| \(SU(4),F_4\) | \(15/8\) | \(4.2074\ldots\) |

Under the optimistic adaptive zero-debit ceiling
\(20\widehat\eta_{*,20}/(1-\widehat\eta_{*,20})<\log2\), still with
zero slacks, the sufficient pass endpoints become:

| channel | optimistic sufficient \(s\)-endpoint |
| --- | ---: |
| \(SU(2),F_2\) | \(12.3669\ldots\) |
| \(SU(3),F_3\) | \(6.9564\ldots\) |
| \(SU(4),F_4\) | \(4.9468\ldots\) |

Positive slacks multiply these sufficient endpoints by
\(((1-\epsilon_A)(1-\chi))^{-1}\).  Positive activity beyond the optimistic
probe raises them further.

### Theorem 17.4: Exact `TREE-TIME` Classification For The Candidate Rows

For each candidate \((N,F_N)\in\{(2,F_2),(3,F_3),(4,F_4)\}\), the current
`TREE-TIME` status is:

```math
\boxed{
\begin{array}{ccl}
s>S_{T,N}^{pass} &\Rightarrow& \mathrm{pass},\\[1mm]
s\le S_{T,N}^{fail} &\Rightarrow& \mathrm{fail},\\[1mm]
S_{T,N}^{fail}<s\le S_{T,N}^{pass}
&\Rightarrow& \mathrm{straddling}.
\end{array}}
```

No unconditional pass or falsifier for these rows is printed by the current
corpus, because the active branch has not supplied numerical values of

```math
s,\qquad \epsilon_A,\qquad \chi,\qquad \widehat\eta_{*,20}
```

or a sharper actual asymptotic for \(T_j^{SEL2,conv}\).

Proof.

Definition 17.3 substitutes the fundamental Casimir
\(C_2(F_N)=(N^2-1)/(2N)\) into the general Section-16 margins.  The three
cases are exactly Theorem 16.2.  The numerical values in the two diagnostic
tables are direct evaluations of the same formula with zero slacks and either
\(G_{16}=1+\log 19\) or the optimistic upper bound
\(G_{16}<1+\log 19+\log2\).  The absence of a numerical \(s\)-row prevents an
unconditional pass/fail verdict. `square`

### Corollary 17.5: What Steps 1--3 Decide

Steps 1--3 are now complete in the precise finite-record sense.

1. Candidate channels are frozen to \(SU(2),SU(3),SU(4)\) fundamental rows,
   with the general \(SU(N)\) fundamental formula retained.
2. Selector parameters are frozen as far as the current text allows:
   only ranges and the optimistic adaptive ceiling are sourced.
3. `TREE-TIME` has an exact row classifier, but not a numerical verdict.

Therefore the next paper move cannot honestly be "evaluate the surface
prefactor" and should not blindly attack arbitrary escape sets.  The next
source task is one of:

```math
\mathrm{P22\text{-}TTIME\text{-}ROW}
:
\text{print an actual admissible }
(N,s,\epsilon_A,\chi,\widehat\eta_{*,20})
\text{ row,}
```

or

```math
\mathrm{P22\text{-}SURF\text{-}GROW\text{-}SHARP}
:
\text{lower }G_{13,tree}^{SEL2}
\text{ and rerun the same classifier.}
```

Only after `TREE-TIME` has a pass row should the cofinal escape-ceiling
functional \(\mathcal E_\rho^{cof,SEL2}\) be evaluated as the mainline.

## 18. `P22-TTIME-ROW`: A Concrete Selector-Time Row Source

Section 17 left `TREE-TIME` as an exact classifier.  This section does the
next finite-record task: print a concrete time-row source theorem and isolate
the only missing active-branch certification.  The row printed here is not an
area-law input and not a continuum measure assumption.  It is a finite selector
row with declared scalar parameters.

### Definition 18.1: The Time-Row Gate

For \(N\ge2\), let \(F_N\) be the fundamental channel.  The gate

```math
\mathrm{P22\text{-}TTIME\text{-}ROW}
(N,s,\epsilon_A,\chi,\widehat\eta)
```

holds when the following finite scalar-record clauses are all true.

1. The `SEL2` sheet selector is frozen with

   ```math
   L_j=\lfloor\sqrt{sH_j}\rfloor,
   \qquad H_j=g_{i(j)}^{-2},
   ```

   and the standard sheet-time audit of Paper 20 Definition
   4.3A.160BA holds.

2. The slacks and activity ceiling are certified on the same pushed-forward
   record law:

   ```math
   0<\epsilon_A<1,\qquad
   0<\chi<1,\qquad
   0\le\widehat\eta<1.
   ```

3. The activity ceiling used in the rooted tree threshold is bounded by
   \(\widehat\eta\):

   ```math
   \widehat\eta_{*,20}\le\widehat\eta.
   ```

4. The strict selector-time inequality holds:

   ```math
   s>
   {4N\over N^2-1}
   {1+\log 19+20\widehat\eta/(1-\widehat\eta)
   \over(1-\epsilon_A)(1-\chi)}.
   ```

This is a time-row gate only.  It does not assert `ESC-MASS` and does not
assert the final surface prefactor cap.

### Lemma 18.2: The AF-Area Parameter Is A Legitimate Finite Selector Parameter

For every fixed \(s>0\), the choice

```math
L_j=\lfloor\sqrt{sH_j}\rfloor
```

is a legitimate frozen `SEL2` AF-area selector.  It gives

```math
{L_j^2\over H_j}\to s,
\qquad
{L_j\over H_j}\to0.
```

Consequently the collar term \(B_j^{sheet}=O(L_j)\) remains lower order in the
block-time calculation.

Proof.

The floor error is \(O(\sqrt{H_j})\), so

```math
L_j^2=sH_j+O(\sqrt{H_j}),
```

and \(L_j^2/H_j\to s\).  Also \(L_j/H_j=O(H_j^{-1/2})\to0\).  This is exactly
the scaling used in Paper 20 Theorem 4.3A.160BB to evaluate
\(T_j^{SEL2,conv}\).  The selector must be frozen before the row is evaluated;
once frozen, no hidden cofinal reselection or continuum process is being
introduced. `square`

### Lemma 18.3: Time-Row Gate Implies `TREE-TIME`

If

```math
\mathrm{P22\text{-}TTIME\text{-}ROW}
(N,s,\epsilon_A,\chi,\widehat\eta)
```

holds, then

```math
\mathrm{P20\text{-}SEL2\text{-}TREE\text{-}TIME}(F_N)
```

holds.

Proof.

The strict inequality in Definition 18.1 gives

```math
s(1-\epsilon_A)(1-\chi)
>
{4N\over N^2-1}
\left(1+\log 19+{20\widehat\eta\over1-\widehat\eta}\right).
```

Since \(\widehat\eta_{*,20}\le\widehat\eta\) and
\(C_2(F_N)=(N^2-1)/(2N)\), the right side is at least
\(\Theta_T^{tree}(F_N)\).  Therefore

```math
T_{clean,-}^{SEL2}=s(1-\epsilon_A)(1-\chi)
>
\Theta_T^{tree}(F_N),
```

and Theorem 15.3 applies. `square`

### Definition 18.4: A Log-2 Activity `SU(4)` Time Row

Let

```math
\eta_{\log2}
:=
{\log2\over 20+\log2}.
```

Equivalently,

```math
{20\eta_{\log2}\over 1-\eta_{\log2}}=\log2,
\qquad
\eta_{\log2}=0.033496\ldots .
```

This is the natural activity ceiling singled out by the Paper-21 optimistic
adaptive worksheet: it is exactly the condition under which the rooted
activity contribution is bounded by the extra \(\log2\) in Theorem 6.4 of
Paper 21.  It is weaker, and therefore better sourced, than the previously
displayed ad hoc value \(3/100\).

Define the concrete candidate row

```math
\mathfrak W_{18}^{SU4}
:=
\left(
N=4,\rho=F_4,\,
s={51\over10},\,
\epsilon_A={1\over100},\,
\chi={1\over100},\,
\widehat\eta=\eta_{\log2}
\right).
```

For this row,

```math
C_2(F_4)={15\over8},
```

and

```math
G_{18}^{SU4}
:=
1+\log 19
+{20\eta_{\log2}\over1-\eta_{\log2}}
=1+\log19+\log2
=4.637586\ldots.
```

The certified pass endpoint is

```math
S_{T,4}^{pass}
=
{2G_{18}^{SU4}\over(15/8)(99/100)^2}
=5.047197\ldots.
```

Thus

```math
{51\over10}-S_{T,4}^{pass}
>0.0528.
```

### Theorem 18.5: Conditional Printed Row

If the active pushed-forward `SEL2` scalar law certifies

```math
\epsilon_A\le {1\over100},
\qquad
\chi\le {1\over100},
\qquad
\widehat\eta_{*,20}\le \eta_{\log2}
={\log2\over20+\log2},
```

then the concrete row \(\mathfrak W_{18}^{SU4}\) satisfies

```math
\mathrm{P22\text{-}TTIME\text{-}ROW}
\left(4,{51\over10},{1\over100},{1\over100},\eta_{\log2}\right),
```

and therefore

```math
\mathrm{P20\text{-}SEL2\text{-}TREE\text{-}TIME}(F_4)
```

holds on that same scalar record law.

Proof.

Definition 18.4 computes the pass endpoint using the worst allowed values in
the displayed certification bounds.  Since \(s=5.1\) is strictly above that
endpoint, Definition 18.1 holds.  Lemma 18.3 then gives the tree-time gate.
`square`

### Theorem 18.6: Current Active-Branch Verdict For `P22-TTIME-ROW`

The current corpus prints a concrete conditional row, Theorem 18.5, but it
does not yet print the active unconditional row.

More precisely:

1. `s` itself is not the obstruction.  Lemma 18.2 shows that once a finite
   selector value is chosen, the AF-area selector can realize it without
   changing the ontology of the record law.
2. The actual missing active data are the same-record small-slack/activity
   certifications

   ```math
   \epsilon_A\le {1\over100},
   \qquad
   \chi\le {1\over100},
   \qquad
   \widehat\eta_{*,20}\le \eta_{\log2}
   ={\log2\over20+\log2},
   ```

   or any alternative bounds strong enough to make the inequality in
   Definition 18.1 strict for a declared \(N\) and \(s\).
3. If those certifications are supplied, `TREE-TIME` passes and the mainline
   moves to the cofinal escape-ceiling functional

   ```math
   \mathcal E_{F_4}^{cof,SEL2}.
   ```

4. If such certifications cannot be supplied for any reasonable fundamental
   channel, the correct next move is not to attack escape.  It is to lower
   \(G_{13,tree}^{SEL2}\) by sharpening the same-record surface-growth theorem.

Proof.

Item 1 is Lemma 18.2.  Item 2 is the distinction between a conditional finite
row and an active row: Papers 20--21 state the selector-time formulas and
activity worksheets, but do not print the displayed numerical small-slack
certificate on the active branch.  Item 3 is Theorem 18.5.  Item 4 follows
from the monotonicity of the tree-time endpoint in \(G_{13,tree}^{SEL2}\),
\(\epsilon_A\), and \(\chi\). `square`

### Corollary 18.7: Updated Next Step

`P22-TTIME-ROW` has been pushed to a finite, checkable source certificate.  The
next executable task is no longer "choose \(s\)" in the abstract.  It is one of:

```math
\mathrm{P22\text{-}SMALL\text{-}SLACK\text{-}ACTIVITY}
\left({1\over100},{1\over100},\eta_{\log2}\right),
```

which would activate the printed `SU(4)` row, or

```math
\mathrm{P22\text{-}SURF\text{-}GROW\text{-}SHARP},
```

which would lower the threshold and rerun the row classifier.  Escape remains
downstream of this decision.

## 19. Small-Slack Tightening On The Same `SEL2` Law

Section 18 left a mixed source condition:

```math
\epsilon_A\le {1\over100},
\qquad
\chi\le {1\over100},
\qquad
\widehat\eta_{*,20}\le\eta_{\log2}.
```

This section closes the first two inequalities.  The point is modest but
important: \(\epsilon_A\) and \(\chi\) are not dynamical escape data.  They are
tail-window tolerances for already frozen selector-time convergences.  Passing
farther out on the same cofinal `SEL2` row tightens them without changing the
pushed-forward scalar records.

### Definition 19.1: `P22-SLACK-TIGHT`

For \(0<\epsilon_0<1\) and \(0<\chi_0<1\), the certificate

```math
\mathrm{P22\text{-}SLACK\text{-}TIGHT}(\epsilon_0,\chi_0)
```

means that the active standard `SEL2` selector can be evaluated on a cofinal
tail, with the same pushed-forward scalar law restricted to that tail, so that

```math
s(1-\epsilon_0)
\le {S_j\over H_j}
\le s(1+\epsilon_0),
\qquad
1-\chi_0
\le {t_{i(j)}\over g_{i(j)}^2}
\le 1+\chi_0,
```

where

```math
H_j=g_{i(j)}^{-2},
\qquad
L_j=\lfloor\sqrt{sH_j}\rfloor,
\qquad
S_j=L_j^2.
```

It also includes the preservation clause: every exact zero, finite row map,
finite comparison envelope, finite inverse/admissibility tag, and finite-depth
reduced-tail statement already proved in Sections 11--14 remains valid on the
tightened tail.

### Lemma 19.2: AF-Area Slack Can Be Made Arbitrarily Small

For every \(0<\epsilon_0<1\), the standard `SEL2` square selector satisfies

```math
s(1-\epsilon_0)
\le {S_j\over H_j}
\le s(1+\epsilon_0)
```

on a cofinal tail.

Proof.

By the standard `SEL2` selector,

```math
L_j=\lfloor\sqrt{sH_j}\rfloor,
\qquad
S_j=L_j^2.
```

Since \(H_j\to\infty\),

```math
L_j^2=sH_j+O(\sqrt{H_j}),
```

and therefore

```math
{S_j\over H_j}
=s+O(H_j^{-1/2})
\to s.
```

For any fixed \(\epsilon_0>0\), convergence to \(s\) gives the displayed
two-sided inequality after removing a finite prefix.  This is the same
selector used in Paper 20 Definition 1.4 and Paper 22 Lemma 18.2; no
observable, law, or representation channel is changed. `square`

### Lemma 19.3: Heat-Time Scheme Slack Can Be Made Arbitrarily Small

For every \(0<\chi_0<1\), the standard Paper-16/Paper-20 heat-kernel scheme
row satisfies

```math
1-\chi_0
\le {t_{i(j)}\over g_{i(j)}^2}
\le 1+\chi_0
```

on a cofinal tail.

Proof.

The imported finite heat-kernel scheme is normalized as

```math
t_i=g_i^2+O(g_i^4)
```

after the declared finite scheme choice; this is the Paper-16 local
heat-kernel normalization used by Paper 20's frozen selector.  Along the
cofinal AF row, \(g_{i(j)}\to0\), hence

```math
{t_{i(j)}\over g_{i(j)}^2}
=1+O(g_{i(j)}^2)
\to1.
```

For any fixed \(\chi_0>0\), convergence to \(1\) gives the displayed two-sided
inequality after deleting a finite prefix.  This is exactly the scheme-slack
tail of Paper 20 Definition 1.1, tightened rather than replaced. `square`

### Lemma 19.4: Cofinal Tail Tightening Preserves The Closed Finite Tables

Passing from the active `SEL2` row to the tail supplied by Lemmas 19.2--19.3
does not reopen Work Packages I--III.

Proof.

The pushed-forward scalar law is not replaced.  It is the same sequence of
finite scalar pushforwards read on a farther cofinal tail.  Exact zero
statements remain zero on every subsequence.  Limsup upper bounds and finite
carried envelopes cannot increase after deleting a finite prefix or passing to
a cofinal subsequence.  Finite row maps, comparison coefficients, inverse
tags, no-double-charge masks, and the support-cardinality rank of the licensed
pass graph are pointwise finite algebraic data, so their values are unchanged.

The finite-depth reduced-tail closure of Section 14 is also unchanged:

```math
T_{\ge K}^{red,act,22}(j)=0
\qquad(K>K_{\max}^{22}\le81)
```

is a pointwise structural statement for every surviving row.  Restricting to a
tail preserves it verbatim.  No lower-floor falsification is being used in
Sections 11--18, so no negative certificate is discarded. `square`

### Theorem 19.5: `P22-SLACK-TIGHT(0.01,0.01)`

The active standard `SEL2` branch satisfies

```math
\boxed{
\mathrm{P22\text{-}SLACK\text{-}TIGHT}
\left({1\over100},{1\over100}\right).
}
```

Consequently, on the tightened tail,

```math
\epsilon_A\le {1\over100},
\qquad
\chi\le {1\over100}
```

are certified on the same pushed-forward scalar law, and all Sections 11--14
finite-table closures remain closed.

Proof.

Apply Lemma 19.2 with \(\epsilon_0=1/100\) and Lemma 19.3 with
\(\chi_0=1/100\).  Intersect the two cofinal tails.  The intersection is still
cofinal, and Lemma 19.4 proves preservation of the already closed finite
tables.  This is exactly Definition 19.1. `square`

### Corollary 19.6: Updated Time-Row Source Target

After Theorem 19.5, the conditional `SU(4)` row of Theorem 18.5 has only one
remaining active source input:

```math
\widehat\eta_{*,20}\le\eta_{\log2}
={\log2\over20+\log2}.
```

Equivalently, the next live gate is

```math
\mathrm{P22\text{-}ACTIVITY\text{-}LOG2}.
```

If this activity gate is proved on the same tightened `SEL2` scalar law, then

```math
\mathrm{P22\text{-}TTIME\text{-}ROW}
\left(4,{51\over10},{1\over100},{1\over100},\eta_{\log2}\right)
```

holds, and therefore `P20-SEL2-TREE-TIME(F_4)` holds.  If it cannot be proved,
the correct continuation remains `P22-SURF-GROW-SHARP`, not `ESC-MASS`.

## 20. Active Log-2 Activity Bound

Section 19 reduced the printed `SU(4)` time row to one source input:

```math
\widehat\eta_{*,20}<\eta_{\log2}
={\log2\over20+\log2}.
```

This section closes that input on the active standard `SEL2` law.  The key
point is that Paper 21's log-2 estimate did not actually depend on the
zero-nonsurface-debit probe.  The zero-debit probe used the estimate to prove
nonempty feasibility, but the activity estimate itself is already a consequence
of the Paper-20 active worksheet.

### Definition 20.1: `P22-ACTIVITY-LOG2`

The gate

```math
\mathrm{P22\text{-}ACTIVITY\text{-}LOG2}
```

holds when the active frozen standard `SEL2` worksheet satisfies

```math
\widehat\eta_{*,20}<\eta_{\log2}
={\log2\over20+\log2}
```

on the same pushed-forward scalar law used by Sections 11--19.

### Lemma 20.2: The Signal Logarithm Is Below `log 2`

For the active `SEL2` signal profile and every fixed \(s>0\),

```math
0<L_{20}(s)<\log2.
```

Proof.

Paper 21 Definition 5.1 writes the `SEL2` signal profile as

```math
F_\rho(s)
=
e^{-a_\rho s}\left(1-e^{-b_\rho s}\right),
```

with \(a_\rho>0\) and \(b_\rho>0\).  Hence

```math
0<e^{-a_\rho s}<1,
\qquad
0<1-e^{-b_\rho s}<1,
```

and therefore \(0<F_\rho(s)<1\).  Since

```math
L_{20}(s)=\log(1+F_\rho(s)),
```

we get \(0<L_{20}(s)<\log2\). `square`

### Lemma 20.3: The Active Worksheet Implies The Log-2 Activity Ceiling

On every active standard `SEL2` worksheet satisfying the Step-2 strictness
condition

```math
0<\bar\eta_{res,20}(s)<\tau_{20}(s),
```

one has

```math
\widehat\eta_{*,20}(s)<\eta_{\log2}.
```

Proof.

By Paper 20 Definition 4.3A.43, equivalently Paper 21 Definition 5.5,

```math
\tau_{20}(s)
={L_{20}(s)\over20+L_{20}(s)},
\qquad
\widehat\eta_{*,20}(s)
={1\over2}\left(\tau_{20}(s)+\bar\eta_{res,20}(s)\right).
```

The active worksheet is declared frozen only on the strict tail

```math
0<\bar\eta_{res,20}(s)<\tau_{20}(s).
```

Thus

```math
\widehat\eta_{*,20}(s)<\tau_{20}(s).
```

The map \(L\mapsto L/(20+L)\) is strictly increasing for \(L>0\).  Lemma
20.2 gives \(L_{20}(s)<\log2\), so

```math
\tau_{20}(s)
={L_{20}(s)\over20+L_{20}(s)}
<
{\log2\over20+\log2}
=\eta_{\log2}.
```

Combining the two strict inequalities gives the claim.  Notice that no
pre-surface debit \(U_{pre13}\) appears in this proof.  It uses only the active
decoration worksheet, not the optimistic zero-debit feasibility probe.
`square`

### Theorem 20.4: `P22-ACTIVITY-LOG2` Is Closed

On the active standard `SEL2` branch used by Paper 22,

```math
\boxed{
\mathrm{P22\text{-}ACTIVITY\text{-}LOG2}
}
```

holds.

Proof.

The active branch imported from Paper 20 is the frozen unit-normalized
`SEL2` worksheet of Definition 4.3A.43 after Step 2 strictness has been proved
by Lemma 4.3A.50 and Theorem 4.3A.51.  Therefore the hypothesis of Lemma 20.3
holds on the same pushed-forward scalar law.  Lemma 20.3 gives
\(\widehat\eta_{*,20}<\eta_{\log2}\), which is Definition 20.1. `square`

### Corollary 20.5: The `SU(4)` `TREE-TIME` Row Passes

On the active standard `SEL2` branch, after the slack tightening of Theorem
19.5 and the activity bound of Theorem 20.4,

```math
\mathrm{P22\text{-}TTIME\text{-}ROW}
\left(4,{51\over10},{1\over100},{1\over100},\eta_{\log2}\right)
```

holds.  Consequently,

```math
\boxed{
\mathrm{P20\text{-}SEL2\text{-}TREE\text{-}TIME}(F_4)
}
```

holds on that same scalar law.

Proof.

Theorem 19.5 supplies
\(\epsilon_A\le1/100\) and \(\chi\le1/100\) on a cofinal tail without changing
the scalar law.  Theorem 20.4 supplies
\(\widehat\eta_{*,20}<\eta_{\log2}\).  The concrete numerical inequality for
the `SU(4)` row was computed in Definition 18.4:

```math
{51\over10}
>
{2(1+\log19+\log2)\over(15/8)(99/100)^2}
=5.047197\ldots .
```

Therefore Definition 18.1 holds for the displayed row, and Lemma 18.3 gives
`P20-SEL2-TREE-TIME(F_4)`. `square`

### Corollary 20.6: Updated Main Obstruction

The tree-time half of the Paper-20 tree-rate gate is now closed on the active
standard `SEL2` branch, for the fundamental `SU(4)` channel \(F_4\).  The
remaining rate obstruction is the escape half:

```math
\mathrm{P20\text{-}SEL2\text{-}ESC\text{-}MASS}
(V_{F_4},\gamma_{F_4},q_{F_4}),
```

equivalently, in the exact ceiling language of Section 16,

```math
\mathcal E_{F_4}^{cof,SEL2}
>
\Theta_{esc}^{tree}.
```

Thus the next mainline task is now to evaluate or sharply bound
\(\mathcal E_{F_4}^{cof,SEL2}\).  Surface-growth sharpening remains a useful
fallback only if the escape ceiling is too high for the active law.

## 21. The \(F_4\) Cofinal Escape-Ceiling Decision

Section 20 closed the time half of the tree-rate gate.  This section evaluates
what can actually be evaluated about the escape half from the current corpus.
The result is intentionally sharp: the existing coefficient and time data do
not close `ESC-MASS`; they reduce it to one near-maximal same-record tail
source.

### Definition 21.1: The Frozen \(F_4\) Escape Variable

On the active standard `SEL2` law, specialize Definition 16.3 to the
fundamental `SU(4)` channel \(F_4\).  Write

```math
\psi_4(U):={\Phi_{F_4}(U)\over4},
\qquad
X_4(U):=1-\psi_4(U).
```

Paper 20 Lemma 4.3A.160AI gives

```math
-1\le\psi_4(U)\le1,
\qquad
0\le X_4(U)\le2.
```

With the paired fundamental convention, \(\Phi_{F_4}=\operatorname{Re}\chi_F\).
Since \(-I\in SU(4)\) and \(\chi_F(-I)=-4\), the endpoint \(X_4=2\) is
attained.  Hence the exact escape ceiling may be written as

```math
\mathcal E_{F_4}^{cof,SEL2}
=
\sup_{0<\gamma\le2}
\gamma Q_{4,\gamma}^{SEL2},
```

where

```math
Q_{4,\gamma}^{SEL2}
:=
\liminf_j
\nu_{p,j}^{SEL2}\{U:X_4(U)\ge\gamma\}.
```

This is the largest possible fixed central escape product at character gap
\(\gamma\) on the same pushed-forward scalar law.

### Definition 21.2: The Active Escape Threshold Interval

For the active branch, set

```math
G_{4}^{act}
:=
1+\log19
+20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}},
```

and

```math
\Theta_{4}^{act}
:=
1-\exp(-G_{4}^{act}).
```

By Theorem 20.4,

```math
0\le\widehat\eta_{*,20}<\eta_{\log2}
={\log2\over20+\log2}.
```

Therefore

```math
\Theta_{4}^{min}
:=
1-{1\over19e}
=0.980637924\ldots
\le
\Theta_{4}^{act}
<
1-{1\over38e}
=0.990318962\ldots
=:
\Theta_{4}^{\log2}.
```

The exact `ESC-MASS` pass condition is

```math
\mathcal E_{F_4}^{cof,SEL2}>\Theta_{4}^{act}.
```

Thus \(\mathcal E_{F_4}^{cof,SEL2}>\Theta_{4}^{\log2}\) is a sufficient
uniform pass certificate for the entire active log-2 branch, while
\(\mathcal E_{F_4}^{cof,SEL2}\le\Theta_{4}^{min}\) is a uniform failure
certificate for every allowed activity value.

### Lemma 21.3: The \(F_4\) Escape Gate Is Exactly This Tail Inequality

On the active standard `SEL2` law,

```math
\mathrm{P20\text{-}SEL2\text{-}ESC\text{-}MASS}
(V_{F_4},\gamma_{F_4},q_{F_4})
```

holds for some fixed central escape set if and only if

```math
\mathcal E_{F_4}^{cof,SEL2}>\Theta_{4}^{act}.
```

Proof.

This is Lemma 16.4 with \(\rho=F_4\) and
\(G_{16}=G_4^{act}\).  Definition 21.1 only restricts the supremum to
\(0<\gamma\le2\), which is harmless because \(0\le X_4\le2\). `square`

### Lemma 21.4: The Moment Ceiling Leaves Only A Narrow Escape Band

Define the cofinal \(F_4\) first-moment deficit

```math
M_4^{cof}
:=
\liminf_j
\int X_4(U)\,d\nu_{p,j}^{SEL2}(U)
=
\liminf_j
\left(1-\widetilde a_{F_4,j}^{SEL2}\right).
```

Then

```math
\mathcal E_{F_4}^{cof,SEL2}\le M_4^{cof}.
```

For the active row printed in Section 18,

```math
s={51\over10},
\qquad
\epsilon_A=\chi={1\over100},
\qquad
C_2(F_4)={15\over8},
```

the Paper-20 time window gives

```math
T_-={51\over10}\left({99\over100}\right)^2
=4.99851,
```

and

```math
T_+={51\over10}\left({101\over100}\right)^2
=5.20251.
```

Consequently the same first-moment deficit lies in the licensed interval

```math
1-\exp\left(-{15\over16}T_-\right)
\le
\liminf_j\left(1-\widetilde a_{F_4,j}^{SEL2}\right)
\le
\limsup_j\left(1-\widetilde a_{F_4,j}^{SEL2}\right)
\le
1-\exp\left(-{15\over16}T_+\right),
```

up to the already closed \(o(1)\) scalar-comparison error.  Numerically,

```math
1-\exp\left(-{15\over16}T_-\right)
=0.990777444\ldots,
```

and

```math
1-\exp\left(-{15\over16}T_+\right)
=0.992382850\ldots.
```

Thus even the licensed first-moment room above the uniform log-2 escape target

```math
\Theta_{4}^{\log2}=0.990318962\ldots
```

is narrow.  The lower endpoint clears \(\Theta_4^{\log2}\) by only

```math
0.000458482\ldots.
```

Proof.

The inequality

```math
\gamma\mathbf 1_{\{X_4\ge\gamma\}}\le X_4
```

gives \(\mathcal E_{F_4}^{cof,SEL2}\le M_4^{cof}\), exactly as in Lemma 16.5.
The time-window bounds are Paper 20 Theorem 4.3A.160BB together with the
strict scalar coefficient comparison already used in Lemma 15.2:

```math
\widetilde a_{F_4,j}^{SEL2}
=
\exp\left(-{15\over16}T_j^{SEL2,conv}\right)+o(1).
```

Since \(T_-\le T_j^{SEL2,conv}\le T_+\) cofinally and
\(1-e^{-15T/16}\) is increasing in \(T\), the displayed interval follows.
The decimal values are direct evaluations. `square`

### Lemma 21.5: The Existing Coefficient-Gap Extraction Cannot Close Escape

The escape lower bound obtained from Paper 20 Lemma 4.3A.160AQ.2 can never
prove the present `F_4` escape gate.  More precisely, if the only supplied
input is a normalized coefficient gap

```math
\limsup_j\widetilde a_{F_4,j}^{SEL2}\le1-\sigma
\qquad(0<\sigma\le1),
```

then the Paper-20 extraction gives, for \(0<\gamma<\sigma\),

```math
Q_{4,\gamma}^{SEL2}\ge{\sigma-\gamma\over2},
```

so the product certified by this argument is obtained only by choosing a
strict lower mass

```math
\gamma q
<
{\gamma(\sigma-\gamma)\over2}
\le
{\sigma^2\over8}
\le
{1\over8}.
```

But

```math
\Theta_{4}^{min}=1-{1\over19e}>0.9806.
```

Therefore no one-moment coefficient-gap extraction of this form can close
`P20-SEL2-ESC-MASS` for \(F_4\).

Proof.

The displayed lower mass is exactly Paper 20 Lemma 4.3A.160AQ.2.  Optimizing
\(\gamma(\sigma-\gamma)/2\) over \(0<\gamma<\sigma\) gives
\(\sigma^2/8\).  Since the normalized scalar readout satisfies
\(-1\le\psi_4\le1\), the coefficient gap satisfies \(\sigma\le1\) on the
positive branch relevant to the tree-rate gate.  The threshold comparison is
Definition 21.2. `square`

### Definition 21.6: The Missing Near-Maximal Tail Source

The remaining source theorem is the following same-record anti-concentration
statement:

```math
\mathrm{P22\text{-}F4\text{-}NEARMAX\text{-}TAIL}
```

holds if there exists a fixed \(0<\gamma\le2\) such that

```math
\gamma Q_{4,\gamma}^{SEL2}
>
\Theta_{4}^{act}.
```

Equivalently, a uniform sufficient version is

```math
\gamma Q_{4,\gamma}^{SEL2}
>
\Theta_{4}^{\log2}
=1-{1\over38e}.
```

Because the target is near one, this is not a generic noncollapse theorem.
It says that the active \(F_4\) scalar plaquette law puts enough cofinal mass
in the high-deficit tail of \(X_4=1-\psi_4\) to almost saturate the first
moment ceiling.

### Theorem 21.7: Closed Status Of The \(F_4\) Escape-Mass Evaluation

With the current Papers 10--12 and 20--22, the \(F_4\) escape-mass matter is
closed to the following exact decision.

1. `TREE-TIME` is closed for \(F_4\) by Corollary 20.5.
2. `ESC-MASS` is equivalent to

   ```math
   \mathcal E_{F_4}^{cof,SEL2}>\Theta_4^{act}.
   ```

3. The active log-2 row forces

   ```math
   0.980637924\ldots
   \le
   \Theta_4^{act}
   <
   0.990318962\ldots .
   ```

4. The current one-moment coefficient route cannot prove the inequality; its
   certified product is at most \(1/8\).
5. The current first-moment time row does not falsify the inequality either:
   the licensed moment ceiling is still above the uniform log-2 threshold.
6. Therefore the remaining live source is exactly

   ```math
   \mathrm{P22\text{-}F4\text{-}NEARMAX\text{-}TAIL},
   ```

   or else a same-record sharpening of the rooted surface-growth constant that
   lowers \(\Theta_4^{act}\) below the escape product actually available.

In particular, the present corpus does not prove continuum Yang-Mills
confinement on the strict `SEL2` branch yet: it has closed the finite-table
and tree-time side, but the \(F_4\) near-maximal cofinal escape tail remains
the active rate obstruction.

Proof.

Item 1 is Corollary 20.5.  Item 2 is Lemma 21.3.  Item 3 is Definition 21.2.
Item 4 is Lemma 21.5.  Item 5 is Lemma 21.4: the first-moment ceiling is too
high to give a failure theorem, while Lemma 21.5 says the same moment data
are too weak to give a pass theorem.  Hence the only remaining alternatives
are a direct near-maximal tail theorem on the same pushed-forward law or a
lowered surface-growth threshold. `square`

### Corollary 21.8: Next Execution Order

The next rigorous execution order is now forced.

1. Try to prove `P22-F4-NEARMAX-TAIL` directly for the active `SEL2` scalar
   law.  This must be a tail theorem for \(X_4=1-\psi_4\), not another
   coefficient-gap or noncollapse extraction.
2. If that fails or produces a product below \(\Theta_4^{act}\), return to
   surface-growth sharpening and lower \(G_{13,tree}^{SEL2}\).
3. Only after the escape inequality is strict should the Paper-13 surface
   prefactor cap be evaluated.

This is the Barandes-aligned form of the obstruction: every object is a
finite pushed-forward scalar record, and no continuum Yang-Mills measure,
area-law assumption, or hidden gauge-coordinate ontology is imported.

## 22. Near-Maximal Tail Attack And Surface-Lowering Fallback

Section 21 closed the first evaluation of
\(\mathcal E_{F_4}^{cof,SEL2}\): the existing coefficient extraction cannot
prove it, but the first moment does not falsify it.  This section pushes both
available exits to their present source boundary.

### Definition 22.1: Escape Product And Equivalent Surface Exponent

For any same-record lower tail certificate

```math
P_{esc}
\le
\mathcal E_{F_4}^{cof,SEL2},
```

define its equivalent surface exponent

```math
G_{esc}(P_{esc})
:=
-\log(1-P_{esc}),
\qquad 0<P_{esc}<1.
```

The escape half passes against a surface-growth exponent \(G\) exactly when

```math
P_{esc}>1-e^{-G},
```

equivalently

```math
G<G_{esc}(P_{esc}).
```

Thus lowering surface growth and proving a larger escape tail are two ways of
moving the same inequality.

### Lemma 22.2: The Existing \(1/8\) Escape Route Would Require A Radical Surface Bound

The strongest product available from the current one-moment coefficient-gap
extraction is at most

```math
P_{esc}^{mom}\le {1\over8}.
```

Therefore that route can pass only if the surface-growth exponent is lowered
to

```math
G<-\log\left(1-{1\over8}\right)
=\log{8\over7}
=0.133531392\ldots .
```

The current rooted tree surface exponent, even before the log-2 activity
addition, is

```math
1+\log19=3.944438979\ldots .
```

With the active log-2 ceiling it is bounded by

```math
G_4^{act}<1+\log19+\log2
=4.637586159\ldots .
```

Hence the already-proved positive escape source cannot be rescued by any
bookkeeping-level sharpening of the current rooted-tree surface count.  It
would require a new surface theorem reducing the exponential growth by more
than

```math
(1+\log19)-\log(8/7)
=3.810907586\ldots
```

even before activity is charged.

Proof.

The product ceiling \(1/8\) is Lemma 21.5, imported from Paper 20 Theorem
4.3A.160BH.40T.4.  Definition 22.1 converts any product \(P_{esc}\) into the
largest surface exponent it can beat.  Substituting \(P_{esc}=1/8\) gives
\(\log(8/7)\).  Paper 20 Theorem 4.3A.160BH.40P and Corollary
4.3A.160BH.40Q give the current rooted-tree floor \(1+\log19\), while Paper
22 Theorem 20.4 gives the active log-2 ceiling. `square`

### Lemma 22.3: The First Moment Is In Principle Large Enough, But Only If The Tail Nearly Saturates It

For the active \(F_4\) row of Sections 18--21, the licensed lower first-moment
deficit is

```math
M_{4,-}
:=
1-\exp\left(
-{15\over16}
{51\over10}\left({99\over100}\right)^2
\right)
=0.990777444\ldots .
```

Its equivalent exponent is

```math
G_{esc}(M_{4,-})
=
{15\over16}
{51\over10}\left({99\over100}\right)^2
=4.686103125\ldots .
```

The active log-2 surface exponent obeys

```math
G_4^{act}<1+\log19+\log2
=4.637586159\ldots .
```

Thus a tail certificate that saturated the first-moment deficit would pass,
with exponent room at least

```math
4.686103125\ldots-4.637586159\ldots
=0.048516965\ldots .
```

However, Lemma 21.4 gives only

```math
\mathcal E_{F_4}^{cof,SEL2}\le M_4^{cof}.
```

It gives no lower tail saturation.  The missing theorem is exactly the
conversion from a large first moment of \(X_4\) to a large fixed-threshold
cofinal tail product.

Proof.

The numerical value of \(M_{4,-}\) is Lemma 21.4.  The identity
\(G_{esc}(1-e^{-R})=R\) gives the displayed exponent.  The comparison with
\(G_4^{act}\) is Theorem 20.4.  The final statement is the direction of Lemma
16.5: moment bounds upper-bound the escape ceiling; they do not lower-bound
it. `square`

### Lemma 22.4: The \(F_4\) First Moment Does Not Force A Near-Maximal Tail

Fix any number \(M\) with

```math
\Theta_4^{\log2}<M<1.
```

There are central probability laws on \(SU(4)\) with the same \(F_4\)
coefficient deficit

```math
\int X_4\,d\nu=M
```

but with opposite escape-ceiling verdicts at the log-2 target:

```math
\mathcal E_{F_4}^*(\nu)>\Theta_4^{\log2}
```

for one law, and

```math
\mathcal E_{F_4}^*(\nu)<\Theta_4^{\log2}
```

for another law.

Proof.

For the passing law, use the two central group elements \(I\) and \(-I\).  At
these points \(X_4(I)=0\) and \(X_4(-I)=2\).  Set

```math
\nu_{pass}:={M\over2}\delta_{-I}
+\left(1-{M\over2}\right)\delta_I .
```

Then \(\int X_4\,d\nu_{pass}=M\), and at \(\gamma=2\),

```math
\gamma\nu_{pass}\{X_4\ge\gamma\}=M>\Theta_4^{\log2}.
```

For the failing law, choose \(c\) with

```math
0<c<\Theta_4^{\log2},
\qquad
{2(M-c)\over2-c}<\Theta_4^{\log2}.
```

Such a \(c\) exists by taking \(c\) sufficiently close to
\(\Theta_4^{\log2}\): at \(c=\Theta_4^{\log2}\) the second left side is
\[
{2(M-\Theta_4^{\log2})\over 2-\Theta_4^{\log2}}
<
{2(1-\Theta_4^{\log2})\over 2-\Theta_4^{\log2}}
<
\Theta_4^{\log2},
\]
because \(\Theta_4^{\log2}>0.98\).  By continuity the same strict inequality
holds for \(c<\Theta_4^{\log2}\) sufficiently close to
\(\Theta_4^{\log2}\).  Choose a conjugacy class
\(\mathcal C_c\subset SU(4)\) with \(X_4=c\); for example, for \(0<c<1\) take

```math
U_\alpha=\operatorname{diag}(e^{i\alpha},e^{-i\alpha},1,1),
\qquad
{1+\cos\alpha\over2}=1-c.
```

Let \(\omega_c\) be the central orbital probability measure on
\(\mathcal C_c\), and set

```math
p:={M-c\over2-c},
\qquad
\nu_{fail}:=p\delta_{-I}+(1-p)\omega_c .
```

Then

```math
\int X_4\,d\nu_{fail}=2p+c(1-p)=M.
```

For \(0<\gamma\le c\), the product is at most \(c\).  For
\(c<\gamma\le2\), only the atom at \(-I\) contributes, so the product is at
most \(2p\).  By construction,

```math
\mathcal E_{F_4}^*(\nu_{fail})
\le
\max\{c,2p\}
<
\Theta_4^{\log2}.
```

The two laws have the same \(F_4\) coefficient deficit but opposite escape
ceilings.  Therefore the \(F_4\) first moment, even when it lies above the
escape threshold, does not imply `P22-F4-NEARMAX-TAIL`. `square`

### Theorem 22.5: Current-Source No-Go For Proving `P22-F4-NEARMAX-TAIL`

The present corpus cannot prove `P22-F4-NEARMAX-TAIL` from the closed
tree-time/coefficient data alone.  More precisely:

1. Paper 20's exact \(F_4\) coefficient comparison supplies the first
   moment of \(X_4\), up to \(o(1)\), through

   ```math
   \widetilde a_{F_4,j}^{SEL2}
   =
   \int\psi_4\,d\nu_{p,j}^{SEL2}.
   ```

2. Lemma 22.4 shows that this first moment is compatible with both a passing
   and a failing escape ceiling.
3. Papers 10--12 provide projective finite-battery transport, RG residual
   ledgers, and loop-readout controls, but they do not export a lower
   anti-concentration theorem for the tail event

   ```math
   \{X_4\ge\gamma\}.
   ```

4. Papers 20--21 explicitly park `ESC-MASS` at this same-record scalar source
   and warn that positive noncollapse is too weak.

Consequently `P22-F4-NEARMAX-TAIL` remains a genuine new source theorem.  It
is not derivable from the closed Paper-22 finite-table work, the closed
`TREE-TIME` row, or the existing positive escape extraction.

Proof.

Item 1 is the strict scalar comparison used in Lemmas 15.2 and 21.4.  Item 2
is Lemma 22.4.  Items 3 and 4 are the import boundaries stated in Papers
10--12, Paper 20 Corollary 4.3A.160AQ.5 and Theorem 4.3A.160BH.40T.4, and
Paper 21 Honest Boundary 3.4.  Since a theorem cannot be proved from source
data that admit both the theorem and its negation on the target observable,
the current source package is insufficient. `square`

### Corollary 22.6: What A Real Tail Proof Must Add

A successful direct proof must add at least one of the following same-record
inputs.

1. **Tail distribution source.**  A cofinal lower bound

   ```math
   \liminf_j\nu_{p,j}^{SEL2}\{X_4\ge\gamma\}
   >
   {\Theta_4^{act}\over\gamma}
   ```

   for some fixed \(\gamma>\Theta_4^{act}\).

2. **Moment-saturation source.**  A theorem showing that the deficit
   \(X_4\) is cofinally concentrated in one high-deficit band, so that
   \(\mathcal E_{F_4}^{cof,SEL2}\) is within
   \(o(1)\) of \(M_4^{cof}\).

3. **Law-level comparison source.**  A strong enough comparison of the actual
   pushed-forward `SEL2` plaquette law to an explicitly analyzed compact-group
   law for the tail functional itself, not merely for the normalized
   character coefficient.

Without one of these, the only rigorous continuation is the surface-growth
fallback.

### Theorem 22.7: Surface-Growth Fallback Target

Let \(P_{esc}^{avail}\) be the strongest same-record escape product actually
proved for the active `SEL2` law.  The surface-growth fallback must prove

```math
G_{13,new}^{SEL2}<-\log(1-P_{esc}^{avail}).
```

For the currently available coefficient-extraction product
\(P_{esc}^{avail}\le1/8\), this means

```math
G_{13,new}^{SEL2}<0.133531392\ldots .
```

Thus lowering activity from the log-2 ceiling to zero, or replacing
`3+log20` by `1+log19`, is not enough.  A fallback that relies on the existing
positive escape source would need a qualitatively new surface theorem, not a
minor sharpening of the present rooted-tree enumeration.

Proof.

The first display is Definition 22.1.  The numerical specialization is Lemma
22.2.  The final statement follows because the current best rooted geometry
exponent has the positive floor \(1+\log19\), far above \(\log(8/7)\).
`square`

### Corollary 22.8: Relentless Verdict

The attempted direct closure has reached a hard source boundary.

1. `P22-F4-NEARMAX-TAIL` is not proved by the current corpus.
2. The reason is not cosmetic: the closed \(F_4\) coefficient/time data do not
   determine the needed tail functional.
3. The surface-growth fallback is viable only if it either accompanies a much
   stronger escape product than \(1/8\), or proves a radically smaller
   same-record surface exponent.

Therefore the next valuable work is not another coefficient estimate.  It is
one of two new source projects:

```math
\mathrm{P22\text{-}F4\text{-}TAIL\text{-}LAW}
```

for the actual scalar law, or

```math
\mathrm{P22\text{-}SURF\text{-}EXP\text{-}RADICAL}
```

for the rooted surface-growth exponent.  Until one of those is supplied,
continuum Yang-Mills confinement remains open on the strict `SEL2` branch.

## 23. `P22-SURF-RADICAL-NO`: The \(1/8\) Escape Route Cannot Be Rescued By Full-Support Surface Lowering

Section 22 left a surface fallback: lower \(G_{13}^{SEL2}\) below
\(\log(8/7)\) if the only available escape product remains \(1/8\).  This
section proves that such a fallback is impossible for any honest full-support
same-boundary surface-polymer enumeration.  The proof is finite and local: a
single rooted plaquette already generates exponentially many reduced
same-boundary cube-bump surfaces.

### Definition 23.1: Full-Support Same-Boundary Surface Enumeration

A surface-growth replacement theorem is called full-support for the strict
reduced `SEL2` surface branch if, for every finite Creutz boundary containing
an exposed flat corner block plaquette \(p_0\), it counts every embedded
reduced plaquette surface obtained from the minimal sheet by replacing
\(p_0\) with the exposed boundary of a finite face-connected block-cube animal
in the normal half-space and outward tangent quadrant.

More explicitly, let \(n\) be one lattice direction normal to the minimal
sheet at \(p_0\), and let \(u,v\) be the two tangent lattice directions
pointing outward from the chosen corner of the minimal sheet.  A cube
animal \(\mathcal Q\) is admissible when:

1. its first cube has lower face \(p_0\);
2. all other cubes lie in the half-space on the \(+n\) side;
3. the cubes are face-connected;
4. no cube other than the first cube has a lower face contained in the
   original minimal sheet.

The associated nonminimal sheet is

```math
\Sigma(\mathcal Q)
:=
(\Sigma_0\setminus\{p_0\})
\cup
\left(\partial\mathcal Q\setminus\{p_0\}\right).
```

This operation preserves the boundary of \(\Sigma_0\).  It changes only the
finite scalar surface support; it does not introduce a new gauge coordinate,
new continuum measure, or off-record subprocess.

### Lemma 23.2: Cube-Bump Tubes Have Excess \(4m\)

If \(\mathcal Q\) is a face-connected cube animal with \(m\) cubes, tree
adjacency graph, and a single footprint face \(p_0\), then
\(\Sigma(\mathcal Q)\) has the same boundary as \(\Sigma_0\) and excess area

```math
|\Sigma(\mathcal Q)|-|\Sigma_0|=4m.
```

Proof.

The boundary of a tree-like \(m\)-cube animal has

```math
6m-2(m-1)=4m+2
```

faces, because each of the \(m-1\) face adjacencies removes two exposed cube
faces.  One boundary face is the footprint \(p_0\), which is glued to the
minimal sheet and not exposed in the replacement.  Thus the exposed cube
boundary contributes \(4m+1\) plaquettes.  The original sheet loses the one
plaquette \(p_0\).  The net increase is

```math
(4m+1)-1=4m.
```

Since \(\partial\mathcal Q\) is closed and \(p_0\) is glued exactly along the
removed plaquette, the exterior boundary of the sheet remains
\(\partial\Sigma_0\). `square`

### Lemma 23.3: Monotone Cube-Bump Tubes Give \(2^{m-1}\) Distinct Surfaces

For each word

```math
w=(w_1,\ldots,w_{m-1})\in\{u,v\}^{m-1},
```

define a cube tube by starting with the cube attached to \(p_0\) and then
placing the next cube one step in direction \(w_k\) from the previous cube,
always in the outward tangent quadrant at height one above the original
sheet.  These \(2^{m-1}\) words give
\(2^{m-1}\) distinct admissible cube animals, and therefore
\(2^{m-1}\) distinct reduced same-boundary surfaces of excess \(4m\).

Proof.

Every path uses only the positive tangent directions \(u\) and \(v\), so it is
self-avoiding.  Consecutive cubes share a face, and because \(u,v\) point into
the outward corner quadrant, no later cube has a lower face belonging to the
original minimal sheet.  The ordered monotone path is recovered from the set
of cube centers by reading the unique chain from the footprint cube to the
farthest cube in the partial order generated by \(u\) and \(v\).  Hence
different words give different cube animals.  Lemma 23.2 converts each animal
to a distinct same-boundary plaquette surface of excess \(4m\). `square`

### Theorem 23.4: Full-Support Surface Entropy Has A Positive Lower Bound

Let \(N_{surf}^{full}(q)\) be any full-support same-boundary surface count for
the strict reduced `SEL2` branch, counted at fixed root plaquette and fixed
boundary.  Then along \(q=4m\),

```math
N_{surf}^{full}(4m)\ge2^{m-1}.
```

Consequently every full-support surface-growth exponent satisfies

```math
G_{13,new}^{SEL2}
\ge
{1\over4}\log2
=0.173286795\ldots .
```

Proof.

The inequality is Lemma 23.3.  Taking logarithms gives

```math
{1\over4m}\log N_{surf}^{full}(4m)
\ge
{m-1\over4m}\log2,
```

and the right side tends to \((\log2)/4\).  Decoration activity is
nonnegative in the surface-polymer absolute-value bound, so adding decoration
cannot lower the exponent. `square`

### Theorem 23.5: `P22-SURF-RADICAL-NO`

On every full-support same-boundary surface-polymer route for the strict
reduced `SEL2` branch,

```math
G_{13,new}^{SEL2}
\ge
{1\over4}\log2
>
\log{8\over7}.
```

Numerically,

```math
{1\over4}\log2=0.173286795\ldots,
\qquad
\log{8\over7}=0.133531392\ldots .
```

Therefore no full-support same-boundary surface-growth theorem can rescue the
currently available \(1/8\) escape route.

Proof.

The lower bound is Theorem 23.4.  The strict numerical comparison is immediate.
By Theorem 22.7, an escape product \(P_{esc}\le1/8\) can pass only if

```math
G_{13,new}^{SEL2}<\log(8/7).
```

This contradicts the full-support lower bound. `square`

### Corollary 23.6: Consequence For The Strict `SEL2` Mainline

The surface fallback is now settled for the old escape source.

1. The existing coefficient-gap escape extraction, whose certified product is
   at most \(1/8\), cannot be saved by sharpening the full-support surface
   enumeration.
2. Any route that excludes the cube-bump tube family is no longer the same
   full-support Paper-13/Paper-19 surface-polymer route.  It must be declared
   as a new selector or signed-cancellation theorem and re-audited on the same
   scalar record law.
3. The only direct continuation on the present branch is therefore a stronger
   same-record \(F_4\) tail-law or moment-saturation theorem.

This is not a no-go theorem for confinement.  It is a no-go theorem for one
specific rescue strategy:

```math
\text{old }1/8\text{ escape source}
+\text{full-support surface-growth sharpening}.
```

## 24. Reference Heat-Kernel \(F_4\) Tail Diagnostic

Section 23 rules out the surface-growth rescue for the existing \(1/8\)
escape product.  The remaining direct possibility is a much stronger
same-record \(F_4\) tail law.  Before trying to prove such a law for the
actual `SEL2` scalar row, this section evaluates the corresponding compact
group heat-kernel reference.  This is a diagnostic for the reference branch,
not a replacement for the actual same-record theorem.

### Definition 24.1: The Heat-Kernel Reference Escape Ceiling

Let \(H_T\) be the central heat-kernel probability law on \(SU(4)\), with the
same normalization used in Papers 20--21:

```math
\int_{SU(4)}{\Phi_{F_4}(U)\over4}\,dH_T(U)
=
\exp\left(-{C_2(F_4)\over2}T\right),
\qquad
C_2(F_4)={15\over8}.
```

Define

```math
\mathcal E_{F_4}^{HK}(T)
:=
\sup_{0<\gamma\le2}
\gamma\,H_T\{U:X_4(U)\ge\gamma\},
```

where \(X_4=1-\operatorname{Re}\operatorname{tr}(U)/4\).

For the active row,

```math
T_-=
{51\over10}\left({99\over100}\right)^2
=4.99851,
\qquad
T_+=
{51\over10}\left({101\over100}\right)^2
=5.20251.
```

### Computation 24.2: Weyl-Integration Evaluation

Using the Weyl integration formula on \(SU(4)\), the heat-kernel density was
evaluated from the Peter-Weyl expansion

```math
K_T(U)
=
\sum_\lambda
d_\lambda e^{-C_2(\lambda)T/2}\chi_\lambda(U).
```

The finite computation retained all irreducibles with
\(C_2(\lambda)\le12\).  The first omitted Casimir level is \(12.5\), and the
omitted \(L^2\)-tail at \(T_-\) satisfies, by direct representation
enumeration together with the standard Weyl-polynomial/exponential tail
bound,

```math
{1\over2}
\left(
\sum_{C_2(\lambda)>12}
d_\lambda^2e^{-C_2(\lambda)T_-}
\right)^{1/2}
<
2.5\cdot10^{-12}.
```

Thus the character truncation error is negligible compared with the displayed
decimals.  The torus grid was checked at \(80^3,110^3,140^3\) shifted
midpoints.  The maxima stabilized as follows:

```math
\begin{array}{c|c|c|c}
\text{law} & \mathcal E & \gamma_* & H\{X_4\ge\gamma_*\}\\
\hline
\text{Haar} & 0.70359\ldots & 0.8078\ldots & 0.8710\ldots\\
H_{T_-} & 0.69373\ldots & 0.7993\ldots & 0.8679\ldots\\
H_{T_+} & 0.69547\ldots & 0.7993\ldots & 0.8701\ldots
\end{array}
```

At the actual log-2 escape threshold,

```math
\Theta_4^{\log2}=0.990318962\ldots,
```

the reference tail is much smaller:

```math
\Theta_4^{\log2}\,
H_{T_-}\{X_4\ge\Theta_4^{\log2}\}
=
0.50101\ldots,
```

and

```math
\Theta_4^{\log2}\,
H_{T_+}\{X_4\ge\Theta_4^{\log2}\}
=
0.50450\ldots .
```

### Lemma 24.3: Conservative Reference Envelope

For every \(T\in[T_-,T_+]\), the heat-kernel reference escape ceiling is far
below the active threshold.  A conservative envelope is

```math
\mathcal E_{F_4}^{HK}(T)<0.76.
```

Proof.

The Haar diagnostic gives

```math
\mathcal E_{F_4}^{Haar}
:=
\sup_{0<\gamma\le2}
\gamma\,\mu_{Haar}\{X_4\ge\gamma\}
=0.70359\ldots .
```

The heat-kernel density satisfies the standard \(L^2\) identity

```math
\|K_T-1\|_2^2
=
\sum_{\lambda\ne0}
d_\lambda^2e^{-C_2(\lambda)T}.
```

At \(T_-\) this gives

```math
{1\over2}\|K_{T_-}-1\|_2
=
0.026725263\ldots .
```

Hence total variation from Haar is at most \(0.026725263\ldots\) throughout
the active interval.  Therefore, for every \(\gamma\le2\),

```math
\gamma H_T\{X_4\ge\gamma\}
\le
\gamma \mu_{Haar}\{X_4\ge\gamma\}
+2\,\|H_T-\mu_{Haar}\|_{TV}.
```

Substituting the computed Haar ceiling gives

```math
\mathcal E_{F_4}^{HK}(T)
\le
0.70360\ldots
+2(0.026725263\ldots)
<
0.76.
```

The direct Weyl-grid values in Computation 24.2 are sharper, around
\(0.696\), but the displayed \(0.76\) envelope is already enough for the
decision below. `square`

### Theorem 24.4: Heat-Kernel Tail Comparison Would Falsify Near-Maximal Escape

The compact-group heat-kernel reference cannot supply
`P22-F4-NEARMAX-TAIL` on the active \(F_4\) row.  More precisely,

```math
\sup_{T\in[T_-,T_+]}
\mathcal E_{F_4}^{HK}(T)
<0.76
<
\Theta_4^{min}
=0.980637924\ldots .
```

Consequently any same-record theorem that compares the actual active
plaquette law to \(H_T\) strongly enough for the tail functional
\(\gamma 1_{\{X_4\ge\gamma\}}\) would not prove the escape gate.  It would
instead falsify the heat-kernel-like near-maximal-tail route.

Proof.

The \(0.76\) reference envelope is Lemma 24.3.  The active minimum threshold
is Definition 21.2.  Since \(0.76<0.980637924\ldots\), the heat-kernel
reference law is not merely short of the log-2 row; it is short by more than
two tenths in escape product. `square`

### Corollary 24.5: What The Next Tail Source Must Be

The next source cannot be a routine heat-kernel tail comparison.  The reference
law has the correct first moment,

```math
\int X_4\,dH_{T_-}
=
1-\exp\left(-{15\over16}T_-\right)
=0.990777444\ldots,
```

but its optimal tail product is only

```math
\mathcal E_{F_4}^{HK}(T_-)
=0.69373\ldots .
```

Thus the failure mode is exactly the one isolated in Lemma 22.4: a large first
moment of \(X_4\) does not imply near-maximal fixed-threshold escape.

The only direct continuations are therefore:

1. prove that the actual `SEL2` scalar law is **not heat-kernel-like** in this
   tail and has an additional same-record moment-saturation mechanism; or
2. abandon \(F_4\) near-maximal escape and search for a different channel or
   a genuinely new signed/selector surface theorem.

This keeps the route Barandes-aligned: the obstruction is stated entirely in
terms of finite pushed-forward scalar records and compact-group reference
laws, without importing a continuum Yang-Mills measure or an area-law
assumption.

## 25. The \(F_4\) Saturation-Defect Program

Section 24 changes the continuation strategy.  A heat-kernel-like tail theorem
would not close escape.  It would falsify the \(F_4\) near-maximal branch.  The
only direct \(F_4\) continuation is therefore a same-record theorem saying that
the actual `SEL2` scalar law has a much sharper high-deficit concentration than
the heat-kernel reference.

### Definition 25.1: Six-Step Tail Continuation Plan

The continuation from Section 24 is the following finite-record program.

1. **Saturation-defect theorem.**  Convert the escape gate into a necessary
   small-defect condition for the layer-cake inequality

   ```math
   \gamma\,1_{\{X_4\ge\gamma\}}\le X_4.
   ```

2. **Finite ramp records.**  Add same-record continuous approximants to the
   threshold events \(\{X_4\ge\gamma\}\), so the needed tail data can be
   tested inside a finite scalar battery.

3. **Second-moment and higher-moment falsifiers.**  Source or compute

   ```math
   \int X_4^m\,d\nu_{p,j}^{SEL2}
   ```

   for \(m\ge2\), beginning with \(m=2\).  If these moments are
   heat-kernel-like, the saturation defect cannot be small enough.

4. **Direct tail theorem only after saturation evidence.**  Try to prove

   ```math
   \exists\gamma>\Theta_4^{act}:
   \gamma\liminf_j\nu_{p,j}^{SEL2}\{X_4\ge\gamma\}
   >
   \Theta_4^{act}
   ```

   only if the moment/ramp diagnostics show genuine high-deficit saturation.

5. **Alternate-channel screen.**  Run the same worksheet for other
   \((N,\rho)\): tree-time margin, first-moment room, heat-kernel reference
   tail, and saturation defect.

6. **Signed/selector surface route as a branch change.**  If the \(F_4\) and
   alternate-channel diagnostics fail, declare a non-full-support selector or
   signed-cancellation surface theorem and re-audit the Paper-13/Paper-19/Paper-20
   support ledger from scratch.

This order is forced by the Barandes-aligned same-record rule: first decide
which finite scalar records would certify the tail, then ask whether the
actual pushed-forward law satisfies them.

### Definition 25.2: Saturation Defect

For \(0<\gamma\le2\), define the rowwise \(F_4\) saturation defect

```math
D_{\gamma,j}^{SEL2}
:=
\int X_4(U)\,d\nu_{p,j}^{SEL2}(U)
-
\gamma\,\nu_{p,j}^{SEL2}\{U:X_4(U)\ge\gamma\}.
```

Equivalently,

```math
D_{\gamma,j}^{SEL2}
=
\int_{\{X_4<\gamma\}}X_4\,d\nu_{p,j}^{SEL2}
+
\int_{\{X_4\ge\gamma\}}(X_4-\gamma)\,d\nu_{p,j}^{SEL2}.
```

Thus \(D_{\gamma,j}^{SEL2}\ge0\), and it is small only when almost all of the
first moment of \(X_4\) is carried by a high-deficit band close to the chosen
threshold.  Define also

```math
D_{\gamma}^{cof,SEL2}
:=
\limsup_jD_{\gamma,j}^{SEL2}.
```

Let

```math
M_{4,+}
:=
1-\exp\left(-{15\over16}T_+\right)
=0.992382850\ldots .
```

This is the active upper endpoint for the first moment supplied by Lemma 21.4.

### Theorem 25.3: `P22-F4-SATDEF`, Necessary Form

If the active \(F_4\) escape gate passes, then there exists a fixed
\(0<\gamma\le2\) such that

```math
D_{\gamma}^{cof,SEL2}
<
M_{4,+}-\Theta_4^{act}.
```

In particular, every active-branch pass must satisfy the uniform necessary
bound

```math
D_{\gamma}^{cof,SEL2}
<
M_{4,+}-\Theta_4^{min}
=0.011744926\ldots .
```

If the proof is required to clear the whole log-2 activity interval, then it
must satisfy the sharper necessary bound

```math
D_{\gamma}^{cof,SEL2}
<
M_{4,+}-\Theta_4^{\log2}
=0.002063888\ldots .
```

Proof.

If the escape gate passes, Lemma 21.3 gives a fixed \(\gamma\) such that

```math
\gamma Q_{4,\gamma}^{SEL2}
>
\Theta_4^{act},
\qquad
Q_{4,\gamma}^{SEL2}
=
\liminf_j\nu_{p,j}^{SEL2}\{X_4\ge\gamma\}.
```

Using the upper moment endpoint \(M_{4,+}\),

```math
\begin{aligned}
D_{\gamma}^{cof,SEL2}
&=
\limsup_j
\left(
\int X_4\,d\nu_{p,j}^{SEL2}
-
\gamma\nu_{p,j}^{SEL2}\{X_4\ge\gamma\}
\right)\\
&\le
\limsup_j\int X_4\,d\nu_{p,j}^{SEL2}
-
\gamma\liminf_j\nu_{p,j}^{SEL2}\{X_4\ge\gamma\}\\
&\le
M_{4,+}
-
\gamma Q_{4,\gamma}^{SEL2}
<
M_{4,+}-\Theta_4^{act}.
\end{aligned}
```

The two numerical bounds substitute
\(\Theta_4^{min}=1-1/(19e)\) and
\(\Theta_4^{\log2}=1-1/(38e)\), respectively. `square`

### Corollary 25.4: Heat-Kernel Defect Is Too Large

The heat-kernel reference does not merely have too small a tail product.  It
has a saturation defect two orders of magnitude too large for the active
escape gate.

At \(T_-\),

```math
\int X_4\,dH_{T_-}
-
\mathcal E_{F_4}^{HK}(T_-)
=
0.990777444\ldots-0.69373\ldots
=
0.29704\ldots .
```

At \(T_+\),

```math
\int X_4\,dH_{T_+}
-
\mathcal E_{F_4}^{HK}(T_+)
=
0.992382850\ldots-0.69547\ldots
=
0.29691\ldots .
```

Both are far above the necessary active defect
\(0.011744926\ldots\), and far above the log-2 uniform defect
\(0.002063888\ldots\).

Thus any actual \(F_4\) proof must show that the `SEL2` plaquette law is not
just slightly different from the heat-kernel reference; it must show a
qualitatively different high-deficit saturation profile.

Proof.

The two first moments are the heat-kernel coefficient values already used in
Lemma 21.4.  The two optimal tail products are Computation 24.2.  Subtraction
gives the displayed defects, and Theorem 25.3 gives the necessary active and
log-2 defect bounds. `square`

### Definition 25.5: Finite Ramp Tail Records

For \(0<\gamma<2\) and \(0<\delta<2-\gamma\), let
\(r_{\gamma,\delta}:[0,2]\to[0,1]\) be the continuous ramp

```math
r_{\gamma,\delta}(x)
:=
\begin{cases}
0,&x\le\gamma,\\
(x-\gamma)/\delta,&\gamma<x<\gamma+\delta,\\
1,&x\ge\gamma+\delta.
\end{cases}
```

Define the scalar record

```math
R_{\gamma,\delta}(U)
:=
r_{\gamma,\delta}(X_4(U)).
```

Then

```math
1_{\{X_4\ge\gamma+\delta\}}
\le
R_{\gamma,\delta}
\le
1_{\{X_4>\gamma\}}.
```

The ramp-defect record is

```math
D_{\gamma,\delta,j}^{ramp}
:=
\int X_4\,d\nu_{p,j}^{SEL2}
-
\gamma\int R_{\gamma,\delta}\,d\nu_{p,j}^{SEL2}.
```

Since \(X_4=1-\Phi_{F_4}/4\), every polynomial approximation to
\(r_{\gamma,\delta}(X_4)\) is a finite polynomial in the paired fundamental
character.  By Peter-Weyl tensor closure, such a polynomial lives in a finite
same-record scalar battery generated by tensor powers of \(F_4\) and
\(\overline F_4\).

### Lemma 25.6: The Ramp Program Is A Finite-Battery Program

For every finite grid
\(\Gamma\subset(0,2)\), every finite set of widths
\(\Delta\subset(0,2)\), and every tolerance \(\varepsilon>0\), there is a
finite scalar character battery \(\mathcal B_{F_4}^{ramp}\) such that each
record \(R_{\gamma,\delta}\), \((\gamma,\delta)\in\Gamma\times\Delta\), is
uniformly approximated within \(\varepsilon\) by a record in
\(\mathcal B_{F_4}^{ramp}\).

Proof.

Each \(R_{\gamma,\delta}\) is a continuous function of the single compact
scalar coordinate \(X_4\in[0,2]\).  By the Weierstrass theorem, it is uniformly
approximated by a polynomial in \(X_4\).  Since
\(X_4=1-\Phi_{F_4}/4\), this polynomial is a polynomial in the paired
fundamental character.  Products of finitely many paired fundamental
characters decompose into finitely many Peter-Weyl characters, equivalently
into the finite tensor battery generated by \(F_4\) and \(\overline F_4\) up
to the maximum polynomial degree used for the finite grid.  The union over a
finite grid is finite. `square`

### Corollary 25.7: Next Executable Calculation

The next executable calculation is now precise.  Source or compute the first
new moment/ramp data:

```math
\int X_4^2\,d\nu_{p,j}^{SEL2},
\qquad
\int R_{\gamma,\delta}\,d\nu_{p,j}^{SEL2}
```

on the same pushed-forward `SEL2` scalar law.  If the resulting ramp defects
cannot approach the bounds in Theorem 25.3, the \(F_4\) near-maximal route is
falsified on this branch.  If they can, the direct tail theorem becomes a
well-targeted finite-record statement rather than an unsupported
anti-concentration hope.

## 26. The \(X_4^2\) Character Identity

Section 25 identifies the second moment of \(X_4\) as the cheapest next
finite-battery diagnostic.  This section prints the exact character identity
needed for that calculation.

### Lemma 26.1: Paired-Real Square Of The Fundamental Character

Let \(F\) be the fundamental representation of \(SU(4)\).  In the active
paired-real convention,

```math
\Phi_{F_4}
=
{1\over2}(\chi_F+\chi_{\overline F})
=
\operatorname{Re}\chi_F.
```

Then

```math
\Phi_{F_4}^2
=
{1\over2}
\left(
1+\Phi_{\operatorname{Sym}^2F}
+\Phi_{\Lambda^2F}
+\Phi_{\operatorname{Ad}}
\right).
```

Here \(\Lambda^2F\) and \(\operatorname{Ad}\) are self-conjugate for \(SU(4)\),
while

```math
\Phi_{\operatorname{Sym}^2F}
:=
{1\over2}
\left(
\chi_{\operatorname{Sym}^2F}
+\chi_{\operatorname{Sym}^2\overline F}
\right).
```

Proof.

Use the finite tensor-product identities

```math
F\otimes F
=
\operatorname{Sym}^2F\oplus\Lambda^2F,
```

and

```math
F\otimes\overline F
=
\mathbf 1\oplus\operatorname{Ad}.
```

Therefore

```math
\begin{aligned}
\Phi_{F_4}^2
&=
{1\over4}
(\chi_F+\chi_{\overline F})^2\\
&=
{1\over4}
\left(
\chi_{\operatorname{Sym}^2F}
+\chi_{\Lambda^2F}
+2(1+\chi_{\operatorname{Ad}})
+\chi_{\operatorname{Sym}^2\overline F}
+\chi_{\Lambda^2\overline F}
\right).
\end{aligned}
```

For \(SU(4)\), \(\Lambda^2\overline F\simeq\Lambda^2F\) and
\(\operatorname{Ad}\simeq\overline{\operatorname{Ad}}\).  Grouping conjugate
pairs gives the displayed identity. `square`

### Corollary 26.2: The Exact \(X_4^2\) Battery Decomposition

For

```math
X_4=1-{\Phi_{F_4}\over4},
```

one has the exact finite-character identity

```math
X_4^2
=
{33\over32}
-{1\over2}\Phi_{F_4}
+
{1\over32}
\left(
\Phi_{\operatorname{Sym}^2F}
+\Phi_{\Lambda^2F}
+\Phi_{\operatorname{Ad}}
\right).
```

Consequently the second moment of \(X_4\) is a finite same-record scalar
battery record:

```math
\int X_4^2\,d\nu_{p,j}^{SEL2}
=
{33\over32}
-{1\over2}
\int\Phi_{F_4}\,d\nu_{p,j}^{SEL2}
+
{1\over32}
\sum_{\lambda\in\{\operatorname{Sym}^2F,\Lambda^2F,\operatorname{Ad}\}}
\int\Phi_\lambda\,d\nu_{p,j}^{SEL2}.
```

The next source question is therefore not algebraic.  It is whether the same
`SEL2` scalar law supplies, or can be extended to supply, the three additional
coefficient records

```math
\Phi_{\operatorname{Sym}^2F},
\qquad
\Phi_{\Lambda^2F},
\qquad
\Phi_{\operatorname{Ad}}.
```

Proof.

Expand

```math
X_4^2
=
1-{1\over2}\Phi_{F_4}+{1\over16}\Phi_{F_4}^2
```

and substitute Lemma 26.1.  The final integral identity follows by linearity.
`square`

## 27. Same-Record Sources For The \(X_4^2\) Coefficients

Section 26 reduced the second moment of \(X_4\) to three additional character
records.  This section sources those records on the same active `SEL2` scalar
law.  The point is narrow: it gives coefficient values for the second-moment
diagnostic.  It does not prove the near-maximal \(F_4\) escape tail.

### Definition 27.1: The Degree-Two \(F_4\) Coefficient Battery

Let

```math
\mathcal R_{F_4}^{(2)}
:=
\{\operatorname{Sym}^2F,\Lambda^2F,\operatorname{Ad}\}.
```

The corresponding \(SU(4)\) dimensions and quadratic Casimirs, in the same
normalization as \(C_2(F_4)=15/8\), are

```math
\begin{array}{c|c|c|c}
\lambda & \text{Dynkin label} & d_\lambda & C_2(\lambda)\\
\hline
\operatorname{Sym}^2F & (2,0,0)\text{ paired with }(0,0,2) & 10 & 9/2\\
\Lambda^2F & (0,1,0) & 6 & 5/2\\
\operatorname{Ad} & (1,0,1) & 15 & 4
\end{array}
```

For \(\operatorname{Sym}^2F\) the scalar record is the paired-real character

```math
\Phi_{\operatorname{Sym}^2F}
=
{1\over2}
\left(
\chi_{\operatorname{Sym}^2F}
+\chi_{\operatorname{Sym}^2\overline F}
\right),
```

while \(\Lambda^2F\) and \(\operatorname{Ad}\) are self-conjugate.  These are
finite Peter-Weyl records in the tensor-square battery generated by \(F\) and
\(\overline F\).  Adding them to the diagnostic battery does not change the
pushed-forward law \(\nu_{p,j}^{SEL2}\); it only asks for three additional
bounded scalar expectations under that law.

### Lemma 27.2: Paper-20 Coefficient Comparison Applies To The Degree-Two Battery

On the strict exact-record `SEL2` branch of Paper 20, for every fixed
\(\lambda\in\mathcal R_{F_4}^{(2)}\),

```math
\widetilde a_{\lambda,j}^{SEL2}
:=
{1\over d_\lambda}
\int\Phi_\lambda\,d\nu_{p,j}^{SEL2}
```

satisfies

```math
\widetilde a_{\lambda,j}^{SEL2}
=
\exp\left(
-{C_2(\lambda)\over2}T_j^{SEL2,conv}
\right)
+\varepsilon_{\lambda,j}^{SEL2},
\qquad
\varepsilon_{\lambda,j}^{SEL2}\to0.
```

Equivalently,

```math
\max_{\lambda\in\mathcal R_{F_4}^{(2)}}
\left|
\widetilde a_{\lambda,j}^{SEL2}
-
\exp\left(
-{C_2(\lambda)\over2}T_j^{SEL2,conv}
\right)
\right|
\to0.
```

Proof.

Paper 20 Theorem 4.3A.160AU gives the same-target coefficient comparison for
any fixed normalized central character

```math
\psi_\lambda={\Phi_\lambda\over d_\lambda}
```

included in the finite row battery.  Paper 20 Corollary 4.3A.160BH.40B closes
the strict five-term scalar correction ledger, so
`P20-SEL2-4DCOEFF-CLOSE` holds with an \(o(1)\) error on the same pushed-forward
finite `SEL2` scalar law.  The set \(\mathcal R_{F_4}^{(2)}\) is finite, so the
three rowwise \(o(1)\) errors may be replaced by their maximum.  No
total-variation convergence of the whole law, continuum Yang-Mills measure, or
Wilson-loop area law is used. `square`

### Corollary 27.3: Explicit Same-Record Coefficient Rows

On the same strict active row,

```math
\int\Phi_{\operatorname{Sym}^2F}\,d\nu_{p,j}^{SEL2}
=
10\exp\left(-{9\over4}T_j^{SEL2,conv}\right)+o(1),
```

```math
\int\Phi_{\Lambda^2F}\,d\nu_{p,j}^{SEL2}
=
6\exp\left(-{5\over4}T_j^{SEL2,conv}\right)+o(1),
```

and

```math
\int\Phi_{\operatorname{Ad}}\,d\nu_{p,j}^{SEL2}
=
15\exp\left(-2T_j^{SEL2,conv}\right)+o(1).
```

Together with the already active \(F_4\) row,

```math
\int\Phi_{F_4}\,d\nu_{p,j}^{SEL2}
=
4\exp\left(-{15\over16}T_j^{SEL2,conv}\right)+o(1).
```

Proof.

Insert the dimensions and Casimirs from Definition 27.1 into Lemma 27.2 and
multiply by \(d_\lambda\). `square`

### Corollary 27.4: Same-Record \(X_4^2\) Moment Formula

Define the heat-polynomial comparison function

```math
\mathfrak m_{2,F_4}(T)
:=
{33\over32}
-2e^{-15T/16}
+{3\over16}e^{-5T/4}
+{15\over32}e^{-2T}
+{5\over16}e^{-9T/4}.
```

Then

```math
\int X_4^2\,d\nu_{p,j}^{SEL2}
=
\mathfrak m_{2,F_4}(T_j^{SEL2,conv})
+o(1).
```

Thus the second moment is now sourced as a same-record finite coefficient
calculation.  The remaining \(F_4\) saturation problem is not the availability
of the \(X_4^2\) record; it is whether this moment, together with finite ramp
records or additional higher moments, can force the very small saturation
defect required by Theorem 25.3.

Proof.

Substitute Corollary 27.3 into Corollary 26.2:

```math
\begin{aligned}
\int X_4^2\,d\nu_{p,j}^{SEL2}
&=
{33\over32}
-{1\over2}\left(4e^{-15T_j^{SEL2,conv}/16}\right)\\
&\quad
+{1\over32}
\left(
10e^{-9T_j^{SEL2,conv}/4}
+6e^{-5T_j^{SEL2,conv}/4}
+15e^{-2T_j^{SEL2,conv}}
\right)
+o(1).
\end{aligned}
```

Collecting coefficients gives the displayed formula. `square`

## 28. Degree-Two Saturation Test

The second moment is now sourced, so the next honest question is whether the
first two moments can force or falsify the near-maximal \(F_4\) tail required
by Theorem 25.3.  They cannot.  This section closes that diagnostic.

### Definition 28.1: Moment Pair On The Active \(F_4\) Window

For \(T\in[T_-^{SEL2},T_+^{SEL2}]\), set

```math
\mu_1(T)
:=
1-e^{-15T/16},
```

and

```math
\mu_2(T)
:=
\mathfrak m_{2,F_4}(T).
```

By Corollary 27.4,

```math
\int X_4\,d\nu_{p,j}^{SEL2}
=
\mu_1(T_j^{SEL2,conv})+o(1),
\qquad
\int X_4^2\,d\nu_{p,j}^{SEL2}
=
\mu_2(T_j^{SEL2,conv})+o(1).
```

On the active \(F_4\) row,

```math
T_-^{SEL2}=4.99851,\qquad T_+^{SEL2}=5.20251,
```

so

```math
\begin{array}{c|c|c|c}
T & \mu_1(T) & \mu_2(T) & \mu_2(T)-\mu_1(T)^2\\
\hline
4.99851 & 0.990777444633 & 1.013192947355 & 0.031553002562\\
5.10000 & 0.991614489475 & 1.014819077041 & 0.031519781305\\
5.20251 & 0.992382850990 & 1.016313484787 & 0.031489761847
\end{array}
```

The lower endpoint already satisfies

```math
\mu_1(T_-^{SEL2})
-
\Theta_4^{\log2}
=
0.000458482558\ldots>0.
```

### Lemma 28.2: The Moment Pair Admits A Zero-Defect Saturating Scalar Law

For each \(T\in[T_-^{SEL2},T_+^{SEL2}]\), define

```math
\gamma_2(T):={\mu_2(T)\over\mu_1(T)},
\qquad
p_2(T):={\mu_1(T)^2\over\mu_2(T)}.
```

Then \(0<\gamma_2(T)<2\), \(0<p_2(T)<1\), and the two-point scalar law

```math
\nu_T^{sat}
:=
(1-p_2(T))\delta_0+p_2(T)\delta_{\gamma_2(T)}
```

on the interval \(0\le X\le2\) has

```math
\int X\,d\nu_T^{sat}=\mu_1(T),
\qquad
\int X^2\,d\nu_T^{sat}=\mu_2(T),
```

but

```math
\gamma_2(T)\nu_T^{sat}\{X\ge\gamma_2(T)\}
=
\mu_1(T).
```

Equivalently, its saturation defect at \(\gamma_2(T)\) is exactly zero.

Proof.

The identities are algebraic:

```math
p_2(T)\gamma_2(T)=\mu_1(T),
\qquad
p_2(T)\gamma_2(T)^2=\mu_2(T).
```

The numerical active window gives

```math
\begin{array}{c|c|c}
T & \gamma_2(T) & p_2(T)\\
\hline
4.99851 & 1.022624155247 & 0.968857854129\\
5.10000 & 1.023400815350 & 0.968940491938\\
5.20251 & 1.024114316136 & 0.969015700058
\end{array}
```

so the atoms lie inside the physical scalar range \(0\le X_4\le2\).  Since
\(X_4\) attains every value in \([0,2]\) on \(SU(4)\), for instance along
\(\operatorname{diag}(e^{i\theta},e^{-i\theta},e^{i\theta},e^{-i\theta})\),
this scalar two-point law can also be lifted to a central conjugacy-class
mixture if only the \(X_4\) scalar record is being tested.  Since
\(\nu_T^{sat}\) has no mass in \(0<X<\gamma_2(T)\) and no mass above
\(\gamma_2(T)\), the defect

```math
D_{\gamma_2(T)}(\nu_T^{sat})
=
\int_{X<\gamma_2(T)}X\,d\nu_T^{sat}
+
\int_{X\ge\gamma_2(T)}(X-\gamma_2(T))\,d\nu_T^{sat}
```

is zero. `square`

### Theorem 28.3: `P22-F4-MOM2-SATTEST`, No-Decision Verdict

The same-record first and second moments of \(X_4\) do not decide
`P22-F4-NEARMAX-TAIL`.

More precisely:

1. the moment pair is compatible with a passing near-maximal tail, since
   Lemma 28.2 gives a scalar law with

   ```math
   \gamma_2(T)\nu_T^{sat}\{X\ge\gamma_2(T)\}
   =
   \mu_1(T)
   >
   \Theta_4^{\log2}
   \ge
   \Theta_4^{act};
   ```

2. the same moment pair is compatible with a failing heat-kernel-like tail,
   since Section 24 gives

   ```math
   \mathcal E_{F_4}^{HK}(T)<0.76
   <
   \Theta_4^{min}
   \le
   \Theta_4^{act}
   ```

   throughout the active \(F_4\) time window, while the heat-kernel law has the
   same \(\mu_1(T)\) and \(\mu_2(T)\) by the Peter-Weyl coefficient calculation
   of Sections 24 and 27.

Therefore no theorem using only the same-record degree-two moment data

```math
\left(
\int X_4\,d\nu_{p,j}^{SEL2},
\int X_4^2\,d\nu_{p,j}^{SEL2}
\right)
```

can prove or falsify the active \(F_4\) escape gate.

Proof.

Item 1 follows from Lemma 28.2 and the displayed lower-endpoint inequality
\(\mu_1(T_-^{SEL2})>\Theta_4^{\log2}\).  Item 2 follows from Theorem 24.4 and
Corollary 27.4.  The two laws have identical first two scalar moments but
opposite verdicts for the escape ceiling.  Hence the first two moments are not
logically decisive. `square`

### Corollary 28.4: The Next Source Must Be Ramp Or Higher-Moment Data

After `P22-F4-MOM2-SATTEST`, the remaining \(F_4\) route is forced into one of
three branches.

1. **Finite ramp branch.**  Source the same-record records

   ```math
   \int R_{\gamma,\delta}\,d\nu_{p,j}^{SEL2}
   ```

   from Definition 25.5 for a finite grid near
   \(\gamma\approx1.02\).  These records test the actual layer-cake shape, not
   just its first two moments.

2. **Higher-moment branch.**  Source \(X_4^m\) for \(m\ge3\).  Any successful
   theorem must rule out the saturating two-atom law of Lemma 28.2 while also
   distinguishing the actual law from the heat-kernel failing profile of
   Section 24.

3. **Branch-change route.**  Switch channel or introduce a signed/selector
   surface route, with a full same-record re-audit.  The degree-two moment
   diagnostic does not justify spending the \(F_4\) escape gate.

## 29. Finite-Ramp Heat-Kernel Comparison And \(F_4\) Escape Falsification

The degree-two moment test is non-decisive because moment data are too coarse.
The finite-ramp records are decisive in the opposite direction: on the strict
same-record branch, every fixed continuous scalar function of \(X_4\) has the
same cofinal value as the active heat-kernel convolution reference.  Therefore
the actual \(F_4\) scalar law is heat-kernel-like at the level of fixed
threshold tails, and the near-maximal \(F_4\) escape route fails.

### Definition 29.1: The Scalar \(X_4\) Pushforward Laws

Let

```math
\xi_j^{SEL2}
:=
(X_4)_*\nu_{p,j}^{SEL2}
```

be the actual active scalar law on \([0,2]\), and let

```math
\xi_T^{HK}
:=
(X_4)_*(H_T(U)\,dU)
```

be the scalar heat-kernel reference law.  The active comparison time is
\(T_j^{SEL2,conv}\in[T_-^{SEL2},T_+^{SEL2}]\) cofinally.

### Lemma 29.2: Fixed Continuous \(X_4\)-Records Compare To Heat Kernel

For every fixed continuous function \(f:[0,2]\to\mathbb R\),

```math
\int f\,d\xi_j^{SEL2}
-
\int f\,d\xi_{T_j^{SEL2,conv}}^{HK}
\longrightarrow0.
```

Equivalently,

```math
\int f(X_4(U))\,d\nu_{p,j}^{SEL2}(U)
-
\int f(X_4(U))H_{T_j^{SEL2,conv}}(U)\,dU
\longrightarrow0.
```

Proof.

Fix \(\varepsilon>0\).  By Weierstrass, choose a polynomial \(P_\varepsilon\)
on \([0,2]\) with

```math
\|f-P_\varepsilon\|_\infty\le\varepsilon.
```

Since \(X_4=1-\Phi_{F_4}/4\), \(P_\varepsilon(X_4)\) is a fixed finite
polynomial in the paired-real fundamental character.  By Peter-Weyl tensor
closure it decomposes into a finite sum of central character records in a fixed
finite \(F_4,\overline F_4\) battery.  Paper 20 Theorem 4.3A.160AU and
Corollary 4.3A.160BH.40B apply to every character in this finite battery on the
same strict pushed-forward `SEL2` law.  Therefore

```math
\int P_\varepsilon(X_4)\,d\nu_{p,j}^{SEL2}
-
\int P_\varepsilon(X_4)\,dH_{T_j^{SEL2,conv}}
\to0.
```

The two uniform approximation errors contribute at most \(2\varepsilon\).  Let
\(\varepsilon\downarrow0\). `square`

### Corollary 29.3: Finite Ramp Records Are Heat-Kernel Records On The Strict Branch

For every fixed \((\gamma,\delta)\) from Definition 25.5,

```math
\int R_{\gamma,\delta}\,d\nu_{p,j}^{SEL2}
-
\int R_{\gamma,\delta}\,dH_{T_j^{SEL2,conv}}
\to0.
```

Thus the finite-ramp branch is no longer an open independent source on the
strict scalar branch.  It is the heat-kernel scalar branch.

Proof.

\(R_{\gamma,\delta}=r_{\gamma,\delta}(X_4)\) and
\(r_{\gamma,\delta}\) is continuous on \([0,2]\).  Apply Lemma 29.2. `square`

### Lemma 29.4: Fixed Threshold Tails Are Bounded By The Heat-Kernel Tail Ceiling

For every \(0<\gamma\le2\),

```math
Q_{4,\gamma}^{SEL2}
\le
\sup_{T\in[T_-^{SEL2},T_+^{SEL2}]}
\xi_T^{HK}([\gamma,2]).
```

Consequently

```math
\mathcal E_{F_4}^{cof,SEL2}
\le
\sup_{T\in[T_-^{SEL2},T_+^{SEL2}]}
\mathcal E_{F_4}^{HK}(T).
```

Proof.

Let \(j_k\) be any subsequence.  Passing to a further subsequence if necessary,
assume

```math
T_{j_k}^{SEL2,conv}\to T_*\in[T_-^{SEL2},T_+^{SEL2}].
```

Lemma 29.2 implies weak convergence of the scalar laws

```math
\xi_{j_k}^{SEL2}\Rightarrow\xi_{T_*}^{HK}
```

on the compact interval \([0,2]\).  The heat-kernel law has a smooth central
density on \(SU(4)\), and the level sets of the nonconstant scalar
\(X_4\) have Haar measure zero for \(0<\gamma<2\); the endpoints are handled by
one-sided approximation.  Hence

```math
\limsup_k\xi_{j_k}^{SEL2}([\gamma,2])
\le
\xi_{T_*}^{HK}([\gamma,2]).
```

Taking the supremum over subsequential limits gives the first displayed
inequality.  Multiplying by \(\gamma\) and taking the supremum over
\(\gamma\) gives the second. `square`

### Theorem 29.5: `P22-F4-RAMP-HK-FALSIFY`

On the strict same-record active \(F_4\) branch,

```math
\mathcal E_{F_4}^{cof,SEL2}
<
\Theta_4^{min}.
```

Therefore

```math
\mathrm{P20\text{-}SEL2\text{-}ESC\text{-}MASS}(F_4)
```

fails uniformly for every allowed active activity value.  In particular, the
strict \(F_4\) direct escape route cannot close the Paper-20 tree-rate gate.

Proof.

Lemma 29.4 gives

```math
\mathcal E_{F_4}^{cof,SEL2}
\le
\sup_{T\in[T_-^{SEL2},T_+^{SEL2}]}
\mathcal E_{F_4}^{HK}(T).
```

Lemma 24.3 gives the conservative active-window bound

```math
\sup_{T\in[T_-^{SEL2},T_+^{SEL2}]}
\mathcal E_{F_4}^{HK}(T)
<0.76.
```

Definition 21.2 gives

```math
0.76
<
\Theta_4^{min}
=1-{1\over19e}
\le
\Theta_4^{act}.
```

The exact equivalence between `ESC-MASS` and
\(\mathcal E_{F_4}^{cof,SEL2}>\Theta_4^{act}\) is Lemma 21.3.  Hence
`ESC-MASS` fails on this strict branch. `square`

### Corollary 29.6: What Remains After The \(F_4\) Falsification

The strict \(F_4\) route now has a clean verdict.

1. `TREE-TIME(F_4)` is closed on the active worksheet.
2. `ESC-MASS(F_4)` fails by Theorem 29.5.
3. Therefore the strict \(F_4\) direct-witness branch cannot prove continuum
   Yang-Mills confinement.

The remaining honest continuations are:

1. run the same scalar worksheet for another \((N,\rho)\), including its
   tree-time threshold, heat-kernel tail ceiling, and saturation/ramp verdict;
2. prove a genuinely stronger same-record surface theorem lowering
   \(\Theta_{esc}^{tree}\) below the actual heat-kernel tail ceiling;
3. declare a non-full-support selector or signed-cancellation surface route and
   re-audit the Paper-13/Paper-19/Paper-20 support ledger from scratch.

No conclusion about full continuum Yang-Mills confinement follows from this
falsification alone.  It falsifies the strict \(F_4\) `SEL2` escape-mass route,
not every possible confinement strategy.

## 30. Post-\(F_4\) Branch Ledger

The \(F_4\) verdict forces a branch choice.  The continuation must not keep
spending the same strict \(F_4\) scalar law after Theorem 29.5 has falsified
its escape half.  Under the target convention of Section 0.1, the paper is
allowed to change to a declared alternate \(SU(N)\) fundamental channel before
the final source gate is evaluated.  The remaining branches are the following.

1. **Branch A: alternate channel.**  Keep the strict same-record `SEL2`
   construction, but change the finite representation channel before the
   tree-rate gate is evaluated.  The admissible test is:

   ```math
   \mathrm{TREE\text{-}TIME}(F_N)
   \quad\text{and}\quad
   \mathrm{ESC\text{-}MASS}(F_N)
   ```

   on one fixed \(SU(N)\) fundamental channel, with all scalar records read
   from the corresponding pushed-forward law.  This is a gauge/channel switch,
   not a rescue of the \(SU(4)\) route.  It is admissible for the general
   `4D SU(N)` target convention and inadmissible only if a later theorem
   declares fixed low-rank \(SU(4)\) as the target.

2. **Branch B: stronger surface theorem.**  Keep the strict scalar law but
   replace the rooted tree entropy in
   \(G_{13,tree}^{SEL2}\) by a genuinely sharper same-boundary surface theorem.
   This branch must lower \(\Theta_{esc}^{tree}=1-\exp(-G_{13,tree}^{SEL2})\)
   below the actual available escape product.

3. **Branch C: signed or selector surface route.**  Declare a non-full-support
   selector or signed-cancellation theorem before evaluation, then re-audit the
   Paper-13/Paper-19/Paper-20 support and positivity ledgers from scratch.  This
   is a branch change, not a finite-table refinement.

The Barandes-aligned rule is unchanged: every branch must be stated as a
finite pushed-forward record law before any inequality is evaluated.  No
continuum Yang-Mills measure, area law, or unrecorded process may be inserted
as a source.

## 31. Branch A: Alternate Fundamental Channel Screen

This section settles Branch A in the strict same-record sense.  The low-rank
candidate list from Definition 17.1 has a negative verdict: \(SU(2)\) and
\(SU(3)\) fail the time half on the active row, while \(SU(4)\) passes time but
fails escape by Theorem 29.5.  However, the large-\(N\) fundamental channel
has a positive verdict: for every \(N\ge4096\), the same active `SEL2` row
passes both `TREE-TIME` and `ESC-MASS`.

This is the important distinction.  Branch A is not an \(F_4\) rescue.  It is
a legitimate alternate \(SU(N)\) fundamental route for sufficiently large
\(N\).

### Definition 31.1: The Active Fundamental Row For \(SU(N)\)

For \(N\ge2\), let \(F_N\) be the fundamental representation of \(SU(N)\), and
write

```math
d_N=N,\qquad
C_2(F_N)={N^2-1\over 2N}.
```

Use the same active selector row as Section 18:

```math
s={51\over10},
\qquad
\epsilon_A=\chi={1\over100},
\qquad
\widehat\eta\le\eta_{\log2}
={\log2\over20+\log2}.
```

Thus

```math
T_-^{SEL2}
=s(1-\epsilon_A)(1-\chi)
=4.99851,
\qquad
T_+^{SEL2}
=s(1+\epsilon_A)(1+\chi)
=5.20251,
```

and

```math
G_{\log2}
:=
1+\log19+\log2.
```

The uniform active escape threshold is

```math
\Theta_{\log2}
:=
1-\exp(-G_{\log2})
=1-{1\over38e}.
```

Since
\(\Theta_{esc}^{act}=1-\exp(-G_{13,tree}^{SEL2})<\Theta_{\log2}\)
by Theorem 20.4, any escape product strictly above \(\Theta_{\log2}\) is a
uniform pass certificate for the active branch.

### Lemma 31.2: The Active Time Verdict For Fundamental Channels

On the active row of Definition 31.1:

1. \(SU(2),F_2\) and \(SU(3),F_3\) fail `TREE-TIME`;
2. every \(SU(N),F_N\) with \(N\ge4\) passes `TREE-TIME`.

Proof.

For failure it is enough to use the smallest possible tree exponent

```math
G_{min}:=1+\log19.
```

The largest clean time on the active row is \(T_+^{SEL2}=5.20251\).  For
\(SU(2)\),

```math
{2G_{min}\over C_2(F_2)}
=10.5185\ldots
>T_+^{SEL2},
```

and for \(SU(3)\),

```math
{2G_{min}\over C_2(F_3)}
=5.9167\ldots
>T_+^{SEL2}.
```

Thus even the most favorable active threshold is above the entire selector-time
window for \(N=2,3\).

For \(N=4\), Corollary 20.5 proves the pass:

```math
{51\over10}
>
{2G_{\log2}\over (15/8)(99/100)^2}.
```

The factor \(4N/(N^2-1)=2/C_2(F_N)\) is strictly decreasing for \(N\ge2\).
Therefore the \(N=4\) pass inequality implies the same strict pass inequality
for every \(N\ge4\). `square`

### Definition 31.3: Fundamental Escape Variable

For the fundamental channel of \(SU(N)\), define the paired real normalized
character and escape variable

```math
\psi_N(U)
:=
{\operatorname{Re}\operatorname{tr}(U)\over N},
\qquad
X_N(U):=1-\psi_N(U).
```

Then \(0\le X_N\le2\).  Define the same-record cofinal escape product by

```math
\mathcal E_{F_N}^{cof,SEL2}
:=
\sup_{0<\gamma\le2}
\gamma
\liminf_j
\nu_{p,j}^{SEL2}\{U:X_N(U)\ge\gamma\}.
```

The branch passes `ESC-MASS(F_N)` if

```math
\mathcal E_{F_N}^{cof,SEL2}
>
\Theta_{esc}^{act}.
```

It is enough to prove the stronger uniform inequality

```math
\mathcal E_{F_N}^{cof,SEL2}
>
\Theta_{\log2}.
```

### Lemma 31.4: Fixed \(X_N\)-Records Compare To Heat Kernel

For every fixed \(N\ge2\) and every fixed continuous \(f:[0,2]\to\mathbb R\),

```math
\int f(X_N)\,d\nu_{p,j}^{SEL2}
-
\int f(X_N)\,dH_{T_j^{SEL2,conv}}
\longrightarrow0.
```

Consequently, at every continuity threshold \(\gamma\),

```math
\liminf_j
\nu_{p,j}^{SEL2}\{X_N\ge\gamma\}
\ge
\inf_{T\in[T_-^{SEL2},T_+^{SEL2}]}
H_T\{X_N\ge\gamma\}.
```

Proof.

The proof is the same finite-battery argument as Lemma 29.2, with \(F_4\)
replaced by the fixed fundamental representation \(F_N\).  A polynomial in
\(X_N\) is a finite polynomial in the paired fundamental character of
\(SU(N)\), hence lies in a fixed finite \(F_N,\overline F_N\) Peter-Weyl
battery.  Paper 20 Theorem 4.3A.160AU and Corollary 4.3A.160BH.40B apply to
each character in that finite battery on the strict pushed-forward `SEL2` law.
Uniform polynomial approximation gives the continuous-record comparison.

For the tail statement, pass to an arbitrary subsequence of rows and then to a
further subsequence with \(T_j^{SEL2,conv}\to T_*\).  The continuous-record
comparison gives weak convergence to the \(SU(N)\) heat-kernel scalar law at
\(T_*\).  The level set \(\{X_N=\gamma\}\) has Haar measure zero for the
\(\gamma\) used below, and the heat kernel has a smooth central density.
Portmanteau therefore gives the displayed lower bound. `square`

### Lemma 31.5: Large-\(N\) Heat-Kernel Escape Lower Bound

Let

```math
\delta_*:={1\over76e},
\qquad
\gamma_*:=1-\delta_*.
```

For every \(N\ge4096\) and every
\(T\in[T_-^{SEL2},T_+^{SEL2}]\),

```math
\gamma_*\,H_T\{X_N\ge\gamma_*\}
>
\Theta_{\log2}.
```

Proof.

The event \(X_N<\gamma_*\) is the event

```math
{\operatorname{Re}\operatorname{tr}(U)\over N}
>
\delta_*.
```

By Chebyshev,

```math
H_T\{X_N<\gamma_*\}
\le
{1\over N^2\delta_*^2}
\int_{SU(N)}
(\operatorname{Re}\operatorname{tr}U)^2\,dH_T(U),
```

provided the last integral is at most \(1\).

We verify this integral bound uniformly.  The character identity

```math
(\operatorname{Re}\chi_F)^2
={1\over2}\operatorname{Re}(\chi_{\operatorname{Sym}^2F}
+\chi_{\Lambda^2F})
 +{1\over2}(1+\chi_{\operatorname{Ad}})
```

and the heat-kernel character formula give

```math
\int(\operatorname{Re}\operatorname{tr}U)^2\,dH_T(U)
=
{1\over2}
+\frac{d_{\operatorname{Sym}^2F}}2
e^{-C_2(\operatorname{Sym}^2F)T/2}
+\frac{d_{\Lambda^2F}}2
e^{-C_2(\Lambda^2F)T/2}
+\frac{d_{\operatorname{Ad}}}2
e^{-C_2(\operatorname{Ad})T/2}.
```

For \(SU(N)\),

```math
d_{\operatorname{Sym}^2F}={N(N+1)\over2},
\quad
d_{\Lambda^2F}={N(N-1)\over2},
\quad
d_{\operatorname{Ad}}=N^2-1,
```

and

```math
C_2(\operatorname{Sym}^2F)={(N-1)(N+2)\over N},
\quad
C_2(\Lambda^2F)={(N-2)(N+1)\over N},
\quad
C_2(\operatorname{Ad})=N.
```

For \(N\ge4096\) and \(T\ge T_-^{SEL2}>4\), the nontrivial exponential terms
are bounded by \(N^2e^{-N}\) and \(N^2e^{-2N}\).  In particular,

```math
N^2e^{-N}+N^2e^{-2N}< {1\over2}
\qquad (N\ge4096),
```

so

```math
\int(\operatorname{Re}\operatorname{tr}U)^2\,dH_T(U)<1.
```

Thus

```math
H_T\{X_N\ge\gamma_*\}
\ge
1-{1\over N^2\delta_*^2}.
```

For \(N=4096\),

```math
\gamma_*
\left(1-{1\over N^2\delta_*^2}\right)
>
0.9926
>
0.9904
>
\Theta_{\log2}.
```

The left side is increasing in \(N\), so the same bound holds for every
\(N\ge4096\). `square`

### Theorem 31.6: `P22-BRANCHA-LARGEN-PASS`

For every \(N\ge4096\), the strict same-record active fundamental
\(SU(N)\) branch passes the complete Paper-20 tree-rate source gate:

```math
\mathrm{P20\text{-}SEL2\text{-}TREE\text{-}TIME}(F_N)
```

and

```math
\mathrm{P20\text{-}SEL2\text{-}ESC\text{-}MASS}(F_N)
```

both hold.

Proof.

Since \(N\ge4096\ge4\), Lemma 31.2 gives `TREE-TIME(F_N)`.

For escape, Lemma 31.4 and Lemma 31.5 give

```math
\mathcal E_{F_N}^{cof,SEL2}
\ge
\gamma_*
\inf_{T\in[T_-^{SEL2},T_+^{SEL2}]}
H_T\{X_N\ge\gamma_*\}
>
\Theta_{\log2}
>
\Theta_{esc}^{act}.
```

By Definition 31.3, this is exactly `ESC-MASS(F_N)`. `square`

### Corollary 31.7: Branch A Is Settled

Branch A has the following closed verdict.

1. The original finite candidate list from Definition 17.1 is settled:
   \(SU(2)\) and \(SU(3)\) fail the time half, while \(SU(4)\) passes time but
   fails escape.
2. The alternate large-\(N\) fundamental route passes the full tree-rate source
   gate for every \(N\ge4096\).
3. Therefore the strict same-record obstruction after Section 29 is not a
   universal obstruction to all \(SU(N)\) fundamental channels.  It is an
   obstruction to the low-rank \(F_4\) direct-witness branch.

What remains after Branch A is no longer `TREE-TIME` or `ESC-MASS` on the
large-\(N\) branch.  The next downstream task is the Paper-13/Paper-19/Paper-20
surface prefactor comparison for one declared \(N\ge4096\) branch.  If the
target problem is instead fixed to \(SU(4)\), then Branch A is disallowed by
definition and the only remaining routes are Branch B or Branch C from
Section 30.

The intermediate finite interval \(5\le N<4096\) is not an open source gate
for Branch A.  Branch A asks whether a fixed alternate fundamental channel can
pass the same-record tree-rate source gate.  The explicit declaration
\(N=4096\) already supplies such a channel.  Determining the smallest possible
passing \(N\) would be a numerical optimization of the certificate, not a
mathematical obstruction to the branch.

## 32. Large-\(N\) Surface Prefactor Cap

Branch A closes the rate side.  Paper 20 Corollary 4.3A.160BH.40U says that,
after `P20-SEL2-TREE-RATE-GATE` is proved, the remaining `T13` task is exactly
the surface prefactor cap

```math
M_{13}^{surf,SEL2}
<
\underline M_{pre13}^{SEL2,20}
\left(
\exp(\Delta_{13,tree}^{SEL2})-1
\right),
```

where

```math
\Delta_{13,tree}^{SEL2}
:=
\min\left\{
{T_-^{SEL2}C_2(\rho)\over2},
-\log(1-q_\rho\gamma_\rho)
\right\}
-
G_{13,tree}^{SEL2}.
```

This section evaluates that cap for the declared Branch-A row.  It also records
the adaptive large-\(N\) form needed if the Paper-13 surface prefactor is later
printed as a function of \(N\).

### Definition 32.1: Declared \(N=4096\) Prefactor Row

Declare the Branch-A fundamental channel

```math
N_0:=4096,\qquad \rho=F_{4096}.
```

Use the same active selector data:

```math
T_-^{SEL2}=4.99851,
\qquad
C_2(F_{4096})={4096^2-1\over2\cdot4096}
=2047.999877\ldots .
```

Use the escape threshold from Lemma 31.5:

```math
\delta_*={1\over76e},
\qquad
\gamma_*:=1-\delta_*,
\qquad
q_{4096,*}:=
1-{1\over4096^2\delta_*^2}.
```

Then the certified escape product is

```math
p_{4096,*}:=\gamma_*q_{4096,*}
=0.992627916\ldots .
```

The uniform active tree-growth ceiling is

```math
G_{\log2}:=1+\log19+\log2=4.637586159\ldots .
```

Since \(G_{13,tree}^{SEL2}<G_{\log2}\), a lower bound using \(G_{\log2}\) is a
uniform active certificate.

### Lemma 32.2: Explicit \(N=4096\) Surface Surplus

On the declared \(N=4096\) Branch-A row,

```math
\Delta_{13,tree}^{SEL2}
>
0.2724.
```

Consequently the branch passes the surface prefactor cap whenever

```math
{M_{13}^{surf,SEL2}\over\underline M_{pre13}^{SEL2,20}}
<
e^{0.2724}-1.
```

In particular, the simpler sufficient condition

```math
{M_{13}^{surf,SEL2}\over\underline M_{pre13}^{SEL2,20}}
<0.31
```

closes the `T13` prefactor cap for the declared \(N=4096\) branch.

Proof.

The time side is not the bottleneck:

```math
{T_-^{SEL2}C_2(F_{4096})\over2}
=5118.4739\ldots .
```

The escape side gives

```math
-\log(1-p_{4096,*})
=4.910054964\ldots .
```

Therefore

```math
\Delta_{13,tree}^{SEL2}
\ge
4.910054964\ldots
-G_{\log2}
=0.272468805\ldots
>0.2724.
```

The prefactor cap is exactly Paper 20 Corollary 4.3A.160BH.40U.  Dividing by
\(\underline M_{pre13}^{SEL2,20}>0\) gives the displayed ratio condition.
Since \(e^{0.2724}-1=0.3131\ldots\), the \(0.31\) condition is a strict
rounded sufficient condition. `square`

### Corollary 32.3: What \(N=4096\) Does And Does Not Close

The declared \(N=4096\) row closes:

```math
\mathrm{TREE\text{-}TIME}(F_{4096})
\quad\text{and}\quad
\mathrm{ESC\text{-}MASS}(F_{4096}).
```

It closes the final `T13` surface prefactor comparison if the same-record
Paper-13/Paper-20 prefactor ratio satisfies

```math
{M_{13}^{surf,SEL2}\over\underline M_{pre13}^{SEL2,20}}<0.31.
```

The current corpus does not print that numerical ratio.  Thus the honest
status for the fixed declaration \(N=4096\) is:

```text
rate gate closed; prefactor cap reduced to one explicit finite ratio.
```

This is not Branch B.  Branch B is needed only if the printed prefactor ratio
exceeds the cap for every admissible large-\(N\) declaration, or if the target
is fixed to low-rank \(SU(4)\).

### Lemma 32.4: Adaptive Large-\(N\) Prefactor Absorption

Let \(B<\infty\) be a declared finite prefactor ratio target.  Suppose a
large-\(N\) branch is allowed to choose \(N\) after \(B\) is known, and suppose
the ratio to be absorbed is bounded by \(B\) on that branch:

```math
{M_{13}^{surf,SEL2}(N)\over\underline M_{pre13}^{SEL2,20}(N)}
\le B.
```

Then there exists a finite \(N_B\) such that every declared fundamental branch
with \(N\ge N_B\) passes the surface prefactor cap.

Proof.

Choose \(0<a<1\), and set

```math
\delta_N:=N^{-a},
\qquad
\gamma_N:=1-\delta_N.
```

The same second-moment/Chebyshev argument as Lemma 31.5 gives, for all
sufficiently large \(N\),

```math
H_T\{X_N\ge\gamma_N\}
\ge
1-N^{2a-2},
\qquad
T\in[T_-^{SEL2},T_+^{SEL2}].
```

Thus the certified escape product is at least

```math
p_N:=(1-N^{-a})(1-N^{2a-2}).
```

Since \(a<1\), \(p_N\to1\), and therefore

```math
-\log(1-p_N)\to\infty.
```

The time rate \(T_-^{SEL2}C_2(F_N)/2\) also tends to infinity linearly in
\(N\).  Hence

```math
\Delta_{13,tree}^{SEL2}(N)\to\infty.
```

Choose \(N_B\) so large that

```math
\exp(\Delta_{13,tree}^{SEL2}(N))-1>B
```

for all \(N\ge N_B\).  Paper 20 Corollary 4.3A.160BH.40U then gives the
prefactor cap. `square`

### Corollary 32.5: The Remaining Large-\(N\) Prefactor Question

Branch A can be continued in two honest ways.

1. **Fixed declaration.**  Declare \(N=4096\).  Then the remaining finite
   question is the explicit ratio test

   ```math
   {M_{13}^{surf,SEL2}\over\underline M_{pre13}^{SEL2,20}}<0.31.
   ```

2. **Adaptive declaration.**  Print a same-record growth bound for the ratio

   ```math
   B_N:=
   {M_{13}^{surf,SEL2}(N)\over\underline M_{pre13}^{SEL2,20}(N)}.
   ```

   If \(B_N\) is bounded along a cofinal set of \(N\), Lemma 32.4 closes the
   cap by choosing \(N\) large enough.  More generally, if \(B_N\) grows more
   slowly than the available large-\(N\) escape surplus, the same argument
   closes the cap with the corresponding choice of \(\delta_N\).

The next mainline task is therefore not Branch B yet.  It is the finite
same-record prefactor-ratio audit:

```math
\mathrm{P22\text{-}PREFRATIO\text{-}LARGEN}.
```

Branch B becomes the correct next branch only if this prefactor-ratio audit
fails or if the target is changed to fixed low-rank \(SU(4)\).

## 33. Large-\(N\) Prefactor-Ratio Audit

The previous section deliberately separated two facts that are easy to
conflate.

1. Paper 13 and Paper 19 give a finite same-record surface prefactor on each
   declared branch once the surface-polymer entry package is available.
2. Paper 20's final surface test does not use \(M_{13}^{surf,SEL2}\) alone. It
   uses the ratio

   ```math
   B_N^{pre}
   :=
   {M_{13}^{surf,SEL2}(N)\over
   \underline M_{pre13}^{SEL2,20}(N)}.
   ```

Finite numerator is therefore not enough.  The denominator is a residual
pre-surface margin, and the active large-\(N\) declaration must control the
ratio on the exact same pushed-forward scalar law.

### Definition 33.1: The `P22-PREFRATIO-LARGEN` Test

For a cofinal set of declared fundamental channels \(F_N\), define the
large-\(N\) prefactor-ratio test `P22-PREFRATIO-LARGEN` to be the following
same-record assertion:

there is a printed scalar envelope \(B(N)\) such that, cofinally,

```math
B_N^{pre}
\le B(N),
```

and for the same escape selector \(\delta_N\) used in the Branch-A rate gate,

```math
\log(1+B(N))
<
\Delta_{13,tree}^{SEL2}(N).
```

Equivalently, the Paper-20 cap

```math
M_{13}^{surf,SEL2}(N)
<
\underline M_{pre13}^{SEL2,20}(N)
\left(\exp(\Delta_{13,tree}^{SEL2}(N))-1\right)
```

holds cofinally.  This is a finite scalar-record statement.  It is not a
continuum-measure assumption and it does not import an area law.

### Lemma 33.2: What The Existing Surface Export Actually Supplies

The Paper-13/Paper-19 surface export supplies, for each fixed declared
branch, the finite envelope

```math
M_{13}^{surf,SEL2}(N)
=
\limsup_j
\max_{C\in B_{CR,j}}
A_{C,j}(N)e^{\xi'_{C,j}(N)}
u_{F_N,s_0,j}^{N_j(C)}
<\infty.
```

It does not by itself print a cofinal \(N\)-growth law for

```math
A_{C,j}(N),\qquad
\xi'_{C,j}(N),\qquad
u_{F_N,s_0,j},\qquad
N_j(C),
```

nor does it print a lower floor for
\(\underline M_{pre13}^{SEL2,20}(N)\).

Proof.

Paper 13 Definition 7.30L and Theorem 7.30M express the nonminimal surface
tail using \(A_Ce^{\xi'_C}u_{\rho,s_0}^{N(C)}\) and the subcritical geometric
factor \(B_Cu_{\rho,s_0}/(1-B_Cu_{\rho,s_0})\). Paper 19 Theorem 8L.11A.23
then exports the limsup surface prefactor \(M_{13}^{surf}\) for the declared
finite battery.  Both statements are branchwise same-record statements.
Neither theorem asserts that the displayed constants are uniformly bounded,
polynomially bounded, or exponentially decaying as \(N\to\infty\). `square`

### Lemma 33.3: The Denominator Cannot Be Treated As Uniform

On the Paper-21 scalar worksheet, the active signal profile is

```math
F_{F_N}(s)
=
\exp(-a_Ns)\left(1-\exp(-b_Ns)\right),
```

where \(a_N,b_N\) are positive multiples of

```math
C_2(F_N)={N^2-1\over2N}.
```

For any fixed \(s>0\) and fixed loss slacks, \(F_{F_N}(s)\) decays
exponentially in \(N\).  Moreover, whenever the pre-surface margin is formed
from the Paper-21 worksheet with nonnegative carried pre-surface debit,

```math
0<
\underline M_{pre13}^{SEL2,20}(N)
\le
\underline M_{loss}^{SEL2,20}(N)
<
F_{F_N}(s).
```

Thus the current papers do not permit the inference

```text
M_13^surf finite  =>  B_N^pre bounded.
```

Proof.

The formula for \(F_\rho(s)\) is Paper 21 Definition 5.1.  Since
\(C_2(F_N)=(N^2-1)/(2N)\), both \(a_N\) and \(b_N\) grow linearly in \(N\).
For fixed \(s\), \(1-\exp(-b_Ns)\le1\), so
\(F_{F_N}(s)\le\exp(-a_Ns)\).

Paper 21 Definition 5.5 gives

```math
\underline M_{loss}^{SEL2,20}
=
1+F_{F_N}(s)
-
\exp\left(
{20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}
\right).
```

The exponential term is strictly larger than \(1\) whenever
\(\widehat\eta_{*,20}>0\), hence
\(\underline M_{loss}^{SEL2,20}<F_{F_N}(s)\).  Paper 20 forms the
pre-surface margin by subtracting the nonnegative carried pre-surface debit,
so a positive pre-surface margin is at most
\(\underline M_{loss}^{SEL2,20}\). `square`

### Lemma 33.4: Exact Growth Requirement Under The Chebyshev Large-\(N\) Row

Let the Branch-A large-\(N\) escape selector be

```math
\delta_N:=N^{-a},
\qquad
0<a<1,
```

so that the same heat-kernel second-moment/Chebyshev estimate gives

```math
p_N
:=
q_N\gamma_N
\ge
(1-N^{2a-2})(1-N^{-a})
```

cofinally.  Then

```math
-\log(1-p_N)
\ge
\min\{a,2-2a\}\log N-\log 2+o(1).
```

Consequently `P22-PREFRATIO-LARGEN` follows from the printed growth condition

```math
\log(1+B_N^{pre})
<
\min\{a,2-2a\}\log N
-\log2
-G_{\log2}
+o(1)
```

cofinally.  The optimal Chebyshev exponent is \(2/3\), attained at
\(a=2/3\).

Proof.

For the displayed selector,

```math
1-p_N
\le
N^{-a}+N^{2a-2}.
```

The larger of the two powers is
\(N^{-\min\{a,2-2a\}}\), so

```math
1-p_N
\le
2N^{-\min\{a,2-2a\}}.
```

Taking \(-\log\) gives the rate lower bound.  The time side
\(T_-^{SEL2}C_2(F_N)/2\) grows linearly in \(N\), so for large \(N\) the
escape side is the bottleneck in
\(\Delta_{13,tree}^{SEL2}(N)\).  Subtracting the frozen tree-growth ceiling
\(G_{\log2}\) gives the displayed sufficient condition.  The function
\(\min\{a,2-2a\}\) is maximized at \(a=2/3\), where it equals \(2/3\).
`square`

### Theorem 33.5: Current Verdict On `P22-PREFRATIO-LARGEN`

With the information currently printed in Papers 13, 19, 20, 21, and 22,
`P22-PREFRATIO-LARGEN` is not closed.

What is closed is the exact reduction:

```math
\mathrm{P22\text{-}PREFRATIO\text{-}LARGEN}
```

is proved as soon as one of the following same-record prefactor facts is
printed.

1. **Fixed-row test.**  For the declared \(N=4096\) row,

   ```math
   {M_{13}^{surf,SEL2}(4096)\over
   \underline M_{pre13}^{SEL2,20}(4096)}
   <0.31.
   ```

2. **Cofinal growth test.**  For some \(0<a<1\),

   ```math
   \log(1+B_N^{pre})
   <
   \min\{a,2-2a\}\log N
   -\log2
   -G_{\log2}
   +o(1).
   ```

3. **Sharper escape-tail test.**  A same-record escape theorem improves the
   Chebyshev logarithmic surplus; then the right side in item 2 is replaced
   by that improved surplus.

Without one of these facts, the branch is parked at the named finite
same-record growth problem

```math
\mathrm{P22\text{-}PREFRATIO\text{-}GROWTH}.
```

Proof.

Definition 33.1 is exactly Paper 20's necessary-and-sufficient prefactor cap
written for the large-\(N\) Branch-A family. Lemma 33.2 says the existing
surface export is branchwise finite but does not print the ratio's
\(N\)-growth. Lemma 33.3 shows why that missing datum is real: the denominator
may shrink exponentially in \(N\). Lemma 33.4 gives the precise growth
condition that the current Chebyshev large-\(N\) surplus can absorb. Therefore
the current corpus reduces the problem to items 1--3 and does not close it
unconditionally. `square`

### Corollary 33.6: Next Branch Decision

The mainline continuation after Branch A is now sharply split.

1. If the target declaration is fixed at \(N=4096\), compute the literal
   finite ratio \(B_{4096}^{pre}\) and test \(B_{4096}^{pre}<0.31\).
2. If the target may remain adaptive in \(N\), prove
   `P22-PREFRATIO-GROWTH`, preferably by combining a lower floor for
   \(\underline M_{pre13}^{SEL2,20}(N)\) with a same-record surface entry
   bound for \(M_{13}^{surf,SEL2}(N)\).
3. If the ratio grows faster than the available Branch-A surplus, return to
   Branch B and attempt a genuinely stronger same-record surface theorem.

Thus Branch A has closed the rate gate but has not yet closed the full
Paper-20 surface pass.  The surviving obstruction is no longer
`TREE-TIME` or `ESC-MASS`; it is the explicitly named ratio-growth source
`P22-PREFRATIO-GROWTH`.

## 34. Fixed \(N=4096\) Ratio Worksheet And Denominator Floor

Section 33 showed why a naive large-\(N\) prefactor ratio is not licensed:
if the signal profile is frozen poorly, the pre-surface margin can decay with
\(N\).  This section records the cheapest repair before touching Branch B.
The repair is not a new law.  It is a scalar selector choice inside the
Paper-21 signal worksheet, frozen before the final \(N=4096\) cap is tested.

### Definition 34.1: High-\(\alpha\) Fixed-Row Selector

For the declared \(N=4096\) fundamental row, set

```math
\alpha_{4096}:=1-{1\over4096},
\qquad
\epsilon_{G,4096}:={1\over4096}.
```

Keep the already active values

```math
s={51\over10},
\qquad
\epsilon_A=\chi={1\over100}.
```

For the large-field excess in the residual activity worksheet, choose

```math
\epsilon_{lf}\ge\log2.
```

All these are scalar proof parameters in the same pushed-forward `SEL2`
record law.  They do not add a new observable and they do not alter the
finite-table closures of Sections 11--14.

### Lemma 34.2: Uniform Signal Floor For The High-\(\alpha\) Row

For every \(N\ge4096\), the high-\(\alpha\) selector

```math
\alpha_N:=1-{1\over N},
\qquad
\epsilon_{G,N}:={1\over N}
```

satisfies the Paper-21 admissibility inequalities

```math
0<\alpha_N<1,
\qquad
0<\epsilon_{G,N}<\min\{\alpha_N^2,2(1-\alpha_N)\}.
```

Moreover, for \(s=51/10\) and \(\epsilon_A=\chi=1/100\), the `SEL2` signal
profile obeys the \(N\)-uniform lower floor

```math
F_{F_N}(s)\ge F_*,
```

where

```math
F_*:=
\exp\left(
-{3(101/100)^2\over4}{51\over10}
\right)(1-e^{-1})
=0.0127712638\ldots .
```

Proof.

The admissibility inequalities are immediate for \(N\ge4096\):
\(\epsilon_{G,N}=1/N<2/N=2(1-\alpha_N)\), and also
\(1/N<(1-1/N)^2=\alpha_N^2\).

Paper 21 Definition 5.1 gives

```math
F_{F_N}(s)
=
e^{-a_Ns}(1-e^{-b_Ns}),
```

with

```math
a_N
=
\left(2(1-\alpha_N)+\epsilon_{G,N}\right)
{(1+\chi)(1+\epsilon_A)C_2(F_N)\over2}.
```

For the high-\(\alpha\) selector,

```math
2(1-\alpha_N)+\epsilon_{G,N}={3\over N},
```

and \(C_2(F_N)=(N^2-1)/(2N)\).  Hence

```math
a_N
=
{3(101/100)^2\over4}\left(1-{1\over N^2}\right)
<
{3(101/100)^2\over4}.
```

Thus \(e^{-a_Ns}\) is bounded below by the first factor in \(F_*\).

For \(b_N\), the coefficient
\((1-1/N)^2-1/N\) is positive and close to \(1\), while
\((99/100)^2C_2(F_N)s/2\) grows linearly in \(N\).  In particular,
\((1-1/N)^2-1/N>1/2\) and \(C_2(F_N)/2>N/5\) for every
\(N\ge4096\), so

```math
b_Ns>{1\over2}\left({99\over100}\right)^2{N\over5}{51\over10}>1.
```

Therefore
\(1-e^{-b_Ns}\ge1-e^{-1}\). Multiplying the two lower bounds gives the
claim. `square`

### Lemma 34.3: Uniform Decoration-Margin Floor

On the same high-\(\alpha\) row, if \(\epsilon_{lf}\ge\log2\), then

```math
\bar\eta_{res,20}\le {1\over2}\tau_{20},
\qquad
\widehat\eta_{*,20}\le {3\over4}\tau_{20}.
```

Consequently the Paper-20 decoration margin satisfies

```math
\underline M_{loss}^{SEL2,20}(N)
\ge
M_*,
```

where

```math
M_*:={1\over4}\log(1+F_*)
=0.00317259975\ldots .
```

Proof.

Paper 20 Theorem 4.3A.31 and Paper 21 Lemma 6.2 give, with
\(\delta_{20}=\delta_{20}^{suff}+\epsilon_{lf}\),

```math
\bar\eta_{res,20}
\le
{2C_{KP}e^{-\epsilon_{lf}}\tau_{20}
\over
2C_{KP}+(1-e^{-\epsilon_{lf}})\tau_{20}}.
```

Since \(\epsilon_{lf}\ge\log2\), \(e^{-\epsilon_{lf}}\le1/2\), and the
denominator is at least \(2C_{KP}\). Hence
\(\bar\eta_{res,20}\le\tau_{20}/2\).  The definition
\(\widehat\eta_{*,20}=(\tau_{20}+\bar\eta_{res,20})/2\) then gives
\(\widehat\eta_{*,20}\le3\tau_{20}/4\).

Write \(L=\log(1+F_{F_N}(s))\) and
\(\tau_{20}=L/(20+L)\).  The map \(h(\eta)=20\eta/(1-\eta)\) satisfies
\(h(\tau_{20})=L\). Since

```math
h\left({3\over4}\tau_{20}\right)
=
{15\tau_{20}\over1-(3/4)\tau_{20}}
<
{3\over4}L,
```

we get

```math
\underline M_{loss}^{SEL2,20}
=
e^L-e^{h(\widehat\eta_{*,20})}
\ge
e^L-e^{3L/4}
\ge
{L\over4}.
```

Lemma 34.2 gives \(L\ge\log(1+F_*)\), hence the displayed floor. `square`

### Definition 34.4: Fixed-Row Literal Ratio Data

On the high-\(\alpha\), \(N=4096\) row, define the two finite quantities still
needed for the literal prefactor cap:

```math
L_{pre13}^{4096}
:=
L_{pre13}^{SEL2}(4096),
```

and

```math
S_{13}^{4096}
:=
M_{13}^{surf,SEL2}(4096)
=
\limsup_j\max_{C\in B_{CR,j}}
A_{C,j}e^{\xi'_{C,j}}
u_{F_{4096},s_0,j}^{N_j(C)}.
```

The fixed-row usable denominator is

```math
M_{pre}^{4096}
:=
\underline M_{loss}^{SEL2,20}(4096)-L_{pre13}^{4096}.
```

By Lemma 34.3, the denominator is certainly positive if

```math
L_{pre13}^{4096}<M_*.
```

### Theorem 34.5: Fixed \(N=4096\) Cap Reduced To Two Literal Numbers

The fixed \(N=4096\) Branch-A surface prefactor cap is closed if

```math
L_{pre13}^{4096}<M_*
```

and

```math
S_{13}^{4096}
<
0.31\left(M_*-L_{pre13}^{4096}\right).
```

In the strict zero-predebit subcase \(L_{pre13}^{4096}=0\), it is enough to
prove

```math
S_{13}^{4096}
<
0.000983505923\ldots .
```

With the constants currently printed in Papers 13, 19, 20, and 21, the first
inequality and the second inequality are not yet literal numeric theorems.
Thus the fixed-row route is not closed, but it is now reduced to two finite
same-record source values:

```math
\mathrm{P22\text{-}PREDEBIT\text{-}4096}(L_{pre13}^{4096})
\quad\text{and}\quad
\mathrm{P22\text{-}SURFNUM\text{-}4096}(S_{13}^{4096}).
```

Proof.

Lemma 34.3 gives
\(\underline M_{loss}^{SEL2,20}(4096)\ge M_*\). Therefore

```math
M_{pre}^{4096}
\ge
M_*-L_{pre13}^{4096}.
```

If \(L_{pre13}^{4096}<M_*\), this lower bound is positive. Lemma 32.2 says the
declared \(N=4096\) rate surplus is \(>0.2724\), so the rounded Paper-20
prefactor cap follows from

```math
{S_{13}^{4096}\over M_{pre}^{4096}}<0.31.
```

The displayed sufficient inequality implies this ratio bound. The strict
zero-predebit number is \(0.31M_*=0.000983505923\ldots\).

The current papers define \(L_{pre13}^{4096}\) and \(S_{13}^{4096}\) as finite
same-record quantities, but do not print their literal values or sharp enough
upper bounds. Hence the reduction is complete, while the cap itself remains
parked at these two finite source values. `square`

### Corollary 34.6: Updated Branch-A Status

The denominator-growth worry from Section 33 is removable by the high-\(\alpha\)
selector.  The remaining fixed-row obstruction is more concrete:

```text
print L_pre13^4096 and S_13^4096 sharply enough.
```

If those two values satisfy Theorem 34.5, the declared \(N=4096\) Branch-A
surface pass closes.  If they do not, the next rational move is not to revisit
`TREE-TIME` or `ESC-MASS`; it is either:

1. prove a sharper same-record surface numerator bound for
   \(S_{13}^{4096}\);
2. reduce the pre-surface debit \(L_{pre13}^{4096}\); or
3. abandon the fixed \(N=4096\) row and return to the adaptive
   `P22-PREFRATIO-GROWTH` route.

## 35. Printed Fixed-\(4096\) Bounds For \(L_{pre13}\) And \(S_{13}\)

Section 34 reduced the fixed-row surface pass to two literal same-record
numbers.  This section prints the sharpest bounds licensed by the present
papers.  The point is deliberately modest: no parked debit is spent as zero
unless a previous theorem has actually licensed that deletion on the same
pushed-forward scalar law.

### Definition 35.1: Strict Fixed-Row Ledger Convention

Work on the high-\(\alpha\), \(N=4096\) row of Definition 34.1 and on the
strict scalar-record branch with:

1. exact Paper-12 diagonal loop records, so the reduced \(T_{12}\) readout
   debit is zero;
2. the no-corner selector already used in the non-corner worksheet;
3. exact block-entry `BC/CE/KPdec/WP` conventions as reduced in Paper 21;
4. the remaining Paper-16 RP/covariance and exact-entry `RPF` slots kept in
   their own ledgers.

If the no-corner selector is not used, every bound below must be enlarged by
the corresponding fixed-row corner debit \(E_{corn}^{car,4096}\).

### Definition 35.2: Fixed-Row Pre-Surface Carriers

Define the conservative Paper-21 carrier

```math
\mathcal L_{4096}^{car}
:=
E_{14}^{park}(4096)
+X_{13}^{(26),SEL2}(4096)
+U_{11}^{RPCov,car,SEL2}(4096)
+U_{13}^{RPF,bd}(4096).
```

Here \(U_{11}^{RPCov,car,SEL2}(4096)\) means the Paper-16 RP/covariance
moving-row carry evaluated on the fixed \(N=4096\) high-\(\alpha\) row.

On the stricter Paper-22 row-complete finite-table branch
`P22-LICGRAPH-CLOSE+`, the common \(E_{14}/X_{13}\) reduced-tail obstruction
is discharged by Theorem 14.7.  On that branch one may instead use

```math
\mathcal L_{4096}^{rc}
:=
U_{11}^{RPCov,car,SEL2}(4096)
+U_{13}^{RPF,bd}(4096).
```

The second carrier is not a universal replacement for the first; it is
licensed only together with the strict row-complete same-record envelope of
Sections 11--14.

### Theorem 35.3: Printed Bound For \(L_{pre13}^{4096}\)

On the fixed \(N=4096\) strict ledger branch,

```math
\boxed{
L_{pre13}^{4096}\le \mathcal L_{4096}^{car}.
}
```

On the additional `P22-LICGRAPH-CLOSE+` branch,

```math
\boxed{
L_{pre13}^{4096}\le \mathcal L_{4096}^{rc}.
}
```

Consequently the denominator condition of Theorem 34.5 is certified by either
of the sufficient inequalities

```math
\mathcal L_{4096}^{car}<M_*
```

or, on the row-complete branch,

```math
\mathcal L_{4096}^{rc}<M_*,
```

where

```math
M_*=0.00317259975\ldots .
```

Proof.

Paper 20 Theorem 4.3A.58 gives
\(L_{pre13}^{SEL2}\le U_{pre13}^{SEL2}\).  Paper 21 Sections 59--67 reduce
the strict non-corner \(U_{pre13}^{SEL2}\) ledger to

```math
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{11}^{RPCov,car,SEL2}
+U_{13}^{RPF,bd},
```

after the exact Paper-12 diagonal and exact-entry `BC/CE/KPdec/WP` reductions.
Evaluating that same ledger on the fixed \(N=4096\) row gives the first
display.

The second display uses the extra Paper-22 branch assumption
`P22-LICGRAPH-CLOSE+`: Theorem 14.7 discharges the common finite-table
reduced-tail obstruction for the \(E_{14}/X_{13}\) pair, while explicitly not
touching the disjoint Paper-16 RP/covariance carry or exact-entry `RPF` carry.
Thus only \(U_{11}^{RPCov,car,SEL2}(4096)+U_{13}^{RPF,bd}(4096)\) remains in
the fixed-row pre-surface ledger.  The two denominator tests are then
immediate from Lemma 34.3. `square`

### Definition 35.4: Surface-Numerator Source Constants

For the same fixed row, define the literal surface constants

```math
A_{4096}^{surf}
:=
\limsup_j\max_{C\in B_{CR,j}} A_{C,j},
```

```math
\Xi_{4096}^{surf}
:=
\limsup_j\max_{C\in B_{CR,j}} \xi'_{C,j},
```

```math
\kappa_{4096}^{surf}
:=
\liminf_j\bigl(-\log u_{F_{4096},s_0,j}\bigr),
```

and

```math
N_{4096}^{surf}
:=
\liminf_j\min_{C\in B_{CR,j}}N_j(C).
```

The Paper-13 surface-entry branch is subcritical, so \(u_{F_{4096},s_0,j}<1\)
eventually and \(\kappa_{4096}^{surf}>0\) is the same-record surface
coefficient decay exponent.  Since a nonminimal surface correction has at
least one elementary surface unit,

```math
N_{4096}^{surf}\ge1.
```

### Theorem 35.5: Sharp Printed Bound For \(S_{13}^{4096}\)

The fixed-row surface numerator obeys

```math
\boxed{
S_{13}^{4096}
\le
\mathcal S_{4096}^{surf}
:=
A_{4096}^{surf}
\exp\left(
\Xi_{4096}^{surf}
-\kappa_{4096}^{surf}N_{4096}^{surf}
\right).
}
```

In particular, without printing the literal minimum surface size beyond
nonemptiness, the universal fixed-row bound is

```math
\boxed{
S_{13}^{4096}
\le
A_{4096}^{surf}\exp\left(\Xi_{4096}^{surf}-\kappa_{4096}^{surf}\right).
}
```

Proof.

Definition 34.4 gives

```math
S_{13}^{4096}
=
\limsup_j\max_{C\in B_{CR,j}}
A_{C,j}e^{\xi'_{C,j}}
u_{F_{4096},s_0,j}^{N_j(C)}.
```

For every \(\varepsilon>0\) and all sufficiently large \(j\),

```math
A_{C,j}\le A_{4096}^{surf}+\varepsilon,\qquad
\xi'_{C,j}\le \Xi_{4096}^{surf}+\varepsilon,
```

uniformly in \(C\), while

```math
-\log u_{F_{4096},s_0,j}\ge \kappa_{4096}^{surf}-\varepsilon,
\qquad
N_j(C)\ge N_{4096}^{surf}.
```

Therefore the row-\(j\) maximum is bounded by

```math
(A_{4096}^{surf}+\varepsilon)
\exp\left(
\Xi_{4096}^{surf}+\varepsilon
-(\kappa_{4096}^{surf}-\varepsilon)N_{4096}^{surf}
\right).
```

Taking the limsup and then \(\varepsilon\downarrow0\) proves the first bound.
The second bound uses \(N_{4096}^{surf}\ge1\). `square`

### Corollary 35.6: Fixed-\(4096\) Cap In Fully Printed Form

The fixed \(N=4096\) surface pass is closed by the conservative carried test

```math
\mathcal L_{4096}^{car}<M_*
```

and

```math
\mathcal S_{4096}^{surf}
<
0.31\left(M_*-\mathcal L_{4096}^{car}\right).
```

On the row-complete `P22-LICGRAPH-CLOSE+` branch, the corresponding sharper
test is

```math
\mathcal L_{4096}^{rc}<M_*
```

and

```math
\mathcal S_{4096}^{surf}
<
0.31\left(M_*-\mathcal L_{4096}^{rc}\right).
```

Equivalently, the surface-numerator inequality may be written as the log
condition

```math
\kappa_{4096}^{surf}N_{4096}^{surf}
>
\log A_{4096}^{surf}
+\Xi_{4096}^{surf}
-\log\left(0.31(M_*-\mathcal L)\right),
```

where \(\mathcal L\) is either \(\mathcal L_{4096}^{car}\) or, on the
row-complete branch, \(\mathcal L_{4096}^{rc}\).  In the strict zero-predebit
subcase this becomes

```math
\kappa_{4096}^{surf}N_{4096}^{surf}
>
\log A_{4096}^{surf}
+\Xi_{4096}^{surf}
+6.924386899\ldots .
```

Thus the present corpus has now printed the fixed-row problem as two explicit
finite same-record inequalities.  On the conservative Paper-21 carrier, the
additional live source values are

```math
E_{14}^{park}(4096),\quad
X_{13}^{(26),SEL2}(4096).
```

On the Paper-22 row-complete branch, the remaining six source values are

```math
U_{11}^{RPCov,car,SEL2}(4096),\quad
U_{13}^{RPF,bd}(4096),
\quad
A_{4096}^{surf},\quad
\Xi_{4096}^{surf},\quad
\kappa_{4096}^{surf},\quad
N_{4096}^{surf}.
```

Without the appropriate source values for the chosen carrier, the fixed
\(N=4096\) cap is sharply bounded but not yet closed. `square`

## 36. Terminal Branch-A Audit On The Fixed \(N=4096\) Row

We now execute the fixed-row tasks from Corollary 35.6 in their most favorable
licensed order.  The conclusion is a terminal current-corpus verdict: Branch A
closes the rate side and supplies a large normalized coefficient rate, but the
full Paper-20 surface pass is still not an unconditional theorem unless the
remaining tiny predebit and surface-numerator source values are printed.

### Definition 36.1: Active Branch-A Carrier

For the rest of the Branch-A audit, use the strict row-complete carrier

```math
\mathcal L_{4096}^{rc}
=
U_{11}^{RPCov,car,SEL2}(4096)
+U_{13}^{RPF,bd}(4096).
```

The conservative carrier with \(E_{14}^{park}+X_{13}^{(26),SEL2}\) is retained
only as a fallback.  It is not the active Branch-A attempt, because
Theorem 14.7 has already discharged the common finite-table \(E_{14}/X_{13}\)
reduced-tail obstruction on the row-complete branch.

### Lemma 36.2: The RP/Cov Slot Cannot Be Spent As Zero From The Present Papers

The current source stack does not prove

```math
U_{11}^{RPCov,car,SEL2}(4096)=0.
```

The only licensed fixed-row evaluation is the carried bound

```math
U_{11}^{RPCov,car,SEL2}(4096)
\le
U_{11}^{RP,bd,SEL2}(4096)+U_{11}^{Cov,bd,SEL2}(4096),
```

if the two finite ceilings are supplied.  To close the fixed-row cap by this
route one needs the much sharper smallness condition

```math
U_{11}^{RPCov,car,SEL2}(4096)
+U_{13}^{RPF,bd}(4096)
<
0.00317259975\ldots .
```

Proof.

Paper 21 Theorem 59.2 and Lemma 67.5 identify this slot as a moving-row
Paper-16 RP/covariance transport tail.  Paper 16 supplies the RP/covariance
transport architecture and the heat-kernel/actual-trajectory ledgers, but its
compact gate ledger still lists the actual-trajectory burden as the need to
verify summable RP and covariance defects on the chosen tower.  It does not
print the fixed \(N=4096\) moving-row limits

```math
\sum_{k\ge j}D_{11;j,k}^{RP,red,SEL2}\to0,
\qquad
\sup_g\sum_{k\ge j}D_{11;j,k}^{Cov,red,SEL2}(g)\to0.
```

Therefore the zero conclusion is not licensed.  The numerical smallness
threshold is just Lemma 34.3's value \(M_*\), because the row-complete
pre-surface margin is positive only if
\(\mathcal L_{4096}^{rc}<M_*\). `square`

### Lemma 36.3: The `RPF` Slot Cannot Be Spent As Zero From The Present Papers

The current source stack does not prove

```math
U_{13}^{RPF,bd}(4096)=0.
```

The exact-entry `RPF` record availability cost is zero, but the pure residual
factorization defect remains live unless one proves

```math
\mathrm{P21\text{-}U13\text{-}RPF\text{-}FACT0}
```

or a fixed-row bound small enough to fit inside the same \(M_*\) budget.

Proof.

Paper 13 Theorem 7.30AS proves `RPF` and `KP_dec` from a connected-cumulant
KP criterion for the exact block record functional.  Paper 20 Definition
4.3A.72 and Theorem 4.3A.73 place the corresponding residual
\(\epsilon_{RPF,j}^{SEL2}\) in the exact-entry ledger.  Paper 21 Theorem 33.4
then separates record availability from actual factorization: the records are
available on the strict scalar branch, but
\(U_{13}^{RPF,car}=0\) only under `P21-U13-RPF-FACT0`; otherwise one may carry
the finite template bound \(U_{13}^{RPF,bd}\).  No later Paper-22 finite-table
closure deletes this disjoint exact-entry factorization slot. `square`

### Definition 36.4: Certified \(N=4096\) Surface Coefficient Rate

For the declared \(N=4096\) row, Definition 32.1 gives

```math
p_{4096,*}=0.992627916884\ldots .
```

Set

```math
\kappa_{4096}^{esc}
:=
-\log(1-p_{4096,*})
=4.910054964\ldots ,
```

and

```math
\kappa_{4096}^{time}
:=
{T_-^{SEL2}C_2(F_{4096})\over2}
=5118.4739\ldots .
```

The Branch-A certified normalized rate is therefore

```math
\kappa_{4096}^{cert}
:=
\min\{\kappa_{4096}^{time},\kappa_{4096}^{esc}\}
=4.910054964\ldots .
```

Every strict

```math
0<\kappa_{4096}^{use}<\kappa_{4096}^{cert}
```

may be inserted into downstream strict inequalities.

### Lemma 36.5: Surface \(u\)-Decay Is Certified Up To The Branch-A Rate

On the strict normalized surface convention of Paper 20, the fixed-row
surface coefficient satisfies

```math
\kappa_{4096}^{surf}
\ge
\kappa_{4096}^{use}
```

for every strict \(\kappa_{4096}^{use}<4.910054964\ldots\).

Proof.

Paper 20 Definition 4.3A.160BH.40D defines the conservative certified surface
rate as the minimum of the time and escape floors, and Corollary
4.3A.160BH.40E proves the normalized coefficient rate for every strict smaller
constant.  Paper 20's normalized dimension-cancellation audit identifies the
active surface sheet weight with the normalized one-plaquette coefficient used
in that rate audit.  Definition 32.1 computes the two fixed-row floors for
\(F_{4096}\), and the escape floor is the bottleneck.  Therefore the
surface-numerator exponent in Definition 35.4 may use any strict
\(\kappa_{4096}^{use}<4.910054964\ldots\). `square`

### Corollary 36.6: The Fixed-Row Cap As A Numeric Source Inequality

Choose any strict
\(\kappa_{4096}^{use}<4.910054964\ldots\).  The row-complete fixed
\(N=4096\) Branch-A cap closes if

```math
U_{11}^{RPCov,car,SEL2}(4096)
+U_{13}^{RPF,bd}(4096)
<
M_*
```

and

```math
A_{4096}^{surf}
\exp\left(
\Xi_{4096}^{surf}
-\kappa_{4096}^{use}N_{4096}^{surf}
\right)
<
0.31\left(
M_*
-U_{11}^{RPCov,car,SEL2}(4096)
-U_{13}^{RPF,bd}(4096)
\right).
```

Equivalently,

```math
\kappa_{4096}^{use}N_{4096}^{surf}
>
\log A_{4096}^{surf}
+\Xi_{4096}^{surf}
-\log\left(
0.31\left(
M_*
-U_{11}^{RPCov,car,SEL2}(4096)
-U_{13}^{RPF,bd}(4096)
\right)
\right).
```

In the optimistic zero-predebit, unit-prefactor diagnostic

```math
U_{11}^{RPCov,car,SEL2}(4096)=U_{13}^{RPF,bd}(4096)=0,
\qquad
A_{4096}^{surf}=1,\quad \Xi_{4096}^{surf}=0,
```

the right side is \(6.924386899\ldots\).  Since

```math
{6.924386899\ldots\over4.910054964\ldots}
=1.41024631\ldots ,
```

the certified rate would need at least

```math
N_{4096}^{surf}\ge2
```

even in that optimistic diagnostic.  A merely nonempty surface factor
\(N_{4096}^{surf}\ge1\) is not enough by itself.

### Theorem 36.7: Terminal Current-Corpus Verdict For Branch A

Branch A is now fully decided at the current source level.

1. **Rate side:** closed.  The declared \(N=4096\) branch passes
   `TREE-TIME` and `ESC-MASS`, with rate surplus \(>0.2724\).
2. **Common \(E_{14}/X_{13}\) reduced-tail obstruction:** closed on the
   strict row-complete branch by `P22-LICGRAPH-CLOSE+`.
3. **Pre-surface denominator:** reduced to the tiny same-record inequality

   ```math
   U_{11}^{RPCov,car,SEL2}(4096)+U_{13}^{RPF,bd}(4096)
   <0.00317259975\ldots .
   ```

   The current papers do not prove this inequality, and they do not prove the
   two summands are zero.
4. **Surface numerator:** the coefficient decay part is certified up to
   \(4.910054964\ldots\), but the current papers do not print the fixed-row
   values

   ```math
   A_{4096}^{surf},\quad
   \Xi_{4096}^{surf},\quad
   N_{4096}^{surf}.
   ```

5. **Full surface prefactor cap:** not closed unconditionally by the current
   corpus.  It is also not falsified, because sufficiently small RP/Cov and
   `RPF` carries together with \(N_{4096}^{surf}\ge2\) and modest surface
   prefactors would pass the displayed inequalities.

Thus the exact terminal status is the named fixed-row source gate

```math
\mathrm{P22\text{-}BRANCHA\text{-}4096\text{-}PREFCAP}
```

consisting of the two inequalities in Corollary 36.6.  No additional
iteration inside Papers 13, 16, 19, 20, 21, or the current Paper 22 can turn
this into a theorem without new same-record source data for RP/Cov, `RPF`, or
the printed surface constants.

This is the honest Branch-A endpoint.  The next mathematical work is not to
re-open `TREE-TIME` or `ESC-MASS`; it is to prove the named fixed-row
prefactor source gate, move to the adaptive \(N\)-growth version
`P22-PREFRATIO-GROWTH`, or abandon Branch A for a stronger Branch-B surface
route. `square`

## 37. Branch-A Closure Attempt And Adaptive Endpoint

Section 36 left no hidden algebraic freedom on the fixed \(N=4096\) row.  This
section executes the promised five-step closure attempt.  The outcome is
sharp: the fixed row cannot be made into an unconditional theorem from the
present corpus, but adaptive Branch A reduces to one precise same-record
growth theorem.

### Definition 37.1: Fixed-Row Closure Package

On the row-complete \(N=4096\) branch write

```math
\mathcal L_{4096}^{rc}
=
U_{11}^{RPCov,car,SEL2}(4096)
+U_{13}^{RPF,bd}(4096)
```

and

```math
\mathcal S_{4096}^{surf}
=
A_{4096}^{surf}
\exp\left(\Xi_{4096}^{surf}
-\kappa_{4096}^{surf}N_{4096}^{surf}\right).
```

The fixed-row cap is the pair of inequalities

```math
\mathcal L_{4096}^{rc}<M_*,
```

and

```math
\mathcal S_{4096}^{surf}
<
0.31\left(M_*-\mathcal L_{4096}^{rc}\right).
```

This is a source package, not a definition of success by decree:

```math
\mathrm{P22\text{-}BRANCHA\text{-}4096\text{-}PREFCAP}.
```

### Lemma 37.2: Fixed \(4096\) Cannot Be Closed From The Printed Corpus

The present papers do not prove

```math
\mathrm{P22\text{-}BRANCHA\text{-}4096\text{-}PREFCAP}.
```

More explicitly:

1. they do not prove

   ```math
   U_{11}^{RPCov,car,SEL2}(4096)
   +U_{13}^{RPF,bd}(4096)
   <M_*;
   ```

2. they do not print numerical values of

   ```math
   A_{4096}^{surf},\quad
   \Xi_{4096}^{surf},\quad
   N_{4096}^{surf};
   ```

3. the universal nonempty-sheet consequence of Paper 13 is only
   \(N_{4096}^{surf}\ge1\), while Corollary 36.6 shows that even the
   zero-predebit, unit-prefactor diagnostic needs \(N_{4096}^{surf}\ge2\).

Proof.

Item 1 is exactly Lemmas 36.2 and 36.3.  Paper 16 supplies the RP/covariance
transport ledgers, but Paper 21 Lemma 59.1 and Lemma 67.5 record that the
active moving-row RP/Cov tail limits are not printed.  Paper 13 supplies the
`RPF` criterion, but Paper 21 Theorem 33.4 keeps the pure residual
factorization slot carried unless `P21-U13-RPF-FACT0` is proved.

Item 2 is the finite surface envelope of Paper 13 and Paper 19.  Paper 13
Proposition 7.30E and Theorem 7.30M prove the form

```math
A_Ce^{\xi'_C}u_{\rho,s_0}^{N(C)}
{B_Cu_{\rho,s_0}\over1-B_Cu_{\rho,s_0}},
```

and Paper 19 Theorem 8L.11A.23 exports the cofinal envelope
\(M_{13}^{surf}\).  They prove finiteness under the surface-entry package;
they do not print the fixed \(4096\) values needed in Definition 37.1.

Item 3 is the strict geometry check.  Paper 13's target surface-polymer entry
requires a declared minimal sheet with \(N(C)\in{\mathbb N}\), hence a
nonempty lower bound.  It does not declare that the active \(N=4096\) Creutz
battery has minimal area at least two in every row entering the maximum.
Corollary 36.6 already computes that one sheet is not enough even in the
best diagnostic.  Therefore the fixed \(4096\) route is fully reduced but
not closed by the printed corpus. `square`

### Definition 37.3: Adaptive Branch-A Carrier

For a cofinal family of fundamental channels \(F_N\), \(N\ge4096\), use the
same high-\(\alpha\) selector from Lemma 34.2:

```math
\alpha_N=1-{1\over N},
\qquad
\epsilon_{G,N}={1\over N},
\qquad
s={51\over10},
\qquad
\epsilon_A=\chi={1\over100},
\qquad
\epsilon_{lf}\ge\log2.
```

Define

```math
\mathcal L_N^{rc}
:=
U_{11}^{RPCov,car,SEL2}(N)
+U_{13}^{RPF,bd}(N),
```

and

```math
S_N^{surf}
:=
M_{13}^{surf,SEL2}(N)
=
\limsup_j\max_{C\in B_{CR,j}(N)}
A_{C,j}(N)e^{\xi'_{C,j}(N)}
u_{F_N,s_0,j}^{N_j(C)}.
```

The usable pre-surface denominator is

```math
M_{pre,N}^{rc}
:=
\underline M_{loss}^{SEL2,20}(N)-\mathcal L_N^{rc}.
```

By Lemma 34.3, the loss floor itself is uniform:

```math
\underline M_{loss}^{SEL2,20}(N)\ge M_*
\qquad (N\ge4096).
```

Thus adaptive Branch A is not blocked by the old Section-33 exponential
denominator worry once the high-\(\alpha\) selector is frozen.  It is blocked
only by the growth of \(\mathcal L_N^{rc}\) and \(S_N^{surf}\) on the same
pushed-forward scalar law.

### Definition 37.4: Adaptive Prefactor-Growth Source

For \(0\le\beta<2/3\), define

```math
\mathrm{P22\text{-}BRANCHA\text{-}ADAPT\text{-}PREFGROWTH}(\beta)
```

to mean that there are constants \(C<\infty\), \(\mu>0\), and a cofinal set of
integers \(N\ge4096\) such that

```math
\mathcal L_N^{rc}\le M_*-\mu
```

and

```math
S_N^{surf}\le CN^\beta
```

on the same high-\(\alpha\), row-complete, pushed-forward `SEL2` scalar law.

The exact logarithmic version is the same statement with the two displayed
inequalities replaced by

```math
M_{pre,N}^{rc}>0,
\qquad
\log\left(1+{S_N^{surf}\over M_{pre,N}^{rc}}\right)
<
\Delta_{13,tree}^{SEL2}(N)
```

cofinally.  The polynomial form above is the cleanest sufficient source
because the Chebyshev Branch-A surplus has exponent \(2/3\).

### Theorem 37.5: Adaptive Branch A Closes Under Sub-\(2/3\) Prefactor Growth

If

```math
\mathrm{P22\text{-}BRANCHA\text{-}ADAPT\text{-}PREFGROWTH}(\beta)
```

holds for some \(\beta<2/3\), then adaptive Branch A closes the Paper-20
surface prefactor cap cofinally.

Proof.

By Definition 37.4 and Lemma 34.3,

```math
M_{pre,N}^{rc}
\ge
\mu
```

on the cofinal set.  Therefore

```math
\log\left(1+{S_N^{surf}\over M_{pre,N}^{rc}}\right)
\le
\log\left(1+{C\over\mu}N^\beta\right)
=
\beta\log N+O(1).
```

Use the Chebyshev selector \(a=2/3\) in Lemma 33.4.  Then

```math
\Delta_{13,tree}^{SEL2}(N)
\ge
{2\over3}\log N-\log2-G_{\log2}+o(1)
```

cofinally, because the time rate grows linearly in \(N\) and the escape rate
is the logarithmic bottleneck.  Since \(\beta<2/3\), the difference between
the right side and \(\beta\log N+O(1)\) tends to \(+\infty\).  Hence the exact
Paper-20 cap

```math
S_N^{surf}
<
M_{pre,N}^{rc}
\left(\exp(\Delta_{13,tree}^{SEL2}(N))-1\right)
```

holds cofinally.  All quantities are scalar loop/block records under the same
pushforward; no continuum Yang-Mills measure, area law, or hidden field
ontology is imported. `square`

### Theorem 37.6: Final Branch-A Verdict At The Current Source Level

Branch A is fully settled as a source audit.

1. **Fixed \(N=4096\):** rate, escape, and denominator floor are closed, but
   the full surface cap is not an unconditional theorem.  It is exactly
   `P22-BRANCHA-4096-PREFCAP`.
2. **Adaptive \(N\):** the denominator-growth obstruction is removed by the
   high-\(\alpha\) selector, and the whole remaining problem is exactly
   `P22-BRANCHA-ADAPT-PREFGROWTH(beta)` for some \(\beta<2/3\), or the exact
   logarithmic inequality in Definition 37.4.
3. **Current corpus:** Papers 13, 16, 19, 20, 21, and the present finite-table
   closures do not print either source package.  They give branchwise finite
   surface envelopes and disjoint carried RP/Cov and `RPF` slots, but not the
   fixed tiny bounds, fixed surface constants, or cofinal sub-\(2/3\) growth
   law.

Therefore Branch A is neither an unconditional confinement proof nor a
falsified route.  Its exact continuation theorem is now:

```math
\boxed{
\text{prove fixed } \mathrm{P22\text{-}BRANCHA\text{-}4096\text{-}PREFCAP}
\text{ or adaptive }
\mathrm{P22\text{-}BRANCHA\text{-}ADAPT\text{-}PREFGROWTH}(\beta<2/3).
}
```

If neither can be sourced on the same scalar law, Branch A is exhausted and
the work must move to Branch B or to a new signed/selector surface route.
`square`

## 38. Final Adaptive Branch-A Source Split

The previous section reduced adaptive Branch A to a sub-\(2/3\) prefactor
growth theorem.  This section pushes that reduction one step further, so that
Branch A has no vague remaining "large constant" problem.  The exact
remaining inputs are a predebit margin and a surface-log growth bound.

### Definition 38.1: Adaptive Surface Log Data

On the high-\(\alpha\) adaptive branch of Definition 37.3, define

```math
H_N^{surf}
:=
\limsup_j
\max_{C\in B_{CR,j}(N)}
\left(\log A_{C,j}(N)+\xi'_{C,j}(N)\right),
```

and

```math
n_N^{surf}
:=
\liminf_j\min_{C\in B_{CR,j}(N)}N_j(C).
```

Then

```math
S_N^{surf}
\le
\exp\left(
H_N^{surf}-\kappa_N^{surf}n_N^{surf}
\right),
```

where

```math
\kappa_N^{surf}
:=
\liminf_j\left(-\log u_{F_N,s_0,j}\right).
```

All three quantities are finite scalar-record readouts once the Paper-13
surface-entry package is available on the declared row.

### Lemma 38.2: What Is Already Closed In The Adaptive Surface Split

On the adaptive Branch-A family:

1. the coefficient-rate part supplies, for every strict use of the Chebyshev
   selector \(a=2/3\),

   ```math
   \kappa_N^{surf}
   \ge
   {2\over3}\log N-\log2+o(1);
   ```

2. Paper 13 supplies the nonempty minimal-sheet floor

   ```math
   n_N^{surf}\ge1;
   ```

3. if the Creutz template is kept in one fixed finite geometric type while
   only the representation \(F_N\) changes, the pure excess-surface entropy
   part of \(H_N^{surf}\), namely \(\log A_{C,j}(N)\), is \(O(1)\).

Proof.

Item 1 is Lemma 33.4 with the optimizing choice \(a=2/3\), imported through
the Paper-20 normalized coefficient-rate comparison exactly as in Lemma 36.5.
The time rate grows linearly in \(N\), so the logarithmic escape rate is the
bottleneck.

Item 2 is the minimal-sheet clause in Paper 13 Definition 7.30L and Lemma
7.30P: every declared rectangular loop has a nonempty area-minimizing
admissible block surface.

Item 3 is the finite-degree geometry statement of Paper 13 Lemma 7.30Q.  For
a fixed finite Creutz template, the root plaquette choices, local replacement
types, and plaquette-adjacency degree are finite geometric data, not
representation-theoretic data.  This controls the entropy prefactor.  It does
not control \(\xi'_{C,j}(N)\), which is produced by the decoration KP
cluster bound and belongs to the same-record decoration/source ledger.
`square`

### Definition 38.3: Two Adaptive Source Gates

For \(\mu>0\), define

```math
\mathrm{P22\text{-}BRANCHA\text{-}ADAPT\text{-}PREDEBIT}(\mu)
```

to mean that, cofinally,

```math
\mathcal L_N^{rc}
=
U_{11}^{RPCov,car,SEL2}(N)+U_{13}^{RPF,bd}(N)
\le
M_*-\mu.
```

For \(\theta\ge0\) and \(n_0\in{\mathbb N}\), define

```math
\mathrm{P22\text{-}BRANCHA\text{-}ADAPT\text{-}SURFLOG}(\theta,n_0)
```

to mean that, cofinally,

```math
n_N^{surf}\ge n_0,
\qquad
H_N^{surf}\le \theta\log N+O(1).
```

The default geometry supplied by Lemma 38.2 is \(n_0=1\).  A larger \(n_0\)
requires an explicit battery declaration saying that every Creutz loop used
in the surface maximum has minimal block area at least \(n_0\).

### Theorem 38.4: Exact Adaptive Closure Inequality

Assume

```math
\mathrm{P22\text{-}BRANCHA\text{-}ADAPT\text{-}PREDEBIT}(\mu)
```

and

```math
\mathrm{P22\text{-}BRANCHA\text{-}ADAPT\text{-}SURFLOG}(\theta,n_0).
```

If

```math
\theta<{2\over3}(n_0+1),
```

then adaptive Branch A closes cofinally.

In the default nonempty-sheet case \(n_0=1\), this becomes the concrete
threshold

```math
\theta<{4\over3}.
```

Proof.

By Definition 38.1, Lemma 38.2, and the surface-log source,

```math
\log S_N^{surf}
\le
\theta\log N
-n_0\left({2\over3}\log N-\log2+o(1)\right)
+O(1).
```

Thus

```math
S_N^{surf}
\le
C N^{\theta-(2/3)n_0+o(1)}.
```

If \(\theta<2(n_0+1)/3\), choose
\(\beta<2/3\) with

```math
\theta-{2n_0\over3}<\beta< {2\over3}.
```

Then, after enlarging \(C\) and passing to a cofinal tail,

```math
S_N^{surf}\le CN^\beta.
```

The predebit source gives \(\mathcal L_N^{rc}\le M_*-\mu\).  Hence the two
conditions of Definition 37.4 hold, and Theorem 37.5 closes adaptive Branch
A. `square`

### Lemma 38.5: Current Corpus Does Not Prove The Two Adaptive Source Gates

The current papers prove neither

```math
\mathrm{P22\text{-}BRANCHA\text{-}ADAPT\text{-}PREDEBIT}(\mu)
```

for any \(\mu>0\), nor

```math
\mathrm{P22\text{-}BRANCHA\text{-}ADAPT\text{-}SURFLOG}(\theta,n_0)
```

with \(\theta<2(n_0+1)/3\).

Proof.

For the predebit gate, Paper 21 Theorem 59.2 and Lemma 67.5 keep
\(U_{11}^{RPCov,car,SEL2}\) carried unless the Paper-16 moving-row RP/Cov
tails are proved on the active schedule.  Paper 21 Theorem 33.4 keeps
\(U_{13}^{RPF,bd}\) carried unless the pure residual factorization zero or a
sharp finite bound is supplied.  No later Paper-22 finite-table theorem gives
a uniform margin below \(M_*\).

For the surface-log gate, Lemma 38.2 closes the coefficient-rate piece,
the nonempty area floor, and the pure finite-template entropy prefactor under
a fixed geometric template.  The missing term is the same-record
decoration/minimal-collar log growth \(\xi'_{C,j}(N)\), together with any
change of the battery template as \(N\) varies.  Paper 19 closes
finite-template decoration audits along a declared cofinal row, but the
present corpus does not print a uniform-in-\(N\) bound

```math
\limsup_j\max_C \xi'_{C,j}(N)
\le
\theta\log N+O(1)
```

with \(\theta<2(n_0+1)/3\), nor does it print a larger \(n_0\) battery floor.
Therefore the adaptive source gates are not theorems of the present corpus.
`square`

### Theorem 38.6: Branch A Is Complete As A Source Audit

Branch A now has a final, non-ambiguous status.

1. **Unconditional Branch-A proof:** not obtained from the present corpus.
2. **Fixed \(N=4096\) route:** exactly
   `P22-BRANCHA-4096-PREFCAP`.
3. **Adaptive route:** exactly the pair

   ```math
   \mathrm{P22\text{-}BRANCHA\text{-}ADAPT\text{-}PREDEBIT}(\mu),
   \qquad
   \mathrm{P22\text{-}BRANCHA\text{-}ADAPT\text{-}SURFLOG}(\theta,n_0),
   \quad
   \theta<{2\over3}(n_0+1).
   ```

4. **Current-corpus verdict:** Branch A is exhausted unless one imports one
   of the displayed same-record source packages.  No remaining step inside
   Branch A is a hidden tree-time, escape-mass, coefficient-normalization,
   finite-table, or Barandes-ontology issue.

Thus, if the goal is to continue without adding new Branch-A source data, the
next mathematical branch is Branch B: a genuinely stronger same-record
surface theorem, or a signed/selector route with a full support re-audit.
If the goal is to keep Branch A alive, the only honest next tasks are the two
source theorems in item 3. `square`

## 39. Executing Branch-A Tasks 1--4

The requested Branch-A continuation consists of four operations:

1. continue on the adaptive \(F_N\), \(N\ge4096\), high-\(\alpha\) row;
2. attack the surface-log gate;
3. split \(H_N^{surf}\) into geometry and decoration/minimal-collar growth;
4. attack the predebit gate.

This section performs those operations and leaves Branch A with no hidden
subtask.

### Definition 39.1: The Active Adaptive Branch-A Row

The active row remains the high-\(\alpha\) adaptive row of Definition 37.3:

```math
\rho=F_N,\qquad N\ge4096,
```

with

```math
\alpha_N=1-{1\over N},
\qquad
\epsilon_{G,N}={1\over N},
\qquad
s={51\over10},
\qquad
\epsilon_A=\chi={1\over100},
\qquad
\epsilon_{lf}\ge\log2.
```

The coefficient/escape side is closed on this row.  The live Branch-A data
are exactly

```math
\mathcal L_N^{rc}
=
U_{11}^{RPCov,car,SEL2}(N)+U_{13}^{RPF,bd}(N)
```

and

```math
H_N^{surf},\qquad n_N^{surf}.
```

No later Branch-A step may change the pushed-forward scalar law, add an
unrecorded gauge-fixed process, or import an area law.

### Definition 39.2: The \(\xi'\)-Log Source

Define

```math
\Xi_N'
:=
\limsup_j\max_{C\in B_{CR,j}(N)}\xi'_{C,j}(N).
```

For \(\theta_\xi\ge0\), define

```math
\mathrm{P22\text{-}BRANCHA\text{-}XIPLOG}(\theta_\xi)
```

to be the same-record source assertion

```math
\Xi_N'\le \theta_\xi\log N+O(1)
```

cofinally on the adaptive row.  This is the missing uniform-in-\(N\)
decoration/minimal-collar growth theorem.  Paper 13 proves that each
\(\xi'_{C,j}(N)\) is finite once the `KP_dec` entry package holds on a
declared finite row; it does not print this cofinal \(N\)-growth law.

### Lemma 39.3: Surface-Log Split

Assume the Creutz battery is held in one fixed finite geometric template as
\(N\) varies.  Then

```math
H_N^{surf}
\le
\Xi_N'+O(1).
```

Consequently

```math
\mathrm{P22\text{-}BRANCHA\text{-}XIPLOG}(\theta_\xi)
\quad\Longrightarrow\quad
\mathrm{P22\text{-}BRANCHA\text{-}ADAPT\text{-}SURFLOG}
(\theta_\xi,1).
```

Proof.

By Definition 38.1,

```math
H_N^{surf}
=
\limsup_j\max_C(\log A_{C,j}(N)+\xi'_{C,j}(N)).
```

Paper 13 Lemma 7.30Q bounds the excess-surface entropy prefactor by a
finite-degree plaquette-animal count depending on the fixed block
plaquette-adjacency geometry and on the fixed finite Creutz template.  If
that template is not changed as \(N\) varies, the finite root set and local
replacement list are independent of the representation dimension.  Thus
\(\log A_{C,j}(N)=O(1)\) cofinally.  The only remaining \(N\)-growth in
\(H_N^{surf}\) is \(\xi'_{C,j}(N)\), so the displayed implication follows
from Definition 39.2 and the default \(n_N^{surf}\ge1\) floor of Lemma 38.2.
`square`

### Definition 39.4: Fixed Minimal-Area Amplifier

For a fixed integer \(n_0\ge1\), define

```math
\mathrm{P22\text{-}BRANCHA\text{-}AREA}(n_0)
```

to mean that the adaptive Creutz battery is declared before the final
inequalities and satisfies

```math
n_N^{surf}\ge n_0
```

cofinally, while still using one fixed finite geometric template family in
the sense of Lemma 39.3.

This is not a new physical ontology.  It is only a choice of finite scalar
loop records with larger block-rectangle minimal area.

### Theorem 39.5: Surface Side Closed By \(\xi'\)-Log Growth Plus Area

Assume

```math
\mathrm{P22\text{-}BRANCHA\text{-}XIPLOG}(\theta_\xi)
```

and

```math
\mathrm{P22\text{-}BRANCHA\text{-}AREA}(n_0).
```

If

```math
\theta_\xi<{2\over3}(n_0+1),
```

then the adaptive Branch-A surface-log gate closes:

```math
\mathrm{P22\text{-}BRANCHA\text{-}ADAPT\text{-}SURFLOG}
(\theta_\xi,n_0).
```

In particular, if \(\theta_\xi<4/3\), the default \(n_0=1\) battery is enough.
If \(\theta_\xi<\infty\) is printed but exceeds \(4/3\), any fixed

```math
n_0>{3\over2}\theta_\xi-1
```

is sufficient, provided the battery-area amplifier is declared and the
finite-template geometry remains fixed.

Proof.

Lemma 39.3 gives \(H_N^{surf}\le\theta_\xi\log N+O(1)\).  The area amplifier
gives \(n_N^{surf}\ge n_0\).  This is exactly
`P22-BRANCHA-ADAPT-SURFLOG(theta_xi,n0)`.  The inequality
\(\theta_\xi<2(n_0+1)/3\) is the closure threshold in Theorem 38.4. `square`

### Definition 39.6: Split Predebit Sources

For \(\lambda_{11},\lambda_{13}\ge0\), define

```math
\mathrm{P22\text{-}BRANCHA\text{-}RPCOV\text{-}MARGIN}(\lambda_{11})
```

to mean

```math
U_{11}^{RPCov,car,SEL2}(N)\le\lambda_{11}
```

cofinally, and define

```math
\mathrm{P22\text{-}BRANCHA\text{-}RPF\text{-}MARGIN}(\lambda_{13})
```

to mean

```math
U_{13}^{RPF,bd}(N)\le\lambda_{13}
```

cofinally.

The zero routes are the already isolated Paper-21 sources:

```math
\sum_{k\ge j}D_{11;j,k}^{RP,red,SEL2}\to0,
\qquad
\sup_g\sum_{k\ge j}D_{11;j,k}^{Cov,red,SEL2}(g)\to0,
```

for the RP/Cov term, and

```math
\mathrm{P21\text{-}U13\text{-}RPF\text{-}FACT0}
```

for the exact-entry residual factorization term.

### Theorem 39.7: Predebit Gate Reduced To Two Margins

If

```math
\mathrm{P22\text{-}BRANCHA\text{-}RPCOV\text{-}MARGIN}(\lambda_{11})
```

and

```math
\mathrm{P22\text{-}BRANCHA\text{-}RPF\text{-}MARGIN}(\lambda_{13})
```

hold with

```math
\lambda_{11}+\lambda_{13}<M_*,
```

then

```math
\mathrm{P22\text{-}BRANCHA\text{-}ADAPT\text{-}PREDEBIT}(\mu)
```

holds with

```math
\mu=M_*-\lambda_{11}-\lambda_{13}>0.
```

Proof.

By Definition 37.3,

```math
\mathcal L_N^{rc}
=
U_{11}^{RPCov,car,SEL2}(N)+U_{13}^{RPF,bd}(N).
```

The two margin sources bound this by
\(\lambda_{11}+\lambda_{13}=M_*-\mu\) cofinally.  This is precisely Definition
38.3's adaptive predebit gate. `square`

### Theorem 39.8: Branch-A Tasks 1--4 Final Verdict

The four requested Branch-A tasks are now completed.

1. The adaptive row is fixed by Definition 39.1.
2. The surface-log gate is reduced to the \(\xi'\)-log source and optional
   fixed minimal-area amplifier by Theorem 39.5.
3. The split is exact: pure finite-template geometry contributes \(O(1)\);
   the only unprinted surface growth is the same-record decoration/minimal
   collar term \(\Xi_N'\), plus any deliberate change of finite battery
   template.
4. The predebit gate is reduced to two disjoint margin sources by Theorem
   39.7: RP/Cov moving-row smallness and exact-entry `RPF` smallness.

Combining Theorems 38.4, 39.5, and 39.7, adaptive Branch A closes if there
exist \(n_0,\theta_\xi,\lambda_{11},\lambda_{13}\) such that

```math
\theta_\xi<{2\over3}(n_0+1),
\qquad
\lambda_{11}+\lambda_{13}<M_*,
```

and the four source gates

```math
\mathrm{P22\text{-}BRANCHA\text{-}XIPLOG}(\theta_\xi),
\quad
\mathrm{P22\text{-}BRANCHA\text{-}AREA}(n_0),
\quad
\mathrm{P22\text{-}BRANCHA\text{-}RPCOV\text{-}MARGIN}(\lambda_{11}),
\quad
\mathrm{P22\text{-}BRANCHA\text{-}RPF\text{-}MARGIN}(\lambda_{13})
```

hold on the same pushed-forward `SEL2` law.

The present corpus does not print the \(\xi'\)-log source or the two predebit
margin sources.  Thus Branch A is now genuinely complete: further progress
requires adding one of these explicit same-record source theorems, or else
leaving Branch A for Branch B. `square`

## 40. Branch B: Stronger Same-Record Surface Theorem Audit

Branch B is the surface-growth route left by the \(F_4\) falsification and by
the Branch-A source audit.  It keeps the same pushed-forward scalar ontology:
finite `SEL2` records, the same whole-process law, the same scalar readouts,
and the positive Paper-13/Paper-19 surface-polymer ledger.  It does not change
channel as Branch A does, and it does not introduce a signed or non-full-support
selector as Branch C would.

This section settles Branch B at the current-corpus level.  The verdict is
not an absolute mathematical no-go for every possible surface theorem.  It is
the exact source audit: the current papers do not contain the theorem Branch B
needs, and every hidden shortcut either has already been spent or belongs to a
different branch.

### Definition 40.1: Branch-B-Admissible Surface Replacement

A replacement theorem is Branch-B-admissible when it proves, on the same
strict reduced `SEL2` scalar law, a full-support positive surface-growth
constant

```math
G_B^{SEL2}
```

for the Paper-13/Paper-19 nonminimal sheet sum, with the following restrictions.

1. The same finite Creutz boundary and same pushed-forward scalar law are used.
2. Every reduced same-boundary surface counted by the strict Paper-13 support
   convention remains in support.
3. Orientation, sign, and character data may not be used for cancellation;
   they are scalar record data, not a license to delete supports.
4. No channel switch, large-\(N\) battery change, adaptive minimal-area
   amplifier, or prefactor-ratio argument is used.  Those are Branch-A moves.
5. No signed selector, non-full-support projection, or cancellation theorem is
   used.  Those are Branch-C moves.

Thus Branch B may improve only the positive full-support surface-growth
constant.  It may sharpen a connective-constant estimate, a decoration-growth
estimate, or an equivalent same-boundary finite-support enumeration, but it
must leave the underlying record law unchanged.

### Definition 40.2: The Current Branch-B Baseline

The best current same-record positive surface-growth baseline is the rooted
tree value from Paper 20 Definitions 4.3A.160BH.40N--4.3A.160BH.40S:

```math
G_{13,tree}^{SEL2}
=
1+\log 19
+
20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}.
```

This already incorporates the current improvements over the older
`3+log20` envelope:

```math
\Delta_{plaq}^{4D}=20,\qquad R_{loc}^{4D}=1,
```

unoriented reduced supports, no separate local-replacement multiplicity, and
subexponential component partitions.  Therefore Branch B cannot claim credit
for any of those reductions again.

For the \(F_4\) route falsified in Theorem 29.5, a Branch-B replacement would
have to lower the escape threshold below the actual same-record escape ceiling:

```math
1-\exp(-G_B^{SEL2})
<
\mathcal E_{F_4}^{cof,SEL2}.
```

Since Theorem 29.5 gives

```math
\mathcal E_{F_4}^{cof,SEL2}<0.76,
```

a necessary condition for an \(F_4\) Branch-B rescue is the conservative scalar
bound

```math
G_B^{SEL2}
<
-\log(1-0.76)
=
-\log(0.24)
=
1.427116\ldots.
```

By contrast, the current rooted-tree baseline satisfies

```math
G_{13,tree}^{SEL2}
\ge
1+\log19
=
3.944438\ldots.
```

So the existing baseline is not merely a little too weak for the strict
\(F_4\) branch; it is in the wrong scale.

### Lemma 40.3: The Already-Spent Surface Reductions Cannot Be Reused

Branch B cannot lower \(G_{13,tree}^{SEL2}\) by deleting orientation labels,
local replacement labels, component partitions, root placements, or finite
battery endpoint constants.

Proof.

Paper 19 closes the finite-degree surface entropy audit
`P19-T13-ESURF(3+log20)` by using the reduced support convention
\(\Delta_{plaq}^{4D}=20\) and \(R_{loc}^{4D}=1\).  Paper 20 then sharpens the
geometry part to the rooted tree-graph bound \(1+\log19\).  The proof
explicitly removes orientation/sign bookkeeping from support entropy, assigns
finite root placements and fixed boundary/collar choices to the surface
prefactor, and treats component partitions as subexponential.

Therefore none of these items remains as an exponential growth source that can
be newly subtracted.  Subtracting them again would double-spend the same
finite-record audit. `square`

### Lemma 40.4: The Old \(1/8\) Escape Source Cannot Be Saved By Branch B

If the only escape product available is the old coefficient-gap product

```math
P_{esc}^{old}\le {1\over8},
```

then no Branch-B-admissible full-support surface theorem can close the escape
gate.

Proof.

Theorem 23.5 proves that every full-support same-boundary surface route on the
strict reduced `SEL2` branch has

```math
G_B^{SEL2}\ge {1\over4}\log2>\log{8\over7}.
```

But a product \(P_{esc}^{old}\le1/8\) can pass only if

```math
1-\exp(-G_B^{SEL2})< {1\over8},
```

equivalently

```math
G_B^{SEL2}<\log{8\over7}.
```

This contradicts the full-support lower bound. `square`

### Lemma 40.5: The Heat-Kernel \(F_4\) Falsification Leaves Only A New Connective-Constant Theorem

For the strict \(F_4\) law of Theorem 29.5, Branch B can reopen the escape
gate only by proving a genuinely new full-support same-boundary surface
constant satisfying

```math
{1\over4}\log2
\le
G_B^{SEL2}
<
1.427116\ldots,
```

and, in fact, satisfying the sharper unrounded inequality

```math
G_B^{SEL2}
<
-\log\left(1-\mathcal E_{F_4}^{cof,SEL2}\right).
```

No theorem in Papers 19--22 prints such a constant.

Proof.

The lower bound is Theorem 23.4, because Branch B remains full-support.  The
upper requirement is Definition 40.2 and Theorem 29.5.  The current printed
positive constants are:

1. the old finite-degree envelope \(3+\log20\) from Paper 19;
2. the rooted tree-graph envelope \(1+\log19\) from Paper 20;
3. the decoration surcharge \(20\widehat\eta_{*,20}/(1-\widehat\eta_{*,20})\),
   which is nonnegative;
4. the full-support cube-bump lower bound \((\log2)/4\) from Section 23.

Items 1--3 are upper envelopes too large for the \(F_4\) heat-kernel tail, and
item 4 is only a lower bound.  None prints a full-support connective constant
below \(1.427116\ldots\). `square`

### Lemma 40.6: Normalized-Dimension And Signed Routes Are Not Branch B

The normalized surface fork of Paper 20 and any signed/selector cancellation
route do not close Branch B unless they are recast as a positive full-support
same-boundary theorem.

Proof.

Paper 20's `P20-SEL2-NORM-SURF` audit decides the dimension surcharge in the
coefficient normalization chain.  On the strict reduced branch it can remove a
dimension surcharge, but it does not by itself print a new positive
full-support connective constant for the same-boundary surface sum.  Its clean
conclusion is already reflected in the current coefficient/source ledger.

A signed or selector theorem changes the support or uses cancellation among
scalar weights.  That may be a legitimate future route, but Definition 40.1
excludes it from Branch B.  Such a move must be declared as Branch C and must
re-audit positivity, support, no-double-charge, and same-record compatibility
from the beginning. `square`

### Theorem 40.7: Branch B Is Settled For The Current Corpus

Branch B has the following final current-corpus status.

1. It cannot rescue the old \(1/8\) escape source, by Lemma 40.4.
2. It cannot rescue the strict \(F_4\) heat-kernel-like branch with the current
   rooted tree constant, because

   ```math
   1+\log19>1.427116\ldots.
   ```

3. It is not absolutely impossible: the cube-bump lower bound leaves a logical
   interval

   ```math
   {1\over4}\log2
   \le
   G_B^{SEL2}
   <
   -\log\left(1-\mathcal E_{F_4}^{cof,SEL2}\right)
   ```

   in which a future full-support connective-constant theorem could live.
4. The present papers do not prove such a theorem.  Therefore Branch B is a
   parked source theorem, not an available proof route.

Equivalently, the exact reopening gate is

```math
\mathrm{P22\text{-}BRANCHB\text{-}SURF\text{-}SHARP}
(G_B)
```

with all clauses of Definition 40.1 and with

```math
1-\exp(-G_B)
<
\mathcal E_{\rho}^{cof,SEL2}
```

for the declared same-record channel \(\rho\).  For the strict \(F_4\) channel,
Theorem 29.5 forces the necessary numerical target

```math
G_B<1.427116\ldots.
```

Until this explicit theorem is supplied, Branch B is closed as a current-corpus
audit with a negative verdict: it contributes no unconditional continuum
Yang-Mills confinement proof.

Proof.

Items 1--2 are Lemmas 40.4 and 40.5.  Item 3 records exactly the gap between
the full-support lower bound and the heat-kernel-tail necessary upper bound.
Item 4 follows from the source inventory in Lemma 40.5 and the branch
separation in Lemma 40.6.  The reopening gate is just Definition 40.1 plus the
escape-threshold algebra

```math
q_\rho\gamma_\rho>1-\exp(-G_B),
```

or its cofinal escape-ceiling form. `square`

### Corollary 40.8: What Comes After Branch B

The branch ledger is now sharp.

1. Branch A is complete as a source audit by Theorem 39.8.
2. Branch B is complete as a current-corpus source audit by Theorem 40.7.
3. The only remaining mainline alternatives are:

   ```math
   \mathrm{P22\text{-}BRANCHB\text{-}SURF\text{-}SHARP}(G_B)
   ```

   as a new positive full-support surface theorem, or Branch C: a declared
   signed/selector surface route with a full support and positivity re-audit.

The Barandes-aligned rule is unchanged: whichever route is chosen must be a
finite pushed-forward record theorem before any confinement inequality is
spent.  There is still no licensed place to insert a continuum Yang-Mills
measure, an area law, or an unrecorded dynamical subprocess.

## 41. Branch C: Signed Or Selector Surface Route Audit

Branch C is the last branch in the Section-30 ledger.  It is deliberately not
Branch B.  Branch B kept the positive full-support Paper-13/Paper-19 surface
sum and asked for a sharper full-support surface-growth theorem.  Branch C
changes the rule of the surface sum itself: either it introduces a declared
non-full-support selector, or it keeps signed surface weights and tries to use
cancellation before taking absolute values.

That move is allowed only if it is declared as a new finite record theorem.
It cannot be slipped into the old Paper-13 `SUB` gate, because that gate is an
absolute positive tail estimate.

### Definition 41.1: Branch-C Declaration

The declaration

```math
\mathrm{P22\text{-}BRANCHC\text{-}DECL}
```

consists of one of the following finite same-record objects, fixed before any
surface inequality is evaluated.

1. **Selector form.**  A finite scalar support selector

   ```math
   \mathfrak S_j(\Sigma)\in\{0,1\}
   ```

   on admissible block surfaces in the finite Creutz battery.

2. **Signed form.**  A signed scalar surface weight

   ```math
   \omega_j(\Sigma)\in\mathbb R
   ```

   or a finite central-record complex weight with a declared real extraction,
   evaluated on the same pushed-forward block law.

3. **Mixed form.**  A selector and signed weight together.

The declaration is admissible only if all of the following are also declared:

```math
\mathrm{P22\text{-}BRANCHC\text{-}EXACTID},
\qquad
\mathrm{P22\text{-}BRANCHC\text{-}NODEBIT},
\qquad
\mathrm{P22\text{-}BRANCHC\text{-}NOSMUGGLE}.
```

Here `EXACTID` means the selected/signed expansion is exactly the same finite
Creutz/Wilson scalar record, or else that a new scalar anchor is explicitly
defined and transported.  `NODEBIT` means every term removed, signed, paired,
or regrouped is assigned to exactly one ledger.  `NOSMUGGLE` means the
selector or sign rule is not chosen using an area law, string tension, mass
gap, confinement, or continuum Yang-Mills existence conclusion.

### Lemma 41.2: Paper-13 `SUB` Is Not A Signed Theorem

The Paper-13/Paper-19 surface-polymer entry route cannot be reused unchanged
after a Branch-C declaration.

Proof.

Paper 13 Definition 7.30L estimates the nonminimal tail by

```math
|T_{a,s_0}(C)|
\le
A_Ce^{\xi'_C}u_{\rho,s_0}^{N(C)}
\sum_{q\ge1}(B_Cu_{\rho,s_0})^q
```

in the equivalent geometric-series form.  Its inputs are absolute
convergence, the KP bound

```math
\sup_x\sum_{\Gamma\ni x}|\psi_{a,\Sigma}(\Gamma)|e^{m|\Gamma|}\le\kappa,
```

the absolute decoration estimate

```math
|Z_{a,s_0}(\Sigma)|\le e^{\xi'_C}D_C^q,
```

and the positive support count

```math
\#\{\Sigma:\partial\Sigma=C,\ |\Sigma|-N(C)=q\}
\le A_CE_C^q.
```

Paper 19 imports the same structure as `P19-T13-ESURF`,
`P19-T13-DEC`, and `P19-T13-LEAD`.  None of these clauses estimates a signed
sum after cancellations.  They dominate the absolute value of every
nonminimal contribution.  Therefore a Branch-C cancellation or support-deletion
claim requires a new exact signed/selector theorem.  It cannot be obtained by
renaming the existing positive `SUB` ledger. `square`

### Definition 41.3: Branch-C Effective Surface Gate

After `P22-BRANCHC-DECL`, the replacement surface theorem is

```math
\mathrm{P22\text{-}BRANCHC\text{-}EFFSURF}
(G_C,M_C)
```

and means that, for every loop \(C\) in the declared finite Creutz battery,
the nonminimal selected/signed tail satisfies the same-record bound

```math
\left|
\sum_{\Sigma\ne\Sigma_C:\partial\Sigma=C}
\mathfrak S_j(\Sigma)\omega_j(\Sigma)
u_{\rho,j}^{|\Sigma|}
Z_j(\Sigma)
\right|
\le
M_C\,u_{\rho,j}^{N(C)}
\sum_{q\ge1}\exp(qG_C)u_{\rho,j}^{q},
```

or any algebraically equivalent finite-battery bound that leads to the
subcritical ratio

```math
u_{\rho,j}\exp(G_C)<1
```

with the same \(G_C\) and finite \(M_C\) cofinally.

This is the exact replacement for the Paper-13 positive gate
`SUB(s_0,rho,L)`.  It is not a separate escape theorem and not a continuum
measure assumption.

The anchor pass gate

```math
\mathrm{P22\text{-}BRANCHC\text{-}ANCHORPASS}
```

means that, after the Branch-C exact identity or new-anchor declaration, the
resulting finite scalar anchor has a positive margin and its transport ledger
loses less than that margin on the same pushed-forward record law.  If the
original Creutz anchor is preserved, this is the old Paper-13/Paper-19 anchor
pass with the new `EFFSURF` theorem substituted for `SUB`.  If a new anchor is
declared, this is a fresh positivity and transport theorem for that new anchor.

### Lemma 41.4: Branch C Must Preserve The Original Anchor Or Declare A New One

If the selector form has \(\mathfrak S_j(\Sigma)=0\) for some admissible
surface whose contribution to the original Wilson/Creutz scalar record is not
proved to vanish or cancel, then Branch C no longer computes the old
Paper-13/Paper-19 Creutz anchor.

Consequently the route can continue only if it proves either
`P22-BRANCHC-EXACTID` for the original anchor, or a new anchor theorem

```math
\mathrm{P22\text{-}BRANCHC\text{-}NEWANCHOR}
```

with its own positivity, transport, and scalar extraction ledgers.

Proof.

Paper 13 Theorem 7.30M starts from the exact identity

```math
\mu_{a,s_0}(W_\rho(C))
=
\sum_{\Sigma:\partial\Sigma=C}
u_{\rho,s_0}^{|\Sigma|}Z_{a,s_0}(\Sigma).
```

Deleting a support term changes the right-hand side unless an exact
same-record identity proves that the deleted terms have zero net contribution
or are represented elsewhere.  If the right-hand side changes, the proof no
longer concerns the same loop record \(W_\rho(C)\).  A different record may
still be useful, but it must be declared and transported as a new scalar
anchor. `square`

### Lemma 41.5: Fixed \(F_4\) Scalar Selectors Are Heat-Kernel Limited

On the strict \(F_4\) branch, any Branch-C selector whose claimed escape
source is a fixed continuous function of \(X_4\), or a finite uniform limit of
such fixed functions, is bounded by the heat-kernel comparison of Section 29.

In particular, it cannot prove

```math
\mathcal E_{F_4}^{cof,SEL2}>\Theta_4^{act}
```

and it cannot rescue the \(F_4\) branch unless the effective surface theorem
also lowers the required threshold below the heat-kernel ceiling.

Proof.

Lemma 29.2 proves that every fixed continuous \(f(X_4)\) has the same cofinal
value as the active heat-kernel reference.  Lemma 29.4 then bounds every fixed
threshold tail by the heat-kernel tail ceiling, and Theorem 29.5 gives

```math
\mathcal E_{F_4}^{cof,SEL2}<\Theta_4^{min}\le\Theta_4^{act}.
```

Finite uniform limits preserve the comparison because the approximation error
is uniform on the compact interval \([0,2]\).  Therefore fixed \(X_4\)-scalar
selectors cannot create the near-maximal \(F_4\) escape mass that Theorem 29.5
has already falsified.  A Branch-C route must instead lower the effective
surface threshold or leave the \(F_4\) channel. `square`

### Lemma 41.6: Existing Signed Cancellations Do Not Supply Branch C

The signed cancellations already proved or reduced in Paper 20 are local
coefficient-source cancellations.  They do not constitute
`P22-BRANCHC-EFFSURF`.

Proof.

Paper 20's signed work around `P20-SEL2-INTBULK-FOC`,
`GENMATCH`, perimeter/cusp residuals, and the local Schwinger-Dyson root
census concerns the scalar coefficient comparison and local bulk/collar
source terms.  Those estimates decide whether the block plaquette coefficient
or comparison defect has a zero or finite debit on the same pushed-forward
record.

Branch C needs a different theorem: a signed or selected nonminimal
same-boundary surface tail estimate for the Paper-13 surface sum.  A local
coefficient-source cancellation does not bound the global signed surface
tail, does not identify the selected surface expansion with the original
Creutz record, and does not replace the positive `SUB` gate. `square`

### Theorem 41.7: Branch C Current-Corpus Verdict

Branch C is settled at the current-corpus level as follows.

1. The old Paper-13/Paper-19 positive surface-polymer theorem cannot be reused
   after changing support or using signed cancellation.
2. A non-full-support selector is admissible only with an exact same-record
   identity for the original anchor, or with a newly declared scalar anchor and
   a full transport/positivity ledger.
3. A signed surface route is admissible only with a new same-record signed-tail
   theorem `P22-BRANCHC-EFFSURF(G_C,M_C)`.
4. Fixed \(F_4\) scalar selectors are heat-kernel limited by Theorem 29.5 and
   cannot by themselves restore `ESC-MASS(F_4)`.
5. No theorem in Papers 13, 19, 20, 21, or the current Paper 22 supplies the
   full package

   ```math
   \mathrm{P22\text{-}BRANCHC\text{-}DECL}
   +\mathrm{P22\text{-}BRANCHC\text{-}EXACTID}
   +\mathrm{P22\text{-}BRANCHC\text{-}EFFSURF}(G_C,M_C)
   +\mathrm{P22\text{-}BRANCHC\text{-}ANCHORPASS}.
   ```

Therefore Branch C is not an available proof route in the current corpus.  It
is parked behind the displayed finite same-record package.

Proof.

Item 1 is Lemma 41.2.  Item 2 is Lemma 41.4.  Item 3 is Definition 41.3.
Item 4 is Lemma 41.5.  Item 5 follows from the source audit: Paper 13 gives an
absolute positive surface-polymer theorem in the strong-block domain; Paper 19
imports its positive ledgers; Paper 20 supplies local signed coefficient
cancellations and no-smuggling rules; Paper 21 and Sections 21--29 of this
paper falsify the fixed \(F_4\) heat-kernel-like escape route.  None prints a
signed or selected surface-tail theorem with exact anchor preservation.
`square`

### Corollary 41.8: Final Branch Ledger After A--C

The three branches opened after the \(F_4\) falsification now have exact
current-corpus statuses.

1. **Branch A:** complete as a source audit.  It closes only under the fixed
   `P22-BRANCHA-4096-PREFCAP` gate or the adaptive
   `XIPLOG/AREA/RPCOV/RPF` margin package of Theorem 39.8.
2. **Branch B:** complete as a source audit with a negative current-corpus
   verdict.  It reopens only through a positive full-support theorem
   `P22-BRANCHB-SURF-SHARP(G_B)`.
3. **Branch C:** complete as an admissibility/source audit with a negative
   current-corpus verdict.  It reopens only through the signed/selector package
   of Theorem 41.7.

Thus Paper 22 should not claim unconditional continuum Yang-Mills confinement.
The honest next mathematical work is no longer to choose among vague branches;
it is to prove one explicit source theorem:

```math
\mathrm{P22\text{-}BRANCHA\text{-}4096\text{-}PREFCAP},
\quad
\mathrm{P22\text{-}BRANCHA\text{-}ADAPT\text{-}SOURCE},
\quad
\mathrm{P22\text{-}BRANCHB\text{-}SURF\text{-}SHARP},
\quad
\text{or}\quad
\mathrm{P22\text{-}BRANCHC\text{-}SIGNED\text{-}SELECTOR\text{-}PACKAGE}.
```

Every option remains Barandes-aligned only if it is proved as a finite
pushed-forward record theorem before the final confinement inequality is
evaluated.

## 42. Handoff To Paper 23

Paper 22 stops here.  Its result is not an unconditional continuum
Yang-Mills confinement proof.  Its result is sharper and narrower:

1. the strict \(F_4\) branch is falsified at `ESC-MASS`;
2. Branch A is reduced to explicit fixed or adaptive prefactor/source gates;
3. Branch B is parked behind a new positive full-support surface theorem;
4. Branch C is parked behind a new signed/selector exact-anchor package.

The next paper should therefore not be a synthesis paper.  It should be the
active source campaign for the most concrete surviving route:

```math
\text{adaptive Branch A}.
```

The Paper-23 target is the adaptive package isolated in Theorem 39.8:

```math
\mathrm{P22\text{-}BRANCHA\text{-}XIPLOG}(\theta_\xi),
\quad
\mathrm{P22\text{-}BRANCHA\text{-}AREA}(n_0),
\quad
\mathrm{P22\text{-}BRANCHA\text{-}RPCOV\text{-}MARGIN}(\lambda_{11}),
\quad
\mathrm{P22\text{-}BRANCHA\text{-}RPF\text{-}MARGIN}(\lambda_{13}),
```

with

```math
\theta_\xi<{2\over3}(n_0+1),
\qquad
\lambda_{11}+\lambda_{13}<M_*.
```

Paper 23 should begin by freezing the same high-\(\alpha\), large-\(N\),
same-record branch and then attacking the two live source families:

1. the decoration/minimal-collar logarithmic growth source
   `XIPLOG(theta_xi)`, plus any deliberate area amplifier;
2. the disjoint carried-predebit margins for RP/Cov and exact-entry `RPF`.

No Branch-B or Branch-C theorem should be spent inside Paper 23 unless it is
explicitly declared as a branch change.
