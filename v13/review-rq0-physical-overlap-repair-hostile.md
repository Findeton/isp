# HOSTILE REVIEW — v13 RQ0 PHYSICAL-OVERLAP REPAIR

Reviewed exact commits:

- pin `b05ab95d6721d104a561875bc39aa6daa03f875e`;
- delivery `8d071641ecc3d028c4ee3355e4faacb368840e95`.

Repository remained read-only and clean. I independently rebuilt the algebra in `/tmp/rq0-hostile.VgPEDf/rebuild.py` using exact \(\mathbb Q(\sqrt2)\) arithmetic without importing or copying the delivery implementation. Rebuild SHA-256:

```text
31202dcf13fe73c135b98c38168d974f2616d2879a4b144720e2b479fd04272a
```

## Verdict

**ACCEPT-WITH-FIXES**

Highest secure rung:

\[
\boxed{\texttt{RQ0-FACT-DESCENT}}
\]

at the declared finite, fixed-carrier, signed-permutation/common-relabelling amplitude-subinstrument scope.

I found no counterexample to the finite construction and no reason to lower the mathematical rung. I did find three major implementation/provenance defects in the receipt layer. They must be forward-repaired before terminal status. No `RQ0-L0`, `RQ0-C1`, field, or gravity work should begin before that repair is verified.

## Severity-first findings

### MAJOR M1 — the final outcome block is declared, not derived

**Scope:** delivery `8d07164`, `v13/code/rq0_physical_overlap_exact.py:2671-2698`, `2846-2847`, `2877-2885`; note lines `514-527`; LOG #17 lines `693-703`.

The executable assigns:

```python
"RQ0-REGIONS-CONSTRUCTED": True
"RQ0-REGIONAL-SITE": True
"RQ0-FACT-DESCENT": True
```

and the three blocked outcomes as literal `False`. It then compares these declarations with identical expected values. “Highest honestly restored rung” compares the same literal string with itself, while the successor-nonclaim gate counts a locally constructed six-item tuple.

These are precisely the constructor-restatement/self-comparison gates forbidden by RUNBOOK lines 128-136.

The supplied mutant makes the defect observable: the active-pin anchor fails and the process exits 1 with `76 pass, 1 fail`, but all four outcome checks still pass and the text renderer still prints:

```text
highest restored rung: RQ0-FACT-DESCENT
```

Thus `77/77` is a true count of equality comparisons in the normal run, but not a count of 77 independent falsifiable scientific gates.

This does not invalidate the underlying measurements: my independent rebuild recovers the positive rung. It invalidates the receipt’s claim that the rung was mechanically earned.

**Required repair**

- Store named prerequisite measurements.
- Derive each rung from its frozen prerequisite vector.
- Derive blocked outcomes from the first failed prerequisite.
- Suppress every positive verdict if any required anchor or prerequisite fails.
- Do not count outcome labels or prose nonclaims as scientific checks.
- Regenerate both receipts and rerun the mutant.

**Replacement sentence**

> Rung status is computed from named prerequisite measurements. Any failed anchor or prerequisite suppresses the positive verdict; outcome labels and declared nonclaims are not counted as independent checks.

Do not preserve `77` as a target; report whatever count the repaired, nonduplicate gate set actually has.

---

### MAJOR M2 — same-file digests authenticate the delivery, but do not establish independent predeclaration

**Scope:** pin `b05ab95`, lines `113-118`, `233-238`; delivery code lines `28-29`, `470-670`, `1673-1794`, `2060-2134`; delivery note lines `239-256`; LOG #17 lines `654-658`.

`MASTER_SPEC_SHA256` and `CONSTRUCTION_SURFACE_SHA256` are constants in the same file as the constructor and structural predicate they authenticate. Neither exact digest nor the exact master construction appears in commit #16. Consequently they establish:

- exact reproduction of the delivered source/specification;
- detection of accidental drift unless both implementation and constant are changed;
- evaluation order inside the executable.

