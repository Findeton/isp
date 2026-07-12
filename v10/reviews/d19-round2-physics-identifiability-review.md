# D19 round-2 focused physical-identifiability review

**Date:** 2026-07-12  
**Referee stream:** final history-law/generator/holdout scope audit  
**Candidate:** `FINITE-HISTORY-LAW-EMPIRICAL-NONIDENTIFIABILITY`  
**Verdict:** **PASS AT THE FROZEN FINITE HISTORY-LAW SCOPE**

## Decision

Every requested round-1 scope repair is present.

The executable, semantic packet, receipt and theorem now call the exact result
`FINITE-HISTORY-LAW-EMPIRICAL-NONIDENTIFIABILITY`.  They no longer claim that
two physical generators have been constructed.  The theorem explicitly says
that `EMPIRICAL-GENERATOR-NONSELECTION` would require two complete inequivalent
local covariant generators whose images realize the survivor laws.

The `xyz` statistic is now called a **designed discriminator** chosen from the
same null direction used to construct the survivor family.  The future
conditional is explicitly called an equivalent exposure of that same
coordinate.  Neither is described as an untouched prediction or an empirical
measurement of our universe.

The effective-theory wording is also repaired.  Einstein-Hilbert gravity plus
the Standard Model is described as the leading extensively tested low-energy
baseline, with higher operators and extensions still allowed.  State, record
emergence, units, `G`, gauge contour and ultraviolet completion remain open or
measured inputs rather than derived consequences.

Finally, the theorem keeps all V9 cone and dimension data closed because no
surviving fundamental generator fixes a cross-candidate value independently
of fitted nuisance parameters.

The exact finite theorem can therefore close.  The broader D19 physical
generator-identification problem remains `INCOMPLETE-INVESTIGATION`, exactly
as stated.

## Reproduction

I copied the dependency-free revised D19 source to a clean `/tmp` tree and ran
normal and optimized Python.  Both pass `20/20`, produce identical stdout
hashes, and regenerate a packet byte-identical to the primary packet.

```text
checks                    20/20 normal and -O
source SHA-256             fdf804f29144513dcfe2398262213551e1c462c222118939d5587a5173331bdb
packet SHA-256             5a53f79470f22d9b517b440b7c6752b39719da01696f0e2cd56fecaa33a5dc68
semantic SHA-256           d188a40340eca1148a8c957d8139e411748aacc355531a87f20ef6fbd9866856
normal/-O stdout SHA-256   5d1f0f22ea566082279990e92a04e5483ef3acb64e11cbcc72d36ac9f311f3a8
```

The receipt reproduces exactly.  Explicit check-count and semantic-hash guards
survive `-O`.

## Repair ledger

```text
R1 PASS  Verdict renamed from generator nonselection to finite history-law
         empirical nonidentifiability.
R2 PASS  Source labels xyz a designed triple-correlation discriminator.
R3 PASS  Source labels the future conditional an equivalent view of the same
         invisible coordinate.
R4 PASS  Theorem says both cells are algebraically the same r coordinate.
R5 PASS  Neither discriminator is called an untouched nature prediction.
R6 PASS  Stronger generator verdict is explicitly withheld.
R7 PASS  Standard Model plus Einstein-Hilbert wording is narrowed to a leading
         tested low-energy baseline with allowed extensions.
R8 PASS  State, records, units and UV completion retain their separate scope.
R9 PASS  V9 geometry data remain unopened.
R10 PASS Broader D19 remains incomplete pending physical candidates, a full
         evidence ledger and a real untouched discriminator.
```

## 1. Exact theorem scope

The accepted theorem remains:

```text
history carrier       eight binary histories (x,y,z)
training map          1,x,y,z,xy,xz,yz
rank                  7
null direction        xyz/8
positive family       P_r=(1+rxyz)/8, -1<r<1
survivors             r=1/2 and r=1/3
```

The two laws agree on normalization and all one-record and two-record
marginals.  They differ on the omitted cubic coordinate.  The positive checks
at `r=-9/10,0,9/10` show that the invisible direction passes through the
interior of the normalized simplex.

This proves that the frozen low-order observation map is not injective on the
complete positive history-law class.  It does not assume statistical noise,
finite-sample approximation or a fitted asymptotic model.

