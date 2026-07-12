# D19 round-1 hostile physical-identifiability review

**Date:** 2026-07-12  
**Referee stream:** physical identifiability, evidence and holdout discipline  
**Verdict:** **MAJOR REVISION — EXACT HISTORY-LAW NONIDENTIFIABILITY PASSES; GENERATOR/HOLDOUT VERDICT DOES NOT**

## Decision

The exact rank/null-space theorem is correct and important.  On the frozen
eight-history carrier, normalization plus every one-variable and two-variable
binary marginal leaves one positive interior direction unmeasured.  The two
displayed laws agree on all those training observables and differ in their
three-record correlation and associated future conditional.  Therefore low-
order record shadows do not identify a complete history law.

Two ontology/discipline problems block the advertised candidate verdict.

First, the executable constructs two probability laws `P_r`; it constructs no
physical generators

```text
G = (domain/fields, measure/contour, action, state, record dynamics, units).
```

The protocol's verdict `EMPIRICAL-GENERATOR-NONSELECTION` requires explicit
inequivalent positive generators agreeing on the frozen training evidence.
That antecedent is absent.  The theorem itself admits that it has not built two
Standard-Model-plus-gravity ultraviolet generators.  The exact subresult is
therefore **finite history-law nonidentifiability**, not yet physical-generator
nonselection.

Second, `xyz` is the null direction used to construct the survivor family

```math
P_r=(1+rxyz)/8.
```

It consequently informed candidate invention.  Evaluating `E[xyz]` is an
exact separating coordinate, but it is not an untouched predictive holdout
under protocol I8, which forbids use in candidate invention, architecture
choice or stopping.  The future conditional at `x=y=1` is algebraically the
same `r` direction, not an independent second holdout.  Calling either cell
“untouched” overstates the training/holdout discipline.

These defects do not weaken the noninjectivity proof.  They change what the
proof may be called and prevent it from satisfying the empirical prediction
gate.

The qualitative evidence ledger is mostly appropriately cautious about
state, records, units and ultraviolet completion.  It is not yet a complete
physical evidence census: it provides no frozen candidate list, dataset list,
likelihood, numerical cutoff/curvature domain or parameter-identifiability
map for Standard Model plus gravity.  “Einstein-Hilbert plus Standard Model
EFT is the maximal tested local covariant normal form” should be narrowed to a
leading low-energy baseline with constrained but nonzero allowed extensions.

The nature-law ceiling passes.  D19 explicitly says the toy cells are not
measurements of our universe, keeps all V9 geometry data closed, and leaves the
broader physical verdict `INCOMPLETE-INVESTIGATION`.

## Frozen reproduction

I copied the dependency-free D19 source to a clean `/tmp` tree and ran normal
and optimized Python.  Both pass `20/20`, have byte-identical stdout, and
regenerate a packet byte-identical to the primary packet.

```text
checks                    20/20 normal and -O
source SHA-256             9f2f9c7b8a9a27ed145fcc8e13524054db28c69251d70cc4fe173437ebf29bf6
packet SHA-256             f137019ca9cb7aaa8f98eb81c4ef887a29a851959b8a2918134d7a0fa7dd7507
semantic SHA-256           6e102423970bff5e8732c29cf7fcc8d8a51e5d04136e1cce62ac155bc9314df5
normal/-O stdout SHA-256   4504da4feb37e3556d6d3fd856894954b8a915cb53e184ea422c21082900e75f
```

The receipt is exact.  Check-count and semantic-hash guards survive `-O`.

## Finding ledger

