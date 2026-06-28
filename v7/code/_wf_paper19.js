export const meta = {
  name: 'paper19-seal-swerve-and-norevival',
  description: 'SHARD v7 Paper XIX: fully investigate two experimental channels from the discrete-sealed substrate -- (A) the seal-swerve, a Lorentz-invariant covariant momentum-diffusion (Dowker-Henson-Sorkin) whose coefficient is tied to the seal rate sigma (testable / NOT mechanism-blind, magnitude scale-gated); (B) the CP-divisible no-revival decoherence (Paper 56) and whether it can escape the Paper-X mechanism-blindness (honest verdict, likely blind vs QM). Investigate -> write -> hostile review to terminal.',
  phases: [
    { title: 'Investigate', detail: 'swerve derivation + seal-rate tie + scale-gating; no-revival escape-or-blind probe; literature/bounds; adversarial' },
    { title: 'Write', detail: 'single-threaded MIX paper: [TESTABLE scale-gated] swerve, [BLIND] no-revival' },
    { title: 'Review', detail: 'hostile referees -> investigate opens -> fix -> terminal' },
  ],
}

const V6 = '/Users/felixrobles/workspace/isp/v6'
const V7 = '/Users/felixrobles/workspace/isp/v7'
const CODE = '/Users/felixrobles/workspace/isp/v7/code'
const PAPER = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper19-seal-swerve-norevival.md'

const PHYS = [
  'PHYSICS CONTEXT (two channels from the SHARD discrete-sealed substrate; the records ARE the causal set, v6 paper1).',
  'CHANNEL A -- THE SEAL-SWERVE. In causal set theory a massive particle propagating through the discrete substrate undergoes a LORENTZ-INVARIANT diffusion of its energy-momentum on the mass shell -- the "swerves" (Dowker-Henson-Sorkin, Mod.Phys.Lett.A19:1829 (2004); Philpott-Dowker-Sorkin, Phys.Rev.D79:124047 (2009), "Energy-momentum diffusion from spacetime discreteness"). The unique Lorentz-invariant diffusion is a Fokker-Planck equation on the mass hyperboloid H_m: df/dtau = kappa * Laplacian_{H_m}(f), with kappa the swerve diffusion constant and tau proper time; isotropic momentum diffusion in the rest frame, <p^2>(tau) ~ kappa*tau (slow covariant heating). In plain causal sets kappa is a phenomenological Planck-suppressed constant. THE SHARD CONTRIBUTION to derive: tie kappa structurally to the SEAL RATE sigma (the entropy-production / click flux; v6 paper42 eta, the seal entropy production sigma=D(P_AB||P_BA)) -- the worldline crosses seal events at a rate set by the seal density, each contributing a momentum kick; so kappa_swerve is proportional to sigma (a weight-0 structural relation) times an absolute scale (l_step power, weight -- the IMPORT wall). The KEY VALUE: the swerve is NOT mechanism-blind -- continuum QFT conserves a free particle momentum (no diffusion), so a measured covariant momentum-diffusion / anomalous heating is a discrete-substrate-vs-continuum DISCRIMINATOR. Existing bounds (Kaloper-Mattingly; PDS; cosmic-ray / molecular-coherence / CMB heating limits) constrain the combination kappa ~ sigma*l_step^k.',
  'CHANNEL B -- THE NO-REVIVAL / CP-DIVISIBILITY. The SHARD seal is a state-independent irreversible commitment: the off-diagonal coherence decays as |rho_01(t)| = exp(-Integral_0^t lambda(s) ds) with lambda(s) >= 0 (v6 paper56, the indivisible gravitational channel) -> CP-DIVISIBLE, MONOTONE, NO REVIVALS; and CP-divisibility is incompatible with Barandes-indivisibility. Paper X (gravitational decoherence) proved the Gaussian onset (|rho_01| ~ exp(-k t^2/2) near t=0, lambda ~ t) is MECHANISM-BLIND: sparse sealing and continuous classical noise are bit-identical to all orders. THE QUESTION to fully investigate: can the no-revival / CP-divisibility be turned into a signature that ESCAPES this blindness? Probe higher-order / multi-time correlations, the specific lambda(t) form, the BLP/RHP non-Markovianity measure N. THE HONEST PRIOR (test it, do not assume): the no-revival CANNOT discriminate SHARD from standard QM with ordinary CP-divisible decoherence (both give N=0, no revivals); it CAN only discriminate against REVIVAL-exhibiting (non-CP-divisible / non-Markovian) collapse models (which give N>0). So it is BLIND in the SHARD-vs-QM sense, a discriminator only against a specific exotic class. Verdict likely [NO-GO/BLIND]; report the precise discrimination boundary.',
  'THE MIX: Channel A = [TESTABLE / NOT mechanism-blind] but magnitude scale-gated (so it CONSTRAINS sigma*l_step^k rather than predicting a number -- analogous to how Testing-ER=EPR-with-Hydrogen constrains the ER=EPR amplitude). Channel B = [BLIND] (seal-specific but cannot beat QM). The seal-swerve is the only channel that is BOTH seal-specific AND escapes mechanism-blindness.',
].join('\n')

