# D12 hostile ontology/locality/physics review — round 1

**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION / `INCOMPLETE-INVESTIGATION`**

## Executive finding

D12 contains a sound finite nonselection result and an unsound implementation
claim.

The exact `P_r` pair proves that one- and two-record marginals do not determine
a three-record conditional. The exact iSWAP pair proves that unitarity,
exchange symmetry, excitation conservation, entangling capacity, and a common
input/output type do not determine the interaction angle. These are valuable,
correct counterexamples to a unique record-only dynamics.

But the restored executable does not implement the sealed-diamond object
frozen in the protocol. It has no screen, collar state, frame link, local
order unit, emitted opportunity, durable record node, output-collar object,
or generated variable history. “Seal-and-birth” is a Boolean/type equality;
“256 commits” is integer bookkeeping; construction gauge is tensor-factor
commutation; integrated gauge is one common unitary basis change; and
profinite projectivity is one two-record deletion plus a finite three-bit
example. Consequently the receipts do not close U1–U7 at their registered
meaning.

The strongest defensible disposition is:

```text
FINITE DYNAMICAL NONUNIQUENESS WITNESSES = PASS
EVIDENCE/FIXED-POINT SELECTION OF INTERACTION = REFUTED
GEOMETRY-AFTER-LAW = CORRECTLY REFUSED
RESTORED SEALED-DIAMOND GENERATIVE IMPLEMENTATION = NOT EXECUTED
LOCAL WHOLE-HISTORY CLICK LAW = NOT ESTABLISHED
PROTOCOL VERDICT = INCOMPLETE-INVESTIGATION
```

## Artifacts and reproduction

Reviewed:

- all five `note-d12-*.md` files;
- `relativistic-isp-v10-paper13-the-click-law-is-the-whole-history-process.md`;
- all three `code/d12_*.py` executables.

All three scripts reproduce their frozen results:

```text
d12_diamond_law_nonuniqueness_exact.py       42/42
receipt 1f9472d6ed613ad96fe875d68cf0a773062c077e9a44fc357f65ccfd93bd4b97

d12_symmetric_interaction_family_exact.py    18/18
receipt 7da912f8deb705aaa1467d3428aacf7cc626b249bf16c324c5c365f376b89db9

d12_restored_diamond_process_exact.py        25/25
receipt c31174cbc695de30169e5acf1492998990609ea68e2b20e09b98d6370e039391
```

The issue is not arithmetic drift. It is that several gates test a much
weaker object than their labels and the protocol require.

## Blockers

### B1 — The sealed diamond is described in prose but absent from the executable

**Severity:** critical

The protocol defines a restored diamond with `Omega_D`, `mu_D`, a complete
whole-history law, contrast ledger, holonomy, lower and upper screens,
eventless collar, order unit, frame links, and typed exposed interfaces.
`SealedDiamond` in the restored code contains only:

```text
name, interaction, incoming type labels, outgoing type labels,
owner labels, terminal flag.
```

The other scripts reduce the ontology further to a `DiamondPacket` or a
metadata dictionary. A string pair `("q","q")`, the names `left/right`, and
`connected_collar=True` do not establish that a previously recorded collar
exists, owns both legs, matches a lower screen, or transports state and frame
data to an upper screen.

This fails frozen gate U1 and leaves U6 asserted rather than modeled.

**Required repair:** implement immutable typed objects for the diamond,
screens, input and output collars, collar identifiers and owners, local order
units, endpoint frame links, history atoms, durable records, and emitted
opportunities. A rewrite must reject missing, disconnected, stale, or
wrong-type inputs by construction.

### B2 — Seal-and-birth is a primitive hidden grammar, not a restoration theorem

**Severity:** critical

A durable record and a continuing carrier are different ontological objects.
Persistence of the record does not imply birth of a successor collar. D12 is
right that observational truncation is not automatically physical
annihilation, but it reverses the error when it treats continuation as what a
seal intrinsically means.

The code “proves” seal-and-birth by checking

```text
incoming == outgoing and terminal == False.
```

No branch creates an output-collar object, successor identity, provenance,
state, frame link, opportunity, or lower-screen match for a later diamond.
The 100- and 256-commit checks repeatedly subtract two type labels and add two
type labels to an integer. No commit is generated.

D8 may supply seal-and-birth as one SCIR rule, but that makes it primitive
grammar. It is not forced by the sealed-record ontology, and Paper 13 itself
later lists bridge/branch opportunities and record instruments as primitive.
Calling D11 an “accidental ablation” is therefore too strong: terminal SEAL is
a different declared continuation ontology, not deletion of its already
durable record.