```text
P1 PASS     The seven-row Walsh observation map has exact rank seven.
P2 PASS     xyz/8 is its nonzero one-dimensional null direction.
P3 PASS     r=1/2 and r=1/3 are strictly positive normalized inequivalent
            history laws with identical one/two-record marginals.
P4 PASS     Triple expectation and future conditional distinguish the laws.
P5 MAJOR    No pair of physical generators is constructed; the semantic and
            stdout `EMPIRICAL-GENERATOR-NONSELECTION` verdict exceeds the
            executable object.
P6 MAJOR    xyz was used to define the survivor family and therefore is a
            designed discriminator, not an untouched predictive holdout.
P7 MODERATE The triple moment and displayed future conditional are two
            functions of the same one-dimensional null coordinate, not two
            independent discriminators.
P8 MODERATE No pre-data physical candidate census or quantitative evidence map
            establishes I0/I3 for the Standard Model plus gravity.
P9 MODERATE The EFT ledger has no numerical energy/curvature scope and calls
            the baseline “maximal,” while higher operators and extensions are
            explicitly allowed and incompletely bounded.
P10 PASS    Boundary state, record emergence, unit calibration, G and UV
            completion are kept distinct and open.
P11 PASS    Gauge-equivalent factorization is distinguished from observational
            equivalence in the protocol.
P12 OPEN    Local sewing, covariance and construction-order independence are
            not tested for any physical survivor.
P13 PASS    No V9 holdout, geometry-emergence or nature-law selection claim is
            made.
```

## 1. Exact history-law theorem

Order the eight histories by `(x,y,z) in {-1,+1}^3`.  The training observables
are the seven Walsh characters

```text
1, x, y, z, xy, xz, yz.
```

They are mutually orthogonal on the uniform cube and span a seven-dimensional
subspace.  The omitted character `xyz` spans the orthogonal complement.
Hence the observation matrix has rank seven and exact kernel

```math
v(x,y,z)=xyz/8.
```

The family

```math
P_r(x,y,z)=\frac{1+rxyz}{8}
```

is normalized because the `xyz` character sums to zero.  It is strictly
positive for `-1<r<1`.  Every one- and two-variable marginal is uniform,
because summing over any missing bit cancels the cubic term.

For the chosen survivors,

```text
r=1/2:  E[xyz]=1/2
r=1/3:  E[xyz]=1/3.
```

Conditioning on `x=y=1` gives

```math
P_r(z=1\mid x=1,y=1)=\frac{1+r}{2},
```

hence `3/4` versus `2/3`.  Both current-`y` processes are visibly non-Markov
because changing the earlier `x` changes the next-`z` conditional.

The source also checks positive laws at `r=-9/10,0,9/10`, establishing that the
null direction passes through the interior rather than touching positivity at
a single boundary point.

This proves:

> The specified low-order observation map is not injective on the full
> positive history-law simplex.

It does not require random sampling, asymptotic statistics or numerical
tolerance.  The conclusion is an exact identifiability theorem.

## 2. Why it is not yet generator nonselection

A history law and a physical generator are different levels of description:

```text
physical generator G  ->  history functional/law D_G  ->  observed shadows.
```

Noninjectivity of the second arrow on all abstract history laws does not prove
noninjectivity of the composite map on a restricted physical candidate class.
It may be that a justified candidate family intersects each training fiber in
only one physical equivalence class.  Conversely, many generators can map to
the same complete history law.

D19 builds only the middle objects `P_(1/2)` and `P_(1/3)`.  It supplies none
of the following for either survivor:

- causal domain or field content;
- local action and coefficients;
- gauge/groupoid measure or contour;
- boundary/cosmological state;
- durable record instrument;
- regional sewing or construction-order covariance; or
- operational scale dictionary.

The source itself calls the objects “whole-history laws,” and its semantic
scope says “eight classical complete histories.”  Those labels are accurate.
The verdict `EMPIRICAL-GENERATOR-NONSELECTION` is not.

The smallest repair is to rename the exact candidate subresult, for example:

```text
FINITE-HISTORY-LAW-NONIDENTIFIABILITY
```

or

```text
LOW-ORDER-SHADOW-NONSELECTION.
```

To earn the protocol verdict, D19 must exhibit two inequivalent complete
generators in a predeclared physical class, show that each maps to the same
training vector, and demonstrate a legal untouched physical discriminator.

The current theorem appropriately says independent evidence can identify a
restricted family when the observation map is injective on that family.  That
qualification is exactly why abstract-simplex noninjectivity cannot be
promoted to universal generator nonselection.

## 3. Training versus discriminator versus holdout

There are three different roles:

```text
training coordinates       used to fit or eliminate candidates
designed discriminator     chosen after analyzing surviving null directions
untouched predictive test  not used in candidate invention, fitting,
                           architecture choice or stopping
```

