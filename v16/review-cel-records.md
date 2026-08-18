# CEL hostile review — Seat R: records, recurrence identity, and relational flag typing

## 1. Immutable-target and hash audit

I reviewed the target bound by `v16/note-cel-hostile-protocol.md`, without
consulting either other CEL report. The candidate commit
`f3c3ef99f1506f01208a670198a91abe27c952d5` and verification commit
`15299d1ee6ffca4ede9b9bd0ae86dfe2dee386c1` both exist as commit objects.

The current bytes reproduce every immutable target hash:

| artifact | protocol SHA-256 | reviewer SHA-256 | status |
|---|---|---|---|
| pin | `83762533fa6dad63acbeb3c13b2db9a63b6533b0ce113a61012d959552fa542d` | same | PASS |
| generic core | `f08b880095e71ac79082d2672ec849dc9ffd1ab66c702a85f2b24165a02aedac` | same | PASS |
| core-freeze note | `01f584c0117a79f61d9dcb2dc352d7ecf291f4176f583882d72c5a13bfd6966c` | same | PASS |
| physical fixture | `8a18a70f1e1b7781806d800c54afd5dcbd10dbac1307db4420bafcb4b57854f2` | same | PASS |
| scorer | `27ee69af161382dfda3de81e1ea4d0edf4d6b4afb8d11d5f30ec7d3e075749c8` | same | PASS |
| fixture-freeze note | `b5bf12b6d8032601ed59a6d8d32d46ea7f4e809c842c3efa7020f3546d4748e7` | same | PASS |
| transcript | `098d6113fb9f3ce0dbf43a28aeec213a5b06235c55556389989e93e1387028f6` | same | PASS |
| receipt | `a2fe34ccbbc8a1049824fd72020da5806e399f7a50a45e9bdf832e7e45a8eeda` | same | PASS |
| Paper 7 | `acf2dafb165d5ceb82bf4bc532b194f760095ce355b0b5ee7c5996df13878f90` | same | PASS |
| candidate verification | `abbc2eba6042a519769986c480931e10accccbea58454df1750453d3a66c7106` | same | PASS |

The receipt has 44 unique passing gates, 13 claims, 11 qualifiers, and 15
scope walls. I recomputed its eight canonical-JSON payload seals; all eight
match. A clean replay to three fresh paths under `/private/tmp` reproduced
the transcript, receipt, and paper byte-for-byte at the three frozen hashes.
Seven seat-relevant registered mutants (`reset-kraus`, `all-word-grammar`,
`catalogue-enlargement`, `branch-label`, `recovery-licence`,
`flag-attachment`, and `operational-null`) each exited `1` and wrote no
artifact.

Integrity is therefore green. The rejection below is scientific and typed,
not a provenance failure.

## 2. Independent method and tools

I read the runbook, the complete CEL protocol, pin, two freeze notes, generic
core, fixture, scorer, transcript, both receipts, generated paper, and
candidate verification. For the required lineage comparison I read Papers
3–6, the v12 record definition/theorem/eraser sections, and the v15 homonym
audit. I did not use the candidate receipt's gates as proofs.

I rebuilt the Seat-R claims in a separate exact script,
`/private/tmp/cel_records_independent.py`, importing neither `cel_core.py` nor
`cel_score.py`. It uses `fractions.Fraction`, explicit permutation matrices,
exact matrix products, deterministic finite-semigroup closure, and explicit
source/flag readouts. It reconstructs the recurrence histories, reset in both
pictures, relabeling, one- and two-copy grammars, retained/discarded branch
recovery, both JCV dilations, their support and covariance, and an alternative-
catalogue control.

The crucial hostile distinction was applied throughout:

1. an algebraic equality is not automatically a law identity;
2. a repeated token suffix is not an event-type dictionary;
3. a Stinespring target basis is not automatically a created relational cell;
4. information surviving somewhere is not the same claim as a licensed flag
   record surviving; and
5. a conditional port is not an actualized event.

## 3. Exact recomputation table

