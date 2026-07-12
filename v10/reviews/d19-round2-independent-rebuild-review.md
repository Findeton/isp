# D19 focused round-2 independent rebuild

**Referee:** independent clean-room/reproducibility stream  
**Date:** 2026-07-12  
**Verdict:** **PASS — `FINITE-HISTORY-LAW-EMPIRICAL-NONIDENTIFIABILITY`**  
**Generator-level verdict:** **OPEN / `INCOMPLETE-INVESTIGATION`**

Round two repairs the claim scope without changing the mathematical witness.
The executable now labels the result as finite history-law
nonidentifiability, and its two former “holdouts” are correctly described as a
designed triple discriminator and an equivalent conditional view of the same
null coordinate.  Normal and optimized execution reproduce 20/20 and every
new receipt hash.

A byte-level reconstruction proves that only four classes of text changed:
the two check labels, the semantic/verdict string, and the frozen semantic
digest implied by that verdict.  Reversing those substitutions reconstructs
the original round-one source hash exactly.  No rank, probability, marginal,
positivity, conditional or scaling code changed.

I found no remaining material generator or holdout overclaim.  The theorem and
receipt explicitly state that the executable does not realize two physical
generator packets, does not measure the toy discriminator in nature, and does
not open a V9 geometry dataset.

## 1. Reproduction and repaired hashes

The following were repeated:

```bash
python3 v10/code/d19_empirical_identifiability_exact.py
python3 -O v10/code/d19_empirical_identifiability_exact.py
python3 v10/code/d19_empirical_identifiability_exact.py | shasum -a 256
python3 -O v10/code/d19_empirical_identifiability_exact.py | shasum -a 256
shasum -a 256 v10/code/d19_empirical_identifiability_exact.py
shasum -a 256 v10/data/d19-empirical-identifiability-exact.json
```

Both modes end with:

```text
CHECKS PASSED: 20/20
SEMANTIC SHA256: d188a40340eca1148a8c957d8139e411748aacc355531a87f20ef6fbd9866856
SOURCE SHA256: fdf804f29144513dcfe2398262213551e1c462c222118939d5587a5173331bdb
VERDICT: FINITE-HISTORY-LAW-EMPIRICAL-NONIDENTIFIABILITY
```

Normal and `-O` stdout hashes are identical:

```text
5d1f0f22ea566082279990e92a04e5483ef3acb64e11cbcc72d36ac9f311f3a8
```

The packet hash matches the repaired receipt:

```text
5a53f79470f22d9b517b440b7c6752b39719da01696f0e2cd56fecaa33a5dc68
```

No Python `assert` or `__debug__` gate occurs.  Explicit checks, count guard
and semantic-hash guard survive `-O`; the packet is written afterward.

## 2. Exact source-delta proof

Starting from the repaired source, I reversed only:

1. `d188a4...` to the original semantic digest `6e1024...`;
2. “designed triple-correlation discriminator” to “untouched ... holdout”;
3. “equivalent future conditional ... same invisible coordinate” to the old
   second-holdout label; and
4. both occurrences of `FINITE-HISTORY-LAW-EMPIRICAL-NONIDENTIFIABILITY` to
   `EMPIRICAL-GENERATOR-NONSELECTION`.

The reconstructed source digest is:

```text
9f2f9c7b8a9a27ed145fcc8e13524054db28c69251d70cc4fe173437ebf29bf6
```

exactly the reviewed round-one source.  Therefore the entire executable
mathematical body is unchanged.

I applied the corresponding substitutions to current stdout, including the
old source and semantic hashes.  Its reconstructed digest is:

```text
4504da4feb37e3556d6d3fd856894954b8a915cb53e184ea422c21082900e75f
```

exactly the round-one stdout.  Every numerical PASS result and its order are
therefore unchanged.

## 3. Mathematical witness remains exact

The round-one clean-room results remain authoritative:

