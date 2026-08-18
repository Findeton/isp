# CSF hostile review — records, representation, and recurring-history identity

Seat: **R — records, representation, and recurring-history identity**  
Target: Paper 6 candidate commit
`61c32d884d688f49f29d3863fe5959d1053d382e`  
Protocol: `v16/note-csf-hostile-protocol.md`  
Review mode: repository read-only except this assigned report; independent
exact reconstruction in `/private/tmp`; no candidate implementation imported
into the reconstruction  
Grade: **REJECT**

## 1. Immutable-target and hash audit

I read the complete runbook and frozen CSF protocol before starting this seat,
then read the pin, generic-core freeze, fixture/refusal/repair freeze,
verification note, full core and scorer, fixture, transcript, receipt, Paper
6, and the relevant JCV/PPR/SRW/OVG antecedents. I did not consult either
other CSF review.

The immutable target re-hashes exactly:

| object | protocol SHA-256 | reviewer SHA-256 | status |
|---|---|---|---|
| pin | `c953618c66685b20705bef7436ebfa29d4b0370b076493bc1997aea898e1bcba` | same | PASS |
| core-freeze note | `60fc2c5b2174631f33bdb946e6b6c051cac533d9dbbe9fcbbde885d578d4068a` | same | PASS |
| generic core | `93a093d6ce72be4167d277719daf37aa7df7704510819f3b2e264546a14362b4` | same | PASS |
| fixture | `8c10210b6fee0a5477f3f70593cca080c26a4c91d678ad60bf691f6d853fbd37` | same | PASS |
| repaired scorer | `d3adf994e1c89fca5b53a0969cf0eed256488790b361477116b7cd1a76da84ba` | same | PASS |
| freeze/refusal/repair record | `b2a140a123cab91fe1aba19a87aa2ee9d9c09c97992260338123b3bd7be1ddf1` | same | PASS |
| transcript | `59077d8ad0f9e9ba4cf5afc0a44fea242d7a6032f1d998e088b3433cf4541785` | same | PASS |
| receipt | `7ae9b4a17fd38883bbff39b212f0edf819e2edf17942c9d54f8cf9f772414fdc` | same | PASS |
| Paper 6 | `543a2c927ecc7bd184fc758e4d72ebd4d4974327ae5ae2bb279d1fe33086c5d9` | same | PASS |
| candidate verification | `c0b3e7072ae2ba5a5fe45e1a26c988d36fe989b33cb02e71e57490db077b7cd5` | same | PASS |

The #63 first invocation honestly refused before artifact creation because the
anchor requested `erasable` while the antecedent contained `eraser`. The #64
repair changes exactly that token and none of the physical construction.

A clean replay to fresh `/private/tmp` paths reproduced output, receipt, and
paper byte-for-byte. The receipt has 30 unique passing gates, eight total
payload seals, 36 registered mutants, and twelve one-occurrence claims. I
reran fifteen records/recurrence mutants; each refused at its registered gate
without result artifacts. The `seal-after-write` control was caught by the
final promotion seal, not after disk write.

The exact process is sound. The primary classifier is not protected from a
bad physical referent merely because its shallow `typed` predicate passed.

## 2. Independent method and tools

I reconstructed the context constraints, recurrence intersection, calibrated
port fiber, and flag/eraser controls in
`/private/tmp/csf_records_independent.py`, using only rational arithmetic and
an independent row-reduction routine. No CSF source or receipt is imported.

For a Hermitian two-history kernel

```text
M = [[p, r+i s],
     [r-i s, q]],
```

and an eigenphase `lambda=a+i b` of the relative history operator, the
completeness row is

```text
p + q + 2 a r - 2 b s = 1.
```

This supplies every context equation directly. I then:

1. row-reduced each context and the stacked training systems;
2. compared row spaces of training and held-out controls;
3. distinguished quotienting an exchange label from imposing exchange
   invariance as a physical law symmetry;
