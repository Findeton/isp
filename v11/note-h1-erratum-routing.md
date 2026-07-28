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
contact (corrected)", line 1157), item B1 — the item runs **lines 1178–1193**
(1194–1195 are item B2); the passage quoted below is **lines 1178–1188**
*(range corrected 2026-07-27, hostile-round fix m1; the first delivery wrote
1178–1195 for both)*:

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
**233–235** *(corrected 2026-07-27, hostile-round fix m2; the first delivery
wrote 232–235 — line 232 is blank)*: *"The record imprint sends rho_01 -> <e_1|e_0> rho_01 with
|e_chi> = sum_b sqrt(P_chi(b)) |b>, so the per-cycle multiplier is
exactly BC."*  The phase-free pointer `|e_chi> = sum_b
sqrt(P_chi(b))|b>` **is the (strictly stronger) phase-free case of** paper 7
§12 B1's constant-relative-phase hypothesis *(so amended 2026-07-27,
hostile-round fix m4; the first delivery wrote "**is** B1's hypothesis",
conflating a special case with the hypothesis itself — and the corresponding
"strictly below `BC`" clause in `v6/ERRATA.md` E2 now carries its "whenever
the relative pointer phase is non-constant" qualifier, since a constant
non-zero relative phase still saturates)*.  Paper 7 itself carries the
correction in-file and is cited as the source, not as an affected locus.

### Routing destinations

| destination | what was added |
|---|---|
| `v6/ERRATA.md` — new entry **E2** (59 lines) | The correction quoted verbatim with its file/line; the affected paper-26 loci enumerated; the v8 §1.2 forward statement quoted; the routing table. |
| `v6/ARCHIVE-STATUS.md` — one caveat line (4 lines) | Added to the freeze-time caveat list, pointing at `ERRATA.md` E2. |
| `v10/relativistic-isp-v10-paper18-…-click-law.md` — appended `## Erratum (2026-07-27, v11 H1 — erratum routing)` (35 lines) | Forward-only, per the v10 convention already used by paper 30's `## Erratum (2026-07-19, D46h/N5)`. Original §2 text unmodified. |
| `v8/LEDGER.md` — entry **#498**, part (a) | The corrections-and-supersessions log. |

**Lines as added — `v6/ARCHIVE-STATUS.md`:**

> - paper26's Theorem A carries a restriction it does not flag as one. Its proof writes the
>   phase-free pointer explicitly — `|e_chi> = sum_b sqrt(P_chi(b)) |b>`, line 234 — but never
>   says that writing it *restricts* the theorem: the coherence multiplier is `BC` only when the
>   relative pointer phase is constant across the record alphabet, `BC` being the Cauchy-Schwarz
>   bound in general (paper 7 §12 item B1, "Duality law, CORRECTED"). Per
>   `../v10/THE-THEORY-SO-FAR.md:11937-11938`, the correction *"does not move the theorem's
>   leading coefficient; it moves the theorem's hypothesis"*. Routed in `ERRATA.md` E2;
>   `../v8/LEDGER.md` #498.

*(Wording amended 2026-07-27, hostile-round fix n4.  The first delivery wrote
"holds under a hypothesis it does not state", which reads as though the
phase-free pointer were absent from paper 26's proof.  It is not — the proof
writes it at `v6/relativistic-isp-v6-paper26.md:234`; what the paper omits is
that writing it is a **restriction**.  The replacement wording tracks
`v10/THE-THEORY-SO-FAR.md:11937-11938` instead of asserting a fact about the
paper that is false.)*

