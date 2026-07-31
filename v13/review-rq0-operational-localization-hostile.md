# HOSTILE REVIEW — RQ0-L0 OPERATIONAL LOCALIZATION

## Verdict

\[
\boxed{\texttt{REJECT}}
\]

The exact algebraic measurements are mostly correct, the estimator really was frozen before the fixture file existed, and the delivery does not smuggle causal or geometric structure. But neither positive L0 rung is secure.

The decisive obstruction is structural: the pinned primitive requires an operational composite-implementation table \(\mathsf{Comp}_D\), and independently addressable complements must pass a measured joint-implementation test. The frozen estimator’s input type omits \(\mathsf{Comp}_D\) completely and infers factorization from matrix-algebra closure. It therefore cannot distinguish two operational instruments with identical supplied matrices but different sets of admitted cross-factor composites.

The top rung also directly violates mandatory C10: the receipt counts 14 positive local objects while only 10 carry derived records; the four single-atom objects have empty record algebras.

Recommended current scientific status:

\[
\boxed{\text{No terminal positive L0 rung.}}
\]

If the hostile round’s exact two-world addressability countermodel is gated natively in a forward repair, the appropriate negative rung is:

\[
\boxed{\texttt{RQ0-L0-BLOCKED-AT-ADDRESS}.}
\]

Do not begin `RQ0-C1`.

---

## Reviewed immutable targets

| Object | Commit / independently verified SHA-256 |
|---|---|
| Strict pin | `f218dde7b73631f7fd6359582d7bf494990eb076` |
| Pin file | `02ed47ad0a294741e613639b02066797a2057fcfcd816edd81203f353b1f9a59` |
| Frozen estimator commit | `a5b71735fb80d7214e1cc4e5a389289572895d53` |
| Frozen estimator source | `0b8d90bad735f6574ee367dd0bf7e98bcc1c6f2854f7a12070c82bae84e063b8` |
| Delivery commit | `3572774435c8940993610c3204edf85b94627141` |
| Fixture/truth module | `ada6dcbce2e9686b7ab45523cb8e8937a0c98cbae6504fd95092cf60aa7388f5` |
| Scorer/runner | `60a9819790b4c81ff76c04ef14b0bb2e0dedeb41a516ec884bd11eebdfb61988` |
| Delivery note | `89f038ca2521a9c65f476693743d2a4bb7536905d41d2164fba82486284d2778` |
| Text receipt | `0297ac85c85743eb5ef0dc15ca4fdb07acf421b142019cc256da3f4d671e5068` |
| JSON receipt | `a073dd2da23d2236658b118ab3d0e19965ae12a1b5caafbac7e7ad1fc59144a5` |

Both ancestry relations

\[
f218dde7 \prec a5b71735 \prec 35727744
\]

were independently verified. The fixture and scorer paths are absent from the estimator-freeze commit. The estimator blob at the freeze and delivery commits is byte-identical.

---

# Ranked findings

## FATAL F1 — The pinned joint-implementation referent is absent

The pin defines the primitive operational instrument with a flat implemented-composite table \(\mathsf{Comp}_D\), explicitly stating that joint implementability must be inferred from the existence and exact law of admitted composites:

- `f218dde7:v13/note-rq0-operational-localization-pin.md:87–123`.

Its independently addressable-complement test then requires:

- independently selectable generators;
- exact joint implementation in \(\mathsf{Comp}_D\);
- faithful composition;
- closure and a product test:

`f218dde7:...pin.md:198–209`.

But `OperationalDataset` contains only preparations, interventions, contexts, probes, support actions, presentation actions, and records:

- `a5b71735:v13/code/rq0_l0_localization_estimator_exact.py:571–583`.

There is no composite table, no admitted-word relation, and no joint-implementation predicate. Dataset validation consequently cannot check it:

- `...estimator_exact.py:599–630`.

The factor search instead closes arbitrary matrix products synthetically and checks commutation, scalar intersection, and algebra dimensions:

- `...estimator_exact.py:1096–1155`.

The fixture likewise supplies no \(\mathsf{Comp}_D\):

- `35727744:v13/code/rq0_l0_fixtures_exact.py:278–298`.

### Exact underdetermination countermodel

Take the delivery’s preparations, matrices, contexts, probes, records, and gauge data unchanged. Define two operational instruments:

- \(D_+\): admits all required cross-block composites;
- \(D_-\): admits only identity and within-block composites, with no cross-block joint implementation.