4. reconstructed both `C` factorizations and their retained-port screens;
5. computed the three flag overlaps and the reconvergence map; and
6. audited the source-level construction of history coordinates, recurrence
   dictionaries, and doctrine-control “predictions.”

## 3. Exact recomputation table

| item | candidate value | reviewer value | status |
|---|---|---|---|
| `phase-sign` affine dimension | 2 | 2 | PASS |
| `quarter-sign` affine dimension | 2 | 2 | PASS |
| `rich-three` affine dimension | 1 | 1 | PASS |
| `held-rich` affine dimension | 1 | 1 | PASS |
| `left-calibrated` affine dimension | 2 | 2 | PASS |
| separate training dimension | 5 | `2+2+1=5` | PASS, sum of independent spaces |
| identity-recurrence intersection | 1 | 1 | PASS, conditional on full coordinate equality |
| exchange-fixed dimension | 0 | 0 | PASS, conditional on invariance equation |
| selected kernel | `diag(1/2,1/2)` | same | PASS |
| held-out adds independent rank | not reported | `0` | NEW: algebraically redundant |
| asymmetric control adds independent rank | not reported | `0` | NEW: same completeness rows as `phase-sign` |
| parity/rotated kernels | both `diag(1/2,1/2)` | same | PASS |
| retained port-zero screens | `1`, `9/25` | `1`, `9/25` | PASS |
| flag overlaps | `1,3/5,0` | same | PASS |
| reconverged overlap | `1` | `1` | PASS |
| configuration-individuated histories | gate says typed | not constructed | FAIL |
| recurrence dictionary selected by physical fact | gate says frozen/covariant | identity recurrence is a universality postulate | FAIL |
| doctrine-control polynomials | `[1,0]`, `[0,1]` | literal source constants, no probe derivation | FAIL |

The context row spaces are transparent:

```text
phase-sign:   p+q=1, r=0; s free
quarter-sign: p+q=1, s=0; r free
rich-three:   p+q=1, r=s=0; p-q free
held-rich:    p+q=1, r=s=0; p-q free
left-calibrated: p+q=1, r=0; s free
```

Stacking the first three leaves the diagonal trace-one line

```text
M(t)=diag(t,1-t), 0<=t<=1.
```

Imposing `X M X=M` then gives `t=1/2`. The arithmetic is exact. The
interpretation of those two operations is the disputed point.

## 4. Theorem and proof audit

### 4.1 Fixed-history spectrahedra and calibrated ports

The kernel/fiber separation is the strongest surviving result of the unit.
At fixed, already typed histories, `M=C^dagger C` determines both all-input
completeness and the unconditioned channel, while retained output maps depend
on `C`. The exact JCV and selected-kernel factorizations verify that distinction.

The selected-kernel pair is

```text
C  = [[ 1/2,  1/2],
      [ 1/2, -1/2]],

C' = [[ 7/10, -1/10],
      [-1/10, -7/10]].
```

Both have `C^dagger C=I/2`. For histories `I,Z` and preparation `|0>`, the
first retained-port amplitude is the row sum, hence probabilities `1` and
`(3/5)^2=9/25`. Ignoring ports gives the same channel; retaining a fixed
apparatus calibration gives two different instruments.

This is a theorem about fixed operator histories and calibrated instruments.
It does not establish record permanence, actualization, or the physical
identity of those history coordinates across contexts.

### 4.2 The recurrence cut is exact but postulated

The number `5` is the sum of dimensions of three independent law spaces. The
number `1` is obtained by writing all three kernels in one common coordinate
packet `(p,q,r,s)` and requiring the packet to be identical. That is not a
consequence of the local completeness equations. It is precisely the
recurring-history universality postulate.

The contexts use disjoint actor names (`a0,b0,c0`, `a1,b1,c1`, and so on),
different carrier dimensions, and independently supplied relative operators.
No shared event token, gluing arena, transport of a local coupling, or
successor rewrite connects them. Thus the honest physical reading is:

```text
5 -> 1 : price of declaring one full kernel packet universal
1 -> 0 : price of declaring endpoint exchange a law symmetry
```