**Scope carried into v10 paper 18's erratum (quoting nothing beyond the
corpus's own statements):** the reception metric is `−ln|F| ≥ −ln BC`,
so the quarter law is a lower bound on sealing at fixed evidence unless
the recorded pointer phases align; the phase face of `F` leaves `|ρ₀₁|`
untouched (`v8/relativistic-isp-v8-paper6-phenomenology.md`:50, §3: *"the
phase face of §1.2's influence functional leaves `|ρ₀₁|` untouched"*), so
**no clause of the principle, the falsifier, or the identification
changes**.

*(Amended 2026-07-27, v11 H1 hostile-round fix M2: the first delivery
attributed the phase-face statement to v10 paper 18's own §8. It is not
there — §8 is "Hostile fronts after round 1" — and the attribution has been
deleted from the paper-18 erratum and from this line. The sourced locus is
v8 paper 6 §3 alone.)*

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
the headline strengthens (more freedom than published — the corpus's own
statement of this, now cited in the D49 erratum per hostile-round fix 10, is
`v10/note-d50-form-law-or-choice-result.md:124-128`: *"**The damage is that
the conclusion strengthens.**  The corrected dimensions are *larger*, still
monotone, still far from 0"*).  Recorded at `v8/LEDGER.md` #498, part (c).

**Amended 2026-07-27 (hostile-round fix M1): the sweep was incomplete.**  The
claim above that "no committed v10 *paper* quotes the number" is true, but
`v10/THE-COMPLETION-DICHOTOMY.md` — a live-era v10 book file, not a note —
still printed the full stale row at **line 1132**: *"| bisimulation-invariance
of the completed class transfer at every interior cut | 589 | 194 | **119 of
313** |"*.  **Two** of its numbers are stale, not one: the rank is `176`, not
`194`.  The corrected row is committed at `v10/THE-THEORY-SO-FAR.md:7387`.  An
appended forward-only erratum in the same pattern now routes it there.  The
`119` also survives at three loci in `v10/note-d50-is-the-form-a-law-pin.md`
(§5(c)), which are recorded rather than edited — pins are frozen by convention
once their unit has run.

---

## 4. THE `1.82` DOWNGRADE — ROUTED (amended 2026-07-27, hostile-round fix M3)

Per the pin's scope clause, checked for an unpointed reader path.  The
number's live home is `v7/relativistic-isp-v7-paper30-rooted-boundary-law.md:2833`
(`max dual-conjugation error = 1.8210207227600682556870097725525`) — a
**frozen v7 file**, and the downgrade is already carried at
`v10/note-d72-weld-result.md` §5(a) and `v10/THE-THEORY-SO-FAR.md` §0.3
/ §B2.12, and in [V11-CAT] §§4.6–4.7 as a graded entry.  No v8/v10/v11
paper quotes `1.82` as evidence.  The one remaining reader path is the
frozen v7 paper itself; `v7/` has an `ARCHIVE-STATUS.md` but no
`ERRATA.md`, and creating a v7 errata layer is a larger decision than
this unit's remit.

**Amended 2026-07-27 (hostile-round fix M3): the `1.82` IS now routed.**
Creating a v7 `ERRATA.md` remains out of remit, but `v7/ARCHIVE-STATUS.md`
already exists and already is the v7 caveat layer — the same layer
`v6/ARCHIVE-STATUS.md` provides for v6.  One caveat line was appended there
in exactly the v6 style, pointing at `v7/…-paper30-…:2833`, at
`v10/note-d72-weld-result.md` §5(a) (line 308) for the downgrade, and at
`v8/LEDGER.md` #498.  The first delivery's "no new routing owed" verdict was
wrong on the layer question and is withdrawn.  One sub-finding recorded while
verifying: d72 §5(a) cites the digits as `paper30:2838`; the receipt line is
**2833** (2838 is the *corrected* expression `L_dual = e^{-kE}e^{i\theta O}`).
The caveat line carries that note; d72 itself is not edited.

## 5. WHAT COULD NOT BE LOCATED — AND THE NAMED RESIDUALS

Every correction routed here has a committed source, quoted with file and
line, and no `[DISPUTED-UNROUTED]` line was needed.

**Amended 2026-07-27 (hostile-round fix m5/m7).  The first delivery of this
section read "Nothing."  That claim is WITHDRAWN — it was a claim about the
corpus, not about this unit's sources, and it is false.**  The hostile round
found unpointed reader paths this unit did not route.  They are named here,
verified line by line, and left *unrouted by design*: routing (a) and (b)
would require sweeping frozen papers and, for v5, building a status layer
that does not exist — both beyond this unit's remit.  Recorded so the next
housekeeping unit inherits a list, not a search.

**(a) Unpointed quarter-law citations** (each cites `−ln BC = σ/4` with no
pointer to the Cauchy–Schwarz hypothesis now routed in `v6/ERRATA.md` E2):

- `v6/relativistic-isp-v6-paper10.md:576-581` — *"the quarter law of quantum-processor
  decoherence (-ln BC = sigma/4 + corrections, proved with its correction
  series and measured to four digits)"* (frozen v6 paper; the E2 entry is
  scoped to paper 26 only).
- `v8/relativistic-isp-v8-paper10-experimental-program.md:9` (the echo-floor
  protocol's framing of paper 6 §3's blindness boundary) and `:43` —
  *"Paper 6 §1: `−ln BC = σ/4 + (ε²/6)σ + O(σ³)` is a theorem *within* the
  which-path pair"*.  Live-era v8, so routable; not routed here.
- `v10/note-d22-no-silent-erasure-principle.md:13` — the principle's own
  clause (ii): *"the quarter law −ln BC = σ/4 … is its metric, bridged by the
  [POSITED] seal-is-record postulate"*.  Live-era v10; the same clause is what
  v10 paper 18's appended erratum scopes, but the D22 note itself has no
  pointer.

**(b) The v4 GR compilation loci and their v5 downstream** (the `E2` entry
just added to `v4/ERRATA.md` names papers 25 and 32; these carry the descent
forward and are not named):

- `v4/relativistic-isp-v4-paper36-hardening-summary-and-compilation.md:154`
  (*"## 2. P32 Compilation: Effective GR"*), `:203`
  (*"\hbox{effective GR inside active ISP} &"*), `:599`
  (*"Proof.  P32 gives effective GR closure relative to"*).
- `v5/relativistic-isp-v5-paper0-review-introduction-for-physicists.md:513` —
  *"ISP theorem says that effective GR is the no-anomaly finite-record
  geometry."*
- `v5/relativistic-isp-v5-paper1-finite-record-horizons-black-hole-ontology.md:3054`
  — *"Proof.  Paper 25 established that effective GR is a finite readout and"*.
- **The structural fact behind (b):** `v5/` has **no errata layer and no
  archive-status layer at all** — `ls v5/` returns 21 files, every one a paper
  (plus one `.tex`/`.pdf` pair).  There is nowhere in v5 to append a routed
  correction.  Creating that layer is a decision beyond this unit; it is
  recorded as a residual for a future housekeeping unit.

**(c) The `119` loci in the D50 pin.**
`v10/note-d50-is-the-form-a-law-pin.md` prints the superseded `119` at three
places — `:25` (the B2 measurement table row, *"| bisimulation-invariance of
the completed class-to-class transfer at every interior cut | **119 of 313**
|"*), `:51` (*"(B2's measurement; 119/313 free.)"*), and `:96` (*"B2's two
numbers (308, 119 at depth-4) as a port check"*).  **A pin is frozen by
convention once its unit has run**, so these are recorded rather than edited
or errata'd in place — and the third is doubly instructive, since it is
exactly the port check `THE-THEORY-SO-FAR.md:7464-7469` names as the reason
the error survived.  The corrected value is `137 of 313` (rank `176`, not
`194`) at all three.  The routing this unit *did* perform for the same number
is the appended erratum in `v10/THE-COMPLETION-DICHOTOMY.md` (line 1132's row
— a second stale locus the first delivery missed, found by the hostile round
as fix M1) and in `v10/note-d49-…-result.md`.

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

### 6b. RECEIPT AFTER THE HOSTILE ROUND (2026-07-27)

**The receipt above is the FIRST DELIVERY's and is now superseded on two
counts**: five more files are touched, and the round's fixes are *in-place
amendments*, so the diff is no longer deletion-free. It is retained above as
the record of what the first delivery did. The post-fix `git diff --numstat`
for this unit's files, run in `/Users/felixrobles/workspace/isp` (no commit):

```text
 32   0  v10/THE-COMPLETION-DICHOTOMY.md
  1   1  v10/THE-THEORY-SO-FAR.md
 10   2  v10/note-d49-completion-dichotomy-settlement-result.md
  2   1  v10/relativistic-isp-v10-paper18-…-click-law.md
  n  20  v11/note-h1-erratum-routing.md   ← self-counting; see below
  7   1  v11/note-v11p0a-reproduction-catalog.md
 18   4  v4/ERRATA.md
 10   4  v6/ARCHIVE-STATUS.md
 14   6  v6/ERRATA.md
 12   0  v7/ARCHIVE-STATUS.md
  1   1  v8/LEDGER.md
 11 files changed, 107 + n insertions(+), 40 deletions(-)
```

The insertion count of **this file's own row is left symbolic (`n`)** on
purpose: it counts the lines of this receipt block, so any figure written here
is stale the moment it is written. The ten other rows are exact and stable
(**107 insertions**), and **the deletion column — 40, which is what the gate
turns on — is complete and exact**, this file's 20 included.

**Verdict: GATE STILL PASSED, on the amended criterion.** `git diff
--name-only | grep -E 'v[1-7]/relativistic-isp'` returns **nothing** — **no
v1–v7 paper is modified.** The two corrections to the first receipt's own
claims:

1. **`v7/` IS now touched** — `v7/ARCHIVE-STATUS.md` only, the archive-status
   layer, never a v7 paper (fix M3). The sentence above reading "No file under
   … `v7/` … is touched" describes the first delivery and is superseded here.
2. **40 deletions, all accounted for.** Every deleted line is a line this
   round's fix list names, replaced by a corrected line carrying a dated
   attribution: the `119`/`194` row pointer, the `1178–1195` and `232–235`
   ranges, the false `§8` attribution, the unqualified "strictly below `BC`",
   the mis-attributed `CLOSED_{…}` tokens, the "Nothing" residual claim, the
   "no new routing owed" verdict, the "holds under a hypothesis it does not
   state" wording, and the two quotation repairs. **No committed substance was
   removed without a replacement that states what changed and why.**

By layer, unchanged in kind: status/errata (`v4/ERRATA.md`, `v6/ERRATA.md`,
`v6/ARCHIVE-STATUS.md`, `v7/ARCHIVE-STATUS.md`); live-era v10
(`THE-COMPLETION-DICHOTOMY.md`, `THE-THEORY-SO-FAR.md`, paper 18, the D49
note); correction spine (`v8/LEDGER.md` #498); and two `v11/` notes. Files
belonging to the parallel L0/L1 unit (`v11/note-L0-*`, `v11/note-L1-*`,
`v11/code/L1_L0*`) appear in the repository-wide diff and are **not this
unit's** — untouched here.
