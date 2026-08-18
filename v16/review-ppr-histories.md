# PPR hostile review — histories, quotient congruence, and records

Seat: **H — histories/category/congruence/records**  
Target: Paper 3 candidate commit
`0f7a4b9bfc55be224143b2bc56bd4a5f5f51e5ee`  
Protocol: `v16/note-ppr-hostile-protocol.md`  
Review mode: repository read-only except this assigned report; independent
exact reconstruction in `/private/tmp`; no PPR implementation imported  
Grade: **ACCEPT-WITH-FIXES**  
Proposed adjudicated primary:
**`PPR-CONTEXTUAL-PULLBACK-CONSTRUCTED-BUT-LAW-UNSELECTED`**, only after the
finite, case-specific continuation-grammar qualification below is made
binding.

Normalized self-SHA-256:
`30c8877b6509f18a26123cd54be60f2265f5ec5b69f2b3f70569ef863fad772c`.
This is the SHA-256 of the complete UTF-8 report after replacing only the
64 hexadecimal characters in this field by 64 ASCII zeroes. This convention
allows the report to carry a non-self-referential integrity value in its own
bytes.

## 1. Bottom line

The exact finite mathematics I rebuilt is correct. The descending construction
does compute the greatest null family invariant under the **supplied finite
continuation graph**; the reported ranks and two strict rounds are right; all
supplied continuation arrows descend. The v12 co-live/co-merge criterion is
implemented correctly on the preserving and erasing controls. The registered
partition censuses, the three comparison paths, and the relevant hostile
mutants also reproduce exactly.

The candidate nevertheless compresses four different levels too aggressively:

1. the null grammar has only two continuation arrows;
2. the support-record positive and eraser are two separately evaluated future
   cases, not one globally quantified future semigroup;
3. the exhaustive partition fixtures are separate again, and the
   multiple-maximal one uses a non-complete lossy map; and
4. the relational event, null, pullback, and record fixtures are compatible
   neighboring constructions, not one typed history law whose records generate
   its quotient.

Those facts do **not** kill the ninth registered outcome, because that outcome
already withholds the record-generated fixed point and the paper explicitly
admits finite-grammar relativity. They do require the title/headline language
“permanent,” “durable,” and “all licensed futures” to be read only relative to
the exact case-specific grammar under test. If the intended licensed grammar
is instead the union of every future map appearing anywhere in the fixture,
then the record is erasable and outcome 5,
`PPR-BLOCKED-AT-RECORD-PERMANENCE`, is forced. The adjudication must choose and
state one of those two typings; the candidate currently slides between them.

## 2. Frozen-target and process audit

I recomputed the target hashes directly:

| artifact | protocol value | mine | result |
|---|---|---|---|
| scorer | `c7f1cfb63b179746d0a66f28c1a6ec79975f8489a025d1196a2531d9fee069d6` | same | PASS |
| fixture | `cecc3b0d3c7bf46503481fa7b422e915ba0ff6aac42e3cec5f61c395e565b389` | same | PASS |
| transcript | `0c85efb4186e0faf6afc55f06184e9351bd6df621297ab2155745d7106e45b05` | same | PASS |
| receipt | `dc88d6a2fbcf350785cc5f12cdcb8ea0805c4df6deaacac9ceffd34b1699c630` | same | PASS |
| Paper 3 | `ca7b06e9e5540d81afb4a401beb66cb2834e3e74033fd742ac5257108a19654f` | same | PASS |

The candidate commit has the three generated artifacts as additions and parent
`49e93ab...`; the verification commit `6eba1d400ec460bb8b85d117f8679c14365378fe`
has the candidate commit as parent and adds only its verification note. The
first physical invocation is honestly retained as a pre-gate serialization
failure. The repaired scorer delta described in ledger #37 is the bounded
exact-object/serialization repair; the fixture did not move.

An independent clean replay wrote three fresh scratch artifacts and reproduced
all three committed hashes byte-for-byte at 25/25. The fixture contains no key
named `expected`, `result`, `verdict`, or `outcome`. Independent AST scans find
zero floating constants in either `ppr_core.py` or `ppr_score.py`.

