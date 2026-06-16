export const meta = {
  name: 'moveA-seal-bridge-realqm-correction',
  description: 'SHARD v7 Paper XVI (Move A): position the Gamma>=0 envelope as the tensor-product-free, multi-scenario complement to Barandes-Hasan-Kagan causal-locality Tsirelson; correct the now-contested Renou real-QM overclaim corpus-wide; revise the meta-result to three record-blind inputs of DIFFERENT epistemic status.',
  phases: [
    { title: 'Investigate', detail: 'recon overclaim locations; pin Gamma>=0 vs causal-locality-Tsirelson novelty (re-run PART 5 receipt); revised meta-result balanced on the live real-QM controversy' },
    { title: 'Write', detail: 'single-threaded positioning + correction paper' },
    { title: 'Review', detail: 'hostile referees -> fix -> terminal' },
  ],
}

const V6 = '/Users/felixrobles/workspace/isp/v6'
const V7 = '/Users/felixrobles/workspace/isp/v7'
const CODE = '/Users/felixrobles/workspace/isp/v7/code'
const PAPER = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper16-seal-indivisibility-bridge-real-quantum-reopening.md'

const CITES = [
  'VERIFIED CITATIONS (fetched 2026-06-16 from arXiv; use ONLY these facts):',
  '- Barandes, arXiv:2507.21192, Quantum Systems as Indivisible Stochastic Processes (Jul 2025): the stochastic-quantum correspondence; a quantum system is an indivisible (non-Markovian) stochastic process in configuration space; Hilbert space and wavefunction are secondary tools.',
  '- Barandes, Hasan, Kagan, arXiv:2512.18105, The CHSH Game, Tsirelson Bound, and Causal Locality (19 Dec 2025): reformulate the CHSH game via indivisible stochastic processes; a novel proof of the Tsirelson bound; the postulates of causally-local indivisible stochastic processes are precisely strong enough to allow violations of the Bell inequality up to but not beyond the Tsirelson bound. NOTE: CHSH-GAME-SPECIFIC.',
  '- Doukas, arXiv:2602.22095, On the emergence of quantum mechanics from stochastic processes (25 Feb 2026): lifts a stochastic kernel Gamma to a map on B(H); Chapman-Kolmogorov divisibility of the lifted family is the decisive additional constraint; a CK-consistent CPTP family admits a Lindblad form; off-diagonal phase is a compressed carrier of history dependence not fixed by transition kernels; states and proves a divisibility criterion for the underlying stochastic kernels. This is a DIVISIBILITY/emergence paper (NOT unistochastic from first principles); cite as such.',
  '- Hoffreumon, Woods, arXiv:2603.19208, Quantum theory based on real numbers cannot be experimentally falsified (19 Mar 2026): real quantum theory (RQT) with the Kronecker composition rule reproduces ALL finite network correlations of QT under OPERATIONAL (not product-state) independence; RQT empirically indistinguishable from QT absent a QT violation.',
  '- Maioli, Curado, Gazeau, arXiv:2604.19482, Quantum mechanics over real numbers fully reproduces standard quantum theory (21 Apr 2026): a real Kahler-space framework with a SYMPLECTIC composition rule (replacing Kronecker) reproduces all of QM; achieves the maximal CHSH3 = 6 sqrt(2) with real variables.',
  '- Moradi Kalarde, Xu, Renou, arXiv:2604.07425, Comment on Quantum theory based on real numbers cannot be experimentally falsified (8 Apr 2026): Renou et al. RESPOND that the Hoffreumon-Woods postulate fails in Fermionic Information Theory and is not a general physical postulate. THE DEBATE IS LIVE; Renou et al. 2021 (Nature 600, 625) stands in its own framing.',
  'FRAMING RULE: the complex-over-real / tensor-product bit is NOW CONTESTED (arguably a composition-rule / local-tomography CONVENTION that may not be experimentally fixable), a live 2026 controversy. NEVER state Renou is wrong or that real QM is settled. The contested status VINDICATES (does not prove) the SHARD verdict that the tensor product is the un-forceable field-blind import.',
].join('\n')

