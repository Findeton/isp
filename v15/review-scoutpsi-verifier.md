# SCOUT-PSI — SINGLE HOSTILE VERIFIER SEAT (operator + effectus + instrument)

**Seat:** the one verifier seat the pin promises (scout scale), launched at
ledger #71.  Adversarial charge: break SCOUTPSI-DECOMPOSITION-SENSITIVE-AT-2.
**Object, hash-verified at open and at close:**

| file | sha256-12 (open) | sha256-12 (close) |
|---|---|---|
| `v15/note-scoutpsi.md` | `7c3655632bc4` | `7c3655632bc4` |
| `v15/code/scoutpsi_exact.py` | `a5c4f323e741` | `a5c4f323e741` |
| `v15/code/scoutpsi_output.txt` | `55390f282cff` | `55390f282cff` |
| `v15/code/scoutpsi_receipt.json` | `d61a7f6e5ac0` | `d61a7f6e5ac0` |
| `v15/note-scoutpsi-pin.md` | `8e9fe2448b00` | `8e9fe2448b00` |
| `v15/note-scoutpsi-pin-addendum.md` | `e717d3bbc1df` | `e717d3bbc1df` |

Sources verified: `v14/paper-20-coupling.md` `4824d190af73` (both quoted
delivered-rule sentences present verbatim at the :633 region); the committed
scout S4 apparatus at commit `b9514b6` (`v15/note-scout-bridge.md`
`34f10a6fd494` / `v15/code/scout_receipt.json` `12bdb7a58909`, s4_linearity
witness {branch_cell 0, entry (4,4), 1/36, 0} read from those bytes); the
repaired successors live at `57177f5bb9b9` / `9fd9029516f2` (= commit
`e8cb399`), s4_linearity rows value-identical.  The unit's hard-coded
`S4_COMMITTED` block matches the committed bytes field by field.

**Method.**  Operator: full rebuild in a scratch tree sharing no code and no
intermediate with `scoutpsi_exact.py` — my own Z[ω] arithmetic (identities
self-checked), my own arena/coin/shift from the committed S4 formalization,
my own tree walker (history-tracking, not count-only), my own density
matrices and mixture Born functional.  Effectus: the #68 addendum held
against the note line by line; numeral occurrences counted; the wall scanned
with 15 fresh paraphrases.  Instrument: a git-less rsync mirror under the
scratchpad (`scoutpsi_verify/mirror`), 14 live injections + 3 registry
mutants + 7 hostile argv + selftest + regeneration probes.  Repo access
read-only; this file is the sole write.

---

## VERDICT: ACCEPT-WITH-MAJOR-REPAIRS

The measured physics is fully reproduced — every published number is exact
on my independent rebuild (~120 recomputations, zero mismatches), the
window-1 linearity mechanism and the null's channel-linearity verify from
first principles, both controls fire, and the headline survives even the
legs the unit failed to run (I ran them).  But the unit is NOT compliant
with the #68 addendum it was built under: the frozen SECONDARY preparation
was never run, three of the four frozen comparison rows were silently
dropped, the required operational-qualification wall sentences are absent
from the note, the per-occurrence numeral totality was not implemented, and
the addendum itself is neither cited nor digest-gated by the unit.  LOG #70's
sentence "the pre-registered preparations run exactly as frozen" is false as
written.  Under the addendum's own standard ("nothing selected after
behavior is visible"; "no row is silently dropped") these are majors even
though — by my measurement — none of them would have moved the verdict word.

---

## 1. RECOMPUTATION LEDGER (operator)

All from scratch; "=" means exact equality over Q(ω)/Q.