const STANDING = [
  'STANDING CONSTRAINTS (NON-NEGOTIABLE):',
  '- FULL PRECISION: mpmath dps >= 120 for ALL numeric (diffusion solutions, heating rates, coherence decays, the BLP/RHP measure); sympy-EXACT for the structural/algebraic claims (the Lorentz-invariance of the diffusion, the weight grading of kappa, the CP-divisibility monotonicity, the kappa ~ sigma relation). NEVER float64 for cancellation-heavy or near-vacuum quantities. Flag any numeric digit.',
  '- SINGLE-THREADED: the paper reads as written once. NO round/version/referee/revision/campaign narration. Date stamp 2026-06-17 only.',
  '- HONEST SCOPE / MIX-GRADED. Tags: [TESTABLE]=a falsifiable consequence; [SCALE-GATED]=magnitude needs the imported l_step; [NOT-BLIND]=distinguishes discrete-substrate from continuum; [NO-GO/BLIND]=cannot discriminate SHARD from QM; [INHERITED]=from causal sets, not SHARD-specific; [SHARD-SPECIFIC]=the seal contribution. The swerve EXISTENCE is INHERITED (DHS); the seal-rate TIE is SHARD-SPECIFIC; the MAGNITUDE is SCALE-GATED; the no-revival is BLIND. Do NOT overclaim a numerical prediction (the scale is imported) nor a discrimination the no-revival cannot deliver.',
  '- Cite the literature correctly (DHS 2004, PDS 2009, Kaloper-Mattingly, Gran Sasso 2021, BLP/RHP). Numbers trace to receipts.',
].join('\n')

phase('Investigate')
const SWERVE_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['receipt_path', 'pass', 'n_checks', 'kappa_sigma_relation', 'scale_gating', 'not_blind_argument', 'heating_law', 'bounds_constrain', 'precision', 'caveats'],
  properties: {
    receipt_path: { type: 'string' }, pass: { type: 'boolean' }, n_checks: { type: 'integer' },
    kappa_sigma_relation: { type: 'string' }, scale_gating: { type: 'string' }, not_blind_argument: { type: 'string' },
    heating_law: { type: 'string' }, bounds_constrain: { type: 'string' }, precision: { type: 'string' }, caveats: { type: 'string' },
  },
}
const NOREV_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['receipt_path', 'pass', 'n_checks', 'verdict', 'discrimination_boundary', 'escape_attempts', 'blp_rhp', 'precision', 'caveats'],
  properties: {
    receipt_path: { type: 'string' }, pass: { type: 'boolean' }, n_checks: { type: 'integer' },
    verdict: { type: 'string', enum: ['BLIND_NO_ESCAPE', 'PARTIAL_ESCAPE', 'CLEAN_ESCAPE'] },
    discrimination_boundary: { type: 'string' }, escape_attempts: { type: 'string' }, blp_rhp: { type: 'string' }, precision: { type: 'string' }, caveats: { type: 'string' },
  },
}
const LIT_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['swerve_bounds', 'norevival_bounds', 'what_constrains_shard', 'sources'],
  properties: { swerve_bounds: { type: 'string' }, norevival_bounds: { type: 'string' }, what_constrains_shard: { type: 'string' }, sources: { type: 'array', items: { type: 'string' } } },
}
const ADV_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['swerve_verdict', 'norevival_verdict', 'strongest_objection', 'overclaim_risks', 'notes'],
  properties: { swerve_verdict: { type: 'string' }, norevival_verdict: { type: 'string' }, strongest_objection: { type: 'string' }, overclaim_risks: { type: 'string' }, notes: { type: 'string' } },
}

