# R1–R6 Residue Campaign — Summary (2026-06-14)

The full-corpus audit reduced SHARD v6 (55 papers) to **six load-bearing open residues**. This campaign
attacked all six, in preference order (leverage × tractability). Per-residue notes are in the linked files.

## The six attacks

| # | Residue | Tractability | Outcome of the attack | Status now |
|---|---------|-------------|-----------------------|-----------|
| **R1** | (C-reg-b) continuum regularity | tractable | **Concrete advance.** Derived the first heat coefficient `a₁=−c″/4+(c′)²/16c` (Liouville transform, verified); verified the window-modulus parametrix structure; **resolved the α∈(1,2) band paper 32 left open** (rate=min(1,α/2) across the full range, and diagnosed the sup-contamination artifact that fooled the earlier attempt); laid the rigorous Duhamel+Besov proof route; float-safety verified vs mp dps-80 (1.4e-13). | **Forward direction essentially closed**; residue reduced to a standard error-bound write-up + the multi-d port. [paper32-R1-advance.md] |
| **R5** | Born reconstruction | tractable | **Concrete advance.** Localized the import exactly: the derived Born exponent **p = q** (the assumed admissible-transport norm) — B3 *is* the import. Identified the real load-bearing axiom: **continuous reversibility** of screen transports, which by **Banach–Lamperti** forces q=2 uniquely (U(n) is the only continuous transitive ℓ_q isometry group). | Reduced from "imports the Hilbert structure" to **one decidable axiom** (do records force continuous/Lie transports?), not settled by p16's process-reversibility. [paper5-R5-advance.md] |
| **R2** | (PR-RP+) / multi-letter Anderson | hard-but-doable | **Clock lane confirmed; residue relocated.** An optimization-based composite-clock search (after correcting 3 metric pitfalls: spectral≠dynamical, validity-depth≫period, trust the direct diagonal) found **no valid clock** — confirming paper 27's validity wall under optimization pressure. | Residue is the **multi-letter Anderson joint-realization** (one cone invariant under all letter maps) — classical positive-systems theory, *not* the clock. [code/v6_r2_README.md] |
| **R6** | p=ε + O35.1 bridge (neutrino) | hard-but-doable | **Audit corrected + residue localized.** The *dressed* prediction `ε_eff=ε(1−ε)` matches **JUNO to 0.05σ** (the audit's "dying at JUNO" was the *bare* point). `p=ε` (marginality) is **derived** from P8's 2nd-order binding defect; the residue is **O35.1**: derive the `(1−ε)` per-rung factor *uniquely* (it is "identified, not derived"). | Live, data-consistent; residue is a **bounded algebraic** obligation, among the more closable. [R6-attack.md] |
| **R4** | gravity: interacting TS-integrability | **clay-hard** | **Barrier characterized.** It IS the open relativistic-collapse-integrability problem (Tumulka's interacting flash *assumes* the microcausal TS evolution; constructing it is open field-wide). SHARD's concrete construction is **branch B** (postulated covariant collapse model, free γ,β); the **Q3 tension** (covariant-localization non-sharpness vs a point gravity source) may be a structural *obstruction*. | Not closable; a frontier, with a live possibility it is obstructed. [R4-attack.md] |
| **R3** | YM uniform tower gap | **clay-hard** | **Barrier characterized.** It IS the literal Clay Yang–Mills mass gap (forward direction almost-certainly true; proof Clay-hard). SHARD gives a reduction + roadmap (dressed-Z₂ polymer RG, P45 rung-by-rung); the nonperturbative core (CL1: U/LF/ER/ZF) is open, as field-wide. Sub-target: P45 rung-1, 3D SU(2). | Not closable; the genuine Millennium problem. [R3-attack.md] |

## The picture after the campaign

- **Four residues (R1, R5, R2, R6) are tractable-to-hard-but-doable**, and each got a concrete advance or
  a sharp residue-relocation. The corpus's most leveraged residue, **R1**, had its forward direction
  essentially closed and the one open numerical band resolved — the single highest-value increment.
- **Two residues (R3, R4) are genuinely Clay-hard** — the Yang–Mills mass gap and interacting
  relativistic-collapse integrability. These are not SHARD-specific gaps; they are recognized frontiers of
  mathematical physics. SHARD maps each correctly to one residue + a roadmap, but neither is closable here.
- **Two audit corrections surfaced during the attacks**: R6's dressed neutrino prediction is *not* dying at
  JUNO (matches to 0.05σ; the audit cited the bare point); and R2's "validity wall" is robust under
  optimization but the spectral-subordination metric is a red herring (the dynamical clock is the
  Ω-weighted diagonal).

## Post-campaign update — the residue dossiers sharpened three attacks
A parallel dossier workflow (deep-read of papers 30, II, 34–38, 1–3, 41, 39, 46) landed after the direct
attacks and sharpened three of them onto the corpus' *actual* decisive sub-targets:

- **R2 → the (NR) needle.** The real residue is not the composite clock but **(NR)**: "a *normal* word in
  two PSD letters has real spectrum." I tested it decisively (`v6_r2_NR_needle.py`): the minimum normality
  defect grows monotonically with complex-strength (0.19→0.42), so complex-spectrum words are *robustly
  non-normal* — **strong evidence FOR (NR)** (with a quantitative-frontier seed for a proof). Supports the
  rank-3 CPE reduction; residue = (ISO) + higher-rank + Anderson assembly.
- **R6 → p=ε is at genuine risk.** The dossier verified the corpus' natural commit probability is
  **θ=0.544, not ε=0.032** — so `p=ε` (seam weight, not commit probability) is *not securely derived*. The
  decisive five-minute probe (stationary seam Bernoulli weight) would settle it; R6 is closable *either
  way* (derivation or clean refutation).
- **R4 → a branch-A-may-be-false witness.** The dossier surfaced the **do-delete observational no-go**
  (paper 3 §19): two distinct lower-level mechanisms produce the *same* observed history law — the memory
  is not identifiable from observations, a finite witness that the strong (branch-A) "derive the memory"
  form may be **false**, not merely open. Strengthens the R4 verdict (Q3 + this = two obstruction signals).

These corrections are themselves a result: even my honest direct attacks were improved by the deeper read,
and two (R2's clock, R6's "p=ε derived") were partly off the real target — now corrected.

## Honest scope
None of the six residues is *closed*. The campaign **advanced the four tractable ones** (R1 forward-closed +
band resolved; R5 reduced to one axiom; R2 clock-lane confirmed + residue relocated to Anderson; R6
corrected + residue localized to a bounded algebraic O35.1) and **precisely characterized the two
Clay-hard ones** (R3, R4) as genuine frontiers with roadmaps but no tractable advance. The corpus's path
to "conditional → established" runs through R1 (most leverage, most closable) first; the two Clay problems
remain exactly that.
