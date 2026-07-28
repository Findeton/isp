# v11 H1 — ERRATUM ROUTING (unit note)

**Status:** DONE, 2026-07-27.  Binding pin:
`note-h1-erratum-routing-pin.md`.  Specification: paper 0 §6.7 (the
unrouted-erratum duty) + `note-v11p0a-reproduction-catalog.md` §0.3
(the errata census) under §0.4's correction-spine doctrine (v1–v7
frozen; corrections land in v8/LEDGER.md and forward).

A documentation unit.  **No new claims, no new mathematics.**  Every
routed line quotes its correction verbatim from a committed source and
cites that source by file and line.  Frozen papers are not edited; the
routing lands in the archive-status/errata layer, in the two live-era
v10 files that carry the affected passages, and in `v8/LEDGER.md`.

---

## 1. THE `BC` / CAUCHY–SCHWARZ ERRATUM — ROUTED

**The correction, and its committed source.**
`v6/relativistic-isp-v6-paper7.md` §12 ("Predictions and experimental
contact (corrected)", line 1157), item B1, **lines 1178–1195**:

> B1. Duality law, CORRECTED. Cauchy-Schwarz gives |<phi0|phi1>| <= B =
>     sum sqrt(p0 p1), with equality iff the relative pointer phase is
>     constant. Phase-structured pointers with IDENTICAL densities give
>        alpha = 0: V_QM = 1.000000, B = 1.000000
>        alpha = 1: V_QM = 0.726149, B = 1.000000
>        alpha = 3: V_QM = 0.056135, B = 1.000000
>     (5000-trial Cauchy-Schwarz check: 0 violations). A classical-record
>     (Bhattacharyya) clock is FALSIFIED by phase-structured which-path
>     marking; SHARD, through its own dilation, carries pointer holonomy and
>     uses the dilation overlap - coinciding with QM everywhere at this
>     layer.

**Its filed-but-unrouted status, quoted.**
`v10/LOG.md:11472` — *"LIVE ERRATUM FILED: the quarter law's BC is only
the Cauchy-Schwarz bound (saturated iff relative pointer phase constant)
— v6 paper 7 §12's correction never reached paper 26, ARCHIVE-STATUS, or
v10 paper 18."*  Carried at `v10/THE-THEORY-SO-FAR.md:11932` as *"LIVE
ERRATUM, filed and unrouted."*

**Its silent forward discharge, quoted.**
`v8/relativistic-isp-v8-paper6-phenomenology.md` §1.2 (**line 32**):

> the seal overlap **is** a genuine discrete (Gell-Mann–Hartle/Feynman–Vernon)
> influence functional `F = ⟨e₁|e₀⟩ = Σ_b √(P₀(b)P₁(b))·e^{iΔθ(b)}`, whose
> **modulus is the Bhattacharyya kernel** — `|F| = BC` exactly when the
> recorded phases align, `|F| ≤ BC` in general (recorded phases only *add*
> dephasing)

(receipt `pPRIN_seal_record.py`).  The corrected form is therefore
already in the live corpus; only the reader paths lacked the pointer.

**The affected frozen locus, located precisely.**
`v6/relativistic-isp-v6-paper26.md`: the quarter law at lines 15–17
(abstract), 61–62 (*"coherence multiplier = Bhattacharyya overlap"*),
and Theorem A at lines 222–238.  The load-bearing step is lines
232–235: *"The record imprint sends rho_01 -> <e_1|e_0> rho_01 with
|e_chi> = sum_b sqrt(P_chi(b)) |b>, so the per-cycle multiplier is
exactly BC."*  The phase-free pointer `|e_chi> = sum_b
sqrt(P_chi(b))|b>` **is** paper 7 §12 B1's constant-relative-phase
hypothesis.  Paper 7 itself carries the correction in-file and is cited
as the source, not as an affected locus.

### Routing destinations

| destination | what was added |
|---|---|
| `v6/ERRATA.md` — new entry **E2** (59 lines) | The correction quoted verbatim with its file/line; the affected paper-26 loci enumerated; the v8 §1.2 forward statement quoted; the routing table. |
| `v6/ARCHIVE-STATUS.md` — one caveat line (4 lines) | Added to the freeze-time caveat list, pointing at `ERRATA.md` E2. |
| `v10/relativistic-isp-v10-paper18-…-click-law.md` — appended `## Erratum (2026-07-27, v11 H1 — erratum routing)` (35 lines) | Forward-only, per the v10 convention already used by paper 30's `## Erratum (2026-07-19, D46h/N5)`. Original §2 text unmodified. |
| `v8/LEDGER.md` — entry **#498**, part (a) | The corrections-and-supersessions log. |

**Lines as added — `v6/ARCHIVE-STATUS.md`:**

> - paper26's Theorem A holds under a hypothesis it does not state: the coherence multiplier is
>   `BC` only when the relative pointer phase is constant across the record alphabet, `BC` being
>   the Cauchy-Schwarz bound in general (paper 7 §12 item B1, "Duality law, CORRECTED"). Routed
>   in `ERRATA.md` E2; `../v8/LEDGER.md` #498.

**Scope carried into v10 paper 18's erratum (quoting nothing beyond the
corpus's own statements):** the reception metric is `−ln|F| ≥ −ln BC`,
so the quarter law is a lower bound on sealing at fixed evidence unless
the recorded pointer phases align; the phase face of `F` leaves `|ρ₀₁|`
untouched (the paper's own §8 and v8 paper 6 §3), so **no clause of the
principle, the falsifier, or the identification changes**.

---

## 2. THE v4 EFFECTIVE-GR DESCENT — ERRATA'D

**The claim, and its frozen loci.**
`v4/relativistic-isp-v4-paper25-finite-descent-reconstruction-of-effective-gr.md`
(the Einstein/Feynman descent; `[{\mathcal A}]=0` ⟺ `GR-DYN-COFINAL-PASS`,
line 6021) and
`v4/relativistic-isp-v4-paper32-formal-hardening-of-effective-gr-descent.md`
§8, lines 964–975.  `v4/ERRATA.md` carried **no GR entry** (E1 is
Yang–Mills) — the catalog's *"one unrouted supersession in the gravity
sector"* ([V11-CAT] §2.9).

**The committed later corrections, all located and quoted** — no fix was
invented, and nothing is marked `[DISPUTED-UNROUTED]`:

1. `v6/relativistic-isp-v6-paper5-born-and-gr-verdict.md` §8, **lines
   456–459** (four-attack campaign, receipt
   `code/v6_p5b_gr_derivation_falsification_campaign.py`; the §8 table's
   verdict row, **line 439**, reads `FULL-GR-FALSIFIED-FROM-CURRENT-DATA`):

   > SHARD has operative finite record gravity.
   > SHARD does not currently derive full 3+1 GR.
   > Full GR is falsified as a theorem from the current SHARD screen/source data
   > alone.

2. `v6/relativistic-isp-v6-paper57-gravity-from-sealed-records.md`,
   **line 9**: *"**SHARD derives gravity's equation of state but provably
   not its scale.**"* — with the unified no-go: *"SHARD cannot fix the
   single absolute scale `σ_A` … and this is one unified no-go theorem,
   not a list of failures."*

3. `v8/relativistic-isp-v8-paper4-gravity-continuum.md`, **line 9**:
   *"the continuum is buildable up to `l_step` given manifoldlikeness;
   the conformal direction is owned; Λ's scaling is owned and its
   magnitude provably needs one structurally-resisted import; and the
   covariance frontier is reduced to one named hinge plus one shared
   wall."*

**What survives, quoted from the frozen paper itself** — paper 32 lines
973–975: *"This is the hardened GR claim.  Effective GR is not assumed
as the ontology.  It is the unique no-anomaly finite coincidence
geometry of the active ISP corpus."*  And the limit v4 already states
in-file — `…-paper6-dynamical-geometry-configuration-gate.md` lines
39–44: *"The same metric detector and fixed-background curvature data
are compatible with many inequivalent geometry-update kernels … Therefore
Papers 1-5 do not determine Einstein dynamics, constraint propagation,
or a gravitational action."*

### Routing destinations

| destination | what was added |
|---|---|
| `v4/ERRATA.md` — new entry **E2** (60 lines) | Affected files; the surviving scope clauses quoted; the three committed later corrections quoted with file/line; the consequence for readers. |
| `v8/LEDGER.md` — entry **#498**, part (b) | The corrections-and-supersessions log. |

No v4 status file other than `ERRATA.md` exists, and `ERRATA.md`'s own
preamble (*"All entries are additive; no frozen v4 text has been modified
in place"*) is the layer the pin specifies — no new status note was
needed.

---

## 3. THE `119 → 137` CORRECTION — PARTIALLY ROUTED; COMPLETED HERE

**Already routed, and where:**

- `v10/LOG.md:10501` — *"CORPUS-WIDE: D49/B2's published 119 becomes 137
  — a port check reproduces 119 exactly because porting the method ports
  the error; a port check cannot be an independence check."*
- `v10/THE-THEORY-SO-FAR.md`, **lines 7464–7469** — the corpus-wide
  number correction with its lesson, closing *"Every quotation of 119 in
  this book is corrected."*

**Not routed, and where the gap was:** that sweep is scoped to
THE-THEORY-SO-FAR (*"in this book"*).  `v10/LOG.md` and
`v8/LEDGER.md` carry no per-file pointer, and
`v10/note-d49-completion-dichotomy-settlement-result.md` still printed
`119` at two loci with no pointer — **line 44** (the round-1 B2 binding
note, *"bisimulation-invariance leaves **119** (§4b)"*) and **line 302**
(*"new gate H1 measures 308/313 and 119/313 free directions"*).  No
committed v10 *paper* quotes the number.

**Routed by the same pattern:** an appended `## Erratum (2026-07-27, v11
H1 — erratum routing)` in the D49 result note (live-era, forward-only,
original text unmodified) quoting the THE-THEORY-SO-FAR correction and
instructing **137/313 for 119/313** at both loci; `308/313` unaffected;
the headline strengthens (more freedom than published).  Recorded at
`v8/LEDGER.md` #498, part (c).

---

## 4. THE `1.82` DOWNGRADE — NO NEW ROUTING OWED

Per the pin's scope clause, checked for an unpointed reader path.  The
number's live home is `v7/relativistic-isp-v7-paper30-rooted-boundary-law.md:2833`
(`max dual-conjugation error = 1.8210207227600682556870097725525`) — a
**frozen v7 file**, and the downgrade is already carried at
`v10/note-d72-weld-result.md` §5(a) and `v10/THE-THEORY-SO-FAR.md` §0.3
/ §B2.12, and in [V11-CAT] §§4.6–4.7 as a graded entry.  No v8/v10/v11
paper quotes `1.82` as evidence.  The one remaining reader path is the
frozen v7 paper itself; `v7/` has an `ARCHIVE-STATUS.md` but no
`ERRATA.md`, and creating a v7 errata layer is a larger decision than
this unit's remit.  **Recorded as the one carried residual, not routed.**

## 5. WHAT COULD NOT BE LOCATED

Nothing.  Every correction routed here has a committed source, quoted
with file and line.  No `[DISPUTED-UNROUTED]` line was needed.

One numbering trap found and avoided, recorded because the next
housekeeping unit will hit it.  `v8/LEDGER.md`'s corrections log is **not
contiguous in the file**: entries 1–139 run at lines 35–245, then the
Phase-0/Orphans/Phase-1 sections intervene, and entries **140–171 plus
264** resume at lines 310–376.  The ledger numbering is shared with
`v10/LOG.md`, which runs to **#497** and is closed there (`v11/LOG.md:6`;
`v10/THE-THEORY-SO-FAR.md:15` stamps *"as of **LEDGER #495**
(v10/LOG.md) / **#130** (v8/LEDGER.md)"*).  A first draft of this unit's
entry was numbered 140 — a collision with the committed D32A entry at
line 310 — and was renumbered.  **The entry is `v8/LEDGER.md` #498**,
appended at the file's end, and every pointer added by this unit is
file-qualified.

---

## 6. FROZEN-FILES RECEIPT

`git diff --stat`, run in `/Users/felixrobles/workspace/isp` after all
edits (no commit):

```text
 v10/note-d49-completion-dichotomy-settlement-result.md                             | 20 +++++++++++++++++
 v10/relativistic-isp-v10-paper18-no-silent-erasure-and-the-identified-click-law.md | 35 +++++++++++++++++++++++++++++
 v4/ERRATA.md                                                                       | 60 ++++++++++++++++++++++++++++++++++++++++++++++++++
 v6/ARCHIVE-STATUS.md                                                               |  4 ++++
 v6/ERRATA.md                                                                       | 59 +++++++++++++++++++++++++++++++++++++++++++++++++
 v8/LEDGER.md                                                                       |  2 ++
 6 files changed, 180 insertions(+)
```

**Verdict: GATE PASSED.**  Six files changed, 180 insertions, **zero
deletions** — no existing line anywhere was rewritten.  By layer:

- **status/errata layer:** `v4/ERRATA.md`, `v6/ERRATA.md`,
  `v6/ARCHIVE-STATUS.md`;
- **live-era v10:** `v10/relativistic-isp-v10-paper18-…-click-law.md`
  (appended erratum only), `v10/note-d49-…-result.md` (appended erratum
  only);
- **correction spine:** `v8/LEDGER.md` (one entry, #498, appended at the
  file's end).

**No frozen paper appears in the diff.**  No file under `v1/`–`v3/`,
`v5/`, `v7/`, or `v9/` is touched; under `v4/` and `v6/` only the errata
/ archive-status layer is touched, never a paper.  `v11/` files are the
unit's own note (this file).  Untracked at receipt time:
`v11/note-L0-scale-no-go-lemma.md`, `v11/note-L1-lorentz-no-go-lemma.md`,
`v11/code/` — the parallel units' deliverables, not this unit's.