| # | recomputation | result |
|---|---|---|
| R1 | arena: 27 cells / 9 sites / shift a permutation / Grover Gram = 9I | = |
| R2 | ρ-equality: D1A=D1B=D1C mixture and D2A=D2B mixture, entry by entry over Q(ω); every declared scale2 = exact squared norm (12 members) | = (pin gate honest) |
| R3 | pairwise ensemble distinctness (4 pairs) + all six RHO1 member rays pairwise distinct | = |
| R4 | frozen-secondary ρ-equality: computational-uniform = F3-character-uniform = I/27 (my run; the unit never built these) | = |
| R5 | delivered rule windows 1–3, all five ensembles; total mass exactly 1 at every window (15 checks); every branch denominator = 9·scale2 (unitarity enforced per branch) | = |
| R6 | window 1 BLIND at all 4 pairs, record by record | confirmed |
| R7 | mechanism: window-1 ensemble marginal = Born functional of the mixture density matrix, computed directly from ρ (all 5 ensembles); one-step weights are quadratic-form ratios with the unitarity-fixed denominator 9·scale2 | confirmed |
| R8 | first divergence at window 2 for all 4 pairs; lexicographically least diverging window-2 record = {2:1,14:1} | = |
| R9 | witness masses 16/729 (D1A) vs 32/729 (D1B), difference −16/729; ALL 27 window-2 records diverge (27 of 27 in the union support) | = |
| R10 | full window-1 + window-2 D1A/D1B distributions vs receipt `witness_distributions` (record-by-record equality) + 8 spot records printed (e.g. {2:1,13:1} 64/729 vs 128/729; {2:1,11:1} 40/729 vs 8/729; {2:1,9:1} 10/729 vs 2/729) | = |
| R11 | window-3 divergence at every pair; all five `window3_digests` recomputed under the unit's own serialization: digests and record counts match | = |
| R12 | null instrument: Kraus form K_c = (1/3)\|e_{SH[c]}⟩⟨row c of C(n)\|, Σ K†K = I verified at two records; one-step output ensemble computed from the mixture MATRIX identical for D1A vs D1B (channel linearity); record distributions BLIND at windows 1|2|3 on all five ensembles, mass 1 everywhere | confirmed |
| R13 | positive control: squared-Born weights; SENSITIVE at window 1; first diverging record {2:1}, masses 16/33 vs 64/129 | = |
| R14 | S4 weld: closed form −(1/4)(w_c(ρ0)−w_c(ρ1))(P0−P1) verified entry by entry on my own machinery; witness = branch cell 0, entry (4,4), value 1/36 + 0ω; equals committed bytes AND repaired-successor rows | = |
| R15 | receipt `delivered_summary`, witness row, positive row, null rows, `numeral_bindings` (9, all resolving) | = |
| R16 | THE UN-RUN FROZEN SECONDARY (my run): ρ** = I/27, computational vs F3-character uniform, delivered rule — window 1 BLIND (0 diffs), window 2 SENSITIVE (378 diverging records; first diverging record {26:2}, masses 0 vs 1/729) | new measurement |
| R17 | THE MISSING ROWS (my run), witness pair: ordered-history raw diverges 27 classes at w2, 486 at w3 (count-raw: 27 / 477); translation-group relabelling quotient (Z3×Z3 site translations): BLIND w1, SENSITIVE w2 (27 classes, first class {23:1,26:1} 40/729 vs 8/729), w3 240 classes; COARSEST quotient (cell identity fully forgotten): BLIND at w1 AND w2 (both preparations put mass 1 on the class "two distinct cells once each"), first divergence at WINDOW 3 (2 classes) | new measurement |

Scripts: `scratchpad/verifier_rebuild.py` (108 gated checks, 0 mismatches),
`scratchpad/quotient_probe.py` (12 row comparisons).  Independent
recomputations total ≈ 120; **no published number moved**.

## 2. FINDINGS (effectus), with severity and evidence

**F1 — MAJOR — the frozen SECONDARY preparation was never run.**  Addendum
item 1 freezes SECONDARY ρ** = the maximally mixed state on the S4 carrier,
D1 = computational basis uniform, D2 = F3-character basis uniform.  The unit
instead measured RHO2 = the equal mixture of cells 0 and 5 (nowhere frozen)
plus an unfrozen third primary ensemble D1C.  Neither substitution is
disclosed; the note's deviations section is silent; LOG #70 states "the
pre-registered preparations run exactly as frozen", which is false for the
secondary.  Only the PRIMARY pair (D1A/D1B) is on frozen ground — and the
headline witness does live there.  Mitigation, measured at this seat (R16):
the frozen secondary yields the same row verdict (blind at 1, sensitive at 2),
so the breach did not manufacture the headline — but that is this review's
measurement, not the unit's.

