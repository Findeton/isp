# D12 hostile round-2 mathematics / probability review

**Date:** 2026-07-11  
**Verdict:** **PASS AT THE NARROWED `A_D12` SCOPE, WITH MINOR/MODERATE LABEL REPAIRS**  
**Round-1 protocol blocker:** removed  
**New fatal opening:** none found  
**Final D12 verdict licensed:** `UNIVERSAL-FORM/PRIMITIVE-PROCESS-REMAINS`, only at the explicit finite-packet/unitary-frame scope stated in the revised paper

## Executive finding

The replacement is not a cosmetic expansion of the rejected 25-check program.
It constructs an actual history tree, carries normalized branch states into new
collars, emits immutable records, gives explicit prefix pushforwards, transports
links and screens through different endpoint frames, quotients the two
linearizations of a disjoint pair, retains overlapping order, and supplies an
all-level classical cylinder formula.  The all-depth arguments for the two
fixed quantum packets are mathematically valid.  The revised Theorem 3 no
longer quantifies over all of `A_SHARD`; it quantifies over the exact shared
packet principles implemented by the countermodels.  At that narrowed scope,
the two-model nonuniqueness proof is sound.

Round one's `INCOMPLETE-INVESTIGATION` verdict therefore does not survive the
repair.  Some receipt labels remain broader than the exact executable: the
construction quotient is explicitly a two-disjoint-event cell, the frame test
executes one independently varying five-vertex assignment rather than an
enumeration of all assignments, and the packet's so-called
`log_rn_history_coefficients` are extended atomwise log-density values, not
coefficients in the displayed contrast basis.  These require wording or short
general lemmas.  None invalidates the narrowed underdetermination theorem.

## Frozen repaired sources and reproduction

The authoritative repaired artifacts reviewed were:

```text
228e34053549fcfbeb9cb894004195fe1d558241b470e58b888b6873cd29afe1  code/d12_multidiamond_history_exact.py
12604d2edb5438ec35719b710cc797cf84371eb84e8a8c45994b5d10c2c38796  note-d12-round1-opening-repairs.md
61834ebdd235c1a7eadb074fc2fb9a42a987e7cbf79adedd7c51922c2af787c3  note-d12-selection-principle-audit.md
db80a8cd1ff48d649eaf83154d7f53b2148f30dadb5ae7b2e1a4538cf934364b  relativistic-isp-v10-paper13-the-click-law-is-the-whole-history-process.md
2497f7878cf464bc54f6e505b548fcb09fb5c2abc6f76891f22f212dd96ea2e9  data/d12-round1-repair-receipt.md
```

I ran the 137-check replacement under ordinary and optimized Python.  Both
outputs were byte-identical:

```text
stdout SHA-256 normal = ef930e21338322c76c3581cbcaab0e6f8f95c370ccc9bb2a0a22e319f5031091
stdout SHA-256 -O     = ef930e21338322c76c3581cbcaab0e6f8f95c370ccc9bb2a0a22e319f5031091
checks                = 137
semantic receipt      = b8a0dd95bf1487860d981ae4d41782d155820d9fd5c5309c3167047fea219433
```

All theorem-critical arithmetic is exact in `Fraction` or
`Q(sqrt(2),i)`.  No probability or gauge verdict depends on floating-point
tolerance.

## Opening-by-opening adjudication

### M1 — finite `P_r` was not an all-level projective process

**Disposition: CLOSED mathematically; one prose insertion requested.**

The replacement defines, for every finite prefix `v=(v_1,...,v_n)`,

$$
P_r^{(n)}(v)=
\prod_{j=0}^{\lfloor n/3\rfloor-1}
\frac{1+r v_{3j+1}v_{3j+2}v_{3j+3}}8
\;2^{-(n\bmod3)}.
$$

This is the product of independent complete `P_r` triples and the uniform
marginal of the final incomplete block.  Summing the last sign gives the
preceding prefix mass in all three residue classes modulo 3.  Strict positivity
holds for `|r|<1`.  The conditional is fair at block positions 1 and 2 and is

$$
P(v_{3j+3}=z\mid v_{3j+1}=x,v_{3j+2}=y)=\frac{1+rxyz}{2}
$$

at position 3.  Hence the process is non-first-order-Markov and the `r=1/2`
and `r=1/3` families differ while all one- and two-coordinate shadows remain
uniform.  Exact normalization, adjacent bonding, and conditionals were
exhaustively checked through depth 9; the displayed formula proves arbitrary
depth.

Paper 13's Theorem 1 section still stops after the three-variable formula and
does not display this all-level extension, even though the later proof cites
the block families.  Add the formula above to the paper.  The executable and
repair note already close the mathematical opening.

This also resolves the Egri category issue.  D12 explicitly supplies a
probability on histories and disintegrates it; it does not infer joint paths
from a trajectory of one-time probabilities.

### M2 — local iSWAP matrices were not full countermodels

**Disposition: CLOSED for revised Theorem 3.**

