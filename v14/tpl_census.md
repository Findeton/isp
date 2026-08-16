# TPL EXPOSURE CENSUS — the nine disease families over the sealed v14 instruments

*The #267 template sweep, chartered at v14 ledger #371 per #362.  Companion to `v14/TEMPLATE.md` (the spec) and `v14/code/era_template.py` (the reference implementations).  Rendered from `v14/code/tpl_census_receipt.json`; every numeral below is interpolated from the run's own registries.*

**Scope.** 39 sealed instruments at HEAD, 36 of them with a K3 (instrument) panel and 3 without.  179 panel citations over 36 reviews, each machine-located in the review it names.  9 structural probes per instrument, 351 probe verdicts in all, every one run read-only in a scratch mirror.  **Zero sealed objects were edited, executed or re-delivered.**

## 1. How to read this census

Two layers, published side by side and never merged.

**THE PANEL LAYER** is what the units' own K3 seats measured with LIVE INJECTIONS — a corruption that survived at exit 0.  It is the authoritative layer.  It is also incomplete by construction: a seat reports what it probed, and no seat probed all nine.

**THE PROBE LAYER** is structural and uniform.  It asks of the source at HEAD whether the MECHANISM each family names is present, not whether a corruption survives.  `CARRIES` means the mechanism is absent; `PARTIAL` means some legs are present; `CLOSED` means all the legs the probe knows how to see are present; `NO-SURFACE` means the instrument has no such surface (an honest denominator, #34).  **A probe verdict is not an injection verdict.**  `CLOSED` says the shape is there, never that the shape has teeth — LOR #269's caveat of record applies to this census as much as to a mutant sweep.

The two layers disagree productively.  Where a panel measured PRESENT at review time and the probe reads CLOSED at HEAD, a repair landed between them; that is the census's main use.

## 2. The nine families

| # | family | reference check | probe asks |
|---|---|---|---|
| (a) | SEAL-INTEGRITY | `T-SEAL-PROMOTION` | does the promotion path re-verify the GATE-TIME seals and RECOMPUTE totality before the artifacts land? |
| (b) | TRANSCRIPT-BOUND-TO-THE-LEDGER | `T-TRANSCRIPT-BOUND` | is the transcript reconciled with the ledger by content — its PASS lines parsed back and compared against the gate rows? |
| (c) | SEMANTIC-WALLS | `T-WALL-SEMANTIC` | are the wall patterns semantic (regex, case-folded) with a positive leg, rather than literal strings? |
| (d) | VERBATIM-ANCHORS-CONSUMED | `T-ANCHOR-CONSUMED` | is a verbatim anchor's text CONSUMED — read back out of the anchor registry by a gate predicate? |
| (e) | CLAIMS-BY-EQUALITY-TWO-WAY-TABLE-SIGHTED | `T-CLAIMS-EQUAL` | are claims, tables and fences gated by EQUALITY in both directions rather than containment or a floor? |
| (f) | SENTENCE-LEVEL-REFERENT-BINDING | `T-REFERENT-BOUND` | is there a sentence-level referent binding, per occurrence, over prose only? |
| (g) | NO-TYPED-COUNTS | `T-NO-TYPED-COUNTS` | how many numerals are TYPED into published gate statements rather than interpolated from a live registry? |
| (h) | FALSIFIERS-POISON-MEASUREMENTS | `T-FALSIFIER-POISONS` | how many falsifier hooks poison a verdict variable (a constant boolean, a constant append) instead of a measurement? |
| (i) | READ-SETS-AT-THE-I-O-ACCESSOR | `T-READ-SET` | is the read set recorded where reads happen (an audit hook or an open wrapper) rather than inside one helper? |

## 3. The exposure matrix

One row per instrument.  Each cell is `probe/panel`: the probe verdict at HEAD, then the panel's live-injection verdict where its seat reported one (`P` = PRESENT, `A` = ABSENT, `·` = not reported).

| instrument | sha256-12 | (a) | (b) | (c) | (d) | (e) | (f) | (g) | (h) | (i) |
|---|---|---|---|---|---|---|---|---|---|---|
| `act_exact.py` | `a90559ee0e0f` | CLSD/P | CARR/P | PART/P | CARR/P | PART/P | CARR/· | CARR/P | PART/· | CARR/· |
| `aid_exact.py` | `b4419b0d1daa` | CLSD/P | PART/P | CARR/P | CARR/P | PART/P | PART/P | CARR/· | PART/P | PART/· |
| `coupling_exact.py` | `72e7b299f66e` | CLSD/P | PART/P | CLSD/· | CARR/· | PART/P | CARR/P | CARR/· | PART/P | PART/P |
| `cra_accumulation_exact.py` | `dc629dfac7be` | CARR/P | CARR/· | CARR/· | CARR/· | CARR/P | CARR/P | CARR/P | CLSD/P | CARR/P |
| `crb_stochastic_exact.py` | `5f2a54ea8a98` | CARR/· | CARR/· | CARR/· | CARR/· | CARR/· | CARR/· | CARR/· | CLSD/· | CARR/· |
| `crc_coarsegrain_exact.py` | `fc15b9922ec6` | CARR/· | CARR/· | n/s/· | CARR/· | CARR/· | CARR/· | CARR/· | CLSD/· | CARR/· |
| `crd_tower_exact.py` | `1583b235da86` | CARR/· | CARR/· | CARR/· | CARR/· | CARR/· | CARR/· | CARR/· | CLSD/· | CARR/· |
| `epr_exact.py` | `ac2582b44c37` | CLSD/P | PART/P | CLSD/P | CARR/P | PART/P | PART/P | CARR/P | PART/P | CARR/A |
| `fac_exact.py` | `f7df0fad29e5` | CLSD/P | PART/P | PART/P | CARR/· | CLSD/P | PART/P | PART/· | PART/· | PART/· |
| `gdl_exact.py` | `55963dcbe4b4` | CLSD/· | PART/· | PART/· | CARR/· | PART/P | CARR/P | CARR/P | PART/P | PART/· |
| `giter_exact.py` | `a75c435bffda` | CARR/P | PART/· | CARR/P | CARR/· | CARR/· | CARR/· | CARR/· | CLSD/P | CARR/· |
| `gmain_exact.py` | `a47d622c7608` | CARR/· | CARR/· | CARR/· | CARR/· | CARR/P | CARR/· | CARR/P | CLSD/P | CARR/P |
| `gprep_foundation_exact.py` | `8ddbc93cd48d` | CARR/· | CARR/· | n/s/· | CARR/P | CARR/· | CARR/· | CARR/· | CLSD/P | CARR/P |
| `lor_exact.py` | `e8bd6214bbff` | CLSD/P | CARR/P | CLSD/P | CARR/· | CLSD/P | CARR/P | CARR/P | PART/· | PART/P |
| `ndep_exact.py` | `3ba62f7a5ac5` | CLSD/P | CARR/P | PART/P | CARR/P | PART/P | PART/P | CARR/P | PART/P | PART/· |
| `occ_exact.py` | `49b739cecac1` | CLSD/· | PART/· | CLSD/· | CARR/· | PART/P | PART/P | CLSD/· | CLSD/· | PART/· |
| `perl_exact.py` | `9764427bf14a` | CLSD/P | CARR/· | CLSD/· | CARR/· | PART/P | CARR/P | CARR/P | PART/P | PART/P |
| `perr_exact.py` | `603319c24257` | CLSD/P | PART/P | CLSD/P | CARR/P | PART/P | PART/P | CLSD/P | CLSD/· | CARR/P |
| `pot_exact.py` | `a811bbb92138` | PART/P | PART/P | PART/P | CLSD/P | CARR/P | CARR/P | PART/P | PART/P | CARR/· |
| `r1_continuum_exact.py` | `e5a895c894d0` | CARR/· | CARR/· | CARR/· | CARR/· | CARR/P | CARR/P | CARR/P | CLSD/P | CARR/· |
| `r2_manifold_exact.py` | `a4b0e71819be` | CARR/· | CARR/· | CARR/· | CARR/· | CARR/P | CARR/· | CARR/· | CLSD/P | CARR/· |
| `r3_relativity_exact.py` | `afe3452d067b` | CARR/· | CARR/· | CARR/· | CARR/· | CARR/· | CARR/· | CARR/P | CLSD/P | CARR/P |
| `r3_weld_exact.py` | `f95a26a1764b` | CLSD/· | PART/· | PART/P | CARR/· | CARR/· | CARR/· | CARR/· | PART/P | PART/· |
| `r4_defect_stage_exact.py` | `2959c5a6a84b` | CARR/· | CARR/· | CARR/· | CARR/· | CARR/P | CARR/· | CARR/P | PART/P | CARR/P |
| `r4b_momentum_exact.py` | `4216f3de5f44` | PART/P | CARR/· | CARR/· | CARR/P | CARR/· | CARR/· | CARR/· | PART/· | PART/P |
| `r4c_multi_exact.py` | `f202cf185804` | PART/P | CARR/· | PART/· | CARR/P | PART/P | CARR/· | CARR/P | PART/· | CARR/P |
| `r4dec_exact.py` | `1958a8cdfe28` | CLSD/· | PART/· | CLSD/· | CARR/· | PART/P | CARR/· | CARR/P | PART/P | PART/P |
| `r5_gauge_exact.py` | `0d98de793b79` | CLSD/P | CARR/· | PART/P | CARR/· | CARR/· | CARR/· | CARR/· | PART/P | PART/· |
| `r5m_measure_exact.py` | `faf353385905` | CLSD/· | PART/· | CLSD/P | CARR/· | CARR/P | CARR/P | CARR/P | PART/P | CARR/· |
| `r6a_refinement_exact.py` | `a3a15ed3c3c8` | CARR/· | CARR/P | PART/· | CARR/P | CARR/· | CARR/P | CARR/P | CLSD/P | CARR/· |
| `r6bp_transport_exact.py` | `b1562bce5a5f` | CARR/· | CARR/· | n/s/· | CARR/P | CARR/P | CARR/· | CLSD/P | PART/P | CARR/P |
| `sec_exact.py` | `558cc00b3e28` | CLSD/P | CARR/· | CLSD/· | CARR/P | PART/P | PART/· | CARR/P | CLSD/P | CARR/P |
| `sec2_exact.py` | `bac3bf371c42` | CLSD/P | CARR/P | PART/P | CARR/P | PART/P | PART/P | CARR/P | PART/P | PART/P |
| `sig_exact.py` | `720487178b75` | CLSD/· | PART/P | PART/· | CLSD/P | PART/P | CARR/P | CARR/· | PART/P | CARR/P |
| `smu_exact.py` | `126912ae7142` | CLSD/P | CARR/· | PART/· | CARR/P | CARR/P | CARR/P | CARR/P | PART/P | CARR/· |
| `spc_exact.py` | `234493dc5fce` | CLSD/P | CARR/P | CLSD/· | CARR/A | PART/· | PART/P | CARR/· | PART/A | CARR/· |
| `u4_crystals_exact.py` | `d3aac4c5f413` | PART/P | PART/· | PART/P | CARR/· | CARR/· | CARR/· | PART/· | CLSD/· | CARR/· |
| `u4b_schedule_exact.py` | `6d5278b38dcc` | PART/P | PART/· | CLSD/P | CARR/· | CARR/· | PART/· | CARR/P | PART/P | PART/P |
| `w2_census_exact.py` | `9bfcef7b3e11` | CARR/· | CARR/· | n/s/· | CARR/P | CARR/P | CARR/· | CARR/· | PART/· | CARR/P |

## 4. Counts per family

| family | probe CARRIES | probe PARTIAL | probe CLOSED | probe NO-SURFACE | panel PRESENT | panel ABSENT |
|---|---|---|---|---|---|---|
| (a) SEAL-INTEGRITY | 14 | 5 | 20 | 0 | 21 | 0 |
| (b) TRANSCRIPT-BOUND-TO-THE-LEDGER | 24 | 15 | 0 | 0 | 13 | 0 |
| (c) SEMANTIC-WALLS | 11 | 13 | 11 | 4 | 15 | 0 |
| (d) VERBATIM-ANCHORS-CONSUMED | 37 | 0 | 2 | 0 | 16 | 1 |
| (e) CLAIMS-BY-EQUALITY-TWO-WAY-TABLE-SIGHTED | 22 | 15 | 2 | 0 | 26 | 0 |
| (f) SENTENCE-LEVEL-REFERENT-BINDING | 29 | 10 | 0 | 0 | 19 | 0 |
| (g) NO-TYPED-COUNTS | 33 | 3 | 3 | 0 | 22 | 0 |
| (h) FALSIFIERS-POISON-MEASUREMENTS | 0 | 24 | 15 | 0 | 26 | 1 |
| (i) READ-SETS-AT-THE-I-O-ACCESSOR | 25 | 14 | 0 | 0 | 18 | 1 |

The probe layer reads `CARRIES` or `PARTIAL` at 294 of the 347 instrument-family cells it could evaluate (4 cells have no surface); the panel layer measured a live PRESENT at 176 cells and an ABSENT at 3.  36 instruments carry at least one panel-measured PRESENT.

## 5. Where the layers disagree

| instrument | family | panel | probe at HEAD | reviewed sha256-12 | HEAD sha256-12 | reading |
|---|---|---|---|---|---|---|
| `act_exact.py` | (a) | PRESENT | CLOSED | `02df3f00f788` | `a90559ee0e0f` | the object MOVED after the review; the mechanism is present at HEAD |
| `aid_exact.py` | (a) | PRESENT | CLOSED | `edf3a540cd57` | `b4419b0d1daa` | the object MOVED after the review; the mechanism is present at HEAD |
| `coupling_exact.py` | (a) | PRESENT | CLOSED | `9e71cf511ab3` | `72e7b299f66e` | the object MOVED after the review; the mechanism is present at HEAD |
| `cra_accumulation_exact.py` | (h) | PRESENT | CLOSED | `e289d3afc852` | `dc629dfac7be` | the object MOVED after the review; the mechanism is present at HEAD |
| `epr_exact.py` | (a) | PRESENT | CLOSED | `9ed817d9649d` | `ac2582b44c37` | the object MOVED after the review; the mechanism is present at HEAD |
| `epr_exact.py` | (c) | PRESENT | CLOSED | `9ed817d9649d` | `ac2582b44c37` | the object MOVED after the review; the mechanism is present at HEAD |
| `epr_exact.py` | (i) | ABSENT | CARRIES | `9ed817d9649d` | `ac2582b44c37` | the two layers measure different legs — the seat measured existence and naming, the probe measures the accessor; both stand at their own leg |
| `fac_exact.py` | (a) | PRESENT | CLOSED | `53e1e2683937` | `f7df0fad29e5` | the object MOVED after the review; the mechanism is present at HEAD |
| `fac_exact.py` | (e) | PRESENT | CLOSED | `53e1e2683937` | `f7df0fad29e5` | the object MOVED after the review; the mechanism is present at HEAD |
| `giter_exact.py` | (h) | PRESENT | CLOSED | `not located` | `a75c435bffda` | the review publishes no digest for this instrument, so the comparison could not be made — THE SEAT IS AUTHORITY |
| `gmain_exact.py` | (h) | PRESENT | CLOSED | `not located` | `a47d622c7608` | the review publishes no digest for this instrument, so the comparison could not be made — THE SEAT IS AUTHORITY |
| `gprep_foundation_exact.py` | (h) | PRESENT | CLOSED | `not located` | `8ddbc93cd48d` | the review publishes no digest for this instrument, so the comparison could not be made — THE SEAT IS AUTHORITY |
| `lor_exact.py` | (a) | PRESENT | CLOSED | `878e6007b785` | `e8bd6214bbff` | the object MOVED after the review; the mechanism is present at HEAD |
| `lor_exact.py` | (c) | PRESENT | CLOSED | `878e6007b785` | `e8bd6214bbff` | the object MOVED after the review; the mechanism is present at HEAD |
| `lor_exact.py` | (e) | PRESENT | CLOSED | `878e6007b785` | `e8bd6214bbff` | the object MOVED after the review; the mechanism is present at HEAD |
| `ndep_exact.py` | (a) | PRESENT | CLOSED | `d83df6c1e07d` | `3ba62f7a5ac5` | the object MOVED after the review; the mechanism is present at HEAD |
| `perl_exact.py` | (a) | PRESENT | CLOSED | `976d5b9e4ac8` | `9764427bf14a` | the object MOVED after the review; the mechanism is present at HEAD |
| `perr_exact.py` | (a) | PRESENT | CLOSED | `d2f8fdac143d` | `603319c24257` | the object MOVED after the review; the mechanism is present at HEAD |
| `perr_exact.py` | (c) | PRESENT | CLOSED | `d2f8fdac143d` | `603319c24257` | the object MOVED after the review; the mechanism is present at HEAD |
| `perr_exact.py` | (g) | PRESENT | CLOSED | `d2f8fdac143d` | `603319c24257` | the object MOVED after the review; the mechanism is present at HEAD |
| `pot_exact.py` | (d) | PRESENT | CLOSED | `8c11f16002d1` | `a811bbb92138` | the object MOVED after the review; the mechanism is present at HEAD |
| `r1_continuum_exact.py` | (h) | PRESENT | CLOSED | `not located` | `e5a895c894d0` | the review publishes no digest for this instrument, so the comparison could not be made — THE SEAT IS AUTHORITY |
| `r2_manifold_exact.py` | (h) | PRESENT | CLOSED | `not located` | `a4b0e71819be` | the review publishes no digest for this instrument, so the comparison could not be made — THE SEAT IS AUTHORITY |
| `r3_relativity_exact.py` | (h) | PRESENT | CLOSED | `not located` | `afe3452d067b` | the review publishes no digest for this instrument, so the comparison could not be made — THE SEAT IS AUTHORITY |
| `r5_gauge_exact.py` | (a) | PRESENT | CLOSED | `not located` | `0d98de793b79` | the review publishes no digest for this instrument, so the comparison could not be made — THE SEAT IS AUTHORITY |
| `r5m_measure_exact.py` | (c) | PRESENT | CLOSED | `f7de59960fe6` | `faf353385905` | the object MOVED after the review; the mechanism is present at HEAD |
| `r6a_refinement_exact.py` | (h) | PRESENT | CLOSED | `not located` | `a3a15ed3c3c8` | the review publishes no digest for this instrument, so the comparison could not be made — THE SEAT IS AUTHORITY |
| `r6bp_transport_exact.py` | (g) | PRESENT | CLOSED | `not located` | `b1562bce5a5f` | the review publishes no digest for this instrument, so the comparison could not be made — THE SEAT IS AUTHORITY |
| `sec_exact.py` | (a) | PRESENT | CLOSED | `6481a8706503` | `558cc00b3e28` | the object MOVED after the review; the mechanism is present at HEAD |
| `sec_exact.py` | (h) | PRESENT | CLOSED | `6481a8706503` | `558cc00b3e28` | the object MOVED after the review; the mechanism is present at HEAD |
| `sec2_exact.py` | (a) | PRESENT | CLOSED | `4cb4011cfa05` | `bac3bf371c42` | the object MOVED after the review; the mechanism is present at HEAD |
| `sig_exact.py` | (d) | PRESENT | CLOSED | `a41b6d549e14` | `720487178b75` | the object MOVED after the review; the mechanism is present at HEAD |
| `smu_exact.py` | (a) | PRESENT | CLOSED | `not located` | `126912ae7142` | the review publishes no digest for this instrument, so the comparison could not be made — THE SEAT IS AUTHORITY |
| `spc_exact.py` | (a) | PRESENT | CLOSED | `6b399487f286` | `234493dc5fce` | the object MOVED after the review; the mechanism is present at HEAD |
| `spc_exact.py` | (d) | ABSENT | CARRIES | `6b399487f286` | `234493dc5fce` | the two layers measure different legs — the seat measured existence and naming, the probe measures the accessor; both stand at their own leg |
| `u4b_schedule_exact.py` | (c) | PRESENT | CLOSED | `not located` | `6d5278b38dcc` | the review publishes no digest for this instrument, so the comparison could not be made — THE SEAT IS AUTHORITY |

34 cells read panel PRESENT against probe CLOSED.  Of those, 23 sit on an instrument whose digest MOVED after its review — a repair landed, and the mechanism is present at HEAD — and 0 sit on an instrument that has NOT moved, where the probe is crediting a shape the seat measured toothless and THE SEAT IS AUTHORITY; on 11 the review publishes no digest and the comparison could not be made.  2 cells read panel ABSENT against probe CARRIES; those are two legs, not a contradiction.  The reviewed digest was located in 21 of the 36 reviews.

## 6. Registered residuals (already in the ledger; this sweep owns them)

| unit | family | ledger | residual |
|---|---|---|---|
| `perr` | (g) | #353 | six claim templates still TYPE numerals whose facts are gated elsewhere; liftable string-identical repair REGISTERED for the #267 template sweep |
| `epr` | (g) | #359 | two typed-testimony receipt leaves (subprocesses / reads outside the list), safe by G-READS-DECLARED but typed — folds into the #267 sweep |
| `pot` | (f) | #363 | the REFERENT-BINDING residual PUBLISHED as outside the wall's reach |
| `sec` | (g) | #367 | 234 small structural numerals stated honestly in-paper as a residual |

## 7. Panel citations, machine-located

Every citation below was located in the review it names, at the review's published sha256-12.  179 citations, 179 located, 0 unlocated.

| unit | family | finding | verdict | review | review sha256-12 | occurrences |
|---|---|---|---|---|---|---|
| `act` | (a) | MAJOR-2 | PRESENT | `v14/review-act-instrument.md` | `49045aa82b90` | 5 |
| `aid` | (a) | MAJOR-5 | PRESENT | `v14/review-aid-instrument.md` | `b333a08ba565` | 1 |
| `coup` | (a) | MAJOR-2 | PRESENT | `v14/review-coup-instrument.md` | `8e71c5df2b8e` | 2 |
| `cra` | (a) | MAJOR-3 | PRESENT | `v14/review-cra-instrument.md` | `64235eac24b9` | 1 |
| `epr` | (a) | MAJOR-5 | PRESENT | `v14/review-epr-instrument.md` | `30950725b61a` | 3 |
| `fac` | (a) | MAJOR-4 | PRESENT | `v14/review-fac-instrument.md` | `b328a819d752` | 4 |
| `giter` | (a) | MAJOR-2 | PRESENT | `v14/review-giter-instrument.md` | `c4e0e08050e7` | 3 |
| `lor` | (a) | MAJOR-5 | PRESENT | `v14/review-lor-instrument.md` | `c90b0231a147` | 3 |
| `ndep` | (a) | MAJOR-1 | PRESENT | `v14/review-ndep-instrument.md` | `1133b154ff8d` | 8 |
| `perl` | (a) | MAJOR-2 | PRESENT | `v14/review-perl-instrument.md` | `a624d1a5211a` | 5 |
| `perr` | (a) | MAJOR-7 | PRESENT | `v14/review-perr-instrument.md` | `802071ab4c91` | 4 |
| `pot` | (a) | MAJOR-6 | PRESENT | `v14/review-pot-instrument.md` | `6ffa7681fb94` | 1 |
| `r4b` | (a) | MAJOR-1 | PRESENT | `v14/review-r4b-instrument.md` | `29c75e73ede9` | 8 |
| `r4c` | (a) | MAJOR-4 | PRESENT | `v14/review-r4c-instrument.md` | `73dd15300ea8` | 7 |
| `r5` | (a) | MAJOR-5 | PRESENT | `v14/review-r5-instrument.md` | `f15f4136446e` | 4 |
| `sec` | (a) | MAJOR-4 | PRESENT | `v14/review-sec-instrument.md` | `d872435e6064` | 5 |
| `sec2` | (a) | MAJOR-1 | PRESENT | `v14/review-sec2-instrument.md` | `5724179ec187` | 4 |
| `smu` | (a) | MAJOR-2 | PRESENT | `v14/review-smu-instrument.md` | `dd11bd925adc` | 2 |
| `spc` | (a) | MAJOR-1 | PRESENT | `v14/review-spc-instrument.md` | `c18b16c76992` | 5 |
| `u4` | (a) | MAJOR-3 | PRESENT | `v14/review-u4-instrument.md` | `96ac6ff9a264` | 1 |
| `u4b` | (a) | MAJOR-1 | PRESENT | `v14/review-u4b-instrument.md` | `ebcfbb49fa88` | 2 |
| `act` | (b) | MAJOR-2 | PRESENT | `v14/review-act-instrument.md` | `49045aa82b90` | 5 |
| `aid` | (b) | MAJOR-5 | PRESENT | `v14/review-aid-instrument.md` | `b333a08ba565` | 1 |
| `coup` | (b) | MAJOR-2 | PRESENT | `v14/review-coup-instrument.md` | `8e71c5df2b8e` | 2 |
| `epr` | (b) | MAJOR-6 | PRESENT | `v14/review-epr-instrument.md` | `30950725b61a` | 4 |
| `fac` | (b) | m1 | PRESENT | `v14/review-fac-instrument.md` | `b328a819d752` | 3 |
| `lor` | (b) | MAJOR-5 | PRESENT | `v14/review-lor-instrument.md` | `c90b0231a147` | 3 |
| `ndep` | (b) | MAJOR-2 | PRESENT | `v14/review-ndep-instrument.md` | `1133b154ff8d` | 5 |
| `perr` | (b) | MAJOR-3 | PRESENT | `v14/review-perr-instrument.md` | `802071ab4c91` | 5 |
| `pot` | (b) | MAJOR-7 | PRESENT | `v14/review-pot-instrument.md` | `6ffa7681fb94` | 1 |
| `r6a` | (b) | M4 | PRESENT | `v14/review-r6a-instrument.md` | `8d05097f3d0f` | 2 |
| `sec2` | (b) | MAJOR-9 | PRESENT | `v14/review-sec2-instrument.md` | `5724179ec187` | 5 |
| `sig` | (b) | MINOR-5 | PRESENT | `v14/review-sig-instrument.md` | `6d0b7e73279a` | 1 |
| `spc` | (b) | m6 | PRESENT | `v14/review-spc-instrument.md` | `c18b16c76992` | 3 |
| `act` | (c) | MAJOR-4 | PRESENT | `v14/review-act-instrument.md` | `49045aa82b90` | 11 |
| `aid` | (c) | MAJOR-3 | PRESENT | `v14/review-aid-instrument.md` | `b333a08ba565` | 1 |
| `epr` | (c) | MAJOR-7 | PRESENT | `v14/review-epr-instrument.md` | `30950725b61a` | 3 |
| `fac` | (c) | MAJOR-3 | PRESENT | `v14/review-fac-instrument.md` | `b328a819d752` | 6 |
| `giter` | (c) | MAJOR-6 | PRESENT | `v14/review-giter-instrument.md` | `c4e0e08050e7` | 1 |
| `lor` | (c) | MAJOR-1 | PRESENT | `v14/review-lor-instrument.md` | `c90b0231a147` | 6 |
| `ndep` | (c) | MAJOR-6 | PRESENT | `v14/review-ndep-instrument.md` | `1133b154ff8d` | 6 |
| `perr` | (c) | MAJOR-6 | PRESENT | `v14/review-perr-instrument.md` | `802071ab4c91` | 2 |
| `pot` | (c) | MAJOR-1 | PRESENT | `v14/review-pot-instrument.md` | `6ffa7681fb94` | 1 |
| `r3w` | (c) | M3 | PRESENT | `v14/review-r3w-instrument.md` | `f04d46009228` | 3 |
| `r5` | (c) | MAJOR-3 | PRESENT | `v14/review-r5-instrument.md` | `f15f4136446e` | 3 |
| `r5m` | (c) | M2 | PRESENT | `v14/review-r5m-instrument.md` | `0890efbf3071` | 3 |
| `sec2` | (c) | MAJOR-11 | PRESENT | `v14/review-sec2-instrument.md` | `5724179ec187` | 4 |
| `u4` | (c) | MAJOR-1 | PRESENT | `v14/review-u4-instrument.md` | `96ac6ff9a264` | 1 |
| `u4b` | (c) | MAJOR-6 | PRESENT | `v14/review-u4b-instrument.md` | `ebcfbb49fa88` | 2 |
| `act` | (d) | MAJOR-3 | PRESENT | `v14/review-act-instrument.md` | `49045aa82b90` | 5 |
| `aid` | (d) | MAJOR-4 | PRESENT | `v14/review-aid-instrument.md` | `b333a08ba565` | 1 |
| `epr` | (d) | MINOR-10 | PRESENT | `v14/review-epr-instrument.md` | `30950725b61a` | 2 |
| `gprep` | (d) | MAJOR-4 | PRESENT | `v14/review-gprep-instrument.md` | `aa9b0362fbed` | 2 |
| `ndep` | (d) | MAJOR-4 | PRESENT | `v14/review-ndep-instrument.md` | `1133b154ff8d` | 4 |
| `perr` | (d) | MAJOR-4 | PRESENT | `v14/review-perr-instrument.md` | `802071ab4c91` | 3 |
| `pot` | (d) | MAJOR-9 | PRESENT | `v14/review-pot-instrument.md` | `6ffa7681fb94` | 2 |
| `r4b` | (d) | MAJOR-2 | PRESENT | `v14/review-r4b-instrument.md` | `29c75e73ede9` | 3 |
| `r4c` | (d) | MAJOR-1 | PRESENT | `v14/review-r4c-instrument.md` | `73dd15300ea8` | 9 |
| `r6a` | (d) | M5 | PRESENT | `v14/review-r6a-instrument.md` | `8d05097f3d0f` | 4 |
| `r6bp` | (d) | M3 | PRESENT | `v14/review-r6bp-instrument.md` | `05f6032bbc86` | 1 |
| `sec` | (d) | MAJOR-5 | PRESENT | `v14/review-sec-instrument.md` | `d872435e6064` | 1 |
| `sec2` | (d) | MINOR-3 | PRESENT | `v14/review-sec2-instrument.md` | `5724179ec187` | 2 |
| `sig` | (d) | MAJOR-5 | PRESENT | `v14/review-sig-instrument.md` | `6d0b7e73279a` | 2 |
| `smu` | (d) | MAJOR-1 | PRESENT | `v14/review-smu-instrument.md` | `dd11bd925adc` | 3 |
| `w2` | (d) | MAJOR-4 | PRESENT | `v14/review-w2-instrument.md` | `e83855bd5e74` | 2 |
| `spc` | (d) | MAJOR-1 | ABSENT | `v14/review-spc-instrument.md` | `c18b16c76992` | 5 |
| `act` | (e) | MAJOR-1 | PRESENT | `v14/review-act-instrument.md` | `49045aa82b90` | 7 |
| `aid` | (e) | MAJOR-3 | PRESENT | `v14/review-aid-instrument.md` | `b333a08ba565` | 1 |
| `coup` | (e) | MAJOR-3 | PRESENT | `v14/review-coup-instrument.md` | `8e71c5df2b8e` | 2 |
| `cra` | (e) | MAJOR-2 | PRESENT | `v14/review-cra-instrument.md` | `64235eac24b9` | 3 |
| `epr` | (e) | MAJOR-1 | PRESENT | `v14/review-epr-instrument.md` | `30950725b61a` | 5 |
| `fac` | (e) | MAJOR-5 | PRESENT | `v14/review-fac-instrument.md` | `b328a819d752` | 7 |
| `gdl` | (e) | MAJOR-2 | PRESENT | `v14/review-gdl-instrument.md` | `1565d161354f` | 6 |
| `lor` | (e) | MAJOR-2 | PRESENT | `v14/review-lor-instrument.md` | `c90b0231a147` | 3 |
| `ndep` | (e) | MAJOR-5 | PRESENT | `v14/review-ndep-instrument.md` | `1133b154ff8d` | 7 |
| `occ` | (e) | MAJOR-1 | PRESENT | `v14/review-occ-instrument.md` | `49e66c63db89` | 4 |
| `perl` | (e) | MAJOR-9 | PRESENT | `v14/review-perl-instrument.md` | `a624d1a5211a` | 4 |
| `perr` | (e) | MAJOR-1 | PRESENT | `v14/review-perr-instrument.md` | `802071ab4c91` | 4 |
| `pot` | (e) | MAJOR-5 | PRESENT | `v14/review-pot-instrument.md` | `6ffa7681fb94` | 1 |
| `r1` | (e) | M3 | PRESENT | `v14/review-r1-instrument.md` | `d3685698da65` | 3 |
| `r2` | (e) | M2 | PRESENT | `v14/review-r2-instrument.md` | `7eabff507110` | 3 |
| `r4` | (e) | F6 | PRESENT | `v14/review-r4-instrument.md` | `7fa287a04367` | 3 |
| `r4c` | (e) | MAJOR-2 | PRESENT | `v14/review-r4c-instrument.md` | `73dd15300ea8` | 3 |
| `r4dec` | (e) | MAJOR-2 | PRESENT | `v14/review-r4dec-instrument.md` | `5490807d2796` | 9 |
| `r5m` | (e) | M5 | PRESENT | `v14/review-r5m-instrument.md` | `0890efbf3071` | 2 |
| `r6bp` | (e) | M5 | PRESENT | `v14/review-r6bp-instrument.md` | `05f6032bbc86` | 4 |
| `sec` | (e) | MAJOR-1 | PRESENT | `v14/review-sec-instrument.md` | `d872435e6064` | 2 |
| `sec2` | (e) | MAJOR-3 | PRESENT | `v14/review-sec2-instrument.md` | `5724179ec187` | 6 |
| `sig` | (e) | MAJOR-3 | PRESENT | `v14/review-sig-instrument.md` | `6d0b7e73279a` | 2 |
| `smu` | (e) | MAJOR-1 | PRESENT | `v14/review-smu-instrument.md` | `dd11bd925adc` | 3 |
| `w2` | (e) | MAJOR-5 | PRESENT | `v14/review-w2-instrument.md` | `e83855bd5e74` | 2 |
| `gmain` | (e) | M5 | PRESENT | `v14/review-gmain-instrument.md` | `0721475b1709` | 2 |
| `aid` | (f) | MAJOR-1 | PRESENT | `v14/review-aid-instrument.md` | `b333a08ba565` | 1 |
| `coup` | (f) | MAJOR-3 | PRESENT | `v14/review-coup-instrument.md` | `8e71c5df2b8e` | 2 |
| `cra` | (f) | MAJOR-2 | PRESENT | `v14/review-cra-instrument.md` | `64235eac24b9` | 3 |
| `epr` | (f) | MINOR-7 | PRESENT | `v14/review-epr-instrument.md` | `30950725b61a` | 2 |
| `fac` | (f) | MAJOR-2 | PRESENT | `v14/review-fac-instrument.md` | `b328a819d752` | 4 |
| `gdl` | (f) | MAJOR-5 | PRESENT | `v14/review-gdl-instrument.md` | `1565d161354f` | 3 |
| `lor` | (f) | MAJOR-6 | PRESENT | `v14/review-lor-instrument.md` | `c90b0231a147` | 5 |
| `ndep` | (f) | MAJOR-7 | PRESENT | `v14/review-ndep-instrument.md` | `1133b154ff8d` | 6 |
| `occ` | (f) | MAJOR-4 | PRESENT | `v14/review-occ-instrument.md` | `49e66c63db89` | 3 |
| `perl` | (f) | MAJOR-5 | PRESENT | `v14/review-perl-instrument.md` | `a624d1a5211a` | 3 |
| `perr` | (f) | MAJOR-2 | PRESENT | `v14/review-perr-instrument.md` | `802071ab4c91` | 3 |
| `pot` | (f) | MAJOR-2 | PRESENT | `v14/review-pot-instrument.md` | `6ffa7681fb94` | 1 |
| `r1` | (f) | M5 | PRESENT | `v14/review-r1-instrument.md` | `d3685698da65` | 3 |
| `r5m` | (f) | M3 | PRESENT | `v14/review-r5m-instrument.md` | `0890efbf3071` | 3 |
| `r6a` | (f) | M7 | PRESENT | `v14/review-r6a-instrument.md` | `8d05097f3d0f` | 6 |
| `sec2` | (f) | MAJOR-12 | PRESENT | `v14/review-sec2-instrument.md` | `5724179ec187` | 3 |
| `sig` | (f) | MAJOR-4 | PRESENT | `v14/review-sig-instrument.md` | `6d0b7e73279a` | 2 |
| `smu` | (f) | MINOR-5 | PRESENT | `v14/review-smu-instrument.md` | `dd11bd925adc` | 2 |
| `spc` | (f) | MAJOR-2 | PRESENT | `v14/review-spc-instrument.md` | `c18b16c76992` | 4 |
| `act` | (g) | MAJOR-5 | PRESENT | `v14/review-act-instrument.md` | `49045aa82b90` | 6 |
| `cra` | (g) | MAJOR-1 | PRESENT | `v14/review-cra-instrument.md` | `64235eac24b9` | 5 |
| `epr` | (g) | MINOR-5 | PRESENT | `v14/review-epr-instrument.md` | `30950725b61a` | 2 |
| `gdl` | (g) | MAJOR-4 | PRESENT | `v14/review-gdl-instrument.md` | `1565d161354f` | 3 |
| `gmain` | (g) | D7 | PRESENT | `v14/review-gmain-instrument.md` | `0721475b1709` | 2 |
| `lor` | (g) | MAJOR-3 | PRESENT | `v14/review-lor-instrument.md` | `c90b0231a147` | 1 |
| `ndep` | (g) | m5 | PRESENT | `v14/review-ndep-instrument.md` | `1133b154ff8d` | 1 |
| `perl` | (g) | MAJOR-6 | PRESENT | `v14/review-perl-instrument.md` | `a624d1a5211a` | 3 |
| `perr` | (g) | MAJOR-5 | PRESENT | `v14/review-perr-instrument.md` | `802071ab4c91` | 3 |
| `pot` | (g) | MAJOR-3 | PRESENT | `v14/review-pot-instrument.md` | `6ffa7681fb94` | 1 |
| `r1` | (g) | M6 | PRESENT | `v14/review-r1-instrument.md` | `d3685698da65` | 2 |
| `r3` | (g) | M5 | PRESENT | `v14/review-r3-instrument.md` | `cae0f52610d8` | 6 |
| `r4` | (g) | F4 | PRESENT | `v14/review-r4-instrument.md` | `7fa287a04367` | 6 |
| `r4c` | (g) | MINOR-4 | PRESENT | `v14/review-r4c-instrument.md` | `73dd15300ea8` | 1 |
| `r4dec` | (g) | MAJOR-3 | PRESENT | `v14/review-r4dec-instrument.md` | `5490807d2796` | 5 |
| `r5m` | (g) | m2 | PRESENT | `v14/review-r5m-instrument.md` | `0890efbf3071` | 1 |
| `r6a` | (g) | M2 | PRESENT | `v14/review-r6a-instrument.md` | `8d05097f3d0f` | 4 |
| `r6bp` | (g) | M7 | PRESENT | `v14/review-r6bp-instrument.md` | `05f6032bbc86` | 3 |
| `sec` | (g) | Head literals are typed | PRESENT | `v14/review-sec-instrument.md` | `d872435e6064` | 1 |
| `sec2` | (g) | MAJOR-13 | PRESENT | `v14/review-sec2-instrument.md` | `5724179ec187` | 3 |
| `smu` | (g) | MINOR-2 | PRESENT | `v14/review-smu-instrument.md` | `dd11bd925adc` | 1 |
| `u4b` | (g) | MAJOR-5 | PRESENT | `v14/review-u4b-instrument.md` | `ebcfbb49fa88` | 2 |
| `aid` | (h) | MAJOR-4 | PRESENT | `v14/review-aid-instrument.md` | `b333a08ba565` | 1 |
| `coup` | (h) | MAJOR-4 | PRESENT | `v14/review-coup-instrument.md` | `8e71c5df2b8e` | 3 |
| `cra` | (h) | MAJOR-1 | PRESENT | `v14/review-cra-instrument.md` | `64235eac24b9` | 5 |
| `epr` | (h) | MAJOR-4 | PRESENT | `v14/review-epr-instrument.md` | `30950725b61a` | 5 |
| `gdl` | (h) | MAJOR-3 | PRESENT | `v14/review-gdl-instrument.md` | `1565d161354f` | 5 |
| `giter` | (h) | MAJOR-5 | PRESENT | `v14/review-giter-instrument.md` | `c4e0e08050e7` | 1 |
| `gmain` | (h) | M2 | PRESENT | `v14/review-gmain-instrument.md` | `0721475b1709` | 2 |
| `gprep` | (h) | MAJOR-6 | PRESENT | `v14/review-gprep-instrument.md` | `aa9b0362fbed` | 2 |
| `ndep` | (h) | MAJOR-10 | PRESENT | `v14/review-ndep-instrument.md` | `1133b154ff8d` | 3 |
| `perl` | (h) | MAJOR-4 | PRESENT | `v14/review-perl-instrument.md` | `a624d1a5211a` | 4 |
| `pot` | (h) | MUT-MUSTNOT | PRESENT | `v14/review-pot-instrument.md` | `6ffa7681fb94` | 2 |
| `r1` | (h) | M4 | PRESENT | `v14/review-r1-instrument.md` | `d3685698da65` | 4 |
| `r2` | (h) | M6 | PRESENT | `v14/review-r2-instrument.md` | `7eabff507110` | 3 |
| `r3` | (h) | M6 | PRESENT | `v14/review-r3-instrument.md` | `cae0f52610d8` | 4 |
| `r3w` | (h) | M3 | PRESENT | `v14/review-r3w-instrument.md` | `f04d46009228` | 3 |
| `r4` | (h) | F13 | PRESENT | `v14/review-r4-instrument.md` | `7fa287a04367` | 3 |
| `r4dec` | (h) | MAJOR-4 | PRESENT | `v14/review-r4dec-instrument.md` | `5490807d2796` | 6 |
| `r5` | (h) | MAJOR-4 | PRESENT | `v14/review-r5-instrument.md` | `f15f4136446e` | 4 |
| `r5m` | (h) | M4 | PRESENT | `v14/review-r5m-instrument.md` | `0890efbf3071` | 1 |
| `r6a` | (h) | M3 | PRESENT | `v14/review-r6a-instrument.md` | `8d05097f3d0f` | 6 |
| `r6bp` | (h) | M4 | PRESENT | `v14/review-r6bp-instrument.md` | `05f6032bbc86` | 3 |
| `sec` | (h) | MAJOR-6 | PRESENT | `v14/review-sec-instrument.md` | `d872435e6064` | 4 |
| `sec2` | (h) | MAJOR-7 | PRESENT | `v14/review-sec2-instrument.md` | `5724179ec187` | 5 |
| `sig` | (h) | MAJOR-1 | PRESENT | `v14/review-sig-instrument.md` | `6d0b7e73279a` | 2 |
| `smu` | (h) | MAJOR-4 | PRESENT | `v14/review-smu-instrument.md` | `dd11bd925adc` | 3 |
| `u4b` | (h) | m4 | PRESENT | `v14/review-u4b-instrument.md` | `ebcfbb49fa88` | 1 |
| `spc` | (h) | MAJOR-1 | ABSENT | `v14/review-spc-instrument.md` | `c18b16c76992` | 5 |
| `coup` | (i) | MINOR-3 | PRESENT | `v14/review-coup-instrument.md` | `8e71c5df2b8e` | 1 |
| `cra` | (i) | MINOR-2 | PRESENT | `v14/review-cra-instrument.md` | `64235eac24b9` | 2 |
| `gmain` | (i) | D1 | PRESENT | `v14/review-gmain-instrument.md` | `0721475b1709` | 2 |
| `gprep` | (i) | MAJOR-3 | PRESENT | `v14/review-gprep-instrument.md` | `aa9b0362fbed` | 2 |
| `lor` | (i) | MAJOR-4 | PRESENT | `v14/review-lor-instrument.md` | `c90b0231a147` | 2 |
| `perl` | (i) | MINOR-13 | PRESENT | `v14/review-perl-instrument.md` | `a624d1a5211a` | 1 |
| `perr` | (i) | MAJOR-4 | PRESENT | `v14/review-perr-instrument.md` | `802071ab4c91` | 3 |
| `r3` | (i) | M1 | PRESENT | `v14/review-r3-instrument.md` | `cae0f52610d8` | 7 |
| `r4` | (i) | F7 | PRESENT | `v14/review-r4-instrument.md` | `7fa287a04367` | 2 |
| `r4b` | (i) | MAJOR-4 | PRESENT | `v14/review-r4b-instrument.md` | `29c75e73ede9` | 5 |
| `r4c` | (i) | MINOR-6 | PRESENT | `v14/review-r4c-instrument.md` | `73dd15300ea8` | 2 |
| `r4dec` | (i) | MINOR-1 | PRESENT | `v14/review-r4dec-instrument.md` | `5490807d2796` | 4 |
| `r6bp` | (i) | M1 | PRESENT | `v14/review-r6bp-instrument.md` | `05f6032bbc86` | 5 |
| `sec` | (i) | MAJOR-3 | PRESENT | `v14/review-sec-instrument.md` | `d872435e6064` | 2 |
| `sec2` | (i) | MAJOR-2 | PRESENT | `v14/review-sec2-instrument.md` | `5724179ec187` | 5 |
| `sig` | (i) | MAJOR-7 | PRESENT | `v14/review-sig-instrument.md` | `6d0b7e73279a` | 2 |
| `u4b` | (i) | m6 | PRESENT | `v14/review-u4b-instrument.md` | `ebcfbb49fa88` | 2 |
| `w2` | (i) | MAJOR-2 | PRESENT | `v14/review-w2-instrument.md` | `e83855bd5e74` | 2 |
| `epr` | (i) | MAJOR-5 | ABSENT | `v14/review-epr-instrument.md` | `30950725b61a` | 3 |

## 8. Method, and what this census cannot say

- Every instrument was copied once into a scratch mirror and probed there; 79 distinct repository paths were read and 2 written (this document and the receipt).  The read set was recorded at an `open` audit hook and gated order-insensitively at the last gate.
- The spec `v14/TEMPLATE.md` states 12 counts about this census; each is read back out of that document and compared with the live registry at `G-TEMPLATE-COUNTS-BOUND`, so neither document can drift from the other.
- The probes are STATIC.  They cannot see a gate that exists and does not bind, and they cannot see a corruption that survives.  Where a panel spoke, the panel is authority.
- The probes are also uniform, which is their whole value: they cover the 3 instruments with no panel, and they see HEAD rather than the sha the seat reviewed.
- No verdict here reopens a seal.  Every unit named is terminal; this census is a map of the shared perimeter, not a re-adjudication of any unit's physics.  **No measured physical quantity of any unit is in question anywhere in this document** — every K3 seat cited here recorded that no measured quantity was wrong.

---

*Rendered from `v14/code/tpl_census_receipt.json`.  Reference implementations `v14/code/era_template.py` (`d04a3eb58fbc`); pin `v14/note-tpl-pin.md` (`38aae39ca5f3`); census instrument `v14/code/tpl_census.py` (`2e893b77c733`).  Instruments censused at the committed working tree at the census run.*
