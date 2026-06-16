export const meta = {
  name: 'moveB-three-walls-classification',
  description: 'SHARD v7 Paper XVII (Move B): the flagship classification theorem. The three record-blind inputs (scale, tensor product, mode) are ONE no-go SHAPE: a self-consistency principle invariant under an internal symmetry fixes the orbit (form/envelope/ratios), and the orbit PARAMETER is the record-blind residual each time, with three DIFFERENT residual types and epistemic statuses.',
  phases: [
    { title: 'Investigate', detail: 'formalize the common shape as a quotient-by-symmetry classification; build the unifying receipt; epistemic grading + the Jacobson-conditional caveat on G; position vs the reconstruction literature' },
    { title: 'Write', detail: 'single-threaded classification-theorem paper' },
    { title: 'Review', detail: 'hostile referees -> fix -> terminal' },
  ],
}

const V6 = '/Users/felixrobles/workspace/isp/v6'
const V7 = '/Users/felixrobles/workspace/isp/v7'
const CODE = '/Users/felixrobles/workspace/isp/v7/code'
const PAPER = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper17-three-walls-classification-theorem.md'

const SHAPE = [
  'THE COMMON NO-GO SHAPE to formalize precisely (this is a CLASSIFICATION THEOREM, not a survey):',
  'Each of the three record-blind inputs is an instance of ONE structure: a self-consistency principle is INVARIANT under an internal symmetry group G_i; the records see only the G_i-ORBIT (the equivalence class / the form / the envelope / the ratios); the one datum the records cannot supply is the ORBIT PARAMETER (the position within the orbit) = the record-blind residual. The three instances:',
  '(1) SCALE: symmetry = the length-relabeling automorphism g_lambda (l_step -> mu*l_step); the invariants are exactly the weight-0 record functionals (paper6 Theorem G); the residual = the absolute length / scale, a positive real R_+ (=l_step, hence Newton G, the seal spacing d, the matter c_m, the metric, the 4-volume unit). CONTINUOUS residual.',
  '(2) TENSOR PRODUCT: symmetry = the field-reduction R (qubit-pair <-> rebit-pair, complex<->real); the invariant is the moment algebra M (level-(1+AB) moments {1,A_x,B_y,A_xB_y}); records factor through M (paper12 M2 field-blindness); the residual = the local-tomography / complex-over-real bit (K_AB - K_A*K_B: +1 real / 0 complex), in ker R, equivalently the Q-vs-Q-tilde tensor-product choice. DISCRETE (binary) residual.',
  '(3) MODE: symmetry = the gauge-inequivalent superselection-sector relabeling (each sector measured vs its OWN reference; no common energy zero); the invariant is the within-sector spectrum / the ledger rank 2^n-1; the residual = the cross-sector canonical-mode / which-mass-is-which label (paper8/paper14). DISCRETE (label) residual.',
  'THE THEOREM: records carry exactly the G_i-invariants (everything relative/weight-0) and are blind to exactly the orbit parameter; self-consistency fixes the fence (the orbit), never the filling (the parameter). The three are the SAME shape with residuals of different TYPE and different EPISTEMIC STATUS.',
  'EPISTEMIC STATUSES (the Move-A revision): (1) scale/G genuinely MEASURED (an experimental datum) BUT the SHARD route to it via the entropic equation of state is CONDITIONAL on the Jacobson-Clausius premise (cf. Visser, Why gravity is not an entropic force) -- so the G leg is honestly a CONDITIONAL no-go, two structural + one conditional; (2) mode/masses IMPORT-FIXED by measured spectra; (3) tensor product a NOW-CONTESTED composition-rule / local-tomography convention possibly experimentally unfixable (Hoffreumon-Woods arXiv:2603.19208, Maioli arXiv:2604.19482; Renou Comment arXiv:2604.07425; Renou 2021 Nature 600 625 stands in its framing).',
].join('\n')

