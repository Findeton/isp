# D12 hostile ontology/locality/physics review — round 2

**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION / `INCOMPLETE-INVESTIGATION` — THREE RESIDUAL BLOCKERS**

## Executive finding

Round 1 caused a real reconstruction. The replacement executable now creates
immutable quantum records, born output collars, frame-transported links,
emitted opportunities, depth-indexed cylinders, bounded construction fibers,
overlap controls, and explicit classical prefix laws. The revised paper also
separates grammar from measure support, conditions its locality claim,
distinguishes decoherent histories from process tensors, treats the Barandes
bridge as contested, withdraws the “real law” claim, and narrows its theorem.

The finite nonselection theorem is now substantially stronger and remains
accepted: the quarter- and half-iSWAP packets pass the same tested finite
architecture while disagreeing on a durable-record probability.

Three concrete ontology/type defects still prevent PASS:

1. firing accepts a collar whose screen, order unit, or frame is corrupted;
2. the claimed complete log-RN packet uses extended-real strings on a law
   with zero atoms, not a valid coefficient vector for the stated strictly
   positive reconstruction theorem; and
3. the classical “local” collar stores an ever-growing copy of the complete
   sealed prefix, violating the finite-interface rule.

These defects are localized and repairable. They do not reopen the exact
matrix probabilities, the all-level `P_r` cylinder family, or the central
underdetermination result.

## Frozen artifacts and reproduction

Authoritative round-2 artifacts:

```text
228e34053549fcfbeb9cb894004195fe1d558241b470e58b888b6873cd29afe1  code/d12_multidiamond_history_exact.py
db80a8cd1ff48d649eaf83154d7f53b2148f30dadb5ae7b2e1a4538cf934364b  relativistic-isp-v10-paper13-the-click-law-is-the-whole-history-process.md
12604d2edb5438ec35719b710cc797cf84371eb84e8a8c45994b5d10c2c38796  note-d12-round1-opening-repairs.md
61834ebdd235c1a7eadb074fc2fb9a42a987e7cbf79adedd7c51922c2af787c3  note-d12-selection-principle-audit.md
```

Normal and optimized execution are byte-identical:

```text
checks=137
stdout_sha256=ef930e21338322c76c3581cbcaab0e6f8f95c370ccc9bb2a0a22e319f5031091
semantic_receipt=b8a0dd95bf1487860d981ae4d41782d155820d9fd5c5309c3167047fea219433
```

The predecessor now honestly labels itself a one-cell metadata precursor. The
42- and 18-check supporting countermodels retain their earlier exact receipts.

## Round-1 opening adjudication

| Opening | Round-2 finding |
|---|---|
| B1 sealed-diamond runtime object | **PARTIAL / BLOCKED.** Actual packets, records, collars, links, screens, units, and opportunities exist. Screen/unit/frame eligibility and valid log-RN packet data remain defective. |
| B2 seal-and-birth hidden grammar | **MECHANICALLY CLOSED, TEXT PARTIAL.** The selected packet now really emits a record and successor collar and the verdict calls birth declared, not universal. The abstract still calls D11 an accidental ablation of V6, which overreads record persistence as carrier continuation. |
| B3 projector versus durable record | **CLOSED at declared classical-record scope.** Records are immutable typed values linked to input/output collars and persist byte-for-byte. The paper now calls the quantum calculation exact projector-history decoherence and leaves the physical record instrument primitive. |
| B4 `Ext_mu` hides grammar | **CLOSED.** The paper uses `Ext_(G,mu)` and explicitly keeps `G` and `mu` primitive. |
| B5 local versus global/non-Markov | **PROSE CLOSED; ARCHITECTURE-E BLOCKED.** The paper distinguishes absence of global order, causal locality, no-signalling, and local computability. The classical threshold implementation still copies the full past into its live collar. |
| B6 construction-order gauge | **CLOSED only at bounded outcome-law scope.** `AB/BA` instruments and outcome weights push to one canonical labeled fiber with no double counting, and overlap changes a probability. Full marked record/collar graph canonicalization is not executed. |
| B7 integrated frame claim | **CLOSED at stated unitary scope.** Five independently assigned unitary vertex frames transport states, screens, effects, and links through depth four. Full nonunitary Lorentz integration remains explicitly open. |
| B8 projective/profinite claim | **CLOSED at stated hypotheses.** The arbitrary-depth independent-block formula supplies finite cylinder levels and bonding maps; the paper now conditions the word profinite on finite inverse-limit hypotheses. |
| B9 decoherence/process-tensor conflation | **CLOSED.** The representations and translation assumptions are separated; D12 claims only exact projector histories. |
| B10 Egri/Barandes literature boundary | **SUBSTANTIALLY CLOSED.** Paper 13 and the audit cite Egri et al., distinguish path measures from instantaneous probability dynamics, and treat the correspondence as contested. One selector-table cell remains too affirmative. |
| B11 real-law language | **CLOSED.** The final answer says D12 has not found the real law of nature and reserves universe-specific claims for selection. |
| B12 theorem scope | **NARROWED CORRECTLY, BUT DEPENDS ON B1.** `A_D12` now names only the executed finite/unitary packet principles. Its log-RN and screen-eligibility clauses still need repair before the complete-packet premise is literally satisfied. |

