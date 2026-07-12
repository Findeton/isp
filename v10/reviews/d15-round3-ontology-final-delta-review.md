# D15 final ontology/physics delta review — round 3

**Date:** 2026-07-11  
**Review verdict:** **PASS FOR THE FINAL NARROWED DELTA**  
**Formal D15 verdict retained:** **`INCOMPLETE-INVESTIGATION`**

## Result

The final 28-check delta is correct and remains inside the scope approved in
round 2.

The D14 dictionary is now explicitly confined to one owned component.  The
system, environment, protected record and live collar ports all carry owner
`cell-A`.  The exact receipt checks the composed source and target ownership,
and source inspection confirms that the intermediate environment port carries
the same owner.  No multi-owner interaction or cross-component join is used.

The protected-record claim is also hardened.  A direct X flip on the sealed
record register is passed to the actual D14 `Mor` constructor and rejected.
Thus persistence is not only inferred from the chosen later system action;
the forbidden rewrite fails admission.

The memory cell is now assembled from the same exact two-bit CNOT kernel used
by the action dictionary.  Two embeddings store X in hidden M and later copy M
to Z.  The resulting finite visible law has

```text
P(Z=1 | X=1,Y=0)=1,
P(Z=1 | X=0,Y=0)=0.
```

This closes the provenance gap between the regulated CNOT constraint weight
and the prior memory helper.

Finally, the working theorem prints the exact regulator and gauge ledger for
this witness: a finite binary sum is the regulator, gauge group and quotient
are trivial, boundary basis and normalization are fixed, every port has one
owner, no join is exercised, and all phases are dimensionless.  It explicitly
denies a metre/second/`G` bridge and denies that the witness discretizes EFT4
or gravity.

No new ontology or physics blocker is introduced.  The explicit commit,
environment state, system/environment split, pointer basis/coarse graining
and collar emission remain supplied, so S5 is still conditional.  General
covariance, gravity, S6 diagram generation/joining and the frozen empirical
selection ledger remain open.  The formal D15 verdict therefore correctly
stays incomplete.

## Exact reproduction

The final D15 source and frozen D13/D14 dependencies were copied to an isolated
temporary tree.  Normal and optimized execution did not modify the primary
packet.

```text
checks                         = 28/28
normal stdout SHA-256          = 06c5ab5d6455942e14835814914a57f0cc6dad4a4f30997bc504d04153446408
-O stdout SHA-256              = 06c5ab5d6455942e14835814914a57f0cc6dad4a4f30997bc504d04153446408
generated JSON SHA-256         = b9bc2fc3a2c8dc9342d985df55f2298db182e8cf0a0e97fc22fd8de5fa2d3b41
primary JSON SHA-256           = b9bc2fc3a2c8dc9342d985df55f2298db182e8cf0a0e97fc22fd8de5fa2d3b41
semantic SHA-256               = 12f73918e7876a2f423d1d4596163e787f52ac50332f2d59bb941c0381f499fe
source SHA-256                 = 9f539129d5712d28b86d89637248a0fe3b60678fcc29fcddf2e5e675aa8fb4b9
D13 dependency SHA-256         = 1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45
D14 dependency SHA-256         = e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425
normal/-O stdout               = byte-identical
generated/primary JSON         = byte-identical
```

The receipt and packet hashes agree with the frozen pre-review receipt.

## Ownership confinement

`d14_seal_from_action()` declares:

```text
system       owner=cell-A
environment  owner=cell-A
record       owner=cell-A, sealed, record_id=R
collar       owner=cell-A.
```

The primitive chain is therefore:

```text
cell-A system
  -> cell-A system + cell-A environment
  -> cell-A CNOT interaction
  -> cell-A system + cell-A protected record
  -> cell-A system + record + collar.
```

Every primitive source is either a single owner or a one-component tensor
word.  D14's primitive admission sees no ownerless mixing and no multi-owner
join.  The explicit check confirms all ports visible at the composite boundary
are `cell-A`; the definitions confirm the same for the internal environment.

This proves confinement for the finite cell.  It does not derive an
entitlement between distinct components or close S6, and the note says no
cross-component join is exercised.