```text
A A^T                         = 8 I_7
rank(A)                       = 7
ker(A)                        = span{xyz/8}
P_r(x,y,z)                    = (1+r xyz)/8
strict positivity             = -1 < r < 1
all one-record marginals      = uniform 1/2
all two-record marginals      = uniform 1/4
E_r[xyz]                      = r
P_r(z=1|x,y)                  = (1+rxy)/2
P_1/2 - P_1/3                 = (1/6)(xyz/8)
```

Thus `r=1/2` and `r=1/3` agree on every frozen low-order training statistic
while differing as full laws.  At fixed `y=1`, their `x=1` next-record
conditionals are `3/4` and `2/3`; changing the earlier `x` changes the
conditional for each nonzero `r`, establishing the visible non-Markov cell.

No rank, normalization or parameter-scaling issue is introduced by the scope
repair.

## 4. Discriminator and holdout language

The source now calls check 12 a **designed triple-correlation discriminator**.
This is correct: `xyz` is the omitted Walsh character used to construct the
null direction and survivor family.  It was not selected independently after
the candidates were frozen.

Check 13 now says the future conditional exposes the **same invisible
coordinate**.  This is also exact because

```math
P_r(z=1|x=1,y=1)=(1+r)/2.
```

The triple expectation and conditional are algebraically equivalent views of
`r`, not independent holdouts.

The theorem's Holdout Discipline section is explicit that these are:

- designed from the null direction;
- not untouched predictions;
- not empirical measurements of our universe;
- insufficient to open any V9 cone or dimension dataset.

The earlier leakage/independence overclaim is therefore closed.

## 5. Generator claim audit

The repaired semantic verdict and receipt now describe exactly what the code
contains: two probability laws on eight complete classical histories and a
seven-row observation map.

The theorem explicitly says the result is **not**
`EMPIRICAL-GENERATOR-NONSELECTION`.  That stronger result would still require:

- two complete inequivalent local covariant generators;
- a frozen generator class and equivalence quotient;
- realization of both survivor laws as generator images;
- a complete evidence ledger; and
- a genuinely untouched discriminator.

None is silently inferred from the law-level rank theorem.  The broader D19
status remains `INCOMPLETE-INVESTIGATION`, which is correct.

The source filename and schema retain “empirical identifiability,” but neither
says “generator”; empirical nonidentifiability here means noninjectivity of the
specified observation map, not a claim about an actual universe dataset.  The
packet ceiling—“not a census of physical UV theories”—prevents that overread.

## 6. Remaining wording and evidence scope

One sentence in the theorem calls the null direction a “nonzero physical
direction.”  At the proved level it is more precisely an **operationally
distinct history-law direction**, because the designed discriminator separates
its points.  It is not yet a direction in the space of physical generator
packets.  The immediate next sentence and the later explicit ceiling make the
intended meaning clear, so this is minor wording rather than a blocker.

The inherited low-energy evidence ledger is also narrowed appropriately:
Einstein-Hilbert plus Standard Model is called the leading extensively tested
baseline, with higher operators and extensions allowed—not the maximal
possible action.  State, ultraviolet completion, contour, record emergence,
scale and `G` remain supplied, constrained or open.

## 7. Finding ledger

```text
R2-1 PASS  Repaired 20/20 normal/-O hashes reproduce exactly.
R2-2 PASS  Reversing only label/semantic substitutions reconstructs the
           complete round-one source and stdout hashes.
R2-3 PASS  Rank, kernel, P_r, marginals, positivity and conditionals are
           mathematically unchanged and exact.
R2-4 PASS  xyz and the conditional are correctly labeled designed/equivalent,
           not independent untouched holdouts.
R2-5 PASS  Semantic verdict is now history-law nonidentifiability; generator
           nonselection is explicitly withheld.
R2-6 MINOR Replace “physical direction” with “operational history-law
           direction” for perfect layer consistency.
```

## 8. Decision

**PASS `FINITE-HISTORY-LAW-EMPIRICAL-NONIDENTIFIABILITY`.**  The scope repair
is complete, the executable mathematics is unchanged, and the new receipt
matches current bytes.

This closes the finite rank/null counterexample only.  It does not identify or
exclude a fundamental generator, provide a real untouched prediction, or
license downstream geometry claims.