Neither arrow is “modulo gauge” selection. The first is nomological
identification; the second is a fixed-point restriction under a physical
symmetry assumption.

### 4.3 Exchange quotient and exchange invariance are different operations

On the surviving line, endpoint exchange sends

```text
M(t) -> M(1-t).
```

If exchange is only a coordinate gauge, the physical quotient identifies
`t` with `1-t` and leaves a continuum of orbits. It does **not** select
`t=1/2`. If the physical context is postulated to obey the endpoint-reflection
symmetry, then the law must be fixed and `t=1/2` follows.

The scorer performs the second operation by stacking `X^dagger M X-M=0`.
Calling the resulting point `SELECTED-MODULO-GAUGE` conflates it with the
first. Paper 6 partly corrects this by saying “conditional on exchange
symmetry,” but the primary string remains stronger than its proof.

The relational path graph does have an endpoint-reflection automorphism when
its calibration is marked symmetric. That licenses the **question**. It does
not derive symmetry of the process law. In particular, the scorer checks only
the relation-pair set and a calibration string; it does not show that the
relative history operators or their elementary events are transported by the
same automorphism. `rich-three` is taken to its conjugate `held-rich` under
history exchange, rather than proved internally invariant.

### 4.4 The held-out check is vacuous at the affine-law level

The `rich-three` and `held-rich` systems have the same row span:

```text
p+q=1, r=0, s=0.
```

Adding the held-out rows to the full training stack raises the exact rank by
zero. Consequently every kernel surviving `rich-three` already passes
`held-rich`; the selected half-half point could not fail it. The held-out
label is procedurally honest—it was not put in the fit—but algebraically it is
not a new prediction.

Likewise `left-calibrated` has the same completeness equations as
`phase-sign`. Its external calibration forbids endpoint exchange, which is a
useful semantic control, but its `heldout_complete` check adds no operator
constraint.

### 4.5 The doctrine-control gate is not a computation

The scorer literally assigns

```text
doctrine_prediction_polynomials = {
    "identity": [1,0],
    "asymmetric_exchange": [0,1]
}
```

and defines movement by inequality of those two arrays. No history map,
kernel, preparation, port factorization, calibrated readout, or graph-derived
probe produces them. The fixture does not contain the polynomials. Therefore
`CSF-DOCTRINE-CONTROL` is a declaration-only gate, and
`RECURRENCE-DOCTRINE-MOVES-PHYSICS` is not an earned machine finding.

A genuine replacement would construct two admissible recurrence doctrines,
solve each, and evaluate the same predeclared gauge-invariant calibrated
observable. The present unit shows that imposing recurrence changes the
dimension of the law space; it does not measure a held-out physical screen
that moves between doctrines.

## 5. Recurrence, gauge, history identity, and records

### 5.1 The history coordinates are names, not configuration-individuated
histories

For every context, the scorer builds

```text
(V_0,V_1)=(I,Omega_context)
```

from the supplied relative operator. It never constructs the two elementary
neighbor events, never composes `left-then-right` or `right-then-left`, and
never binds a basis state to a complete relational configuration. The
`CSF-HISTORY-INDIVIDUATION` gate checks only:

- the two coordinate strings have the expected names;
- there are five contexts;
- each context has three actors and two relation pairs; and
- each supplied relative operator is unitary.

Those checks do not meet the pin's own definition of a “record-individuated
complete-history operator.” The two histories are anonymous operator
coordinates decorated with relational roles. They inherit Paper 5's fixed-
carrier order representation, not Paper 3's record-derived event algebra or
Paper 4's rewrite/transport bundle.

Strictly applying the pre-registered decision order should therefore stop at

```text
CSF-BLOCKED-AT-HISTORY-INDIVIDUATION.
```

If adjudication instead accepts declared names as a provisional finite
typing, every recurrence result must remain explicitly conditional on that
declaration.

### 5.2 Classification of the recurrence dictionary

