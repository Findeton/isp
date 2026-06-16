export const meta = {
  name: 'review-v7-paper8-matter-round2-confirming',
  description: 'Round-2 CONFIRMING review of v7 Paper VIII (matter sector / mode wall) verifying the round-1 fixes hold and opened no new defect. FIX 1 (was MAJOR, math+faithfulness): the false/superseded oriented prefactor "c approx 0.27" is DROPPED; sec 3 now states the receipt-supported numbers -- successive minimum ratios m(n)/m(n+1) = 2.069, 2.033, 2.016 (approaching 2 from above) and m(n)*2^n approx 1.0 slowly decreasing (1.07->1.01), so the oriented minima fall at least as fast as 2^-n with prefactor near 1, asymptotics O2-open, NO prefactor/closed-law claimed. Confirm the numbers match the m1 receipt and no superseded value remains. FIX 2 (was minor framing): "fifth l_step-type wall" now clarified as the same SHAPE as the scale no-go but with a DISTINCT missing input (the canonical MODE, not a length) -- in abstract, sec 4, claim (3). FIX 3 (was minor): the orphan Barandes reference (never cited in body) is DROPPED. RUN m1/m2. Final sweep: the theorem(gapped W=0.156109200157240, three-roles<1e-40)/conjecture(gapless 2^-n exact n=3,4) split still crisp; the gauge-inequivalence fifth-wall (ranks 1/3/7 superselection sectors, all 3 routes fail) intact; the FORM-ONLY hierarchy (1/N, one calibration = Paper V) + NO mass ratio (doubly gated) intact; NO mass prediction manufactured; pre-geometric (no continuum field/spinor/mass scale as INPUT), single-threaded, faithfulness to Levin-Wen / Wen-PSG / Nielsen-Ninomiya / Ginsparg-Wilson / Wen-1305.1045 / Sakharov-Dvali and v6 papers 7/8/9/14.',
  phases: [{ title: 'Review', detail: '3 referees confirming Paper VIII fixes' }],
}

const P8 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper8-matter-sector-mode-wall.md'
const P3 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper3-seal-spacing-no-go.md'
const P8v6 = '/Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper8.md'
const PLAN = '/Users/felixrobles/workspace/isp/v7/LONG_MARCH_PLAN.md'
const M1 = '/Users/felixrobles/workspace/isp/v7/code/v7_m1_psg_gap_chiral_receipt.py'
const M2 = '/Users/felixrobles/workspace/isp/v7/code/m2_mode_canonicalization.py'

const RULES = `
Confirm the three round-1 fixes are correctly integrated and opened NO new defect. Enforce: pre-geometric discipline (every quantity a record-internal evidence content / character-ledger rank / lattice index; NO continuum field/spinor bundle/mass scale as a derivation INPUT), high precision (RUN python3 ${M1} , ${M2} ; if mpmath missing use /Users/felixrobles/workspace/isp/code/.venv/bin/python -- reproduce: W=eta*theta-log cosh eta=0.156109200157240, the three roles <1e-40, the commitment cubic, the oriented minima m(3)=0.133531/m(4)=0.064539/m(5)=0.031749/m(6)=0.015748 and their ratios m(n)/m(n+1) = 2.069/2.033/2.016 + m(n)*2^n approx 1.07->1.01; the dilution ladder 0.609>0.495>0.368, the xi=1/eta tautology, ranks [1,3,7]), single-threaded (no round/version narration; bare date stamp OK; AND no content-level re-import of a source-SUPERSEDED number), BOTH-direction honesty.
SPECIFIC CONFIRMATIONS:
- FIX 1 (THE BIG ONE): is "c approx 0.27" fully GONE? Does sec 3 now state ONLY receipt-supported numbers (ratios 2.069/2.033/2.016 approaching 2 from above; m(n)*2^n approx 1.0 slowly decreasing 1.07->1.01; falls at least as fast as 2^-n, prefactor near 1; asymptotics O2-open; n5/n6 sampled UBs)? Cross-check every number against the m1 receipt. Confirm NO superseded/false value remains and the ratio pairing is unambiguous (the receipt's '1.169' is the W->n3 step, distinct from the oriented m(n)/m(n+1) ratios).
- FIX 2: is the "fifth wall" now framed as the same SHAPE as the l_step scale no-go but with a DISTINCT missing input (the canonical MODE, not a length / scale), in abstract + sec 4 + claim (3)? Not conflating shape with the literal scale?
- FIX 3: is the orphan Barandes reference dropped, and do all remaining references resolve to in-text anchors?
- Did the edits introduce any NEW defect or inconsistency? Confirm intact: the theorem(gapped)/conjecture(gapless) split crisp; the gauge-inequivalence fifth-wall decisive (ranks 1/3/7, all 3 routes fail); the FORM-ONLY hierarchy + NO-mass-ratio-doubly-gated; NO manufactured mass prediction; all 5 disavowals (no mass/ratio; no finished biconditional; no PSG group derived; no chirality bridge; no fixed count N).
Read companion Paper III ${P3}, v6 paper8 ${P8v6}, and the plan ${PLAN}.
`

const SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['focus', 'verdict', 'fixes_confirmed', 'must_fix', 'overclaims', 'new_problems_introduced', 'single_threaded_violations', 'summary'],
  properties: {
    focus: { type: 'string' },
    verdict: { type: 'string', enum: ['accept', 'minor-revision', 'major-revision', 'reject'] },
    fixes_confirmed: { type: 'array', items: { type: 'string' } },
    must_fix: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['issue', 'where', 'severity', 'fix'], properties: { issue: { type: 'string' }, where: { type: 'string' }, severity: { type: 'string', enum: ['minor', 'major', 'critical'] }, fix: { type: 'string' } } } },
    overclaims: { type: 'array', items: { type: 'string' } },
    new_problems_introduced: { type: 'array', items: { type: 'string' } },
    single_threaded_violations: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
}

phase('Review')
const reviews = await parallel([
  ['FIX 1 (the oriented prefactor, sec 3) -- THE LOAD-BEARING math/faithfulness fix. RUN m1. Confirm "c approx 0.27" is fully GONE and sec 3 now states ONLY receipt-supported numbers: successive minimum ratios m(n)/m(n+1) = 2.069, 2.033, 2.016 (approaching 2 FROM ABOVE), m(n)*2^n approx 1.0 slowly decreasing (1.07 -> 1.01), oriented minima fall at least as fast as 2^-n with prefactor near 1, asymptotics O2-open, n5/n6 sampled UBs, NO prefactor/closed-law claimed. Cross-check EVERY number against the m1 receipt output. Confirm no superseded value remains and the ratio pairing is unambiguous (the receipt prints W->n3 = 1.169 distinct from the oriented m(n)/m(n+1)). Confirm the theorem(gapped W)/conjecture(gapless) split is still crisp.'],
  ['FIX 2 (the fifth-wall framing, sec 4 + abstract + claim 3) + PART B integrity. RUN m2. Confirm "fifth wall" is now the same SHAPE as the l_step scale no-go but with a DISTINCT missing input (the canonical MODE, not a length), not conflating shape with the literal scale. Confirm the gauge-inequivalence diagnosis is intact and decisive (ranks 1/3/7 invariant => distinct superselection sectors; all 3 routes fail: completeness pushes down the dilution ladder 0.609>0.495>0.368; xi=1/eta tautology + mode-covariant; variational opposite + clock mode-blind E[I]=1; skewed base 0.526>W_*). Did the framing edit introduce any inconsistency between abstract/sec4/claim3?'],
  ['FIX 3 (orphan Barandes ref dropped) + FINAL SWEEP both directions + discipline (secs 1,5,6,7,8,9 + coherence). Confirm the Barandes reference is dropped and all remaining references resolve to in-text anchors. Confirm intact: the FORM-ONLY hierarchy (sec 5: 1/N mode-count, count not corpus-forced ~37 orders short, one calibration = Paper V) NOT smuggled into a value; "no single mass ratio computable now, doubly gated" (sec 6); all 5 disavowals (no mass/ratio prediction; no finished massless-iff biconditional; no PSG group H1(SG,IGG) derived; no ledger-chirality<->Weyl-chirality bridge; no fixed count N). NO mass prediction manufactured anywhere. Pre-geometric (no continuum field/spinor/mass scale as INPUT); single-threaded (no narration; no content-level re-import of a superseded number now that FIX 1 is in); abstract<->body<->claims coherent. Hunt any new or residual overclaim/inconsistency.'],
].map(([f]) => () => agent(
  `Round-2 CONFIRMING hostile review of v7 Paper VIII at ${P8}. Your focus: ${f}\n${RULES}\nReturn the schema (fixes_confirmed = which round-1 fixes you verified; new_problems_introduced = anything the edits broke).`,
  { label: `P8r2:${f.slice(0, 22)}`, phase: 'Review', schema: SCHEMA }
)))

return { reviews }