| item | candidate value | independent reviewer value | status |
|---|---:|---:|---|
| CNOT-order endpoints from `100` | `111`, `110` (indices `7,6`) | `7,6` | PASS |
| biased/balanced `111` screen | `16/25`, `1/2` | `16/25`, `1/2` | PASS |
| idle-dressed screens | `16/25`, `1/2` | `16/25`, `1/2` for **both** lawful kernels | PASS, but nonselecting |
| identical-history raw kernels | unequal | unequal | PASS |
| identical-history unconditioned channels | equal | equal identity channel | PASS at discarded-port grain |
| identical-history calibrated two-port control | not run | outcome vectors `(1,0)` versus `(0,1)` | KILLS unqualified null language |
| exchange-fixed biased/balanced kernels | `false,true` | `false,true` | PASS algebraically; licence declared |
| joint-coordinate restrictions | `(3/5,4/5)`, `(3/5,5/13)` | same | PASS as coordinate restriction only |
| independent/universal affine dimensions | `2 -> 1` | `2 -> 1` | PASS as price of imposed `x=y` |
| reset, Schrödinger picture | both sectors merge | `0 -> 0`, `1 -> 0` | PASS |
| reset, Heisenberg picture | diagonal-covariant | `P0 -> I`, `P1 -> 0` | PASS |
| flag relabel | recoverable, fixed `P0` not commuting | `P0 <-> P1`, exactly invertible | PASS |
| append-only semigroup | one word, all recoverable | identity only, one word | PASS but trivial |
| one-copy refire | flag erased | `00/11 -> 00/10`; flag merges, source remains | PASS, flag-only |
| restricted two-copy semigroup | 2 words, licensed all-word recovery | outputs `000/111`, `000/101`; flag 2 always reads | PASS |
| enlarged two-copy semigroup | 4 words, licensed recovery fails | additionally `000/110`, `000/100`; last word erases both flags | PASS |
| enlarged global mathematical recovery | `true` | source bit distinguishes all four words | PASS; not flag permanence |
| retained identity/flip branch | recoverable | both branches invert exactly | PASS |
| discarded equal branch | `[[1/2,1/2],[1/2,1/2]]` | same | PASS |
| shared JCV kernel | `diag(16/25,9/25)` | same | PASS |
| stacked flag isometries | exact | exact | PASS mathematically |
| support union | `(0,0),(1,1),(2,0),(3,1)` | same | PASS |
| printed covariance | `P_out W1 P_in = W2` | exact | PASS as basis permutation |
| first-port movement | `0 -> 49/625` | `0 -> 49/625` | PASS with fixed calibration |
| relational attachment used by any prediction | claimed weld | no matrix, channel, port probability, or continuation consumes it | FAIL |
| alternative relational readings of same `W` | anonymous control rejected by metadata | attached cell, internal matter port, and anonymous target give identical exact operator/statistics | KILL |

The two exact dilation matrices are

```text
W1 = [[0,0],[0,24/25],[1,0],[0,7/25]],
W2 = [[7/25,0],[0,1],[24/25,0],[0,0]].
```

They support the candidate's Stinespring and calibrated-port arithmetic.
They do not select whether the four target directions mean a new attached
cell, an internal two-level degree of the matter cell, or an anonymous
four-level target. All three readings retain the same arrays and every frozen
probability.

## 4. Theorem/proof audit

### 4.1 The five recurrence rungs are not five instances of one theorem

| rung | what actually establishes equality | reviewer classification |
|---|---|---|
| transport locality | nothing; two complete kernels give different screens | exact nonselection countermodel |
| spectator naturality | the standing idle-extension axiom, represented in the fixture by a Boolean licence | axiom-propagated operational equality, not derived recurrence |
| automorphism covariance | a declared swap of two history coordinates | fixed-packet symmetry selection, not cross-context recurrence |
| shared-token gluing | equality of restrictions of one three-entry rational vector | correctly typed equality control, not a joint probability/process law |
| token-disjoint universality | the explicit equation `x-y=0` | nomological declaration, with a one-dimensional price |

The paper is commendably explicit that naturality is an axiom and universality
is a postulate. Two remaining promotions are nevertheless too strong.

