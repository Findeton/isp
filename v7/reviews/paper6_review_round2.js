export const meta = {
  name: 'review-v7-paper6-transverse-round2-confirming',
  description: 'Round-2 CONFIRMING review of v7 Paper VI (transverse / almost-quantum) verifying the three round-1 fixes hold and opened no new defect. FIX 1 (was major): the exhaustiveness now SEPARATES (C-form) [robust: any record self-consistency principle is a moment-positivity condition] from (C-level) [flagged substrate-modeling PREMISE: a record interface commits a single joint outcome pair => degree-(1,1) cross moments => level 1+AB], AND adds the level-INDEPENDENT fallback (the qualitative gap survives at every finite level: commutation-on-state != tensor-factorization, Tsirelson problem) -- so the headline no-go does NOT depend on (C-level). Confirm (C-level) is tagged a premise not a theorem, and the level-independent no-go is correct. FIX 2 (was minor x2): the "one name" no longer asserts strict equivalence "global tensor product EQUIVALENTLY local tomography"; it now says the records furnish NO COMPOSITE STATE SPACE, hence lack BOTH the tensor product (closes Q-tilde\\Q, t1) AND local tomography (complex-over-real selector, t2) -- two distinct axioms (a rebit HAS a tensor product yet FAILS local tomography), one origin. Confirm this is now correct and not over-identified. FIX 3 (was major): "Tsirelson derived/theorem" is now ANCHORED to the moment-positivity route (Gamma>=0 caps CHSH at 2sqrt2 = a theorem of record self-consistency, t1), with the static IC core demoted to an INDEPENDENT WITNESS (one operational RAC lever short); and the upgrade over Paper IV (respected->inherited) is sourced. Confirm the Tsirelson claim now matches what t1/t3 license and is consistent with Paper IV. RUN all 3 receipts. Final sweep: overclaims BOTH directions, pre-geometric (no composite state space smuggled as INPUT), single-threaded, faithfulness to NGHA 2015 / NPA / Tsirelson-problem / Pawlowski IC / Hardy / Wootters / Papers I/III/IV.',
  phases: [{ title: 'Review', detail: '3 referees confirming Paper VI fixes' }],
}

const P6 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper6-transverse-almost-quantum.md'
const P4 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper4-entanglement-graph-not-metric.md'
const P3 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper3-seal-spacing-no-go.md'
const PLAN = '/Users/felixrobles/workspace/isp/v7/LONG_MARCH_PLAN.md'
const T1 = '/Users/felixrobles/workspace/isp/v7/code/t1_npa_q_vs_qtilde.py'
const T2 = '/Users/felixrobles/workspace/isp/v7/code/t2_purification_uniqueness.py'
const T3 = '/Users/felixrobles/workspace/isp/v7/code/t3_tsirelson_derivation.py'