Their serialized `OperationalDataset` objects are identical because that type has no \(\mathsf{Comp}_D\) field. The frozen estimator must return the same four-factor result for both. Under the frozen pin, however, \(D_+\) can pass addressability while \(D_-\) must fail it.

Therefore no estimator on the committed input schema can decide the pinned addressability property. This is a genuine access-underdetermination result, not a missing cosmetic check.

### Consequence

The exact result earned by the code is:

> a factorization of the generated intervention star-algebra.

It has not yet earned:

> independently addressable operational quantum subinstruments.

That blocks both `RQ0-LOCALIZATION-GROUPOID` and `RQ0-LOCAL-ATLAS` as presently defined.

---

## FATAL F2 — Four counted atlas objects violate mandatory C10

Mandatory C10 says:

> Every positive localized object counted toward the main atlas must contain a nonempty record algebra derived from its own write/preserve dynamics.

Evidence:

- `f218dde7:...pin.md:404–409`.

The estimator constructs every nonempty proper union of four atoms, whether or not a record attaches:

- `a5b71735:...estimator_exact.py:1165–1183`.

The delivery itself reports:

- 14 local objects;
- 10 record-bearing regions;
- single-atom objects carry no pair record.

Evidence:

- `35727744:v13/note-rq0-operational-localization.md:236–244`;
- `35727744:v13/code/rq0_l0_output.txt:17–23`.

My independent combinatorial reconstruction obtained exactly:

\[
14=4+6+4
\]

proper nonempty subsets of four atoms, of which only the six two-atom and four three-atom objects carry a pair witness:

\[
10=6+4.
\]

Thus exactly four counted positive objects have empty record algebras.

The receipt does not miss this accidentally: its expected attachment table explicitly accepts empty records on the singletons. It therefore passes a fixture property that contradicts the frozen mandatory control.

### Consequence

Even if F1 were repaired by interpretation, `RQ0-LOCAL-ATLAS` still fails its mandatory record condition.

Restricting the atlas after the fact to the ten record-bearing objects does not automatically repair it: intersections of those regions can be recordless singleton objects, so meet closure and record descent must be reconstructed at the revised scope.

---

## MAJOR F3 — The equal-law “no bridge” control is declared, not measured

C11 requires equal marginal laws with no common operational subinstrument or typed restriction bridge:

- `f218dde7:...pin.md:411–415`.

The fixture returns:

```python
"declared_bridge_type": "fixed-carrier operational isomorphism",
"bridge_exists": False,
"obstruction": "boundary_dimension_mismatch:4->8",
```

without constructing or enumerating candidate bridges:

- `35727744:v13/code/rq0_l0_fixtures_exact.py:488–499`.

The scorer then compares that typed `False` and obstruction string with the same expected values:

- `35727744:v13/code/rq0_l0_operational_localization.py:918–930`.

This is a circular receipt gate.

Moreover, \(4\neq8\) excludes only a bijective fixed-carrier isomorphism. It does not exclude:

- an isometric subinstrument embedding;
- a quotient or conditional expectation;
- a channel-level restriction;
- a shared record-algebra pullback.

Those are precisely the broader bridge types relevant to regional overlaps.

The record witnesses do have equal exact fair laws; that number survives. The absence of a physical bridge does not.

### Required replacement claim

> The control establishes equal fair record marginals across dimensions four and eight. It does not establish absence of every admissible subinstrument or record-restriction bridge.

---

## MAJOR F4 — Record “restrictions” are metadata, not checked descent maps

The pin requires commuting pair and triple diagrams in `Reg`, `FactIface`, and the contravariant record assignment:

- `f218dde7:...pin.md:256–260`.

The delivery’s `RecordRestriction` contains source and target indices, a handle, and a constant description string:

- `35727744:v13/code/rq0_l0_operational_localization.py:196–202`.

`build_restriction_categories` creates an arrow whenever the same record handle occurs in source and target:

- `...operational_localization.py:204–222`.

The triple “path law” checks only that three tuples of the form

\[
(\text{source},\text{meet},\texttt{"w0"})
\]

exist:

- `...operational_localization.py:895–917`.

It does not construct or compare:

- algebra homomorphisms;
- projector pullbacks;
- direct versus composite record maps;
- pair-to-triple composition;
- a distinct `FactIface` object.

Because all objects sit in one ambient algebra and use literally the same global witness matrix, an identity-inclusion theorem may be available. But the committed receipt does not type or check that theorem; it replaces it with handle equality and a constant string.

