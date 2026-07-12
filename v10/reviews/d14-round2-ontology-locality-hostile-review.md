# D14 hostile ontology/locality review — round 2

**Date:** 2026-07-11  
**Review verdict:** **MAJOR REPAIR STILL REQUIRED — `INCOMPLETE-INVESTIGATION`**  
**Conditional bridge core:** **SUBSTANTIALLY SUPPORTED**

## Executive finding

Round 1 produced a real scientific repair, not a cosmetic downgrade.

The executable now builds sequential record seals, integrates projective
cylinders with the finite hidden-memory process, executes a complete CPTP
memory-deletion control, rejects the tested record flip at construction,
requires a collar for the declared continuation, and distinguishes
unconditional marginal permanence from postselection.  Paper 15 now says
that evaluation order is gauge only for a supplied DAG, that diagram
generation is open, that the record instrument is supplied, that finite
memory does not implement arbitrary full-history or Barandes dynamics, and
that no V9 geometry holdout is licensed.  The exact 39-check receipt
reproduces byte-for-byte.

Two category-level defects nevertheless prevent a round-2 pass.

1. **Protected-record admission is incompatible with the advertised
   symmetric-monoidal category.**  The constructor tracks sealed registers by
   positional `zip`, not persistent wire identity.  The category's own
   symmetry on two protected record wires is rejected as an overwrite, while
   changing the owners of those wires without moving their values is
   accepted.  Thus protection is neither invariant under structural wire
   permutation nor ownership-safe.
2. **Join admission is not enforced on the morphism class and the real packet
   is ownerless.**  `Signature.declare` rejects the tested two-owner join, but
   direct `Mor(...)` construction admits the same unentitled join.  An owned
   port can also join an ownerless port without entitlement, and the seal
   collar plus integrated memory packet use no owners at all.  The string
   tuple called an entitlement is honestly declared primitive, but it is not
   a connected-collar capability whose provenance is checked.

These are not objections to the abstract universal property of a free strict
symmetric-monoidal category.  They show that the executable's **protected and
owned subcategory** has not yet been defined coherently.  Because B0/B1 and
the round-1 ownership repair depend on exactly that claim, the formal verdict
must remain `INCOMPLETE-INVESTIGATION`.

At the claim level, the construction-order repair is nearly complete.  The
abstract, theorem note and dedicated section now use the correct
“evaluation-schedule gauge for one supplied DAG” language.  Three isolated
sentences still say that a regional action “generates” records, that no global
physical commit order is required, or that the result is “clock-free.”  They
should inherit the supplied-DAG/supplied-instrument qualifier, but this is a
wording repair rather than a new mathematical blocker.

## Independent reproduction

The repaired source and its reviewed arithmetic dependency were copied to an
isolated temporary tree.  Normal and optimized Python were run without
modifying the primary packet.

```text
checks                         = 39/39
normal stdout SHA-256          = 99e51861cf472bdfea9dad570e7a6663d112b5704425db80609eaa65aceea20b
-O stdout SHA-256              = 99e51861cf472bdfea9dad570e7a6663d112b5704425db80609eaa65aceea20b
generated JSON SHA-256         = 70f552bf3f9d962029d1a48dff20159f170a8e10f971c15e9ef54bdb5865ab22
primary JSON SHA-256           = 70f552bf3f9d962029d1a48dff20159f170a8e10f971c15e9ef54bdb5865ab22
semantic SHA-256               = 6bead748846c5b33995212ac03576e30c2ed17e6689570a4e1c4119072637ea3
source SHA-256                 = abf7e4d2e4638e4a8f4e545e9a21fe77cb5dbfceb86eb7ef366a8b0d165b514d
dependency SHA-256             = 1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45
normal/-O stdout               = byte-identical
generated/primary JSON         = byte-identical
```

The new semantic verdict is appropriately narrower:

```text
FINITE-REGIONAL-AMPLITUDE-TO-RECORDED-HISTORY-CORE-PASSED.
```