const STANDING = [
  'STANDING CONSTRAINTS:',
  '- SINGLE-THREADED: the paper reads as written ONCE. NO round/version/referee/revision/draft/campaign narration. Bare date stamp 2026-06-16 only.',
  '- HIGH PRECISION: any receipt at mpmath dps>=100 or sympy-exact; SDP/numeric digits flagged solver-tolerance. Re-run, do not trust.',
  '- HONEST SCOPE: SHARD is ahead in FRAMING (the seal as a physical MECHANISM; the weight-0 / ker-R localization of the bit) and in having the multi-scenario tensor-product-free Gamma>=0 envelope plus the un-forceability-of-the-filling no-go. SHARD is NOT ahead on the undecidability math (MIP*=RE, Slofstra) which is IMPORTED, nor did SHARD originate the local-tomography-least-motivated lineage (Hardy / Barnum-Mueller-Ududec / Hoehn). State this.',
  '- Cite by arXiv id; numbers trace to receipts.',
].join('\n')

const CONTEXT = [
  'SHARD context: the record click-law forces a multiplicative SEALING skeleton S=exp(-kappa*chi) (survival-multiplicativity along the refinement axis). Paper XII (v7) proved the transverse moment-positivity Gamma>=0 (the Gram matrix of the systems OWN observables {1,A_x,B_y,A_xB_y} = the COMMUTING-OPERATOR relaxation, strictly weaker than the tensor product it lacks) ENTAILS the full almost-quantum-adjacent envelope: no-signaling + Tsirelson CHSH<=2sqrt(2) + PR-box exclusion + I3322 strict outer relaxation (level-1 8.748 > level-2 8.000) + the monogamy facet CHSH_AB^2+CHSH_AC^2<=8. Papers XII/XIII proved chi_AB (entangling content) is FREE up to the almost-quantum set Q-tilde and un-forceable from inside (the tensor-product wall). The meta-result: records carry everything relative/weight-0, barred from three last inputs: scale l_step (=G), tensor product (chi_AB / local tomography), canonical mode (masses).',
  'Receipt to reuse: ' + CODE + '/p6_transverse_nogo.py (PART 5 = the Gamma>=0 entailments, dps=140).',
].join('\n')

phase('Investigate')

const RECON_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['occurrences', 'summary'],
  properties: {
    occurrences: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['file', 'locator', 'verbatim', 'why_overclaim', 'suggested_replacement'], properties: {
      file: { type: 'string' }, locator: { type: 'string' }, verbatim: { type: 'string' }, why_overclaim: { type: 'string' }, suggested_replacement: { type: 'string' } } } },
    summary: { type: 'string' },
  },
}
const POS_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['receipt_rerun', 'entailments_confirmed', 'novelty_statement', 'caveats', 'what_shard_does_not_own'],
  properties: { receipt_rerun: { type: 'string' }, entailments_confirmed: { type: 'boolean' }, novelty_statement: { type: 'string' }, caveats: { type: 'string' }, what_shard_does_not_own: { type: 'string' } },
}
const META_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['revised_meta_result', 'scale_leg', 'mode_leg', 'tensor_leg', 'controversy_framing'],
  properties: { revised_meta_result: { type: 'string' }, scale_leg: { type: 'string' }, mode_leg: { type: 'string' }, tensor_leg: { type: 'string' }, controversy_framing: { type: 'string' } },
}

const pRecon = [
  'RECON task. Find EVERY occurrence in the SHARD corpus of the now-contested overclaim that the Renou 2021 real-QM result EXPERIMENTALLY FIXES the complex-over-real / tensor-product bit (phrases like Renou ruled out real QM, experiment-fixed, fixed by experiment just as Newton G, ruled out real quantum).',
  'GREP across ' + V6 + ' , ' + V7 + ' , and ' + V7 + '/LONG_MARCH_PLAN.md for: Renou, real QM, real quantum, experiment-fixed, ruled out, Chen/Li, complex-over-real, C-over-R.',
  'Known hotspots: v7 paper6, paper12, paper13 (esp. sec 7), the LONG_MARCH_PLAN. For EACH occurrence return file, a locator (section or quoted anchor), the verbatim claim, why it overclaims (given the live 2026 reopening), and a suggested single-sentence replacement stating the CONTESTED status (cite arXiv:2603.19208 / 2604.19482 reopening; arXiv:2604.07425 Renou defending; Renou 2021 stands in its framing) and that this VINDICATES the un-forceable-import verdict.',
  CITES, 'Return RECON_SCHEMA. Final message is data.',
].join('\n')

