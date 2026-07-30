# v13 RQ0 — quantum factual-base amendment pin

**Status:** PIN, STRICT, 2026-07-30.  **Binding amendment to the clean-sheet
RQ0 pin committed at `76b9d4d3672862b43e7931087b00a49adbdf841c`.**
No replacement construction begins before this amendment is committed.

## 1. Correction and first-pass ceiling

A Boolean dependency process already contains a directed structure.  Reading
that structure back through interventions and recognizing a tailored diamond
would recover what the fixture planted.  Generic record witnesses attached
afterward would not make the substrate quantum.  The uncommitted diamond-tail
prototype is rejected and removed; it earns no result.

The binding rule is:

> **Construct the quantum factual base first.  Classical DAGs, diamonds and
> causal sets are held-out benchmarks only after a quantum-native causal
> instrument has been separately pinned and frozen.**

This pass may earn only:

1. `RQ0-REGIONS-CONSTRUCTED`;
2. `RQ0-REGIONAL-SITE`;
3. `RQ0-FACT-DESCENT`.

It may measure token automorphisms, but it may not claim
`RQ0-GROUPOID-ARENA`, `RQ0-CAUSAL-ARENA` or
`RQ0-CONFORMAL-ARENA`.  No causal order, spacetime region, metric, field or
gravity structure is constructed here.

## 2. Primitive quantum-region type

The primitive object is

$$
D=
\bigl[
X_D,\mathrm{Prep}_D,\mathrm{Amp}_D,U_D^{\mathrm{write}},
\mathrm{Pres}_D,\mathrm{Erase}_D,\mathrm{Ctrl}_D,\mathrm{Obs}_D
\bigr]/G_D.
$$

- $X_D$ is a finite local configuration carrier.
- $\mathrm{Prep}_D$ is the operationally admitted preparation scope and
  includes the actual $x_{D,0}$.
- $\mathrm{Amp}_D$ is a typed family of composable exact amplitude arrows.
- $U_D^{\mathrm{write}}$ is the declared record-writing arrow.
- $\mathrm{Pres}_D$, $\mathrm{Erase}_D$ and $\mathrm{Ctrl}_D$ are disjoint,
  typed families of operationally admissible continuations.
- $\mathrm{Obs}_D$ is a frozen family of accessible diagonal readouts
  $r:X_D\to V_r$.
- $G_D$ is the declared regional gauge.

$\mathcal R(D)$ is **not** primitive.  All record objects are derived after
the readout family is frozen.  A quantum region at this rung means an
operationally closed local amplitude-instrument family with declared
preparations, interventions and accessible readouts.  It is not yet a
spacetime region.

**Provisional postulate — operational nomological individuation.**  A region
is individuated by the composition laws accessible through
$\mathrm{Prep}_D$, the intervention families and $\mathrm{Obs}_D$, modulo
$G_D$; it is not individuated solely by the one history realized from
$x_{D,0}$.  Permanently inaccessible matrix structure does not distinguish
regions in this pass.  Every amplitude entry used by an isomorphism
discriminator must be reachable by an admitted preparation/control/readout
experiment or be quotiented out.

## 3. Derived, continuation-relative record structure

Candidate readouts are declared and hash-locked before H-corr/H-avail are
evaluated.  The executable may not search partitions for a passing answer.
For each frozen $r\in\mathrm{Obs}_D$,

$$
\mathrm{Occ}_D(r)
=H_{\mathrm{corr}}(U_D^{\mathrm{write}},r),
$$

and, for every continuation $V$,

$$
\mathrm{Avail}_D(r;V)=H_{\mathrm{avail}}(V,r).
$$

The derived algebras are

$$
\mathcal R_D^{\mathrm{hist}}
=\operatorname{Bool}\{r:\mathrm{Occ}_D(r)=1\},
$$

$$
\mathcal R_D(V)
=\operatorname{Bool}\{r:\mathrm{Occ}_D(r)=1,
\mathrm{Avail}_D(r;V)=1\},
$$

and

$$
\mathcal R_D^{\mathrm{pres}}
=\bigcap_{V\in\mathrm{Pres}_D}\mathcal R_D(V).
$$

Writing establishes historical occurrence; preserving continuations maintain
availability; erasure destroys availability without deleting occurrence.
This is the binding W6/Paper 2 distinction.

Required controls:

- removing the record-writing interaction makes H-corr fail;
- every declared preserving continuation passes H-avail;
- every declared eraser fails H-avail for the target readout;
- current and historical algebras are printed separately.

## 4. Gauge-typed regional identity

Raw matrices are presentations, not physical regions.  At minimum,

$$
G_D=
\text{configuration relabellings}
\times
\text{composition-compatible boundary gauge},
$$

with

$$
U:V_a\to V_b,qquad U\sim D_bUD_a^{-1}.
$$

The gauge acts on the complete composable instrument family with compensated
middle boundaries.  The executable must verify:

- configuration relabelling preserves Born shadows, composition defects,
  record status and derived algebras;
- outer boundary rephasings and compensated-cut rephasings are gauge;
- an uncompensated cut insertion that changes the accessible composite law is
  physical;
- loop/path invariants may discriminate physical amplitude instruments but
  never enter fact identity.

The isomorphism search ranges only over operationally accessible instrument
data and the declared gauge.  Three physical regions must be proven
non-isomorphic by an exhaustive finite search or an exact accessible
invariant, not by prose or filenames.

## 5. Two typed levels of classicality and recoherence

For a continuation $V$, define the exact cut-coherence entries

$$
\mathcal C^{ij}_{k\ell}(V,U_D^{\mathrm{write}})
=V_{ik}(U_D^{\mathrm{write}})_{kj}
\overline{V_{i\ell}(U_D^{\mathrm{write}})_{\ell j}}.
$$