It no longer prints the round-1 action-level positive verdict.

## Round-1 opening closure ledger

| Round-1 opening | Round-2 adjudication |
|---|---|
| evaluation order promoted to generative construction order | **SUBSTANTIALLY CLOSED.** The main theorem is fixed-DAG evaluation gauge; three residual headline sentences need synchronization. |
| overwrite merely diagnosed after construction | **CLOSED for the tested fixed-position record flip; NOT CLOSED for record identity under symmetry/owner permutation.** |
| block support equated with probability permanence | **CLOSED.** Direct-sum CPTP/isometry and sectorwise completeness are now required; postselection is separated. |
| live collar only a basis label | **CLOSED for the declared continuation.** Live composes, omission is ill-typed, dead has zero amplitude.  The grammar remains supplied. |
| disconnected joins silently admitted | **NOT CLOSED.** Signature-level owner-list checking exists, but `Mor` bypasses it and ownerless ports evade it. |
| history strings appended only after history | **CLOSED.** Sequential local copy/seal isometries reproduce the depth-1–3 cylinders exactly. |
| projectivity and memory shown in separate cells | **CLOSED.** One packet carries X into memory, seals X/Y/Z and is projective. |
| memory-deletion control absent | **CLOSED.** An exact complete CPTP reset changes the visible law and removes dependence. |
| finite witness generalized to arbitrary full history/Barandes | **CLOSED.** The claim is finite compatibility; growing memory and Barandes realization remain open. |
| no-signalling overread | **CLOSED in the main scope section.** One Bell/local-unitary marginal plus interchange only. |
| `SL(2,C)` cell called Lorentz seed | **CLOSED.** It is one positive-cone dual-pairing cell, not emergent Lorentz geometry. |
| action-to-record headline exceeded supplied inputs | **CLOSED in title, abstract, theorem and verdict; one motivational sentence remains.** |
| B10/B11/V9 ceiling | **PASS.** Primitive packet and missing dictionary remain explicit; holdout remains refused. |

## Blocker 1 — record protection is not symmetric-monoidal

### The implementation

For a morphism with sealed source ports, `Mor.__post_init__` gathers the source
and target sealed positions and pairs them by

```text
zip(source_sealed, target_sealed).
```

It checks matching `kind` and `dim` and demands equal basis labels at each
paired position.  It does not carry a persistent record/wire identifier or an
explicit source-to-target correspondence.  `owner` is ignored by this check.

That works for the receipt's append-at-the-end and fixed-position operations.
It is not stable under the symmetry morphisms required by `FSDiam`.

### Exact hostile probes

Let `R_A` and `R_B` be two sealed two-level record ports with the same kind
and different owners.  The structural symmetry should implement

```text
|a>_A |b>_B -> |b>_B |a>_A
```

while preserving both records.  The executable instead gives:

```text
protected_record_symmetry= rejected:protected record overwrite
```

Conversely, use target word `(R_B,R_A)` but the identity matrix, which leaves
the numerical labels in their old positions and therefore associates them
with the opposite owners.  The constructor gives:

```text
owner_swap_identity_constructed= True
```

So a correct structural wire swap is rejected, while a semantic owner swap is
accepted.  The current record predicate is positional, not identity
preserving.

The problem also appears whenever a generator inserts a new sealed port
before an existing one or permutes several same-typed records.  The ordered
lists alone cannot distinguish old from new records.

### Why this blocks B0/B1

Paper 15 and the theorem claim both:

```text
free strict symmetric-monoidal category with permutation symmetries;
protected records closed under licensed morphisms.
```

The matrix image tests symmetry only on two unsealed `q` wires.  It tests
record closure only in fixed-position composition/tensor cells.  Those two
successful tests do not prove their conjunction.  The advertised protected
subcategory presently lacks its structural symmetry, so the executable is
not yet a model of the full claimed protected `FSDiam` class.

### Required repair

