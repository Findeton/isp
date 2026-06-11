# Publication Plan for Paper 1

Preprint, not peer reviewed, version 2026-06-04.

## Goal

Publish `paper1-nonmarkovian-gravitational-decoherence` as a serious independent-research contribution in quantum foundations / gravitational decoherence.

The strategic posture is:

```text
Independent researcher, conventional paper, modest claims, reproducible calculations, current literature, open feedback trail.
```

Do not lead with "I am an engineer with no contacts." Lead with the result:

```text
The Diósi-Penrose exponential is the white-noise member of a finite-memory family. Under a DP-scale finite-memory benchmark, the residual gravitational log-coherence has a Gaussian onset distinguishable by shape and E_G scaling.
```

No contacts is solvable. No feedback loop is dangerous. The plan below builds the feedback loop.

## Current Assessment

The five publication-level tasks the early reviews flagged are now **done**:

1. The "any finite-memory noise" claim is qualified (regular covariance, no white component). ✓
2. ISP is kept as *motivation*; §4.3 grounds the kernel in division events one level deeper without claiming a first-principles derivation. ✓
3. **Superseded.** The manuscript no longer merely "identifies" `tau_c` with `tau_G`: §4.3/§7 now show `tau_c ~ tau_G` is **forced** — by a self-consistency fixed point (`chi(tau_c) ~ 1`), by record information-gating, and by the demand for DP-scale decoherence at physical amplitude. The honest gain is that the new scale is *not* a free parameter; softening it back to "merely identified" would now understate the result. ✓
4. The log-coherence quantitative table is in §5. ✓
5. The bibliography is expanded (refs [25]–[28]: Carlesso 2022 review, Fein 2019, Delić 2020, Levitodynamics 2021). ✓

The manuscript has since been hardened through several further review rounds: the generic-colored-noise uniqueness objection → a third, **non-Gaussian discriminator axis** (kurtosis / coherence revivals, §5); the radiation bound → the **decoupling** of the (R_0-independent) decoherence from the (per-nucleon, R_0-set) emission/heating (§8); and the `tau_c` state-dependence → an explicit clarification that it is *not* a Schrödinger–Newton nonlinearity (a linear dephasing channel; §4.3). It is now **submission-ready** (11-page compiled PDF). See `SUBMISSION-PLAN.md` for the live, staged checklist. Submit as phenomenology / foundations, not as a completed first-principles derivation.

## Phase 1 - Make the Paper Look Like It Belongs

Timeline: 1-2 weeks.

Deliverables:

1. Finalize a clean LaTeX version.
2. Produce a PDF with standard physics formatting.
3. Add one figure or table for residual log-coherence:

```text
x = T / tau_G
L_exp = -x
L_Gauss = -x^2 / 2
Delta L = x - x^2 / 2
```

4. Add a short numerical/reproducibility appendix or companion notebook that recomputes:

```text
E_G thresholds
visibility table
log-coherence table
kernel limits
```

5. Add a short "Scope of claim" paragraph near the abstract or introduction:

```text
This paper does not derive the gravitational noise kernel from ISP. It uses ISP as a motivation for replacing the DP white-noise channel by a finite-memory channel, then studies the resulting onset shape.
```

6. Add an author statement:

```text
Affiliation: Independent researcher
Funding: No external funding
Competing interests: None declared
Data/code availability: Calculation scripts and notebooks available at [repository link]
```

Why this matters: arXiv says submissions should be topical, refereeable scientific contributions, prepared to accepted scholarly standards, and arXiv moderation is not peer review or a feedback service.[^arxiv-submit][^arxiv-moderation] You want the paper to look boringly professional before anyone evaluates the speculative physics.

## Phase 2 - Build Your Research Identity

Timeline: parallel with Phase 1.

1. Register an ORCID and fill it out.

ORCID is free for researchers and gives you a persistent identifier independent of institution.[^orcid] Use it everywhere: paper, personal page, repository, email signature, journal systems.

2. Create a minimal research page.

It can be very simple:

```text
Felix Robles Elvira
Independent researcher
Research interests: quantum foundations, non-Markovian decoherence, gravitational collapse phenomenology
ORCID: ...
Email: ...
Preprints: ...
Code: ...
```