const pPos = [
  'POSITIONING task. Pin down PRECISELY and defensibly how the SHARD Gamma>=0 envelope relates to Barandes-Hasan-Kagan arXiv:2512.18105 (causal-locality Tsirelson).',
  'STEP 1: re-run ' + CODE + '/p6_transverse_nogo.py and confirm PART 5 entailments hold (no-signaling, Tsirelson 2sqrt(2), PR-box exclusion, I3322 level-1 8.748 > level-2 8.000, monogamy facet). Report the receipt result verbatim (pass/fail, key numbers, dps).',
  'STEP 2: state the NOVELTY precisely and HONESTLY. The SHARD Gamma>=0 is the Gram matrix of the systems OWN observables = the commuting-operator relaxation, TENSOR-PRODUCT-FREE, entailing a MULTI-SCENARIO envelope (CHSH + I3322 + monogamy + PR-exclusion), PLUS the un-forceability-of-the-filling no-go (Papers XII/XIII). Barandes-Hasan-Kagan derive the Tsirelson bound for the CHSH GAME specifically, via causally-local indivisible stochastic processes. Articulate exactly what is genuinely complementary/novel vs what merely overlaps. Be skeptical: do not overclaim a generalization you cannot defend; flag where their framework might already cover a scenario.',
  'STEP 3: state what SHARD does NOT own (the undecidability core MIP*=RE / Slofstra is imported; the local-tomography-least-motivated lineage predates SHARD).',
  CITES, CONTEXT, STANDING, 'Return POS_SCHEMA. Final message is data.',
].join('\n')

const pMeta = [
  'META-RESULT REVISION task. The corpus meta-result currently reads: records carry everything relative; barred from THREE experiment-fixed inputs: scale l_step (=G), tensor product (chi_AB), mode (masses). The clean three-fold all-experiment-fixed symmetry is now FALSE given the live real-QM reopening.',
  'Produce the REVISED meta-result: three record-blind inputs of DIFFERENT epistemic status. (1) SCALE l_step/G: genuinely MEASURED (G is an experimental datum). (2) MODE/masses: import-fixed (measured spectra). (3) TENSOR PRODUCT / chi_AB / complex-over-real bit: a NOW-CONTESTED composition-rule / local-tomography CONVENTION that may be experimentally UNFIXABLE (Hoffreumon-Woods 2603.19208, Maioli 2604.19482 reopen; Renou Comment 2604.07425 defends; Renou 2021 stands in its framing).',
  'State each leg precisely with its epistemic status, and the controversy framing (balanced, live, not Renou is wrong). Explain why the contested status VINDICATES rather than threatens the SHARD verdict that the tensor product is an un-forceable field-blind import (in ker R, weight-0): if the bit is a convention no experiment fixes, that is EXACTLY the records cannot supply it and neither can experiment cleanly.',
  CITES, CONTEXT, 'Return META_SCHEMA. Final message is data.',
].join('\n')

const inv = await parallel([
  () => agent(pRecon, { label: 'recon-overclaim', phase: 'Investigate', schema: RECON_SCHEMA }),
  () => agent(pPos, { label: 'gamma-vs-barandes', phase: 'Investigate', schema: POS_SCHEMA }),
  () => agent(pMeta, { label: 'revised-meta-result', phase: 'Investigate', schema: META_SCHEMA }),
])
const recon = inv[0], pos = inv[1], met = inv[2]
log('Investigate: ' + (recon ? recon.occurrences.length : 0) + ' overclaim sites; entailments_confirmed=' + (pos ? pos.entailments_confirmed : 'NULL'))

phase('Write')
const PAPER_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['path', 'title', 'abstract', 'sections', 'word_count'],
  properties: { path: { type: 'string' }, title: { type: 'string' }, abstract: { type: 'string' }, sections: { type: 'array', items: { type: 'string' } }, word_count: { type: 'integer' } },
}