## Protected overwrite control

The forbidden map is

```text
I_system tensor X_record tensor I_collar.
```

It has the correct dimensions and source/target object, so rejection is not a
shape mismatch.  D14 inspects the nonzero entries against the persistent
sealed correspondence and raises on the record-label change.  The exact check
therefore establishes constructor-level protection for the D15 record.

The accepted future remains

```text
H_system tensor I_record tensor I_collar,
```

which composes and preserves the record marginal.  Together the positive and
negative cells support the narrow permanence claim.

Protection is still a supplied D14 algebraic rule.  The action does not derive
why nature forbids all future record rewrites; this is part of the retained S5
conditional ceiling.

## Same-action memory provenance

The repaired `cnot_four(two_bit_kernel,control,target)` embeds the supplied
two-bit matrix into the declared pair of a four-bit carrier.  The memory unitary
is composed as

```text
CNOT(X -> M)
then CNOT(M -> Z),
```

using the same `cnot` returned by the finite `Z2` multiplier sum.  It is not an
imported helper with separate provenance.

The input is the equal mixture of X=0 and X=1 with M=Y=Z=0.  Exact evolution
leaves mass `1/2` on `0000` and `1101`; hence the two finite conditionals are
one and zero.  The denominators are nonzero and the source additionally checks
the unitary identity.

This remains a compatibility witness, not an autonomous full-history law or
a proof that arbitrary non-Markov processes have bounded memory.

## Regulator, gauge and scale ledger

**PASS as a trivial-cell declaration.**

The note now states every relevant field:

| Field | Finite witness status |
|---|---|
| regulator | complete printed finite binary boundary/history sum |
| gauge group/quotient | trivial |
| boundary basis | fixed binary basis |
| vertex measure | supplied fixed normalization |
| ownership | one component, `cell-A` |
| join | none exercised |
| action phase | dimensionless |
| continuum limit | absent |
| general covariance/gravity | absent |
| metre/second/`G` bridge | absent |

This is the correct way to close the finite receipt ledger without pretending
the toy has gauge fixing, gravitational covariance or physical units.  The
continuum EFT4 regional integral and any gravity dictionary remain separate
open tasks.

## S5 and formal-status check

The delta does not change the record-ontology grade:

```text
CNOT correlation and reduced decoherence             derived conditionally
fresh |0> environment                                 supplied
system/environment split                              supplied
computational pointer interaction/basis               supplied
partial trace/coarse graining                         supplied
environment -> protected-record commit                explicit primitive
live-collar emission                                  explicit primitive
universal autonomous seal instrument                  not derived
```

The working theorem explicitly calls the cell a conditional
environment-decoherence instance of S5 and retains
`INCOMPLETE-INVESTIGATION`.  No text promotes the new flip or memory checks
into autonomous universe record formation.

## Delta gate adjudication

| Delta | Result |
|---|---|
| one-owner D14 confinement | **PASS.** All system/environment/record/collar ports are `cell-A`. |
| multi-component entitlement claim | **NOT MADE.** No join is exercised; S6 remains open. |
| protected-record negative control | **PASS.** Direct record flip fails D14 construction. |
| same-CNOT memory derivation | **PASS.** Embedded multiplier-derived CNOT gives exact `1/0` conditionals. |
| trivial regulator/gauge ledger | **PASS at declared finite scope.** |
| dimensionful scale/gravity inference | **NONE; explicitly denied.** |
| S5 autonomous record derivation | **CONDITIONAL/OPEN, correctly.** |
| formal D15 verdict | **`INCOMPLETE-INVESTIGATION`, correctly retained.** |

## Final verdict

**PASS FOR THE FINAL NARROWED DELTA.**  The 28/28 packet reproduces exactly;
single-component ownership, constructor-level overwrite rejection, and
same-CNOT memory provenance are real.  The regulator/gauge/no-join/scale ledger
is complete for the toy and does not overstate its physics.

The accepted result remains a finite nongravitational action-weight-to-D14
dictionary with a supplied environment/commit packet.  It is not an autonomous
record law, a generally covariant gravity action, a cross-component generation
law or a fundamental selector.  Formal D15 properly remains incomplete.