The four declared map types are not one kind of object:

| map | correct type |
|---|---|
| `event-identity` across all five contexts | new universality/recurrence postulate; not gauge and not derived |
| `quarter-rephase` | coordinate/boundary gauge when histories and kernel transform together; channel invariant |
| `held-exchange` | comparison under an endpoint-reflection automorphism, conditional on physical calibration and transport covariance |
| `asymmetric-exchange` | deliberately non-gauge because it moves the retained source calibration |

At two history coordinates, the admitted representation group is monomial:
independent history rephasings and, in symmetric contexts, endpoint exchange.
Modulo those transformations, no alternative **gauge** dictionary moves a
gauge-invariant prediction. Rephasings rotate the off-diagonal coordinate;
the rich context has already forced it to zero. Exchange identifies
`t` and `1-t`; it does not choose their fixed point unless imposed as a law
symmetry.

The genuine alternative is not another gauge frame. It is to let token-
disjoint contexts have independent kernels, or to derive a smaller shared
parameter set from elementary couplings. Both preserve every local
completeness and relational-path datum. CSF chooses full-kernel identity as a
universality doctrine and measures its dimension cost. No non-circular fact
inside the arena selects that doctrine.

The source's `dictionary_frozen` test is also weak: it verifies only that each
row ID belongs to a four-name whitelist. It does not validate the declared
kind, target context, phase, event-algebra action, or completeness of the row
set.

### 5.3 Three levels above one kernel

1. **Unobserved Kraus unravelling.** If output labels are discarded, port
   rotations with the same `M` are representation freedom.
2. **Calibrated instrument.** If `port-zero` is retained under a fixed
   apparatus calibration, the `1` versus `9/25` probabilities are an exact
   operational distinction.
3. **Durable relational record.** The output must be carried by a relational
   fact recoverable under every licensed future continuation. CSF does not
   construct this.

The witness reaches level 2 and no farther. Calling the object a “record
fiber” is safe only under the pin's specialized definition “calibrated port
record,” not under the corpus's stronger durable-record ontology.

### 5.4 Flags and permanence

The flag vectors give exact overlaps

```text
<f|f>=1,
<f|g_partial>=3/5,
<f|g_orthogonal>=0.
```

The branch-specific reconvergence rows map `f` and `g_orthogonal` to the same
one-dimensional state, restoring overlap `1`. This is a valid exact eraser
counterexample. It proves that one-cut orthogonality is not permanence and
supports the candidate's negative qualifier.

What remains owed is the Paper 3 question: does **every licensed future**
preserve recoverability of the flag partition, possibly through redundant
copies and relabelings? One selected eraser proves nonpermanence if it is
licensed by the actual law. In this fixture it proves only that the catalogue
permits erasure. There is no generative continuation grammar or census.

### 5.5 Refinement, spectator, and catalogue extensions

Appending a zero port leaves `M` unchanged; it is a mathematical refinement
with a null outcome, not a new record. Tensoring an idle spectator and taking
a direct-sum copy preserve completeness. Neither operation establishes the
physical quotient when:

- the number of history coordinates changes;
- one record partition refines another with nonzero new ports;
- the output carrier changes because a relation/cell is created; or
- a formerly null direction becomes reachable.

Those are exactly the contexts in which recurrence and record identity need
new comparison maps. CSF is fixed-history by construction.

## 6. Counterexamples and unrun controls

### 6.1 Gauge quotient versus symmetry-fixed singleton

The exact family

```text
M(1/4)=diag(1/4,3/4),
M(1/3)=diag(1/3,2/3),
M(1/2)=diag(1/2,1/2)
```

passes all three training completeness systems. Exchange sends the first two
to `M(3/4)` and `M(2/3)` respectively. Quotienting by exchange leaves the
`1/4` and `1/3` orbits distinct; only imposing fixed-point invariance removes
them. This exact control kills any claim that ordinary gauge quotient alone
selected half-half.

### 6.2 Independent-context countermodel