Both interactions now enter the same `DiamondPacket`/history constructor.
They share the history carrier, positive reference, contrast ledger,
evidence/commitment tags, pointer screens, types, order unit, collar ownership,
eligibility grammar, branch constructor, record constructor, frame transport,
and prefix machinery.  Both are separately audited through depth four and by
the same continuation induction.  They disagree on the same atom `(1,)` with
probabilities `1/2` and `0`.

The revised theorem correctly replaces the former `A_SHARD` quantifier with
`A_D12`, enumerates the actually shared packet principles, and explicitly
excludes integrated nonunitary Lorentz gauge and universe-specific field
theory.  Two models of those premises with different record probabilities are
enough to refute unique interaction/history-measure entailment.

### M3 — universal exponential form lacked hypotheses

**Disposition: CLOSED.**

The revised paper restricts the finite expression to a supplied finite
`Ext_G(B)` with a strictly positive reference, and its measure-theoretic
disintegration only assumes measurable positive-mass cylinders.  It separates
grammar `G` from positive-mass support `Ext_(G,mu)`.  The action/MaxEnt refusal
remains correct.

### M4 — the minimum U1 packet was absent

**Disposition: SUBSTANTIALLY CLOSED; naming repair required.**

The replacement supplies history atoms, a positive reference, a spanning
three-mode contrast ledger, one-diamond law, screens, order unit, eventless
collar flag, input/output types, evidence and commitment data.  Runtime collars
and records carry owners, states, endpoint frames, links, effects, provenance,
outcomes, output interfaces, opportunities, and continuation state.  This is a
real packet rather than the predecessor's metadata shell.

One field is mislabeled.  For the quarter packet the stored tuple is

```text
(-infinity, ln(2), ln(2), -infinity)
```

and for the half packet it is

```text
(-infinity, -infinity, ln(4), -infinity).
```

These are the **atomwise extended values** of `log(P/mu)`, not coefficients in
the three-row contrast ledger.  Because both Born laws contain zeros, the V6
strict-positive finite log-RN coefficient theorem does not apply without
support restriction or an extended-boundary treatment.  The code only checks
that the tuples differ and have the right length; it does not reconstruct the
laws through the contrast ledger.

**Repair:** rename the field `extended_log_rn_atom_values`, state that
`exp(-infinity)=0`, and do not call it a contrast coefficient vector.  If an
actual `h_D` in the displayed basis is required, restrict each packet to its
positive support (noting that the supports then differ) or define and prove the
extended exponential-family convention.  The revised theorem only assumes
complete contrasts and a positive reference, not a finite `h_D` generating
these zero-bearing laws, so this does not defeat Theorem 3.

The stale-input refusal is also a predicate test rather than a global consumed
collar registry.  Within `generate`, every history node is expanded once, so no
double-use occurs.  Do not promote that bounded constructor fact into a general
distributed uniqueness theorem.

### M5 — U3 was only one marginalization

**Disposition: CLOSED for the constructed models.**

The quantum tree has explicit levels 0 through 4.  Every adjacent prefix map
pushes the fine cylinder law to the previous level; earlier record tuples
persist byte-for-byte.  For quarter-iSWAP every positive prefix through depth 3
has two conditional masses `(1/2,1/2)`.  The all-depth step is valid for these
two fixed packets: unitarity and pointer completeness normalize every parent,
rank-one projection returns a pointer branch, and the output constructor
preserves normalized state and input type.  Iteration therefore defines a
compatible prefix law at arbitrary depth.

Separately, the classical block formula supplies an explicit all-level
non-Markov projective family.  The receipt no longer relies on a neutral-bit
refinement as its main projectivity evidence.

The induction is packet-specific.  It should not be read as proving that every
arbitrary instrument accepted by the abstract architecture works with the
hard-coded `normalize` routine.

### M6 — disintegration hypotheses were missing

**Disposition: CLOSED.**

Paper 13 now requires `D(H,H)>0`, an exhaustive durable record partition, and
exact consistency/decoherence.  It explicitly says coherent alternatives are
summed at class-operator level before taking a diagonal and that approximate
decoherence needs a separate error analysis.  It distinguishes decoherent
histories from process tensors rather than declaring them identical.

The exact quantum constructor uses complete orthogonal pointer outcomes, and
the classical constructor checks conditional ratios against its cylinder
family.  No approximate probability is promoted to an exact one.

### M7 — U4 canonical fibers were absent

**Disposition: CLOSED at the explicit two-disjoint-event scope; unrestricted
U4 wording still needs a lemma or narrower label.**

The code now constructs the `AB` and `BA` auxiliary schedules, marks outcomes
by physical diamond, maps both presentations to the same canonical keys,
checks equal weights, and stores only one weight per physical fiber.  The
canonical law normalizes to one rather than double-counting the two gauges.  A
same-collar `X_left`/iSWAP control fails to commute and changes a downstream
record probability, so overlapping order is not incorrectly quotiented.

This is exactly the missing bounded cell for two disjoint diamonds.  It is not
an exhaustive implementation of "all auxiliary linearizations of bounded
concurrent firings" for arbitrary finite partial orders.  The general extension
is straightforward if every allowed adjacent swap of incomparable operations
commutes and the weight is invariant: any two linear extensions are connected
by such swaps.  State and prove that lemma, or label the receipt
`two_disjoint_event_canonical_fiber=PASS`.  The revised theorem can be read at
the executed two-event scope, so no fatal gap follows.