const reconDigest = recon ? recon.occurrences.map(o => '  - ' + o.file + ' (' + o.locator + '): ' + o.verbatim + ' -> ' + o.suggested_replacement).join('\n') : 'none'
const writePrompt = [
  'Write SHARD relativistic-ISP v7 Paper XVI to ' + PAPER + ' (markdown). POSITIONING + CORRECTION paper, single-threaded.',
  'THESIS: the SHARD forced sealing skeleton makes the SEAL a physical mechanism in the indivisible-stochastic family (Barandes); its Gamma>=0 transverse envelope is the TENSOR-PRODUCT-FREE, MULTI-SCENARIO complement to the CHSH-specific causal-locality Tsirelson derivation (Barandes-Hasan-Kagan 2512.18105), augmented by the un-forceability-of-the-filling no-go (Papers XII/XIII); and the 2026 real-quantum REOPENING (Hoffreumon-Woods 2603.19208, Maioli 2604.19482; Renou Comment 2604.07425) shows the complex-over-real / tensor-product bit is a now-CONTESTED composition convention, which REVISES the meta-result to three record-blind inputs of DIFFERENT epistemic status (scale measured / mode import-fixed / tensor-product contested-convention) and VINDICATES (does not prove) the SHARD un-forceable-import verdict.',
  'SECTIONS: (1) abstract; (2) the seal skeleton in the indivisible-stochastic family (position vs Barandes 2507.21192; the seal as the physical mechanism the correspondence leaves unmotivated; honest owned-vs-imported); (3) the Gamma>=0 envelope vs causal-locality Tsirelson, the precise novelty (tensor-product-free Gram / commuting-operator relaxation, multi-scenario CHSH+I3322+monogamy+PR-exclusion, + un-forceability no-go) vs the CHSH-specific 2512.18105, with receipt numbers; (4) the real-quantum reopening and the CORRECTED epistemic status of the tensor-product bit (balanced live controversy; the vindication argument); (5) the REVISED meta-result (three record-blind inputs, three epistemic statuses) as a table; (6) what SHARD does not own; (7) conclusion. Include a short note listing the in-corpus correction sites WITHOUT review-narration.',
  'POSITIONING: novelty=' + (pos ? pos.novelty_statement : '') + ' || caveats=' + (pos ? pos.caveats : '') + ' || not-owned=' + (pos ? pos.what_shard_does_not_own : '') + ' || receipt=' + (pos ? pos.receipt_rerun : ''),
  'REVISED META: ' + (met ? met.revised_meta_result : '') + ' || scale=' + (met ? met.scale_leg : '') + ' || mode=' + (met ? met.mode_leg : '') + ' || tensor=' + (met ? met.tensor_leg : '') + ' || controversy=' + (met ? met.controversy_framing : ''),
  'CORRECTION SITES (mention the retired overclaim, single-threaded, no round-narration):',
  reconDigest,
  CITES, CONTEXT, STANDING, 'Write the full paper to ' + PAPER + '. Return PAPER_SCHEMA.',
].join('\n')

const paperInfo = await agent(writePrompt, { label: 'write-paper16', phase: 'Write', schema: PAPER_SCHEMA })
log('Wrote ' + paperInfo.title + ' (' + paperInfo.word_count + ' words)')

phase('Review')
const REVIEW_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['referee', 'overall', 'findings', 'one_line'],
  properties: { referee: { type: 'string' }, overall: { type: 'string', enum: ['ACCEPT', 'MINOR_REVISION', 'MAJOR_REVISION', 'REJECT'] },
    findings: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['severity', 'location', 'issue', 'fix'], properties: { severity: { type: 'string', enum: ['CRITICAL', 'MAJOR', 'MINOR', 'NIT'] }, location: { type: 'string' }, issue: { type: 'string' }, fix: { type: 'string' } } } },
    one_line: { type: 'string' } },
}
const FIX_SCHEMA = { type: 'object', additionalProperties: false, required: ['changes_made', 'receipts_rerun', 'rebuttals', 'remaining'], properties: { changes_made: { type: 'array', items: { type: 'string' } }, receipts_rerun: { type: 'array', items: { type: 'string' } }, rebuttals: { type: 'array', items: { type: 'string' } }, remaining: { type: 'string' } } }