Assign `M(1/4)` to one rich context and `M(1/3)` to another token-disjoint
rich context, with the same local path graph, symmetric calibration, and all-
input completeness. Every context passes its local surface. The model fails
only the externally imposed full-kernel identity. Thus transport/locality
constraints at the level supplied by CSF do not force recurrence.

To exclude this model, the theory must add a universality axiom (“the same
event type has the same kernel in every disconnected realization”) or derive
both kernels from one recurring set of elementary couplings. That is a
legitimate law postulate, but not a gauge theorem.

### 6.3 A non-vacuous held-out replacement

The current held-out relative operator is another rich-spectrum row and adds
rank zero. A meaningful held-out test must constrain something not already in
the training row span—for example a new overlap whose completeness depends on
the surviving diagonal bias, or a calibrated port statistic computed from a
factorization rule fixed before the context is seen. Merely changing `i` to
`-i` after both cross coordinates are already zero cannot test the recurrence
ansatz.

### 6.4 Doctrine-screen replacement

The stored arrays `[1,0]` and `[0,1]` should be deleted as evidence. A valid
control would:

1. construct two recurrence maps that both preserve the declared event and
   calibration data but are not related by admitted gauge;
2. solve their PSD intersections;
3. apply one common calibrated preparation/port probe; and
4. compare exact probabilities.

If no such pair exists, the correct result is that doctrine sensitivity was
not tested, not that it was measured.

## 7. Consequence and scope reclassification

| candidate finding | review classification |
|---|---|
| `CSF-RECURRING-LAW-SELECTED-MODULO-GAUGE` | **KILL/REPLACE:** history individuation and recurrence selection are not earned; arithmetic singleton is conditional on full-kernel universality plus exchange invariance |
| `COMPLETENESS-SPECTRAHEDRON-CONSTRUCTED` | **KEEP:** fixed-history exact scope |
| `JCV-UNCONDITIONED-BASE-AND-CALIBRATED-FIBER-EMBEDDED` | **KEEP:** exact operator/instrument reconstruction |
| `RICH-SPECTRUM-UNCONDITIONED-CROSS-MOMENT-ZERO` | **KEEP:** unconditioned operator theorem, not record/actual-order fact |
| `CALIBRATED-RECORD-FIBER-OPERATIONALLY-NONTRIVIAL` | **NARROW:** calibrated retained-port instrument, not durable relational record |
| `SELECTION-CONDITIONAL-ON-EXCHANGE-SYMMETRY` | **KEEP BUT STRENGTHEN CONDITION:** also conditional on full-kernel recurrence and provisional history typing |
| `RECURRENCE-DOCTRINE-MOVES-PHYSICS` | **KILL:** gate compares hard-coded arrays, not a derived calibrated observable |
| `EXTREME-POINT-SELECTION-UNSTABLE` | **KEEP:** constraint-relative extremality result |
| `FLAG-ORTHOGONALITY-CONSTRUCTED-BUT-PERMANENCE-UNPROVED` | **KEEP:** eraser makes the limitation exact |
| `CONDITIONAL-STEERING-OPEN` | **KEEP:** explicit open scope |
| `ELEMENTARY-TRANSPORTS-AND-CATALOGUE-UNSELECTED` | **KEEP:** central limitation |

### Declaration-relativity ledger

CSF genuinely reduces several earlier debts:

- JCV's same-channel/different-calibrated-instrument distinction is expressed
  cleanly as base kernel versus factorization fiber.
- OVG's overlap completeness families acquire one convex fixed-history home.
- Rich spectrum supplies an exact unconditioned cross-moment theorem.
- Extreme-point selection is killed by an exact restriction control.

The unresolved debts have moved, not disappeared:

- PPR's record-generated event algebra becomes a declared two-name history
  dictionary;
- SRW's recurring local type becomes full-kernel universality across disjoint
  contexts;
- OVG's fixed-carrier order maps remain anonymous relative-operator fixtures;
- instrument calibration is external metadata;
- flag permanence depends on an unbuilt future grammar; and
- actualization remains a postulate, correctly untouched.

