export const meta = {
  name: 'review-v7-paper11-round2-confirming',
  description: 'Round-2 CONFIRMING review of v7 Paper XI verifying the round-1 fixes hold and opened no new defect. FIX 1 (real math error): the Myrheim-Meyer ordering fraction is now the CANONICAL f(d)=Gamma(d+1)Gamma(d/2)/(2 Gamma(3d/2)) -- denominator 2 not 4 -- in the paper sec2 (f(2)=1/2, f(3)=8/35, f(4)=1/10) AND in receipt r2 (mm_fraction fixed, f(4)=1/10 not the false 1/5); r3 docstring stale numbers (f(2)=1/4->1/2, f(3)=8/70->8/35) fixed. FIX 2 (real math error): the Kleitman-Rothschild dominance exponent is now n^2/4 (not the wrong (3/16)n^2) in the paper (abstract/sec4/sec6/sec7) AND receipt r3 (kr_log2_count_leading + the C1 PASS check); verified vs OEIS A001035 log2 P(n)/n^2 -> 1/4. FIX 3: the "sixth appearance" count (contested/inflated) is reframed to "a recurrence of the SAME l_step no-go (behind d, G, c_m, the metric), now on the volume axis" -- no contested ordinal. FIX 4: the absolute volume weight is now "+d (here +2, the 2d demo)" not a flat +2. FIX 5: the conformal result is attributed to "Malament-HKMM" (HKMM 1976 / Malament 1977) not Malament alone. FIX 6: the n-hat=(0.710,-0.705) is reframed -- the order-only content is the dilation-invariance of the link/null relation (bit-identical); the specific vector is a held-out-coordinate SCORE, not an order-only recovery. FIX 7: v6 paper1 "non-discriminating drift" softened to "first symptom consistent with the manifoldlikeness gate (not named as such there)". RUN all 3 receipts r1/r2/r3. Confirm: the load-bearing tiers intact (order->conformal/direction owned-in-principle scale-free; number->volume up to l_step; manifoldlikeness the field-shared gate); no new defect; pre-geometric, single-threaded, honest. Faithfulness to Malament/HKMM/Myrheim-Meyer/Kleitman-Rothschild and v6 paper1.',
  phases: [{ title: 'Review', detail: '2 referees confirming Paper XI fixes' }],
}

const P11 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper11-order-owns-direction-manifoldlikeness-gate.md'
const P1v6 = '/Users/felixrobles/workspace/isp/v6/relativistic-isp-v6-paper1-indivisible-causal-set-gravity.md'
const R1 = '/Users/felixrobles/workspace/isp/v7/code/r1_order_to_conformal_direction.py'
const R2 = '/Users/felixrobles/workspace/isp/v7/code/r2_number_volume_lstep.py'
const R3 = '/Users/felixrobles/workspace/isp/v7/code/r3_manifoldlikeness_myrheim_meyer.py'

