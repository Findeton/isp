# JCV hostile review — algebraic geometry and quantifiers

Review seat: **A — algebraic geometry / quantifiers**  
Immutable target: `35c2511657efbee6c1c1887f2d7626faa4d396ea`  
Grade: **ACCEPT-WITH-FIXES**

## Independence statement

I performed this review from the frozen protocol and the immutable target
only.  I did not read, list, summarize, or receive another JCV review.  I
reconstructed the quotient and solution sets before inspecting
`jcv_score.py` as an implementation audit.  I did not import that scorer or
use it as an oracle.

## Executive finding

The registered exact result survives hostile reconstruction.

- The chart-sign quotient really has 16 orbits, each of size 64, and the four
  displayed holonomies separate those orbits.
- The shared-law model has exactly 7 nonempty holonomy sectors: one sector
  whose full-coherent locus is nonempty and has algebraic dimension 2, plus
  six sectors that are forced to rank one or less and have dimension 1.
- The independent-triangle control has exactly 9 nonempty sectors, with
  dimensions `2,2,2,2,3,3,3,3,4`; its two extra keys are exactly those in the
  receipt.
- The two active rational witnesses satisfy every equation, lie on
  `Delta*x*y != 0`, and give `p_plus=0` and `p_plus=49/625`.
- The frozen decision table therefore emits
  `JCV-PAIRING-SELECTED-WEIGHTS-FREE` on the registered active locus and
  `JCV-STRATIFIED` globally.

There are **zero numerical discrepancies** and no false sector, dimension,
witness, probability, orbit, or control count.

The fixes are about certification and scope, not the primary arithmetic.  In
particular, (i) this is a joint constraint variety, not a literal fixed point,
and (ii) algebraic dimension plus two real points is not a generally valid
certificate of a continuous real family.  Here the latter claim happens to be
true and has a short exact proof that should be added: the active component is
linearly isomorphic over `Q` to a product of two unit conics.  The paper should
also say that its count of six dark sectors does not enumerate the lower-
dimensional inactive divisors inside the all-trivial-holonomy sector.

## Read set

All paths below were read at the immutable target unless a different commit is
explicitly named.

- `v16/note-jcv-hostile-protocol.md` (complete)
- `v16/note-jcv-pin.md` (complete)
- `v16/code/jcv_fixture.json` (complete)
- `v16/code/jcv_output.txt` (complete)
- `v16/code/jcv_receipt.json` (parsed completely; selected large subobjects
  rendered separately)
- `v16/paper-02-joint-comparison-fixed-point.md` (complete)
- `v16/code/jcv_score.py` (complete, after the independent reconstruction)
- `v16/code/jcv_variety.py` (complete, with line-by-line attention to the
  polynomial, Buchberger, dimension, substitution, and saturation routines)
- `v16/note-jcv-fixture-freeze.md`
- `v16/note-jcv-official-run-failure.md`
- `v16/note-jcv-scorer-repair.md`
- `v16/note-jcv-solver-freeze.md`
- `v16/note-jcv-solver-postcommit.md`
- `v16/note-jcv-postcommit-verification.md`
- the exact scorer delta from fixture commit
  `ee8e414c2e354b5447af57efedbe234ae12af111` to the review target
- the path-limited commit history through fixture freeze, failed-run record,
  scorer refreeze, and candidate commit

No other JCV review path was read or listed.

## Tools and runtime

- Python `3.13.5` for independent standard-library exact enumeration with
  `fractions.Fraction`; no candidate module was imported.
- `/opt/homebrew/bin/python3.13` `3.13.2` for runtime identification only.
- Git `2.50.1 (Apple Git-155)` for immutable-blob reads, history, and exact
  diffs.
- `shasum` `6.02` / SHA-256 for artifact hashes.
- Independent hand algebra for the ideals, coordinate change, component and
  radical analysis, and classifier derivation.

No float, numerical root finder, tolerance, finite rational sampling, CAS, or
network source was used.

## Artifact and receipt audit

All five protocol hashes match the immutable blobs exactly:

| artifact | frozen SHA-256 | observed SHA-256 | discrepancy |
|---|---|---|---:|
| fixture | `ad887c213d14781838c6e70227b8f2c162f1392a08060de7c6e57829a8db012b` | same | 0 |
| scorer | `66b87bdf68f7210d959e13bfacae4c5957413e6d8f234647bfe3ad4a19619a03` | same | 0 |
| paper | `b54858c394fe22626ef1e233781737b7199cc56bf816f52e8aae063a99deaefc` | same | 0 |
| transcript | `b1d950c804c8b568514f1a0206853496b2f578650a3d98187e64c1c8a9b70d6d` | same | 0 |
| receipt | `a1b0baeee418d3f2c82e1ec6d07993cb51f69f3f51d63a9996dae9fb177fe3d1` | same | 0 |

