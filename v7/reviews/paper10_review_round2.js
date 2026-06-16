export const meta = {
  name: 'review-v7-paper10-round2-confirming',
  description: 'Round-2 CONFIRMING review of v7 Paper X (graviton spin-2 pricing), verifying the round-1 minor fixes hold and opened no new defect. FIX 1 (major-flagged): leg (a) re-attribution -- the missing propagation direction n-hat is NO LONGER mis-identified with the l_step SCALE wall; it is now the unbuilt EMERGENT METRIC CONTINUUM (a direction is scale-free; Paper IV owns connectivity + hop-metric-up-to-scale, walls the absolute metric as l_step for scale + premature for the continuum), with l_step named only as the scale residue. FIX 2 (major-flagged): the sec2 "without any geometric input" overclaim is DROPPED -- the selection rules are the conserved-stress index structure + conservation hierarchy, witnessed on (not dependent on) an illustrative Euclidean circular embedding (Tier-B), reproducing paper55-A. FIX 3 (minor): the two-wall decomposition is softened to "largely ONE missing structure (the metric continuum + a canonical mode frame) seen through two walls" -- the +/x basis is gauge GIVEN a metric, so leg (b) is a separate input only because the continuum is unbuilt. FIX 4 (minor): the sec2/sec3 two-toy-model bridge added (binary slice = multipole rules; massless-field slice = conserved-symmetric algebra; same record stress, neither model carries both). FIX 5 (minor): sec5 5-static-dof vs 2-polarization conflation tightened (same traceless sector, different counts/objects: static charge vs propagating source). FIX 6 (receipt): p10 (Q-polarization) two hard-coded BLIND booleans DEMOTED from PASS to an [ATTRIBUTION] print; the 5->2 TT counting remains the genuine machine check; sec7 notes the BLIND attribution is an argument not a receipted computation. RUN p10_spin2_pricing.py (now 6 genuine checks). Confirm: the core math intact (tensor fingerprint, conserved-symmetric Weinberg source, 5->2 TT counting); all disavowals present; confirmatory honesty intact; pre-geometric/single-threaded; no new defect from the reframing. Faithfulness to Weinberg / Weinberg-Witten / BHS and Papers III/IV/VII/VIII/IX + v6 49/52/55/57.',
  phases: [{ title: 'Review', detail: '2 referees confirming Paper X fixes' }],
}

const PX = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper10-spin2-carried-helicity2-modeblind.md'
const P4v7 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper4-entanglement-graph-not-metric.md'
const P9v7 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper9-chiral-gap-and-chirality-nogos.md'
const RX = '/Users/felixrobles/workspace/isp/v7/code/p10_spin2_pricing.py'

const RULES = `
Confirm the six round-1 fixes are correctly integrated and opened NO new defect. RUN python3 ${RX} (if numpy/sympy missing use /Users/felixrobles/workspace/isp/code/.venv/bin/python -- now 6 genuine PASS checks, the BLIND booleans demoted). Enforce pre-geometric discipline (a metric direction / mode frame / collar appear ONLY as walled inputs), single-threaded (no 'previously/we now/corrected/round N/version N'; bare date OK), BOTH-direction honesty.
SPECIFIC CONFIRMATIONS:
- FIX 1 (the big one): is the missing propagation direction n-hat now attributed to the EMERGENT METRIC CONTINUUM (NOT the l_step scale wall) in abstract + sec4 leg(a) + sec6 claim(3)? Is the framing faithful to Paper IV (read it: connectivity + hop-metric-up-to-scale owned; absolute metric = l_step no-go for scale + premature for the continuum)? Is l_step correctly named only as the scale RESIDUE, and is "a direction is scale-free" correct?
- FIX 2: is "without any geometric input" GONE from sec2, replaced by "selection rules = index structure + conservation hierarchy, witnessed on an illustrative Euclidean circular embedding (Tier-B), reproducing paper55-A"? No residual claim that the binary numeric demo needs no geometry?
- FIX 3: is the two-wall decomposition softened to "largely ONE missing structure (metric continuum + canonical mode frame) seen through two walls", with the +/x basis gauge-given-a-metric (leg (b) a separate input only because the continuum is unbuilt)?
- FIX 4: is the sec2/sec3 two-toy-model bridge present (binary vs massless-field as illustrative slices of the same record stress, neither carrying both)?
- FIX 5: is sec5's 5-static-dof vs 2-polarization conflation tightened (same traceless sector, different counts: static charge vs propagating source; "is exactly" softened)?
- FIX 6: are the two hard-coded BLIND booleans demoted from PASS to an [ATTRIBUTION] print in p10 (the 5->2 TT counting the genuine check), and does sec7 note the BLIND attribution is an argument not a receipted computation?
- Any NEW defect/inconsistency from the reframing? Confirm intact: the core math (tensor fingerprint sympy-exact, conserved-symmetric Weinberg source on-shell, 5->2 TT counting); the [LEVER] grade (Weinberg external, Weinberg-Witten evasion); all sec6 disavowals (no graviton constructed, no EP derived, no polarizations fixed, NO new no-go); the confirmatory honesty; the headline "spin-2 carried, helicity-2 mode-blind".
Read Paper IV ${P4v7} and Paper IX ${P9v7}.
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
  ['FIX 1 + FIX 2 + FIX 3 (the wall-attribution reframing) -- the substantive fixes. RUN p10. Confirm the missing propagation direction is now the EMERGENT METRIC CONTINUUM (not the l_step scale wall) consistently in abstract + sec4 leg(a) + sec6 claim(3), faithful to Paper IV (connectivity + hop-metric-up-to-scale owned; absolute metric walled), with l_step the scale residue and "a direction is scale-free" correct. Confirm "without any geometric input" is GONE from sec2 (selection rules = index structure + conservation hierarchy on an illustrative Euclidean embedding). Confirm the two-wall decomposition is softened to "largely one missing structure seen through two walls" (+/x gauge given a metric). Any inconsistency introduced between abstract/sec4/sec6 by the reframing?'],
  ['FIX 4 + FIX 5 + FIX 6 + final coherence sweep. RUN p10 (6 genuine checks). Confirm the sec2/sec3 two-toy-model bridge is present; sec5 5-static-vs-2-polarization conflation tightened; the p10 BLIND booleans demoted to an [ATTRIBUTION] print (5->2 counting the genuine check) and sec7 notes the attribution is an argument not a receipted computation. Final: the core math intact (tensor fingerprint, Weinberg conserved-symmetric source on-shell, 5->2 TT counting); the [LEVER] grade + Weinberg-Witten evasion correct; all sec6 disavowals present (no graviton constructed / no EP derived / no polarizations fixed / NO new no-go); confirmatory honesty intact; pre-geometric + single-threaded; references resolve. Headline "spin-2 carried, helicity-2 mode-blind" still supported. Any new or residual overclaim/inconsistency?'],
].map(([f]) => () => agent(
  `Round-2 CONFIRMING hostile review of v7 Paper X at ${PX}. Your focus: ${f}\n${RULES}\nReturn the schema (fixes_confirmed = which round-1 fixes you verified; new_problems_introduced = anything the edits broke).`,
  { label: `P10r2:${f.slice(0, 22)}`, phase: 'Review', schema: SCHEMA }
)))

return { reviews }