const RULES = `
Confirm the seven round-1 fixes are correctly integrated and opened NO new defect. RUN python3 ${R1} , ${R2} , ${R3} (if mpmath/numpy missing use /Users/felixrobles/workspace/isp/code/.venv/bin/python). Enforce pre-geometric discipline (order/count are load-bearing; the sprinkling is a test scaffold scored vs held-out ground truth), single-threaded (no previously/we-now/corrected/round-N; bare date OK), both-direction honesty.
SPECIFIC CONFIRMATIONS:
- FIX 1: is the Myrheim-Meyer formula now CANONICAL (denominator 2, f(2)=1/2, f(3)=8/35, f(4)=1/10) consistently in paper sec2 AND r2 (re-run r2: f(4) prints 0.1, not 0.2) AND r3 docstring (no residual f(2)=1/4 or 8/70)? Independently verify f(4)=1/10 from Gamma(5)Gamma(2)/(2 Gamma(6)) = 24*1/(2*120)=1/10.
- FIX 2: is the KR exponent now n^2/4 (not (3/16)n^2) in the paper (abstract/sec4/sec6/sec7) AND r3 (re-run: n=10000 -> 25,000,000 bits; the C1 PASS check uses n^2/4)? Is the dominance conclusion intact (KR bits >> manifold-data bits)?
- FIX 3: is the contested "sixth appearance" gone, replaced by "recurrence of the same l_step no-go (behind d, G, c_m, the metric), on the volume axis" -- no contested ordinal count anywhere (abstract/sec3/sec5/sec6)?
- FIX 4: is the absolute volume weight now "+d (here +2, the 2d demo)" not a flat +2 (abstract/sec3/sec6)?
- FIX 5: is the conformal result attributed to "Malament-HKMM" (sec2/abstract), matching the reference list?
- FIX 6: is the n-hat vector reframed -- the order-only content is the dilation/boost-invariance of the link relation (bit-identical), the specific (0.710,-0.705) a held-out-coordinate SCORE not an order-only recovery (sec2/sec6)? No residual "recovered n-hat" overclaim?
- FIX 7: is the v6 paper1 "non-discriminating drift" softened to "symptom consistent with the gate (not named as such there)" (sec4/sec5/references), not equated as a proof/naming?
- Any NEW defect/inconsistency from the edits? Confirm the load-bearing tiers intact (Tier I order->conformal/direction owned-in-principle + scale-free; Tier II number->volume up to l_step; Tier III manifoldlikeness field-shared gate, click-law no lever); the 3 new moves (reclassify Paper X direction, name manifoldlikeness, l_step recurrence + G closure); all sec6 disavowals; pre-geometric + single-threaded.
Read v6 paper1 ${P1v6} for the FIX 7 faithfulness check.
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
  ['FIX 1 + FIX 2 (the two real math errors). RUN r2 + r3. Confirm the Myrheim-Meyer formula is now canonical (denominator 2; f(2)=1/2, f(3)=8/35, f(4)=1/10) in the paper sec2 AND r2 (f(4) prints 0.1) AND the r3 docstring (no residual 1/4 / 8/70); independently verify f(4)=Gamma(5)Gamma(2)/(2Gamma(6))=1/10. Confirm the KR exponent is now n^2/4 (not (3/16)n^2) in the paper (abstract/sec4/sec6/sec7) AND r3 (n=10000 -> 25e6 bits; C1 check on n^2/4), matching OEIS A001035 (log2 P(n)/n^2 -> 1/4); the dominance conclusion intact. Any residual wrong-formula anywhere?'],
  ['FIX 3-7 + final coherence. RUN r1. Confirm: (3) no contested "sixth appearance" ordinal -- reframed to "recurrence of the same l_step no-go" (abstract/sec3/sec5/sec6); (4) absolute volume weight "+d (here +2)" not flat +2; (5) "Malament-HKMM" attribution (sec2/abstract); (6) the n-hat (0.710,-0.705) reframed as a held-out-coordinate SCORE, the order-only content being the bit-identical dilation/boost-invariance of the link relation -- no "recovered n-hat" overclaim; (7) v6 paper1 "non-discriminating drift" softened to "symptom consistent with the gate (not named as such there)" -- READ v6 paper1 to confirm the softened reading is faithful. Final: the three tiers + the three new moves + all disavowals intact; pre-geometric (sprinkling = test scaffold); single-threaded; no new defect. Headline "buildable up to l_step given manifoldlikeness; manifoldlikeness the field-shared gate" still supported.'],
].map(([f]) => () => agent(
  `Round-2 CONFIRMING hostile review of v7 Paper XI at ${P11}. Your focus: ${f}\n${RULES}\nReturn the schema (fixes_confirmed = which round-1 fixes you verified; new_problems_introduced = anything the edits broke).`,
  { label: `P11r2:${f.slice(0, 22)}`, phase: 'Review', schema: SCHEMA }
)))

return { reviews }