**Required repair:** call continuation a primitive candidate rule. Execute a
branch that returns `(durable_record, output_collars, opportunities)` and feed
those exact outputs into subsequent diamonds. Test state normalization,
provenance, ownership, record persistence, and local eligibility at every
step. Replace the integer-loop receipt by actual generated histories.

### B3 — An orthogonal projector is not yet a durable record

**Severity:** critical

The restored script inserts computational projectors into a class operator.
Off-diagonal history terms then vanish because mutually exclusive sharp
projectors are orthogonal. That is a correct consistent-history calculation
for the chosen pointer family. It does not implement an immutable record or
prove durability.

There is no record identity, owner, stored outcome/effect, parent diamond,
finite evidence payload, output inscription, repeat-read law, persistence
under later dynamics, or test against recoherence. The word “durable” is
therefore attached to a measurement operator rather than a generated
ontological object. This is precisely the measurement/record conflation that
the protocol required D12 to avoid.

**Required repair:** either rename the present result `EXACT ORTHOGONAL
POINTER-HISTORY DECOHERENCE`, or generate immutable record objects and verify
repeatability and persistence through later allowed interactions and coarse
grainings. A physical decoherence claim also needs a declared environment or
record channel, not only an inserted final projector.

### B4 — `Ext_mu` hides the missing birth and bridge grammar inside the measure

**Severity:** critical

For a supplied measure, the identity

```text
P(e|H) = mu([He])/mu([H])
```

is correct disintegration. Defining

```text
Ext_mu(H) = {e : mu([He]) > 0}
```

does not construct the candidate extensions. The variable-history sample
space, the meaning of `[He]`, the lower-screen match, collar ownership, output
types, and bridge opportunities must already exist before the cylinder can be
measured. Thus `mu` silently contains both the probability law and the birth
grammar whose origin D12 set out to investigate.

This is acknowledged in some lists of primitive data, but contradicted by the
headline that the “actual interactive click law” has now been identified.
Conditioning a complete law is a representation theorem, not a local
generative mechanism or explanation of how new record types arise.

**Required repair:** separate an explicitly supplied local grammar `G` from
measure support:

```text
Ext_(G,mu)(H) = {e in Ext_G(B_H) : mu([He]) > 0}.
```

State plainly that `G`, the complete process measure, and its evaluation are
primitive unless separately selected.

### B5 — Removing a global race does not establish a decentralized local law

**Severity:** critical

D12 contains no D11-style global enabled-token normalization. That is a real
improvement in presentation. But an arbitrary non-Markov measure on complete
histories can encode global constraints and nonlocal correlations. Evaluating
`mu([He])/mu([H])` may require the entire sealed history or an oracle for the
complete universe measure. Calling `e` local does not make the conditional
law dynamically local.

The finite `P_r` example has no collar graph, spacelike separation, causal
screening, or ownership relation. It proves non-Markov dependence; it does not
prove a local non-Markov process. Likewise, disjoint tensor operators
commuting is not a no-signalling or causal-factorization theorem for the
whole-history measure.

Paper 13's claim that the law is “local in its dynamical ingredients” and
“requires no global clock or machine update” is therefore half established.
A presentation-free measure needs no physical total order, but D12 has not
constructed a decentralized evaluator or proved that the primitive measure
obeys local causality.

**Required repair:** distinguish:

1. absence of a preferred global linear order;
2. locality/no-signalling constraints on cylinder marginals;
3. causal ownership of extension support; and
4. local computability or realization of the conditional law.

Prove the applicable conditions or leave each open. Do not equate
whole-history non-Markovianity with benign global correlation by definition.

### B6 — Construction-order gauge is only disjoint operator commutation

**Severity:** major

U4 required all auxiliary linearizations to be grouped into canonical
physical fibers with equal pushed probability or decoherence-functional
weight. The scripts only verify

```text
(U tensor I)(I tensor U) = (I tensor U)(U tensor I).
```

They do not generate either presentation's durable records, collar births,
identities, opportunities, class operators, or canonical marked history. No
fiber is enumerated or pushed forward, and no overlapping negative control is
executed in the restored process.

**Required repair:** execute both orders of at least two disjoint complete
diamond commits, including their instruments and emitted collars; canonicalize
the resulting partial history; compare the full probability/decoherence
weight; and show that an overlapping pair retains physical order.

### B7 — “Integrated frame covariance” is a one-frame basis-change check

**Severity:** major

The restored code conjugates the two-qubit state, interaction, and both
pointer families by one common unitary `H tensor H`. This correctly verifies
basis covariance for one finite experiment. It is not U7.