const REF = [
  ['R1-overclaim', 'Hunt overclaiming + the real-QM framing. Is the complex-over-real bit presented as CONTESTED (not Renou wrong)? Is the Renou Comment 2604.07425 cited so the controversy is balanced? Is the SHARD novelty over Barandes-Hasan-Kagan honestly scoped (multi-scenario/tensor-free vs CHSH-only) and NOT claiming the undecidability math? Is the vindication argument stated as vindication-not-proof?'],
  ['R2-citations', 'Verify EVERY arXiv citation matches the verified facts (2507.21192 Barandes; 2512.18105 Barandes-Hasan-Kagan CHSH-Tsirelson; 2602.22095 Doukas divisibility NOT unistochastic; 2603.19208 Hoffreumon-Woods; 2604.19482 Maioli CHSH3=6sqrt2; 2604.07425 Renou Comment; Renou 2021 Nature 600 625). Flag any mis-citation, wrong author, or wrong claim.'],
  ['R3-precision', 'Verify the Gamma>=0 entailment numbers (no-signaling, 2sqrt(2), I3322 level-1 8.748 > level-2 8.000, monogamy facet) match p6_transverse_nogo.py PART 5; re-run it (cd ' + CODE + ' then python3 p6_transverse_nogo.py). Flag any number not traceable. Confirm dps flagged where relevant.'],
  ['R4-style', 'Enforce single-threaded style (no round/version/referee/revision/campaign narration; only the dateline). Verify the correction is stated WITHOUT we-previously-claimed narration. Confirm the revised meta-result table is internally consistent.'],
]

let round = 0, terminal = false, last = null
while (round < 3 && !terminal) {
  round++
  const reviews = (await parallel(REF.map(rf => () =>
    agent(['You are hostile referee ' + rf[0] + ' for SHARD v7 Paper XVI at ' + PAPER + '. READ it from disk first. ' + rf[1], 'You may read/run receipts in ' + CODE + ' and grep the corpus. Be adversarial but fair; CRITICAL/MAJOR only for genuine errors/overclaims/mis-citations.', CITES, 'Return REVIEW_SCHEMA.'].join('\n'),
      { label: rf[0] + '-r' + round, phase: 'Review', schema: REVIEW_SCHEMA })
  ))).filter(Boolean)
  last = reviews
  const blocking = []
  for (const r of reviews) for (const f of r.findings) if (f.severity === 'CRITICAL' || f.severity === 'MAJOR') blocking.push({ referee: r.referee, severity: f.severity, location: f.location, issue: f.issue, fix: f.fix })
  log('Review r' + round + ': ' + reviews.map(r => r.overall).join(',') + ' | ' + blocking.length + ' blocking')
  if (blocking.length === 0) { terminal = true; break }
  const fixLines = blocking.map((f, i) => (i + 1) + '. [' + f.severity + '] (' + f.referee + ' @ ' + f.location + ') ' + f.issue + ' >> ' + f.fix).join('\n')
  const fix = await agent(['You are the author revising SHARD v7 Paper XVI at ' + PAPER + '. Resolve each CRITICAL/MAJOR finding (fix the paper, or rebut with evidence). Keep single-threaded, keep the real-QM controversy balanced (contested not settled), do not overclaim novelty over Barandes-Hasan-Kagan, do not claim the undecidability math.', 'FINDINGS:', fixLines, CITES, STANDING, 'Edit in place. Return FIX_SCHEMA.'].join('\n'),
    { label: 'fix-r' + round, phase: 'Review', schema: FIX_SCHEMA })
  log('Fix r' + round + ': ' + fix.changes_made.length + ' changes, ' + fix.rebuttals.length + ' rebuttals')
}

return { paper: paperInfo.path, title: paperInfo.title, terminal: terminal, rounds: round,
  overclaim_sites: recon ? recon.occurrences.map(o => ({ file: o.file, locator: o.locator, verbatim: o.verbatim, replacement: o.suggested_replacement })) : [],
  final: last ? last.map(r => ({ referee: r.referee, overall: r.overall, one_line: r.one_line })) : null }
