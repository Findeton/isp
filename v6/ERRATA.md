# v6 ERRATA / SUPERSESSION LEDGER

Created 2026-07-19 (D46h/N5 housekeeping batch; audit verdict A5, LOG #379).
All entries are additive; no frozen v6 text has been modified in place.

## E1 — The Renou-retirement sweep (executed; the caveat in ARCHIVE-STATUS.md discharged)

The 2026-06-16 retirement (v7 paper 16,
`../v7/relativistic-isp-v7-paper16-seal-indivisibility-bridge-real-quantum-reopening.md`)
retired the "Renou et al. ruled out real QM / three experiment-fixed inputs"
overclaim in favour of "three record-blind inputs of distinct epistemic
status" (the complex-over-real / tensor-product bit is a CONTESTED
composition-rule / local-tomography convention, possibly experimentally
unfixable). `ARCHIVE-STATUS.md` recorded at freeze time that v6 was never
swept. This entry records the sweep, now executed.

**Sweep method:** recursive grep of `v6/` (all files, including
`publishable/` and its `tex/` and `reviews/` subtrees) for: `Renou`
(case-insensitive), `ruled out real`, `real quantum` / `real QM` /
`real-valued quantum` / `real numbers`, `experiment-fixed` /
`experimentally fixed` / `experiment fixes`, `three ... inputs`,
`complex-over-real`, `Chen`+`Li` / `040403`, `Nature 600` / `625 (2021)`,
and the Renou-2021 co-author surnames (Trillo, Weilenmann, Tavakoli,
Navascués in the Renou-2021 context).

**Finding: ZERO Renou citations in any v6 paper.** The only occurrence of
"Renou" anywhere under `v6/` is `ARCHIVE-STATUS.md` itself (the freeze-time
caveat). No v6 file asserts "Renou ruled out real QM" or the "three
experiment-fixed inputs" framing by name or by reference.

**Near-miss loci examined and classified NOT substantive (no in-file
erratum blocks warranted):**

- `publishable/companion-B-almost-quantum.md` (line ~308): mentions "local
  tomography `K_AB = K_A·K_B` (the complex-over-real selector)" only as an
  input the seal is provably BLIND to, and its Non-claims section explicitly
  disclaims deriving complex quantum theory / local tomography / the tensor
  product. This is consistent with (indeed anticipates) the corrected
  post-retirement framing; it does not depend on the retired Renou claim.
  Its Navascués citations are NPA/almost-quantum references, not Renou 2021.
- `relativistic-isp-v6-paper28.md` (line ~60): "REAL quantum hardware" refers
  to the Google 2023 surface-code dataset — unrelated to real-vs-complex QM.

**Consequence:** no substantive (results-level) Renou dependence exists in
v6; hence no per-file erratum blocks are appended. Should any v6 line later
be found to assert the retired framing in other words, it is stale per the
retirement record above; citations of Renou et al. 2021 anywhere in the
corpus are historical (Renou 2021 stands in its own framing; the debate is
live and the corpus takes no side).

## E2 — The quarter law's `BC` is only the Cauchy-Schwarz bound (paper 7 §12's correction routed to paper 26)

Filed live and unrouted at `../v10/LOG.md:11472` — *"LIVE ERRATUM FILED: the
quarter law's BC is only the Cauchy-Schwarz bound (saturated iff relative
pointer phase constant) — v6 paper 7 §12's correction never reached paper 26,
ARCHIVE-STATUS, or v10 paper 18."* — and carried at
`../v10/THE-THEORY-SO-FAR.md:11932` as *"LIVE ERRATUM, filed and unrouted."*
This entry routes it. It moves the theorem's **hypothesis**, not its leading
coefficient.

**The correction, verbatim from its committed source** —
`relativistic-isp-v6-paper7.md` §12 ("Predictions and experimental contact
(corrected)", line 1157), item B1 — the item runs lines 1178-1193 (1194-1195
are item B2); the passage quoted here is lines 1178-1188 *(range corrected
2026-07-27, v11 H1 hostile round; first written as 1178-1195)*:

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

**Affected frozen locus (no in-file text modified):**
`relativistic-isp-v6-paper26.md` — the quarter law at lines 15-17 (abstract),
61-62 (*"coherence multiplier = Bhattacharyya overlap"*), and Theorem A at
lines 222-238. The load-bearing step is lines 233-235 *(corrected 2026-07-27,
v11 H1 hostile round; first written as 232-235 — line 232 is blank)*: *"The record imprint
sends rho_01 -> <e_1|e_0> rho_01 with |e_chi> = sum_b sqrt(P_chi(b)) |b>, so
the per-cycle multiplier is exactly BC."* The phase-free pointer
`|e_chi> = sum_b sqrt(P_chi(b))|b>` **is** the (strictly stronger) phase-free
case of paper 7 §12 B1's constant-relative-phase hypothesis; for
phase-structured pointers the multiplier's modulus is strictly below `BC`
**whenever the relative pointer phase is non-constant**, and `BC` is the
Cauchy-Schwarz bound on it. *(Both clauses tightened 2026-07-27, v11 H1
hostile round, fix m4: the first delivery wrote "strictly below `BC`"
unqualified — false at constant non-zero relative phase, where the modulus
saturates — and identified the phase-free pointer *with* B1's hypothesis
rather than as a special case of it.)* Paper 26's `-ln BC = sigma/4 + (eps^2/6) sigma + O(sigma^3)` and
its receipt table stand as stated **under that hypothesis**.

**Paper 7 carries the correction in-file** and is cited here as the source,
not as an affected locus.

**The forward statement, committed:**
`../v8/relativistic-isp-v8-paper6-phenomenology.md` §1.2 (line 32):

> the seal overlap **is** a genuine discrete (Gell-Mann–Hartle/Feynman–Vernon)
> influence functional `F = ⟨e₁|e₀⟩ = Σ_b √(P₀(b)P₁(b))·e^{iΔθ(b)}`, whose
> **modulus is the Bhattacharyya kernel** — `|F| = BC` exactly when the
> recorded phases align, `|F| ≤ BC` in general (recorded phases only *add*
> dephasing)

(receipt `pPRIN_seal_record.py`). The v8 line therefore already carries the
corrected form; the frozen v6 reader path lacked the pointer, which this entry
supplies.

**Routing:** this entry (v6 paper 26); an appended erratum in
`../v10/relativistic-isp-v10-paper18-no-silent-erasure-and-the-identified-click-law.md`
(§2's quarter-law clause); recorded at `../v8/LEDGER.md` #498 (the v8 ledger's
own numbering, distinct from the v10 numbering in `../v10/LOG.md`).
