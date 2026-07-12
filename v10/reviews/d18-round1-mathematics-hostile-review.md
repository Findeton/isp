# D18 hostile round-1 mathematics review

**Date:** 2026-07-12  
**Verdict:** **MAJOR REVISION**

## Decision

The 27 exact checks reproduce, and the finite decoherence-functional algebra
is correct. Both functionals are Gram matrices, normalized by `D(Omega,Omega)=1`,
and their tested coarse grainings give the claimed deterministic, half-half,
and interference-sensitive laws. The imported causal tower is projective and
its conditionals follow by disintegration.

The proposed **minimal** packet is not established. At operational level, a
typed event algebra plus a normalized strongly-positive decoherence functional
already determines every licensed decoherent partition probability. A record
instrument is one physical generator of such a functional, not an additional
necessary operational input after `D` is supplied. Units are explicitly shown
unnecessary for record odds. Changing the question/coarse map changes which
observable is asked, but does not prove that a separate packet field is
mathematically irreducible.

The exact witness also combines two parallel examples—an interferometer `D`
and an imported causal tower—rather than deriving one projective tower from
the displayed `D`. Thus finite sufficiency of one integrated packet and
minimality by deletion remain open.

## Reproduction

```text
source    43b0273d2d3e13e7957a05d3358597edeba26371b45123708ccebbb74fdb8ecb
packet    ebd888d83d258809a3ae8daf23908a7d83ccf0af4f23ee5fc07e5b3874e236d7
receipt   18b91bb230458233bc183a947ef27d1f96b8d73fb0a9e2e61a19a8e6791f79b1
semantic  3f0df227b71779758eb24820bb3c5a99b446ff6c729aedf1e6fb0cd4a0683719
stdout    0471d3060a0c424d93589b09c6132c35190df393c9c6c202eb40d020dd247696
checks    27/27 normal and optimized
```

## Blocker ledger

```text
M1 MAJOR operational sufficiency and explanatory generation are conflated.
M2 MAJOR minimality of record maps, coarse maps and units is not proved.
M3 MAJOR the decoherence-functional example and projective tower are parallel,
         not one integrated packet.
M4 MODERATE strong positivity is sampled only on a real finite grid; the
            general Gram proof is stated but not frozen as a symbolic identity.
M5 MODERATE arbitrary coarse-graining closure is not tested/proved explicitly.
M6 MODERATE factorization example is representational gauge freedom, not
            physical nonuniqueness.
M7 MINOR the finite cylinder family is not a full sigma-algebra measure; the
         literature audit correctly warns of the extension obstruction.
```

## Positivity, normalization and coarse graining

`D_ij=<branch_i,branch_j>` is Hermitian and strongly positive for **all**
complex coefficient vectors because

```math
c^dagger D c = ||sum_i c_i branch_i||^2 >= 0.
```

The code checks this identity only for coefficients in the real grid
`{-1,0,1}^4`, plus one extra real vector. That grid is not itself a proof for
arbitrary complex coefficients. The Gram construction supplies the proof, so
the theorem is true; freeze the general matrix identity or state clearly that
the proof is analytic and the grid is regression coverage.

Normalization by summing every matrix entry is correct here: it is
`D(Omega,Omega)`. Fine-history diagonals alone sum to one as well, but do not
determine interference, as the exact comparison correctly shows.

`coarse` correctly sums all fine blocks. A coarse matrix of a strongly-positive
functional is `M D M^dagger`, hence strongly positive and additive for every
partition. The receipt tests output and path partitions only. Add the general
incidence-matrix proof and exhaust all finite partitions of the four histories
if the claim is arbitrary coarse-graining closure.

The rejection of nonzero off-diagonals before reading classical probabilities
is correct. It implements exact decoherence, not approximate operational
decoherence; retain that finite scope.

## Operational sufficiency versus generator packet

For a finite event algebra `E`, supplying `(E,D)` is sufficient to calculate

```text
quantum measures D(A,A);
decoherence of partitions;
probabilities of decoherent events;
conditionals on positive-probability cylinders.
```

The declared question is an element/partition of `E`, analogous to a function
argument, not necessarily an independent physical law field. If event labels
do not carry their operational meaning, then a semantic interpretation map is
needed—but its necessity must be stated at that level.

The record instrument is necessary for an **explanatory physical generator**
that produces durable records, but once its effect is already encoded in `D`,
it is not necessary for operational probability calculation. Likewise units
are necessary for dimensional reports, not for next-record odds; the code
explicitly proves this.

Therefore two different packets must be separated:

```text
operational probability core: typed event algebra + D;
physical generator/interpretation: domain, measure, action, state,
instrument, record semantics and units.
```

Neither should be called minimal by inheriting fields required only by the
other.

## Projectivity and conditional law

The imported D17 tower is genuinely projective, and the two displayed
conditionals equal one by ordinary disintegration. There is no second lottery.

But this tower is not derived from `d_un` or `d_rec`; it is imported from a
different causal-growth packet. D18 therefore proves two facts side by side,
not that one supplied `D` has those cylinder restrictions. To pass Q1/Q6,
construct `D_n` on the actual D17 cylinder algebras, verify restriction
compatibility, and derive `P_n` and the visible conditional from their
diagonals in the same object family.

No full sigma-algebra extension follows. The literature audit accurately cites
the known obstruction and must remain part of the ceiling.

## Factorization nonuniqueness

The two envelope/phase pairs have identical products. This proves that a
factorization of a fixed amplitude is nonunique until conventions are fixed.
It does **not** exhibit physically inequivalent actions or states, because all
operational amplitudes are identical. Treat it as representation/gauge
redundancy, not evidence that nature permits two different generators.

Physical necessity interventions must vary one equivalence-class field while
holding the others fixed and produce different observables. The state examples
do this more credibly; the “reference envelope” still needs a clean separation
from boundary state and orbit measure.

## Gate disposition

```text
Q0 PARTIAL; fields listed, operational/generator roles conflated.
Q1 PARTIAL; exact components exist but are not one integrated packet.
Q2 FAIL as a complete minimality proof.
Q3 inherited finite relabeling scope only.
Q4 inherited from D17, not newly integrated with D.
Q5 PASS for Gram positivity and tested exact partitions; general closure needs proof.
Q6 PARTIAL; imported projective tower, no D-based inverse-limit extension.
Q7-Q10 scope ledgers only; no new geometry selection.
Q11 OPEN; this review finds major repairs.
```

## Final verdict

**MAJOR REVISION.** The finite decoherence and conditional calculations are
sound, but `MINIMAL-COMPLETE-CONDITIONAL-RULEBOOK` is not yet proved. Separate
the operational core from the physical generator packet, integrate `D` with
the causal cylinder tower, and prove necessity only modulo derivability and
physical equivalence.
