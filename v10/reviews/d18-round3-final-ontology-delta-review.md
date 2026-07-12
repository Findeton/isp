# D18 round-3 final ontology delta review

**Date:** 2026-07-12  
**Referee stream:** final operational-core/minimality scope audit  
**Candidate:** `FINITE-DECOHERENCE-FUNCTIONAL-SUFFICIENCY`  
**Verdict:** **PASS AT THE FINITE/CYLINDER OPERATIONAL SCOPE**

## Decision

The two requested ontology corrections are present and correct.

First, the executable docstring now agrees with the repaired theorem and
semantic packet.  At operational probability level, the supplied inputs are
the typed event algebra `E` and normalized strongly-positive decoherence
functional `D`.  Record semantics and units are explicitly placed in the
interpretation layer, while the action/state/measure/instrument packet is a
physical explanatory generator.

Second, the theorem now states that even the literal pair `(E,D)` has not been
proved minimal modulo every operational equivalence.  It gives the right
reason: two matrices can differ by representation data invisible to the
currently licensed Boolean-event quantum measures and decoherent-partition
probabilities, while a richer phase-sensitive composition could distinguish
them.  Therefore D18 proves sufficiency, not uniqueness or literal minimality
of the representation.

All prior ontology ceilings remain intact:

- primitive `D` supplies the whole-history law by stipulation rather than
  deriving it from sealed records;
- durable-record meaning and the future algebra live outside the bare
  operational core;
- locality, regional sewing and construction-order independence are generator
  properties, not consequences of strong positivity;
- a whole-history law need not use a physical global commit clock, but bounded
  local computability and foliation independence remain unproved;
- profinite completion hosts compatible cylinder shadows but does not select
  `D` or guarantee a full quantum sigma extension; and
- no unique law of nature, geometry, scale, `G` or V9 holdout is claimed.

No new blocker was introduced by the delta.  The finite operational
sufficiency subresult can close.  The larger physical-generator and empirical-
selection investigation remains open exactly as stated.

## Reproduction

I copied D13, D14, D16, both D17 executables and the revised D18 executable to
a clean `/tmp` tree.  Normal and optimized Python both pass `30/30`, produce
identical stdout hashes, and regenerate a packet byte-identical to the primary
packet.

```text
checks                    30/30 normal and -O
source SHA-256             010c68757d259badab81667f1ff04c549e87aa32448027d884679ad864bc61b4
packet SHA-256             fb0e70c1d2701c69dd17b20b9b40237de756e6393289b63dfbe9e3db93c3cf3a
semantic SHA-256           e92b39b7308e6e51887ef073430e86608e96de863874fcf46b217f1d5d5dc779
normal/-O stdout SHA-256   8010279a8bc98f18ce5e5457d409d553b9c7874763797c8ce982b2f8adb1b1b6
D17 integrated dependency  5fffa4d676da38a64e61cdd3b01c031d6fa74d2e1119f72c35369ad7be40be57
```

The receipt matches every regenerated value.  The semantic hash remains
unchanged because the scientific result and ceiling are unchanged; the source,
packet and stdout hashes correctly changed with the docstring revision.

## Delta ledger

```text
D1 PASS  Docstring operational core is now exactly typed event algebra plus D.
D2 PASS  Record semantics and units are interpretation, not extra probability
         inputs once D is supplied.
D3 PASS  Action/state/measure/instrument data remain the explanatory generator.
D4 PASS  `(E,D)` is called sufficient, not proved minimal modulo all
         operational equivalences.
D5 PASS  Primitive D is still described as stipulating rather than deriving
         the whole-history law.
D6 PASS  Durable-record semantics remain explicitly external to bare `(E,D)`.
D7 PASS  Local sewing/global-correlation distinction and bounded-memory ceiling
         remain explicit.
D8 PASS  Profinite/cylinder versus quantum sigma-extension ceiling remains.
D9 PASS  `MINIMAL-COMPLETE-CONDITIONAL-RULEBOOK` remains unearned.
D10 PASS `UNIQUE-FUNDAMENTAL-RULEBOOK-SELECTED` and nature-law claims remain
         explicitly rejected.
```

## 1. Corrected executable ontology

The old docstring described record/coarse maps and a unit dictionary as if
they were mathematical inputs needed to answer every operational probability
question.  That conflicted with both the source's semantic packet and the
repaired theorem.

The new wording is exact:

```text
operational input      typed event algebra + normalized strongly-positive D
supplied question      a decoherent event/partition argument
interpretation         record meaning and units
physical explanation  local action/state/measure/instrument generator
```

This does not make queries or interpretation physically unimportant.  It says
only that after a question is typed and `D` is supplied, they are not
additional numerical probability factors.  The distinction prevents a second
Born/click lottery from being inserted and prevents units from being counted
as inputs to dimensionless odds.

