# Publishable drafts — ISP / RISP program

This folder holds **markdown drafts** of the papers from the ISP/RISP corpus that are judged
publishable in their own right, scoped and framed to survive peer review. They will be converted
to LaTeX once the content is settled. The corpus is ~16 papers across versions; the defensible,
non-overlapping publishable content compresses to the **four (optionally five)** drafts below.

## Guiding discipline

- **One claim per paper.** Each paper makes a single, defensible claim and states its non-claims up
  front.
- **Reconstruction ≠ achievement.** Where a result is conditional, open, or table-stakes, it is
  labelled as such. No paper claims to "reproduce QFT/QCD/GR" — because the manuscripts behind them
  do not (the effective-GR work explicitly declines to "derive continuum GR"; even the strongest
  field-theory result is non-relativistic configuration-space QM).
- **External references only.** No ISP-corpus self-citation as evidence; the corpus papers are
  cited as companion preprints where a detailed construction is needed.
- **Render-safe markdown.** Display math in ```math fences or `$$`; inline symbols in backticks;
  never inline `$...$` inside prose.

## The drafts

| # | File | Claim (one line) | Status | Target venue |
|---|------|------------------|--------|--------------|
| 1 | `paper1-nonmarkovian-gravitational-decoherence.md` | If gravitational decoherence exists, indivisibility forces a Gaussian (non-Markovian) onset at the DP scale; a two-axis (onset × `E_G`-scaling) test separates it from DP/CSL/SN/unitary QM. | **Ready** (copied from the polished publishable v5-paper2). | PRD / PRA; sharp framing → PRL |
| 2 | `paper2-hypersurface-deformation-obstruction.md` | The QFT-reconstruction and effective-GR-kinematics obstructions are the *same* obstruction — foliation-independent representation of the hypersurface-deformation (Dirac–Schwinger) algebra on an indivisible substrate; non-Markovianity is the shared lever. | **Drafted fresh.** Needs ref re-verification + a careful read of the K1–K4 clearings against the source §10 papers. | Foundations of Physics |
| 3 | `paper3-isp-foundations-positioning.md` | ISP placed among Nelson / Bohm / collapse models; escapes Wallstrom in its original form; category problem stated; single empirical lever isolated. | **Drafted fresh.** Needs the Wallstrom §6 residue tightened with a referee in mind. | Found. Phys. / SHPMP |
| 4 | `paper4-unimodular-gravity-from-nonconserved-matter.md` | Non-conserved (collapse/beable) matter can source classical gravity via unimodular gravity → dynamical Λ; one clean positive prediction (negative-BMV + mandatory decoherence) and two clean negatives (DP magnitude excluded as dark energy; no dark matter). **Markovian-agnostic** — ISP is one instance, not a premise. | **Drafted fresh / de-programmed.** Standalone; the §10 obstruction-map material moved to #2, the §11 program-meta dropped. Needs ref re-verification. | PRD / CQG |
| 5 | `paper5-black-hole-three-idealizations-DRAFT-from-program.md` | The information/singularity/firewall paradoxes are each an over-extension of one of three idealizations (global state, divisibility, continuum beable). | **Optional / draft from program version** — publish as a perspective, or fold into a review. Weakest novelty (all resolution stances are known addresses). Still needs de-programming. | Perspective / Found. Phys. |

## Recommended order

1 (establish teeth + credibility) → 3 (scholarly standing) → 2 (the research contribution) → 4 (in
parallel, it is Markovian-agnostic and largely independent) → 5 (last, or never-standalone).

## Explicitly NOT for submission

- The Yang–Mills confinement / mass-gap "descent" claims (credibility liability; and superseded by
  the program's own later YM honesty — those manuscripts are marked conditional / not-a-proof).
- The V1–V16 reconstruction papers *as new physics* (table-stakes; every interpretation reconstructs
  QM).
- Any omnibus bundling reconstruction + Penrose + black holes + warp drives into one claim.

## Cross-cutting TODO before any submission

- Re-verify every reference's volume / page / year / arXiv against primary sources (flagged at the
  foot of each draft).
- De-program **#5** (remove program voice, internal cross-refs; make standalone). **#4 done** —
  rewritten standalone as a collapse-matter-sources-gravity paper that names ISP as one instance.
- For **#2**, read the K1–K4 "clearings" once more against the source §10 papers, and decide whether
  the GR Branch-2 content (currently restated) needs its own companion-preprint citations.
- Convert settled drafts to LaTeX (RevTeX4-2 for the physics venues; the program already has a
  working Tectonic setup and compiled .tex for #1 and the unimodular paper).