Add stable port/record identities and require every morphism to carry an
explicit injective correspondence from each sealed input identity to its
sealed output identity.  Structural permutation should transport identities
with wires.  Fresh records must have fresh identities.  Owner changes must be
forbidden unless a separately typed ownership-transfer rule exists.

Then execute at least:

```text
swap(R_A,R_B) admitted and preserves A/B values;
swap twice = identity;
identity matrix with target owners exchanged rejected;
append fresh R_C before and after existing records preserves A/B;
composition/tensor/symmetry preserve the protection certificate.
```

## Blocker 2 — ownership admission has a bypass and an ownerless loophole

### What the repair added

`Signature.declare` collects the distinct non-null owners of a primitive
source.  If there is more than one, it requires the supplied
`join_entitlement` tuple to equal that owner set.  The intended test rejects
owners `A+B` without the tuple and admits them with `("A","B")`.

This is a useful declaration-layer check.  The paper is also honest that the
physical origin of the entitlement is not derived.

### What remains

The restriction is not part of `Mor`.  The same two-owner matrix can be
constructed directly:

```text
direct_unowned_join_constructed= True
```

This is not a merely hypothetical API path: most primitive matrices in the
receipt are themselves created directly as `Mor`, not declared through
`Signature`.  The code does not define a raw matrix layer that is formally
excluded from the source signature.

The owner set also ignores `None`.  One owned and one ownerless input therefore
join without an entitlement:

```text
owned_plus_unowned_constructed= True
```

Most importantly, the actual seal collar is declared as

```text
Port("collar",2)
```

with no owner.  The X/M/Y/Z carriers and integrated memory packet are also
ownerless.  Thus the new owner gate is a separate toy cell; it does not certify
the locality of the record/birth/history packet described as local in the
paper.

### Entitlement origin and honest scope

The tuple `("A","B")` names owners.  It does not prove that a previously
recorded connected collar owns both legs, as required by D12 U6.  Any caller
may supply the strings.  The error message and receipt label call this a
“connected join entitlement,” but connectedness is not checked.

The prose correctly says the origin law is open.  At the narrowed
`BRIDGE-CONDITIONAL` scope, an entitlement may be supplied as primitive
grammar data.  The executable must then call it a **declared owner-list
entitlement**, not a derived connected collar, and enforce that declaration
on every primitive generator.

### Required repair

Choose and implement one admission boundary:

```text
RawLinearMap                         unrestricted matrix
Signature.declare(...) -> Generator only admitted primitive
FSDiam morphisms                     composites/tensors/symmetries of admitted generators
```

Make direct construction of an admitted `Mor` impossible, or put the owner
check into `Mor` with a non-forgeable certificate field.  Require every live
or joinable port to have an owner; `None` must not silently count as outside
the component ledger.  Run the seal, live continuation and integrated memory
packet with owned carriers.  Add controls for:

```text
direct two-owner bypass rejected;
owned + ownerless join rejected;
wrong/missing owner tuple rejected;
declared entitlement admitted;
actual owned collar continuation admitted.
```

Deriving a connected-collar entitlement from the action remains outside D14
and should stay in B10/B11.

## Evaluation-schedule gauge

**PASS in the theorem note and dedicated section; residual wording repair.**

The repaired formal statement is exact:

```text
For one supplied finite DAG, topological contraction schedules give the same
matrix.  D14 does not generate the DAG, choose among DAGs or derive a local
next-extension law.
```

Paper 15 now explicitly says a whole-history approach avoids sequential
commit order only after an amplitude/measure over alternative complete
diagrams is supplied.  Proper time is only analogy.  This closes the main
round-1 overclaim.

Three isolated phrases should still be synchronized:

- section 1 asks whether an action/amplitude can “generate the record picture”
  and answers yes, although the instrument is supplied;
- section 11 ends “No global physical commit order is required” without the
  fixed-supplied-DAG qualifier; and
- the final schematic arrow calls the result “CLOCK-FREE” rather than
  “EVALUATION-SCHEDULE-INDEPENDENT FOR A SUPPLIED DAG.”