**F2 — MAJOR — three of the four frozen comparison rows silently dropped.**
Addendum item 2: {complete ordered CELL-HIT emission histories, final count
field} × {raw, relabelling-quotiented}, each with its own verdict word, "no
row is silently dropped."  The unit measured and published exactly one row
(final count field, raw).  No ordered-history distribution, no quotient row,
no per-row verdicts, no acknowledgment.  The rows are NOT redundant (R17):
under the coarsest relabelling quotient the witness pair is BLIND at window 2
and first diverges at window 3 — the "AT-2" index is grain-relative exactly
as the addendum anticipated.  Under the arena's translation relabelling group
the row stays SENSITIVE-AT-2, and the ordered-history rows diverge wherever
the count rows do, so the qualitative verdict word survives every row I
built; the window index survives all but the coarsest reading.  (Residual
freeze defect, charged to the addendum itself: "relabelling-quotiented" never
names its group.)

**F3 — MAJOR — the operational-qualification wall sentences are absent.**
Addendum item 4 requires gated sentences in the note: sensitivity proves ρ
insufficient FOR THE DELIVERED CELL-HIT RULE on pure-state ensembles;
preparation/intervention protocols are UNBUILT, so no experimental
distinction is claimed; a future triple-event law may remove or change the
sensitivity.  None of the three appears anywhere in the note (grep:
"sufficient", "protocol", "unbuilt", "triple" — zero hits).  A version of
the first lives only in LOG #70; the object under test carries none.

**F4 — MAJOR — the #68 addendum is neither cited nor gated by the unit, and
the required already-inspected disclosure is missing.**  The note's
Authority block names only the pin; the instrument's `PINNED` table pins
only the pin note and paper-20 — `e717d3bbc1df` appears nowhere in note,
code, output, or receipt.  #68 routed both addenda "with a REQUIRED
DISCLOSURE: each worker must state which computations it had already
inspected before receipt … disclosing the order of events."  No such
disclosure exists in the unit.  (F1–F3 are the downstream consequences.)

**F5 — MODERATE — numeral totality not implemented (addendum item 5).**
Required from birth: EVERY numeral occurrence classified BOUND (specific
receipt field) or NON-CLAIM (reason class), gated and total.  Delivered:
9 explicit bindings (verified, all resolve) plus a blanket
`LAYOUT_NUMERALS` whitelist (all integers 0–59 wholesale plus a hand list)
plus receipt-inventory membership.  Measured: 233 numeral occurrences in the
note; no per-occurrence classification exists in note or receipt (zero
fields of that shape); bare 16 and 32 — the witness masses' numerators —
would pass the integer gate via the 0–59 whitelist even if unbound (the
slash-rational forms are separately inventoried and kit-gated, which is
where the real teeth are).  This is exactly the "local fix" #68 engraved
against.

**F6 — MODERATE — the ontology wall's machine enforcement is a 7-pattern
blacklist; fresh paraphrases pass (injections I5/I6).**  Planted sentences
"the wavefunction is physically real and the ensemble is the true state of
affairs" and "the density matrix is therefore an incomplete-description of
the actual state, settling the fork" both pass FULL DELIVERY (rc 0, artifacts
rewritten around them).  The delivered note itself is clean under my
15-paraphrase scan, and the pin's candidate-reading discipline plus this seat
are the actual enforcement — but LOG #70's "the ontology wall
MACHINE-ENFORCED (no sentence decides the fork)" overstates the surface.

**F7 — MODERATE — a false mathematical sentence in Deviations item 4.**
"Unequal-weight decompositions would need amplitudes outside Q(w) at this
rho family" is wrong in both directions: (i) two-member unequal-weight pure
decompositions of these rank-2 equal-eigenvalue rhos do not exist over ANY
field (Bloch balance forces 1/2–1/2: p·n̂_u = −(1−p)·n̂_v with unit vectors
forces p = 1/2); (ii) larger unequal-weight decompositions exist ENTIRELY
inside Z[ω]: {1/3 e0; 1/3 e1; 1/6 (e0+e1); 1/6 (e0−e1)} mixes exactly to
RHO1 (verified).  The disclosed scope (equal-weight two-member only) is
accurate; the reason given for it is false, and LOG #70 repeats it.  No
measured number is affected.