I independently canonicalized each receipt value with sorted keys and compact
JSON separators.  The receipt declares 17 keys outside its manifest, contains
exactly 17 such keys, and its manifest has exactly the same key set.  All 17
per-key hashes match.  Total-seal discrepancies: **0**.  The paper, output,
fixture, and scorer cross-hashes in the receipt also match.

## Independent gauge reconstruction

Treat the plus and minus calibrated eigenchannels separately.  For either
channel the overlap graph has four vertices and five edges.  A chart-sign
choice at each vertex acts on an edge sign by the product of the signs at its
two endpoints.  The graph is connected, so the all-vertices sign is the
one-element stabilizer of that channel action.  The effective gauge orbit has
size

`2^(4-1) = 8`

per channel, hence `8*8=64` for the two independent channels.

The cycle rank is `5-4+1=2` per channel.  A cycle basis is supplied by the two
triangles, giving

`q012+ = a*c*e`, `q123+ = c*g*j`,

and independently

`q012- = b*d*f`, `q123- = d*h*k`.

The products are invariant because every chart sign occurs twice around a
cycle.  Conversely, if two raw assignments have the same four products, take
their edgewise ratio, gauge-fix the three edges of a spanning tree, and use
the two equal cycle products to fix the two chords.  Thus equal `q` keys are
gauge-equivalent: the four invariants separate the orbits, rather than merely
having the right count.

Independent enumeration gave:

- raw assignments: `2^10 = 1024`;
- quotient keys: `2^4 = 16`;
- orbit-size set: `[64]`;
- orbit mismatches: `0`.

The raw defect identity is also exact.  For example,

`a*c-e = e*(a*c*e-1) = e*(q012+-1)`

because `e^2=1`; the other three channels are identical.  Therefore passing
from raw defects to the four quotient defects loses no solution information
inside the declared sign family.

## Independent shared-law solution

Write a key as `(q0+,q0-,q1+,q1-)`.  The plus column `(x,u)` is available iff
both plus holonomies are `+1`; otherwise at least one nonzero sign defect
forces `x=u=0`.  Likewise the minus column `(y,v)` is available iff both minus
holonomies are `+1`.

The completeness equations are

`x^2+y^2+u^2+v^2=1`, `x*y+u*v=0`.

Hence:

1. If neither column is available, normalization is impossible.
2. If only the plus column is available, the ideal reduces to
   `<y,v,x^2+u^2-1>` and has dimension 1.
3. If only the minus column is available, the ideal reduces to
   `<x,u,y^2+v^2-1>` and has dimension 1.
4. If both are available, the ideal is
   `<x^2+y^2+u^2+v^2-1, x*y+u*v>` and has dimension 2.

This gives the exact nonempty table:

| key | dimension | full-coherent locus |
|---|---:|---|
| `(-1,1,-1,1)` | 1 | empty |
| `(-1,1,1,1)` | 1 | empty |
| `(1,-1,1,-1)` | 1 | empty |
| `(1,-1,1,1)` | 1 | empty |
| `(1,1,-1,1)` | 1 | empty |
| `(1,1,1,-1)` | 1 | empty |
| `(1,1,1,1)` | 2 | nonempty |

All other nine keys are empty.  This matches the receipt exactly.

### Active component, radicality, and dimension

The active ideal has an especially transparent exact form that the candidate
should expose.  Make the invertible rational linear change

`A=x+y`, `B=x-y`, `C=u+v`, `D=u-v`.

Then the two equations become

`A^2+C^2=1`, `B^2+D^2=1`.

Thus the active component is the product of two affine unit conics.  Over an
algebraic closure each conic is isomorphic to `G_m` (use
`A+iC` and `A-iC`), so the product is irreducible, smooth, reduced, and has
Krull dimension 2.  Over the reals it is `S^1 x S^1`, so its real locus is
also genuinely two-dimensional and continuous.  This proves more than the
receipt's leading-ideal count and removes the real-versus-complex ambiguity
for this particular ideal.

The displayed active Groebner basis, in lexicographic order `x>y>u>v`, is

`x^2+y^2+u^2+v^2-1`,