const pSwerve = [
  'CHANNEL A -- derive the SEAL-SWERVE. Build and RUN a receipt at ' + CODE + '/p19a_seal_swerve.py (mpmath dps>=120, sympy-exact structure).',
  'STEPS: (1) set up the Lorentz-invariant momentum diffusion on the mass hyperboloid H_m: the Fokker-Planck df/dtau = kappa*Laplacian_{H_m} f; VERIFY it is the unique Lorentz-invariant diffusion (isotropic in the rest frame; boost-covariant) -- sympy where possible, and show <p^2>(tau) ~ kappa*tau (the heating law). (2) Derive the SHARD-specific TIE: relate kappa to the seal rate sigma -- model the worldline crossing seal events at a rate set by the seal density, each contributing a mean-zero momentum kick of variance ~ (kick scale)^2; so kappa_swerve = (const) * sigma * (l_step power). State the structural relation kappa proportional to sigma (weight-0) and the absolute magnitude scale-gated (l_step, weight). (3) WEIGHT ANALYSIS (sympy-exact, reuse the g_lambda automorphism idea): kappa_swerve*l_step^? is weight-0 (structural) while the absolute kappa is weight-gated (the import wall) -- exactly the campaign pattern. (4) NOT-BLIND argument: continuum QFT conserves free-particle momentum (no diffusion), so the swerve is a genuine discrete-vs-continuum discriminator; quantify <p^2> growth vs the continuum (zero). (5) connect to existing bounds: kappa is constrained by Kaloper-Mattingly / PDS / cosmic-ray/coherence-heating limits; state what bound on sigma*l_step^k follows.',
  'Print pass/fail per check and ALL CHECKS PASS (k/k). HONEST: the swerve EXISTENCE is INHERITED (DHS); only the seal-rate TIE is SHARD-specific; the magnitude is SCALE-GATED. Do not claim a numerical prediction.',
  PHYS, STANDING, 'Return SWERVE_SCHEMA. Final message is data.',
].join('\n')

const pNorev = [
  'CHANNEL B -- fully investigate the NO-REVIVAL / CP-DIVISIBILITY escape question. Build and RUN a receipt at ' + CODE + '/p19b_norevival_blindness.py (mpmath dps>=120, sympy-exact).',
  'Read v6 paper56 (CP-divisible sealing, |rho_01|=exp(-Integral lambda), lambda>=0, no revivals) and v6 paper-X / publishable paper-X (the Gaussian-onset mechanism-blindness).',
  'STEPS: (1) encode the CP-divisible seal coherence |rho_01(t)|=exp(-Integral_0^t lambda); verify monotone, no revivals, the Gaussian onset (lambda~t => |rho_01|~exp(-k t^2/2)). (2) Build the COMPARISON: (a) standard QM with ordinary CP-divisible environmental decoherence (also monotone, no revivals); (b) a NON-Markovian / revival-exhibiting collapse model (lambda(t) goes negative over some interval => coherence partially REVIVES). (3) The BLP/RHP non-Markovianity measure N: compute N=0 for the seal AND for QM-decoherence, N>0 for the revival model. So N CANNOT separate SHARD from QM (both 0); it separates SHARD from revival models. (4) ESCAPE ATTEMPTS -- genuinely try: does any HIGHER-ORDER / MULTI-TIME correlation, or the SPECIFIC lambda(t) FORM (Gaussian onset, the exact decay shape), distinguish the seal CP-divisible decoherence from a generic CP-divisible noise with the same |rho_01(t)|? (Paper X says the onset itself is bit-identical; test whether anything beyond it discriminates.) (5) VERDICT: BLIND_NO_ESCAPE (the honest prior -- no measurable quantity separates seal from QM-decoherence, only from revival models) / PARTIAL_ESCAPE / CLEAN_ESCAPE. State the precise discrimination boundary (vs what class it CAN discriminate).',
  'Print pass/fail and ALL CHECKS PASS (k/k). Be brutally honest -- a clean BLIND verdict is the expected, valuable outcome; do NOT manufacture an escape.',
  PHYS, STANDING, 'Return NOREV_SCHEMA. Final message is data.',
].join('\n')