### Surviving result

The exact W3 witness rows and algebra-membership attachments survive.

### Unsupported result

Exact regional fact-descent diagrams do not yet survive.

---

## MAJOR F5 — Fail-closed behavior is incomplete

The observed estimator-anchor mutant works correctly:

- 55/56 checks;
- receipt invalid;
- both positive outcomes false;
- highest outcome `None`;
- exit status 1.

However, the general outcome logic has a separate fail-open path.

The runner sets:

```python
receipt_valid = procedural_valid
```

where procedural validity checks only anchors, caps, and classification:

- `35727744:...operational_localization.py:1034–1063`.

It separately sets status to `"INVALID"` when there is no highest scientific outcome:

- `...operational_localization.py:1080–1084`.

But `main()` exits according to `receipt_valid`, not status or existence of an outcome:

- `...operational_localization.py:1255–1262`.

Hence the exact Boolean case

\[
\text{procedural\_valid}=1,\qquad
\text{highest}=\varnothing
\]

produces:

\[
\text{status}=\texttt{INVALID},
\qquad
\text{exit code}=0.
\]

For example, a classified scientific mutation that makes `quotient.intervention_classes` fail can make `candidate_class_constructed=false` and `highest=None` while leaving `receipt_valid=true`.

In addition, cap/schema exceptions raised inside the estimator are uncaught by the runner. They exit nonzero, but do not print the pinned structured `RQ0-L0-INVALID` receipt.

### Required repair

Define validity so that:

\[
\texttt{receipt\_valid}
=
\texttt{procedural\_valid}
\land
(\texttt{highest}\neq\varnothing),
\]

unless a separately typed valid negative outcome exists. Catch cap/schema/access exceptions and emit the structured invalid receipt before exiting 1. Add a scientific-path mutant, not only an anchor mutant.

---

## MAJOR F6 — One presentation control does not test the estimator

The “two circuit presentations” are constructed to yield the identical encoding matrix, and the fixture constructor raises immediately if they differ:

- `35727744:v13/code/rq0_l0_fixtures_exact.py:301–321`.

The receipt then checks only:

```python
bundle.encoding_a == bundle.encoding_b
```

- `35727744:v13/code/rq0_l0_operational_localization.py:641–647`.

No two distinct operational datasets reach the estimator. Circuit words are not part of `OperationalDataset` at all. Therefore this is an identity of fixture constructors, not a localization-invariance test.

The encoded conjugation and gauge controls are separate and substantive; they survive. The “distinct circuit presentation” row should not be counted as an independent localization control.

---

## MINOR F7 — The non-star counts are exact, but the claim is broader than the mechanism

The estimator genuinely constructs pair and triple meets from its recovered atom lattice and checks algebra-intersection dimensions:

- `a5b71735:...estimator_exact.py:1185–1243`.

The counts \(66\) and \(134\) are correct.

But once one finest four-atom factorization is found, the estimator defines every nonempty proper atom union to be a local object. The complete proper Boolean lattice is automatically non-star. The scorer then maps these objects to hidden atom labels and constructs the reported restriction category using the truth-mapped sets:

- `35727744:...operational_localization.py:713–810`.

Thus the delivery constructs a non-star proper-join lattice; it does not independently learn a selective or irregular overlap nerve beyond that factorization.

### Replacement wording

> The recovered four-factor intervention algebra induces its complete nonempty proper-join lattice, whose meet nerve is non-star.

That statement is exact.

---

## NOTE N1 — Access-postulate scope is honestly disclosed

The access contract is extremely strong:

- 48 preparations;
- 48 probes;
- eight independently selectable Pauli-type intervention handles;
- candidate records built from hidden two-slot pairs.

The unencoded fixture constructs these from four tensor slots and then conjugates all accessible data by a global exact encoding:

- `35727744:v13/code/rq0_l0_fixtures_exact.py:184–298`;
- `:425–477`.

The resulting black-box tables contain the commutation and factor structure needed for recovery even though names and visible tensor coordinates are hidden. This is not direct label smuggling, but addressability is heavily planted in the access postulate.

The note states the correct limited claim:

> localization recovery from a sufficiently separating access contract whose intervention algebra already admits addressable factors.

Evidence:

- `35727744:v13/note-rq0-operational-localization.md:41–47`;
- `:324–339`.

That scope statement should be retained. The result is not emergence of locality from a bare quantum amplitude law.

---

## NOTE N2 — Estimator/fixture source separation passes at its claimed scope