The file and protocol titles still contain “minimal history rulebook,” but the
load-bearing executable verdict is
`FINITE-DECOHERENCE-FUNCTIONAL-SUFFICIENCY`, and the JSON ceiling says the
generator, interpretation and sigma extension remain supplied.  No scientific
minimality claim depends on the historical filename.

## 2. Sufficiency does not imply minimal representation

The new theorem paragraph correctly separates two questions:

```text
Does supplied `(E,D)` determine licensed probabilities?       yes
Is literal matrix D the unique smallest operational object?   not proved
```

For subset events, the quantum measure is

```math
\mu(A)=D(A,A)=\sum_{i,j\in A}D_{ij}.
```

Hermitian imaginary antisymmetric off-diagonal contributions cancel in this
sum.  They can therefore be invisible to all subset quantum measures and to
the licensed decoherent classical probabilities on a frozen event algebra,
even when the underlying matrices differ.  Whether they are physically
redundant depends on the declared operational equivalence: composition with a
phase-sensitive system can make such data observable.

This is the right ontology.  D18 has not proved a quotient theorem identifying
all operationally equivalent functionals, nor a universal composition class
that separates them.  It therefore withholds literal uniqueness/minimality
instead of choosing one equivalence notion silently.

The correction strengthens rather than weakens the accepted subresult.
Sufficiency is invariant under the possibility that a representation contains
redundant data; minimality is not.

## 3. Primitive `D` ceiling remains

The theorem continues to say:

> specifying a primitive `D`/whole-history law solves the next-click problem
> by stipulation rather than deriving it from sealed records.

This is the central ontological caveat.  A single symbol `D` may encode the
entire global interference and correlation structure.  It is concise notation,
not automatically a concise physical law, local algorithm or empirical
selection principle.

The generator packet remains richer because it explains how a particular
functional might arise from a history domain, fields, reference measure,
action, boundary state and record instruments.  D18's state and envelope
interventions continue to show that the action alone does not select `D`.
The sign-moving example remains representation gauge rather than physical
nonselection.

No wording in the revised delta says that the actual `D` of nature has been
found.  The accepted result is conditional:

> once a finite `D` is supplied, its licensed conditional record shadows are
> fixed without a second probability law.

## 4. Records and locality ceilings remain

The repaired interpretation layer still identifies:

- which event variables are physical records;
- which future algebra protects those records; and
- how dimensionless answers acquire operational units.

Bare `(E,D)` does not create or durably seal a record.  The finite
interferometer's orthogonal path factor models decoherence, while the D17
dependency supplies the explicit owner/seal/collar durability construction.
Those physical meanings are not inferred from matrix positivity.

Likewise the theorem retains the correct local/global distinction.  A local
generator may sew regional amplitudes on owned boundaries, while a boundary
state and final functional contain global correlations.  A global correlation
object is not a global update machine, but neither does its existence prove
bounded-collar computability, no-signalling, or construction-filtration
independence.

D18 still does not promote its finite source into a universal local generator.
The exact result remains an operational history-law theorem.

## 5. Profinite and nature-law ceilings remain

The profinite section is unchanged and correctly restricted:

```text
compatible classical record cylinders  may support inverse-limit extension
arbitrary quantum D                     needs a separate sigma theorem
profinite completion                    hosts, but does not select, the law
```

The final section also remains explicit that field content, coefficients,
cosmological state, ultraviolet measure/contour, record emergence, scale and
`G` are open.  Neither `MINIMAL-COMPLETE-CONDITIONAL-RULEBOOK` nor
`UNIQUE-FUNDAMENTAL-RULEBOOK-SELECTED` is awarded, and no V9 geometry holdout
opens.

## Gate delta

```text
Q0  improved: docstring now matches the operational/generator split.
Q1  unchanged: finite sufficiency pieces pass; full physical generator remains
                outside the accepted subresult.
Q2  improved/honest: literal minimality modulo operational equivalence is now
                      explicitly unproved.
Q3  unchanged/open beyond supplied finite covariance scope.
Q4  unchanged/partial: local generation is generator structure, not primitive D.
Q5  unchanged/pass at finite Gram/coarse scope.
Q6  unchanged/partial: cylinder theorem only; sigma extension open.
Q7-Q10 unchanged recovery/selection ceilings.
Q11 ontology delta PASS for the candidate subresult.
```

## Final verdict

**PASS AT THE FINITE/CYLINDER OPERATIONAL SCOPE.**  The revised docstring and
new nonminimality paragraph make the ontology internally consistent:
`(E,D)` is sufficient to answer supplied finite decoherent questions, but it
is neither proved the unique minimal representation nor a locally derived law
of nature.

Primitive-law, durable-record, locality, construction-order, profinite/sigma,
empirical-selection and geometry ceilings all remain intact.  No further
ontology revision is required for `FINITE-DECOHERENCE-FUNCTIONAL-SUFFICIENCY`.