First, the recurrence fixture supplies no catalogue map, rewrite isomorphism,
local neighbourhood type, or calibrated event algebra that identifies
`lab-left:AB` with `lab-right:AB`. Their shared suffix is the entire type
certificate. Thus `2 -> 1` measures the cost of declaring two free coordinates
equal; it does not yet price universality of an independently established
physical event type. The type dictionary and the law equality are introduced
in the same declaration.

Second, the “joint law” in the gluing rung has no histories, kernel,
normalization, preparation, output, or observable. It is the vector
`(3/5,4/5,5/13)` with two coordinate projections. The positive and mismatch
controls prove restriction consistency only. They do not establish a
shared-token interaction/gluing theorem.

### 4.2 Operational-null equivalence is port-relative

For histories `(I,I)`, `diag(1,0)` and `diag(0,1)` do induce the same complete
unconditioned channel. That is an exact null direction after the history label
has been discarded. Retain two calibrated history ports instead and the same
two kernels give outcome probabilities `(1,0)` and `(0,1)` on every normalized
input. Therefore the null is not an intrinsic property of the raw history
family; it is a null of the selected observable packet.

This agrees with Paper 3's continuation-stable quotient doctrine, but the CEL
fixture does not perform that doctrine: it checks one unconditioned channel
signature and supplies no retained-port or future-continuation census for the
null control. The qualifier must read “kernel identity only modulo the
registered **unconditioned-channel** null,” not operational null without a
port condition.

### 4.3 Recoverability results survive, at their declared grammar

The reset is a clean theorem-sized counterexample to bare algebra covariance:
its adjoint sends `P0` to `I` and `P1` to `0`, while both Schrödinger sectors
become sector 0. The relabel control correctly shows why fixed-projector
commutation is too strong. The finite semigroup calculations also survive:
the restricted two-copy grammar keeps a licensed flag copy under all two
words, while the four-word enlargement contains the last-word output
`000/100`, on which both licensed flag readouts are constant.

The scope is essential. The last source bit still distinguishes the encoded
alternatives under every enlarged word. Hence the enlargement destroys the
declared **flag-record algebra**, not all information about the source. The
paper says this in prose, and that caveat must remain in every headline.
Likewise, all-word means all words in the frozen finite grammar. Catalogue
closure is neither proved nor expected; a new generator can change the
classification.

These controls refine rather than replace v12's record notion. V12 requires
mutually exclusive sectors, correlation with alternatives, and availability
under the future. CEL exactly tests classical distinguishability and licensed
readout availability for a declared encoding. It does not show that an
actualized relational division/event record exists, nor does it run v12's
interference-killing support test on the created-flag dilation. “Conditional
recoverable flag label” is earned; “actual record event” is not.

### 4.4 The Stinespring theorem survives; the relational weld does not

The stacks are exact isometries and the two factorizations move a calibrated
port while keeping the unconditioned channel fixed. That is a real instrument
fact. The attempted ontological promotion is carried entirely by fixture
metadata:

- catalogue dimension is obtained by counting a supplied list;
- `attachment=[matter,flag]` is checked only for membership and orientation;
- allowed support is a supplied transition-support list;
- no later probe is computed from the attachment or output graph; and
- the anonymous control differs only by two metadata Booleans.

Erasing or changing the relational reading leaves `W1`, `W2`, their Gram
kernels, support, channel, isometry, port statistics, and flag-level
continuations unchanged. The classifier therefore distinguishes annotations,
not an operational relational role. Under Paper 4's typed-bundle doctrine,
this is a mathematical dilation plus one proposed bundle typing, not a welded
creation event.

There is also a precise prose error. The frozen covariance uses input
permutation `[1,0]` and output permutation `[3,2,1,0]`. It flips the matter
state label and, at output, the matter and flag value labels. It does **not**
“swap the matter and flag names”; the input has no flag factor to swap. This
basis covariance neither proves attachment covariance nor identifies a
recurring local vertex coupling.

## 5. Seat-specific ontology and representation audit

The strongest ontology earned by this seat is narrower than the primary:

- The overlapping CNOT maps and PSD kernels are finite process
  representations. Their “actor” and “event type” readings are declared, not
  recovered from a relational catalogue.
- An unconditioned kernel and a calibrated port factorization are distinct
  operational coordinates. A port basis can matter when its label is retained.
- The one- and two-copy fixtures contain exact classical encodings whose flag
  information is recoverable relative to specified readouts and finite future
  grammars.
- A Stinespring flag is a candidate carrier of a conditional record. It is not
  yet a relationally attached created cell, because the attachment has no
  indispensable future consequence.
- Actualization remains outside the model. Append/reset durability of a
  conditional port says what would remain distinguishable **if** that port is
  the realized record; it does not say why one port occurs.

The event-type universality analogy with identical couplings in two
laboratories is premature at this fixture. Ordinary physical universality
presupposes an independently calibrated species/type identity across the
laboratories. Here the equality of type and the equality of kernel are bundled
into the same postulate. Different token-disjoint dictionaries could pass all
local gates and change future physics.

The lineage is consequently consistent only after demotion:

- Paper 3's quotient makes nullness dependent on all licensed contexts; CEL
  checks only the unconditioned channel in its null arm.
- Paper 4's bundle keeps rewrite and transport jointly typed; CEL supplies a
  possible typing but no graph-dependent observable that makes it physical.
- Paper 5 left local flags kinematically permitted and implementation
  unselected; the current metadata does not close that implementation debt.
- Paper 6's recurrence selection was conditional on a dictionary and
  automorphism; CEL still does not construct the cross-context type
  dictionary.
- V12's record is correlation plus future availability at a division cut;
  CEL constructs grammar-relative conditional flag availability, not a
  division-event/actualization theorem.

## 6. Counterexamples and unrun controls

1. **Retained-port null counterexample.** With histories `(I,I)`, the two
   frozen raw kernels are equal after unconditioned channel projection, but
   calibrated two-port factorizations yield `(1,0)` versus `(0,1)`. This kills
   port-independent operational-null wording.

2. **Relational-reading counterexample.** The exact same `W1,W2` can be read
   as an attached created flag, an internal two-level port on matter, or an
   anonymous four-level codomain. Every frozen numerical observable is
   identical. This kills the claim that the attachment is already physical.

3. **Missing graph-erasure control.** Remove all graph/attachment metadata
   while retaining the matrices and calibrated ports. The scorer rejects the
   annotation by construction, but no predicted statistic moves. A genuine
   weld needs a later probe derived from the output relation graph and an
   erasure control showing that the probe cannot be reconstructed without it.

4. **Missing event-type census.** No cross-context catalogue isomorphism,
   rewrite neighbourhood invariant, or calibration establishes that the two
   token-disjoint packets instantiate one type. A census over admissible type
   dictionaries is unrun.

5. **Missing physical gluing fixture.** The shared-token arm needs one complete
   joint process law whose restrictions are the two local packets, plus a
   mismatch that changes a calibrated observable. Coordinate projection of a
   rational triple is insufficient.

6. **Missing full relational relabeling control.** Only one chosen basis
   permutation is checked. Cell attachment covariance under the relational
   relabeling groupoid, including a multi-cell fixture where attachments can
   differ, is unrun.

7. **Missing record/interference weld.** No composition-defect or coherent-
   eraser calculation is run on the JCV flag dilation. Thus CEL has not shown
   that its recoverable flag is the v12 record that separates the same history
   alternatives whose interference is at issue.

8. **Open-catalogue control.** A certificate for all words in a finite
   semigroup is not a certificate under later catalogue enlargement. The
   candidate correctly admits this; any absolute permanence reading is killed.

9. **Actualization control.** There is no operation or law that makes one port
   the actual record. Stinespring stacking and branchwise recovery do not fill
   that gap.

## 7. Consequence and scope reclassification

The following survive hostile reconstruction:

- two exact complete kernels with different screens, proving local
  completeness does not select recurrence;
- exact provenance distinctions among a standing naturality axiom, a declared
  history-coordinate symmetry, a coordinate restriction, and a universality
  equation;
