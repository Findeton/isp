export const meta = {
  name: 'review-v7-paper9-round2-confirming',
  description: 'Round-2 CONFIRMING review of v7 Paper IX (closed chiral-gap law + PSG-ingredient functor + two chirality no-gos), verifying the round-1 fixes hold and opened no new defect. FIX 1 (the main one): the n=4 global-optimality is now EXHAUSTIVE -- receipt p9a runs all 2^15=32768 orientation classes at n=4 (not a random challenge), confirming alternating-by-weight is the global minimum (= closed form 0.064538521138); the paper now says "exhaustively brute-forced through n=4" consistently in abstract/sec2/sec7/sec8. FIX 2 (cross-paper): the H1/H2 cohomology-degree inconsistency is resolved -- Paper VIII now uses H^2(SG,IGG) (the correct extension-class degree, matching Paper IX). FIX 3 (receipt): p9c checks (4)/(4b) were hardcoded tautologies -> demoted to PROSE; the genuine machine checks are now (1) layer structure, (2)/(2b) handedness-blindness, (3) parity-invariance. FIX 4 (single-threaded): dropped "previously a sampled bound" and "superseded 0.27 first-edition fit" (revision-history narration); n=5 qualified as "the closed-form value / exact given the lemma"; the split-extension framing now rests the no-go on "no space group => no H^2 content" (split noted as by-construction); parity-invariance noted as structurally automatic. RUN all 3 receipts p9a/p9b/p9c (note p9a now takes ~7s for the exhaustive n=4). Final sweep: the closed gap THEOREM (two-value identity, m_hat_min=-ln(1-2^-n)-delta_n, anchors at dps130, asymptotically gapless, prefactor 1) intact and correctly graded theorem-mod-finite-lemma; the two NO-GOs (no Wen-PSG without geometry; no record-forced chirality bridge) faithful and not overclaimed; NO mass prediction; pre-geometric, single-threaded, faithfulness to Wen PSG cond-mat/0107071 / Griffiths-Toulouse / v6 papers 7/8/9/14 + v7 III/VIII.',
  phases: [{ title: 'Review', detail: '3 referees confirming Paper IX fixes' }],
}

const P9 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper9-chiral-gap-and-chirality-nogos.md'
const P8v7 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper8-matter-sector-mode-wall.md'
const P8v6 = '/Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper8.md'
const PLAN = '/Users/felixrobles/workspace/isp/v7/LONG_MARCH_PLAN.md'
const RA = '/Users/felixrobles/workspace/isp/v7/code/p9a_chiral_gap_closed.py'
const RB = '/Users/felixrobles/workspace/isp/v7/code/p9b_psg_ingredient_functor.py'
const RC = '/Users/felixrobles/workspace/isp/v7/code/p9c_chirality_bridge_nogo.py'

