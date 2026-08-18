# OVG hostile review — relational rewriting, concurrency, and primitive arity

Seat: **R — relational rewriting, concurrency, and primitive arity**  
Target: Paper 5 candidate commit
`bb0f13aedadc354068ea2bcc08478bcd8c43ded1`  
Protocol: `v16/note-ovg-hostile-protocol.md`  
Review mode: repository read-only except this assigned report; independent
exact reconstruction in `/private/tmp`; no candidate implementation imported
into the reconstruction  
Grade: **ACCEPT-WITH-FIXES**

## 1. Immutable-target and hash audit

I read the complete runbook and frozen protocol before beginning this seat,
then read the pin, core/fixture freezes and refusal/repair chronology, generic
core, physical scorer, fixture, transcript, receipt, Paper 5, candidate
verification, and the relevant history/rewrite antecedents. I did not consult
either other OVG review.

The immutable target reproduces:

| object | protocol SHA-256 | reviewer SHA-256 | status |
|---|---|---|---|
| pin | `286e681a05b7346226f4f3f381036b2b6bc07d809c93c2ac352d9f71a0f44c40` | same | PASS |
| generic core | `7b17a138dc45f564a5180fca81bdb4620aaa570514d090d8a5c45f0f22d985bf` | same | PASS |
| physical fixture | `7b7658492a49c77f6c9ee3e0a2031d5121c627aad5ae6630e21940a68c92b133` | same | PASS |
| repaired scorer | `75cc0e7279ee93a60bfa520eecb4ea37fcde49b3d9e9f7298d98031396628844` | same | PASS |
| freeze/refusal/repair record | `d44fd66678fe16ce85c2c9780142583a111776108b87788b734833419c9a3b34` | same | PASS |
| transcript | `48cf0fdecc43b1d148c97bac936a879cbbcf14daddfccd6e597014017155fe7f` | same | PASS |
| receipt | `4ba954430acd0772da62c8df16b2c6b08bca9e76fd7b25d3b5b72fcc43ce2852` | same | PASS |
| Paper 5 | `89a6ad8b10b97351d71a499ebbb36b2cf5a89f32d5ec9d005f9b4a68dab16b31` | same | PASS |
| candidate verification | `12774e1a2d9d72d147a67e066679bc6e376e29f4acecc453f3d164ce19ba37e5` | same | PASS |

The #55 first physical invocation correctly refused before artifact creation
because one antecedent token crossed a Markdown line break. The #56 repair
normalizes whitespace only for token comparison; it does not change the
fixture, operator/rewrite constructions, gates, classifiers, or renderer.

One clean replay into fresh `/private/tmp` paths reproduced the committed
transcript, receipt, and paper byte-for-byte. The receipt contains 32 unique
passing gates, 30 mutation bindings, twelve one-occurrence generated claims,
nine sealed payload components, and the seven frozen finding words. I reran
twelve rewrite-relevant mutants; each exited `1` at its registered gate and
wrote no result:

```text
history-order-drop            -> OVG-REFERENT-TYPES
common-boundary-forge         -> OVG-REFERENT-TYPES
dependency-call-record        -> OVG-DEPENDENCY-TYPE
divergent-call-common         -> OVG-DEPENDENCY-TYPE
local-flag-call-implemented   -> OVG-LOCAL-FLAG
local-factorization-drop      -> OVG-LOCAL-FLAG
binary-product-call-primitive -> OVG-ARITY-COMPOSITE
ancilla-policy-hide           -> OVG-ANCILLA-POLICY
durability-assume             -> OVG-RECORD-PERMANENCE-SCOPE
all-n-promote                 -> OVG-ALL-N-SCOPE
typed-count                   -> OVG-ARITY-COMPOSITE
seal-after-write              -> OVG-PREWRITE-INTEGRITY
```

This is a clean finite candidate. The review issue is not receipt integrity;
it is which relational typing the exact operator results have actually
earned.

## 2. Independent method and tools