const RULES = `
Confirm the three round-1 fixes are correctly integrated and opened NO new defect. Enforce: pre-geometric discipline (NO composite state space / Hilbert tensor product smuggled as a derivation INPUT -- its absence IS the result; chains meet ONLY via the shared moment <A_x B_y>), high precision (RUN python3 ${T1} , ${T2} , ${T3} ; if cvxpy/mpmath missing use /Users/felixrobles/workspace/isp/code/.venv/bin/python -- reproduce: NPA-1 CHSH ceiling 2sqrt2 gap 2.78e-10, PR-box infeasible, complex 16=4*4 / rebit 10!=9 deficit 1, field-blindness E=E^2=E* over R and C, chain-rule residual 3.63e-122, IC facet saturating at E=1/sqrt2), single-threaded (no round/version/'we now'/'corrected' narration; bare date stamp OK), and BOTH-direction honesty.
SPECIFIC CONFIRMATIONS:
- FIX 1: Is (C-form) vs (C-level) cleanly separated, (C-level) tagged a PREMISE (not theorem), and the level-INDEPENDENT fallback (commutation-on-state != tensor product at every finite level, Tsirelson's problem) CORRECT -- so the headline no-go does not rest on (C-level)? Is "Tsirelson's problem / commuting != tensor" cited correctly (Slofstra / MIP*=RE context)?
- FIX 2: Is the "no composite state space => lacks BOTH tensor product (GAP1) AND local tomography (GAP2)" framing correct, with the two NOT over-identified (rebit has tensor product, fails local tomography)? Is "two faces, one origin" honest?
- FIX 3: Is "Tsirelson is a THEOREM via moment-positivity (Gamma>=0, t1)" correct and machine-verified, with the static IC core correctly an INDEPENDENT WITNESS (not the primary source), one operational lever short? Is the Paper IV reconciliation (respected -> inherited, sourced in the new SDP result) faithful to Paper IV sec 7?
- Any NEW overclaim/understatement introduced by the edits? Any internal inconsistency (abstract vs body vs claims sec 7)? Confirm the 5 disavowals (no complex-QT/local-tomography/tensor-product derived; no Q-tilde=Q; no chi_AB pinned; no full IC; Q-tilde external) all still present.
Read companion Papers III ${P3}, IV ${P4} and the plan ${PLAN}.
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
  ['FIX 1 (the (C-form)/(C-level) split + level-independent fallback, secs 2-3). RUN t1. Confirm: (C-form) [moment-positivity] is cleanly separated from (C-level) [the 1+AB cap, now flagged a substrate-modeling PREMISE]; the level-independent no-go (commutation-on-state != tensor product at EVERY finite level, Tsirelson problem) is correct and makes the headline gap independent of (C-level). Is the Tsirelson-problem / commuting-vs-tensor citation accurate? Did the restructure introduce any inconsistency between sec 2, sec 3, the abstract (i), and claim (1)/(2)? Verify the NPA-1 ceiling 2sqrt2 (gap 2.78e-10) + PR-box infeasible still hold.'],
  ['FIX 2 + FIX 3 (the one-name "no composite state space" + Tsirelson anchored to moment-positivity, secs 4-5). RUN t2 + t3. Confirm FIX 2: the records lack BOTH the tensor product (GAP1, closes Q-tilde\\Q) AND local tomography (GAP2, complex-over-real), NOT over-identified as one axiom (rebit has tensor product but fails local tomography, deficit 1); "two faces one origin" honest. Confirm FIX 3: "Tsirelson is a THEOREM via moment-positivity (Gamma>=0 caps CHSH at 2sqrt2, t1)" correct + machine-verified; the static IC core (chain-rule residual 3.63e-122, facet saturating at E=1/sqrt2) correctly demoted to an INDEPENDENT WITNESS one operational lever short; the Paper IV reconciliation (respected->inherited, sourced) faithful. Field-blindness E=E^2=E* over R and C still verified. Any new overclaim from the rewrites?'],
  ['FINAL SWEEP both directions + discipline + faithfulness (secs 1,6,7,8 + whole-paper coherence). Confirm all 5 disavowals present in sec 7 (no complex-QT / local-tomography / tensor-product derived; no Q-tilde=Q; no chi_AB pinned; no full IC; Q-tilde external + now: (C-level) not a theorem). Is the sec 6 "fifth wall" framing now consistent with the "composite state space" missing-input language (not the old "global tensor product" only)? Is "necessary-not-sufficient" still the right strength and the whole paper internally coherent (abstract <-> secs <-> claims) after the edits? Pre-geometric (no composite state space as INPUT), single-threaded (no round/version narration), references resolve (NGHA 2015, NPA, Tsirelson, Pawlowski IC, Hardy, Wootters, CDP, Barandes, Papers I/III/IV). Hunt any remaining or newly-introduced overclaim/inconsistency.'],
].map(([f]) => () => agent(
  `Round-2 CONFIRMING hostile review of v7 Paper VI at ${P6}. Your focus: ${f}\n${RULES}\nReturn the schema (fixes_confirmed = which round-1 fixes you verified as correctly integrated; new_problems_introduced = anything the edits broke).`,
  { label: `P6r2:${f.slice(0, 22)}`, phase: 'Review', schema: SCHEMA }
)))

return { reviews }