const STANDING = [
  'STANDING CONSTRAINTS:',
  '- SINGLE-THREADED: reads as written once. NO round/version/referee/revision/campaign narration. Date stamp 2026-06-16 only.',
  '- HIGH PRECISION: the unifying receipt at sympy-exact / mpmath dps>=100; reuse + cross-check the existing receipts (paper6 weight grading, p6_transverse_nogo.py M-invariance, m1/m2 mode rank). Re-run, do not trust. Flag SDP digits.',
  '- HONEST: this is CONSOLIDATION/positioning, not new heavy mathematics. The individual walls are mostly convergent-not-novel (the reconstruction field independently treats G as un-derivable, local tomography as the least-motivated axiom selecting complex-over-real, and mass spectra as measured). SHARD novelty = the UNIFICATION into one quotient-by-symmetry SHAPE + the three-epistemic-status grading. Do NOT claim to own the undecidability math (MIP*=RE / Slofstra) or the local-tomography-least-motivated lineage (Hardy / Barnum-Mueller-Ududec / Hoehn).',
  '- The G leg is CONDITIONAL on the Jacobson premise; state it as such (two structural no-gos + one conditional), do not overclaim it as unconditional.',
].join('\n')

const CONTEXT = [
  'SHARD context: the record click-law (v7 Papers I-XVI). Meta-result: records carry everything relative/weight-0, barred from three last inputs (scale, tensor product, mode). Paper XVI established the three have DIFFERENT epistemic statuses. Foundations: paper6 (g_lambda relabeling automorphism + Theorem G: intrinsic readout => g_lambda-invariant => weight-0); paper12 (Gamma>=0 / moment algebra M / field-reduction R / M1 capacity blindness + M2 field blindness; K_AB-K_A*K_B = +1 real / 0 complex); paper8 + paper14 (mode = superselection sectors, ledger rank 2^n-1, no common energy zero); paper57 + companion-G (the G / l_step scale no-go, kappa*sigma_A const, G*Lambda^2 const).',
  'Existing receipts to reuse/cross-check in ' + CODE + ': p6_transverse_nogo.py (M-invariance, weight), m1/m2 receipts (mode rank), and the v6 weight-grading receipts.',
].join('\n')

phase('Investigate')

const FORMAL_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['receipt_path', 'receipt_pass', 'n_checks', 'common_structure', 'instances', 'precision', 'caveats'],
  properties: {
    receipt_path: { type: 'string' }, receipt_pass: { type: 'boolean' }, n_checks: { type: 'integer' },
    common_structure: { type: 'string' },
    instances: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['wall', 'symmetry', 'invariant', 'residual', 'residual_type'], properties: { wall: { type: 'string' }, symmetry: { type: 'string' }, invariant: { type: 'string' }, residual: { type: 'string' }, residual_type: { type: 'string' } } } },
    precision: { type: 'string' }, caveats: { type: 'string' },
  },
}
const EPI_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['scale_status', 'mode_status', 'tensor_status', 'jacobson_conditional', 'honest_headline'],
  properties: { scale_status: { type: 'string' }, mode_status: { type: 'string' }, tensor_status: { type: 'string' }, jacobson_conditional: { type: 'string' }, honest_headline: { type: 'string' } },
}
const LIT_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['what_is_convergent', 'what_is_novel', 'what_not_owned', 'positioning'],
  properties: { what_is_convergent: { type: 'string' }, what_is_novel: { type: 'string' }, what_not_owned: { type: 'string' }, positioning: { type: 'string' } },
}