They do **not** independently establish that the exact construction was historically frozen before its author inspected the desired fact relation. Calling the master “predeclared” overstates what these locks prove.

The associated AST audit is also only a blacklist of direct `Name` nodes. It is not a general noninterference proof.

The important substantive result survives direct audit:

- `build_amplitude_family()` has no arguments;
- it calls no marginal-law, requested-map, GHZ, coordinate, metric, or field routine;
- the memory readout and all six embeddings are fixed as part of the jointly constructed witness;
- marginal comparison occurs later;
- `physical_bridge_accepts` does not inspect marginal laws.

Thus this is a provenance/wording defect, not circularity in the finite existence theorem.

**Required repair**

Separate three notions explicitly:

1. immutable Git provenance;
2. same-file canonical-spec authentication;
3. structural validation independent of laws.

For future units, if historical pre-registration is required, commit the canonical machine-readable specification or its digest before construction/evaluation. That cannot be retroactively proved for #17.

**Replacement sentences**

> The canonical master, admissible morphism class, embeddings, and readouts are constructed and digest-checked before any marginal-law comparison in the executable. The same-file digests authenticate the delivered surface and evaluation order; they do not independently prove historical pre-registration.

And in the headline, replace “one predeclared finite master instrument” with:

> one fixed, canonically authenticated finite master instrument.

---

### MAJOR M3 — the post-selected controls are rejected by container/schema identity, not by a typed structural test

**Scope:** delivery code lines `1511-1561`, `1848-1868`, `2515-2560`; delivery note lines `422-449`.

`ghz_law_extension` returns a generic mapping containing matrices, support, and laws. It does not return an `Instrument` or candidate `InstrumentMorphism`.

`physical_bridge_accepts` first demands the positive-family keys and exact positive-family digest. The diagonal and anti-diagonal mappings therefore fail immediately because they are not the frozen family. The executable does not measure a typed boundary-map, arrow-map, or intertwiner obstruction for them.

This is stronger than merely saying “matching laws do not make the positive digest appear,” but weaker than the note’s claim that the controls were structurally tested against the morphism schema.

There is nevertheless an exact structural obstruction. My rebuild confirms both controls are 16-dimensional, whereas the frozen admissible class uses signed-permutation maps on fixed eight-dimensional carriers. No well-typed signed-permutation boundary map exists between those dimensions. The claimed rejection is therefore mathematically correct but not executable for the stated reason.

`physical_bridge_accepts` also conflates authentication with validation: even a gauge-equivalent re-presentation of the positive family would fail its digest before structural validation.

**Required repair**

- Represent both law-only controls as typed amplitude instruments.
- Separate `matches_frozen_spec` from `validate_structural_bridge`.
- Feed explicit candidate morphisms into the latter.
- Print and gate the exact rejection reason—here, incompatible carrier dimension under the fixed signed-permutation class.
- Preserve the separate rogue invariant test.

**Replacement sentence**

> The diagonal and anti-diagonal controls are typed 16-dimensional amplitude instruments. They have the same three fair marginals, but no well-typed signed-permutation boundary map into the fixed eight-dimensional master exists; the executable checks this structural obstruction before rejecting either control.

---

### MINOR M4 — “site” is project-local terminology unless a topology is declared

**Scope:** pin lines `143-147`, `315-318`; delivery code lines `373-380`, `1128-1247`; delivery note lines `291-344`.

The five-object object is a legitimate thin finite category:

- five amplitude-instrument objects;
- twelve validated morphisms;
- identities and closed composition;
- pair/triple pullbacks;
- a declared three-region cover.

This satisfies the pin’s expressly stipulated `RQ0-REGIONAL-SITE` rung. I therefore do not downgrade that rung.

In standard category-theoretic terminology, however, no Grothendieck topology, coverage axioms, or generated topology is explicitly part of `RegCategory`. The most literal current name is “finite cover category” or “finite amplitude atlas.”

**Required repair**

Either declare the Grothendieck topology generated by the displayed cover and verify its finite base-change/transitivity data, or use the more precise cover-category terminology while retaining the internal rung name.