Independent checks found:

- both commit ancestry relations hold;
- the fixture/scorer paths do not exist at the estimator-freeze commit;
- the estimator source is byte-identical at freeze and delivery;
- estimator imports are standard-library only;
- no main fixture handles, truth type, expected triple, or atom partition occur in the estimator;
- no float literals occur in any of the three substantive source files.

The delivery also correctly disclaims independent blind authorship. The main fixture is nevertheless a four-factor extension of the same Pauli tensor family used by the public two-factor calibration, so the chronology should not be advertised as broad out-of-family generalization.

---

## NOTE N3 — Phase and gauge scope are correct

The exact phase calculation survives:

- scalar ring: \(\mathbb Q(\zeta_8)\);
- gauge normalization: finite \(\mu_8\), not full \(U(1)\);
- uncompensated phase changes exactly 576 of 2304 access-table entries for the targeted intervention;
- its generated local atom algebra remains \(M_2\);
- phase is not used as a fact-identity predicate.

The full-\(U(1)\) nonclaim is accurate.

---

# Independent numbers table

The independent rebuild used only `fractions.Fraction`, a fresh implementation of \(\mathbb Q[z]/(z^4+1)\), exact matrices, Pauli commutation, set partitions, and finite-set combinatorics. It imported no delivery module.

| Quantity | Delivery | Independent result | Status |
|---|---:|---:|---|
| \(z^4=-1\) | true | true | confirmed |
| \((1/\sqrt2)^2\) | \(1/2\) | \(1/2\) | confirmed |
| Main carrier/access dimension | \(16/16\) | \(16/16\) | confirmed |
| Preparations / probes | \(48/48\) | \(48/48\) | confirmed |
| Cells per operational signature | 2304 implicit | \(48\times48=2304\) | confirmed |
| Distinct primitive signatures | 8 | 8 | confirmed |
| Bell partitions of 8 generators | 4140 | 4140 | confirmed |
| Valid nontrivial factorizations | 14 | 14 | confirmed |
| Finest factorizations | 1 | 1 | confirmed |
| Finest block count | 4 | 4 | confirmed |
| Atom-algebra dimensions | \((4,4,4,4)\) | \((4,4,4,4)\) | confirmed |
| Ambient algebra dimension | 256 | \(4^4=256\) | confirmed |
| Proper local objects | 14 | 14 | confirmed |
| Identity/restriction arrows | 50 | 50 | confirmed |
| Nonempty pair overlaps | 66 | 66 | confirmed |
| Nonempty triple overlaps | 134 | 134 | confirmed |
| Record-bearing objects | 10 | 10 | confirmed |
| Recordless counted objects | not foregrounded | 4 | **C10 violation** |
| Universal atom core of record-bearing objects | empty | empty | confirmed |
| Distinct nonempty pair meets | 10 | 10 | confirmed |
| W3 row | \(T,T,F,2,F\) | \(T,T,F,2,F\) | confirmed |
| Required triple meet | \(\{0,1\}\) | \(\{0,1\}\) | confirmed |
| Triple-meet algebra dimension | 16 | 16 | confirmed |
| Physical-phase changed cells | 576 | 576 | confirmed |
| Ambiguity maps under supplied identity/swap actions | 2 | 2 | confirmed at supplied-action scope |
| Text receipt checks | 56/56 | fresh run 56/56 | confirmed internally |
| Anchor mutant | 55/56, exit 1 | 55/56, exit 1 | confirmed |
| Fresh text receipt SHA-256 | `0297…5068` | `0297…5068` | confirmed |
| Fresh JSON receipt SHA-256 | `a073…44a5` | `a073…44a5` | confirmed |
| Fresh suite runtime | below 240 s | below 240 s | confirmed |
| \(\mathsf{Comp}_D\) supplied and checked | claimed by type prose | absent | **not confirmed** |
| Every counted object has nonempty \(\operatorname{Rec}\) | required | false, 4/14 empty | **refuted** |
| Equal-law bridge absent | claimed | typed false; no search | **not established** |
| Record descent diagrams commute | claimed | handle presence only | **not established** |

Independent scratch source:

- `/tmp/rq0_l0_independent_review.py`
- SHA-256 `d82b9b2829521e803999a6de49a1aab5d27b38ef06465ec306f58b540e6b9df8`
- 7,962 bytes.

The repository remained read-only and clean.

---

# Claims that survive

The following are solid exact results:

- exact \(\mathbb Q(\zeta_8)\) arithmetic at the tested scope;
- exact reachable-support removal of the inaccessible direct-sum completion;
- eight distinct operational signatures under the declared access contract;
- exhaustive 4,140-partition search;
- one finest four-block factorization of the generated intervention star-algebra;
- block dimensions \((4,4,4,4)\) and ambient dimension 256;
- encoded-presentation covariance under the tested exact conjugations;
- rejection of the tested irreducible \(M_4\) calibration;
- retention of identity and swap arrows from the supplied presentation-action group;
- the complete 14-object proper-subset lattice and exact 50/66/134 incidence counts;
- all six W3 write/preserve/erase/no-write rows;
- exact fair record marginals;
- exact physical-phase measurement with 576 changed cells;
- exact finite \(\mu_8\) gauge scope;
- deterministic text/JSON regeneration and successful anchor mutant;
- every causal, geometric, field, and gravity nonclaim.

These should be preserved as calibration data and lemmas.

---

# Claims to withdraw or replace

Withdraw:

- `RQ0-LOCALIZATION-GROUPOID = true`;
- `RQ0-LOCAL-ATLAS = true`;
- “independently addressable subinstruments were recovered”;
- “every mandatory control passes”;
- “equal-law fact matching is rejected by a typed bridge test”;
- “three explicit record pullback diagrams were checked”;
- “the first unresolved obstruction is influence.”

The first unresolved obstruction is still inside L0:

> supply and test the operational composite-implementation structure needed to distinguish algebraic commutation from independently executable subinstruments.

Suggested forward-correction paragraph:

> The RQ0-L0 delivery exactly recovers a four-factor decomposition of the generated intervention star-algebra and its complete proper-join lattice under a strong separating access postulate. The positive L0 rungs are withdrawn because the frozen estimator omits the pinned \(\mathsf{Comp}_D\) joint-implementation data, four of fourteen counted objects have empty derived record algebras, the equal-law no-bridge control is declarative, and the record-restriction diagrams are not typed maps. The current access schema is compatible with operational worlds that differ on joint implementability, so localization is blocked at addressability pending a new estimator freeze and unseen fixture.

---

# Required repair architecture

Because fixture truth is already open, adding \(\mathsf{Comp}_D\) changes the frozen estimator schema. The pin’s own anti-tailoring rule therefore requires a new estimator freeze and a genuinely new unseen fixture family; rescoring the current fixture is insufficient.

The repair should:

1. Add an exact typed \(\mathsf{Comp}_D\) table to the black-box dataset.
2. Require every claimed factor pair to have admitted cross-block composites with measured amplitudes and types.
3. Check faithful joint implementation and quotient compatibility, not merely matrix-product existence.
4. Add the exact \(D_+/D_-\) control: identical matrices and access statistics, differing only in admitted cross-block composition; only \(D_+\) may localize.
5. Require every object counted toward the positive atlas to have nonempty independently derived W3 records.
6. Ensure the resulting record-bearing atlas is closed under every claimed overlap, or explicitly lower the category scope.
7. Construct actual algebra restriction maps, projector pullbacks, `FactIface`, and contravariant `Rec` maps.
8. Check direct and composite pair/triple descent diagrams, not handle-string presence.
9. Replace the equal-law control with a same-carrier or otherwise bridge-compatible fixture and exhaust the declared morphism class. The no-bridge result must be computed.
10. Exercise two genuinely distinct operational presentations through the estimator; matrix equality of two circuit words is not sufficient.
11. Make `status=INVALID` imply `receipt_valid=false` and exit 1.
12. Catch cap, schema, and access-underdetermination exceptions into structured invalid receipts.
13. Add a scientific-path mutant in addition to the anchor mutant.
14. Use a genuinely new fixture family, preferably not merely a larger Pauli tensor calibration.
15. Remain halted before influence, causality, geometry, fields, or gravity.

---

# Terminal-rung recommendation

Current delivery:

\[
\boxed{\text{NONTERMINAL; NO POSITIVE RQ0-L0 RUNG}}
\]

After a forward adjudication that natively gates the exact missing-\(\mathsf{Comp}_D\) two-world countermodel:

\[
\boxed{\texttt{RQ0-L0-BLOCKED-AT-ADDRESS}}
\]

is the appropriate terminal negative at the current access-schema scope.

A future positive rung requires the new estimator-freeze/unseen-fixture cycle above. `RQ0-C1` must remain unpinned and unstarted.