## Residual blockers

### R1 — Screens, order units, and frames are stored but not eligibility data

**Severity:** major

`Collar` now contains a frame, order unit, and lower screen. However,
`eligible()` checks only:

```text
not consumed;
eventless flag;
input types;
owner names;
the INTERACT opportunity;
state normalization.
```

It never checks that:

- the frame basis is unitary;
- the order unit is the packet's order unit in that frame;
- the stored lower screen equals the transported packet screen; or
- the lower screen actually matches the incoming diamond boundary.

`fire()` then ignores `collar.lower_screen` and `collar.order_unit` and derives
its pointer/link from the supplied frame and packet. Direct hostile probes on
the frozen artifact return:

```text
bad_screen_eligible True
bad_unit_eligible   True
bad_frame_eligible  True
```

Thus screens and units are still partly decorative metadata. The positive
generated path happens to carry correct values, but U1/U6 require malformed
boundary data to be rejected before firing. The receipt
`local_type_owner_opportunity_stale_eligibility=PASS` is narrower than its
paper interpretation, and `screen gates=PASS` checks only generated screen
length and `I4`, not boundary matching.

**Required repair:** define exact incoming-boundary compatibility and include
it in `eligible()`. Check frame unitarity, transported order-unit equality,
and exact screen equality. Add hostile controls for a wrong screen of the
right length, wrong order unit, nonunitary frame, and mismatched frame/screen
pair. The transition should either consume the validated stored screen or
make explicit why it is only a redundant receipt field.

### R2 — The “complete log-RN coefficients” are neither coefficients nor in the positive theorem's domain

**Severity:** major

The protocol's restored packet includes a whole-history law and `h_D`, and
Paper 13 states the reconstruction theorem for a **strictly positive** law
relative to a positive reference. The frozen quantum packets instead use:

```text
reference = (1/4, 1/4, 1/4, 1/4)
P_Q       = (0, 1/2, 1/2, 0)
P_H       = (0, 0,   1,   0)
```

Their new field is:

```text
P_Q.log_rn_history_coefficients =
  ("-infinity", "ln(2)", "ln(2)", "-infinity")
```

These are four atomwise extended log densities represented as strings. They
are not the three mode coefficients of `CONTRAST_LEDGER`, are not exact
runtime numbers, and cannot satisfy the finite strictly positive
exponential-family theorem. The half-iSWAP packet has a different
positive-mass support from the quarter-iSWAP packet even though check 2 says
the packets share “support”; what they share is the grammar's nominal atom
set and positive reference, not `Ext_(G,mu)`.

This does not invalidate the interaction counterexample. It invalidates
`minimum_diamond_packet_fields=PASS` and the claim that both executable
packets instantiate the complete positive log-RN/holonomy premise as stated.

**Required repair:** choose one honest route:

1. restrict each measure to its positive support, compute the appropriate
   finite ledger coordinates there, and explicitly allow the induced supports
   to differ;
2. choose a generic exact input/instrument for which every shared atom has
   positive mass in both models, then compute and verify the actual ledger
   coordinates and reconstruction; or
3. state and prove a nonnegative/support-stratified extension using
   extended-real densities, without calling the strings finite coefficient
   vectors or invoking the strictly positive theorem.

Add an exact reconstruction gate from the stored `h_D`, ledger, and reference
to the stored law.

### R3 — The local-threshold collar carries an unbounded copy of history

**Severity:** major

The frozen protocol explicitly forbids a live interface from carrying an
unbounded copy of the past. `ClassicalCollar` contains:

```text
sealed_prefix: tuple
```

and every classical birth copies the complete enlarged prefix into the next
collar. The displayed tower stops at three records, but the architecture-E
claim is all-level. At arbitrary depth this is exactly the growing ancestry
payload D12 promised to distribute over immutable records.