const RULES = `
Confirm the four round-1 fixes are correctly integrated and opened NO new defect. Enforce: pre-geometric discipline (every quantity a record-internal code / character / finite group / KL gap; the ABSENT space group / fiber-handedness map appear only as no-go content), high precision (RUN python3 ${RA} , ${RB} , ${RC} ; if mpmath/numpy missing use /Users/felixrobles/workspace/isp/code/.venv/bin/python -- note p9a now runs the EXHAUSTIVE n=4 over all 32768 orientations, ~7s; reproduce: the two-value identity T(s) in {-(2^n-1),+1}, the closed form vs anchors n=3,4,5, the n=2/3/4 exhaustive global min = closed form, 168=GL(3,2), the gap as a pure function of sigma + parity-invariance), single-threaded (NO 'previously/superseded/first-edition/we now/round N/version N' narration; bare date stamp OK), BOTH-direction honesty.
SPECIFIC CONFIRMATIONS:
- FIX 1: is the n=4 global-optimality now EXHAUSTIVE in receipt p9a (all 32768, not a random sample), and does the paper say "exhaustively brute-forced through n=4" CONSISTENTLY in abstract/sec2/sec7/sec8 (no residual "random-challenged at n=4")? Re-run p9a and confirm the n=4 brute min = closed form 0.064538521138.
- FIX 2: is the H^2(SG,IGG) degree now CONSISTENT between Paper IX (abstract/sec4/sec7/refs) and Paper VIII (sec7/sec8 -- now H^2, no residual H^1)? Is H^2 the correct extension-class degree (1->IGG->PSG->SG->1, abelian kernel)?
- FIX 3: are p9c checks (4)/(4b) now demoted to PROSE (the NO-GO drawn as a logical consequence of the genuine checks 1-3), with no hardcoded-tautology PASS entries? Are the remaining machine checks (handedness-blindness, parity-invariance) genuine computations?
- FIX 4: are the single-threaded slips gone ("previously", "superseded 0.27 first-edition fit")? Is n=5 now honestly qualified (closed-form value / exact given the lemma, not unconditionally "exact")? Does the split-extension framing now rest the no-go on "no space group => no H^2 content" (split = by-construction, not a discovered proof step)? Is parity-invariance noted as structurally automatic?
- Any NEW defect/inconsistency introduced by the edits? Confirm intact: the closed gap THEOREM correctly graded (theorem mod a finite global-optimality lemma, now exhaustive through n=4); the two NO-GOs faithful (no Wen-PSG without geometry; chirality bridge not record-forced) and correctly credited as PROGRESS (1 conjecture closed + 2 proved no-gos); NO mass/ratio predicted; all disavowals present (sec 6-7).
Read companion Paper VIII ${P8v7}, v6 paper8 ${P8v6}, and the plan ${PLAN}.
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
  ['FIX 1 + the closed gap THEOREM (sec 2). RUN p9a (note ~7s for exhaustive n=4). Confirm the n=4 brute force is now EXHAUSTIVE over all 32768 orientation classes (not random), the brute min = closed form 0.064538521138 = alt-by-weight, and the paper says "exhaustively brute-forced through n=4" CONSISTENTLY (abstract, sec2, sec7, sec8 -- no residual "random-challenged"). Re-verify the theorem core: two-value identity T(s), closed form m_hat_min(n)=-ln(1-2^-n)-delta_n vs anchors n=3,4,5, asymptotically-gapless + prefactor-1. Is the grade now consistent and honest (theorem mod a finite global-optimality lemma, exhaustive through n=4; closed form for n>=5)? Is the n=5 wording now honest (closed-form value / exact given the lemma, not unconditional)?'],
  ['FIX 2 + FIX 4(split) + NO-GO 1 (secs 3-4). RUN p9b. Confirm the H^2(SG,IGG) degree is CONSISTENT between Paper IX and Paper VIII (read VIII sec7/sec8 -- no residual H^1) and is the correct extension-class degree. Confirm the split-extension framing now rests the no-go on "no space group => no H^2 content" with split noted as by-construction (not presented as a discovered proof step). Verify 168=GL(3,2) + 1+7+7+1. Is "no Wen-PSG without geometry" still faithful (Wen H^2(SG,IGG), SG=space group) and the PSG-ingredient/Wen-PSG boundary crisp? Any new inconsistency from the reframing?'],
  ['FIX 3 + FIX 4(single-threaded) + NO-GO 2 + final sweep (secs 1,5,6,7,8). RUN p9c. Confirm p9c checks (4)/(4b) are demoted to PROSE (NO hardcoded-tautology PASS entries; the no-go drawn as a logical consequence of the genuine checks), and the remaining machine checks (handedness-blindness, parity-invariance) are real computations. Confirm the single-threaded slips are gone ("previously", "superseded 0.27 first-edition fit") and parity-invariance is noted as structurally automatic. Is NO-GO 2 (chirality bridge not record-forced) still a sound PROVED no-go (handedness-blindness + parity-odd-on-symmetric-data => supplied by g), not overclaimed/understated? Final: NO mass/ratio predicted; all disavowals present (sec 6-7); the progress framing (1 conjecture closed + 2 proved no-gos, matter sector more resolved) correct; pre-geometric; references resolve + faithful. Any residual or newly-introduced overclaim/inconsistency?'],
].map(([f]) => () => agent(
  `Round-2 CONFIRMING hostile review of v7 Paper IX at ${P9}. Your focus: ${f}\n${RULES}\nReturn the schema (fixes_confirmed = which round-1 fixes you verified; new_problems_introduced = anything the edits broke).`,
  { label: `P9r2:${f.slice(0, 22)}`, phase: 'Review', schema: SCHEMA }
)))

return { reviews }