`x*y+u*v`,

`x*u*v-y^3-y*u^2-y*v^2+y`,

`y^4+y^2*u^2+y^2*v^2-y^2+u^2*v^2`.

The third polynomial is the negative of `y*f-x*g`; the fourth is
`u*v*g-y*h`, with `f,g,h` the first three rows in order.  Their leading
monomials are `x^2`, `x*y`, `x*u*v`, and `y^4`.  The smallest vertex cover of
their supports has size 2, so the leading monomial ideal has dimension
`4-2=2`.  The source's exact S-pair reduction reports zero failures, and the
independent conic decomposition shows that no hidden embedded or nonreduced
component can alter this result.

Every dark nonempty sector is one smooth irreducible conic, so it is prime,
radical, and dimension 1.  The sign ideals are reduced in characteristic zero.
The shared quotient variety is therefore a non-equidimensional reduced union
of one dimension-2 component and six dimension-1 components.  Nonreduced or
embedded-component discrepancy: **0**.

### Saturation and real quantifiers

The full-coherent query is exactly

`H = x*y*(x*v-y*u)`.

The backend tests `H != 0` by adjoining `t*H-1`.  This is the correct
localization/saturation nonemptiness test over an algebraic closure; its graph
has the same dimension as the corresponding open subset.  On each dark conic
one entire column vanishes, so `H`, `Delta`, and `x*y` vanish identically and
the three nonzero loci are empty.  On the active prime component, the rational
witnesses below show that `H` is not in the prime ideal, so all three nonzero
loci are nonempty and remain dimension 2.

There is an important quantifier distinction.  A non-unit ideal over `Q` proves
an algebraic-closure point, not a real point.  Algebraic dimension 2 plus two
real points also does not, in general, prove that the real locus has a
two-dimensional continuum; positive-dimensional complex varieties can have
very small real loci.  In this fixture the `S^1 x S^1` transformation above
supplies the missing real certificate.  The claim is true, but the paper's
stated inference should cite this structural proof rather than present two
points plus a nonconstant remainder as a generally sufficient rule.

## Independent control reconstruction

With separate laws, triangle 012 and triangle 123 factor.  A triangle is
empty only at `(-1,-1)`, dimension 1 when exactly one channel is allowed, and
dimension 2 when both are allowed.  Taking products gives nine real nonempty
sectors:

| key | dimension |
|---|---:|
| `(-1,1,-1,1)` | 2 |
| `(-1,1,1,-1)` | 2 |
| `(-1,1,1,1)` | 3 |
| `(1,-1,-1,1)` | 2 |
| `(1,-1,1,-1)` | 2 |
| `(1,-1,1,1)` | 3 |
| `(1,1,-1,1)` | 3 |
| `(1,1,1,-1)` | 3 |
| `(1,1,1,1)` | 4 |

The two control-only keys are exactly
`(-1,1,1,-1)` and `(1,-1,-1,1)`.  Each factor has trivial rational real
points such as `(1,0)` or `(0,1)`, so these are real, not merely complex,
control solutions.  Reported control discrepancies: **0**.

## Witness, probability, and all-input checks

For the first active witness

`(x,y,u,v)=(12,-12,16,9)/25`,

the exact values are

- norm: `1`;
- `x*y+u*v`: `0`;
- `Delta`: `12/25`;
- `x*y`: `-144/625`;
- `H`: `-1728/15625`;
- `p_plus`: `0`.

For the second

`(x,y,u,v)=(16,-9,12,12)/25`,

the first five values are identical and `p_plus=49/625`.  Equation residuals
and reported-value discrepancies are **0**.

For all inputs, not merely these witnesses,

`K0^dagger K0 + K1^dagger K1`

equals

`(x^2+y^2+u^2+v^2) I + 2(x*y+u*v) Z`

on the frozen real slice.  The two polynomial equations are therefore exactly
the operator trace-preservation identity.  `p_plus=(x+y)^2=A^2` is a calibrated
outcome probability and is plainly nonconstant on `S^1 x S^1`.  The two
rational values prove operational movement.  A finite row-sign/Kraus-phase
quotient, if one additionally takes it, cannot remove either the dimension or
the differing probability.

## Frozen classifier audit

The independently reconstructed summary is

- `nonempty_count=7`;
- `active_count=1`;
- `dark_count=6` in the scorer's sector-level sense;
- `active_max_dimension=2`;
- `observable_moves=true`;
- `observable_signatures_differ=false`.