I wrote an independent integer/permutation reconstruction at
`/private/tmp/ovg_rewrite_independent.py`. It uses only tuples, finite sets,
XOR, and exhaustive word enumeration. It does not import `ovg_core.py`,
`ovg_score.py`, or the receipt. Its checks were:

1. construct three- and four-actor CNOT permutations directly from bit rules;
2. compose both `AB/BC` event orders;
3. enumerate every word of length one through four in the two frozen binary
   generators;
4. reconstruct the four token-rewrite critical pairs from their declarations;
5. test `F_2` linearity of both CNOT generators and Toffoli;
6. extend the operator and rewrite fixtures with one idle spectator;
7. enumerate all six orders of three overlapping generators `AB,BC,CD`; and
8. compare the operator and token-rewrite layers for shared data dependencies.

The analytic portions are elementary. CNOT circuits are linear maps over
`F_2`; passive actor relabelling conjugates a gate by the corresponding tensor-
factor permutation; and a class-map common boundary is relationally licensed
only if both histories are maps between independently identified boundary
configurations, not merely square matrices of the same dimension.

## 3. Exact recomputation table

| item | candidate value | reviewer value | status |
|---|---|---|---|
| `AB` and `BC` actor-support overlap | `{A,B} intersection {B,C}={B}` | same | PASS, declared support fact |
| common operator carrier | both maps `8 x 8` | both permutations of 8 basis states | PASS, fixed-carrier fact |
| order maps distinct | `True` | `True` | PASS |
| disjoint critical pair | `disjoint-commuting`, final `{ab,ab1,c,c1}` both ways | same | PASS |
| joinable overlap | `joinable-overlap`, final `{ab,ab1,bc,bc1}` both ways | same | PASS |
| delete/use | forward undefined; reverse `{ab,c1}` | same | PASS |
| divergent pair | finals `{}` and `{x}` | same | PASS |
| left factorization count through length 4 | `5` | `5` | PASS |
| right factorization count through length 4 | `5` | `5` | PASS |
| shortest left/right words | `(u_ab,v_bc)` / `(v_bc,u_ab)` | same | PASS |
| CNOT involutions | implicit in padded words | `u_ab^2=v_bc^2=I` | PASS; explains four padded words |
| Toffoli factor words through length 4 | `0` | `0` | PASS |
| binary generators `F_2`-linear | `True` | `True` | PASS |
| Toffoli nonlinear witness | `[2,4]` | `T(2 xor 4)=7`, `T(2) xor T(4)=6` | PASS |
| formal flag dilation | shape `16 x 8`, isometry | not rederived in this lens; typing audited below | RECEIPT FACT |
| typed flag implementation | absent (`(16,8)` not in `[(8,8)]`) | absent | PASS |
| record permanence | not censused | not censused | PASS/refusal |
| operator idle spectator | complete instrument extended by identity | `A tensor I_D` and `B tensor I_D` remain distinct typed permutations | PASS, unrun control |
| rewrite idle spectator | not a physical rewrite gate | adding untouched token `d` preserves joinable final set | PASS, unrun control |
| three-overlap extension | not run | six orders of `AB,BC,CD`, four distinct composites | NEW EXACT CONTROL |
| dimension-changing relational critical pair | pin requires one; fixture has none | absent | FAIL OF PIN COVERAGE |
| full actor-relabel groupoid | pin requires it; no gate | frozen generator set not closed under `A <-> C` | FAIL OF PIN COVERAGE |

The factorization words reproduce exactly. For the left order they are

```text
(u,v)
(u,u,u,v)
(u,v,u,u)
(u,v,v,v)
(v,v,u,v)
```

and the right list is the reversed analogue. The number five is not a robust
physical multiplicity. Four rows are identity padding enabled by
`u^2=v^2=I` and the length-four cutoff. The physical result is the existence
of the length-two factorization.

## 4. Theorem and proof audit

### 4.1 The four rewrite classifications are correct but independent

