# D20 full-objective independent manifest audit

**Date:** 2026-07-12  
**Referee stream:** independent provenance, scope and holdout audit  
**Candidate:** `v10/note-d20-full-objective-closure-audit.md`  
**Verdict:** **PASS WITH REQUIRED SCOPE REPAIRS; `NOT ACHIEVED` IS STABLE**

## Decision

D20 reaches the correct full-objective verdict.  The D14--D19 exact chain does
not derive or empirically select one complete interacting covariant universe
law, and it does not license a new geometry comparison.  Every exact D14--D19
source, packet and final-review hash cited by the final receipts still matches.
Fresh normal and optimized executions of all seven exact executables pass:

```text
D14                    42/42  FINITE-REGIONAL-AMPLITUDE-TO-RECORDED-HISTORY-CORE-PASSED
D15                    28/28  REGULATED-ACTION-DICTIONARY-WITNESS-PASSED
D16                    26/26  INTERVAL-ACTION-FAMILY-NONSELECTING
D17 first              26/26  CAUSAL-ACTION-TO-MEASURE-NONSELECTION
D17 integrated         40/40  INTEGRATED-CAUSAL-HISTORY-KERNEL-NONSELECTION
D18                    30/30  FINITE-DECOHERENCE-FUNCTIONAL-SUFFICIENCY
D19                    20/20  FINITE-HISTORY-LAW-EMPIRICAL-NONIDENTIFIABILITY
```

The manifest nevertheless needs repairs before it can be called final.  It
currently blends exact results, corpus syntheses and external-literature
assessments without marking the evidence class.  One sentence says the
Einstein--Hilbert plus Standard Model packet is the "best empirically selected
effective generator packet"; that exceeds D19's explicit hostile-reviewed
ceiling.  The status line is stale.  The phrase "untouched V9 holdout" is also
internally inconsistent with D20's later acknowledgement that the V9 data were
already used in program development.

## Audit method

I used three evidence grades:

```text
E  exact executable result with a final receipt and hostile closure
S  sound corpus-level synthesis of several bounded exact results
L  literature/evidence-ledger assessment, not a theorem of a D14--D19 receipt
```

For D14--D19 I independently recomputed SHA-256 for every final-receipt source,
JSON packet and cited closing review.  All matched.  Normal and `-O` executions
also exited zero with the receipt-carried source and semantic hashes.  For V9
I checked the reviewed correction in `v9/LOG.md`, the paper-8 status language,
the D12 geometry gate, D13--D19 receipts, and the V10 plan.  This audit did not
run a V9 geometry executable or inspect a new geometry result.

## Clause-by-clause provenance