The exponential-race identity is mathematically correct: choosing rates equal
to supplied conditional masses reproduces those conditionals. It is not yet a
finite local-threshold realization. The rate function is called with the full
prefix; for a general whole-history measure that may be a global oracle. Paper
13 correctly admits this in its final paragraph, but the architecture table
and receipt still call E a local exponential-threshold representation.

For the independent `P_r` block family the repair is easy because the next law
needs only bounded state: block phase plus the previous zero, one, or two
values. Store that bounded sufficient statistic in the live collar, keep the
complete prefix only in immutable history records, and compute the clocks
from the bounded collar. For a genuinely full-history law without such a
sufficient statistic, drop `local` and call the race a conditional sampling
representation rather than a decentralized implementation.

## Nonblocking residual openings

### N1 — D11 is still described as an accidental ontology replacement

The revised verdict correctly says the continuing packet is declared rather
than universally derived. The abstract and Section 2 nevertheless call D11
an accidental replacement/ablation and say its physical interpretation was
wrong. D11's repaired terminal packet retains a durable record while ending
its live carrier. Record persistence does not force successor birth.

Replace that narrative with: D11 intentionally tests terminal architecture A
and cannot adjudicate declared continuing architectures. This synchronizes
Paper 13 with its own final verdict.

### N2 — Construction fibers canonicalize outcomes, not full typed histories

The new `AB/BA` calculation genuinely includes both interactions and pointer
outcomes and correctly avoids double counting. Its canonical key contains
only labeled outcomes `(A,a),(B,b)`, while the separate typed history engine
is not used to compare record IDs, collars, screens, links, opportunities, or
provenance across schedules.

This is sufficient for the stated bounded probability-law gauge, but not yet
a full marked-history construction quotient. Keep that scope explicit or
integrate the typed objects into both schedules and canonicalize the complete
partial history.

### N3 — One selector-table cell still treats the Barandes bridge as established

The literature paragraphs are now appropriately cautious. The selector table
still says Barandes “permits a primitive non-Markov stochastic law and its
Hilbert dilation” without marking the bridge proposed/contested. Synchronize
that cell with the Egri paragraph. This is a wording repair; D12's
disintegration theorem no longer depends on the correspondence.

### N4 — “Repeat-read” means stored-value persistence

The executable proves byte-for-byte record persistence and that each stored
`value` equals the history label. That is enough for its immutable classical
record type. It does not execute a second physical measurement of an
inscription. Rename the receipt to `record_value_persistence`, or add a typed
read operation and a nondemolition/repeatability gate if physical repeat-read
is intended.

## Results that remain accepted

The following round-2 results are not reopened by the residual defects:

- exact quarter-/half-iSWAP unitarity, common symmetries, and different
  durable-outcome probabilities;
- explicit record and successor-collar generation through depth four;
- immutable quantum record persistence along generated branches;
- exact prefix normalization, bonding, and nontrivial disintegration for the
  executed quantum towers;
- the arbitrary-depth independent-`P_r` block cylinder formula and its
  projectivity;
- independent unitary vertex-frame covariance through the tested tower;
- bounded `AB/BA` outcome-law construction gauge and overlapping-order
  sensitivity;
- exact conditional sampling by exponential races once the rates are
  supplied;
- separation of `Ext_G` from positive measure support;
- separation of decoherent histories from process tensors/combs;
- the repaired Egri/Barandes literature boundary, subject to N3;
- withdrawal of universe-specific real-law claims; and
- refusal to use geometry to select the process after the fact.

The exact scientific core remains:

```text
THE TESTED RECORD/TYPE/SYMMETRY PRINCIPLES DO NOT SELECT THE INTERACTION
A SUPPLIED PROJECTIVE HISTORY MEASURE DETERMINES ITS CYLINDER CONDITIONALS
THE GRAMMAR, MEASURE, COUPLINGS, AND UNIVERSE-SPECIFIC PROCESS REMAIN PRIMITIVE
```

## Verdict

**MAJOR REVISION / `INCOMPLETE-INVESTIGATION` — THREE RESIDUAL BLOCKERS.**
Round 2 closes most of the original review and upgrades D12 from a schematic
one-cell model to a genuine bounded multi-commit countermodel. It does not yet
close the exact finite typed packet it claims: malformed relational boundary
data can fire, the positive log-RN field is not a valid ledger coefficient
object, and the claimed local classical collar copies the whole past.

Repair those three items and synchronize the four nonblocking labels. The
finite/unitary underdetermination theorem should then be eligible for PASS at
the explicitly narrowed `UNIVERSAL-FORM/PRIMITIVE-PROCESS-REMAINS` scope.