The token grammar implements a rewrite as three sets: requirements, additions,
and deletions. Sequential application yields exactly the four rows above.
Calling the delete/use row a **dependency** is correct: after deletion one
order is not a well-typed history. Calling the divergent row **not common at
that cut** is also correct. Neither row supplies a record, because neither
constructs a record variable or proves continuation-stable distinguishability.

However, these token rewrites are not the relational histories whose CNOT
matrices enter the Gram calculation. `event_matrix()` consumes gate kind,
qubit count, control, and target; it never consumes the event's declared actor
`support`. `history_matrix()` consumes only the ordered event names. The four
`rewrite_cases` are evaluated later by a separate set machine. No event-library
row is assigned one of those rewrites, and no boundary graph/token catalogue
is assigned to either CNOT order.

Thus the result contains two neighboring fixtures:

- fixed-carrier operator orders `VU` and `UV`; and
- token critical pairs with four concurrency types.

They illustrate the intended correspondence. They do not construct it.

### 4.2 The common boundary is operator-typed, not relationally derived

Both CNOT orders are permutations of the same eight-dimensional qubit carrier,
so `A^dagger B` is perfectly well typed as an operator. The actor labels also
make their supports overlap at `B`. This is enough for the exact operator
variety.

It is not an independently derived **relational common future** in the sense
of Papers 3 and 4. No before/after relational configuration, persistence map,
created relation, port, or continuation identifies the final basis facts of
the two orders. Equal matrix dimension is doing all common-boundary work. The
joinable token pair happens to reach one equal token set, but it is not linked
to `VU` and `UV`; swapping that token pair for the dependency or divergent
pair would leave every CNOT/Gram number unchanged.

The strongest correct theorem is therefore:

> For two declared fixed-carrier event-order maps with a common operator
> domain and codomain, the Gram/instrument equations are well typed.

The stronger sentence “the relational rewrite law provides the common
boundary” is unproved.

### 4.3 Toffoli irreducibility is stronger than the finite census—but only
relative to the frozen grammar

Every CNOT on any number of bits acts by an invertible linear transformation
over `F_2`. Products of CNOTs remain linear. Toffoli sends

```text
(a,b,c) -> (a,b,c xor ab),
```

which is nonlinear. The exact witness is `x=010` (2), `y=100` (4):

```text
T(x xor y)=T(110)=111,
T(x) xor T(y)=010 xor 100=110.
```

Consequently no arbitrary-length CNOT-only circuit on the same three bits can
implement Toffoli. The result also survives any number of ancillas initialized
to zero and returned to zero: the full CNOT circuit is linear on `(x,0)`, so
its data output is still a linear function of `x`. The scorer merely checks
that the ancilla policy is present and enumerates no ancillary circuit, but
the analytic linearity proof supplies the missing quantifier for this specific
resource grammar.

This is not ontology-level primitive arity. Adding Toffoli as a generator makes
it primitive by declaration; enlarging the resource set with other gates may
factor it. What is earned is **irreducibility relative to CNOT-only linear
resources**, plus a sensitivity control demonstrating that the factorization
assay can return both answers.

### 4.4 Relabelling and spectator naturality are not delivered gates

For a permutation `pi` of actor tensor factors,

```text
P_pi CNOT(i->j) P_pi^-1 = CNOT(pi(i)->pi(j)).
```

That is the correct passive-covariance theorem. The frozen physical event
library, however, contains only `A->B` and `B->C`. Under `A <-> C` it requires
`C->B` and `B->A`, neither of which is in the library. The candidate therefore
does not implement the full declared relabelling groupoid or establish closure
of the selected generator catalogue under it.

An idle spectator extension exists independently at both levels: tensor the
operator maps by `I_D`, and add an untouched token `d` to the rewrite state.
My exact reconstruction preserves order distinction and the joinable final
set. The delivered spectator gate instead checks the unconditioned parity
instrument's remote marginal. It is not a rewrite/operator naturality weld.