There are no independently changed vertex frames, nonunitary endpoint
`SL(2,C)` maps, local order units, links, anchors, screens, or collar
transports. The separate SWAP/CNOT script checks a nonunitary diagonal
endpoint template, but still does not generate a multi-vertex history.

**Required repair:** rename the receipt `ONE-DIAMOND UNITARY BASIS
COVARIANCE`. Leave integrated generated-history gauge open until the actual
typed history is run in independent endpoint frames with all transported
objects compared.

### B8 — The projective and profinite claims exceed the finite checks

**Severity:** major

The restored code performs one deletion: it sums over the later first-leg
projector and reproduces the earlier second-leg mass. The `P_r` code checks a
three-bit law's pair marginals and a neutral binary refinement. Neither script
constructs an inverse system of variable sealed histories, canonical
truncation maps at arbitrary depth, or a compatible cylinder family on an
infinite/profinite limit.

The conditional-ratio formula is standard once such a measure exists, but
the D12 executable does not establish that its variable diamond histories
form a profinite space or that the finite witnesses extend as the claimed
local process. With unbounded or continuously typed extensions, “profinite”
may not even apply without additional finiteness and compactness hypotheses.

**Required repair:** define finite history sets `X_n`, bonding maps, canonical
fibers, and compatible measures `mu_n`; prove or execute pushforward
consistency across several nontrivial depths; state the hypotheses that make
the inverse limit profinite. Otherwise use `finite cylinder example`, not
`profinite whole-history implementation`.

### B9 — Decoherence functionals, process tensors, and combs are not one object

**Severity:** major

For a supplied closed-system sequence and a consistent projector family, the
class-operator decoherence functional is legitimate. A process tensor is an
operational multilinear object that maps inserted CP instruments to
multi-time probabilities and obeys causality/normalization constraints. A
quantum comb is a related network object. They are not automatically the
same object as `D(alpha,beta)`, nor do process tensors generically “generate
amplitudes.”

The formula

```text
P(e|H) = D(He,He)/D(H,H)
```

also needs `H` and its extensions to belong to a consistent/decoherent family.
For unresolved alternatives, the coarse class operator must be summed before
forming `D(H,H)`; interference terms cannot be dismissed by a parenthetical
phrase. The executable only covers a sharp exactly orthogonal family and has
no process-tensor intervention or causality test.

**Required repair:** present decoherent histories, process tensors, and combs
as alternative supplied representations with explicit translation
hypotheses. State the consistency conditions for conditional probabilities
and implement one genuine process-tensor/comb causality test before claiming
that representation.

### B10 — The Barandes relation is stated too affirmatively after a direct contemporary challenge

**Severity:** major literature repair

Paper 13 says Barandes's indivisible stochastic process “fits precisely here”
and that the stochastic-quantum correspondence can supply a Hilbert-space
representation. The literature section says the cited works “show” how broad
non-Markov stochastic dynamics correspond to quantum representations.