const pFormal = [
  'FORMALIZE the common no-go shape as a CLASSIFICATION THEOREM and build a unifying receipt at ' + CODE + '/p17_classification.py (sympy-exact / mpmath dps>=120).',
  'For EACH of the three walls, instantiate the triple (internal symmetry G_i, the invariant the records carry, the residual orbit-parameter the records are blind to) and VERIFY the invariance + the residual identification, reusing and cross-checking the existing receipts.',
  'Concretely: (1) SCALE: verify g_lambda(weight-0 functional)=identity and g_lambda(absolute length)=mu*(length) (sympy-exact; the residual is the orbit param R_+). (2) TENSOR: verify the moment algebra M is invariant under the field-reduction R while the local-tomography count K_AB-K_A*K_B flips (+1 real / 0 complex) (reuse p6_transverse_nogo.py PART 4 numbers: K_single R=3 C=4, K_AB 2rebit=10 2qubit=16; residual = the binary bit in ker R). (3) MODE: verify the within-sector spectrum is sector-relative (the cross-sector shift (n-prime - n)*ln2 is state-independent, H(P) cancels) and the residual = the rank/mode label (reuse the m1/m2 mode-rank facts; rank 2^n-1).',
  'STATE the common structure precisely: records = the G_i-invariants; blind to the orbit parameter; self-consistency fixes the orbit (fence) never the parameter (filling). The three differ in residual TYPE (continuous R_+ / discrete bit / discrete label).',
  'Aim for 15+ checks. Print ALL CHECKS PASS (k/k). Be honest in caveats about what is genuinely a theorem vs a structural analogy.',
  SHAPE, STANDING, CONTEXT, 'Return FORMAL_SCHEMA. Final message is data.',
].join('\n')

const pEpi = [
  'EPISTEMIC-GRADING task. Articulate the three residuals epistemic statuses precisely and the Jacobson-conditional caveat on the scale/G leg.',
  '(1) SCALE/G: the residual (absolute length / Newton G) is genuinely MEASURED. BUT the SHARD derivation that G is record-un-derivable rides the entropic equation-of-state route (Jacobson Clausius dQ=TdS => Einstein form), which carries the Jacobson premise; cite Visser Why gravity is not an entropic force as the live critique. So the G LEG of the classification is honestly a CONDITIONAL no-go (conditional on the Jacobson-Clausius premise + the three paper57 conditionals: axiom R beta=2pi, local-equilibrium theta=sigma=0, the focusing gate). State the honest headline: TWO structural no-gos (tensor, mode) + ONE conditional (scale).',
  '(2) MODE/masses: import-fixed by measured spectra (genuinely measured).',
  '(3) TENSOR PRODUCT: a now-contested composition-rule / local-tomography convention possibly experimentally unfixable (Hoffreumon-Woods arXiv:2603.19208; Maioli arXiv:2604.19482; Renou Comment arXiv:2604.07425; Renou 2021 stands in its framing). Balanced, live, never Renou is wrong.',
  'Deliver each status + the jacobson_conditional caveat + the honest_headline (one shape three times; three residual types; three epistemic statuses; two structural + one conditional).',
  SHAPE, CONTEXT, 'Return EPI_SCHEMA. Final message is data.',
].join('\n')

const pLit = [
  'LITERATURE-POSITIONING task. The three walls individually are mostly CONVERGENT with how the foundations/quantum-gravity field already treats these inputs; the SHARD novelty is the UNIFICATION + the epistemic grading. State precisely:',
  '- CONVERGENT (not SHARD-novel): G as un-derivable from within (general in quantum gravity / entropic gravity); local tomography as the least-motivated reconstruction axiom that selects complex over real (Hardy 2001; Barnum-Mueller-Ududec; Hoehn; Masanes-Mueller); mass spectra as measured inputs (the Standard Model has ~19+ measured parameters).',
  '- NOVEL (SHARD): the proof that these three are ONE quotient-by-internal-symmetry SHAPE (self-consistency fixes the orbit, never the parameter), with the records carrying exactly the invariants; PLUS the three-epistemic-status grading (measured / contested-convention / import-fixed); PLUS the un-forceability-of-the-filling no-go for the tensor leg (Papers XII/XIII).',
  '- NOT OWNED: the undecidability math (MIP*=RE, Slofstra 2019) is imported; the local-tomography-least-motivated lineage predates SHARD; the entropic-gravity G argument is field-shared and Jacobson-premise-conditional.',
  'Deliver the positioning honestly (a classification/structural-unification result, not new foundational mathematics).',
  SHAPE, CONTEXT, 'Return LIT_SCHEMA. Final message is data.',
].join('\n')