3. Make a public repository for the paper.

Recommended structure:

```text
paper1-nonmarkovian-gravitational-decoherence/
  README.md
  paper/
    paper.tex
    references.bib
    figures/
  code/
    thresholds.py
    visibility_shape.py
  docs/
    one-page-summary.md
```

The README should say exactly what the repository contains. Avoid manifesto language.

4. Decide how to disclose tool use.

If generative AI tools materially assisted the manuscript text, follow the target venue's policy. arXiv says significant use of text-to-text generative AI should be reported according to subject standards, authors remain fully responsible, and AI tools should not be listed as authors.[^arxiv-ai]

Suggested acknowledgement if needed:

```text
The author used language-model tools for editorial assistance and internal critique. All scientific claims, calculations, references, and final text are the responsibility of the author.
```

## Phase 3 - Get Private Technical Feedback

Timeline: weeks 2-4.

Do not start by asking for arXiv endorsement. Ask for technical feedback.

Build a list of 20 people from the paper's own reference network:

1. DP / collapse-model researchers.
2. Non-Markovian open-systems researchers.
3. Levitated nanosphere / matter-wave interferometry people.
4. Quantum-foundations people familiar with stochastic or beable approaches.
5. Authors of recent arXiv papers you cite or should cite.

For each person, read at least one recent paper and write one sentence explaining why they are relevant. Then email 5 at a time. Expect few replies. That is normal.

Feedback email:

```text
Subject: Short feedback request on finite-memory DP decoherence model

Dear Prof./Dr. [Name],

I am an independent researcher working on a short phenomenological paper about gravitational decoherence. The core claim is modest: the standard Diósi-Penrose exponential is the white-noise limit of a finite-memory noise model, and a DP-scale finite-memory benchmark gives a quadratic/Gaussian onset in residual log-coherence.

I cite your work on [specific topic], and I would be grateful for a brief sanity check on whether the framing is obviously missing something in the collapse/decoherence literature. I am not asking for a detailed review.

PDF: [link]
One-page summary: [link]
Code/calculations: [link]

The main question is whether the paper correctly distinguishes:
1. generic finite-memory quadratic onset,
2. the inherited DP energy scale,
3. the ISP motivation for finite record memory.

Thank you for considering it.

Best regards,
Felix Robles Elvira
Independent researcher
ORCID: [link]
```

Rules:

1. Do not send mass email.
2. Do not ask for coauthorship unless someone makes a real technical contribution.
3. Do not ask for endorsement until the person has had a reason to trust the paper.
4. Track feedback in a changelog.

## Phase 4 - Preprint Route

Timeline: weeks 4-6.

### Route A: arXiv

Use arXiv if possible. It is the main physics preprint venue.

Account setup:

1. Register with arXiv.
2. Use `Independent` as organization if unaffiliated. arXiv explicitly allows unaffiliated users to enter "Independent" as the organization during registration.[^arxiv-independent]
3. Pick a likely category.

Recommended first category:

```text
quant-ph
```

Possible cross-list:

```text
gr-qc
```

Reason: the paper is primarily about quantum coherence, collapse/decoherence phenomenology, and an interferometric discriminator. It touches gravity, but it is not a full quantum-gravity model. Avoid `physics.gen-ph` unless arXiv reclassifies it there.

Endorsement:

arXiv may require endorsement for a first submission or a new category.[^arxiv-endorsement] If required:

1. Start the arXiv submission.
2. Get the endorsement request email/link.
3. Identify eligible endorsers from recent arXiv papers you cite.
4. Contact a very small number of relevant people.
5. Include ORCID, PDF, one-page summary, and endorsement link.

arXiv's own instructions say not to email large numbers of potential endorsers or repeatedly email the same person.[^arxiv-endorsement] Treat that as a hard rule.

Endorsement email:

```text
Subject: arXiv endorsement request for quant-ph finite-memory DP paper

Dear Prof./Dr. [Name],

I am preparing an arXiv submission in quant-ph on a finite-memory version of Diósi-Penrose gravitational decoherence. Your paper [specific paper] is directly relevant to the discussion of [specific point], which is why I am writing to you rather than sending a broad request.

The manuscript is here: [PDF link]
One-page summary: [link]
ORCID: [link]

If, after a brief skim, you think the submission is appropriate for arXiv's quant-ph category, I would be grateful for endorsement using this arXiv link:

[endorsement link]

If not, no worries at all.

Best regards,
Felix Robles Elvira
Independent researcher
```