None overrides the detailed caveats, but the theorem headline should be safe
when quoted alone.  Use:

```text
No preferred total contraction order is required to evaluate or accumulate
records within a supplied FSDiam DAG.  D14 proves no generative clock theorem.
```

## Record instrument, permanence and action ceiling

**PASS at conditional scope.**

The CPTP repair is correct.  For

```math
M_k=\sum_r |r\rangle\langle r|\otimes M_{r,k},
\qquad \sum_k M_{r,k}^\dagger M_{r,k}=I,
```

the unconditional probability of every old record sector is preserved.
Conditioning on a future outcome may update the inferred probability without
rewriting the stored label.  Arbitrary block-diagonal filters are explicitly
excluded.  This closes the round-1 probability-permanence error.

The title, abstract, theorem and executable verdict now say regional
amplitudes **plus supplied instruments** produce recorded histories.  The
autonomous action/environment-to-record-instrument map remains open.  This is
exactly the distinction between:

```text
conditional action/instrument-to-history translation
and
empirical or theoretical action selection.
```

D14 does not claim to select fields, kernels, couplings, state, pointer basis,
protected algebra or scales.  The remaining motivational sentence noted above
is a local wording inconsistency, not a failure of the repaired ceiling.

## Sequential history, integrated memory and Barandes scope

**PASS.**

The repair now executes the missing integrated construction.

- `local_record_history_network` evolves the live qubit and locally copies its
  value into a fresh protected record at each depth.
- The resulting depth-1–3 branch masses agree exactly with the class-operator
  cylinders.
- Orthogonal protected strings make the record-extended functional diagonal;
  the bare system functional is explicitly distinguished.
- The integrated X/M/Y/Z network stores X, seals X, seals common Y=0, reveals
  memory into Z and seals Z.
- Its nonzero depth-three histories are `000` and `101`, each with probability
  `1/2`, and its depth-1–3 tables are projective.
- The two reset Kraus maps satisfy exact completeness.  Resetting memory makes
  both relevant Z=1 conditionals zero and therefore changes the visible law.

This genuinely proves one finite projective non-Markov recorded process, not
just two disconnected examples.

The Barandes/Egri ceiling is now honest.  The paper says neither that arbitrary
full-history laws have bounded local memory nor that the cell derives a
Barandes indivisible process or selects a path measure.  A general process may
need a growing boundary carrier.  Disintegration remains conditional on an
already constructed/supplied projective history measure.

The word “local” in the integrated-packet label should remain operational
rather than SHARD-geometric until Blocker 2 is fixed: the actual carriers have
no ownership data.

## No-signalling and `SL(2,C)` scope

**PASS.**

Section 9 now states exactly what the receipt proves: disjoint unitary
interchange and one Bell-state marginal under a local Hadamard.  It denies a
class-wide theorem for arbitrary linear kernels/multi-input generators and
does not infer microcausality, a propagation speed or relativistic causal
structure.

The positive-cone section is likewise narrowed.  It presents the exact
`diag(2,1/2)` dual state/effect pairing and positive-cone preservation as one
cell.  It expressly denies a smooth Lorentz metric, round cone or `3+1`
dimension.  No broader covariance claim is smuggled into the gate ledger.

The abstract phrase “all microscopic composition remains local in that finite
packet” would be safer as “the displayed memory operations act on the carried
finite system,” especially while ownership remains unresolved.  The dedicated
scope section is otherwise correct.

## B10, B11 and V9

**PASS.**

B10 remains explicit that the following are supplied:

```text
carriers/types;
allowed grammar and ownership declarations;
local kernels;
boundary state;
record instrument and pointer basis;
protected future algebra;
frame/pairing rule;
dimensionful unit bridge.
```

The join entitlement and live-collar grammar must be added visibly to that
list, but the paper already treats them as grammar inputs rather than physical
derivations.

B11 still gives the correct downstream dictionary from physical
action/state, through carriers/kernels and an autonomous record instrument,
to record adjacency/influence observables and proper-unit calibration.  Gauge
and gravity boundary data remain open.