### M8 — U7 was one global Hadamard change

**Disposition: CLOSED at the stated unitary-frame scope.**

The repaired history uses five distinct endpoint frames:

```text
I, H⊗I, I⊗H, H⊗H, SWAP.
```

At each edge the stored link is

$$
L_{j+1,j}=B_{j+1}U B_j^\dagger.
$$

The state and pointer screen transform by `B_j`, so adjacent frame factors
cancel and every cylinder mass agrees with the identity-frame history.  The
program checks all depths, final collar transport, record endpoint names, link
matrices, screens, and both interaction packets.

Only one nontrivial sequence is executed, but the displayed conjugation
identity proves the same result for any independently assigned unitaries for
which the packet arithmetic is defined.  The paper now explicitly refuses to
claim nonunitary Lorentz-frame integration.  This is an honest closure of the
round-one overclaim.

### M9 — 256 commits were integer bookkeeping

**Disposition: CLOSED.**

The fake `live -= 2; live += 2` claim is retracted and the old script is labeled
a one-cell precursor.  Four levels are actually generated with histories,
records, collar states, masses, links, and ownership data.  The arbitrary-depth
statement is now an induction from pointer completeness, unitarity, branch
normalization, and preserved output type.  That induction is valid for the two
fixed iSWAP packets.

### M10 — U8 and Theorem 3 exceeded the constructed premises

**Disposition: CLOSED for the narrowed theorem and verdict scope.**

The revised theorem no longer claims that the two toy packets are complete
models of every V6–V10 principle.  It defines `A_D12` from the exact shared
packet properties and states its exclusions.  The two-model argument proves
that `A_D12` does not select an interaction coupling or induced history
measure.  Grammar nonselection is attributed to the separate D7 witnesses,
not smuggled into the iSWAP conclusion.

The A–E census is now explicit.  In particular, architecture E uses independent
exponential races with rates equal to the already supplied conditional masses.
The repair checks through depth 9, for both `r` values, that products of the
block-relative winner probabilities equal every `P_r^(n)` cylinder.  This is a
representation of class C, not a new selector.  The earlier first-block-only
gap is absent from the frozen 137-check build.

The final verdict is licensed only in the sense the revised paper states:
the universal **conditional representation** is disintegration of a supplied
typed whole-history process, while the grammar, measure, action, coupling,
state, and instruments remain primitive or empirical.  It is not a derived
law of nature.

## New and residual opening ledger

```text
R2-1  MINOR     Put the arbitrary-n independent-block P_r formula in Paper 13's Theorem 1 proof.
R2-2  MODERATE  Rename extended atomwise log(P/mu) values; they are not contrast-basis coefficients.
R2-3  MODERATE  Restrict U4 PASS to the executed two-event fiber or prove the finite-poset adjacent-swap lemma.
R2-4  MINOR     State explicitly that the quantum continuation induction is for the two fixed packets,
                 not every possible instrument accepted by the abstract architecture.
R2-5  MINOR     Treat stale-input exclusion as a constructor invariant, not a proved distributed registry law.
```

None is fatal to the revised `A_D12` nonuniqueness theorem.  R2-2 prevents the
receipt from being described as an exact implementation of the V6
strict-positive log-RN reconstruction on the zero-bearing Born carrier.  R2-3
prevents the two-event computation from being advertised as an unrestricted
construction-gauge theorem until the short general lemma is supplied.

## Claims independently confirmed

- The all-level `P_r` block families are normalized, strictly positive,
  projective, and non-first-order-Markov for nonzero `r`.
- The local exponential-race products reproduce those all-level cylinder laws;
  the threshold representation does not introduce a different process.
- Quarter- and half-iSWAP remain unitary, exchange-symmetric,
  excitation-preserving, entangling countermodels with record probabilities
  `1/2` and `0`.
- Both repaired quantum history trees normalize and restrict projectively, and
  their continuation induction is valid for arbitrary depth.
- Conditional probabilities are taken only on positive cylinders, with exact
  decoherence hypotheses stated.
- Different endpoint unitary frames give the same cylinder laws after correct
  link/screen/state transport.
- The two auxiliary schedules of a disjoint pair give one normalized physical
  law, while overlapping order remains observable.
- Action, MaxEnt, holonomy, profinite completion, and Born calculus constrain or
  represent supplied dynamics but do not select the missing coupling/process.
- Geometry remains correctly gated.

## Decision

**Pass the repaired mathematics at the narrowed theorem scope.**  The main
round-one verdict is reversed: the exact finite-packet countermodels and the
all-level classical process now support the underdetermination conclusion, and
no new fatal gap was found.  Before final archival acceptance, correct the
extended-log-RN name and either narrow or generalize the U4 receipt label.  Keep
the final headline explicitly bounded to the paper's stated
finite-packet/unitary-frame conditional representation; it is not the final
interactive law of our universe.