### 4.5 The fifth pinned critical-pair case is absent

The pin requires five cases, the fifth being two relational rewrites that
change carrier dimension and reach a common larger codomain. The fixture has
four `rewrite_cases`. Its separate `C^2 -> C^4` isometry pair has no relational
rewrite at all. This absence is especially important after Papers 3 and 4:
the unit has not shown that its overlap classifier survives a carrier created
by the same relational events whose order is being summed.

## 5. Representation and ontology audit

### 5.1 What the two “histories” are

At the mathematical level they are two ordered circuit maps on one fixed
three-qubit carrier. The sequence labels `AB then BC` and `BC then AB` are
declared fine-history labels. Because the maps differ, calibrated inputs and
outputs can distinguish the transformations; they are not merely two matrix
factorizations of one identical operator.

At the ISP ontological level, more is required before calling them two
configuration-individuated relational histories. A complete configuration
catalogue must say what each basis element means, an elementary event must
change the corresponding relation/process configuration, and both orders must
land in one independently identified unread boundary. Paper 5 supplies event
names and actor supports, but not those configurations or rewrites.

The coherent class-map sum can therefore be read safely as a representation
of a candidate whole-history law. It is not yet an implemented physical
procedure or proof that the ontology admits controllable superposition of
event order. The paper correctly refuses quantum-switch and causal-
nonseparability language.

The ordered token sequence need not introduce an ontic background micro-time
if it remains an internal description of a complete history between division
events. It would reintroduce one only if each intermediate circuit step were
promoted to an actual universal update. The candidate does not make that
promotion, but it also does not derive the ordering from back-reacting local
relations.

### 5.2 Four arity notions remain distinct

1. **Lower-arity composite:** `VU` and `UV` are exactly products of two binary
   generators. This is proved.
2. **Named fusion:** writing either product as one arrow changes notation and
   proves nothing about indivisibility.
3. **Primitive generator relative to a grammar:** Toffoli is irreducible in
   the complete CNOT-only grammar by the `F_2` theorem. This is a valid control,
   not a selected ISP law.
4. **Ontology-level indivisible event:** no internal division is physically
   lawful and no lower-arity realization exists in the full selected theory.
   Nothing in this unit establishes such an event.

Therefore `COMPOSITE-SUPPORT-DOES-NOT-FORCE-PRIMITIVE-ARITY` survives exactly.
It is a refusal of an inference, not selection of arity two or denial of all
higher primitives.

### 5.3 The flag is formal and local only by catalogue declaration

Stacking the two parity-port maps gives a `16 x 8` isometry. The fixture adds
the metadata `carrier_actor: B` and `flag_dimension: 2`, while its elementary
map types contain only `(8,8)`. This proves a formal dilation and explicitly
records that the frozen elementary grammar cannot implement it.

It does not yet prove relational locality. There is no created flag cell, no
attachment to `B`, no local observable algebra, no reachability rule, no
relabel-covariant event implementing the `16 x 8` map, and no continuation
census. The minimum physical completion would require all of the following:

1. a target relational configuration with a flag cell attached to `B`;
2. a support/rewrite-compatible transport into that target fiber;
3. a factorization into licensed local events or a separately declared new
   generator;
4. covariance under actor relabelling and idle neighbors; and
5. a future recoverability/permanence test distinguishing a durable record
   from an erasable ancilla.

The current suffix is acceptable only if “kinematically permitted” is made
explicitly synonymous with **formally dimension-compatible after declaring a
local catalogue slot**. It is not a theorem of locality.

## 6. Counterexamples and unrun controls

### 6.1 Same Gram physics, different relational concurrency

Keep the exact CNOT maps `U,V`, their two order matrices, all coefficients,
and their common eight-dimensional carrier fixed. Attach them first to the
candidate's additive joinable token rewrites, then to a delete/use grammar in
which the first event removes the referent required by the second. Every Gram
operator, completeness residual, phase row, port map, and factorization word
is byte-for-byte the same, while the relational order family changes from two
lawful histories to one lawful history.