The frozen `classify_core` branch for one active sector, positive dimension,
and a moving observable is exactly
`JCV-PAIRING-SELECTED-WEIGHTS-FREE`.  The frozen compound rule changes the
global word to `JCV-STRATIFIED` when at least one active and at least one dark
sector coexist.  Both words therefore follow from the decision table rather
than from the paper prose.  Classifier discrepancies: **0**.

One terminology precision is needed: `dark_count=6` counts holonomy sectors
whose full-coherent locus is empty.  The `(1,1,1,1)` component itself also
contains lower-dimensional divisors where `Delta*x*y=0`.  Those points do not
invalidate active-locus selection, and they do not change the primary word,
but the paper should not let readers infer that the six sectors exhaust every
inactive or rank-deficient sublocus.

## Declared-assumption countermodels

These are conditional extensions, not changes to the registered primary
scope.

### 1. Remove the shared-law declaration

This is the frozen control, and it changes the solution set exactly.  The
nonempty count rises from 7 to 9 and admits the two mixed-handoff keys above.
The full-rank-at-both-triangles locus still forces all four holonomies to one,
so active flatness survives, but the global component structure and the claim
that those two keys are excluded do not.  Homogeneity is therefore measured,
not derived, exactly as the paper says.

### 2. Remove isometry while retaining the calibrated eigenspaces

Allow an intertwiner of the form

`P_ij = E_j diag(lambda_ij+, lambda_ij-) E_i^T`

with nonzero real channel scalings rather than signs.  A plus-only law
`(y,v)=(0,0)` remains normalized while every minus-channel defect is silent.
The minus cycle ratios can then vary continuously.  Thus the finite `16`
quotient sectors and the exact six-dark-sector census are consequences of the
isometry/sign declaration; without it the dark comparison family becomes
continuous.  On a genuinely full-rank law, however, both columns are nonzero,
so the same cut equations still force both channel defects to vanish.  This
conditional countermodel changes the global variety but not the narrow active
flatness mechanism.

### 3. Enlarge from the real slice to complex quantum data

Merely base-extending the frozen polynomial ideal preserves the two real
witnesses and therefore cannot restore weight uniqueness.  But a physical
complex instrument uses conjugates in the completeness equations, and complex
unitary intertwiners carry phases rather than signs.  That is a different
real-algebraic/semialgebraic system, not the holomorphic complexification
solved here.  The current positive pairing-selection statement therefore
cannot be promoted to the complex doctrine.  The paper's explicit refusal of
complex uniqueness is necessary and correct.

### 4. Remove nondegenerate binary calibration

The reduction of every intertwiner to two eigenchannel signs, and even the
canonical meanings of `p_plus` and `p_minus`, cease to follow.  Degenerate
eigenspaces permit rotations within a calibrated sector; a mismatch can live
in an unprobed degeneracy direction.  The current word `selected` is then
untyped until a larger comparison algebra and a law acting on all of it are
specified.  This supports, rather than weakens, the paper's doctrine-local
scope.

## Failure and repair chronology

The fixture and original scorer were committed at
`ee8e414c2e354b5447af57efedbe234ae12af111`.  The first run failed during the
predeclared mutant survey because the move-proof serializer encountered a
Python set.  At the failure-record commit
`b0c0d244de3b1344a2a9e72c234460ebd0f2a670`, all three result paths are absent.

The exact scorer delta to the repaired version is one branch in `serial` that
recursively serializes sets/frozensets and sorts their canonical encodings.
The fixture did not move.  No equation, witness, quotient, decision branch,
outcome word, or paper renderer moved.  The repaired scorer was committed at
`c561acc03e0837f7e72508a1e5aad06a8c75d2ff`; the candidate artifacts first
appear in the later as-is candidate commit
`ab2102a0f452b5760674946cecf5e9b581986bde`.

One wording nuance should be corrected in the failure note.  Source order
shows that the clean run had computed the physical measurements and rendered a
paper string in memory before the mutant-survey exception.  What is proved is
that no verdict or numeral was printed, promoted, or committed—not that the
calculation had not occurred.  I found no evidence of observable result
leakage and no route by which the generic set-serialization repair could tune
the physical result.  Physical-rule changes: **0**.  Artifact leakage:
**0 observed**.

## Words under challenge

### `fixed point`