The histories-relevant registered mutants all refused before writing:

| mutant | exit | first refusal |
|---|---:|---|
| `split-weight` | 1 | `PPR-HISTORY-REFINEMENT` |
| `dark-reactivate-drop` | 1 | `PPR-STABLE-NULL-DESCENT` |
| `null-promote` | 1 | `PPR-STABLE-NULL-DESCENT` |
| `eraser-ignore` | 1 | `PPR-RECORD-AVAILABILITY` |
| `record-preplant` | 1 | `PPR-PARTITION-CENSUS` |
| `comparison-phase` | 1 | `PPR-COMPARISON-COCYCLE` |
| `loop-conflate` | 1 | `PPR-COMPARISON-DYNAMICS-TYPE` |

This secures the receipt mechanics for this seat. It does not settle the
quantifiers discussed below.

## 3. Type audit: what the candidate actually contains

The following objects must not be identified merely because the prose uses
the word “history” for all of them.

| name | implemented object | relation actually proved |
|---|---|---|
| relational configurations | two named finite labelled output graphs in `relational_wedge.branches` | their coarse graph signatures differ and survive one declared relabelling |
| syntactic complete histories | weighted matrix terms in several independent fixtures | no single global history catalogue joins all fixtures |
| history event algebra | declared prose plus two graph signatures and one split/merge class-operator identity | no Boolean/coarse algebra object is constructed in code |
| boundary objects | `cut` (4), `middle` (3), `final` (2) for null descent; separate 2/3/3 carrier spaces for the pullback | these are separately typed examples, not one common boundary category |
| continuation arrows | two null-grammar matrices; separate record futures; separate graph-edge transports | each family is checked internally; there is no common arrow registry |
| quotient family | kernels of accumulated observation constraints on the three null boundaries | every one of the two supplied null arrows descends |
| class operators | exact weighted sums in interference and law fixtures | individual completeness/interference identities pass |
| record partitions | support criterion on one first leg plus preserving/erasing futures; four independent partition censuses | finite case results only |
| actualization | a prose postulate that one complete recorded successor occurs | no selector, sample, or dynamical map is built; correctly withheld |

This table matters for two conclusions.

First, the paper is entitled to say that it built compatible examples of each
layer. It is not entitled to say that records **generate** the quotient or that
one law reproduces the typing it presupposes. The paper itself withholds the
record-generated fixed point, so this is a scope repair rather than a kill of
outcome 9.

Second, “all registered continuations” is ambiguous. In the null theorem it
means the two arrows in `stable_null.continuations`. In the support-record test
it means one future matrix per call. In each partition census it means the list
stored in that case. It cannot mean the union of all maps in the fixture,
because those maps do not even share one declared boundary category and the
eraser deliberately destroys the record.

## 4. Exact reconstruction of the stable-null theorem

For each boundary `B`, let

`N0[B] = ker O[B]`

and define the monotone operator on families of subspaces

`F(N)[B] = N0[B] intersection all_(e:B->B') C[e]^-1 N[B']`.

Starting at `N0`, the chain `N(k+1)=F(N(k))` descends. In finite dimension it
stabilizes. If `S` is any family with `S subseteq N0` and
`C[e]S[B] subseteq S[B']` for every supplied edge, induction gives
`S subseteq N(k)` for all `k`; hence `S subseteq Ninf`. The fixed family is
therefore the greatest invariant null family for that exact finite edge set.
This proves the generic theorem; it is not merely a fixture observation.

My independent rational implementation, importing none of the candidate code,
recovered:

```text
rank history:
  (cut=1, middle=1, final=1)
  (cut=1, middle=2, final=1)
  (cut=2, middle=2, final=1)
strict rounds: 2
Ninf[cut] = span(e2,e3)
```

The delayed direction `e1` is initially null and later read by
`O_final C_middle-final C_cut-middle`; `e2` and `e3` are not read by the
registered chain. Thus the candidate’s 3-to-2 null-dimension statement and
its “presently dark is not gauge” negative are exact.