### Proposed adjudicated result

The strict pre-registered outcome should be

```text
CSF-BLOCKED-AT-HISTORY-INDIVIDUATION
```

with the following exact conditional corollary:

> Given the declared history coordinates, identity recurrence of the full
> kernel packet reduces the three independent affine families from total
> dimension five to a one-dimensional diagonal family. Imposing endpoint
> exchange as a physical law symmetry, not merely quotient gauge, leaves the
> unique kernel `I/2`. The held-out completeness row is algebraically
> redundant, and the calibrated port factorization remains unselected.

If adjudication elects to accept the declared names as provisional history
typing, the primary should instead be

```text
CSF-UNIVERSAL-KERNEL-AND-EXCHANGE-CONDITIONAL-SINGLETON
```

never `SELECTED-MODULO-GAUGE` without these conditions.

## 8. Grade

**REJECT.**

This grade does not dispute a single printed rational number. It follows from
three load-bearing failures:

1. the two recurring history coordinates are not configuration- or record-
   individuated by any constructed event/rewrite law;
2. the selected singleton is obtained by an unselected full-kernel
   universality postulate plus a fixed-point symmetry constraint, not by gauge
   quotient; and
3. the advertised doctrine-sensitive prediction is literal source data, not a
   computed observable.

The spectrahedral base, JCV fiber reconstruction, spectral theorem,
extremality counterexample, and flag eraser all survive as substantial
conditional results. The registered primary and one qualifier do not.

## 9. Numbered repairs and kill conditions

1. **Kill the registered primary.** Replace it by the blocked or conditional
   result wording in section 7. Do not describe the `1 -> 0` cut as selection
   modulo gauge.

2. **Kill `RECURRENCE-DOCTRINE-MOVES-PHYSICS`.** The hard-coded polynomial
   arrays are not evidence. A successor unit must derive a shared calibrated
   screen from two admissible, non-gauge recurrence maps.

3. **Repair history typing.** Construct the two ordered histories from one
   relational event grammar, including their elementary maps, configurations,
   common boundary, and record/null quotient. Names and actor counts are
   insufficient.

4. **Price recurrence explicitly.** State that `5 -> 1` is the dimension cost
   of a universality postulate across token-disjoint contexts. Derive a smaller
   recurring coupling packet if possible; do not call equality of full `M`
   vertex locality.

5. **Separate gauge from symmetry.** Rephasings and passive coordinate changes
   are quotiented covariantly. Endpoint exchange selects `I/2` only when
   imposed as a physical automorphism of the law and calibration.

6. **Replace the held-out context.** Require a context whose affine equations
   or calibrated prediction are not in the training span. Record the exact
   rank increment before calling it held-out validation.

7. **Narrow the record-fiber language.** The `1` versus `9/25` result is a
   retained calibrated instrument outcome. Promotion to a durable record
   requires a relational carrier and continuation-stable recoverability.

8. **Run the permanence grammar.** Include append-only, erasing, relabelling,
   and redundant-copy futures in one licensed continuation system rather than
   one branch-specific reconvergence witness.

9. **Do not infer selection from recurrence freeze timing.** Freezing a
   dictionary prevents postselection; it does not provide the physical
   principle selecting that dictionary.

10. **Kill condition for future recurrence.** Any proposed universal kernel
    is refuted if two independently identified occurrences of the same event
    type require gauge-invariantly different kernels under a common
    calibration. Conversely, agreement in chosen coordinates is not enough
    without the identifying transport.

## 10. Report SHA-256

Normalized self-SHA-256:
`c15b5c7a9a116b26d255f5d44109a8dfb0f616bbdbbab0f30ff40f21b1a6a4ec`.
This is the SHA-256 of the complete UTF-8 report after replacing only the
64 hexadecimal characters in this field by 64 ASCII zeroes. This convention
allows the report to carry a non-self-referential integrity value in its own
bytes.
