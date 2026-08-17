# SCOUT-PSI — LIGHT SECOND VERIFIER (the new rows only)

**Seat:** the light second verifier of ledger #91, scoped by order to the
measured rows the #76 seat never saw.  The unit's prior physics (the
RHO1/RHO2 window results, the S4 weld, the null's linearity, the positive
control) is #76-verified and was NOT re-verified here beyond incidental
contact.  **Object, hash-verified at open and at close:**

| file | sha256-12 (open) | sha256-12 (close) |
|---|---|---|
| `v15/note-scoutpsi.md` | `5c46b34a4de9` | `5c46b34a4de9` |
| `v15/code/scoutpsi_exact.py` | `25adcd54a1ea` | `25adcd54a1ea` |
| `v15/code/scoutpsi_output.txt` | `2cbef1d9ceea` | `2cbef1d9ceea` |
| `v15/code/scoutpsi_receipt.json` | `681a9cccfa75` | `681a9cccfa75` |
| `v15/note-scoutpsi-pin-addendum.md` | `e717d3bbc1df` | `e717d3bbc1df` |

**Method.**  Full rebuild of every charged row in my own exact code
(scratchpad `scoutpsi_verify2/rebuild2.py`), sharing no code and no
intermediate with the instrument: own Z[omega] arithmetic, own arena/coin/
shift from the declared constructors, own per-branch walker (ordered-history
tracking, integer numerators over level denominators — a different
propagation layout from the unit's), own density matrices, own T9/S27
quotient machinery and verdict-word builder.  Every published value named in
my charges compared against the committed receipt AND the note's table.
Instrument leg: a git-less mirror under the scratchpad
(`scoutpsi_verify2/mirror/`), baseline regeneration plus 6 injections plus
wall-paraphrase probes; the mirror restored byte-perfect after every run.
Repo access read-only; this file is the seat's only repo write.

---

## VERDICT: ACCEPT

Every number, verdict word, class count, record mass and digest in the new
rows reproduces exactly on my independent rebuild — 45 gated top-level
checks, covering ~1,500 individual exact equalities, zero mismatches.  The
addendum-consumption gate matches the frozen text field by field, the
grain-indexed head tokens match the table, and the disclosures are coherent
with the #77/#83/#90 chain.  One minor hardening finding (V2-F1, below)
that moves no number and falsifies no published sentence.

---

## 1. RECOMPUTATION LEDGER

All from scratch; "=" means exact equality over Q(omega)/Q against both the
receipt and, where published, the note.

| # | recomputation | result |
|---|---|---|
| S1 | frozen secondary: D1S (computational uniform) and D2S (F3-character uniform) each mix to I/27 entry by entry (2 × 729 entries), mixtures equal | = |
| S2 | delivered rule on the frozen pair D1S\|D2S, my walker: window 1 BLIND (0 diverging records); window 2 SENSITIVE with **378** diverging records; first (lexicographically least) diverging record **{26:2}** at masses **0 vs 1/729** | = |
| S3 | receipt `secondary_distributions` window-1 + window-2, record by record, both legs: 27+243 (D1S) and 27+378 (D2S) record masses, all equal; both `window3_digest` values re-derived under the unit's serialization (256673ddcf0d / 377603d9e518) | = |
| S4 | 5 further diverging window-2 records spot-verified with masses: {25:1,26:1} 0\|2/729; {25:2} 0\|1/729; {8:2} 0\|1/729; {0:1,1:1} 0\|2/729; {0:2} 0\|1/729 | = |
| S5 | THE 30-ROW TABLE: all five pairs × {ordered, count} × {raw, T9, S27}, windows 1–3, delivered rule — verdict word AND per-window diverging-class counts re-derived per row; pattern exact: BLIND-AT-1-SENSITIVE-AT-2 everywhere EXCEPT the six RHO1-family S27 rows at BLIND-AT-1-2-SENSITIVE-AT-3; THE CAVEAT confirmed: RHO2's pair and the secondary stay SENSITIVE-AT-2 even at S27 | = (30/30, note AND receipt) |
| S6 | witness counts: ordered-raw 27/486; count-raw 27/477; count-T9 27/240; count-S27 w2 equal, w3 = 2 classes; secondary counts: ordered-raw 729/19683; count-raw 378/3654; count-T9 42/414; count-S27 2/3 | = (8/8 rows) |
| S7 | the T9 class of {23:1,26:1} on the witness pair at window 2: representative {23:1,26:1}, masses **40/729 vs 8/729**; 27 diverging T9 classes | = |
| S8 | quotient consistency: no quotient row diverges where its raw row is equal (5 pairs × 4 quotient rows × 3 windows) | confirmed |
| S9 | null-control grain rows: the selective completion re-run through my own walker is BLIND at windows 1-2-3 at all 5 pairs × all 6 rows (90 comparisons); receipt verdicts all BLIND-AT-1-2-3 | = |
| S10 | mass exactly 1 at every window, both rules, all 7 ensembles (42 checks); per-branch unitarity asserted at every branch of every tree | confirmed |
| S11 | HJW: D1A and D1B internally orthogonal; all 4 cross overlap ratios exactly **1/2** on the two-dimensional span (my own inner products over Z[omega]) | = |
| S12 | Z6 Bloch balance: rho·rho = rho/2 entry by entry for BOTH committed rhos (2 × 729 entries); tr(rho²) = 1/2; the forcing inequality p(1−p) < 1/4 strict for every p ≠ 1/2 (so any two-member pure decomposition is weight-forced to 1/2–1/2 over every field, and the cross term must vanish) | confirmed |
| S13 | the four-member Z[omega] witness {1/3 e0; 1/3 e1; 1/6 (e0+e1); 1/6 (e0−e1)}: weights sum to 1 and the mixture equals RHO1 entry by entry | = |

## 2. COMPLIANCE SPOT-CHECK (light)

**Addendum consumed field by field.**  `addendum_consumed.digest` =
e717d3bbc1df = the live file's sha256-12 (verified at open and close).
Item 1: `frozen_primary_cells` [0, 1] with weights 1/2 (the
embedded-constant anchor is deviation 7, matching the first seat's F8
disclosure); secondary = computational uniform vs F3-character uniform, both
proven = I/27 in-run (S1 re-derives it).  Item 2: the four frozen rows
published with per-row verdicts at every pair, the quotient row at BOTH
named groups (the unnamed-group freeze defect disclosed as deviation 6).
Item 3: the frozen selective null is the one that ran (declaration + Kraus
verified; blindness re-derived at S9).  Item 4: all qualification sentences
present in the note and gated (G-QUAL-GATED), the #80 sharpenings included.
Item 5: per-occurrence totality implemented, 616/616, 0 unclassified.  All
eight `checks` fields True and each checked against the frozen text.

**Head tokens vs the table.**  The grain-indexed verdict string is identical
across note, output and receipt, and each token re-derives from my own
measurement: EVERY-MEASURED-PAIR...AT-THE-RAW-AND-TRANSLATION-GRAINS = the
20 raw/T9 rows; SECONDARY-...-AT-378-DIVERGING-RECORDS = S2;
BLIND-AT-2-SENSITIVE-AT-3-AT-THE-COARSEST-QUOTIENT-ON-THE-WITNESS-PAIR =
the witness S27 rows; the RHO1-family-only caveat sentence matches S5.

**Disclosures vs the #83 timeline.**  The receipt's `order_of_events` (the
#68 mid-build freeze, never routed; #70 built to the pin as launched with
the already-inspected computations named; the repair receiving the addendum
text in its launch order) is coherent with LOG #77's erratum and with the
#83 outage chain — LOG #90 discloses the continuation ("audited the
predecessor's near-complete instrument end-to-end") that the #83 kill made
necessary.  No contradiction found.  (Incidental: the note's "33 gate
names" vs the transcript's "gates: 31" is consistent — 33 registered names,
31 ledger rows; G-DETERMINISM and G-SERIAL are enforced outside the ledger.)