The V9 holdout refusal is therefore correct.  The repaired bridge has not
selected a physical action, derived the record-web map, or predicted cone
shape/dimension.  D9's conditional partial-iSWAP angle and failed geometry map
do not change this gate.

## Gate adjudication

| Gate | Round-2 result |
|---|---|
| B0 typed/protected category | **FAIL/PARTIAL.** Fixed-position overwrite is rejected; persistent identity under symmetry and enforced ownership are not. |
| B1 category/coherence | **PASS for unsealed matrix cells; FAIL for symmetry closure of protected records.** |
| B2 construction-order gauge | **PASS only as evaluation-schedule gauge for a supplied DAG; three wording repairs remain.** |
| B3 coherent gluing | **PASS at exact finite scope.** |
| B4 frame/positive-cone pairing | **PASS at unitary internal-frame plus one `SL(2,C)` pairing-cell scope.** |
| B5 records and birth | **PASS for tested seal, repeat-read, CPTP permanence and declared collar continuation; owner-integrated birth remains blocked by B0.** |
| B6 recorded decoherence | **PASS for sequential orthogonal record seals; bare and extended functionals distinguished.** |
| B7 projective law | **PASS for finite cylinders plus the stated completeness induction.** |
| B8 finite visible non-Markov memory | **PASS, including integrated packet and CPTP deletion control.** |
| B9 locality/no-signalling | **PASS for the one finite unitary witness only; ownership locality not passed.** |
| B10 action scope | **PASS at `BRIDGE-CONDITIONAL` ceiling.** |
| B11 downstream handoff | **PASS; V9 correctly withheld.** |
| B12 hostile closure | **OPEN because B0/B1 ownership/protection blockers remain.** |

## Required round-2 repair set

1. Replace positional protected-record pairing with persistent identities and
   explicit transport maps.
2. Execute protected-record symmetry, double symmetry, owner-swap rejection
   and fresh-record insertion controls.
3. Make `Signature` the only primitive-generator admission path, or enforce
   entitlement in every `Mor` constructor.
4. Require owners on all live/joinable ports and reject owned-plus-ownerless
   joins.
5. Run the seal/collar/integrated-memory witness with those owned ports.
6. Rename the string tuple a declared owner-list entitlement unless a typed
   connected-collar capability with provenance is implemented.
7. Synchronize the three residual global-clock/action-generation phrases.

## Verdict

The round-1 repairs close the scientific-scope problems around CPTP
permanence, sequential records, integrated non-Markov memory, Barandes,
no-signalling, `SL(2,C)`, action selection and V9 refusal.  The executable
core is exact and reproducible.

The protected/owned source category is not yet coherent: it rejects a valid
record-wire symmetry, accepts an owner reassignment, and permits unentitled
joins through direct or ownerless paths.  Those exact counterexamples keep B0,
B1 and B12 open.

The current honest status is:

```text
FINITE REGIONAL AMPLITUDE/INSTRUMENT HISTORY CORE       PASSED
SEQUENTIAL PROJECTIVE RECORDED HISTORY                  PASSED
FINITE NON-MARKOV MEMORY + CPTP DELETION                PASSED
FIXED-DAG EVALUATION-SCHEDULE GAUGE                      PASSED
PROTECTED SYMMETRIC-MONOIDAL SUBCATEGORY                NOT YET PASSED
OWNED/COLLAR-GATED INTERACTION SUBCATEGORY               NOT YET PASSED
ACTION/INSTRUMENT/DIAGRAM GENERATION                     OPEN
ACTION SELECTION AND V9 GEOMETRY                         OPEN/WITHHELD
PROTOCOL VERDICT                                         INCOMPLETE-INVESTIGATION
```

Once the two admission defects and the residual wording are repaired, a
`BRIDGE-CONDITIONAL` pass would be warranted.  That verdict must continue to
mean a supplied finite grammar/kernel/instrument bridge, not the final
interactive click law.