### Route B: OSF Preprints or Zenodo/Figshare first

If arXiv endorsement stalls, do not freeze.

1. Post a citable preprint on OSF Preprints, Zenodo, or Figshare.
2. Link the code and figures.
3. Mark it clearly as "Version 0.1 - seeking technical feedback."
4. Continue journal submission in parallel.

OSF Preprints supports manuscript submission and can connect supporting data/code with the preprint.[^osf] Figshare and Zenodo-style repositories are also useful for DOI-backed research outputs and code/data records.[^figshare]

Important: an OSF/Zenodo/Figshare posting is not a substitute for peer review, but it gives you a stable public object to send to people.

## Phase 5 - Public Circulation Without Hype

Timeline: weeks 6-8.

After a preprint is public:

1. Post a concise thread or page:

```text
New preprint: finite-memory version of Diósi-Penrose gravitational decoherence.
Claim: not a derivation of collapse from ISP, but a shape-based phenomenological discriminator.
Main test: residual log-coherence linear in T for Markovian DP, quadratic in T for regular finite-memory noise.
```

2. Share with:

```text
quantum foundations communities
open-systems/decoherence people
matter-wave/levitated-interferometry researchers
Barandes/ISP-adjacent readers
```

3. Ask for corrections, not applause.

4. Keep a public revision log:

```text
v0.1: initial preprint
v0.2: corrected kernel wording; added log-coherence table; expanded bibliography
v1.0: journal-submission version
```

## Phase 6 - Journal Submission

Timeline: weeks 8-12.

Do not submit first to PRL, Nature Physics, or high-bar quantum-gravity venues. That is mostly a waste at this stage. Submit where the paper's actual genre fits.

Recommended target order:

1. **Quantum Studies: Mathematics and Foundations**

Good fit if the paper is framed as quantum foundations plus mathematical/phenomenological structure. The journal explicitly promotes fundamental aspects of quantum theory and bridges theoretical questions, foundational issues, and mathematical methods.[^qsmf]

2. **Foundations of Physics**

Good fit if the paper emphasizes conceptual structure and fundamental theories. The journal covers foundational aspects of quantum theory, quantum gravity, relativity, cosmology, and related areas.[^foundphys]

3. **Journal of Physics A: Mathematical and Theoretical**

Use this if the derivation is tightened and the open-systems/non-Markovian mathematics becomes central. Higher technical bar.

4. **Classical and Quantum Gravity**

Use this only if the gravitational-physics side is strengthened substantially. CQG welcomes work across gravitational physics and spacetime theory, but the paper must be of interest to a broad gravitational-physics readership.[^cqg]

5. **Physics Open or similar broad OA physics journals**

Use only if you accept the APC. Physics Open states an APC of USD 1,730, excluding taxes, so this is not the first choice unless funding is available.[^physicsopen]

Avoid:

1. Predatory journals.
2. Venues that promise guaranteed acceptance.
3. Paying APCs just to obtain a publication.
4. Journals whose recent articles are not technically close to your topic.

Cover letter:

```text
Dear Editor,

Please consider the manuscript "Non-Markovian Gravitational Decoherence: A Gaussian-Onset Alternative to the Diósi-Penrose Exponential" for publication in [Journal].

The paper proposes a finite-memory phenomenological extension of Diósi-Penrose gravitational decoherence. Its main result is that a regular non-white gravitational record-mismatch noise kernel gives a zero-initial-slope, quadratic onset in residual gravitational log-coherence, while the standard DP exponential is recovered as the white-noise limit. The ISP framework is used as motivation for finite record memory, not as a first-principles derivation of the kernel.

The work may interest readers concerned with quantum foundations, collapse phenomenology, gravitational decoherence, and mesoscopic interferometric tests. The manuscript includes explicit limitations, a benchmark DP-scale closure, and a proposed two-axis experimental discriminator based on onset shape and E_G scaling.

The author is an independent researcher. There is no external funding and no competing interest.

Sincerely,
Felix Robles Elvira
Independent researcher
ORCID: [link]
```