| D20 objective clause | Terminating evidence | Grade | Audit result |
|---|---|---:|---|
| local generally covariant action | `data/d16-final-receipt.md`; `code/d16_covariant_causal_action_exact.py`; `reviews/d16-round2-{order-action,ontology-covariance,independent-rebuild}-review.md` | E | Exact only for finite poset-relabel covariance, intrinsic interval counts and typed quotient sewing.  D16 explicitly denies continuum diffeomorphism covariance, factorized action sewing and a selected coefficient packet. |
| general-boundary amplitude architecture | `note-d18-literature-and-architecture-audit.md`; `note-d13-literature-audit-action-selection.md` | L | Supported as the closest established regional-sewing architecture, not as a proved uniquely "strongest" architecture.  D20 must mark this as an assessed architectural fit. |
| Standard Model plus Einstein--Hilbert low-energy baseline | `note-d19-empirical-identifiability-theorem.md`; `reviews/d19-round2-physics-identifiability-review.md`; `note-d15-maximal-low-energy-action.md`; `note-d15-eft-action-parameter-ledger.md` | L | Supported only as the leading extensively tested low-energy baseline, conditional on observed fields and Lorentzian geometry, with higher operators/extensions allowed.  It is not a selected complete generator. |
| no global clock | `data/d17-final-receipt.md`; integrated D17 source/packet; the three `reviews/d17-round5-integrated-*-review.md`; `data/d16-final-receipt.md` | E/S | D17 exactly quotients compatible element relabelings on one supplied filtration and constructs projective whole-history conditionals.  Alternate filtrations, a joint construction-filtration quotient and continuum refoliation equivalence are explicitly open. |
| complete non-Markov law | `data/d17-final-receipt.md`; `data/d18-final-receipt.md`; `reviews/d18-round2-*.md`; `reviews/d18-round3-final-*-delta-review.md` | E | Exact at finite typed/cylinder scope only.  A supplied classical projective law gives its conditionals; supplied finite `(E,D)` gives positive-cylinder quantum conditionals.  Full sigma extension and physical selection of `D` remain open.  D20 should add "finite/cylinder" wherever it says "complete" here. |
| durable records | `data/d14-final-receipt.md`; D14 exact source/packet; `reviews/d14-round3-mathematics-focused-review.md`; `reviews/d14-round4-ontology-final-delta-review.md`; `reviews/d14-round2-independent-rebuild-hostile-review.md`; integrated D17 receipt/reviews | E | Exact owner-local protected commits, live collars, sequential records, memory and reset are present.  Their opportunity grammar, initial instrument and universal emergence are supplied, not derived. |
| quantum correlations | `data/d13-final-receipt.md`; `data/d14-final-receipt.md`; `data/d15-regulated-dictionary-final-receipt.md`; `data/d18-final-receipt.md` and their closing reviews | E | Finite interference, Bell-state/no-signalling compatibility, decoherence and one-time Born/disintegration witnesses are exact.  "Bell" must be read as finite packet compatibility, not a derivation of nature's Bell experiment or quantum-gravity functional. |
| relativistic causal structure | `data/d10-final-receipt.md`; D10 round-3 hostile reviews; `data/d11-final-receipt.md`; `data/d16-final-receipt.md`; D19 evidence ledger | E/L | The exact Bloch/`CP^1=S^2` and `Herm_2(C)_+` Lorentz-cone bridge is D10 and is explicitly `KINEMATICS-ONLY`.  D11 is an `INCOMPLETE-PACKET`, not a second derivation of that bridge.  D16 supplies finite order covariance.  EFT4 assumes observed Lorentzian `3+1`; none derives its emergence. |
| couplings and scales | `note-d15-eft-action-parameter-ledger.md`; `note-d15-maximal-low-energy-action.md`; `note-d16-bdg-provenance-and-scale-ledger.md`; `data/d18-final-receipt.md` | L/E | The coefficient and unit dictionaries are sound ledgers.  D18 exactly verifies that dimensionless odds do not fix `G` without a physical scale dictionary.  The claim that measured `G`, together with `c` and `hbar`, calibrates Planck units is standard input accounting, not a D15 finite-theorem output. |
| new cone/dimension/gravity predictions | `v9/LOG.md` round-48 review; `v9/relativistic-isp-v9-paper8-shape-dimension-frontier.md`; `note-d12-geometry-consequence-gate.md`; `data/d19-final-receipt.md` | measured V9 / E ceiling | The reviewed V9 result is `PARKED-AT-PROTOCOL`, not round-and-4D closure: anisotropy fell about 45%; the robust diffusion witness is `F=1.197`, approximately `z=-3.8`; the `g=0.18` dominant leg is uncorrected-only, the `m4` leg survives correction, and `d=4.4+/-0.2` is instrument-suspect.  D19 supplies no physical generator pair or untouched prediction and keeps geometry closed. |

## Audit of the seven "genuinely closed" statements

1. **Construction order is not automatically physical time -- pass as a
   synthesis.**  D16 presentation independence and D17's one-filtration label
   quotient block identification of raw labels with observables.  Neither
   proves the missing joint filtration/refoliation gauge.  D20 states that
   limitation.

2. **Sealed principles do not create support -- pass as a synthesis.**  D14
   maps admitted alternatives through exact typed instruments; D16 and D17
   respectively supply the finite order family and extension grammar.  Their
   claim ceilings explicitly leave opportunity/support, joins and the physical
   generator open.  No single receipt has this sentence as a named theorem,
   so it should be labelled a cross-receipt consequence.

3. **An action is not the complete rulebook -- exact pass.**  The integrated
   D17 witness holds the finite action and typed grammar fixed while changing a
   positive kernel, producing distinct projective recorded laws.  It does not
   prove this for every continuum action, but one countermodel suffices to
   refute logical sufficiency of the listed principles.

4. **The operational next click is a conditional -- exact finite-scope pass.**
   D17 gives classical disintegration; D18 gives positive-cylinder
   conditionals in decoherent supplied sectors.  Positivity and nonzero
   conditioning mass remain necessary.  This is not an autonomous birth law.

5. **Primitive `D` does not derive itself -- exact pass.**  D18 proves finite
   sufficiency and explicitly retains action, state, measure, instruments and
   record semantics as physical inputs.

6. **Finite local shadows need not identify the law -- exact pass.**  D19's
   rank-seven map on eight histories has the `xyz/8` null direction and two
   strictly positive survivors.  The displayed cubic discriminator is
   designed from that null direction, not untouched evidence, and D20 does not
   get a physical-generator nonselection theorem from it.

7. **Metres, seconds and `G` do not round a dimensionless cone -- pass with
   split authority.**  D18 exactly separates dimensionless probabilities from
   the unit dictionary.  D15's scale ledger explains the standard Planck-unit
   calibration.  The cone statement is a dimensionless-invariance argument;
   it is not a new numerical D15 receipt.

## Rulebook audit

The finite operational display

```text
typed E + normalized strongly-positive D
-> decoherent record probabilities -> positive next-record conditionals
```