### What the theorem does not quantify over

The scorer constructs the null edge list only from the two JSON entries at
`ppr_score.py:524-535`. The history split, graph relabelling, spectator,
disjoint gluing, record futures, comparison routes, and graph readouts are not
arrows in this multi-sorted family. Therefore the sentence “no licensed
preparation, continuation, spectator, or readout can ever distinguish them”
is proved only if “licensed” is stipulated to mean the two-arrow null grammar
and its three immediate observations. It is not established for every
operation used elsewhere in Paper 3.

This is not a defect in the fixed-point algebra. It is an incompleteness of the
common typing. A future paper may weld those separately typed operations into
one grammar and rerun the descent.

## 5. Mandatory new continuation

I added a new typed boundary `probe` of dimension 1, observation `[1]`, and a
future arrow from `cut` to `probe`

```text
C_new = [0 0 0 1].
```

This reads the direction `e3` that is stable-null in the candidate grammar.
The same independent fixed-point algorithm then gives

```text
Ninf_extended[cut] = span(e2),
```

with constraint-rank history

```text
(cut=1,middle=1,final=1,probe=1)
(cut=2,middle=2,final=1,probe=1)
(cut=3,middle=2,final=1,probe=1).
```

This is a **typed reactivation**, but not a counterexample to the finite
theorem: `C_new` was not licensed by the frozen grammar. Its exact lesson is
the one the paper already states at lines 91-93: stable-null is
grammar-relative. It does refute any unqualified reading of “permanently
unphysical” or “every future operation allowed by the model,” because the
model does not yet possess a generative closure rule deciding whether this
probe is allowed.

## 6. Contextual pullbacks and overlap composition

The identity

`<U_alpha x,U_beta y> = <x,U_alpha^dagger U_beta y>`

is exact by adjointness whenever the two continuations have one common
codomain. It proves that no additional bilinear form is operationally needed
for that **chosen** common future context on the reached subspaces. It does not
select the common endpoint or its continuation maps; Paper 3 correctly calls
the result contextual.

For the comparison diagram I independently obtained

```text
R Z I = R Z = R Z
```

for the three declared routes `01-12-23`, `02-23`, and `03`. Gauge-frame
conjugation preserves their equality. Matrix multiplication also makes any
parenthesization of one supplied path associative.

What is not proved is a free three- or four-overlap coherence theorem. The
direct edges `02`, `13`, and `03` are supplied with their composite values in
the fixture. The positive result is therefore one commuting four-boundary
diagram with a closing-edge tamper, not a theorem that arbitrary pullback
contexts form an associative/cocyclic comparison system. That stronger claim
remains a gluing obligation.

## 7. Independent v12 record reconstruction

The v12 criterion has two distinct hypotheses for a declared partition:

- correlation: alternatives simultaneously live after the first leg occupy
  distinct sectors;
- availability: alternatives co-fed into one later configuration occupy one
  sector.

Equivalently, the transitive co-merge partition of the future must separate
every co-live pair of the first leg. I reimplemented the support calculation
directly.

For the PPR first leg the co-live pairs are exactly

```text
(0,2), (1,3).
```

The preserving future has co-merge blocks

```text
(0,1), (2,3),
```

so a record structure exists. The erasing future has blocks

```text
(0,2), (1,3),
```

and therefore fails on both co-live pairs. These are the candidate’s exact
results. They establish correlation/availability and, through the inherited
v12 support theorem, loss or survival of the composition defect. They do not
establish actualization.

### A new appended future

I appended to the preserving future a rational orthogonal `5-12-13` rotation
that mixes the two record sectors:

```text
E = [[ 5/13, 0, 12/13, 0],
     [ 0, 5/13, 0, 12/13],
     [-12/13,0, 5/13, 0],
     [ 0,-12/13,0, 5/13]].
```