**Fresh wall paraphrases (mirror).**  Three fresh sentences overlapping the
widened blacklist die hyphen-robust at G-NOTE-KIT: "rho-is-incomplete
because the mixture members carry the facts" (killed by `rho is
incomplete`), "quietly settling-the-fork toward ontic ensembles" (killed by
`settling the fork`), "the wave amplitude is-physically-real" (killed by
`is physically real`).  A fourth, genuinely novel paraphrase with no
blacklisted substring ("the ensemble members are what exist; the density
operator is mere bookkeeping") SURVIVES — which is exactly what the note
discloses ("the general fresh-paraphrase condition stays registered, not
claimed"): measured residual, not a compliance violation.

## 3. INSTRUMENT — injections (git-less mirror, absolute scratchpad path)

Baseline first: both artifacts DELETED from the mirror and regenerated —
output and receipt byte-identical to committed.  Mirror restored
byte-perfect after every injection (close hashes above).

| inj | what was forged | expected | observed | tree |
|---|---|---|---|---|
| I1 | note table verdict at a non-RHO1 row: RHO2 count-S27 B1-S2 → B12-S3 | die | rc 3, G-NUMERAL-TOTALITY (the extra numeral moved the 616 totals) | intact, restored |
| I2 | the secondary's 378 → 379 in the Z1 sentence | die | rc 3, G-NOTE-KIT: kit sentence missing | intact, restored |
| I3 | the {26:2} mass 1/729 → 2/729 | die | rc 3, G-NOTE-KIT: kit sentence missing + bound numeral absent | intact, restored |
| I4 | the frozen-addendum citation e717d3bbc1df → e717d3bbc1aa in the note | die | rc 3, G-NOTE-KIT: kit sentence missing | intact, restored |
| I5 | registry mutant MUT-SECEXP (corrupts the expected 378) | die at G-SECONDARY-EXPECT | rc 3, died there; artifacts untouched | intact |
| I6 | registry mutant MUT-GRAIN (collapses the S27 map) | die at G-GRAIN-VERDICTS | rc 3, died there; artifacts untouched | intact |

Follow-up probe on I1 (the finding): a **numeral-count-preserving** verdict
swap on the same row (B1-S2 → "BLIND-AT-2-SENSITIVE-AT-1") SURVIVES full
delivery (rc 0, artifacts rewritten around it) — see V2-F1.

## 4. FINDINGS

**V2-F1 — MINOR — the note's grain-table verdict words are not individually
machine-matched to the measurement.**  I1's death was incidental (the
occurrence-count tripwire); a swap that preserves the numeral count passes
G-NOTE-KIT, G-GRAIN-VERDICTS and totality (the GRAIN-line numerals are bound
wholesale to the `grain_rows/delivered` subtree, and `resolve_ref`'s
containment test accepts any digit present anywhere in it).  Mitigations,
measured: the measured verdicts ARE gated in-run (G-GRAIN-VERDICTS, with the
witness verdicts in the gate's data field); the same 30-row table is
rendered into the output transcript directly from measurement; any note edit
moves the note digest stamped in both artifacts; and this seat verified the
committed note's table matches the measurement 30/30.  No published sentence
is false.  Optional hardening for a future micro-repair: render the table
rows as kit-matched lines.

**V2-F2 — OBSERVATION, no violation.**  The fresh-paraphrase residual
(section 2) is real and exactly as disclosed by the unit; the disclosure is
honest and the three widened-blacklist kills work hyphen-robust.

No other findings.  Zero numeric discrepancies anywhere in the charged rows.

## 5. SUMMARY

The new rows seal.  Rebuilt from scratch in my own exact code — own
Z[omega] arithmetic, own walker, own quotient machinery — the frozen
secondary proves to I/27 from both frozen decompositions and re-derives
blind-at-1 / sensitive-at-2 with 378 diverging records, first record {26:2}
at 0 vs 1/729, with the receipt's window-1/2 distributions equal record by
record and both window-3 digests re-derived; the full 30-row four-grain
table re-derives verdict-for-verdict and count-for-count, including the
strengthened caveat that the coarsest-quotient blindness is a RHO1-family
property while RHO2 and the secondary stay sensitive-at-2 even under full
Sym(27) relabelling; the null control is blind at every pair, grain and
window; the HJW pair is mutually unbiased at exactly 1/2; and both Z6
witnesses (Bloch balance forcing 1/2–1/2, the four-member Z[omega]
decomposition of RHO1) verify entry by entry.  The addendum-consumption
gate matches the frozen text field by field, the head tokens match the
table, the disclosures cohere with the #77/#83/#90 chain, six injections
behave (four note forgeries and two registry mutants all dead, tree
intact), and the only findings are a minor table-rendering hardening
(V2-F1) and the honestly-disclosed paraphrase residual.  ACCEPT.

*Frozen at delivery of this file; the mirror under the scratchpad was
restored byte-perfect and this review is the seat's only repo write.*