The seven Walsh rows are clearly identified as training coordinates.  The
problem is the word “untouched” for `xyz`.

The survivor family is parameterized precisely by the `xyz` direction.  The
two values `r=1/2` and `r=1/3` are chosen on that direction.  Reading
`E[xyz]=r` therefore reveals the coordinate used to construct the candidate
pair.  It is an ideal exact discriminator, but it was not withheld from model
invention.

The future conditional is not independent evidence.  In this family,

```math
P(z=1\mid x=y=1)=(1+E[xyz])/2.
```

It is an operationally useful restatement of the same cubic coordinate.

The frozen protocol predates the executable outcome, which prevents arithmetic
tampering with the stated gate.  It does not visibly preregister the exact
eight-history candidate class, the seven-character training matrix, the two
values of `r`, and an untouched `xyz` measurement before those candidates were
invented.  More importantly, even such preregistration would make this a
synthetic theorem demonstration, not a prediction about nature.

Required wording:

> The cubic statistic and future conditional are exact withheld coordinates
> relative to the displayed training map, selected to demonstrate the null
> direction.  They are not untouched empirical holdouts.

This wording preserves the theorem and obeys I8.

For a true holdout, candidates and their numerical predictions must be frozen
without using the held-out observation, then evaluated on a dataset excluded
from candidate invention, parameter fitting, architecture selection and the
decision to stop.

## 4. Effective Standard Model plus gravity evidence ledger

The ledger gets the main ontology right:

- low-energy field content and local action are empirically successful inputs,
  not derived from record combinatorics;
- masses, mixings, couplings, `G` and `Lambda` are measured/fitted;
- higher effective operators remain incompletely bounded;
- the ultraviolet completion and causal-order action are open;
- the cosmological state is constrained but not uniquely derived;
- the quantum-gravity measure/contour is open; and
- record emergence and the unit dictionary remain separate.

That matches the broad evidence picture.  The Particle Data Group continues
to catalogue Standard Model parameters alongside neutrino masses/mixing and
physics beyond the minimal model.  Experimental reviews report extensive
support for GR while continuing to constrain alternatives.  Gravity's EFT
treatment explicitly separates known low-energy effects from unknown
high-energy contributions, and cosmological parameter constraints are
model- and likelihood-dependent.

The present table is not yet the “complete evidence ledger” required by the
broader D19 verdict.  It contains no:

- enumerated datasets and dates;
- likelihood or covariance ownership;
- training/validation/holdout assignment;
- numerical energy, distance or curvature validity range;
- renormalization scale and scheme;
- parameter rank/profile analysis;
- candidate-by-candidate prediction table; or
- record of which data influenced architecture choice.

“Einstein-Hilbert plus Standard Model EFT is the maximal tested local covariant
normal form” is especially risky.  An EFT is an expansion containing every
operator allowed by the declared symmetries, with higher terms constrained at
different strengths.  The defensible phrase is:

> Einstein-Hilbert gravity plus the Standard Model is the leading extensively
> tested low-energy baseline; allowed higher operators and additional sectors
> remain bounded only within specified datasets and scales.

This avoids treating absence of detected deviations as identification of a
complete generator.

## 5. State, records, units and ultraviolet scope

These parts of the ledger pass the hostile ontology audit.

### Boundary/cosmological state

The theorem does not absorb initial conditions into action coefficients.
Cosmological data constrain parameters conditional on a cosmological model,
foreground treatment, priors and likelihood.  They do not uniquely derive a
cosmic wavefunctional or complete boundary state.

### Records and observational interface

D14/D17 give finite conditional mechanisms for owned sealed records.  D19
does not claim universal emergence of quasiclassical records.  The toy bits
`x,y,z` are supplied observable semantics, not dynamically derived detector
records.  Tomography of those variables cannot identify inaccessible phases
or cosmic histories outside the interface.

### Units and `G`

The metre/second dictionary and measured constants calibrate a low-energy
description.  The dimensionless eight-history law contains no operation that
derives metres, seconds or Newton's constant.  D19 correctly refuses to call
calibration emergence.

### Ultraviolet completion