**F8 — MINOR — the primary-support anchor could not be executed as frozen
and the impossibility went undisclosed.**  Addendum item 1: |a⟩,|b⟩ "read
from the committed scout receipt by the deterministic rule (anchor the
field)".  The committed receipt's s4_linearity row carries no support field
to anchor; the unit hard-codes cells 0/1.  The choice is correct (the
committed `scout_exact.py` s4_map uses basis 0 and basis 1), but the
deterministic-rule-with-anchored-field was silently replaced by an embedded
constant.

**F9 — MINOR — `pairwise_distinct_as_ensembles: True` is a literal constant
in the receipt row** (`scoutpsi_exact.py:431`), not the computed value; the
real measurement feeds only the G-DISTINCT gate.  Mitigated (under
MUT-DISTINCT the gate kills the run before the receipt is written), but a
receipt field shaped like a measurement should be wired to one.

Wall verdict on the delivered prose itself: CLEAN — no sentence decides the
fork; the fork paragraph correctly routes the decision to the program; E-34
respected (no CELL-HIT called a division event); sample-space tags present
on every probability sentence.

## 3. INSTRUMENT — injection and mutant tables

Mirror: git-less rsync copy under
`scratchpad/scoutpsi_verify/mirror/` (unit + pin + addendum + paper-20 +
scout_receipt.json + LOG).  Baseline first: artifacts DELETED, regenerated at
PYTHONHASHSEED 0/1/424242 from alien CWDs (`/`, `/private`) —
output and receipt byte-identical to committed all three times; receipt
byte-stable under two live LOG.md appends (the #66 G-ENV probe).  Mirror
restored byte-perfect after every injection (close hashes above).

| inj | what was forged | expected | observed | tree |
|---|---|---|---|---|
| I1 | note prose: witness masses 16/729 → 17/729 | die at note gate | rc 3, G-NOTE-KIT: kit sentence missing + "slash rational not in receipt inventory: 17/729" | intact |
| I2 | verdict word SENSITIVE → BLIND in the note | die | rc 3, G-NOTE-KIT: verdict word missing | intact |
| I3 | null/positive labels swapped (null "SENSITIVE", positive "BLIND") | die | rc 3, G-NOTE-KIT: both kit sentences missing | intact |
| I4 | ontology plant, literal: "psi is ontic in this arena" | die | rc 3, G-NOTE-KIT: forbidden pattern "psi is ontic" | intact |
| I5 | ontology paraphrase: "the wavefunction is physically real … the ensemble is the true state of affairs" | die (claimed wall) | **rc 0, delivery rewrites artifacts — SURVIVED** (finding F6) | moved, restored |
| I6 | ontology paraphrase, hyphenated: "the density matrix is therefore an incomplete-description of the actual state, settling the fork" | die (claimed wall) | **rc 0 — SURVIVED** (finding F6) | moved, restored |
| I7 | code: pre-registered D1A member e1 → basis(3) (hand edit, not registry) | die at preparation gate | rc 3, G-RHO-EQUAL, nothing written | intact |
| I8 | code: embedded committed S4 witness 1/36 → 1/37 | die | rc 3, G-S4-CONSUMED | intact |
| I9 | pin note + one byte | die | rc 3, G-PIN-DIGESTS | intact, restored |
| I10 | paper-20 quoted sentence "coherent" → "decoherent" | die | rc 3, G-PIN-DIGESTS (digest gate fires ahead of the quote gate) | intact, restored |
| I11 | receipt at rest: 16/729 → 17/729 | forgery cannot survive regeneration | selftest rc 0 (content at rest not validated — detection surface is regeneration); full delivery rc 0 restores committed bytes exactly, forgery wiped | restored |
| I12 | output transcript at rest: G-SENSITIVE PASS → FAIL | same | regeneration restores committed bytes exactly | restored |
| I13 | code: live LOG.md digest serialized into the receipt (the G-ENV lesson) | no internal gate exists; battery must catch | rc 0, receipt moves off committed; under two LOG appends the receipt tracks the live file (6e13136a8fd7 → b0bb91a29e59) — regeneration-byte-compare is the only tripwire, and it works | restored |
| I14 | code: `sorted(imports)` → `list(imports)` (bare set iteration into the receipt) | seed probe must catch | receipt digest differs across PYTHONHASHSEED 0 vs 7 (796772251eda vs 308b8e1be80a) — the battery's seed-variance probe has teeth | restored |

Registry mutants at declared gates (fresh full run each): MUT-W1 → rc 3
died at G-WINDOW1-BLIND; MUT-DIV → rc 3 at G-SENSITIVE; MUT-NULL → rc 3 at
G-NULL-BLIND; artifacts untouched.  `--selftest`: 14/14 falsifiers die at
their declared gates with move proofs, rc 0, write-nothing verified by
before/after hashes.  Hostile argv, all rc 2, tree intact: `--frobnicate`,
`--mutant` (bare), `--verify-paper` (bare), `--selftest --kit`, `-x`,
`--mutant MUT-W1 extra`, `--mutant MUT-BOGUS`.

## 4. WHAT THE VERDICT WORD IS NOW WORTH

The delivered headline — under paper-20's delivered rule, two ensembles with
the same density matrix produce different record distributions from window 2
on, while window 1 is blind by an exact linearity mechanism and the declared
linear completion is blind everywhere — is TRUE on this seat's independent
rebuild at every number, and robust: it holds on the frozen primary (the
only frozen ground the unit stood on), on the unit's unfrozen extras, on the
frozen-but-unrun secondary (this review's R16), on the ordered-history
grain, and on the translation-quotient grain.  The one caveat the addendum
demanded and the unit never measured: at the coarsest relabelling quotient
the first divergence moves to window 3 (R17), so the "-AT-2" index is
grain-indexed, not absolute.  ρ-insufficiency remains, per addendum item 4,
a statement about the delivered rule — not an ontology, not yet an
experimental distinction.

## 5. REQUIRED REPAIRS

1. Run and publish the frozen SECONDARY (maximally mixed; computational vs
   F3-character uniform) through the unit's own instrument; disclose D1C and
   RHO2 as unfrozen extensions (F1).
2. Build all four comparison rows with per-row verdict words and a declared
   relabelling group; publish the grain table incl. the coarsest-quotient
   window-3 fact (F2).
3. Add the three operational-qualification wall sentences to the note,
   gated (F3).
4. Cite and digest-gate the addendum; add the already-inspected/order-of-
   events disclosure (F4).
5. Implement per-occurrence numeral totality (F5); correct or delete the
   false Q(ω) justification in Deviations 4 (F7); erratum to LOG #70's
   "exactly as frozen" and "MACHINE-ENFORCED" sentences (F1/F6).
6. Optional hardening: widen the wall scanner beyond the 7 literals; wire
   `pairwise_distinct_as_ensembles` to the computed value (F6/F9).

## 6. SUMMARY

The physics seals and the paperwork does not.  Roughly 120 independent
recomputations — own arithmetic, own walk, own propagation, record-by-record
against the receipt — reproduce every published number exactly: window-1
blindness with its linearity mechanism, the 16/729-vs-32/729 witness at
{2:1,14:1} with all 27 window-2 records diverging, window-3 divergence, a
null that is provably a linear channel (Kraus completeness verified) and
measures blind at all three windows, a positive control sensitive at window
1 at 16/33 vs 64/129, and the S4 weld to the committed digests; fourteen
live injections, three registry mutants, and seven hostile argv all behave,
with forged artifacts unable to survive regeneration.  But the unit was
built under the #68 addendum and does not comply with it: the frozen
secondary preparation was replaced by an unfrozen one, three of four frozen
comparison rows were silently dropped (and this seat's measurement shows the
dropped quotient row genuinely moves the divergence window at the coarsest
grain), the mandated qualification sentences are absent, numeral totality is
a whitelist rather than a classification, the addendum is nowhere cited, and
LOG #70 asserts compliance that did not occur — plus one false (unmeasured)
mathematical sentence in the deviations and a paraphrase-permeable ontology
scanner.  ACCEPT-WITH-MAJOR-REPAIRS: keep every measured number, repair the
protocol debt before this unit is allowed to decide anything downstream.

*Frozen at delivery of this file; the mirror under the scratchpad was
restored byte-perfect and this review is the seat's only repo write.*