const inv = await parallel([
  () => agent(pFormal, { label: 'formalize-classification', phase: 'Investigate', schema: FORMAL_SCHEMA }),
  () => agent(pEpi, { label: 'epistemic-grading', phase: 'Investigate', schema: EPI_SCHEMA }),
  () => agent(pLit, { label: 'literature-positioning', phase: 'Investigate', schema: LIT_SCHEMA }),
])
const formal = inv[0], epi = inv[1], lit = inv[2]
log('Investigate: receipt_pass=' + (formal ? formal.receipt_pass : 'NULL') + ' n_checks=' + (formal ? formal.n_checks : 0))

phase('Write')
const PAPER_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['path', 'title', 'abstract', 'sections', 'word_count'],
  properties: { path: { type: 'string' }, title: { type: 'string' }, abstract: { type: 'string' }, sections: { type: 'array', items: { type: 'string' } }, word_count: { type: 'integer' } },
}
const instDigest = formal ? formal.instances.map(i => '  - ' + i.wall + ': symmetry=' + i.symmetry + ' | invariant(records)=' + i.invariant + ' | residual=' + i.residual + ' [' + i.residual_type + ']').join('\n') : ''
const writePrompt = [
  'Write SHARD relativistic-ISP v7 Paper XVII to ' + PAPER + ' (markdown), single-threaded. A flagship CLASSIFICATION THEOREM (consolidation), not a survey.',
  'THESIS: the records three blind inputs (scale, tensor product, mode) are ONE no-go SHAPE -- a self-consistency principle invariant under an internal symmetry fixes the orbit (the form/envelope/ratios), and the orbit PARAMETER is the record-blind residual each time -- with three different residual TYPES (continuous scale / binary tensor bit / discrete mode label) and three different EPISTEMIC STATUSES (scale measured but Jacobson-conditional; mode import-fixed; tensor a contested composition convention). Headline: one shape three times = TWO structural no-gos + ONE conditional, three epistemic statuses.',
  'SECTIONS: (1) abstract; (2) the common structure stated as a theorem (the quotient-by-internal-symmetry schema: records = G-invariants, blind to the orbit parameter, self-consistency fixes the fence never the filling); (3) the three instances as a table (symmetry / invariant=records / residual / type), each with its receipt + key numbers (p17_classification.py); (4) the three epistemic statuses + the Jacobson-conditional caveat on the G leg (two structural + one conditional); (5) positioning vs the reconstruction literature (convergent individually, novel in the unification + grading); (6) what SHARD does not own; (7) conclusion. Include the unifying receipt result.',
  'INSTANCES TABLE INPUT:',
  instDigest,
  'COMMON STRUCTURE: ' + (formal ? formal.common_structure : ''),
  'RECEIPT: ' + (formal ? (formal.receipt_path + ' pass=' + formal.receipt_pass + ' checks=' + formal.n_checks + ' precision=' + formal.precision) : ''),
  'EPISTEMIC: scale=' + (epi ? epi.scale_status : '') + ' || mode=' + (epi ? epi.mode_status : '') + ' || tensor=' + (epi ? epi.tensor_status : '') + ' || jacobson=' + (epi ? epi.jacobson_conditional : '') + ' || headline=' + (epi ? epi.honest_headline : ''),
  'POSITIONING: convergent=' + (lit ? lit.what_is_convergent : '') + ' || novel=' + (lit ? lit.what_is_novel : '') + ' || not-owned=' + (lit ? lit.what_not_owned : '') + ' || ' + (lit ? lit.positioning : ''),
  SHAPE, STANDING, CONTEXT, 'Write the full paper to ' + PAPER + '. Return PAPER_SCHEMA.',
].join('\n')
const paperInfo = await agent(writePrompt, { label: 'write-paper17', phase: 'Write', schema: PAPER_SCHEMA })
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
  ['R1-overclaim', 'Hunt overclaiming. Is this honestly framed as CONSOLIDATION (one-shape unification + epistemic grading), NOT as new foundational mathematics or as deriving any of the three inputs? Is the G leg correctly CONDITIONAL on the Jacobson premise (two structural + one conditional, not three unconditional)? Is the tensor leg balanced (contested, not Renou-wrong)? Is the literature convergence honestly admitted and SHARD novelty confined to the unification + grading? Does it falsely claim to own MIP*=RE / local-tomography-least-motivated?'],
  ['R2-theorem', 'Attack the CLASSIFICATION THEOREM. Is each wall genuinely an instance of quotient-by-internal-symmetry with the residual = orbit parameter, or is the unification a loose analogy dressed as a theorem? Check each triple (symmetry/invariant/residual) is faithful to the cited receipts (paper6 g_lambda; p6 M-invariance + K_AB flip; m1/m2 mode rank). Re-run ' + CODE + '/p17_classification.py. Flag any instance where the schema does not actually fit.'],
  ['R3-precision', 'Verify every number in the paper traces to a receipt and matches. Re-run p17_classification.py and the cross-checked receipts (p6_transverse_nogo.py PART 4 K-counts 3/4/10/16; the mode rank 2^n-1; the weight grading). Confirm sympy-exact where claimed, SDP/numeric flagged. Flag any untraceable or mismatched number.'],
  ['R4-style-cite', 'Enforce single-threaded style (no round/version/campaign narration; dateline only). Verify all arXiv/lit citations (2603.19208, 2604.19482, 2604.07425, Renou 2021 Nature 600 625; Hardy 2001; Visser entropic-force critique; MIP*=RE/Slofstra 2019) are correctly attributed and not invented. Confirm the three-status table is internally consistent.'],
]
let round = 0, terminal = false, last = null
while (round < 3 && !terminal) {
  round++
  const reviews = (await parallel(REF.map(rf => () =>
    agent(['You are hostile referee ' + rf[0] + ' for SHARD v7 Paper XVII at ' + PAPER + '. READ it from disk first. ' + rf[1], 'You may read/run receipts in ' + CODE + ' and grep the corpus. Be adversarial but fair; CRITICAL/MAJOR only for genuine errors/overclaims/unfaithful citations or a unification that is mere analogy.', SHAPE, 'Return REVIEW_SCHEMA.'].join('\n'),
      { label: rf[0] + '-r' + round, phase: 'Review', schema: REVIEW_SCHEMA })
  ))).filter(Boolean)
  last = reviews
  const blocking = []
  for (const r of reviews) for (const f of r.findings) if (f.severity === 'CRITICAL' || f.severity === 'MAJOR') blocking.push({ referee: r.referee, severity: f.severity, location: f.location, issue: f.issue, fix: f.fix })
  log('Review r' + round + ': ' + reviews.map(r => r.overall).join(',') + ' | ' + blocking.length + ' blocking')
  if (blocking.length === 0) { terminal = true; break }
  const fixLines = blocking.map((f, i) => (i + 1) + '. [' + f.severity + '] (' + f.referee + ' @ ' + f.location + ') ' + f.issue + ' >> ' + f.fix).join('\n')
  const fix = await agent(['You are the author revising SHARD v7 Paper XVII at ' + PAPER + '. Resolve each CRITICAL/MAJOR finding (fix the paper or a receipt, or rebut with evidence). Keep single-threaded; keep it framed as consolidation (not new math); keep the G leg Jacobson-conditional; keep the tensor leg balanced; do not claim to own the undecidability math. If the classification is challenged as analogy, either tighten it to a genuine quotient-by-symmetry statement with the receipt, or scope the claim honestly.', 'FINDINGS:', fixLines, SHAPE, STANDING, 'Edit in place. Return FIX_SCHEMA.'].join('\n'),
    { label: 'fix-r' + round, phase: 'Review', schema: FIX_SCHEMA })
  log('Fix r' + round + ': ' + fix.changes_made.length + ' changes, ' + fix.rebuttals.length + ' rebuttals')
}
return { paper: paperInfo.path, title: paperInfo.title, terminal: terminal, rounds: round,
  receipt: formal ? { path: formal.receipt_path, pass: formal.receipt_pass, checks: formal.n_checks } : null,
  final: last ? last.map(r => ({ referee: r.referee, overall: r.overall, one_line: r.one_line })) : null }