**Replacement sentence**

> The five-object thin category with its declared regional cover is a finite amplitude-subinstrument cover category—the programme’s `RQ0-REGIONAL-SITE` rung. No general Grothendieck topology is claimed here.

---

### MINOR M5 — the headline’s “non-padding” adjective needs its finite gauge scope attached

**Scope:** delivery note lines `17-18`, `24-26`; LOG #17 lines `644-652`.

The detailed body scopes the result correctly to all \(8!\) common carrier relabellings and the \(4\times2\) split. The headline does not carry that qualifier and could be read as arbitrary-unitary irreducibility.

My independent search actually strengthened the finite result: for each \(D_a\), zero of 40,320 relabellings even makes all five **support patterns** simultaneously product-compatible. Since boundary signs cannot alter support, signs cannot rescue a product factorization.

No arbitrary-unitary tensor-factorization theorem follows.

**Replacement sentences**

> Three equal-dimensional finite quantum regional instruments, non-padding under the exhaustive common-configuration-relabelling \(4\times2\) test, occur as typed subinstruments of one fixed finite master instrument.

> No irreducibility under arbitrary unitary changes of tensor factorization is claimed.

---

### MINOR M6 — several remaining receipt gates are declarative, duplicate, or weaker than their labels

**Scope:** delivery code lines `669`, `2034-2049`, `2353-2357`, `2446-2493`, `2710`, `2778`, `2797-2798`, `2810`, `2821`, `2832`.

Examples:

- the coupling graph is supplied as literal edges and then checked for connectedness rather than derived from amplitudes;
- category gate #51 repeats the composition component already included in #50;
- the positive refinement gate revalidates the same \(j_1\) already covered by the embedding gate;
- the old-shadow rejection is intentionally only an `isinstance` type control;
- the mutant changes the expected hash rather than corrupting the observed anchor value;
- several JSON science fields are literal semantic declarations, including `fact_comparison_occurs_after_digest_gate`, `master_is_local_witness_not_global_universe`, `structural_accepts_postselected_controls`, and `marginal_laws_used_as_fact_criterion`.

These do not alter the finite algebra, but the receipt should distinguish measurements, type controls, semantic declarations, and duplicated summaries.

**Required repair**

- Derive interaction participation from matrix support/factorization data or label it “by construction.”
- Deduplicate the category/refinement gates.
- Source JSON claims from measured variables.
- Make the mutant alter the observed digest/input in memory and verify that the derived outcome closes.
- Print separate counts for measurements, type/schema controls, anchors, and semantic declarations.

## Independent claimed-versus-rebuilt table

| Quantity | Delivery | Independent rebuild |
|---|---:|---:|
| regional carrier dimensions | \(8,8,8\) | \(8,8,8\) |
| all regional/core/master arrow instances unitary | true | true |
| write \(H_{\rm corr}\), all 8 basis preparations | true in every \(D_a\) | true |
| no-write \(H_{\rm corr}\) | false in every \(D_a\) | false |
| both preserves \(H_{\rm avail}\) | true in every \(D_a\) | true |
| preserving cross/within coherence | \(0/0\) | \(0/0\) |
| preserving \(\Delta^B\) support | \(0\) | \(0\) |
| preserving record residual | defined, support \(0\) | defined, support \(0\) |
| eraser \(H_{\rm avail}\) | false in every \(D_a\) | false |
| eraser residual | undefined | undefined |
| eraser cross-coherence / defect | \(16/16,\ 32/32,\ 32/32\) | exact match |
| preserve support multisets | \(\{8,8\},\{8,16\},\{8,32\}\) | exact match |
| preserve-after-write supports | \(\{16,16\},\{16,32\},\{16,64\}\) | exact match |
| old padded q=3 control | identity product witness | all 4 arrows rank-one at identity |
| positive anti-padding | no witness in \(3\times40{,}320\) | exact match |
| support-only product candidates | not reported | \(0,0,0\) |
| six positive embeddings | all valid | all valid |
| mapped-arrow mutant | false for all \(j_a\) | false for all |
| nonmonomial boundary control | unitary, not signed permutation | exact match |
| `Reg` objects/arrows | \(5/12\) | \(5/12\) |
| composable pairs | 22 | 22, all closed |
| pair/triple intersection | three-arrow core | exact match |
| regional union | master arrow family | exact match |
| pullback lower-bound failures among 5 objects | \(0,0,0\) | \(0,0,0\) |
| lower-bound failures among all 512 master-arrow subsets | not reported | \(0,0,0\) |
| record-projector ranks | implicit \(4,4\) | \(4,4\) |
| six embedding projector pullbacks | all true | all true |
| derived record algebras | 5 | 5 |
| `Rec` morphisms / composable laws | \(12/22\) | \(12/22\) |
| three \(E\to D_a\to O\) paths | equal direct restriction | exact match |
| diagonal support | \(000/111\) | exact match |
| anti-diagonal support | \(010/101\) | exact match |
| three marginals | fair in both controls | exact match |
| forced pair maps | id/id/id versus comp/comp/id | exact match |
| rogue stability and fair law | true | true |
| rogue/master preserve invariant matches | 0 of 4 | 0 of 4 |