- reset-versus-relabel separation;
- grammar-relative licensed recovery, local flag erasure, redundancy, and
  branch-retention/coarse-graining controls;
- exact same-channel/different-calibrated-port Stinespring instruments; and
- all explicit actualization, catalogue, coupling, arbitrary-`n`, steering,
  gravity, continuum, QFT, particle, Hamiltonian, constant, and phenomenology
  walls.

The following do not survive:

- one physically constructed creation-event layer;
- an independently established recurring event type across the two labs;
- a shared-token gluing theorem;
- port-independent operational-null equivalence;
- a relationally indispensable created flag cell; and
- any objective or catalogue-independent record permanence.

Within the pin's own frozen vocabulary, the strongest defensible primary is

```text
CEL-MATHEMATICAL-LADDER-CONSTRUCTED-BUT-RELATIONAL-FLAG-WELD-UNBUILT
```

with two additional restrictions: “gluing” is only a coordinate-equality
control, and “operational null” is only the registered unconditioned-channel
null unless the port/future packet is specified. The recovery qualifiers may
survive only with “licensed flag algebra” and “registered finite grammar” in
their scope.

## 8. Grade

**REJECT.**

The exact mathematics is largely sound, and the permanence section is a useful
finite construction. But the frozen primary is not licensed. The decisive
countercontrol is exact: all operator and record statistics remain unchanged
under three incompatible relational readings of the same dilation, while the
claimed attachment is never consumed by a future observable. The unit has
constructed a mathematical recurrence/recoverability/dilation interface, not
yet one relational creation-event layer. Changing to the pin's second primary
and narrowing two qualifiers requires a candidate-level rerender, not a prose
clarification.

## 9. Numbered repairs or kill conditions

1. **Replace the primary** with
   `CEL-MATHEMATICAL-LADDER-CONSTRUCTED-BUT-RELATIONAL-FLAG-WELD-UNBUILT`
   unless repair 2 succeeds.
2. **Earn the relational flag weld** in one multi-cell arena: derive a later
   calibrated probe from the output attachment/rewrite, show that erasing or
   changing the attachment moves it, and verify covariance under the full
   admitted relational relabeling groupoid. Kill the weld if the graph-erased
   model reproduces every calibrated output.
3. **Construct event-type identity before universality.** Supply an
   independently frozen catalogue/rewrite type dictionary for the two
   token-disjoint contexts, census its admissible alternatives, and then price
   kernel recurrence. Kill the universality interpretation if witness-moving
   dictionaries survive.
4. **Retype shared-token gluing.** Either call the present arm a coordinate-
   restriction control or replace it with a normalized complete joint process
   law and calibrated mismatch witness.
5. **Qualify the null.** State exactly which preparations, continuations,
   ports, and readouts are discarded. Add the retained-port counter and compute
   the continuation-stable null of the full packet before using “operational.”
6. **Correct the covariance prose.** The registered permutations flip value
   labels; they do not swap the matter and flag cell names. Add actual
   attachment covariance rather than inferring it from basis reversal.
7. **Keep permanence algebra- and grammar-relative.** Report the enlarged
   word `000/100`, the survival of source information, and the exact licensed
   flag readout that fails. Do not promote this to absolute permanence without
   a closed generative catalogue.
8. **Weld the flag record to the history alternatives.** Run the v12-style
   correlation/availability and coherent-eraser tests on the same JCV histories
   whose port the flag records.
9. **Keep actualization separate.** No repaired Stinespring or recoverability
   sentence may say that one outcome occurs unless a distinct actualization
   postulate/law is supplied.
10. **Preserve every scope wall.** Nothing in this seat licenses particles,
    fields, QFT, GR, gravity, Hamiltonian ontology, constants, arbitrary-`n`,
    conditional steering, or empirical deviations.

## 10. Report SHA-256

Normalized self-SHA-256 (computed after replacing the 64 hexadecimal
characters in the next field by 64 ASCII zeroes):

`3217d0ba85254cbf27e0de52b3179740942d352cd35210d0a3313745b1e1b553`