That is not a safe settled premise. Egri, Gomori, Gyenis, and Hofer-Szabó,
[“Trajectory of Probabilities, Probability on Trajectories, and the
Stochastic-Quantum Correspondence”](https://arxiv.org/abs/2602.23491), make
the exact distinction central to D12: one-time probability dynamics do not
determine a probability measure on trajectories. They prove generic
nonuniqueness of stochastic implementations, show that a probability dynamics
always admits a Markov implementation and often non-Markov implementations,
and directly criticize the Barandes correspondence's identification of
dynamics-level transition maps with process conditionals and its claimed
coverage of quantum interference.

This source does not damage D12's finite `P_r` no-go; it independently
supports its logic. It does make the affirmative Barandes bridge and the
implicit priority boundary untenable. Paper 13 cannot use Barandes as an
established theorem that a supplied SHARD path measure has the claimed
quantum representation, or that an indivisible probability dynamics is
already a unique path measure.

**Required repair:** cite Egri et al.; distinguish a trajectory of
probabilities, a family of probability dynamics, a probability measure on
histories, and a stochastic implementation. Recast Barandes as a proposed and
contested correspondence with nontrivial domain assumptions. State that D12's
conditional-measure result stands independently of that correspondence.

### B11 — Paper 13 violates its own “real universe” language gate

**Severity:** major

The frozen protocol permits “real law of the universe” only after empirical
selection and novel holdout prediction. Yet Paper 13 concludes:

> “The real interactive click law ... is the conditional law of the
> universe's complete non-Markov whole-history process.”

No such process for our universe was selected. The statement is true only as
a conditional tautology: if a complete path measure is supplied, its
conditionals give next-extension probabilities. It does not show that our
universe has the specific profinite diamond sample space, exact durable
projector ontology, locality properties, or process representation asserted.

**Required repair:** replace `real/actual law` claims with `universal
conditional representation for any supplied compatible whole-history
measure`. Reserve claims about our universe for an independently selected
process and holdout predictions.

### B12 — The final theorem quantifies over premises not realized by its countermodels

**Severity:** major

Theorem 3 says the exact quarter- and half-iSWAP models satisfy the full
`A_SHARD` package, including typed connected locality, construction-order
gauge, projective history restriction, seal-and-birth, and integrated
record/decoherence semantics. The executables establish the matrix and finite
probability portions, while the missing ontology is supplied by labels.

The theorem can already be narrowed to a useful claim:

> The explicitly tested algebraic, symmetry, type-cardinality, finite
> projective, and disjoint-commutation constraints do not select `theta`.

It cannot yet claim two complete models of every frozen premise. Under the
protocol's own verdict rule, an unexecuted promised object or decisive gate is
`INCOMPLETE-INVESTIGATION`.

**Required repair:** either build two genuinely complete typed models through
U1–U7, or narrow the theorem and verdict to the constraints actually
implemented.

## Frozen-gate adjudication

| Gate | Hostile finding |
|---|---|
| U0 corpus compatibility | **PARTIAL.** The evidence/content and fixed-ledger distinctions are careful; seal persistence is still overread as forced successor birth. |
| U1 finite diamond ontology | **FAIL.** Most frozen fields are absent from runtime types. |
| U2 local evidence clock | **PARTIAL.** `exp(-I)` is checked separately, not coupled to generated commits or shown to represent the whole-history law. |
| U3 whole-history/projective law | **PARTIAL.** Correct finite examples and one deletion, no variable-history projective family. |
| U4 construction-order gauge | **FAIL at registered scope.** Only disjoint matrix commutation. |
| U5 seal, birth, observation | **FAIL.** Pointer projection, durable record, birth, and truncation are not separately implemented. |
| U6 interaction locality | **FAIL as implementation.** Connected ownership is metadata, not a checked prior collar. |
| U7 integrated gauge | **FAIL.** One common unitary basis change plus a separate endpoint template. |
| U8 uniqueness/underdetermination | **PASS at tested finite-constraint scope; OPEN at full `A_SHARD` scope.** The counterexamples are exact, but not full registered diamond models. |
| U9 empirical selection | **NOT ATTEMPTED, correctly.** No law of our universe is selected. |
| U10 geometry after law | **PASS.** Geometry is correctly refused and no new dial scan is performed. |

## Accepted results

Hostile review accepts these narrower statements:

- the `P_r` family exactly demonstrates that lower-order marginals do not
  identify a finite three-record joint law or its continuation;
- the quarter-/half-iSWAP pair exactly demonstrates that the tested common
  symmetries, conservation law, unitarity, and type cardinalities do not fix
  the interaction angle;
- exponential evidence survival and a fixed-ledger commitment coefficient do
  not select an interaction matrix merely because both packets can share
  them;
- disintegration recovers conditional probabilities from a supplied positive
  finite history law;
- D11's extinction theorem remains valid for its terminal globally raced
  packet and does not prove extinction of every continuing architecture;
- profinite/cylinder consistency, when actually supplied, preserves rather
  than selects a measure;
- favorable geometry cannot select a law after the fact, so D12's refusal to
  run new cone and dimension scores is correct; and
- the current SHARD record principles have not uniquely selected an
  interaction, extension grammar, or whole-history measure.

## Verdict

**MAJOR REVISION / `INCOMPLETE-INVESTIGATION`.** The nonuniqueness program has
found a real result, but Paper 13 reports a schematic finite quantum example
as the restored sealed-diamond process promised by the protocol. The missing
objects are exactly the difficult ones: local extension support, physical
record creation, collar birth, independent-frame transport, canonical
construction fibers, and an actual projective variable-history measure.

Do not discard the no-go. Narrow it. The proper round-1 conclusion is:

```text
TESTED STRUCTURAL PRINCIPLES DO NOT SELECT THE FINITE INTERACTION
COMPLETE HISTORY MEASURE WOULD DETERMINE CONDITIONAL EXTENSIONS
BUT EXTENSION GRAMMAR, MEASURE, LOCAL REALIZATION, AND RECORD ONTOLOGY REMAIN
= INCOMPLETE-INVESTIGATION
```