For every $V\in\mathrm{Pres}_D$, the full W3 support test must verify the
division of labour:

- H-avail makes $\mathcal C$ block-diagonal by readout sector;
- H-corr kills the remaining within-sector off-diagonal entries;
- hence the full configuration-level
  $\Delta^B(V,U_D^{\mathrm{write}})$ vanishes whenever the exact W3
  hypotheses hold at that level.

For a deliberately coarse readout, the executable must instead construct the
actual record-level kernels and residual

$$
D_R(V)=\Gamma^R_{20}(V)
-\Gamma^R_{21}(V)\Gamma^R_{10},
$$

and type any classicality claim as $D_R(V)=0$ on that derived algebra.  It may
not call the configuration matrix “an operator on the algebra.”

For every targeted $V\in\mathrm{Erase}_D$:

- $\mathrm{Avail}_D(r;V)=0$;
- at least one cross-sector $\mathcal C^{ij}_{k\ell}$ is nonzero;
- at least one exact model has
  $\Delta^B(V,U_D^{\mathrm{write}})\ne0$.

The cross-sector coherence condition is primary: an accidentally vanishing
$\Delta^B$ from phase cancellation does not count as absence of coherence.

## 6. Certified shared fact and atlas descent

Equal alphabets, equal probabilities and isomorphic Boolean algebras do not
establish fact identity.  The main three-region atlas must use a W6-style
certificate.  This pass selects the **common-extension route**:

- construct one exact, operationally accessible, record-preserving amplitude
  extension carrying the three regional readouts;
- its joint record support must be exactly the diagonal value tuples permitted
  by the declared preparation scope, in the binary fixture
  $(0,0,0)$ and $(1,1,1)$;
- verify H-corr/H-avail for the extension readouts and derive the three
  regional restriction maps from it.

This certifies one shared fact without identifying the regional tokens as the
same occurrence.  The common-extension matrix and every support count are
constructed, not typed.

The atlas must include:

- three genuinely non-isomorphic quantum instruments;
- one nonvacuous coherent triple whose unique fact maps compose;
- a redundant-copy fixture with two event tokens for one certified fact;
- its exact $S_2$ token automorphism, with no representative selected;
- a twisted triple with valid pairwise token maps and nonidentity loop
  holonomy;
- fact descent remaining unique while token descent is groupoid-valued;
- phase data absent from every fact-map predicate.

## 7. Controls and refinement scope

The clean-sheet controls are retained with these exact readings:

- **C1:** relabelled/gauge-related instrument, all physical data invariant;
- **C2:** equal one-step Born shadows but different accessible composite laws,
  no false identification;
- **C3/C7:** one certified fact, redundant tokens, exact token automorphism;
- **C4:** historical occurrence survives coherent erasure while availability
  fails;
- **C5:** three non-isomorphic instruments and the common-extension coherent
  triple;
- **C6:** pairwise token maps exist but a chosen loop has nontrivial holonomy;
- **C8:** fact descent without a frozen quantum-native locality/influence
  instrument is classified `FACT-DESCENT-ONLY`;
- **C9:** geometry/coordinates/causal-order inputs are rejected at the schema
  boundary;
- **C10:** an exact instrument-family refinement/restriction preserves the
  derived record fact and its descent; any change to full amplitude data is
  printed rather than hidden;
- **C11:** field propagators/operators are absent and rejected.

No volume or conformal claim is made in this pass.  Refinement here is a typed
map of operational instrument families and record algebras, not yet a
spacetime-resolution limit.

## 8. Locality-first causal successor

The next obstruction is not yet an ordering relation.  It is the referent:

> What makes an intervention local to one subregion or interface?

The successor must be separately pinned as **RQ0-C1 — operational influence
between regional record algebras**.  It must first define localized
subinstruments.  Only then may it test

$$
A\rightsquigarrow B
$$

by comparing two interventions that differ only on the declared
$A$-subinstrument and asking whether the accessible stable-record law on $B$
changes.  Gauge invariance, shared-record screening, restriction, genuine
triple descent, cycle tests and refinement stability are mandatory.  The word
“later” is forbidden from the strict definition unless composition direction
is explicitly postulated and separately typed; process-composition order is
not yet relativistic causal order.

Only after that estimator is frozen may diamonds or causal sets be opened as
held-out scoring fixtures.

## 9. Exact implementation and files

The replacement construction may create only:

```text
v13/note-rq0-relativistic-arena.md
v13/code/rq0_quantum_regions_exact.py
v13/code/rq0_output.txt
v13/code/rq0_receipt.json
```

The adjudicator may append `v13/LOG.md` and update RUNBOOK's live pointer.
No causal-geometry script is authorized.  No v10–v12 file, old v13 result,
pin, amendment pin or v13 Paper 0 file may be edited.

The executable must use exact arithmetic only; reconstruct every amplitude
fixture in the new v13 code; lock the two pins and binding antecedents; print
all dimensions, preparation scopes, intervention families, readout hashes,
search scopes and legacy-use classes; declare no seeds/tolerances/numerical
geometry; run twice byte-identically; regenerate both committed receipts; and
make one deliberate anchor mutant exit 1 visibly.

If every gate passes, the highest claim is exactly:

$$
\boxed{\texttt{RQ0-FACT-DESCENT}.}
$$

The report must state that a gauge-typed atlas of three non-isomorphic finite
quantum regional instruments and their shared stable fact was constructed;
fact descent is set-valued, token descent may be groupoid-valued; erasing
continuations restore cross-sector coherence; and no causal, spacetime,
metric, field or gravity structure is claimed.  The unit then halts.