const pLit = [
  'LITERATURE / BOUNDS task. Use web search (ToolSearch "select:WebSearch", "select:WebFetch"). Find the actual experimental/observational bounds on: (1) the causal-set SWERVE / energy-momentum diffusion (Dowker-Henson-Sorkin 2004; Philpott-Dowker-Sorkin 2009; Kaloper-Mattingly constraints; any cosmic-ray, neutrino, molecular-coherence, or CMB bound on a Lorentz-invariant momentum-diffusion constant kappa). (2) the collapse/decoherence rate and non-Markovianity: Diosi-Penrose / CSL bounds (Gran Sasso 2021 X-ray; matter-wave interferometry; levitated optomechanics), and the BLP/RHP non-Markovianity measure (does any experiment bound revivals / non-Markovianity in a way relevant to the seal?).',
  'Report: what numerical bounds exist on the swerve kappa (=> a bound on sigma*l_step^k); what bounds exist on the decoherence rate; and honestly whether the no-revival has ANY experimental discriminating handle beyond ruling out revival-models. Give sources (arXiv/DOI).',
  PHYS, 'Return LIT_SCHEMA. Final message is data.',
].join('\n')

const pAdv = [
  'ADVERSARIAL task. Attack BOTH channels (read the receipts ' + CODE + '/p19a_seal_swerve.py and p19b_norevival_blindness.py if present).',
  'SWERVE: (1) is the swerve really NOT mechanism-blind, or could a continuum/conventional effect (ordinary scattering, thermal noise, instrument heating) mimic the Lorentz-invariant momentum diffusion? (2) Is the kappa~sigma tie a genuine derivation or just dimensional hand-waving? (3) Is the scale-gating correctly stated (magnitude imported, not predicted)? Flag any overclaim of a numerical prediction.',
  'NO-REVIVAL: (1) is the BLIND verdict right, or is there an escape the probe missed (a multi-time correlation, a state-dependent test, a weak-measurement protocol)? (2) Is the discrimination boundary (vs revival-models only, not QM) stated honestly? (3) Does the paper avoid implying the no-revival can beat QM?',
  'Report the single strongest objection per channel, the overclaim risks, and whether each channel survives honest scrutiny.',
  PHYS, 'Return ADV_SCHEMA. Final message is data.',
].join('\n')

const inv = await parallel([
  () => agent(pSwerve, { label: 'swerve-derivation', phase: 'Investigate', schema: SWERVE_SCHEMA }),
  () => agent(pNorev, { label: 'norevival-blindness', phase: 'Investigate', schema: NOREV_SCHEMA }),
  () => agent(pLit, { label: 'literature-bounds', phase: 'Investigate', schema: LIT_SCHEMA }),
  () => agent(pAdv, { label: 'adversarial', phase: 'Investigate', schema: ADV_SCHEMA }),
])
const sw = inv[0], nr = inv[1], lit = inv[2], adv = inv[3]
log('Investigate: swerve pass=' + (sw ? sw.pass : 'NULL') + ' | norevival=' + (nr ? nr.verdict : 'NULL') + ' | adversarial done=' + (adv ? true : false))