Agreement on low-energy coefficients does not identify irrelevant operators,
new heavy fields, topology, contour, causal microstructure or boundary state.
The ledger explicitly keeps the D16 action family and D17 kernel nonselection
open.  This is the right ultraviolet ceiling.

## 6. Locality, covariance and equivalence scope

The toy `P_r` laws are global joint distributions.  They establish no regional
factorization, sewing, no-signalling or construction-order independence.
Different local, nonlocal and hidden-state mechanisms can realize the same
three-bit law.

The non-Markov conditional demonstrates dependence on earlier history.  It
does not show how the earlier information is carried locally.  D17 supplies a
separate finite boundary-memory example, but D19 does not attach either `P_r`
survivor to that generator.

Protocol I6 therefore remains open for the survivor class.  This is another
reason the objects cannot yet be called physical generators.

The source check that the laws are inequivalent means only that their ordered
probability vectors differ.  It does not execute the protocol's full quotient
over gauge, relabeling or field redefinitions.  For the obvious signed-bit and
coordinate permutations, `|r|` is invariant, so `1/2` and `1/3` cannot be
related by such a relabeling.  Physical equivalence still requires supplied
semantics for what `x,y,z` mean.

## 7. Nature-law and geometry claim audit

The final theorem paragraphs are commendably explicit:

```text
toy discriminator is not a measurement of our universe
no V9 cone/dimension data opened
no fundamental generator fixes a cross-candidate value
no physical UV generator pair constructed
broader D19 verdict remains incomplete
```

The protocol also says empirical nonselection would not imply that nature has
no exact law.  It would only identify insufficiency of the present evidence
relative to a declared candidate class.

Those ceilings pass.  The sole nature-facing overclaim is the candidate label
`EMPIRICAL-GENERATOR-NONSELECTION`, which sounds like the stronger physical
result explicitly disclaimed in the prose.  Renaming it removes the conflict.

## Gate disposition

```text
I0  FAIL/PARTIAL  no frozen physical generator census; toy class is explicit
                  only in the executable/theorem.
I1  PARTIAL       abstract law vectors differ; full physical equivalence
                  quotient is not implemented.
I2  PASS          exact rank, null direction, interior positivity and legal
                  mathematical discriminator.
I3  PARTIAL       qualitative EFT ledger, not complete quantitative evidence
                  inventory with declared scale.
I4  PASS          state is kept separate from action.
I5  PASS/PARTIAL  record interface is acknowledged as supplied; universal
                  record emergence is open.
I6  OPEN          no local/covariant generator for either survivor.
I7  PASS/HONEST   units and G are calibration inputs, not derived.
I8  FAIL as holdout; PASS as designed exact discriminator.
I9  PASS/HONEST   V9 cone/dimension/geometry data remain closed.
I10 OPEN          round-1 physical review completed; other independent streams
                  remain required for closure.
```

## Required repair

1. Rename the exact verdict to history-law nonidentifiability/nonselection.
2. Replace “untouched holdout” with “designed withheld coordinate” or
   “null-direction discriminator” in source labels and theorem prose.
3. State that the triple moment and displayed future conditional encode the
   same one-dimensional discriminator.
4. Narrow the Standard-Model-plus-gravity row to a leading low-energy baseline
   and add actual datasets, scales, schemes, fitted parameters and data-use
   roles before calling the evidence ledger complete.
5. To claim generator nonselection, freeze a physical candidate class and
   exhibit two inequivalent complete generators that pass the same training
   evidence, locality/covariance checks and unit/record semantics.
6. Only then freeze a real prediction and evaluate a dataset untouched by
   generator invention, fit, architecture choice and stopping.

## Final verdict

**MAJOR REVISION.**  Accept the exact theorem that low-order record marginals
need not identify a complete positive history law.  The rank-seven map,
one-dimensional null direction, positive survivor interval and separating
statistics reproduce exactly.

Do not award `EMPIRICAL-GENERATOR-NONSELECTION`: no physical generators are
built.  Do not call `xyz` or its conditional transform an untouched holdout:
that null direction defines the survivor family.  The effective-theory ledger
is a useful honest outline, but not yet a quantitative candidate/evidence
census.  The broader D19 result correctly remains `INCOMPLETE-INVESTIGATION`,
and no claim about nature or V9 geometry is earned.