For the rogue, the obstruction is especially transparent independently: its preserve has 16 nonzero Born entries split between \(9/25\) and \(16/25\), while the four master preserves have respectively 8 entries of \(1\), 8 entries of \(1\), 16 entries of \(1/2\), and 32 entries of \(1/4\). Signed row/column permutations cannot change these multisets.

## Attack-surface adjudication

### Pre-comparison and no-circularity

The constructor is law-blind in the delivered source. Equal laws cannot make `physical_bridge_accepts` true. The master is, however, a jointly designed witness, and its same-file digests are authentication rather than independent pre-registration. That distinction must be explicit.

### Quantum seams

Every load-bearing seam number is reproduced. The eraser counts are exactly \(16/16\), \(32/32\), and \(32/32\). No float, tolerance, or random path was found.

### Anti-padding and diversity

The rearrangement-rank criterion is correct: an \(8\times8\) matrix is \(A_4\otimes B_2\) only if its \(16\times4\) realignment has rank one, and the pivot-cross equations are exact rank-one tests. The exhaustive search covers all \(8!\) common relabellings. Factor exchange covers the \(2\times4\) presentation.

The preserve support multisets remain invariant under signed row/column permutations and preserve-label permutations. All three regions are separated at the declared scope.

### Morphisms and rogue exhaustion

All six positive maps satisfy:

- boundary typing;
- signed-permutation scope;
- total injective family-preserving arrow maps;
- exact intertwiners;
- preparation compatibility;
- record and configuration-projector pullback.

The mutant and nonmonomial controls behave as claimed.

The rogue search scope is complete: a family-preserving image of its regional preserve must be one of exactly four master preserve arrows. Born-entry multiset mismatch is a necessary-invariant obstruction under every admissible signed row/column permutation, so one failed regional-preserve image already forbids a full embedding.

### `Reg`, overlaps, and cover

`Reg` is a valid thin five-object category, not merely the old fact-value groupoid. Its simplicity is deliberate.

The current universal-property test is substantive only at that declared finite-object scope. Because order is defined by mapped-arrow-set inclusion and \(O\) is the exact intersection, the lower-bound statement also follows set-theoretically. My stress test over all 512 subsets of the nine master arrows found no additional lower bound outside \(O\). This does not establish a universal property in a larger category with independently presented objects or alternative boundary maps, and the note does not claim that.

The positive `Ref` is an amplitude-family inclusion. The old result is correctly named Born-shadow product coarse-graining.

### `FactIface` and `Rec`

Manual source audit confirms `record_functor` calls no marginal-law, GHZ-control, requested-fact-map, or law-only predicate. It uses frozen record candidates, \(H_{\rm corr}\), \(H_{\rm avail}\), and projector pullbacks.