## Phase 7 - Handling Rejection

Expect rejection. That is not failure; it is part of entering the literature.

If desk rejected:

1. Do not argue unless there was a procedural error.
2. Record the stated reason.
3. Revise the title/abstract/framing if the editor misunderstood the genre.
4. Submit to the next venue.

If reviewed and rejected:

1. Treat referee reports as free expert consulting.
2. Write a response document even if not resubmitting.
3. Make a new preprint version incorporating the valid criticisms.
4. Submit elsewhere with the improved version.

Never write:

```text
Reviewers failed to understand the revolutionary nature of the work.
```

Write:

```text
The referee correctly identified that the ISP-to-kernel bridge was under-specified; the revised manuscript now states the model as phenomenological and separates finite-memory consequences from the DP-scale benchmark closure.
```

## 90-Day Checklist

### Week 1

- Apply review4 changes.
- Add log-coherence table.
- Add regularity/no-white-component caveat.
- Build clean PDF.
- Register ORCID.

### Week 2

- Create minimal research page.
- Create public repository or private repository ready to publish.
- Add calculation scripts/notebooks.
- Expand bibliography with recent work.

### Weeks 3-4

- Send 5 private feedback emails.
- Revise based on any responses.
- Send another 5 only after the first batch settles.

### Weeks 5-6

- Try arXiv submission.
- If endorsement is required, request it from a small number of relevant researchers.
- If arXiv stalls, post on OSF/Zenodo/Figshare and continue.

### Weeks 7-8

- Publicly circulate preprint.
- Collect corrections.
- Make version 0.2.

### Weeks 9-12

- Submit to Quantum Studies: Mathematics and Foundations or Foundations of Physics.
- Keep a response log.
- Prepare next target journal.

## Personal Operating Rules

1. Do not ask anyone to believe you because you are outside academia.
2. Do not apologize for being independent.
3. Do not inflate the claim to compensate for lack of credentials.
4. Let precision be the credential.
5. Make every calculation reproducible.
6. Read current papers before contacting their authors.
7. Ask for criticism before endorsement.
8. Use "independent researcher" plainly.
9. Never mass-email.
10. Keep revising.

## Minimum Submission Package

Before any journal submission, have:

```text
paper.pdf
paper.tex
references.bib
one-page-summary.pdf
repository link
ORCID
cover letter
author disclosure statement
preprint link, if available
```

## Best First Move

The best next move is not arXiv. The best next move is:

```text
Finish the review4 fixes, add the log-coherence quantitative table, update the bibliography, and send the paper privately to 5 carefully chosen researchers with a humble technical-feedback request.
```

Once the paper survives that first contact with the field, arXiv and journal submission become much less awkward.

[^arxiv-submit]: arXiv submission guidelines: https://info.arxiv.org/help/submit/index.html
[^arxiv-moderation]: arXiv moderation policy: https://info.arxiv.org/help/moderation/index.html
[^arxiv-ai]: arXiv policy for authors' use of generative AI language tools: https://info.arxiv.org/help/moderation/index.html
[^arxiv-independent]: arXiv author registration says unaffiliated users may enter "Independent" as organization: https://info.arxiv.org/help/registerhelp.html
[^arxiv-endorsement]: arXiv endorsement help: https://info.arxiv.org/help/endorsement.html
[^orcid]: ORCID researcher information: https://info.orcid.org/researchers/
[^osf]: OSF Preprints support: https://help.osf.io/article/690-osf-preprints
[^figshare]: Figshare researcher information: https://info.figshare.com/researchers/
[^qsmf]: Quantum Studies: Mathematics and Foundations journal page: https://link.springer.com/journal/40509
[^foundphys]: Foundations of Physics journal page: https://link.springer.com/journal/10701
[^cqg]: Classical and Quantum Gravity scope: https://publishingsupport.iopscience.iop.org/journals/classical-and-quantum-gravity/about-classical-quantum-gravity/
[^physicsopen]: Physics Open journal page: https://www.sciencedirect.com/journal/physics-open