This is possible because the scorer never maps event-library rows to
`rewrite_cases`. It is a direct model-pair showing that relational history
membership is not determined by the advertised operator object. The overlap
variety remains mathematically valid **conditional on** the event-order family
being independently licensed.

### 6.2 Three-overlap extension

I added four actors and three binary generators

```text
CNOT(A->B), CNOT(B->C), CNOT(C->D).
```

All six orders are well-typed on the same sixteen-state carrier. Exact
enumeration gives four distinct composite maps: `AB` commutes with `CD`, while
the neighboring overlaps do not. Hence the two-history classifier does not
by itself define a three-generator law. The next unit needs:

- a six-history Gram family rather than pairwise relative operators only;
- a port coefficient matrix complete for all six histories;
- consistency under grouping `(AB,BC)` then `CD` versus `AB` then `(BC,CD)`;
- a rewrite critical-triple/diamond or higher associator gate; and
- a cocycle/holonomy rule if different grouping paths are physically distinct.

Pairwise joinability is insufficient to select or even type arbitrary-`n`
coherence. The candidate correctly refuses the all-`n` claim.

### 6.3 Catalogue enlargement

Allowing a flag cell, an ancilla, or a new ternary generator changes the
factorization grammar. The candidate handles this honestly for Toffoli by
stating a frozen CNOT-only scope. The same honesty must be applied to the local
flag: adding a `(16,8)` generator would remove the declared implementation
obstruction immediately but would not derive that generator. Catalogue
enlargement changes what is expressible; it does not retrospectively select
an ontological primitive.

## 7. Consequence and scope reclassification

| candidate consequence/finding | review classification |
|---|---|
| `OVG-GRAM-INSTRUMENT-VARIETY-CONSTRUCTED` | **KEEP WITH SCOPE:** fixed-carrier common-boundary operator history family; relational rewrite/common-future weld not constructed |
| `SINGLE-PORT-PHASE-CONSTRAINED` | **KEEP:** operator theorem; no arity or relational-selection consequence |
| `MULTIPORT-COHERENCE-EXISTS-BUT-PORT-LAW-UNSELECTED` | **KEEP:** mathematical instrument existence; implementation unselected |
| `LOCAL-FLAG-KINEMATICALLY-PERMITTED-BUT-IMPLEMENTATION-UNSELECTED` | **NARROW:** formal flag dilation is dimension-compatible with a declared actor-`B` slot; relational locality and durability untyped |
| `COMPOSITE-SUPPORT-DOES-NOT-FORCE-PRIMITIVE-ARITY` | **KEEP:** exact length-two factorizations; count five is cutoff/padding-dependent |
| `CAUSAL-NONSEPARABILITY-UNTESTED` | **KEEP:** required refusal |
| `OVERLAP-LAW-UNSELECTED` | **KEEP WITH TYPE:** coefficient/operator law unselected; elementary relational overlap law not built |
| delete/use dependency | **KEEP:** typing fact, not a record |
| divergent endpoints | **KEEP:** no common boundary at that cut, not a no-go or record |
| Toffoli irreducibility | **KEEP AS CONTROL:** arbitrary-length CNOT-only theorem, including zero ancillas; not selected ISP primitive |
| local record | **REFUSE:** no implementation or permanence census |
| arbitrary-`n` composition | **REFUSE/OPEN:** first three-overlap extension already needs new coherence data |
| back-reacting relational carrier | **REFUSE:** operator and token fixtures remain unwelded; pinned dimension-changing rewrite is absent |

No result in this seat supports a field/Fock construction, particle species,
exchange statistics, Hamiltonian, continuum, gravity, or QFT/GR deviation.
Those refusals in Paper 5 are correctly placed.

### Proposed adjudicated finding list

I propose retaining all seven machine segments only after two textual changes:

```text
OVG-FIXED-CARRIER-GRAM-INSTRUMENT-VARIETY-CONSTRUCTED
SINGLE-PORT-PHASE-CONSTRAINED
MULTIPORT-COHERENCE-EXISTS-BUT-PORT-LAW-UNSELECTED
FORMAL-FLAG-DILATION-PERMITTED-BUT-RELATIONAL-IMPLEMENTATION-UNSELECTED
COMPOSITE-SUPPORT-DOES-NOT-FORCE-PRIMITIVE-ARITY
CAUSAL-NONSEPARABILITY-UNTESTED
OVERLAP-LAW-UNSELECTED
```

The first rename makes the missing relation-rewrite weld explicit. The fourth
removes an unearned locality implication. If adjudication preserves the
original strings for machine stability, these two qualifications must be
binding prose immediately adjacent to them.

## 8. Grade

**ACCEPT-WITH-FIXES.**

The exact operator variety, the complex-weight counterexample, the composite-
arity refusal, and the dependency/divergence distinctions survive this lens.
I do not grade `REJECT` because Paper 5 explicitly refuses all-`n`, durable
flags, causal nonseparability, and primitive-arity selection, and its main
mathematical object exists on the declared fixed carrier.

The fixes are material rather than cosmetic: the operator histories are not
welded to the relational rewrite cases, the fifth pinned growing-rewrite case
is absent, full relabel covariance is absent, and local flagging is metadata
rather than relational implementation. Those defects prevent promotion from
“fixed-carrier overlap classifier” to “joint relational successor law.”

## 9. Numbered repairs and kill conditions

1. **Bind the primary scope.** Replace “typed relational overlap histories”
   wherever it implies a constructed rewrite law by “declared fixed-carrier
   event-order maps.” Preserve the Gram theorem at that scope.

2. **Weld or separate the fixtures.** Either assign each CNOT event a concrete
   relational rewrite and prove both orders reach the same independently typed
   boundary, or state that the token critical pairs are separate controls with
   no bearing on CNOT history membership.

3. **Restore the fifth pinned case in a successor unit.** Construct a genuine
   dimension-changing relational overlap whose two orders reach one larger
   common future and whose carrier transports are induced by those rewrites.
   Do not retrofit it into the frozen candidate.

4. **Narrow the flag finding.** Replace local kinematic implementation language
   by formal dilation plus declared catalogue placement. A local result requires
   attachment, support/rewrite compatibility, factorization/reachability,
   relabelling covariance, and permanence.

5. **State the arity invariant correctly.** The existence of the length-two
   word, not the finite count five, proves compositeness. Retain Toffoli only as
   a CNOT-resource sensitivity control; its analytic `F_2` proof may be stated
   for arbitrary length and zero-return ancillas.

6. **Add missing naturality gates later.** Close the event library under the
   declared actor relabelling groupoid and test the same spectator at both the
   rewrite and operator levels.

7. **Do not infer all-`n` from pairwise strata.** The next overlap unit must run
   at least the `AB/BC/CD` critical triple, all six histories, grouping/cut
   coherence, and a three-overlap associator/cocycle discriminator.

8. **Kill condition for the relational reading.** If no assignment of the
   CNOT generators to lawful rewrites yields both order maps at one common
   relation-derived boundary, the relational-overlap interpretation is killed;
   the operator variety remains a circuit theorem.

9. **Kill condition for primitive claims.** Any future primitive-arity claim
   dies if the candidate map factors after a predeclared allowed catalogue or
   ancilla enlargement. Conversely, nonfactorization in one grammar never by
   itself proves ontology-level indivisibility.

## 10. Report SHA-256

Normalized self-SHA-256:
`52af4a049e13becc51a87b4a26ee6fd9ad94cfdaa0e1943e87466d3d8f94b545`.
This is the SHA-256 of the complete UTF-8 report after replacing only the
64 hexadecimal characters in this field by 64 ASCII zeroes. This convention
allows the report to carry a non-self-referential integrity value in its own
bytes.