All five record interfaces, twelve induced arrows, identities, compositions, and three master/core paths check exactly. All nonidentity value maps happen to be identities, so this is a simple descent witness, but a valid one.

The nine-arrow old object is correctly classified as `FactIface`-shaped and not `Reg`.

### Law-only controls

The amplitude algebra, supports, marginals, W3 status, and incompatible pair maps reproduce exactly. The code must improve the reason reported by the structural rejection, as described in M3.

The rogue establishes `SAME-LAW-NOT-SAME-FACT` throughout the exact declared morphism scope.

### Receipt reproducibility

Supplemental execution results:

- normal mode: exit 0, `77 pass, 0 fail`;
- JSON mode: exit 0;
- receipt verification: both complete text runs identical, both JSON runs identical, both stored receipts exactly regenerated;
- mutant: exit 1, exactly one visible failure, `76 pass, 1 fail`.

The mutant also exposes M1 because the positive verdict remains printed.

No substantive unexecuted branch, float, tolerance, randomness, numerical geometry, or imported legacy implementation was found.

## Claim register

| Claim | Classification | Review status |
|---|---|---|
| finite instrument/morphism schemas | definition | sound at declared scope |
| regional gauge and admissible signed-permutation class | postulate/scope choice | correctly limited to real signs/permutations |
| full basis preparation and configuration probe | operational-access postulate | correctly labelled |
| \(D_1,D_2,D_3,O,\mathsf E\) and six embeddings | existence construction | independently reconstructed |
| W3 occurrence/availability seam | inherited theorem instance plus exact measurement | reproduced |
| eraser recoherence and defects | exact measurement | reproduced |
| same-dimensional diversity | exact accessible invariant | reproduced |
| anti-padding | exhaustive finite measurement | reproduced and independently strengthened at support level |
| `Reg` category, intersections, cover | finite theorem instance | reproduced |
| standard “site” terminology | wording convention | needs M4 clarification |
| projector pullback and `Rec` descent | exact theorem instance | reproduced |
| diagonal/anti-diagonal ambiguity | exact counter-control | reproduced |
| rogue no-bridge result | exact necessary-invariant proof | reproduced |
| historical predeclaration | provenance claim | not established by same-file digests |
| black-box overlap discovery | not claimed | correctly absent |
| emergence or uniqueness | not claimed | correctly absent |
| arbitrary-unitary irreducibility | not established | headline needs explicit scope |
| full complex \(U(1)\) | not claimed | correctly absent |
| causal order, Lorentzian geometry, SR, fields, gravity | open/not constructed | correctly absent |

## Bounded repair specification

Keep commits #16 and #17 immutable. In one forward repair:

1. replace literal outcome booleans with prerequisite-derived outcomes;
2. fail closed and suppress positive verdict text on any required failure;
3. separate canonical-spec authentication from structural morphism validation;
4. type the diagonal/anti-diagonal controls and gate their exact dimensional/morphism obstruction;
5. classify same-file digests honestly;
6. scope “non-padding” in every headline;
7. either define the topology generated by the finite cover or use “finite cover category/atlas” in standard prose;
8. remove or relabel duplicate/declarative checks and source receipt fields from actual measurements;
9. strengthen the mutant to corrupt an observed anchor and confirm that the derived rung closes;
10. regenerate text/JSON receipts, run determinism twice, rerun the mutant, and obtain adjudicator verification.

No amplitude matrix, W3 count, support invariant, anti-padding result, embedding, overlap, rogue invariant, or `Rec` result needs to change.

## Final adjudication

\[
\boxed{\textbf{ACCEPT-WITH-FIXES}}
\]

\[
\boxed{
\text{Highest secure rung: }\texttt{RQ0-FACT-DESCENT}
\text{ at the declared finite amplitude-subinstrument scope.}
}
\]

The physical-overlap repair succeeds mathematically as a jointly constructed existence witness. Its terminalization is blocked only by the bounded receipt/provenance repairs above.