`E^T E = I` exactly. For `E * preserving_future`, the co-merge partition is
the single block `(0,1,2,3)`, so the same co-live pairs are no longer
separated. The record is erased by this new lawful linear continuation.

Again, this is not a counterexample at the registered grammar: `E` is a new
generator. It proves that the positive claim is exactly
**case-grammar-relative**. “Append-only” must be a restriction on the licensed
future law, not a conclusion inferred from the present record.

### Correlation, permanence, decoherence, and actuality remain distinct

- Correlation is created by the first leg.
- One-future availability is decided by that future’s co-merge partition.
- Permanence means availability/recoverability for every word in a fixed
  licensed future grammar.
- Decoherence or zero composition defect follows under the v12 support
  hypotheses; it is not the occurrence of one alternative.
- Actualization is nowhere derived and is correctly retained as a postulate.

The paper should not use “record,” “permanent record,” and “actualized fact” as
interchangeable words. Most of its prose already respects this; its headline
sentences need the same discipline.

## 8. Partition-census audit

My independent set-partition generator gives Bell numbers `B2=2` and `B4=15`
and reproduces all four finest sets:

| case | independently reconstructed finest stable partitions |
|---|---|
| `block_record` | `((0,1),(2,3))` |
| `coherent_pair` | `((0,1))` |
| `erasable_tag` | `((0,1))` |
| `multiple_maximal` | `((0,1,2),(3))`, `((0,1,3),(2))` |

The multiple-maximal continuation has

```text
C^dagger C = diag(0,0,1,1),
```

not the identity. It annihilates directions 0 and 1. Its two maximal
partitions are therefore a valid combinatorial control of the census routine,
but not evidence of a physical ambiguity between two complete durable record
instruments. The paper’s restrained phrase “a case with two maximal
partitions” is acceptable; any ontological promotion of that case should be
forbidden in adjudication.

The block-record positive is stronger: its supplied continuation is block
preserving, so every word generated by that one map preserves the partition.
That is the clean positive permanence result, at the single-generator grammar.

## 9. Do records generate the null quotient?

No. The null family is computed from observation kernels on dimensions
`4 -> 3 -> 2`. The record constructions use unrelated `4 x 2`, `4 x 4`, and
small decoherence/continuation matrices. No functor maps the record sectors to
the quotient basis, no equality says the record radical equals `Ninf`, and no
iteration feeds one construction back into the other.

They are compatible side by side: delayed visibility is not prematurely
quotiented, and erasable tags are not called durable in the exact rows. That
compatibility is useful. But it is not the self-consistent fixed point. Paper 3
explicitly withholds outcome 10, so the correct repair is to say “parallel
compatible constructions” wherever “the same law produces both” might be
inferred.

## 10. Literature and attribution boundary

The cited primary papers support only the structural analogies claimed at the
end of Paper 3:

- Craig treats a positive decoherence functional as a semi-inner product on
  history operators and consistent histories as orthogonal sets
  ([arXiv:quant-ph/9704031](https://arxiv.org/abs/quant-ph/9704031)).
- Gudder proves Hilbert-space representations of decoherence functionals and,
  for finite systems, uniqueness of a spanning representation up to
  isomorphism; strong positivity is tied to Hilbert representation
  ([arXiv:1011.1694](https://arxiv.org/abs/1011.1694)).

Neither source selects PPR’s relational event algebra, its future grammar, its
record partition, or its weights. Paper 3 explicitly says that those
precedents do not select the event algebra or weights. I found no attribution
overreach in the histories/GNS paragraph.

## 11. Findings, ordered by severity

### H1 — MAJOR: “all licensed futures” has no single typed quantifier

The null, support-record, census, graph, and spectator continuations inhabit
separate fixtures. The positive support future and eraser are evaluated
separately. The paper’s result paragraph can therefore be read as quantifying
over a union grammar that the code never constructs—and under such a union the
record is explicitly erasable.

Required replacement sentence:

> Relative to each explicitly declared finite continuation case, the null
> quotient is stable under every arrow in that case and the block-record
> partition is recoverable under every word of its one-generator preserving
> grammar; the fixture does not construct one generative future grammar
> containing all null, record, spectator, and rewrite operations.

Kill rule: if adjudication insists that all future matrices in the fixture are
licensed continuations of one boundary law, select
`PPR-BLOCKED-AT-RECORD-PERMANENCE`.

### H2 — MAJOR: the event/null/pullback/record objects are not one law

The paper correctly withholds a record-generated fixed point, but phrases such
as “the same law” and “the right type of object on which a law must live” make
the parallel fixtures sound welded. No common history algebra or functor is
implemented.

Required replacement sentence:

> Paper 3 constructs mutually compatible finite representatives of the event,
> null-quotient, contextual-pullback, and record-permanence requirements; it
> does not yet construct one history law whose record structure regenerates
> its own quotient typing.

### H3 — MAJOR: the registered congruence theorem covers only two arrows

The generic greatest-fixed-family theorem is correct, but the physical
instance does not type the registered history refinement, spectator, disjoint
gluing, record futures, or graph readouts as arrows of that family. Thus
“preparation, continuation, spectator, or readout” is broader than the gate.

Required replacement sentence:

> The computed quotient is a congruence for the two supplied arrows and three
> immediate observation maps of the frozen null grammar; congruence under the
> separately tested refinement, spectator, record, and rewrite operations is
> not yet typed in one common category.

### H4 — MINOR: comparison coherence is one closed diagram, not an overlap theorem

All three paths agree exactly, including the direct `03` edge, but several
edge values are supplied as composites. This is a good fixture and tamper,
not a general three-/four-overlap associativity result.

Required replacement sentence:

> One four-boundary comparison diagram, including its direct closing edge,
> commutes exactly and covariantly; arbitrary overlap gluing and cocycle
> coherence remain open.

### H5 — MINOR: multiple-maximal is a lossy combinatorial control

The relevant continuation is not complete. Keep the count, but do not cite it
as physical record ambiguity.

Required replacement sentence:

> The lossy multiple-maximal case validates that the partition census can
> return nonunique maxima; it is not a complete physical record instrument.

### H6 — NOTE: the mandatory new futures confirm, rather than refute, the declared wall

The new `e3` probe shrinks the stable-null family, and the new rational
cross-sector isometry erases the positive record. Both are outside the frozen
grammar. They verify that the grammar-relative limitation is substantive and
must appear at every permanence claim.

## 12. Numbered repair/kill list

1. Bind “licensed future grammar” separately for the null, support-record, and
   partition-census cases; do not quantify over an untyped union.
2. Change every unqualified “permanent/durable” claim to “stable/recoverable
   under the declared finite preserving grammar.”
3. Add an explicit object-separation table stating that the event, null,
   pullback, and record fixtures are not one generated law and do not earn the
   fixed point.
4. Scope the comparison result to the one registered four-boundary diagram.
5. Label the multiple-maximal continuation non-complete and its result
   combinatorial-only.
6. Retain actualization as an independent postulate; do not infer occurrence
   from support separation, zero defect, or stable quotienting.
7. Preserve the candidate primary only under the case-specific grammar
   reading. If the union-grammar reading is intended, kill the primary at
   `PPR-BLOCKED-AT-RECORD-PERMANENCE`.

## 13. Grade and proposed adjudication

**ACCEPT-WITH-FIXES.** I found no counterexample to the exact finite
stable-null theorem, quotient descent, pullback identity, v12 support
criterion, preserving/eraser contrast, or registered path equality. The new
continuations do exactly what a grammar-relative theory predicts: they change
the quotient/record once the grammar is enlarged. The current primary can
survive because it withholds the unified fixed point and the law selector.

The primary survives only with a binding scope sentence:

> `PPR-CONTEXTUAL-PULLBACK-CONSTRUCTED-BUT-LAW-UNSELECTED` at finite exact,
> case-specific declared-continuation scope; the null, pullback, record, and
> rewrite constructions are compatible but not yet one self-generating
> history law, and neither permanence under a generative catalogue nor
> actualization is proved.