The renamed verdict now matches the object actually constructed.  The semantic
scope says “eight classical complete histories; one/two-record training
evidence,” and the ceiling says it is not a census of physical ultraviolet
theories.

## 2. Designed discriminator discipline

The theorem and source now use the right three-way distinction:

```text
training coordinates     the seven displayed low-order characters
designed discriminator   xyz, chosen from the null direction
real untouched holdout   absent
```

Because the survivor family itself is parameterized by `r xyz`, the cubic
statistic cannot be independent of candidate invention.  It is nevertheless a
perfect exact answer to the mathematical question “which additional
observation would distinguish this training fiber?”

The future conditional contains no second independent information.  Within
this family,

```math
P(z=1\mid x=1,y=1)=\frac{1+r}{2}
                  =\frac{1+E[xyz]}{2}.
```

The repaired source check says precisely that the conditional exposes the
same invisible coordinate.  The theorem likewise says the two cells are
algebraically the same `r` coordinate.

One generic sentence says a higher-order holdout *can* select between survivors.
That is correct conditionally: a genuinely untouched higher-order measurement
could do so.  The dedicated holdout section makes clear that the displayed toy
cells are not such a measurement.

## 3. Generator verdict remains withheld

The theorem now explicitly distinguishes:

```text
finite law noninjectivity                  proved
two physical generators realize survivors not proved
generator nonselection                     withheld
```

No action, state, measure, record instrument, local sewing rule or unit
dictionary is attached to either `P_r`.  Consequently no locality/covariance
or physical-equivalence comparison is claimed for the pair.

This is the correct logical boundary.  Abstract law-space noninjectivity warns
that low-order evidence is insufficient unless the physical candidate class
is independently restricted.  It does not prove that every restricted
generator family has a null direction.

The broader result still requires a predeclared physical candidate census,
two inequivalent complete generators, a quantitative evidence map and a real
discriminator excluded from candidate invention and fitting.

## 4. Effective-theory wording and evidence scope

The repaired ledger says:

> Einstein-Hilbert plus the Standard Model is the leading extensively tested
> baseline at declared scope; allowed higher operators/extensions remain.

This no longer suggests that existing evidence identifies a maximal or unique
local covariant generator.  The adjacent rows preserve the essential
limitations:

- measured coefficients depend on scale conventions;
- infinitely many higher EFT coefficients are incompletely bounded;
- the ultraviolet completion and causal-order action remain open;
- the cosmological boundary state is constrained, not uniquely derived;
- the measure/contour is theory- and observable-dependent;
- finite D14/D17 records do not prove universal record emergence; and
- operational metres, seconds and `G` are calibrated rather than derived from
  dimensionless histories.

The ledger remains qualitative rather than a complete quantitative candidate/
dataset census.  The theorem now acknowledges that incompleteness, so it is a
ceiling rather than an overclaim.

## 5. V9 and nature-law ceiling

The holdout section expressly says:

```text
xyz/future cells         designed toy discriminators
empirical universe data  no
V9 cone/dimension access no
fundamental generator    not selected
```

No nature-law, emergent-dimension, cone, scale or gravity result is inferred.
The broader physical verdict remains incomplete until a fundamental candidate
class fixes an untouched cross-candidate prediction.

## Gate delta

```text
I0  still open for physical generators; sufficient for frozen toy law class.
I1  still open physically; law vectors are distinct at toy scope.
I2  PASS exact rank/null/interior theorem.
I3  qualitative ledger retained; full quantitative census open.
I4  PASS state remains separate from law/action coefficients.
I5  PASS/HONEST record semantics and universal emergence remain supplied/open.
I6  OPEN no local generator pair claimed.
I7  PASS/HONEST units and G remain calibrated inputs.
I8  REPAIRED no toy untouched-holdout claim; real holdout remains absent.
I9  PASS V9 geometry remains closed.
I10 focused physical scope review PASS for the renamed subresult.
```

## Final verdict

**PASS `FINITE-HISTORY-LAW-EMPIRICAL-NONIDENTIFIABILITY` at the frozen finite
scope.**  The exact rank/null theorem and positive survivors remain unchanged,
while the claim now matches the constructed object.

The cubic statistic and future conditional are correctly treated as one
designed discriminator, the EFT baseline wording is appropriately limited,
generator nonselection is withheld, and no V9 or nature-law claim is made.
The wider physical-identifiability investigation remains open.