is supported by D18 if all of the following qualifiers remain attached:
finite typed event algebra, supplied `D`, supplied projective cylinder family,
declared decoherent/positive sector, and separately supplied record semantics.
It is sufficient at that scope, not uniquely minimal and not a local physical
generator.

The low-energy display is reasonable as an evidence-ledger decomposition, but
its final arrow is not supportable as written:

```text
-> the best empirically selected effective generator packet.
```

D19's final receipt says explicitly that the qualitative Standard Model plus
Einstein--Hilbert ledger does **not** replace a generator dataset, likelihood,
candidate image or real holdout.  Its focused physical review permits only
"the leading extensively tested low-energy baseline" with higher operators
and extensions allowed.  Required replacement:

```text
-> the leading extensively tested low-energy baseline packet,
   conditional on observed fields and Lorentzian geometry;
   not a uniquely selected complete generator.
```

This is the only D20 sentence that directly contradicts a final hostile-review
ceiling.

## V9 holdout refusal audit

The refusal is substantively correct but needs terminological repair.

Evidence that the gate remained closed after D12:

- `note-d12-geometry-consequence-gate.md` requires a complete selected process,
  an inequivalent rival, frozen cross-candidate predictions and an untouched
  geometry test before a new evaluation.
- `data/d13-final-receipt.md` says no V9 action holdout is licensed.
- D14--D18 final receipts each deny a V9 entitlement at their claim ceiling.
- `data/d19-final-receipt.md` and
  `reviews/d19-round2-physics-identifiability-review.md` explicitly say V9
  remains closed because no physical generator pair fixes a cross-candidate
  value independently of nuisance fitting.
- `PLAN.md` records the geometry holdout as withheld through D19.
- There is no D20 geometry executable, output packet or result receipt.  D20 is
  a documentary audit only.

No auditable D13--D20 artifact reopens or reruns the geometry evaluation.
However, this is a **protocol refusal**, not a machine-enforced access control;
the old V9 files remain readable/executable.  The corpus can establish that no
licensed new result was produced, not prove that no process ever read a V9
file.

More importantly, the existing V9 dataset is not "untouched" now.  V9 used it
to develop and review the diffusion/churn program, and D20 itself says the data
were already used.  Therefore these two phrases must be separated:

```text
existing V9 geometry evidence = closed to renewed candidate ranking/tuning
new untouched geometry holdout = required, but not yet designated or opened
```

Calling the present V9 corpus an "untouched holdout" is false.  Calling it a
closed historical/frozen geometry dataset is accurate.

The candidate-family refusal is otherwise faithful to
`note-d15-uv-survivor-audit.md`: `EFT4` assumes `3+1`; `BDQ`, `ASQ` and `SFQ`
all lack at least one selected measure/state/record/scale or continuum field.
That file is a literature survivor ledger, not an executable census of all
possible fundamental theories, and D20 should say so.

## Required repairs

1. Change the status from "draft pending D19 focused closure" to a post-D19
   audit status.  D19 closed at its finite theorem scope on 2026-07-12, while
   the broader physical investigation remains incomplete.
2. Mark each D20 clause as exact result, cross-receipt synthesis, or
   literature/evidence-ledger assessment.
3. Replace "general-boundary amplitudes are the strongest architecture" with
   "the closest established regional-sewing architecture in the D18 audit."
4. Add "finite/cylinder" to the complete-law claim and retain the sigma-
   extension ceiling.
5. Attribute the exact Bloch/celestial bridge to D10; describe D11 as the
   incomplete attempted integrated packet.
6. Qualify the Bell language as finite packet compatibility/witnesses.
7. Replace "best empirically selected effective generator packet" with the
   narrowed low-energy-baseline wording above.
8. Expand "protocol-level cone result" to the reviewed
   `PARKED-AT-PROTOCOL` grade and its instrument/multiplicity limitations.
9. Replace "untouched V9 holdout" with the two-line distinction between the
   already-used frozen V9 evidence and a future genuinely untouched dataset.
10. State that holdout closure is protocol-enforced and receipt-auditable, not
    technically access-controlled.

## Final referee verdict

```text
D20 full-objective verdict                       NOT ACHIEVED -- CONFIRMED
D14--D19 executable and receipt provenance       PASS
D14--D19 final hostile-review hash manifest       PASS
finite operational rulebook summary              PASS WITH SCOPE QUALIFIERS
low-energy generator-selection wording            OVERCLAIM -- REPAIR REQUIRED
V9 no-new-result protocol                         PASS
"untouched V9" terminology                        INCORRECT -- REPAIR REQUIRED
D20 document status                               STALE -- REPAIR REQUIRED
```

After those repairs, D20 can close as a rigorous negative full-objective
audit.  Nothing in this review licenses a fundamental-law claim, a new V9 run,
or a round-and-four-dimensional headline.