Not earned.  No map is defined whose output comparison/record structure is
required to reproduce its input, and no equation derives the comparison
typing from the law's own durable records.  The system solves two declared
objects jointly under constraints.  The title and the sentence “conditional
fixed-point result” should say “joint comparison/law constraint variety” and
“conditional joint-constraint result.”  This is the smallest honest repair
and is already consistent with the paper's own final paragraph.

### `selected`

Earned only in the narrow form: on `Delta*x*y != 0`, the four gauge-invariant
holonomies must all equal `+1`, so there is one chart-sign orbit.  The
comparison doctrine, calibration, isometry, graph, cut equation, and shared
law are not selected.  The paper mostly states this correctly; “comparison
coherence is selected” should preferably read “flat holonomy is selected
inside the declared doctrine on the full-coherent locus.”

### `stratified`

Earned as a frozen classifier word and supported by the non-equidimensional
component structure.  It is not a complete Whitney/semialgebraic
stratification.  The active component has its own `H=0` divisors, which the
six-sector dark count does not enumerate.

### `dark`

Correct for the six reported sectors: every solution in them has one entire
history column zero, hence `Delta=x*y=H=0`.  Define it explicitly as
“sector whose registered full-coherent locus is empty” to avoid the exhaustion
ambiguity above.

### `dimension two`

Correct as Krull dimension over an algebraic closure and, by the explicit
`S^1 x S^1` form, also correct as the local dimension of the real active
locus.  The generic solver alone only reports the former.

## Sentences stronger than their certificates

1. Title: “A joint comparison/law fixed point ...” — no fixed-point map or
   record-generated self-consistency equation exists.
2. “Therefore this fixture is a conditional fixed-point result ...” — same
   issue; it is a conditional joint-constraint result.
3. “A moving calibrated probability on a positive-dimensional variety proves
   that the surviving direction is physical weight freedom ...” — true here,
   but algebraic-closure dimension plus two real points is not the general
   real-continuity certificate suggested by the sentence.  Add the exact
   product-of-circles proof.
4. “The active weight variety remains continuous ...” — true here for the same
   reason, but that reason is absent from the candidate certificate.
5. “The remaining 6 ... are dark/rank-deficient strata” — correct as a count
   of wholly dark holonomy sectors, not an exhaustive count of every
   rank-deficient sublocus; the all-trivial sector contains `H=0` divisors.
6. “The deepest circularity has been narrowed ...” — defensible research
   interpretation, not a theorem of the fixture; label it as interpretation.
7. The motivating language about histories that “rewrite their relational
   carriers differently” is not instantiated by a rewrite in this arena.  The
   paper's later wall repairs this, but the opening should say that the charts
   are an interface surrogate for that future problem.
8. “Dynamical weights” can be read as a full successor dynamics.  What was
   shown free is the frozen boundary-instrument coefficient law; use that
   narrower phrase.

No sentence promotes geometry, backreaction, growing-factorization
no-signalling, actualization, a Hamiltonian, particles, constants, continuum,
or QFT/GR deviation.  Prohibited-physics promotions found: **0**.

## Smallest repair set

1. Rename the paper and both “fixed-point result” usages to “joint constraint
   variety/result.”
2. Add the exact change of variables
   `(A,B,C,D)=(x+y,x-y,u+v,u-v)` and the equations
   `A^2+C^2=B^2+D^2=1`.  State that this proves radicality, algebraic dimension
   2, a real two-dimensional continuum, and nonconstant `p_plus=A^2`.
3. Define a “dark sector” as a holonomy sector with empty registered
   full-coherent locus, and note that the all-trivial sector also has inactive
   divisors `Delta*x*y=0`.
4. Change the first-run note's “before verdict” language to “before any verdict
   was emitted or promoted”; retain the exact one-branch repair record.
5. Narrow “comparison selected” to “flat holonomy selected, modulo the
   declared chart-sign gauge, on the registered full-coherent locus,” and
   “dynamical weights” to “boundary-instrument weights.”

These repairs do not change any equation, artifact number, primary word,
active-locus word, or consequence wall.  No rerun of the physical fixture is
needed unless the panel's process rules require paper bytes to be regenerated
from a repaired renderer.

## Final grade

**ACCEPT-WITH-FIXES.**  The exact finite result and its registered scope are
correct.  The candidate needs a real-locus certificate already available from
its own equations, a precise definition of its sector-level dark count, and
removal of the unsupported “fixed point” label.  None of these findings
demotes `JCV-STRATIFIED` or the conditional active-locus word.

Report-file SHA-256 is reported out of band after this file is frozen; an
ordinary file cannot contain its own complete-file digest without changing
that digest.