phase('Write')
const PAPER_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['path', 'title', 'abstract', 'sections', 'word_count'],
  properties: { path: { type: 'string' }, title: { type: 'string' }, abstract: { type: 'string' }, sections: { type: 'array', items: { type: 'string' } }, word_count: { type: 'integer' } },
}
const writePrompt = [
  'Write SHARD relativistic-ISP v7 Paper XIX to ' + PAPER + ' (markdown), single-threaded. A MIX paper, honestly graded.',
  'THESIS: the discrete-sealed record substrate has TWO candidate experimental channels. (A) [TESTABLE / NOT-BLIND, but SCALE-GATED] the SEAL-SWERVE -- a Lorentz-invariant covariant momentum-diffusion (inherited from Dowker-Henson-Sorkin) whose diffusion constant is structurally tied to the seal rate sigma (SHARD-specific) but whose absolute magnitude is import-gated (l_step); it is NOT mechanism-blind (continuum QFT has no such diffusion), so it CONSTRAINS sigma*l_step^k against existing heating/cosmic-ray bounds -- the closest SHARD analog of the Testing-ER=EPR-with-Hydrogen argument. (B) [NO-GO / BLIND] the CP-divisible NO-REVIVAL decoherence -- seal-specific but mechanism-blind: it cannot discriminate SHARD from standard QM (both CP-divisible, no revivals), only from revival-exhibiting non-Markovian collapse models. NET: the seal-swerve is the ONLY channel that is both seal-specific AND escapes the Paper-X mechanism-blindness.',
  'SECTIONS: (1) abstract; (2) the two channels and the discrete-sealed substrate (the swerve is geometric/kinematic, the no-revival is thermodynamic/open-system -- different channels, common root); (3) Channel A: the seal-swerve -- the Lorentz-invariant diffusion, the kappa~sigma tie, the weight/scale-gating, the not-blind argument, the bound on sigma*l_step^k; (4) Channel B: the no-revival -- CP-divisibility, the Gaussian onset, the BLP/RHP measure, the honest BLIND verdict + the precise discrimination boundary; (5) the comparison / why the swerve escapes blindness and the no-revival does not; (6) honest scope (inherited vs SHARD-specific; structure vs scale-gated magnitude; testable vs blind); (7) conclusion. Reference the receipts.',
  'INPUTS:',
  'SWERVE: kappa~sigma=' + (sw ? sw.kappa_sigma_relation : '') + ' || scale-gating=' + (sw ? sw.scale_gating : '') + ' || not-blind=' + (sw ? sw.not_blind_argument : '') + ' || heating=' + (sw ? sw.heating_law : '') + ' || bounds=' + (sw ? sw.bounds_constrain : '') + ' || receipt=' + (sw ? (sw.receipt_path + ' pass=' + sw.pass + ' checks=' + sw.n_checks) : '') + ' || caveats=' + (sw ? sw.caveats : ''),
  'NO-REVIVAL: verdict=' + (nr ? nr.verdict : '') + ' || boundary=' + (nr ? nr.discrimination_boundary : '') + ' || escapes=' + (nr ? nr.escape_attempts : '') + ' || BLP/RHP=' + (nr ? nr.blp_rhp : '') + ' || receipt=' + (nr ? (nr.receipt_path + ' pass=' + nr.pass + ' checks=' + nr.n_checks) : '') + ' || caveats=' + (nr ? nr.caveats : ''),
  'LITERATURE: swerve bounds=' + (lit ? lit.swerve_bounds : '') + ' || norevival bounds=' + (lit ? lit.norevival_bounds : '') + ' || constrains SHARD=' + (lit ? lit.what_constrains_shard : '') + ' || sources=' + (lit ? lit.sources.join('; ') : ''),
  'ADVERSARIAL (address these): swerve=' + (adv ? adv.swerve_verdict : '') + ' || norevival=' + (adv ? adv.norevival_verdict : '') + ' || strongest=' + (adv ? adv.strongest_objection : '') + ' || overclaim risks=' + (adv ? adv.overclaim_risks : ''),
  PHYS, STANDING, 'Write the full paper to ' + PAPER + '. Return PAPER_SCHEMA.',
].join('\n')
const paperInfo = await agent(writePrompt, { label: 'write-paper19', phase: 'Write', schema: PAPER_SCHEMA })
log('Wrote ' + paperInfo.title + ' (' + paperInfo.word_count + ' words)')

