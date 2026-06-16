export const meta = {
  name: 'review-v7-paper4-entanglement-graph-not-metric',
  description: 'Hostile review of v7 Paper 4 (entanglement -> graph not metric), round 3 (CONFIRMING): verify the round-2 fixes -- (1) CRITICAL now fixed: chi_AB = I_sigma (signed) is "zero WHEN factorized" = NECESSARY-NOT-SUFFICIENT, NOT "zero iff factorized" (it can cancel at a correlated kernel; p4a now exhibits I_sigma=0 at factorization-defect 0.09, check); only the NON-NEGATIVE E_cl is zero-iff-factorized; {factorized} subset {I_sigma=0}; (2) the positive geometry claim is now scoped to "the connectivity graphs HOP-METRIC up to one overall scale" (unweighted integer shortest-path; ratios l_step-invariant) -- NOT "full relative/similarity geometry" (no continuous metric, no curvature, no conformal class); p4b prose/banner now matches; (3) p4a 24 checks (counterexample added). RUN all 4 receipts. Confirm the half-open thesis (forced-skeleton-free-complement; connectivity+hop-metric YES / absolute metric NO = Newton-G no-go) reads clean end-to-end; faithfulness, pre-geom, high precision, single-threaded, overclaim BOTH directions.',
  phases: [{ title: 'Review', detail: '3 referees on Paper 4' }],
}

const P4 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper4-entanglement-graph-not-metric.md'
const P1 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper1-record-click-law.md'
const P3 = '/Users/felixrobles/workspace/isp/v7/relativistic-isp-v7-paper3-seal-spacing-no-go.md'
const PLAN = '/Users/felixrobles/workspace/isp/v7/LONG_MARCH_PLAN.md'
const P21 = '/Users/felixrobles/workspace/isp/v1/relativistic-isp-v1-paper21-entanglement-indivisible.md'
const P14 = '/Users/felixrobles/workspace/isp/v5/relativistic-isp-v5-paper14-non-markovianity-and-bell-nonlocality.md'
const RA = '/Users/felixrobles/workspace/isp/v7/code/p4a_joint_clicklaw.py'
const RC = '/Users/felixrobles/workspace/isp/v7/code/nonadditive_entangling_complement.py'
const RF = '/Users/felixrobles/workspace/isp/v7/code/f5_oi_pi_consistency.py'
const RB = '/Users/felixrobles/workspace/isp/v7/code/p4b_connectivity_metric_split.py'

const RULES = `
STANDING RULES to enforce:
- PRE-GEOMETRIC DISCIPLINE: every quantity must be a record-internal probability/KL/log-likelihood number; NO spacetime/metric/light-cone/s^2/Lorentz used as INPUT. The metric/RT/wormhole appear ONLY as the things that CANNOT be derived (the no-go). FLAG any geometry smuggled in as a derivation input (esp. a Hilbert/tensor arena re-imported as the 'pre-geometric' stage, or an already-spatial lattice presupposed).
- HIGH PRECISION: every numeric claim reproducible at mpmath dps>=100 / sympy-exact. RUN all four receipts: python3 ${RA} , ${RC} , ${RF} , ${RB} (if mpmath/sympy missing use /Users/felixrobles/workspace/isp/code/.venv/bin/python), plus your own checks. Re-derive: sigma_AB=sigma_A+sigma_B+I_sigma (product I_sigma=0, correlated !=0); the sequential telescope blind to I_sigma; S_AB/(S_A S_B)=exp(-kappa I_sigma); E_cl(Bell)=ln2, E_cl(product)=0; chi weight-0 vs distance weight+1; the pinch I=0=>no edge; the conformal-class scale-invariance.
- SINGLE-THREADED: reads written-once. FLAG 'previously/we now/earlier version/corrected/round N/campaign/version N' (a bare date stamp is allowed).
- HONESTY / OVERCLAIM HUNT (BOTH directions):
  (a) MANUFACTURED GEOMETRY: the paper must NOT claim an emergent absolute METRIC, the RT area-COEFFICIENT 1/4G, or an ER=EPR wormhole LENGTH (all weight+1, no-go-blocked). Must NOT claim the entangling profile chi_AB is FORCED (it is a FREE Tier-A input). Must NOT claim full bulk-emergence (premature). CHECK these are all correctly disavowed.
  (b) UNDER-STATEMENT: the paper must correctly credit what entanglement DOES source -- connectivity (pinch-off) + the conformal class (weight-0), and the joint-law SHAPE forcing + the OI-permission (the real positive results). Is 'half-open' right, or is even connectivity overstated/understated?
  (c) THE GATE FAITHFULNESS: is 'forced-skeleton-free-complement' faithful to the receipts -- is the exp shape genuinely forced on the joint scalar arg, is the additivity genuinely NOT forced (sequential refinement blind to the mutual term), is chi_AB genuinely free (continuum at fixed marginals, two-sided), and is the OI-violation genuinely PERMITTED by (not forced by, not forbidden by) the skeleton? Is E_cl=chi_AB=I_sigma the same object (faithful to v1 paper21)?
  (d) THE WEIGHT-SPLIT: is chi genuinely weight-0 and a metric genuinely weight+1, and does the Paper 3 trichotomy genuinely block the metric (the SAME l_step wall as G)? FLAG any gap in 'metric = the Newton-G no-go again'.
  (e) THE CIRCULARITY AUDIT: is the diagnosis honest (existing 'geometry from entanglement' runs Jacobson-direction; the 'score-vs-true-coordinates' trap named)? Is the weight no-go correctly used as the anti-circularity criterion?
- FAITHFULNESS to the sources (v1 paper21 E_cl, v5 paper14 Bell address, Paper 1 the forced single-chain law, Paper 3 the grading no-go). Read them.
`

const SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['focus', 'verdict', 'must_fix', 'overclaims', 'math_or_claim_errors', 'pre_geometric_violations', 'single_threaded_violations', 'new_paths_opened', 'summary'],
  properties: {
    focus: { type: 'string' },
    verdict: { type: 'string', enum: ['accept', 'minor-revision', 'major-revision', 'reject'] },
    must_fix: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['issue', 'where', 'severity', 'fix'], properties: { issue: { type: 'string' }, where: { type: 'string' }, severity: { type: 'string', enum: ['minor', 'major', 'critical'] }, fix: { type: 'string' } } } },
    overclaims: { type: 'array', items: { type: 'string' } },
    math_or_claim_errors: { type: 'array', items: { type: 'string' } },
    pre_geometric_violations: { type: 'array', items: { type: 'string' } },
    single_threaded_violations: { type: 'array', items: { type: 'string' } },
    new_paths_opened: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
}

phase('Review')
const reviews = await parallel([
  ['THE JOINT CLICK-LAW (sec 3) -- the gate result. Is "forced-skeleton-free-complement" faithful? RUN p4a/complement/f5. Re-derive: the joint odometer split sigma_AB=sigma_A+sigma_B+I_sigma; the sequential telescope being BLIND to I_sigma (telescope gap 0 WHILE I_sigma!=0) -- is this genuinely "additivity not forced", or is there a hidden assumption? Is the exp SHAPE genuinely forced on the joint scalar arg (Cauchy, p=1)? Is chi_AB=I_sigma=E_cl genuinely the SAME object and genuinely FREE (continuum at fixed marginals, two-sided sign)? Is S_AB/(S_A S_B)=exp(-kappa chi_AB) exact? Verify E_cl(Bell)=ln2 (v1 paper21). Is the upgrade of Paper 1 5.2 from [OPEN] to "shape forced/content free" honest, or an overclaim?'],
  ['THE OI/PI CONSISTENCY + WEIGHT-SPLIT (secs 3 end, 4-5). Does the forced multiplicative skeleton genuinely PERMIT (not force, not forbid) OI-violation? RUN f5: is survival-multiplicativity really ORTHOGONAL to outcome-factorization, and is the CHSH=2sqrt2/no-signaling/PI-yes/OI-no joint law genuinely on the forced skeleton (PR-box excluded)? Faithful to v5 paper14? Then the WEIGHT-SPLIT (p4b): is chi genuinely weight-0 (gauge-invariant) and a graph distance genuinely weight+1, and does the Paper 3 grading trichotomy genuinely BLOCK the metric (= the same l_step/Newton-G wall)? Is the pinch-off (I=0=>no edge) and the conformal-class-scale-free claim correct? Is "half-open: connectivity yes / metric no" exactly right -- not over- (manufacturing geometry) or under-stating (denying the conformal class)?'],
  ['OVERCLAIM HUNT BOTH directions + circularity + discipline (secs 1,2,6,7). (a) Does the paper AVOID claiming an absolute metric / RT-coefficient / ER=EPR length / forced chi_AB / full bulk-emergence? Confirm each is disavowed in sec 7. (b) Does it correctly CREDIT what entanglement sources (connectivity+conformal class+the gate result) without under-stating? (c) THE CIRCULARITY AUDIT (sec 6): is the Jacobson-direction diagnosis honest, is the "score-vs-true-coordinates" trap correctly named, and is the weight no-go correctly the anti-circularity criterion? (d) pre-geometric discipline (no metric/Hilbert-arena smuggled as input); single-threaded; references resolve (v1 p21, v5 p5/p14, Papers I/III/V). Hunt any remaining overclaim or unfaithful citation.'],
].map(([f]) => () => agent(
  `Hostile, high-precision review of v7 Paper 4 (entanglement -> graph not metric) at ${P4}. Your focus: ${f}\nRead the paper, the plan ${PLAN}, Paper I ${P1}, Paper III ${P3}, and the sources v1 paper21 ${P21}, v5 paper14 ${P14}. Run the receipts ${RA} , ${RC} , ${RF} , ${RB} + your own sympy/mpmath. ${RULES}\nReturn the schema.`,
  { label: `P4:${f.slice(0, 26)}`, phase: 'Review', schema: SCHEMA }
)))

return { reviews }