phase('Review')
const REVIEW_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['referee', 'overall', 'findings', 'one_line'],
  properties: { referee: { type: 'string' }, overall: { type: 'string', enum: ['ACCEPT', 'MINOR_REVISION', 'MAJOR_REVISION', 'REJECT'] },
    findings: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['severity', 'location', 'issue', 'fix'], properties: { severity: { type: 'string', enum: ['CRITICAL', 'MAJOR', 'MINOR', 'NIT'] }, location: { type: 'string' }, issue: { type: 'string' }, fix: { type: 'string' } } } },
    one_line: { type: 'string' } },
}
const FIX_SCHEMA = { type: 'object', additionalProperties: false, required: ['changes_made', 'opens_investigated', 'receipts_rerun', 'rebuttals', 'remaining'], properties: { changes_made: { type: 'array', items: { type: 'string' } }, opens_investigated: { type: 'array', items: { type: 'string' } }, receipts_rerun: { type: 'array', items: { type: 'string' } }, rebuttals: { type: 'array', items: { type: 'string' } }, remaining: { type: 'string' } } }
const REF = [
  ['R1-physics-swerve', 'Attack Channel A (the seal-swerve). Is the Lorentz-invariant diffusion correct (the unique LI diffusion on the mass shell)? Is the kappa~sigma tie a genuine derivation or hand-waving -- and is it honestly flagged as structural-relation + scale-gated-magnitude? Is the NOT-blind claim sound (does any conventional/continuum effect mimic a covariant momentum-diffusion)? Re-run p19a_seal_swerve.py. Flag any numerical-prediction overclaim (the magnitude is imported).'],
  ['R2-physics-norevival', 'Attack Channel B (no-revival). Is the BLIND verdict correct, or is there an escape the probe missed (multi-time, weak-measurement, state-dependent)? Is the discrimination boundary (vs revival-models, NOT vs QM) stated honestly? Does the paper avoid implying the no-revival beats QM? Re-run p19b_norevival_blindness.py. Confirm CP-divisibility/no-revival monotonicity and N=0-for-both.'],
  ['R3-precision', 'Verify FULL PRECISION: every numeric at mpmath dps>=120, structure sympy-exact, no float64 for cancellation-heavy quantities. Re-run both receipts; confirm every number in the paper traces to a receipt at the stated dps. Flag any precision slip or untraceable number.'],
  ['R4-scope-cite', 'Enforce honest MIX scoping (inherited DHS swerve vs SHARD-specific seal-tie vs scale-gated magnitude vs blind no-revival) and single-threaded style. Verify citations (DHS 2004, PDS 2009, Kaloper-Mattingly, Gran Sasso 2021, BLP/RHP, paper56, paperX) are correct and not invented.'],
]
let round = 0, terminal = false, last = null
while (round < 3 && !terminal) {
  round++
  const reviews = (await parallel(REF.map(rf => () =>
    agent(['You are hostile referee ' + rf[0] + ' for SHARD v7 Paper XIX at ' + PAPER + '. READ it from disk first. ' + rf[1], 'You may read/run receipts in ' + CODE + ' and grep the corpus under ' + V6 + ' and ' + V7 + '. Be adversarial but fair; CRITICAL/MAJOR only for genuine physics errors, overclaims, precision slips, or bad citations.', PHYS, 'Return REVIEW_SCHEMA.'].join('\n'),
      { label: rf[0] + '-r' + round, phase: 'Review', schema: REVIEW_SCHEMA })
  ))).filter(Boolean)
  last = reviews
  const blocking = []
  for (const r of reviews) for (const f of r.findings) if (f.severity === 'CRITICAL' || f.severity === 'MAJOR') blocking.push({ referee: r.referee, severity: f.severity, location: f.location, issue: f.issue, fix: f.fix })
  log('Review r' + round + ': ' + reviews.map(r => r.overall).join(',') + ' | ' + blocking.length + ' blocking')
  if (blocking.length === 0) { terminal = true; break }
  const fixLines = blocking.map((f, i) => (i + 1) + '. [' + f.severity + '] (' + f.referee + ' @ ' + f.location + ') ' + f.issue + ' >> ' + f.fix).join('\n')
  const fix = await agent(['You are the author revising SHARD v7 Paper XIX at ' + PAPER + '. For each CRITICAL/MAJOR finding: if it opens a genuine PHYSICS question, INVESTIGATE it (run a quick receipt check / derivation) BEFORE resolving -- do not hand-wave. Then fix the paper/receipt (re-run), or rebut with evidence. Keep the honest MIX scope (swerve testable-but-scale-gated; no-revival blind), full precision (dps>=120), single-threaded.', 'FINDINGS:', fixLines, PHYS, STANDING, 'Edit in place. Return FIX_SCHEMA (opens_investigated = the physics opens you actually probed).'].join('\n'),
    { label: 'fix-r' + round, phase: 'Review', schema: FIX_SCHEMA })
  log('Fix r' + round + ': ' + fix.changes_made.length + ' changes, ' + fix.opens_investigated.length + ' opens investigated, ' + fix.rebuttals.length + ' rebuttals')
}
return { paper: paperInfo.path, title: paperInfo.title, terminal: terminal, rounds: round,
  swerve: sw ? { pass: sw.pass, kappa_sigma: sw.kappa_sigma_relation } : null,
  norevival: nr ? { verdict: nr.verdict, boundary: nr.discrimination_boundary } : null,
  final: last ? last.map(r => ({ referee: r.referee, overall: r.overall, one_line: r.one_line })) : null }
